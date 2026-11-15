from pathlib import Path
import re
root=Path(__file__).resolve().parent
html=(root/"index.html").read_text(encoding="utf-8-sig")
css=(root/"css"/"upgrade.css").read_text(encoding="utf-8")
js=(root/"js"/"upgrade.js").read_text(encoding="utf-8")
checks={}
checks["hero remains first"]=html.find('id="home"') < html.find('id="courses"')
checks["Inside Academy follows the 45-Day program"]=html.find('id="course-program"') < html.find('id="inside-academy"')
checks["Inside Academy is immediately before footer"]=html.find('id="inside-academy"') < html.find('<footer class="site-footer"')
checks["certificate video preserved"]="academy-certificate-moment.mp4" in html
checks["classroom video preserved"]="academy-classroom-session.mp4" in html
checks["old profile-wide iframe removed"]="amreenkhanum60/embed/" not in html
checks["nine Reel cards present"]=html.count('class="instagram-reel-card"')==9
checks["nine direct Reel links present"]=html.count('class="instagram-reel-link"')==9 and len(re.findall(r'href="https://www\.instagram\.com/amreenkhanum60/reel/',html))==9
checks["nine Reel embeds present"]=len(re.findall(r'src="https://www\.instagram\.com/reel/.*/embed/"',html))==9
checks["previous and next controls present"]='data-reel-step="-1"' in html and 'data-reel-step="1"' in html
checks["carousel CSS present"]=".instagram-reels-track" in css and ".instagram-reel-card" in css
checks["carousel JavaScript present"]="Horizontal Instagram Reel carousel" in js
checks["cache-busting stylesheet present"]="homepage-reels-20261115-1" in html
for k,v in checks.items(): print(("PASS" if v else "FAIL")+" - "+k)
print("CSS braces:",css.count("{"),css.count("}"))
if css.count("{")!=css.count("}"): raise SystemExit("CSS brace mismatch")
if not all(checks.values()): raise SystemExit("Homepage validation failed")
