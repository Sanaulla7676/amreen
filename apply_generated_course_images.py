from pathlib import Path
import re

root=Path(__file__).resolve().parent
assets=root/"assets"/"course-images"
assets.mkdir(parents=True,exist_ok=True)

mapping={
"assets/course-makeup.jpg":"assets/course-images/course-makeup-artistry.webp",
"assets/course-skin.jpg":"assets/course-images/course-skin-aesthetics.webp",
"assets/course-hair.jpg":"assets/course-images/course-hair-styling.webp",
"assets/course-bridal.jpg":"assets/course-images/course-bridal-artistry.webp",
"assets/student-work-01.jpg":"assets/academy-frames/certificate-03.jpg",
"assets/student-work-02.jpg":"assets/academy-frames/certificate-06.jpg",
"assets/student-work-03.jpg":"assets/academy-frames/classroom-04.jpg",
"assets/student-work-04.jpg":"assets/academy-frames/classroom-08.jpg",
}
for p in root.glob("*.html"):
    if p.name=="layout_diagnostic.html": continue
    s=p.read_text(encoding="utf-8-sig")
    for old,new in mapping.items(): s=s.replace(old,new)
    if p.name=="student-success.html":
        s=s.replace("Makeup practice look from the academy homepage gallery","Students celebrating at a certificate presentation")
        s=s.replace("Hair styling practice look from the academy homepage gallery","Students with their academy certificates")
        s=s.replace("Makeup application practice look from the academy homepage gallery","Instructor guiding a classroom learning session")
        s=s.replace("Bridal hairstyle practice look from the academy homepage gallery","Students learning together in the academy classroom")
        s=s.replace("<figcaption>Makeup practice</figcaption>","<figcaption>Certificate presentation</figcaption>")
        s=s.replace("<figcaption>Hair styling</figcaption>","<figcaption>Student milestones</figcaption>")
        s=s.replace("<figcaption>Makeup application</figcaption>","<figcaption>Guided classroom learning</figcaption>")
        s=s.replace("<figcaption>Bridal hair</figcaption>","<figcaption>Learning together</figcaption>")
    p.write_text(s,encoding="utf-8-sig")

p=root/"index.html"
s=p.read_text(encoding="utf-8-sig")
cards={
"course-art-makeup":('course-makeup-artistry.webp','Professional Makeup Artistry training with an academy makeup artist working on a client','01','MAKEUP ARTISTRY'),
"course-art-skin":('course-skin-aesthetics.webp','Skin and Aesthetics facial treatment training at Amreen’s Academy','02','SKIN &amp; AESTHETICS'),
"course-art-hair":('course-hair-styling.webp','Hair styling training with an academy stylist working on a client','03','HAIR STYLING'),
"course-art-bridal":('course-bridal-artistry.webp','Bridal artistry look with makeup and jewellery details','04','BRIDAL ARTISTRY'),
}
for cls,(filename,alt,num,label) in cards.items():
    pattern=re.compile(r'<div class="course-card-media course-art '+re.escape(cls)+r'"[^>]*>.*?</div>',re.S)
    replacement=f'''<div class="course-card-media course-card-photo {cls}">
          <img src="assets/course-images/{filename}" alt="{alt}" loading="lazy" decoding="async">
          <span class="course-card-index">{num}</span>
          <span class="course-card-media-caption">{label}</span>
        </div>'''
    s,n=pattern.subn(replacement,s,count=1)
    if n!=1: raise SystemExit("Could not replace course artwork for "+cls)
p.write_text(s,encoding="utf-8-sig")
print("Replaced four vector placeholders with generated course-image assets.")
print("Updated course-detail pages and blog hero to use the correct generated image.")
print("Updated student-success gallery to use real academy video frames and accurate captions.")
