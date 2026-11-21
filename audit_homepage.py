from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
from collections import Counter

root=Path(__file__).resolve().parent
pages=sorted(root.glob("*.html"))
class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids=[]
        self.refs=[]
        self.buttons=[]
        self.video_count=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if "id" in a: self.ids.append(a["id"])
        if tag in ("a","link","script","img","source"):
            key="href" if tag in ("a","link") else "src"
            if a.get(key): self.refs.append((tag,key,a[key]))
        if tag=="button": self.buttons.append(a)
        if tag=="video": self.video_count+=1

missing=[]
dupes=[]
broken_anchors=[]
parser_cache={}
for page in pages:
    parser=PageParser()
    parser.feed(page.read_text(encoding="utf-8-sig",errors="replace"))
    parser_cache[page.name]=parser
    counts=Counter(parser.ids)
    for ident,n in counts.items():
        if n>1: dupes.append((page.name,ident,n))
    for tag,key,ref in parser.refs:
        u=urlparse(ref)
        if u.scheme or ref.startswith("//") or ref.startswith("data:") or ref.startswith("mailto:") or ref.startswith("tel:") or ref.startswith("javascript:"):
            continue
        path=unquote(u.path)
        if path.startswith("#") or not path:
            continue
        if path.startswith("/"): target=root/path.lstrip("/")
        else: target=page.parent/path
        if not target.exists():
            missing.append((page.name,tag,ref))
    ids=set(parser.ids)
    for tag,key,ref in parser.refs:
        if key=="href" and ref.startswith("#") and ref[1:] not in ids:
            broken_anchors.append((page.name,ref))

home=parser_cache.get("index.html")
h=(root/"index.html").read_text(encoding="utf-8-sig",errors="replace")
css=(root/"css"/"upgrade.css").read_text(encoding="utf-8")
mainjs=(root/"js"/"main.js").read_text(encoding="utf-8")
upgradejs=(root/"js"/"upgrade.js").read_text(encoding="utf-8")
checks={
"Four expanded course cards":h.count('class="course-card course-card-expanded"')==4,
"Course descriptions are present":all(x in h for x in ["Skin preparation and finish","Skin types and preparation","Hair preparation and sectioning","Bridal look planning"]),
"Single integrated 40-day program clearly stated":"not four separate paid enrolments" in h,
"Six detailed Why Choose points":h.count('class="why-item" data-reveal="up"')==6,
"Header CTA opens homepage dialog":'class="button button-primary header-cta" href="#contact"' in h,
"Enquiry dialog remains available":'id="enquiry-dialog"' in h and 'id="enquiry-form"' in h,
"Interest field included in WhatsApp message":"Area of interest:" in mainjs,
"40-day replay pointer-events restored":"pointer-events:auto !important;" in css,
"New course/why motion styles present":all(x in css for x in ["course-card-sheen","why-card-sheen","course-orbit-breathe","program-note-sheen"]),
"Homepage still has no academy video players":home.video_count==0 if home else False,
"Scattered frame gallery retained":'class="academy-scatter"' in h and h.count('class="academy-scatter-frame')==36,
"Instagram marquee retained":'class="instagram-marquee"' in h,
"Header stylesheet cache version current":"homepage-content-motion-20261115-1" in h,
}
print("PAGE / ASSET AUDIT")
print("HTML pages scanned:",len(pages))
print("Missing local references:",len(missing))
for row in missing: print("MISSING",row)
print("Duplicate IDs:",len(dupes))
for row in dupes: print("DUPLICATE",row)
print("Broken hash anchors:",len(broken_anchors))
for row in broken_anchors: print("BROKEN ANCHOR",row)
print("\nHOMEPAGE FEATURE CHECKS")
for k,v in checks.items(): print(("PASS" if v else "FAIL")+" - "+k)
print("\nSYNTAX BALANCE")
print("CSS braces",css.count("{"),css.count("}"))
if css.count("{")!=css.count("}"): raise SystemExit("CSS brace mismatch")
if missing or dupes or broken_anchors or not all(checks.values()): raise SystemExit("Audit failures detected")
