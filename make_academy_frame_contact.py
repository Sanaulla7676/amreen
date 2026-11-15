from PIL import Image, ImageDraw
from pathlib import Path
root=Path(__file__).resolve().parent/"assets"/"academy-frames"
files=sorted(root.glob("*.jpg"))
tw,th=180,320
cols=6
rows=(len(files)+cols-1)//cols
out=Image.new("RGB",(cols*tw,rows*(th+34)),"#09182e")
draw=ImageDraw.Draw(out)
for i,p in enumerate(files):
    im=Image.open(p).convert("RGB")
    im.thumbnail((tw-10,th-8))
    x=(i%cols)*tw+(tw-im.width)//2
    y=(i//cols)*(th+34)+4
    out.paste(im,(x,y))
    draw.text(((i%cols)*tw+7,(i//cols)*(th+34)+th),p.stem,fill="white")
target=Path(__file__).resolve().parent/"academy_frame_contact.jpg"
out.save(target,quality=92)
print("CONTACT",target,out.size)
