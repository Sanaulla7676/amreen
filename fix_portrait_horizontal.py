from pathlib import Path
p=Path(__file__).resolve().parent/"css"/"upgrade.css"
s=p.read_text(encoding="utf-8")
repls=[
("  left: auto !important;\n  right: 2.5% !important;\n  top: 417px !important;",
 "  left: 5.7% !important;\n  right: auto !important;\n  top: 417px !important;"),
("  .hero .hero-figure { right: 1.5% !important; top: 430px !important; height: 460px !important; max-width: 55%; }",
 "  .hero .hero-figure { left: 5.7% !important; right: auto !important; top: 430px !important; height: 460px !important; max-width: 55%; }"),
("  .hero .hero-figure { right: 0 !important; top: 390px !important; height: 470px !important; max-width: 58%; }",
 "  .hero .hero-figure { left: 5.7% !important; right: auto !important; top: 390px !important; height: 470px !important; max-width: 58%; }"),
]
for old,new in repls:
    if old not in s: raise SystemExit("Expected figure layout rule missing: "+old[:80])
    s=s.replace(old,new,1)
p.write_text(s,encoding="utf-8")
print("Restored the portrait's original left-side anchor; the vertical offset remains 417px.")
print("CSS braces:",s.count("{"),s.count("}"))
