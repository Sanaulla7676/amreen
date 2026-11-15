from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import re
root=Path(__file__).resolve().parent
pages=[p for p in root.glob("*.html") if p.name!="layout_diagnostic.html"]
refs=set()
for p in pages:
 s=p.read_text(encoding="utf-8-sig",errors="replace")
 for x in re.findall(r'(?:src|href|poster)="([^"]+)"',s,re.I):
  u=urlparse(x)
  if u.scheme or x.startswith(("//","data:","#","mailto:","tel:","javascript:")): continue
  q=unquote(u.path)
  if q and not q.endswith(".html") and "." in q.split("/")[-1]: refs.add(q)
for p in (root/"css").glob("*.css"):
 s=p.read_text(encoding="utf-8-sig",errors="replace")
 for x in re.findall(r'url\(["\']?([^"\')]+)',s,re.I):
  if x.startswith(("http:","https:","data:","#")): continue
  refs.add(unquote(x.split("?")[0]))
for p in (root/"js").glob("*.js"):
 s=p.read_text(encoding="utf-8-sig",errors="replace")
 for x in re.findall(r'["\']((?:assets/)[^"\']+)["\']',s):
  refs.add(unquote(x.split("?")[0]))
print("PAGES",len(pages),",".join(p.name for p in sorted(pages)))
print("CSS",",".join("css/"+p.name for p in sorted((root/"css").glob("*.css"))))
print("JS",",".join("js/"+p.name for p in sorted((root/"js").glob("*.js"))))
print("REFERENCED ASSETS")
for x in sorted(refs):
 f=root/x
 if f.exists() and f.is_file(): print(f"{x}\t{f.stat().st_size}")
 else: print("MISSING\t"+x)
