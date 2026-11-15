from pathlib import Path
p=Path(__file__).resolve().parent/"index.html"
s=p.read_text(encoding="utf-8-sig")
s=s.replace("homepage-content-motion-20261115-2","homepage-content-motion-20261115-3")
p.write_text(s,encoding="utf-8-sig")
print("Cache-busting stylesheet version advanced after mobile layout fix.")
