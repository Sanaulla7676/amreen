from pathlib import Path
p=Path(__file__).resolve().parent/"index.html"
s=p.read_text(encoding="utf-8-sig")
s=s.replace("reels-marquee-right-20261115-1","academy-scatter-frames-20261115-1")
p.write_text(s,encoding="utf-8-sig")
print("Cache-busting version advanced to academy-scatter-frames-20261115-1.")
