from pathlib import Path
root=Path(__file__).resolve().parent
p=root/"js"/"main.js"
s=p.read_text(encoding="utf-8")
old="""        'Course: ' + (data.get('course') || ''),
        'Please share the latest details, batch dates and fees.'"""
new="""        'Course: ' + (data.get('course') || ''),
        'Area of interest: ' + (data.get('interest') || 'Not specified'),
        'Please share the latest details, batch dates and fees.'"""
if old not in s:
    raise SystemExit("Could not find enquiry message composition block in main.js.")
s=s.replace(old,new,1)
p.write_text(s,encoding="utf-8")

hp=root/"index.html"
h=hp.read_text(encoding="utf-8-sig")
h=h.replace("academy-scatter-frames-20261115-1","homepage-content-motion-20261115-1")
hp.write_text(h,encoding="utf-8-sig")
print("WhatsApp enquiry now includes the selected interest.")
print("Homepage CSS cache version updated.")
