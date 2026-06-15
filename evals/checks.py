#!/usr/bin/env python3
"""Phase-scoped deterministic eval harness for the EA knowledge base.

Usage:
  python evals/checks.py --phase {steward|author|weave|research|all} [--domain NAME]
  python evals/checks.py --phase all --update-baseline   # refresh regression baseline

Exit code is non-zero if any FAIL-severity finding is produced (WARN does not
fail). Writes evals/report.json and evals/REPORT.md.

No third-party dependencies (standard library only) so it runs in CI unchanged.
"""
import argparse, json, os, re, sys, glob, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "glossary", "_canonical-names.md")
VERBS = ["depends_on","derived_from","supersedes","defined_in","related_to","causes","mentions"]
VERB_PROSE = ["depends on","derived from","supersedes","supersede","defined in","related to","causes","cause","mentions","mention","depends_on","derived_from","defined_in","related_to"]
PRONOUNS = re.compile(r"\b(it|its|it's|they|them|their|this|that|these|those|he|she|his|her)\b", re.I)

findings = []  # (severity, phase, path, message)
def add(sev, phase, path, msg): findings.append((sev, phase, path, msg))

def kebab(name):
    s = name.strip().lower().replace("&","and").replace("/","-")
    s = re.sub(r"[^a-z0-9 -]","",s); s = re.sub(r"\s+","-",s); s = re.sub(r"-+","-",s)
    return s.strip("-")

# ---------------- registry parsing ----------------
def parse_registry():
    if not os.path.exists(REG):
        add("FAIL","steward",REG,"registry file missing"); return None
    lines = open(REG, encoding="utf-8").read().splitlines()
    sec=None; data={"domains":[],"caps":[],"proc":[],"tech":[],"legacy":[],"modern":[],"gloss":[]}
    keymap={"Domains (value streams & technology domains)":"domains",
            "Business capabilities":"caps","Business processes":"proc",
            "Technology capabilities":"tech","Legacy systems":"legacy",
            "Modern systems":"modern","Glossary terms":"gloss"}
    for ln in lines:
        if ln.startswith("## "): sec=keymap.get(ln[3:].strip()); continue
        if not sec or not ln.strip().startswith("|"): continue
        cells=[c.strip() for c in ln.strip().strip("|").split("|")]
        if not cells or cells[0] in ("Canonical Name","") or set(cells[0])<=set("-: "): continue
        data[sec].append(cells)
    return data

# ---------------- helpers ----------------
def body_of(text):
    if text.startswith("---"):
        m=re.match(r"^---.*?\n---\n", text, re.S)
        if m: return text[m.end():]
    return text

def frontmatter(text):
    fm={}
    if text.startswith("---"):
        m=re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if m:
            for ln in m.group(1).splitlines():
                mm=re.match(r"^(\w+):\s*(.*)$", ln)
                if mm: fm[mm.group(1)]=mm.group(2).strip()
    return fm

def all_concept_files():
    out=[]
    for d in ["domains","business-capabilities","business-processes","technology-capabilities",
              "systems/legacy","systems/modern","glossary"]:
        for f in glob.glob(os.path.join(ROOT,d,"*.md")):
            if os.path.basename(f).startswith("_"): continue
            out.append(f)
    for f in glob.glob(os.path.join(ROOT,"process-flows","**","*.md"), recursive=True):
        if os.path.basename(f).startswith("_"): continue
        out.append(f)
    return out

def names_set(data):
    s=set()
    for k in ("domains","caps","proc","tech","legacy","modern","gloss"):
        for row in data[k]: s.add(row[0])
    return s

# ---------------- PHASE: steward (registry integrity) ----------------
def check_steward(data):
    seen={}
    for k in ("domains","caps","proc","tech","legacy","modern","gloss"):
        for row in data[k]:
            n=row[0]
            if n in seen: add("FAIL","steward",REG,f"duplicate canonical name '{n}' (in {seen[n]} and {k})")
            else: seen[n]=k
    names=set(seen)
    # alias collisions: alias equal to a different concept's canonical name
    def aliases(row, idx):
        return [a.strip() for a in row[idx].split(",")] if len(row)>idx and row[idx] not in ("","—") else []
    alias_idx={"domains":2,"caps":4,"proc":3,"tech":3,"legacy":3,"gloss":1}
    for k,idx in alias_idx.items():
        for row in data[k]:
            for a in aliases(row,idx):
                if a in names and a!=row[0]:
                    add("FAIL","steward",REG,f"alias '{a}' of '{row[0]}' collides with canonical name '{a}'")
    # capability parent + level monotonicity + domain exists
    domset={r[0] for r in data["domains"]}
    lvlnum={"L1":1,"L2":2,"L3":3,"L4":4}
    capby={r[0]:r for r in data["caps"]}
    for r in data["caps"]:
        name,lvl,dom,parent=r[0],r[1],r[2],r[3]
        if dom not in domset: add("FAIL","steward",REG,f"capability '{name}' defined_in unknown domain '{dom}'")
        if parent not in ("","—"):
            if parent not in capby: add("FAIL","steward",REG,f"capability '{name}' parent '{parent}' not in registry")
            else:
                pl=capby[parent][1]
                if lvlnum.get(lvl,0)!=lvlnum.get(pl,0)+1:
                    add("FAIL","steward",REG,f"capability '{name}' ({lvl}) parent '{parent}' ({pl}) breaks level monotonicity")
        elif lvl!="L1":
            add("FAIL","steward",REG,f"capability '{name}' is {lvl} but has no parent")
    # systems realize/supersede targets
    techset={r[0] for r in data["tech"]}; legset={r[0] for r in data["legacy"]}
    for r in data["legacy"]:
        if r[1] not in techset: add("FAIL","steward",REG,f"legacy '{r[0]}' realizes unknown tech capability '{r[1]}'")
    superseded=set()
    for r in data["modern"]:
        if r[1] not in techset: add("FAIL","steward",REG,f"modern '{r[0]}' realizes unknown tech capability '{r[1]}'")
        for s in r[2].split(";"):
            s=s.strip()
            if s and s not in legset: add("FAIL","steward",REG,f"modern '{r[0]}' supersedes unknown legacy '{s}'")
            superseded.add(s)
    for r in data["legacy"]:
        if r[0] not in superseded: add("WARN","steward",REG,f"legacy '{r[0]}' has no modern successor")
    # kebab/folder collision
    folder={"domains":"domains","proc":"business-processes","tech":"technology-capabilities",
            "legacy":"systems/legacy","modern":"systems/modern","gloss":"glossary"}
    seenpath={}
    for k,fold in folder.items():
        for r in data[k]:
            p=f"{fold}/{kebab(r[0])}.md"
            if p in seenpath: add("FAIL","steward",REG,f"path collision {p}: '{r[0]}' vs '{seenpath[p]}'")
            seenpath[p]=r[0]

# ---------------- PHASE: author (per concept file) ----------------
def check_author(data):
    names=names_set(data)
    sorted_names=sorted(names,key=len,reverse=True)
    # parity expected vs actual
    expected=set()
    expected|={f"domains/{kebab(r[0])}.md" for r in data["domains"]}
    expected|={f"business-capabilities/{r[1]}-{kebab(r[0])}.md" for r in data["caps"]}
    expected|={f"business-processes/{kebab(r[0])}.md" for r in data["proc"]}
    expected|={f"technology-capabilities/{kebab(r[0])}.md" for r in data["tech"]}
    expected|={f"systems/legacy/{kebab(r[0])}.md" for r in data["legacy"]}
    expected|={f"systems/modern/{kebab(r[0])}.md" for r in data["modern"]}
    expected|={f"glossary/{kebab(r[0])}.md" for r in data["gloss"]}
    actual={os.path.relpath(f,ROOT) for f in all_concept_files()
            if not os.path.relpath(f,ROOT).startswith("process-flows")}
    for m in sorted(expected-actual): add("FAIL","author",m,"registry concept missing its file")
    for e in sorted(actual-expected): add("FAIL","author",e,"file not registered in canonical-names registry")
    # per-file
    for f in all_concept_files():
        rel=os.path.relpath(f,ROOT)
        txt=open(f, encoding="utf-8").read()
        size=os.path.getsize(f)
        if size>6144: add("WARN","author",rel,f"file is {size} bytes (>6 KB)")
        fm=frontmatter(txt); body=body_of(txt)
        m=re.search(r"^#\s+(.+)$", body, re.M)
        h1=m.group(1).strip() if m else None
        if not h1: add("FAIL","author",rel,"missing H1"); continue
        title=fm.get("title","").strip().strip('"')
        if title and title!=h1: add("WARN","author",rel,f"frontmatter title '{title}' != H1 '{h1}'")
        # relationships present + position
        idx=body.find("## Relationships")
        if idx<0: add("FAIL","author",rel,"missing '## Relationships'"); continue
        if idx>1800: add("FAIL","author",rel,f"'## Relationships' at {idx} chars (>1800)")
        # definition starts with canonical name
        dm=re.search(r"\*\*Definition\.\*\*\s+(.+)", body)
        if dm:
            if h1 and not dm.group(1).lstrip().startswith(h1):
                add("WARN","author",rel,"definition does not start with the canonical name")
        else:
            add("WARN","author",rel,"no '**Definition.**' line")
        if "Also known as" not in body: add("WARN","author",rel,"no 'Also known as' line")
        # relationship bullets
        after=body[idx+len("## Relationships"):]
        nxt=after.find("\n## "); block=after if nxt<0 else after[:nxt]
        nrel=0
        for bl in block.splitlines():
            bl=bl.strip()
            if not bl.startswith("-"): continue
            # locate the earliest relationship verb phrase
            pos=-1; vfound=None
            for v in VERB_PROSE:
                i=bl.find(" "+v+" ")
                if i>=0 and (pos<0 or i<pos): pos=i; vfound=v
            if vfound is None:
                add("WARN","author",rel,f"relationship bullet has no known verb: {bl[:70]}"); continue
            nrel+=1
            obj=bl[pos+len(vfound)+2:]   # text after the verb = the relationship object
            if not any(nm in obj for nm in sorted_names):
                add("FAIL","author",rel,f"relationship object is not a registry name: {bl[:80]}")
            if PRONOUNS.search(re.sub(r"^- ","",bl)):
                add("WARN","author",rel,f"possible pronoun in relationship: {bl[:70]}")
        if nrel==0: add("FAIL","author",rel,"no usable relationship bullets")
        # system notes need sources
        typ=fm.get("type","")
        if typ in ("legacy-system","modern-system"):
            if not fm.get("sources") or fm.get("sources") in ("[]","",'""'):
                add("WARN","author",rel,"system note has empty 'sources' frontmatter")
            if "## References" not in body or "http" not in body.split("## References")[-1]:
                add("WARN","author",rel,"system note missing a reference link")

# ---------------- PHASE: weave (indexes, maps, flows, links) ----------------
def check_weave(data):
    # index coverage
    for fold in ["domains","business-capabilities","business-processes","technology-capabilities",
                 "systems/legacy","systems/modern"]:
        idx=os.path.join(ROOT,fold,"_index.md")
        if not os.path.exists(idx): add("FAIL","weave",f"{fold}/_index.md","index missing"); continue
        links=set(re.findall(r"\[\[([^\]|]+)", open(idx,encoding="utf-8").read()))
        files={os.path.basename(p)[:-3] for p in glob.glob(os.path.join(ROOT,fold,"*.md"))
               if not os.path.basename(p).startswith("_")}
        for miss in sorted(files-links): add("FAIL","weave",f"{fold}/_index.md",f"file not linked: {miss}")
    # maps reference only registry names (loose) + legacy coverage
    names=names_set(data)
    for mp in ["maps/capability-to-tech.md","maps/current-to-future-state.md"]:
        p=os.path.join(ROOT,mp)
        if not os.path.exists(p): add("FAIL","weave",mp,"map missing")
    # dangling wikilinks across repo
    all_bases={os.path.basename(p)[:-3] for p in glob.glob(os.path.join(ROOT,"**","*.md"),recursive=True)}
    for f in all_concept_files()+glob.glob(os.path.join(ROOT,"**","_index.md"),recursive=True):
        rel=os.path.relpath(f,ROOT)
        for tgt in re.findall(r"\[\[([^\]|]+)", open(f,encoding="utf-8").read()):
            if tgt not in all_bases: add("WARN","weave",rel,f"dangling wikilink [[{tgt}]]")
    # process-flow step chains (only if present)
    for d in glob.glob(os.path.join(ROOT,"process-flows","*")):
        if not os.path.isdir(d): continue
        steps=sorted(os.path.basename(p) for p in glob.glob(os.path.join(d,"*.md"))
                     if re.match(r"\d{2}-",os.path.basename(p)))
        nums=[int(s[:2]) for s in steps]
        if nums and nums!=list(range(1,len(nums)+1)):
            add("FAIL","weave",os.path.relpath(d,ROOT),f"step numbering not contiguous: {nums}")
        for i,s in enumerate(steps):
            txt=open(os.path.join(d,s),encoding="utf-8").read()
            if i<len(steps)-1 and "causes" not in txt and "cause" not in txt:
                add("WARN","weave",os.path.relpath(os.path.join(d,s),ROOT),"non-terminal step has no 'causes' edge")
    # bidirectional coverage metric (report only)
    dep=0; inv=0
    for f in all_concept_files():
        t=open(f,encoding="utf-8").read()
        dep+=len(re.findall(r"depends on", t))
    add("INFO","weave","-",f"depends_on edges counted: {dep}")

# ---------------- PHASE: research (proposed staging files) ----------------
def check_research(data):
    names=names_set(data)
    props=glob.glob(os.path.join(ROOT,"_status","proposed-*.md"))
    if not props: add("INFO","research","-","no _status/proposed-*.md staging files present"); return
    for p in props:
        rel=os.path.relpath(p,ROOT); txt=open(p,encoding="utf-8").read()
        if "http" not in txt: add("WARN","research",rel,"no source URLs found in research staging file")

# ---------------- regression baseline ----------------
def snapshot(data):
    snap={k:len(data[k]) for k in data}
    edges={v:0 for v in VERBS}
    for f in all_concept_files():
        t=open(f,encoding="utf-8").read()
        edges["depends_on"]+=len(re.findall(r"depends on",t))
        edges["derived_from"]+=len(re.findall(r"derived from",t))
        edges["supersedes"]+=len(re.findall(r"supersede",t))
        edges["defined_in"]+=len(re.findall(r"defined in",t))
        edges["related_to"]+=len(re.findall(r"related to",t))
        edges["causes"]+=len(re.findall(r"\bcause",t))
        edges["mentions"]+=len(re.findall(r"\bmention",t))
    snap["files"]=len(all_concept_files()); snap["edges"]=edges
    return snap

def check_regression(data):
    bpath=os.path.join(ROOT,"evals","baseline.json")
    cur=snapshot(data)
    if not os.path.exists(bpath):
        add("INFO","all",bpath,"no baseline yet (run --update-baseline to create)"); return cur
    base=json.load(open(bpath))
    for k in ("domains","caps","proc","tech","legacy","modern","gloss","files"):
        if cur.get(k,0)<base.get(k,0):
            add("FAIL","all","baseline",f"regression: {k} dropped {base[k]} -> {cur[k]}")
    for v in VERBS:
        if cur["edges"][v]<base.get("edges",{}).get(v,0):
            add("WARN","all","baseline",f"edge regression: {v} {base['edges'][v]} -> {cur['edges'][v]}")
    return cur

# ---------------- main ----------------
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--phase",choices=["steward","author","weave","research","all"],default="all")
    ap.add_argument("--domain",default=None)
    ap.add_argument("--update-baseline",action="store_true")
    args=ap.parse_args()
    data=parse_registry()
    if data is None: _emit(); sys.exit(1)
    ph=args.phase
    if ph in ("steward","all"): check_steward(data)
    if ph in ("author","all"): check_author(data)
    if ph in ("weave","all"): check_weave(data)
    if ph in ("research","all"): check_research(data)
    cur=None
    if ph=="all": cur=check_regression(data)
    if args.update_baseline:
        cur=snapshot(data)
        json.dump(cur,open(os.path.join(ROOT,"evals","baseline.json"),"w"),indent=2)
        print("baseline updated")
    _emit(args)
    sys.exit(1 if any(s=="FAIL" for s,_,_,_ in findings) else 0)

def _emit(args=None):
    counts={s:sum(1 for f in findings if f[0]==s) for s in ("FAIL","WARN","INFO")}
    report={"generated":datetime.datetime.utcnow().isoformat()+"Z",
            "phase":getattr(args,"phase","all") if args else "all",
            "counts":counts,
            "findings":[{"severity":s,"phase":p,"path":pa,"message":m} for s,p,pa,m in findings]}
    os.makedirs(os.path.join(ROOT,"evals"),exist_ok=True)
    json.dump(report,open(os.path.join(ROOT,"evals","report.json"),"w"),indent=2)
    md=[f"# Eval Report","",f"Generated: {report['generated']}  ",
        f"Phase: `{report['phase']}`  ",
        f"**FAIL: {counts['FAIL']}  WARN: {counts['WARN']}  INFO: {counts['INFO']}**","",
        "| Severity | Phase | Path | Message |","|---|---|---|---|"]
    order={"FAIL":0,"WARN":1,"INFO":2}
    for s,p,pa,m in sorted(findings,key=lambda x:order[x[0]]):
        md.append(f"| {s} | {p} | {pa} | {m} |")
    open(os.path.join(ROOT,"evals","REPORT.md"),"w").write("\n".join(md)+"\n")
    print(f"FAIL={counts['FAIL']} WARN={counts['WARN']} INFO={counts['INFO']} -> evals/REPORT.md")

if __name__=="__main__":
    main()
