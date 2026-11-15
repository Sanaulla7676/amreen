from pathlib import Path
import re

root=Path(__file__).resolve().parent
p=root/"index.html"
html=p.read_text(encoding="utf-8-sig")

def replace_balanced_section(source, marker, replacement):
    start=source.find(marker)
    if start<0:
        raise SystemExit("Section marker not found: "+marker)
    token=re.compile(r"</?section\b[^>]*>",re.I)
    depth=0
    end=None
    for m in token.finditer(source,start):
        if m.group(0).lower().startswith("</section"):
            depth-=1
            if depth==0:
                end=m.end()
                break
        else:
            depth+=1
    if end is None:
        raise SystemExit("Could not find closing section for: "+marker)
    return source[:start]+replacement+source[end:]

courses=r'''<section class="courses-section light-section" id="courses" aria-labelledby="courses-title">
  <div class="section-container">
    <div class="section-heading courses-heading" data-reveal="up">
      <div>
        <p class="eyebrow">THE 45-DAY INTEGRATED PROGRAM <span></span></p>
        <h2 id="courses-title">Explore Our <em>Beauty Courses</em></h2>
        <p class="courses-intro">Four connected learning areas, brought together in one Beauty &amp; Makeup program. Explore what each pathway focuses on.</p>
      </div>
      <a class="courses-heading-link" href="45-day-course.html">View the 45-day program <span aria-hidden="true">↗</span></a>
    </div>

    <div class="course-grid course-grid-expanded" id="course-grid">
      <a class="course-card course-card-expanded" href="professional-makeup.html" aria-label="Explore Professional Makeup Artistry, one learning area in the 45-day program">
        <div class="course-card-media">
          <img src="assets/course-makeup.jpg" alt="Professional bridal makeup artistry" loading="lazy" decoding="async">
          <span class="course-card-index">01</span>
          <span class="course-card-media-caption">MAKEUP ARTISTRY</span>
        </div>
        <div class="course-card-body">
          <span class="course-card-kicker">LEARNING AREA 01</span>
          <h3>Professional Makeup Artistry</h3>
          <p>Explore the craft of makeup from preparation through the finished look, with learning themes that include:</p>
          <ul>
            <li>Skin preparation and finish</li>
            <li>Colour and product choices</li>
            <li>Application and blending</li>
            <li>Looks for different occasions</li>
          </ul>
          <span class="course-card-link">Explore learning themes <b aria-hidden="true">↗</b></span>
        </div>
      </a>

      <a class="course-card course-card-expanded" href="skin-aesthetics.html" aria-label="Explore Skin and Aesthetics, one learning area in the 45-day program">
        <div class="course-card-media">
          <img src="assets/course-skin.jpg" alt="Skin and aesthetics facial treatment practice" loading="lazy" decoding="async">
          <span class="course-card-index">02</span>
          <span class="course-card-media-caption">SKIN &amp; AESTHETICS</span>
        </div>
        <div class="course-card-body">
          <span class="course-card-kicker">LEARNING AREA 02</span>
          <h3>Skin &amp; Aesthetics</h3>
          <p>Build awareness of skin-focused beauty learning and thoughtful client care through themes such as:</p>
          <ul>
            <li>Skin types and preparation</li>
            <li>Product and tool awareness</li>
            <li>Treatment-room hygiene</li>
            <li>Client care fundamentals</li>
          </ul>
          <span class="course-card-link">Explore learning themes <b aria-hidden="true">↗</b></span>
        </div>
      </a>

      <a class="course-card course-card-expanded" href="hair-styling.html" aria-label="Explore Hair Styling, one learning area in the 45-day program">
        <div class="course-card-media">
          <img src="assets/course-hair.jpg" alt="Professional hair styling and bridal updo" loading="lazy" decoding="async">
          <span class="course-card-index">03</span>
          <span class="course-card-media-caption">HAIR STYLING</span>
        </div>
        <div class="course-card-body">
          <span class="course-card-kicker">LEARNING AREA 03</span>
          <h3>Hair Styling</h3>
          <p>Explore the foundations of hairstyling for everyday, occasion and bridal looks, including:</p>
          <ul>
            <li>Hair preparation and sectioning</li>
            <li>Shape and structure</li>
            <li>Styling and finishing</li>
            <li>Occasion and bridal styling</li>
          </ul>
          <span class="course-card-link">Explore learning themes <b aria-hidden="true">↗</b></span>
        </div>
      </a>

      <a class="course-card course-card-expanded" href="bridal-artistry.html" aria-label="Explore Bridal Artistry, one learning area in the 45-day program">
        <div class="course-card-media">
          <img src="assets/course-bridal.jpg" alt="Bridal eye makeup artistry" loading="lazy" decoding="async">
          <span class="course-card-index">04</span>
          <span class="course-card-media-caption">BRIDAL ARTISTRY</span>
        </div>
        <div class="course-card-body">
          <span class="course-card-kicker">LEARNING AREA 04</span>
          <h3>Bridal Artistry</h3>
          <p>Bring makeup, hair and occasion details together with intention, with learning themes around:</p>
          <ul>
            <li>Bridal look planning</li>
            <li>Complexion and eye details</li>
            <li>Hair and overall coordination</li>
            <li>Finishing and presentation</li>
          </ul>
          <span class="course-card-link">Explore learning themes <b aria-hidden="true">↗</b></span>
        </div>
      </a>
    </div>

    <div class="course-program-note" data-reveal="scale">
      <div class="course-program-note-copy">
        <span class="course-program-note-kicker">ONE INTEGRATED COURSE</span>
        <h3>Four learning areas. One 45-day journey.</h3>
        <p>These are included learning areas within the same Beauty &amp; Makeup program, not four separate paid enrolments. The academy certificate is provided on successful completion.</p>
      </div>
      <div class="course-program-note-metrics">
        <div><strong>45</strong><span>DAYS</span></div>
        <div><strong>₹25,000</strong><span>FULL PROGRAM FEE</span></div>
        <div><strong>3</strong><span>INSTALMENTS AVAILABLE</span></div>
      </div>
      <a class="button button-primary course-program-note-cta" href="45-day-course.html">Explore the full program <span aria-hidden="true">→</span></a>
    </div>
  </div>
  <div class="fine-wave" aria-hidden="true"></div>
</section>'''

why=r'''<section class="why-section light-section" id="why-choose" aria-labelledby="why-title">
  <div class="section-container">
    <div class="why-heading" data-reveal="up">
      <p class="eyebrow">THE AMREEN'S ACADEMY APPROACH <span></span></p>
      <h2 id="why-title">Why Choose <em>Amreen's Academy?</em></h2>
      <p>Learn with a focus on practical technique, thoughtful service and the four connected areas of the integrated Beauty &amp; Makeup program.</p>
    </div>
    <div class="why-grid">
      <article class="why-item" data-reveal="up">
        <span class="why-item-icon" aria-hidden="true">
          <svg viewBox="0 0 48 48"><path d="M6 17 24 7l18 10-18 10L6 17Z M12 21v10c7 7 17 7 24 0V21 M42 18v14"/></svg>
        </span>
        <span class="why-item-number">01</span>
        <h3>Practical, Hands-on Learning</h3>
        <p>Build technique through guided practice and attention to preparation, application, detail and finish.</p>
      </article>

      <article class="why-item" data-reveal="up">
        <span class="why-item-icon" aria-hidden="true">
          <svg viewBox="0 0 48 48"><circle cx="24" cy="13" r="7"/><circle cx="9" cy="20" r="5"/><circle cx="39" cy="20" r="5"/><path d="M10 41v-4a14 14 0 0 1 28 0v4H10Z M2 40v-4a8 8 0 0 1 8-8 M46 40v-4a8 8 0 0 0-8-8"/></svg>
        </span>
        <span class="why-item-number">02</span>
        <h3>Four Learning Areas Together</h3>
        <p>Makeup Artistry, Skin &amp; Aesthetics, Hair Styling and Bridal Artistry are included in one 45-day program.</p>
      </article>

      <article class="why-item" data-reveal="up">
        <span class="why-item-icon" aria-hidden="true">
          <svg viewBox="0 0 48 48"><path d="M24 5 29 17l13 2-9.5 9.2 2.2 13L24 35l-10.7 6.2 2.2-13L6 19l13-2 5-12Z"/><path d="M17 24h14"/></svg>
        </span>
        <span class="why-item-number">03</span>
        <h3>Trainer Guidance</h3>
        <p>Get guidance as you develop technique, make product choices and build confidence in your work.</p>
      </article>

      <article class="why-item" data-reveal="up">
        <span class="why-item-icon" aria-hidden="true">
          <svg viewBox="0 0 48 48"><path d="M8 9h32v25H8z M14 39h20 M24 34v5 M16 17h16 M16 23h12 M16 29h8"/></svg>
        </span>
        <span class="why-item-number">04</span>
        <h3>Care and Hygiene Fundamentals</h3>
        <p>Explore skin preparation, product and tool awareness, treatment-room hygiene and thoughtful client care.</p>
      </article>

      <article class="why-item" data-reveal="up">
        <span class="why-item-icon" aria-hidden="true">
          <svg viewBox="0 0 48 48"><path d="M12 7h19l7 7v27H12z M31 7v8h7 M18 23h14 M18 29h14 M18 35h9"/></svg>
        </span>
        <span class="why-item-number">05</span>
        <h3>Academy Certificate</h3>
        <p>The integrated program includes an academy certificate on successful completion.</p>
      </article>

      <article class="why-item" data-reveal="up">
        <span class="why-item-icon" aria-hidden="true">
          <svg viewBox="0 0 48 48"><path d="M7 39V9 M7 39h35 M13 32l8-9 7 4 11-15 M34 12h5v5"/></svg>
        </span>
        <span class="why-item-number">06</span>
        <h3>Career-focused Foundations</h3>
        <p>Build a foundation across occasion looks, styling, finishing and professional presentation.</p>
      </article>
    </div>
  </div>
  <span class="why-motion-orb why-motion-orb-one" aria-hidden="true"></span>
  <span class="why-motion-orb why-motion-orb-two" aria-hidden="true"></span>
</section>'''

html=replace_balanced_section(html,'<section class="courses-section',courses)
html=replace_balanced_section(html,'<section class="why-section',why)

old='<a class="button button-primary header-cta" href="contact.html#enquiry">Enquire Now <span aria-hidden="true">â†’</span></a>'
new='<a class="button button-primary header-cta" href="#contact">Enquire Now <span aria-hidden="true">→</span></a>'
if old not in html:
    old='<a class="button button-primary header-cta" href="contact.html#enquiry">Enquire Now <span aria-hidden="true">→</span></a>'
if old not in html:
    raise SystemExit("Homepage header CTA was not found.")
html=html.replace(old,new,1)

p.write_text(html,encoding="utf-8-sig")
print("Expanded the course section with four verified learning-theme cards and an integrated-program summary.")
print("Expanded Why Choose into six detailed benefit cards.")
print("Changed the homepage header CTA to open the homepage enquiry dialog.")
