from pathlib import Path
import re, json

ROOT = Path(__file__).resolve().parent
ASSET = ROOT / "assets"
phone = "8123410118"
wa = "https://wa.me/918123410118"
ig = "https://www.instagram.com/amreenkhanum60/"
address = "#23, Bharath Nagar, Ashwath Nagar, 2nd Stage, Thanisandra Main Road, Bengaluru, Karnataka 560077"

video_section = """
<section class="academy-films" id="inside-academy" aria-labelledby="films-title">
  <div class="films-orb films-orb-one" aria-hidden="true"></div>
  <div class="films-shell">
    <div class="films-heading" data-reveal="up">
      <p class="film-kicker">BEHIND THE SKILLS <span></span> INSIDE THE ACADEMY</p>
      <h2 id="films-title">Real learning. <em>Real moments.</em></h2>
      <p>See moments from the studio, including a certificate presentation and a classroom learning session.</p>
    </div>
    <div class="film-grid">
      <article class="film-card" data-reveal="left">
        <div class="film-frame">
          <video controls playsinline preload="none" poster="assets/video-certificate-poster.jpg" aria-label="Certificate presentation at Amreen's Academy">
            <source src="assets/academy-certificate-moment.mp4" type="video/mp4">
            Your browser does not support HTML video.
          </video>
          <span class="film-index">01 / CERTIFICATE MOMENT</span>
        </div>
        <div class="film-caption"><span class="film-dot"></span><div><h3>A moment worth celebrating</h3><p>Certificate presentation and academy community.</p></div><span class="film-arrow">↗</span></div>
      </article>
      <article class="film-card" data-reveal="right">
        <div class="film-frame">
          <video controls playsinline preload="none" poster="assets/video-classroom-poster.jpg" aria-label="Classroom learning session at Amreen's Academy">
            <source src="assets/academy-classroom-session.mp4" type="video/mp4">
            Your browser does not support HTML video.
          </video>
          <span class="film-index">02 / CLASSROOM SESSION</span>
        </div>
        <div class="film-caption"><span class="film-dot"></span><div><h3>Inside a learning session</h3><p>A glimpse of the studio and classroom environment.</p></div><span class="film-arrow">↗</span></div>
      </article>
    </div>
    <div class="films-footer"><span>MORE FROM THE STUDIO</span><a href="https://www.instagram.com/amreenkhanum60/" target="_blank" rel="noopener noreferrer">Follow @amreenkhanum60 <b>↗</b></a></div>
  </div>
</section>
"""

review_section = """
<section class="review-strip" aria-labelledby="review-title">
  <div class="review-strip__inner">
    <div class="review-strip__lead" data-reveal="left">
      <p class="mini-label">LOCAL GOOGLE LISTING</p>
      <h2 id="review-title">A warm welcome, close to home.</h2>
      <div class="google-score"><strong>5.0</strong><span>★★★★★</span><small>3 public reviews · snapshot checked November 2026</small></div>
    </div>
    <div class="review-quote-grid" data-stagger>
      <blockquote><span>“</span><p>Very good beauty parlour</p><cite>Google Business review</cite></blockquote>
      <blockquote><span>“</span><p>Nice experience excellent service</p><cite>Google Business review</cite></blockquote>
    </div>
    <a class="review-map-link" href="https://www.google.com/maps/search/?api=1&query=Amreens%20academy%20%26%20makeover%20studio&query_place_id=ChIJb3bteaUXrjsRIJOmc2EQrmY" target="_blank" rel="noopener noreferrer">View live Google listing ↗</a>
  </div>
</section>
"""

# Home page: videos immediately after hero.
home = ROOT / "index.html"
s = home.read_text(encoding="utf-8")
marker = '  <section class="courses-section light-section"'
if 'id="inside-academy"' not in s:
    if marker not in s:
        raise RuntimeError("Cannot find courses section insertion point in homepage")
    s = s.replace(marker, video_section + "\n" + marker, 1)

# Replace the original standalone program block with the one integrated offer.
program_pattern = re.compile(r'(<div class="program-copy">).*?(</div>\s*<div class="program-ribbon")', re.S)
program_copy = """<div class="program-copy">
          <span class="program-mark" aria-hidden="true"></span>
          <div class="program-count-wrap"><span class="program-count" data-count-up="40">0</span><small>DAYS · ONE INTEGRATED COURSE</small></div>
          <h2 id="program-title">Beauty &amp; Makeup<br>Professional Program</h2>
          <p>One 40-day program bringing together Professional Makeup Artistry, Skin &amp; Aesthetics, Hair Styling and Bridal Artistry.</p>
          <div class="program-facts"><span>✓ Four learning areas</span><span>✓ Academy certificate</span></div>
          <div class="program-price-line"><strong>₹30,000</strong><span>Full course fee</span><span>3 instalments available</span></div>
          <a class="button button-primary" href="45-day-course.html">Explore the 40-Day Course <span aria-hidden="true">→</span></a>
        </div>
        <div class="program-ribbon"""
s, n = program_pattern.subn(lambda m: program_copy, s, count=1)
if n != 1:
    raise RuntimeError("Could not update homepage 40-day program banner")

if 'class="review-strip"' not in s:
    s = s.replace('  <section class="program-section"', review_section + '\n  <section class="program-section"', 1)

s = s.replace('<a href="#contact" aria-label="YouTube">', '<a href="https://www.instagram.com/amreenkhanum60/" target="_blank" rel="noopener noreferrer" aria-label="Instagram updates">', 1) if '<a href="#contact" aria-label="YouTube">' in s else s
# Make the home modal reflect one integrated program, with area of interest rather than separate course purchases.
s = s.replace('<label>Course of interest<select name="course" required><option value="" selected disabled>Select a course</option><option>Professional Makeup Artistry</option><option>Skin &amp; Aesthetics</option><option>Hair Styling</option><option>Bridal Artistry</option><option>40-Day Beauty &amp; Makeup Course</option></select></label>',
'''<label>Program<select name="course" required><option value="40-Day Integrated Beauty & Makeup Program">40-Day Integrated Beauty &amp; Makeup Program</option></select></label>
        <label>Area you are most interested in<select name="interest"><option>All four learning areas</option><option>Professional Makeup Artistry</option><option>Skin &amp; Aesthetics</option><option>Hair Styling</option><option>Bridal Artistry</option></select></label>''')
home.write_text(s, encoding="utf-8")

# Courses overview: clearly explain one integrated course, not four separate paid courses.
p = ROOT / "courses.html"
s = p.read_text(encoding="utf-8")
s = s.replace("The academy homepage highlights four core beauty pathways. Course details, current batches, fees and the latest syllabus should be confirmed directly with the academy.",
"Amreen's Academy offers one integrated 40-day Beauty &amp; Makeup program. The four cards below are learning areas included within the same course, not four separately priced enrolments. The full course fee is ₹30,000; three instalments are available.")
s = s.replace("A focused, practical program designed to build your skills and confidence in the beauty industry. Ask the academy for the current syllabus, batch dates and fee details.",
"A single 40-day program covering all four learning areas: Professional Makeup Artistry, Skin &amp; Aesthetics, Hair Styling and Bridal Artistry. An academy certificate is provided on successful completion. Full fee ₹30,000, with three instalments available. Ask the academy to confirm the instalment schedule and current batch dates.")
# Add price details to highlighted featured course.
s = s.replace('<span class="mini-label">40-DAY PROGRAM</span><h3>Beauty &amp; Makeup Course</h3>',
'<span class="mini-label">ONE INTEGRATED 40-DAY PROGRAM</span><h3>Four learning areas. One complete course.</h3>')
s = s.replace('A focused, practical program designed to build your skills and confidence in the beauty industry.',
'Professional Makeup Artistry · Skin &amp; Aesthetics · Hair Styling · Bridal Artistry. Academy certificate on successful completion.')
s = s.replace('<a class="button button-primary" href="45-day-course.html">View 40-day course <span>→</span></a>',
'<div class="course-price-emphasis"><strong>₹30,000</strong><span>Full course fee</span><b>3 instalments available</b></div><a class="button button-primary" href="45-day-course.html">View 40-day course <span>→</span></a>')
p.write_text(s, encoding="utf-8")

# 40-day detail page: make the offer and payment structure explicit.
p = ROOT / "45-day-course.html"
s = p.read_text(encoding="utf-8")
s = s.replace('<span class="mini-label">40 DAYS · BEAUTY &amp; MAKEUP</span><h3>Learn with focus. Practise with purpose.</h3>',
'<span class="mini-label">ONE INTEGRATED PROGRAM · 40 DAYS</span><h3>Four beauty disciplines. One complete learning journey.</h3>')
s = s.replace("The academy homepage describes this as a focused, practical program designed to build skills and confidence in the beauty industry.",
"The program brings together Professional Makeup Artistry, Skin &amp; Aesthetics, Hair Styling and Bridal Artistry. These are included learning areas within one course, not separate course fees.")
s = s.replace("For the latest course outline, class schedule, eligibility, fee and materials list, contact the academy directly before enrolling.",
"Full course fee: ₹30,000. Three instalments are available: ₹8,333 + ₹8,333 + ₹8,334 (₹30,000 total). The academy provides a course certificate on successful completion. Confirm instalment due dates, batch timings, syllabus and kit requirements with the academy.")
# Replace the 3-point section with the confirmed program facts.
s = s.replace("Ask for the current module list and practical learning plan.","Makeup Artistry, Skin &amp; Aesthetics, Hair Styling and Bridal Artistry are included.")
s = s.replace("Check upcoming dates, class timings and available seats.","Confirm the batch timetable and the dates for each of the three instalments.")
s = s.replace("Confirm the kit, materials and anything to bring to class.","Ask about assessment, certificate requirements and the materials to bring.")
# Add an explicit pricing card before the three points.
anchor = '<div class="three-points" data-stagger>'
pricing = '''<div class="course-investment" data-reveal="scale">
  <div><span class="mini-label">FULL PROGRAM FEE</span><strong>₹30,000</strong><p>One course · Four included learning areas · Academy certificate on successful completion</p></div>
  <div class="installment-plan"><span>THREE INSTALMENTS</span><strong>₹8,333 <i>+</i> ₹8,333 <i>+</i> ₹8,334</strong><small>Total ₹30,000 · Confirm payment dates directly with the academy.</small></div>
</div>
'''
if 'class="course-investment"' not in s and anchor in s:
    s = s.replace(anchor, pricing + anchor, 1)
p.write_text(s, encoding="utf-8")

# Module pages must not imply separately priced courses.
module_files = ["professional-makeup.html", "skin-aesthetics.html", "hair-styling.html", "bridal-artistry.html"]
module_note = "This is one of the four learning areas included within the single 40-day integrated Beauty &amp; Makeup course. It is not a separate paid enrolment. The full program fee is ₹30,000, with three instalments available and an academy certificate on successful completion."
for name in module_files:
    p = ROOT / name
    s = p.read_text(encoding="utf-8")
    s = re.sub(r'<p class="quiet-note">.*?</p>', '<p class="quiet-note">' + module_note + '</p>', s, count=1, flags=re.S)
    s = s.replace("AREAS TO DISCUSS", "LEARNING THEMES")
    p.write_text(s, encoding="utf-8")

# FAQs: replace and expand the most important questions.
p = ROOT / "faqs.html"
s = p.read_text(encoding="utf-8")
s = s.replace("The academy's Instagram bio describes makeup, mehendi and beautician services. Its homepage also presents Professional Makeup Artistry, Skin &amp; Aesthetics, Hair Styling and Bridal Artistry.",
"The public profile describes makeup, mehendi and beautician services. The integrated 40-day Beauty &amp; Makeup course includes Professional Makeup Artistry, Skin &amp; Aesthetics, Hair Styling and Bridal Artistry.")
s = s.replace("The academy homepage features a 40-Day Beauty &amp; Makeup Course. Contact the academy to confirm the current batch, syllabus, schedule and availability.",
"Yes. It is the academy's single integrated 40-day Beauty &amp; Makeup program and includes all four learning areas: Professional Makeup Artistry, Skin &amp; Aesthetics, Hair Styling and Bridal Artistry.")
s = s.replace("Current fees, batch dates and course-specific schedules were not publicly confirmed in the information reviewed. Contact the academy for the latest details.",
"The full course fee is ₹30,000. The academy also offers a three-instalment option: ₹8,333 + ₹8,333 + ₹8,334 (₹30,000 total). Confirm the payment dates and any applicable terms directly with the academy.")
s = s.replace("No such claim is published in the material reviewed. The 40-day duration belongs to the featured Beauty &amp; Makeup Course; ask about the duration of each other pathway.",
"The academy describes one integrated 40-day course that includes all four learning areas. They are not separate paid courses.")
s = s.replace("Certificate details were not confirmed in the public information reviewed. Ask the academy what certificate, if any, is provided for your selected course.",
"The academy provides a course certificate on successful completion of the 40-day integrated program. Confirm assessment and completion requirements before enrolling. No external accreditation is claimed on this website.")
# Append FAQ items before CTA if not present.
if "How much does the integrated 40-day course cost?" not in s:
    insert = '''<details class="faq-item" data-reveal="up"><summary>How much does the integrated 40-day course cost?<span>＋</span></summary><div><p>The full course fee is ₹30,000.</p></div></details>
<details class="faq-item" data-reveal="up"><summary>Can I pay in instalments?<span>＋</span></summary><div><p>Yes. Three instalments are available: ₹8,333 + ₹8,333 + ₹8,334, totalling ₹30,000. Confirm due dates directly with the academy.</p></div></details>
<details class="faq-item" data-reveal="up"><summary>Is a certificate provided?<span>＋</span></summary><div><p>The academy provides a course certificate on successful completion of the integrated program. Ask the academy to confirm assessment and completion requirements.</p></div></details>'''
    s = s.replace('</div></section>', insert + '</div></section>', 1)
p.write_text(s, encoding="utf-8")

# Contact page enquiry form should reflect a single integrated course.
p = ROOT / "contact.html"
s = p.read_text(encoding="utf-8")
s = s.replace('<option>Professional Makeup Artistry</option><option>Skin &amp; Aesthetics</option><option>Hair Styling</option><option>Bridal Artistry</option><option>Mehendi</option><option>Beautician Training</option><option>40-Day Beauty &amp; Makeup Course</option><option>Not sure yet</option>',
'<option>40-Day Integrated Beauty &amp; Makeup Program</option><option>Makeup Artistry module</option><option>Skin &amp; Aesthetics module</option><option>Hair Styling module</option><option>Bridal Artistry module</option><option>Mehendi / beauty service enquiry</option><option>Not sure yet</option>')
s = s.replace("Course of interest", "Program or area of interest")
p.write_text(s, encoding="utf-8")

# Add basic local business metadata consistently for SEO.
schema = {
 "@context":"https://schema.org",
 "@type":"BeautySalon",
 "name":"Amreens Academy & Makeover Studio",
 "telephone":"+91 81234 10118",
 "address":{
   "@type":"PostalAddress",
   "streetAddress":"#23, Bharath Nagar, Ashwath Nagar, 2nd Stage, Thanisandra Main Road",
   "addressLocality":"Bengaluru",
   "addressRegion":"Karnataka",
   "postalCode":"560077",
   "addressCountry":"IN"
 },
 "sameAs":[ig]
}
schema_script = '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + '</script>'
for p in ROOT.glob("*.html"):
    s = p.read_text(encoding="utf-8")
    if 'application/ld+json' not in s:
        s = s.replace('</head>', '  ' + schema_script + '\n</head>', 1)
    p.write_text(s, encoding="utf-8")

print("Enhanced homepage, integrated course offer, FAQ, contact flow and SEO metadata.")
