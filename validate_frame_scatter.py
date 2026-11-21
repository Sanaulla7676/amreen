from pathlib import Path
import re
root=Path(__file__).resolve().parent
h=(root/"index.html").read_text(encoding="utf-8-sig")
c=(root/"css"/"upgrade.css").read_text(encoding="utf-8")
j=(root/"js"/"upgrade.js").read_text(encoding="utf-8")
section=h[h.find('id="inside-academy"'):]
tests={
"Inside Academy remains after the 40-day section":h.find('id="course-program"') < h.find('id="inside-academy"'),
"Inside Academy remains before footer":h.find('id="inside-academy"') < h.find('<footer class="site-footer"'),
"Original two video players removed from homepage":'<video' not in section and 'academy-certificate-moment.mp4' not in section and 'academy-classroom-session.mp4' not in section,
"Frame gallery inserted":'class="academy-scatter"' in section,
"18 extracted source frames included":section.count('class="academy-scatter-frame')==36,
"Two groups for seamless looping":section.count('class="academy-scatter-group"')==2,
"Scattered frame variations applied":all(f'frame-{i:02d}' in section for i in range(1,19)),
"Gallery frame URLs all exist":all((root/'assets'/'academy-frames'/f).exists() for f in [f'certificate-{i:02d}.jpg' for i in range(1,9)]+[f'classroom-{i:02d}.jpg' for i in range(1,11)]),
"Motion graphics CSS present":all(x in c for x in ['academy-orbit-spin','academy-light-sweep','academy-spark-float','academy-scatter-flow-right']),
"Left-to-right motion present":'from{transform:translate3d(-50%,0,0)}' in c and 'to{transform:translate3d(0,0,0)}' in c,
"Old Instagram marquee remains below section videos":'class="instagram-marquee"' in section,
"Existing two video captions removed":'film-card' not in section,
"Cache-busting stylesheet version updated":"academy-scatter-frames-20261115-1" in h,
}
for k,v in tests.items(): print(("PASS" if v else "FAIL")+" - "+k)
print("CSS braces:",c.count("{"),c.count("}"))
if c.count("{")!=c.count("}"): raise SystemExit("CSS brace mismatch")
if not all(tests.values()): raise SystemExit("Validation failed")
