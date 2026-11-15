from pathlib import Path
p=Path(__file__).resolve().parent/"index.html"
s=p.read_text(encoding="utf-8-sig")
old='<div class="instagram-reels-panel" aria-label="Recent Instagram Reels">'
new='<div class="instagram-reels-panel" id="instagram-reels" aria-label="Recent Instagram Reels">'
if old not in s:
    raise SystemExit("Instagram reels panel marker not found.")
s=s.replace(old,new,1)
p.write_text(s,encoding="utf-8-sig")
print("Added a stable anchor for the Instagram carousel.")
