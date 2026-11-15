from pathlib import Path
p=Path(__file__).resolve().parent/"index.html"
s=p.read_text(encoding="utf-8-sig").replace("homepage-content-motion-20261115-1","homepage-content-motion-20261115-2")
p.write_text(s,encoding="utf-8-sig")
print("Updated homepage CSS version after visual asset corrections.")
