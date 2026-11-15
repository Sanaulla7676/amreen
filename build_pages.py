from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
PHONE = "8123410118"
DISPLAY_PHONE = "+91 81234 10118"
ADDRESS = "#23, Bharath Nagar, Ashwath Nagar, 2nd Stage, Thanisandra Main Road, Bengaluru, Karnataka 560077"
IG = "https://www.instagram.com/amreenkhanum60/"
MAP = "https://www.google.com/maps/search/?api=1&query=Amreens%20academy%20%26%20makeover%20studio&query_place_id=ChIJb3bteaUXrjsRIJOmc2EQrmY"
WA = "https://wa.me/91" + PHONE
NAV = [
    ("Home", "index.html"),
    ("About", "about.html"),
    ("Courses", "courses.html"),
    ("Faculty", "faculty.html"),
    ("Student Success", "student-success.html"),
    ("Blog", "blog.html"),
    ("FAQs", "faqs.html"),
    ("Contact", "contact.html"),
]

def header():
    links = "\n".join(f'<a href="{url}">{label}</a>' for label, url in NAV)
    return f'''<div class="scroll-progress" aria-hidden="true"><span></span></div>
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="index.html" aria-label="Amreen's Academy home">
      <span class="brand-word">AMREEN<span class="brand-plus">+</span></span>
      <span class="brand-sub">A C A D E M Y</span>
    </a>
    <span class="brand-divider" aria-hidden="true"></span>
    <p class="brand-tagline">PROFESSIONAL<br>BEAUTY &amp; MAKEUP<br>EDUCATION</p>
    <button class="menu-toggle" type="button" aria-label="Open navigation" aria-expanded="false" aria-controls="primary-nav"><span></span><span></span><span></span></button>
    <nav class="primary-nav" id="primary-nav" aria-label="Main navigation">{links}</nav>
    <div class="header-socials"><a href="{IG}" target="_blank" rel="noopener noreferrer" aria-label="Instagram">◎</a><a href="{WA}" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp">◉</a></div>
    <a class="button button-primary header-cta" href="contact.html#enquiry">Enquire Now <span>→</span></a>
  </div>
</header>'''

def footer():
    return f'''<footer class="site-footer">
  <div class="footer-inner">
    <a class="brand footer-brand" href="index.html"><span class="brand-word">AMREEN<span class="brand-plus">+</span></span><span class="brand-sub">A C A D E M Y</span></a>
    <span class="footer-divider" aria-hidden="true"></span>
    <p class="footer-tagline">PROFESSIONAL<br>BEAUTY &amp; MAKEUP<br>EDUCATION</p>
    <div class="footer-links"><strong>Explore</strong><a href="about.html">About</a><a href="courses.html">Courses</a><a href="faculty.html">Faculty</a></div>
    <div class="footer-links"><strong>Discover</strong><a href="student-success.html">Student Success</a><a href="blog.html">Blog</a><a href="faqs.html">FAQs</a></div>
    <div class="footer-links"><strong>Get in touch</strong><a href="contact.html">Contact</a><a href="tel:{PHONE}">{DISPLAY_PHONE}</a><a href="{IG}" target="_blank" rel="noopener noreferrer">Instagram</a></div>
    <div class="footer-social"><strong>Visit the Academy</strong><p class="footer-address">{ADDRESS}</p><a class="footer-map-link" href="{MAP}" target="_blank" rel="noopener noreferrer">Open in Google Maps →</a></div>
  </div>
  <p class="footer-bottom">© <span class="current-year"></span> Amreen's Academy. All rights reserved.</p>
</footer>
<a class="floating-contact" href="{WA}" target="_blank" rel="noopener noreferrer" aria-label="Chat with Amreen's Academy on WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.2 11.7a8.2 8.2 0 0 1-12.1 7.2L3 20l1.2-4.9a8.2 8.2 0 1 1 16-3.4Z"/><path d="M8.1 7.9c.2-.5.5-.5.8-.5h.5c.2 0 .4.1.5.4l.7 1.7c.1.2.1.4 0 .6l-.5.6c-.2.2-.2.4 0 .6.4.7 1 1.3 1.7 1.7.2.1.4.1.6-.1l.7-.8c.2-.2.4-.2.6-.1l1.6.8c.2.1.4.3.4.5 0 .4-.2 1.1-.6 1.4-.4.4-1 .6-1.6.5-1-.1-2.4-.7-3.7-1.9-1.1-1-2-2.3-2.2-3.3-.2-.8.1-1.5.5-2.1Z"/></svg></a>'''

def page(title, description, kicker, heading, intro, image, content, active):
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#07182f">
  <meta name="description" content="{escape(description, quote=True)}">
  <title>{escape(title)}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/styles.css">
  <link rel="stylesheet" href="css/motion.css">
  <link rel="stylesheet" href="css/pages.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  {header()}
  <main id="main">
    <section class="page-hero" aria-labelledby="page-title">
      <div class="page-hero__glow"></div>
      <div class="page-hero__copy" data-reveal="left">
        <p class="page-kicker">{kicker}<span></span></p>
        <h1 id="page-title">{heading}</h1>
        <p>{intro}</p>
        <div class="page-hero__actions"><a class="button button-primary" href="contact.html#enquiry">Enquire Now <span>→</span></a><a class="text-link" href="courses.html">Explore courses <span>↗</span></a></div>
      </div>
      <div class="page-hero__visual" data-reveal="right">
        <img src="{image}" alt="Amreen's Academy beauty education and training visual">
        <span class="page-hero__visual-ring"></span>
      </div>
      <div class="page-hero__footer"><span>AMREEN'S ACADEMY</span><span>BEAUTY • MAKEUP • MEHENDI</span></div>
    </section>
    {content}
  </main>
  {footer()}
  <script src="js/site.js" defer></script>
  <script src="js/motion.js" defer></script>
</body>
</html>'''
    return html

def section(title, label, body, cls="surface-light"):
    return f'''<section class="content-section {cls}">
  <div class="page-container">
    <div class="section-intro" data-reveal="up"><p class="eyebrow">{label} <span></span></p><h2>{title}</h2></div>
    {body}
  </div>
</section>'''

def cta(title, text="Talk to the academy about the right learning path and the latest batch details."):
    return f'''<section class="page-cta" data-reveal="scale"><div><p class="eyebrow">YOUR NEXT CHAPTER</p><h2>{title}</h2><p>{text}</p></div><a class="button button-primary" href="contact.html#enquiry">Enquire Now <span>→</span></a></section>'''

pages = {}

# About
about_body = section("Beauty education shaped by creativity and practice", "ABOUT THE ACADEMY", f'''
<div class="split-feature">
  <div class="split-feature__image" data-reveal="left"><img src="assets/academy-studio.jpg" alt="Beauty training studio with illuminated makeup mirrors"></div>
  <div class="split-feature__copy" data-reveal="right"><h3>A space to learn the craft with confidence.</h3><p>Amreen's Academy brings together beauty, makeup, mehendi and beautician learning in a focused studio environment. The academy's public profile describes its work around makeup, mehendi and beautician services.</p><p>The website's course pathways also introduce professional makeup artistry, skin and aesthetics, hair styling and bridal artistry.</p><a class="arrow-link" href="courses.html">Explore the course pathways <span>→</span></a></div>
</div>
<div class="value-grid" data-stagger>
  <article class="value-card"><span>01</span><h3>Creativity</h3><p>Build an eye for detail, balance and personal expression through beauty work.</p></article>
  <article class="value-card"><span>02</span><h3>Practice</h3><p>Move beyond watching techniques. Ask about guided demonstrations and opportunities to practise.</p></article>
  <article class="value-card"><span>03</span><h3>Confidence</h3><p>Develop a thoughtful approach to your craft, your clients and your next steps.</p></article>
</div>''')
about_body += section("A local academy with a personal point of contact", "FIND THE STUDIO", f'''
<div class="contact-ribbon"><div><span class="mini-label">THANISANDRA · BENGALURU</span><h3>Visit Amreen's Academy</h3><p>{ADDRESS}</p><p><a href="tel:{PHONE}">{DISPLAY_PHONE}</a> · <a href="{IG}" target="_blank" rel="noopener noreferrer">Instagram profile ↗</a></p></div><a class="button button-primary" href="{MAP}" target="_blank" rel="noopener noreferrer">Get directions <span>↗</span></a></div>''', "surface-dark")
about_body += cta("Let your creativity become your craft.")
pages["about.html"] = page("About Amreen's Academy | Beauty & Makeup Education", "Discover Amreen's Academy in Thanisandra, Bengaluru: makeup, mehendi and beautician learning in a creative studio environment.", "ABOUT US", "Where creativity meets the beauty craft.", "A learning space for people who want to explore makeup, mehendi and professional beauty skills.", "assets/hero-seated-face-swapped.png", about_body, "about")

# Courses
course_cards = [
    ("Professional Makeup Artistry","Learn about the artistry behind a polished makeup look, from preparation to finish.","assets/course-makeup.jpg","professional-makeup.html","01"),
    ("Skin & Aesthetics","Explore skin-focused beauty learning and professional care fundamentals.","assets/course-skin.jpg","skin-aesthetics.html","02"),
    ("Hair Styling","Discover styling techniques, structure and finishing for everyday and occasion looks.","assets/course-hair.jpg","hair-styling.html","03"),
    ("Bridal Artistry","Explore the considered details that bring a bridal look together.","assets/course-bridal.jpg","bridal-artistry.html","04"),
]
course_grid = '<div class="page-course-grid" data-stagger>' + "".join(
    f'''<a class="page-course-card" href="{url}"><div class="page-course-card__image"><img src="{img}" alt="{name}"><span>{num}</span></div><div class="page-course-card__copy"><h3>{name}</h3><p>{desc}</p><b>Explore pathway <span>→</span></b></div></a>'''
    for name,desc,img,url,num in course_cards) + '</div>'
courses_body = section("Choose the direction that inspires you", "COURSE PATHWAYS", f'''<p class="section-lead">The academy homepage highlights four core beauty pathways. Course details, current batches, fees and the latest syllabus should be confirmed directly with the academy.</p>{course_grid}''')
courses_body += section("A focused 45-day learning option", "FEATURED PROGRAM", f'''
<div class="featured-course">
  <div class="featured-course__copy"><span class="mini-label">45-DAY PROGRAM</span><h3>Beauty &amp; Makeup Course</h3><p>A focused, practical program designed to build your skills and confidence in the beauty industry. Ask the academy for the current syllabus, batch dates and fee details.</p><a class="button button-primary" href="45-day-course.html">View 45-day course <span>→</span></a></div>
  <img src="assets/45-days-presenter.png" alt="Amreen's Academy presenter holding the 45 Days sign">
</div>''', "surface-dark")
courses_body += cta("Find the course that fits your goals.", "Share what you want to learn and the academy can guide you through available options.")
pages["courses.html"] = page("Beauty Courses | Amreen's Academy Bengaluru", "Explore professional makeup artistry, skin and aesthetics, hair styling, bridal artistry and the 45-day beauty and makeup course at Amreen's Academy.", "OUR COURSES", "Choose your craft. Shape your next chapter.", "Beauty and makeup learning pathways for curious beginners, working professionals and aspiring artists.", "assets/course-makeup.jpg", courses_body, "courses")

# Faculty
faculty_body = section("A learning experience built around demonstration and practice", "HOW WE TEACH", f'''
<div class="teaching-grid">
  <article class="teaching-card" data-reveal="up"><span class="teaching-icon">01</span><h3>Understand the technique</h3><p>Begin with the purpose behind a step, the tools involved and the finish you are aiming to achieve.</p></article>
  <article class="teaching-card" data-reveal="up"><span class="teaching-icon">02</span><h3>Watch the demonstration</h3><p>Observe the sequence, details and choices that shape a professional beauty result.</p></article>
  <article class="teaching-card" data-reveal="up"><span class="teaching-icon">03</span><h3>Build through practice</h3><p>Use practice to improve control, consistency and confidence in your own work.</p></article>
</div>
<div class="mentor-feature"><img src="assets/career-mentor-folded-arms.png" alt="Amreen's Academy maroon-uniform character portrait"><div><span class="mini-label">GUIDANCE &amp; SUPPORT</span><h3>Good technique grows with thoughtful guidance.</h3><p>Ask about the trainers for your selected course, their experience, the amount of practice included and how feedback is provided during a batch.</p><a class="arrow-link" href="contact.html#enquiry">Ask about faculty and batches <span>→</span></a></div></div>''')
faculty_body += section("Questions worth asking before you enrol", "MAKE AN INFORMED CHOICE", f'''
<div class="question-grid"><div><h3>Who will teach my course?</h3><p>Ask for the trainer's profile and relevant professional experience for the selected specialisation.</p></div><div><h3>How much practice is included?</h3><p>Ask how demonstrations, practice sessions and feedback are arranged during the batch.</p></div><div><h3>What should I bring?</h3><p>Confirm the kit, materials and any model or product requirements before the first class.</p></div></div>''', "surface-dark")
faculty_body += cta("Meet the academy and discuss your learning goals.")
pages["faculty.html"] = page("Faculty & Learning Approach | Amreen's Academy", "Learn about the practice-led teaching approach and what to ask about trainers and guidance at Amreen's Academy.", "FACULTY & MENTORSHIP", "Guidance behind every skill.", "A thoughtful learning journey starts with clear demonstrations, practical work and useful feedback.", "assets/career-mentor-folded-arms.png", faculty_body, "faculty")

# Student success / gallery
gallery = "".join(f'<figure class="portfolio-item" data-reveal="scale"><img src="assets/student-work-{i:02d}.jpg" alt="{alt}"><figcaption>{caption}</figcaption></figure>' for i,alt,caption in [
    (1,"Makeup practice look from the academy homepage gallery","Makeup practice"),
    (2,"Hair styling practice look from the academy homepage gallery","Hair styling"),
    (3,"Makeup application practice look from the academy homepage gallery","Makeup application"),
    (4,"Bridal hairstyle practice look from the academy homepage gallery","Bridal hair"),
])
students_body = section("Practice, detail and creative expression", "STUDENT WORK & PRACTICE", f'''
<p class="section-lead">Explore the work featured on the academy's homepage and social profile. Gallery visuals are presented as examples of beauty practice; enquire directly for current student portfolios and batch work.</p>
<div class="portfolio-grid">{gallery}</div>
<div class="social-follow"><div><span class="mini-label">FOLLOW THE LATEST WORK</span><h3>More looks, lessons and studio moments.</h3><p>See the public Instagram profile for current posts and updates.</p></div><a class="button button-primary" href="{IG}" target="_blank" rel="noopener noreferrer">View Instagram <span>↗</span></a></div>''')
students_body += cta("Build your own body of work.", "Ask about practical sessions, portfolio opportunities and the current course pathway.")
pages["student-success.html"] = page("Student Work & Practice | Amreen's Academy", "Browse beauty and hair practice visuals from Amreen's Academy and follow its public Instagram profile for current updates.", "STUDENT SUCCESS", "Every skill starts with practice.", "A growing craft is built one detail, one technique and one finished look at a time.", "assets/student-work-03.jpg", students_body, "student-success")

# Blog - articles are editorial educational content, not attributed to academy staff
articles = [
    ("01","MAKEUP","Build a makeup base with intention","A polished base starts with preparation, an understanding of skin finish and careful product placement. Work in light layers, blend transitions and check the result in natural light.","Preparation · layers · finish"),
    ("02","BRIDAL","The details that shape a bridal look","A bridal look is a coordinated whole. Consider the outfit, jewellery, lighting, event schedule and the balance between makeup and hairstyling before choosing the final direction.","Coordination · balance · longevity"),
    ("03","HAIR","Think about structure before the final style","Sectioning, direction and support are the foundation of a neat hairstyle. Plan the silhouette first, then refine texture and finishing details.","Sectioning · shape · finishing"),
]
article_html = '<div class="article-grid">' + "".join(
    f'''<details class="article-card" data-reveal="up"><summary><span class="article-number">{n}</span><span class="article-category">{cat}</span><h3>{title}</h3><p>Open this note for a few practical considerations to explore.</p><b>Read note <span>＋</span></b></summary><div class="article-expanded"><p>{body}</p><small>{tags}</small></div></details>'''
    for n,cat,title,body,tags in articles) + '</div>'
blog_body = section("Ideas for curious beauty professionals", "THE ACADEMY JOURNAL", f'''<p class="section-lead">Short educational notes for anyone exploring makeup, bridal beauty and hairstyling. These are general learning articles, not a published academy syllabus.</p>{article_html}''')
blog_body += cta("Want to learn these skills hands-on?")
pages["blog.html"] = page("Beauty Journal | Amreen's Academy", "Read practical beauty education notes on makeup preparation, bridal look planning and hairstyling fundamentals.", "THE JOURNAL", "Ideas that keep your creativity moving.", "A small collection of practical beauty notes for your next learning step.", "assets/course-bridal.jpg", blog_body, "blog")

# FAQs
faq_items = [
    ("What training areas are associated with Amreen's Academy?","The academy's Instagram bio describes makeup, mehendi and beautician services. Its homepage also presents Professional Makeup Artistry, Skin & Aesthetics, Hair Styling and Bridal Artistry."),
    ("Does the academy offer a 45-day course?","The academy homepage features a 45-Day Beauty & Makeup Course. Contact the academy to confirm the current batch, syllabus, schedule and availability."),
    ("What are the fees and batch dates?","Current fees, batch dates and course-specific schedules were not publicly confirmed in the information reviewed. Contact the academy for the latest details."),
    ("Do all courses run for 45 days?","No such claim is published in the material reviewed. The 45-day duration belongs to the featured Beauty & Makeup Course; ask about the duration of each other pathway."),
    ("Is a certificate included?","Certificate details were not confirmed in the public information reviewed. Ask the academy what certificate, if any, is provided for your selected course."),
    ("Where is the academy located?","The Instagram profile lists #23, Bharath Nagar, Ashwath Nagar, 2nd Stage, Thanisandra Main Road, Bengaluru 560077. Open the Google Business listing for directions."),
    ("How can I contact the academy?","Call or WhatsApp +91 81234 10118, or send a message through the Instagram profile."),
    ("Can I visit before enrolling?","Contact the academy first to arrange a visit and confirm availability.")
]
faq_markup = '<div class="faq-list">' + "".join(f'<details class="faq-item" data-reveal="up"><summary>{q}<span>＋</span></summary><div><p>{a}</p></div></details>' for q,a in faq_items) + '</div>'
faq_body = section("Clear answers before you take the next step", "FREQUENTLY ASKED QUESTIONS", faq_markup)
faq_body += cta("Still deciding? Let's talk.", "Ask directly about the latest course details and what to expect before joining.")
pages["faqs.html"] = page("FAQs | Amreen's Academy Bengaluru", "Answers about course categories, the 45-day beauty and makeup course, fees, batches, contact details and academy location.", "HELP & GUIDANCE", "Questions are part of a good beginning.", "Here are the details that are publicly available, plus the questions worth confirming directly.", "assets/academy-studio.jpg", faq_body, "faqs")

# Contact
contact_body = section("Reach the academy directly", "CONTACT & VISIT", f'''
<div class="contact-layout">
  <div class="contact-panel">
    <span class="mini-label">CALL OR WHATSAPP</span><h3>{DISPLAY_PHONE}</h3><p>Use the number listed in the public Instagram profile to ask about course information, current batches and studio visits.</p><div class="contact-actions"><a class="button button-primary" href="{WA}" target="_blank" rel="noopener noreferrer">WhatsApp the Academy <span>↗</span></a><a class="text-link" href="tel:{PHONE}">Call now ↗</a></div>
    <hr><span class="mini-label">STUDIO ADDRESS</span><p class="contact-address">{ADDRESS}</p><a class="arrow-link" href="{MAP}" target="_blank" rel="noopener noreferrer">Open Google Maps <span>↗</span></a>
  </div>
  <div class="map-panel"><div class="map-panel__top"><span class="map-pin">⌖</span><div><strong>Amreens Academy &amp; Makeover Studio</strong><small>Thanisandra · Bengaluru</small></div></div><iframe title="Map showing Amreens Academy and Makeover Studio in Thanisandra, Bengaluru" src="https://www.google.com/maps?q=Amreens%20academy%20%26%20makeover%20studio%2C%20Thanisandra%2C%20Bengaluru&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe><a href="{MAP}" target="_blank" rel="noopener noreferrer">Open listing and directions ↗</a></div>
</div>''')
contact_body += section("A public Google listing", "LOCAL PRESENCE", f'''
<div class="review-snapshot"><div class="review-rating"><strong>5.0</strong><span>★★★★★</span><small>Google Business Profile snapshot</small></div><div><h3>3 public reviews</h3><p>The listing currently shows a 5.0 rating based on three reviews. This is a small review sample; view the live listing for the latest details.</p><a class="arrow-link" href="{MAP}" target="_blank" rel="noopener noreferrer">View Google listing <span>↗</span></a></div></div>''', "surface-dark")
contact_body += f'''<section class="content-section surface-light" id="enquiry"><div class="page-container"><div class="section-intro"><p class="eyebrow">SEND AN ENQUIRY <span></span></p><h2>Tell us what you'd like to learn.</h2><p class="section-lead">This form opens WhatsApp with your message prepared. It does not store your information on this website.</p></div>
<form class="enquiry-form" data-whatsapp-form>
<label>Your name<input name="name" autocomplete="name" required placeholder="Full name"></label>
<label>Phone number<input name="phone" autocomplete="tel" inputmode="tel" required placeholder="Mobile number"></label>
<label>Course of interest<select name="course" required><option value="">Select a course</option><option>Professional Makeup Artistry</option><option>Skin &amp; Aesthetics</option><option>Hair Styling</option><option>Bridal Artistry</option><option>Mehendi</option><option>Beautician Training</option><option>45-Day Beauty &amp; Makeup Course</option><option>Not sure yet</option></select></label>
<label>Message<textarea name="message" rows="4" placeholder="Tell us what you want to know"></textarea></label>
<button class="button button-primary" type="submit">Continue to WhatsApp <span>→</span></button>
<p class="form-status" role="status"></p></form></div></section>'''
pages["contact.html"] = page("Contact Amreen's Academy | Thanisandra, Bengaluru", "Contact Amreen's Academy in Thanisandra, Bengaluru by phone, WhatsApp or Instagram. View the Google Maps listing and send a course enquiry.", "GET IN TOUCH", "Let's start a conversation.", "Ask about courses, current batches or arranging a visit to the academy in Thanisandra.", "assets/academy-studio.jpg", contact_body, "contact")

# 45-day program
day_body = section("A focused program for your next step", "45-DAY BEAUTY & MAKEUP COURSE", f'''
<div class="program-detail">
  <div class="program-detail__copy"><span class="mini-label">45 DAYS · BEAUTY &amp; MAKEUP</span><h3>Learn with focus. Practise with purpose.</h3><p>The academy homepage describes this as a focused, practical program designed to build skills and confidence in the beauty industry.</p><p>For the latest course outline, class schedule, eligibility, fee and materials list, contact the academy directly before enrolling.</p><a class="button button-primary" href="contact.html#enquiry">Ask about this course <span>→</span></a></div>
  <img src="assets/45-days-presenter.png" alt="Amreen's Academy 45 Days course presenter">
</div>
<div class="three-points" data-stagger><div><span>01</span><h4>Request the syllabus</h4><p>Ask for the current module list and practical learning plan.</p></div><div><span>02</span><h4>Confirm the batch</h4><p>Check upcoming dates, class timings and available seats.</p></div><div><span>03</span><h4>Prepare to begin</h4><p>Confirm the kit, materials and anything to bring to class.</p></div></div>''')
day_body += cta("Ready to ask about the 45-day course?")
pages["45-day-course.html"] = page("45-Day Beauty & Makeup Course | Amreen's Academy", "Details for Amreen's Academy 45-Day Beauty & Makeup Course. Contact the academy to confirm the current syllabus, fee and batch dates.", "FEATURED PROGRAM", "45 days to explore your beauty craft.", "A practical Beauty & Makeup program designed to build skills and confidence.", "assets/45-days-presenter.png", day_body, "courses")

# Course detail pages
detail_data = [
    ("professional-makeup.html","Professional Makeup Artistry","MAKEUP ARTISTRY","assets/course-makeup.jpg","Explore professional makeup artistry from preparation through the finished look.","A course pathway for learners interested in the craft, detail and discipline behind professional makeup.","Skin preparation and finish","Colour and product choices","Application and blending","Looks for different occasions"),
    ("skin-aesthetics.html","Skin & Aesthetics","SKIN & AESTHETICS","assets/course-skin.jpg","Explore skin-focused beauty learning and thoughtful client care.","A pathway for learners interested in skin, beauty treatments and the details that support a careful, considered service.","Skin types and preparation","Product and tool awareness","Treatment-room hygiene","Client care fundamentals"),
    ("hair-styling.html","Hair Styling","HAIR STYLING","assets/course-hair.jpg","Build an eye for shape, structure and a polished finish.","Explore the foundations of hairstyling for everyday, occasion and bridal looks. Confirm the current syllabus with the academy.","Hair preparation and sectioning","Shape and structure","Styling and finishing","Occasion and bridal styling"),
    ("bridal-artistry.html","Bridal Artistry","BRIDAL ARTISTRY","assets/course-bridal.jpg","Bring makeup, hair and occasion details together with intention.","A pathway for learners drawn to the coordination and detail involved in bridal beauty. Ask the academy which techniques are covered in the current batch.","Bridal look planning","Complexion and eye details","Hair and overall coordination","Finishing and presentation"),
]
for filename,name,kicker,image,headline,description,*topics in detail_data:
    li = "".join(f'<li><span>✦</span>{topic}</li>' for topic in topics)
    body = section("Explore the focus of this pathway", "COURSE OVERVIEW", f'''
<div class="course-detail-layout"><div><h3>{headline}</h3><p>{description}</p><p class="quiet-note">The points below are indicative learning themes for this specialisation, not a confirmed published syllabus. Ask the academy for the current module list, duration, fee and batch availability.</p></div><div class="topic-panel"><span class="mini-label">AREAS TO DISCUSS</span><ul>{li}</ul></div></div>''')
    body += section("Make sure the course fits your goals", "BEFORE YOU ENROL", '''
<div class="question-grid"><div><h3>Ask about the syllabus</h3><p>Confirm exactly which techniques and practical sessions are included.</p></div><div><h3>Check the class format</h3><p>Ask about batch size, trainer support, practice models and materials.</p></div><div><h3>Understand the outcome</h3><p>Ask what you should be able to do by the end of the course.</p></div></div>''', "surface-dark")
    body += cta("Want to know if this course is right for you?")
    pages[filename] = page(f"{name} Course | Amreen's Academy", f"Explore the {name} pathway at Amreen's Academy in Thanisandra, Bengaluru. Contact the academy for the current syllabus and batch details.", kicker, name + ".", headline, image, body, "courses")

for filename, html in pages.items():
    (ROOT / filename).write_text(html, encoding="utf-8")
print("Generated pages:")
for filename in pages:
    print(" -", filename)
