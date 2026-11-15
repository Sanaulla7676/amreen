from pathlib import Path

ROOT = Path(__file__).resolve().parent

def replace_once(text, old, new, label):
    if old not in text:
        print("SKIP (not found):", label)
        return text
    print("PATCHED:", label)
    return text.replace(old, new, 1)

# Homepage: keep the existing two local videos and add the live public Instagram profile embed.
p = ROOT / "index.html"
s = p.read_text(encoding="utf-8")
s = replace_once(
    s,
    '<h1 id="hero-title">Creativity</h1>',
    '<h1 id="hero-title" aria-label="Creativity"><span class="hero-title-mask"><span class="hero-title-word">Creativity</span></span></h1>',
    "hero masked title entrance"
)
s = replace_once(
    s,
    '    <div class="films-footer"><span>MORE FROM THE STUDIO</span><a href="https://www.instagram.com/amreenkhanum60/" target="_blank" rel="noopener noreferrer">Follow @amreenkhanum60 <b>↗</b></a></div>',
    '''    <div class="films-footer"><span>MORE FROM THE STUDIO</span><a href="https://www.instagram.com/amreenkhanum60/" target="_blank" rel="noopener noreferrer">Follow @amreenkhanum60 <b>↗</b></a></div>
    <div class="instagram-live" data-reveal="up">
      <div class="instagram-live-copy">
        <span class="mini-label">LIVE FROM INSTAGRAM</span>
        <h3>More from Amreen's world.</h3>
        <p>Recent public posts and Reels from @amreenkhanum60, including makeup, mehendi, beautician and studio moments. The feed updates from the public Instagram profile.</p>
        <a class="button button-primary" href="https://www.instagram.com/amreenkhanum60/" target="_blank" rel="noopener noreferrer">Open Instagram <span>↗</span></a>
      </div>
      <div class="instagram-live-frame">
        <iframe title="Live public Instagram posts from Amreen Khanum" src="https://www.instagram.com/amreenkhanum60/embed/" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen></iframe>
      </div>
    </div>
    <p class="instagram-feed-fallback">Instagram may require visitors to open the profile directly in some browsers. <a href="https://www.instagram.com/amreenkhanum60/" target="_blank" rel="noopener noreferrer">View the profile ↗</a></p>''',
    "live Instagram grid after academy videos"
)
s = replace_once(
    s,
    '          <div class="program-count-wrap"><span class="program-count" data-count-up="45">0</span><small>DAYS · ONE INTEGRATED COURSE</small></div>\n',
    '',
    "remove duplicate static-side counter"
)
s = replace_once(
    s,
    '<div class="program-facts"><span>✓ Four learning areas</span><span>✓ Academy certificate</span></div>',
    '<div class="program-facts"><span>✓ Four learning areas</span><span>✓ Certificate on completion</span></div>',
    "certificate fact"
)
s = replace_once(
    s,
    '<div class="program-ribbon aria-hidden="true"></div>\n        <img class="program-presenter" src="assets/45-days-presenter.png" alt="Amreen\'s Academy team member presenting the 45 Days course sign" loading="lazy">',
    '''<div class="program-ribbon" aria-hidden="true"></div>
        <div class="program-presenter-wrap">
          <img class="program-presenter" src="assets/45-days-presenter.png" alt="Amreen's Academy team member holding the 45 Days sign" loading="lazy">
          <button class="animated-number-panel" type="button" aria-label="Replay the 45-day number animation">
            <span class="program-count" data-count-up="45" aria-live="off">0</span>
          </button>
          <span class="celebration-emoji" aria-hidden="true">🎉</span>
        </div>
        <div class="confetti-burst" aria-hidden="true"></div>''',
    "45-day number animated on sign with party burst"
)
# Remove the earlier local Instagram/video duplication folder from the final package; root assets below are the referenced optimized clips.
p.write_text(s, encoding="utf-8")

# Load the dormant campaign styles and the new motion layer on the homepage.
s = p.read_text(encoding="utf-8")
if 'css/campaign-enhancements.css' not in s:
    s = s.replace('  <link rel="stylesheet" href="css/motion.css">', '  <link rel="stylesheet" href="css/motion.css">\n  <link rel="stylesheet" href="css/campaign-enhancements.css">\n  <link rel="stylesheet" href="css/upgrade.css">', 1)
if 'js/upgrade.js' not in s:
    s = s.replace('  <script src="js/motion.js" defer></script>', '  <script src="js/motion.js" defer></script>\n  <script src="js/upgrade.js" defer></script>', 1)
p.write_text(s, encoding="utf-8")

# Add shared animation layer to all inner pages as well.
for p in ROOT.glob("*.html"):
    if p.name == "index.html":
        continue
    s = p.read_text(encoding="utf-8")
    if 'css/upgrade.css' not in s:
        s = s.replace('</head>', '  <link rel="stylesheet" href="css/upgrade.css">\n</head>', 1)
    if 'js/upgrade.js' not in s:
        s = s.replace('</body>', '  <script src="js/upgrade.js" defer></script>\n</body>', 1)
    p.write_text(s, encoding="utf-8")

# Payment terms: advertise the option, not a made-up payment calendar or exact instalment amounts.
p = ROOT / "45-day-course.html"
s = p.read_text(encoding="utf-8")
s = s.replace(
    'Three instalments are available: ₹8,333 + ₹8,333 + ₹8,334 (₹25,000 total). The academy provides a course certificate on successful completion. Confirm instalment due dates, batch timings, syllabus and kit requirements with the academy.',
    'A three-instalment payment option is available. The academy provides a course certificate on successful completion. Confirm the instalment schedule, batch timings, syllabus and kit requirements directly with the academy.'
)
s = s.replace(
    '<strong>₹8,333 <i>+</i> ₹8,333 <i>+</i> ₹8,334</strong><small>Total ₹25,000 · Confirm payment dates directly with the academy.</small>',
    '<strong>Three instalments available</strong><small>Total ₹25,000 · Confirm instalment amounts and payment dates directly with the academy.</small>'
)
p.write_text(s, encoding="utf-8")

# FAQ copy aligned with the single integrated 45-day course.
p = ROOT / "faqs.html"
s = p.read_text(encoding="utf-8")
s = s.replace(
    'The full course fee is ₹25,000. The academy also offers a three-instalment option: ₹8,333 + ₹8,333 + ₹8,334 (₹25,000 total). Confirm the payment dates and any applicable terms directly with the academy.',
    'The full course fee is ₹25,000. A three-instalment payment option is available. Confirm instalment amounts, due dates and any applicable terms directly with the academy.'
)
s = s.replace(
    'No such claim is published in the material reviewed. The 45-day duration belongs to the featured Beauty & Makeup Course; ask about the duration of each other pathway.',
    'The four areas shown on the website are included within one integrated 45-day Beauty & Makeup course: Professional Makeup Artistry, Skin & Aesthetics, Hair Styling and Bridal Artistry. They are not four separately priced courses.'
)
# Add a dedicated instalment FAQ if it is not already present.
if 'Can I pay in three instalments?' not in s:
    s = s.replace(
        '</div></details><details class="faq-item" data-reveal="up"><summary>Is a certificate included?',
        '</div></details><details class="faq-item" data-reveal="up"><summary>Can I pay in three instalments?<span>＋</span></summary><div><p>Yes. A three-instalment payment option is available for the ₹25,000 course. Confirm the instalment amounts and due dates directly with the academy.</p></div></details><details class="faq-item" data-reveal="up"><summary>Is a certificate included?',
        1
    )
p.write_text(s, encoding="utf-8")

# Courses page: make the one-course/four-areas relationship explicit on every module card.
p = ROOT / "courses.html"
s = p.read_text(encoding="utf-8")
s = s.replace('>Explore pathway <span>→</span>', '>Included module <span>→</span>')
s = s.replace(
    '<h3>Professional Makeup Artistry</h3>',
    '<span class="module-included">INCLUDED IN THE 45-DAY COURSE</span><h3>Professional Makeup Artistry</h3>'
)
s = s.replace(
    '<h3>Skin &amp; Aesthetics</h3>',
    '<span class="module-included">INCLUDED IN THE 45-DAY COURSE</span><h3>Skin &amp; Aesthetics</h3>'
)
s = s.replace(
    '<h3>Hair Styling</h3>',
    '<span class="module-included">INCLUDED IN THE 45-DAY COURSE</span><h3>Hair Styling</h3>'
)
s = s.replace(
    '<h3>Bridal Artistry</h3>',
    '<span class="module-included">INCLUDED IN THE 45-DAY COURSE</span><h3>Bridal Artistry</h3>'
)
p.write_text(s, encoding="utf-8")

# The detail pages are modules within the same bundled course, not separate paid enrolments.
for filename in ["professional-makeup.html","skin-aesthetics.html","hair-styling.html","bridal-artistry.html"]:
    p = ROOT / filename
    s = p.read_text(encoding="utf-8")
    if 'href="45-day-course.html"' not in s:
        s = s.replace(
            '</div></div>',
            '</div><a class="button button-primary module-cta" href="45-day-course.html">View the integrated 45-day course <span>→</span></a></div>',
            1
        )
    p.write_text(s, encoding="utf-8")

print("Homepage and offer patches complete.")
