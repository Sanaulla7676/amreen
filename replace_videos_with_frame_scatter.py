from pathlib import Path
import re

root=Path(__file__).resolve().parent
p=root/"index.html"
html=p.read_text(encoding="utf-8-sig")

start=html.find('<div class="film-grid">')
if start<0: raise SystemExit("Existing film-grid was not found.")
# Find balanced div closing tag for film-grid.
tag_re=re.compile(r'<div\b[^>]*>|</div\s*>',re.I)
depth=0
end=None
for m in tag_re.finditer(html,start):
    if m.group(0).lower().startswith("</div"):
        depth-=1
        if depth==0:
            end=m.end()
            break
    else:
        depth+=1
if end is None: raise SystemExit("Could not locate the end of the film-grid.")

frames=[
("certificate-01.jpg","Certificate presentation frame 1"),
("certificate-02.jpg","Certificate presentation frame 2"),
("certificate-03.jpg","Certificate presentation frame 3"),
("certificate-04.jpg","Certificate presentation frame 4"),
("certificate-05.jpg","Certificate presentation frame 5"),
("certificate-06.jpg","Certificate presentation frame 6"),
("certificate-07.jpg","Certificate presentation frame 7"),
("certificate-08.jpg","Certificate presentation frame 8"),
("classroom-01.jpg","Classroom training frame 1"),
("classroom-02.jpg","Classroom training frame 2"),
("classroom-03.jpg","Classroom training frame 3"),
("classroom-04.jpg","Classroom training frame 4"),
("classroom-05.jpg","Classroom training frame 5"),
("classroom-06.jpg","Classroom training frame 6"),
("classroom-07.jpg","Classroom training frame 7"),
("classroom-08.jpg","Classroom training frame 8"),
("classroom-09.jpg","Classroom training frame 9"),
("classroom-10.jpg","Classroom training frame 10"),
]
def make_group(duplicate=False):
    parts=['<div class="academy-scatter-group"'+(' aria-hidden="true"' if duplicate else '')+'>']
    for i,(filename,alt) in enumerate(frames,1):
        tab=' tabindex="-1"' if duplicate else ''
        parts.append(f'''  <a class="academy-scatter-frame frame-{i:02d}" href="assets/academy-frames/{filename}" target="_blank" rel="noopener noreferrer" aria-label="Open full-size image: {alt}"{tab}>
    <img src="assets/academy-frames/{filename}" alt="{alt}" loading="eager" decoding="async">
    <span class="academy-frame-glint" aria-hidden="true"></span>
  </a>''')
    parts.append('</div>')
    return "\n".join(parts)

replacement='''<div class="academy-scatter" aria-label="Scattered carousel of frames from academy videos">
  <span class="scatter-motion-orbit scatter-motion-orbit-one" aria-hidden="true"></span>
  <span class="scatter-motion-orbit scatter-motion-orbit-two" aria-hidden="true"></span>
  <span class="scatter-motion-spark scatter-motion-spark-one" aria-hidden="true"></span>
  <span class="scatter-motion-spark scatter-motion-spark-two" aria-hidden="true"></span>
  <div class="academy-scatter-viewport">
    <div class="academy-scatter-track">
''' + make_group(False) + "\n" + make_group(True) + '''
    </div>
  </div>
</div>'''

html=html[:start]+replacement+html[end:]
html=html.replace(
    "See moments from the studio, including a certificate presentation and a classroom learning session.",
    "A frame-by-frame look inside certificate celebrations and hands-on classroom learning at the academy."
)
p.write_text(html,encoding="utf-8-sig")
print("Removed both video player cards and all <video> elements from this section.")
print("Inserted 18 extracted full-resolution frames in a seamless duplicated scatter track.")
print("Updated section description for a frame gallery.")
