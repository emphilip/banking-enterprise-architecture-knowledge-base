#!/usr/bin/env python3
"""Relationship-weaver: regenerate all _index.md Maps-of-Content and the two maps
from the registry + the actual note files. Idempotent. Run from repo root:
    python tools/weave.py
"""
import os, re, glob
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG=os.path.join(ROOT,"glossary","_canonical-names.md")

def kebab(n):
    s=n.strip().lower().replace("&","and").replace("/","-")
    s=re.sub(r"[^a-z0-9 -]","",s); s=re.sub(r"\s+","-",s); return re.sub(r"-+","-",s).strip("-")
def read(p): return open(p,encoding="utf-8").read()
def title_of(p):
    t=read(p); m=re.search(r'^title:\s*(.+)$',t,re.M)
    if m: return m.group(1).strip().strip('"')
    m=re.search(r'^#\s+(.+)$',t,re.M); return m.group(1).strip() if m else os.path.basename(p)[:-3]
def fm_field(p,f):
    t=read(p); m=re.search(rf'^{f}:\s*(.+)$',t,re.M); return m.group(1).strip().strip('"') if m else ""
def base(p): return os.path.basename(p)[:-3]
def files(folder): return [f for f in glob.glob(os.path.join(ROOT,folder,"*.md")) if not os.path.basename(f).startswith("_")]

def write_index(folder,title,intro,groups):
    out=[f"---\nid: {folder.replace('/','-')}-index\ntitle: {title}\ntype: index\nstatus: draft\n---\n",
         f"# {title}\n",intro+"\n"]
    for gname,items in groups:
        if not items: continue
        if gname: out.append(f"## {gname}\n")
        for t,b in sorted(items): out.append(f"- [[{b}|{t}]]")
        out.append("")
    open(os.path.join(ROOT,folder,"_index.md"),"w").write("\n".join(out))
    print("index:",folder)

# ---- registry parse (sections we map) ----
lines=read(REG).splitlines(); sec=None
reg={"tech":[],"legacy":[],"modern":[]}
keymap={"Technology capabilities":"tech","Legacy systems":"legacy","Modern systems":"modern"}
for ln in lines:
    if ln.startswith("## "): sec=keymap.get(ln[3:].strip()); continue
    if not sec or not ln.strip().startswith("|"): continue
    c=[x.strip() for x in ln.strip().strip("|").split("|")]
    if c[0] in("Canonical Name","") or set(c[0])<=set("-: "): continue
    reg[sec].append(c)

# ---- indexes ----
write_index("domains","Domains Index",
    "Map-of-Content for all value-stream and technology domains.",
    [("",[(title_of(f),base(f)) for f in files("domains")])])

caps=[(title_of(f),base(f)) for f in files("business-capabilities")]
def lvl(b):
    m=re.match(r"(L\d)-",b); return m.group(1) if m else "L?"
write_index("business-capabilities","Business Capabilities Index",
    "Map-of-Content for the L1->L2->L3->L4 capability map (BIAN / APQC). Children are derived_from their parent; each capability is defined_in a domain.",
    [(f"{L} Capabilities",[x for x in caps if lvl(x[1])==L]) for L in ("L1","L2","L3","L4")])

procs=[]; subs=[]
for f in files("business-processes"):
    (subs if fm_field(f,"type")=="business-process" and "level: sub-process" in read(f) else procs).append((title_of(f),base(f)))
# simpler: classify by presence of 'derived from' a process is hard; treat all as processes list + sub-processes via frontmatter type marker
allbp=[(title_of(f),base(f),read(f)) for f in files("business-processes")]
procs=[(t,b) for t,b,c in allbp if "level: sub-process" not in c]
subs=[(t,b) for t,b,c in allbp if "level: sub-process" in c]
write_index("business-processes","Business Processes Index",
    "Map-of-Content for processes and their sub-processes. Processes are defined_in a domain; sub-processes are derived_from a process. Step-level flows live in process-flows/.",
    [("Processes",procs),("Sub-Processes",subs)])

tc=[]
for f in files("technology-capabilities"):
    tc.append((fm_field(f,"domain") or "Other",title_of(f),base(f)))
tdoms=sorted(set(d for d,_,_ in tc))
write_index("technology-capabilities","Technology Capabilities Index",
    "Map-of-Content for technology capabilities and their L2/L3 sub-capabilities, grouped by technology domain.",
    [(d,[(t,b) for dd,t,b in tc if dd==d]) for d in tdoms])

write_index("systems/legacy","Legacy Systems Index",
    "Map-of-Content for current-state / incumbent systems. Each realizes a technology capability and is superseded by a modern system.",
    [("",[(title_of(f),base(f)) for f in files("systems/legacy")])])
write_index("systems/modern","Modern Systems Index",
    "Map-of-Content for modern / cloud-native / AI systems. Each realizes a technology capability and supersedes a legacy system.",
    [("",[(title_of(f),base(f)) for f in files("systems/modern")])])

# concepts grouped by type
if os.path.isdir(os.path.join(ROOT,"concepts")):
    ct=[(fm_field(f,"type") or "concept",title_of(f),base(f)) for f in files("concepts")]
    write_index("concepts","Supporting Concepts Index",
        "Map-of-Content for roles, business events, and artifacts referenced by the process flows.",
        [(g.capitalize()+"s",[(t,b) for tt,t,b in ct if tt==g]) for g in ("role","event","artifact")])

# glossary index
gl=[(title_of(f),base(f)) for f in files("glossary") if base(f)!="_canonical-names"]
out=["---\nid: glossary-index\ntitle: Glossary Index\ntype: index\nstatus: draft\n---\n","# Glossary Index\n",
     "Map-of-Content for glossary terms and the canonical-names registry.\n",
     "## Registry","- [[_canonical-names|Canonical Names Registry]]","","## Terms"]
for t,b in sorted(gl): out.append(f"- [[{b}|{t}]]")
open(os.path.join(ROOT,"glossary","_index.md"),"w").write("\n".join(out)+"\n"); print("index: glossary")

# process-flows index (per flow, ordered steps)
pfroot=os.path.join(ROOT,"process-flows")
if os.path.isdir(pfroot):
    out=["---\nid: process-flows-index\ntitle: Process Flows Index\ntype: index\nstatus: draft\n---\n",
         "# Process Flows Index\n",
         "Map-of-Content for step-level process flows. Steps are ordered; each step causes the next and depends_on the capability/technology it consumes.\n"]
    for d in sorted(glob.glob(os.path.join(pfroot,"*"))):
        if not os.path.isdir(d): continue
        steps=sorted(glob.glob(os.path.join(d,"*.md")),key=lambda p:os.path.basename(p))
        steps=[s for s in steps if re.match(r"\d{2}-",os.path.basename(s))]
        if not steps: continue
        out.append(f"## {os.path.basename(d).replace('-',' ').title()}\n")
        for s in steps: out.append(f"- [[{base(s)}|{title_of(s)}]]")
        out.append("")
    open(os.path.join(pfroot,"_index.md"),"w").write("\n".join(out)); print("index: process-flows")

# ---- maps ----
technames={c[0] for c in reg["tech"]}
# add tech sub-capabilities from technology-capabilities files
for f in files("technology-capabilities"): technames.add(title_of(f))
# capability-to-tech: scan business caps + processes + steps for depends_on a tech name
edges={}
scan=files("business-capabilities")+files("business-processes")+glob.glob(os.path.join(ROOT,"process-flows","**","*.md"),recursive=True)
tn_sorted=sorted(technames,key=len,reverse=True)
for f in scan:
    t=read(f); m=re.search(r'^#\s+(.+)$',t,re.M)
    if not m: continue
    subj=m.group(1).strip()
    body=t.split("## Relationships",1)[-1].split("\n## ",1)[0]
    for bl in body.splitlines():
        if "depends on" not in bl: continue
        obj=bl.split("depends on",1)[1]
        for tn in tn_sorted:
            if tn in obj: edges.setdefault(subj,set()).add(tn); break
m=["---\nid: capability-to-tech\ntitle: Capability to Technology Map\ntype: map\nstatus: draft\n---\n",
   "# Capability to Technology Map\n",
   "Each business capability / process / step and the technology capabilities it depends_on (scanned from note relationships).\n",
   "## Dependency statements\n"]
for subj in sorted(edges):
    for tn in sorted(edges[subj]): m.append(f"- {subj} depends on the {tn} capability.")
m.append("\n## Matrix\n| Business concept | Depends on technology capability |\n|---|---|")
for subj in sorted(edges): m.append(f"| {subj} | {', '.join(sorted(edges[subj]))} |")
m.append("")
open(os.path.join(ROOT,"maps","capability-to-tech.md"),"w").write("\n".join(m)); print("map: capability-to-tech")

# current-to-future-state
mm=["---\nid: current-to-future-state\ntitle: Current to Future State Map\ntype: map\nstatus: draft\n---\n",
    "# Current to Future State Map\n",
    "Each legacy / current-state system and the modern system(s) that supersede it for the same technology capability.\n",
    "## Successor statements\n"]
rows=[]
for c in reg["modern"]:
    for sup in [s.strip() for s in c[2].split(";") if s.strip()]:
        mm.append(f"- {c[0]} supersedes {sup}."); rows.append((c[1],sup,c[0]))
mm.append("\n## Realization statements\n")
for c in reg["legacy"]: mm.append(f"- {c[1]} depends on {c[0]}.")
for c in reg["modern"]: mm.append(f"- {c[1]} depends on {c[0]}.")
mm.append("\n## Successor matrix\n| Technology Capability | Legacy System | Modern Successor |\n|---|---|---|")
for r in sorted(rows): mm.append(f"| {r[0]} | {r[1]} | {r[2]} |")
mm.append("")
open(os.path.join(ROOT,"maps","current-to-future-state.md"),"w").write("\n".join(mm)); print("map: current-to-future-state")
print("weave complete")
