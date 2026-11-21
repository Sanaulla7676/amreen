from pathlib import Path
import re
root=Path(__file__).resolve().parent
h=(root/"index.html").read_text(encoding="utf-8-sig")
c=(root/"css"/"upgrade.css").read_text(encoding="utf-8")
j=(root/"js"/"upgrade.js").read_text(encoding="utf-8")
tests={
"Inside Academy remains after the 40-day program":h.find('id="course-program"') < h.find('id="inside-academy"'),
"Inside Academy remains immediately before footer":h.find('id="inside-academy"') < h.find('<footer class="site-footer"'),
"Nine source Instagram Reels retained":h.count('class="instagram-marquee-item"')==18,
"One visible group and one loop duplicate":h.count('class="instagram-marquee-group"')==2,
"No card or carousel markup":"instagram-reel-card" not in h and "instagram-reels-controls" not in h,
"No arrow controls":"data-reel-step" not in h,
"Every item opens direct Reel":len(re.findall(r'href="https://www\.instagram\.com/amreenkhanum60/reel/',h))==18,
"Every preview embeds Reel source":len(re.findall(r'src="https://www\.instagram\.com/reel/.*/embed/"',h))==18,
"Continuous left-to-right animation present":"instagram-videos-move-right" in c and "translate3d(-50%,0,0)" in c and "to{transform:translate3d(0,0,0)}" in c,
"Marquee runs full viewport width":"width:100vw;" in c and "margin-left:calc(50% - 50vw);" in c,
"Old carousel script removed":"Horizontal Instagram Reel carousel" not in j,
"Previous certificate video still present":"academy-certificate-moment.mp4" in h,
"Previous classroom video still present":"academy-classroom-session.mp4" in h,
"Cache-busting URL updated":"reels-marquee-right-20261115-1" in h,
}
for k,v in tests.items(): print(("PASS" if v else "FAIL")+" - "+k)
print("CSS braces:",c.count("{"),c.count("}"))
if c.count("{")!=c.count("}"): raise SystemExit("CSS brace mismatch")
if not all(tests.values()): raise SystemExit("Validation failed")
