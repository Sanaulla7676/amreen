from pathlib import Path
from html.parser import HTMLParser
import sys

ROOT = Path(__file__).resolve().parent
html_files = sorted(ROOT.glob("*.html"))
broken = []

class RefParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        for key in ("src", "href"):
            value = data.get(key, "")
            if value and not value.startswith(("http:", "https:", "mailto:", "tel:", "data:", "#", "javascript:")):
                value = value.split("#", 1)[0].split("?", 1)[0]
                if value:
                    self.refs.append(value)

for html in html_files:
    parser = RefParser()
    parser.feed(html.read_text(encoding="utf-8"))
    for ref in parser.refs:
        if not (ROOT / ref).exists():
            broken.append((html.name, ref))

print("HTML pages:", len(html_files))
print("Broken local references:", len(broken))
for page, ref in broken:
    print(page, "->", ref)
if broken:
    sys.exit(1)
print("All local file references resolve.")
