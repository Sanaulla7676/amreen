from pathlib import Path
import re

root=Path(__file__).resolve().parent
cssp=root/"css"/"upgrade.css"
htmlp=root/"index.html"
css=cssp.read_text(encoding="utf-8")

# Replace the final headline rules so ACADEMY matches AMREEN'S exactly in type family, weight and scale.
css += r"""

/* Final correction: keep portrait horizontal anchor; only lower it vertically.
   Match ACADEMY typography to AMREEN'S instead of the previous script treatment. */
.hero h1 > .hero-title-academy {
  align-self: flex-end !important;
  margin: -2px 9% 0 0 !important;
  color: #fbfbfd !important;
  font-family: var(--heading) !important;
  font-size: clamp(92px, 12vw, 166px) !important;
  font-weight: 900 !important;
  line-height: .88 !important;
  letter-spacing: -.085em !important;
  text-transform: uppercase;
  white-space: nowrap;
  opacity: 1;
  transform: none;
  animation: none !important;
  text-shadow: 0 5px 14px rgba(255,255,255,.04);
}
/* Main portrait remains at its original left-side position. Only Y is changed. */
.hero .hero-figure {
  left: 5.7% !important;
  right: auto !important;
  top: 417px !important;
  bottom: auto !important;
  height: 481px !important;
  max-width: 54%;
}
/* With the two-line heavy title, put training copy lower on the far right. */
.hero .hero-copy {
  right: 4% !important;
  left: auto !important;
  top: 455px !important;
  width: 33% !important;
  text-align: right !important;
}
.hero .hero-copy .copy-rule {
  margin-left: auto !important;
  margin-right: 0 !important;
}
.hero .hero-copy h2,
.hero .hero-copy > p:not(.hero-signoff) {
  text-align: right !important;
  margin-left: auto !important;
}
.hero .hero-stats {
  justify-content: flex-end !important;
  margin-left: auto !important;
}
/* Tablet */
@media (max-width: 1120px) {
  .hero h1 > .hero-title-academy {
    font-size: clamp(78px, 11vw, 124px) !important;
    margin-right: 11% !important;
  }
  .hero .hero-figure {
    left: 5.7% !important;
    right: auto !important;
    top: 430px !important;
    height: 460px !important;
  }
  .hero .hero-copy {
    top: 420px !important;
    right: 4% !important;
    width: 39% !important;
  }
}
@media (max-width: 900px) {
  .hero h1 > .hero-title-academy {
    font-size: clamp(72px, 11.5vw, 108px) !important;
    margin-right: 13% !important;
  }
  .hero .hero-figure {
    left: 5.7% !important;
    right: auto !important;
    top: 390px !important;
    height: 470px !important;
  }
  .hero .hero-copy {
    top: 345px !important;
    right: 5% !important;
    width: 43% !important;
  }
}
/* Mobile portrait stays left/centered, not moved to the opposite edge. */
@media (max-width: 650px) {
  .hero h1 > .hero-title-academy {
    font-size: clamp(51px, 13.2vw, 84px) !important;
    margin-right: 12% !important;
  }
  .hero .hero-copy {
    top: 265px !important;
    right: 6% !important;
    left: auto !important;
    width: 88% !important;
  }
  .hero .hero-figure {
    left: 5.7% !important;
    right: auto !important;
    top: auto !important;
    bottom: 0 !important;
    height: 48% !important;
    max-width: 78%;
  }
}
@media (max-width: 420px) {
  .hero h1 > .hero-title-academy {
    font-size: clamp(48px, 13vw, 58px) !important;
  }
  .hero .hero-copy { top: 245px !important; }
  .hero .hero-figure { left: 3% !important; right: auto !important; height: 46% !important; max-width: 82%; }
}
@media (prefers-reduced-motion: reduce) {
  .hero h1 > .hero-title-academy { opacity: 1 !important; transform: none !important; animation: none !important; }
}
"""
cssp.write_text(css,encoding="utf-8")

html=htmlp.read_text(encoding="utf-8")
html,n=re.subn(r'href="css/upgrade\.css(?:\?[^"]*)?"',
               'href="css/upgrade.css?v=hero-layout-fix-20261115-2"',html,count=1)
if n!=1:
    raise SystemExit("Could not update the cache-busting stylesheet link.")
htmlp.write_text(html,encoding="utf-8")

print("Final corrected hero rules appended.")
print("CSS brace balance:",css.count("{"),css.count("}"))
print("Cache-busting URL updated.")
