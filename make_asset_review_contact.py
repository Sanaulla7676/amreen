from PIL import Image, ImageDraw, ImageOps
from pathlib import Path
root=Path(__file__).resolve().parent
assets=root/"assets"
names=["course-makeup.jpg","course-skin.jpg","course-hair.jpg","course-bridal.jpg","academy-studio.jpg","career-mentor-folded-arms.png","student-work-01.jpg","student-work-02.jpg","student-work-03.jpg","student-work-04.jpg"]
tw,th=320,210
cols=2
rows=(len(names)+cols-1)//cols
out=Image.new("RGB",(cols*tw,rows*(th+32)),"#07182f")
d=ImageDraw.Draw(out)
for i,n in enumerate(names):
 p=assets/n
 if not p.exists(): continue
 im=Image.open(p).convert("RGB")
 original=im.size
 im=ImageOps.fit(im,(tw-12,th-12))
 x=(i%cols)*tw+6; y=(i//cols)*(th+32)+6
 out.paste(im,(x,y))
 d.text((x,y+th-8),f"{n}  {original}",fill="white")
out.save(root/"asset_review_contact.jpg",quality=92)
print(root/"asset_review_contact.jpg")
