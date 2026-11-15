from pathlib import Path
import re
root=Path(__file__).resolve().parent
p=root/"index.html"
s=p.read_text(encoding="utf-8-sig")
# The visual-asset replacement left the old image-caption fragment duplicated after each new media block.
pattern=re.compile(
 r'(?P<media></div>)\s*'
 r'<span class="course-card-index">(?P<num>0[1-4])</span>'
 r'<span class="course-card-media-caption">(?P<label>MAKEUP ARTISTRY|SKIN &amp; AESTHETICS|HAIR STYLING|BRIDAL ARTISTRY)</span>'
 r'\s*</div>\s*(?=<div class="course-card-body">)',
 re.I
)
s,n=pattern.subn(r'\g<media>\n        ',s)
if n!=4: raise SystemExit(f"Expected to remove 4 duplicate remnants, removed {n}.")
s=s.replace("homepage-content-motion-20261115-3","amreen-production-20261115-1")
p.write_text(s,encoding="utf-8-sig")
print("Removed exactly four duplicated course-media fragments.")
print("Updated production cache-busting CSS version.")
