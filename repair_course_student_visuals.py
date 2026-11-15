from pathlib import Path
import re

root=Path(__file__).resolve().parent
p=root/"index.html"
html=p.read_text(encoding="utf-8-sig")

arts={
"course-makeup.jpg":'''<div class="course-card-media course-art course-art-makeup" aria-hidden="true">
  <span class="course-art-orbit course-art-orbit-one"></span><span class="course-art-orbit course-art-orbit-two"></span>
  <span class="course-art-mark">01</span>
  <div class="course-art-symbol"><svg viewBox="0 0 120 120"><path d="M31 88 78 41" /><path d="m70 31 12-12 18 18-12 12z"/><path d="m26 93 11-11 11 11-11 11z"/><path d="m80 38 8-8 M73 45l8-8 M66 52l8-8"/><path d="M21 100 35 86" /></svg></div>
  <span class="course-card-index">01</span><span class="course-card-media-caption">MAKEUP ARTISTRY</span>
</div>''',
"course-skin.jpg":'''<div class="course-card-media course-art course-art-skin" aria-hidden="true">
  <span class="course-art-orbit course-art-orbit-one"></span><span class="course-art-orbit course-art-orbit-two"></span>
  <span class="course-art-mark">02</span>
  <div class="course-art-symbol"><svg viewBox="0 0 120 120"><path d="M60 18c-22 0-36 17-36 40 0 25 15 44 36 44s36-19 36-44C96 35 82 18 60 18Z"/><path d="M43 55c4-4 9-4 13 0 M64 55c4-4 9-4 13 0"/><path d="M58 62c-1 7-3 11-5 15 5 4 13 4 18 0"/><path d="M44 83c9 7 23 7 32 0"/><path d="M23 32 17 25 M97 32l6-7 M60 11V3"/></svg></div>
  <span class="course-card-index">02</span><span class="course-card-media-caption">SKIN &amp; AESTHETICS</span>
</div>''',
"course-hair.jpg":'''<div class="course-card-media course-art course-art-hair" aria-hidden="true">
  <span class="course-art-orbit course-art-orbit-one"></span><span class="course-art-orbit course-art-orbit-two"></span>
  <span class="course-art-mark">03</span>
  <div class="course-art-symbol"><svg viewBox="0 0 120 120"><path d="M28 100c-9-18-6-46 5-65 8-13 20-20 32-20 14 0 26 8 32 22 9 20 7 46-1 63"/><path d="M37 97c-4-21 4-47 17-66 M52 102c-5-24 3-52 17-74 M68 102c3-19 10-39 24-53"/><path d="M27 62c9-6 13-14 15-24 M77 18c8 7 13 17 15 28"/><path d="M24 102h72"/></svg></div>
  <span class="course-card-index">03</span><span class="course-card-media-caption">HAIR STYLING</span>
</div>''',
"course-bridal.jpg":'''<div class="course-card-media course-art course-art-bridal" aria-hidden="true">
  <span class="course-art-orbit course-art-orbit-one"></span><span class="course-art-orbit course-art-orbit-two"></span>
  <span class="course-art-mark">04</span>
  <div class="course-art-symbol"><svg viewBox="0 0 120 120"><path d="m24 82 9-43 23 19 12-32 17 32 20-19 10 43z"/><path d="M24 82h91v12H24z"/><path d="M56 58c-8 8-13 18-13 30 M71 58c8 8 13 18 13 30"/><circle cx="56" cy="24" r="6"/><circle cx="68" cy="18" r="5"/><circle cx="86" cy="28" r="5"/></svg></div>
  <span class="course-card-index">04</span><span class="course-card-media-caption">BRIDAL ARTISTRY</span>
</div>'''
}

def replace_balanced_div(source,start,replacement):
    token=re.compile(r'<div\b[^>]*>|</div\s*>',re.I)
    depth=0
    end=None
    for m in token.finditer(source,start):
        if m.group(0).lower().startswith("</div"):
            depth-=1
            if depth==0:
                end=m.end()
                break
        else:
            depth+=1
    if end is None: raise SystemExit("Unable to close a course media div.")
    return source[:start]+replacement+source[end:],end

# Replace each of the four damaged low-resolution image blocks with vector artwork.
for filename,art in arts.items():
    marker='<div class="course-card-media">'
    pos=html.find(marker)
    found=False
    while pos>=0:
        # Find the actual image source inside this div.
        token=re.compile(r'<div\b[^>]*>|</div\s*>',re.I)
        depth=0
        end=None
        for m in token.finditer(html,pos):
            if m.group(0).lower().startswith("</div"):
                depth-=1
                if depth==0:
                    end=m.end(); break
            else: depth+=1
        if end is None: raise SystemExit("Could not parse course media block.")
        block=html[pos:end]
        if filename in block:
            html=html[:pos]+art+html[end:]
            found=True
            break
        pos=html.find(marker,end)
    if not found: raise SystemExit("Missing expected broken asset reference: "+filename)

# Replace broken student-work image tiles with real extracted stills and accurate captions.
student_marker='<section class="student-section'
start=html.find(student_marker)
if start<0: raise SystemExit("Student work section missing.")
section_end=html.find("</section>",start)
if section_end<0: raise SystemExit("Student section end missing.")
sec=html[start:section_end+len("</section>")]
old_grid=re.search(r'<div class="student-grid">.*?</div>\s*</div>\s*</section>',sec,re.S)
if not old_grid: raise SystemExit("Student grid not found.")
new_grid='''<div class="student-grid">
          <figure><img src="assets/academy-frames/certificate-03.jpg" alt="Students celebrating at a certificate presentation" loading="lazy" decoding="async"><figcaption>Certificate celebrations</figcaption></figure>
          <figure><img src="assets/academy-frames/certificate-06.jpg" alt="A group of students with their academy certificates" loading="lazy" decoding="async"><figcaption>Student milestones</figcaption></figure>
          <figure><img src="assets/academy-frames/classroom-04.jpg" alt="Instructor guiding a classroom learning session" loading="lazy" decoding="async"><figcaption>Guided classroom learning</figcaption></figure>
          <figure><img src="assets/academy-frames/classroom-08.jpg" alt="Students seated together during an academy session" loading="lazy" decoding="async"><figcaption>Learning together</figcaption></figure>
        </div>
      </div>
    </section>'''
sec=sec[:old_grid.start()]+new_grid+sec[old_grid.end():]
sec=sec.replace("Student Work &amp; Practice","Student Learning Moments")
html=html[:start]+sec+html[section_end+len("</section>"):]

p.write_text(html,encoding="utf-8-sig")
print("Replaced all four damaged course thumbnails with branded SVG artwork.")
print("Replaced four damaged student-work crops with authentic frames from the academy videos.")
