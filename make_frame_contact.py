from PIL import Image, ImageOps, ImageDraw
from pathlib import Path
root=Path(__file__).resolve().parent/"assets"/"video-review"
files=sorted(root.glob("*.jpg"))
thumbs=[]
for p in files:
    im=Image.open(p).convert("RGB")
    im.thumbnail((180,320))
    canvas=Image.new("RGB",(210,365),"#101b30")
    canvas.paste(im,((210-im.width)//2,8))
    d=ImageDraw.Draw(canvas)
    d.text((8,337),p.name[:28],fill="white")
    thumbs.append(canvas)
out=Image.new("RGB",(210*len(thumbs),365),"#07182f")
for i,im in enumerate(thumbs): out.paste(im,(i*210,0))
out.save(Path(__file__).resolve().parent/"video_review_contact.jpg",quality=90)
print("CONTACT",out.size, "FILES", [p.name for p in files])
