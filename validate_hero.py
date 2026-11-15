from pathlib import Path
import re
root = Path(__file__).resolve().parent
html = (root / "index.html").read_text(encoding="utf-8")
css = (root / "css" / "upgrade.css").read_text(encoding="utf-8")
checks = {
    "AMREEN'S headline": "AMREEN'S</span>" in html,
    "ACADEMY script line": 'class="hero-title-academy">ACADEMY</span>' in html,
    "hero tagline removed": 'class="hero-phrase"' not in html,
    "old signoff removed": 'class="hero-signoff"' not in html,
    "swapped portrait kept": 'assets/hero-seated-face-swapped.png' in html,
    "desktop hero height 900px": "min-height:900px;" in css and "height:900px;" in css,
    "portrait moved down 300px": "top:417px;" in css,
    "portrait display height retained": "height:481px;" in css,
    "portrait horizontal side retained": "right:2.5%;" in css,
    "copy aligned to extreme right": "right:4%;" in css and "text-align:right;" in css,
    "mobile responsive rules": "@media(max-width:650px)" in css and "@media(max-width:420px)" in css,
    "sections below hero remain": 'id="inside-academy"' in html and 'id="courses"' in html,
}
for name, ok in checks.items():
    print(("PASS" if ok else "FAIL") + " - " + name)
if css.count("{") != css.count("}"):
    print("FAIL - CSS brace balance")
    raise SystemExit(1)
print("CSS braces:", css.count("{"), "/", css.count("}"))
if not all(checks.values()):
    raise SystemExit(1)
