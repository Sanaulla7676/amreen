from pathlib import Path
import re

root = Path(__file__).resolve().parent
css_path = root / "css" / "upgrade.css"
html_path = root / "index.html"

css = css_path.read_text(encoding="utf-8")
marker = "/* Hero refinement: AMREEN'S / ACADEMY identity and left-aligned training copy */"
if marker not in css:
    raise SystemExit("Could not find the existing custom hero block; stopped without changing files.")
prefix = css[:css.index(marker)]

hero = r"""
/* AUTHORITATIVE HERO LAYOUT: desktop portrait offset, right-aligned course copy */
.hero,
.hero-inner {
  min-height: 900px !important;
  height: 900px !important;
}
.hero {
  position: relative;
  overflow: hidden;
}
.hero .hero-kicker {
  left: 7% !important;
  top: 19px !important;
  z-index: 6;
  color: rgba(255,255,255,.76);
  letter-spacing: 2.4px;
}
.hero h1 {
  position: absolute;
  top: 36px !important;
  left: 7% !important;
  z-index: 4 !important;
  display: flex !important;
  flex-direction: column;
  align-items: flex-start;
  width: 82%;
  margin: 0;
  white-space: normal;
  letter-spacing: -.085em;
}
.hero h1 .hero-title-mask {
  display: block;
  width: 100%;
  overflow: hidden;
  padding-bottom: .09em;
}
.hero h1 .hero-title-word {
  display: inline-block;
  color: #fbfbfd;
  font-family: var(--heading);
  font-size: clamp(92px, 12vw, 166px) !important;
  font-weight: 900;
  line-height: .88;
  letter-spacing: -.085em;
  white-space: nowrap;
  opacity: 1;
  animation: title-rise 1.12s var(--motion-ease) .12s both;
}
.hero h1 > .hero-title-academy {
  display: block !important;
  position: relative;
  align-self: flex-end !important;
  margin: -2px 9% 0 0 !important;
  padding: 0;
  color: #fbfbfd !important;
  font-family: "Allura", "Segoe Script", "Brush Script MT", cursive !important;
  font-size: clamp(58px, 6vw, 82px) !important;
  font-weight: 400 !important;
  line-height: .8 !important;
  letter-spacing: 1.4px !important;
  text-transform: uppercase;
  white-space: nowrap;
  opacity: 0;
  transform: translate3d(0, 26px, 0);
  animation: academy-word-rise .9s cubic-bezier(.18,.72,.22,1) .72s forwards !important;
  text-shadow: 0 4px 14px rgba(255,255,255,.1);
}
@keyframes academy-word-rise {
  from { opacity: 0; transform: translate3d(0,26px,0); }
  to { opacity: 1; transform: translate3d(0,0,0); }
}
/* Former top was approximately 117px. New top is 417px: exactly 300px lower. */
.hero .hero-figure {
  position: absolute !important;
  z-index: 2;
  left: auto !important;
  right: 2.5% !important;
  top: 417px !important;
  bottom: auto !important;
  height: 481px !important;
  width: auto;
  max-width: 54%;
  object-fit: contain;
  object-position: bottom right;
  filter: drop-shadow(0 20px 24px rgba(0,0,0,.26));
  animation: figure-arrive-right 1.1s cubic-bezier(.18,.72,.22,1) .2s both;
}
@keyframes figure-arrive-right {
  from { opacity: 0; transform: translate3d(0,28px,0); }
  to { opacity: 1; transform: translate3d(0,0,0); }
}
/* Training heading and supporting copy anchored to the far right, clear of the portrait. */
.hero .hero-copy {
  position: absolute !important;
  left: auto !important;
  right: 4% !important;
  top: 235px !important;
  z-index: 5 !important;
  width: 33% !important;
  max-width: 470px;
  padding: 0 !important;
  text-align: right !important;
  animation: copy-enter-right .9s cubic-bezier(.18,.72,.22,1) .55s both;
}
@keyframes copy-enter-right {
  from { opacity: 0; transform: translate3d(28px,12px,0); }
  to { opacity: 1; transform: translate3d(0,0,0); }
}
.hero .hero-copy .copy-rule {
  display: block;
  margin: 0 0 12px auto !important;
  transform-origin: right center;
}
.hero .hero-copy h2 {
  max-width: 100% !important;
  margin: 0 0 12px auto !important;
  font-size: clamp(17px, 1.8vw, 23px) !important;
  line-height: 1.18 !important;
  letter-spacing: 1.15px;
  text-align: right !important;
}
.hero .hero-copy > p:not(.hero-signoff) {
  max-width: 380px !important;
  margin: 0 0 0 auto !important;
  font-size: clamp(14px, 1.35vw, 17px) !important;
  line-height: 1.48 !important;
  text-align: right !important;
}
.hero .hero-stats {
  display: flex;
  justify-content: flex-end !important;
  gap: clamp(8px, 1.2vw, 16px);
  max-width: 100%;
  margin: 22px 0 0 auto !important;
}
.hero .hero-stats div {
  min-width: clamp(68px, 7vw, 88px);
  align-items: center;
}
.hero .hero-stats strong { font-size: clamp(13px, 1.35vw, 17px); }
.hero .hero-stats span { font-size: 10px; }
.hero .hero-stats i { height: 36px; }

/* Tablet: preserve the right-side composition and keep the portrait fully inside. */
@media (max-width: 1120px) {
  .hero, .hero-inner { min-height: 900px !important; height: 900px !important; }
  .hero h1 { top: 42px !important; left: 6% !important; width: 88%; }
  .hero h1 .hero-title-word { font-size: clamp(78px, 11vw, 124px) !important; }
  .hero h1 > .hero-title-academy { font-size: clamp(48px, 5.6vw, 68px) !important; margin-right: 11% !important; }
  .hero .hero-copy { right: 4% !important; top: 230px !important; width: 39% !important; }
  .hero .hero-copy h2 { font-size: clamp(16px, 1.9vw, 21px) !important; }
  .hero .hero-copy > p:not(.hero-signoff) { font-size: 14px !important; }
  .hero .hero-stats { gap: 7px; margin-top: 18px !important; }
  .hero .hero-stats div { min-width: 62px; }
  .hero .hero-stats strong { font-size: 12px; }
  .hero .hero-stats span { font-size: 9px; }
  .hero .hero-figure { right: 1.5% !important; top: 430px !important; height: 460px !important; max-width: 55%; }
}
@media (max-width: 900px) {
  .hero, .hero-inner { min-height: 860px !important; height: 860px !important; }
  .hero h1 { top: 40px !important; left: 6% !important; width: 88%; }
  .hero h1 .hero-title-word { font-size: clamp(72px, 11.5vw, 108px) !important; }
  .hero h1 > .hero-title-academy { font-size: clamp(42px, 5.4vw, 56px) !important; }
  .hero .hero-copy { right: 5% !important; top: 205px !important; width: 43% !important; max-width: 350px; }
  .hero .hero-copy h2 { font-size: clamp(15px, 2vw, 19px) !important; }
  .hero .hero-copy > p:not(.hero-signoff) { font-size: 13px !important; }
  .hero .hero-stats { gap: 6px; margin-top: 15px !important; }
  .hero .hero-stats div { min-width: 58px; }
  .hero .hero-stats strong { font-size: 11px; }
  .hero .hero-stats span { font-size: 8px; }
  .hero .hero-figure { right: 0 !important; top: 390px !important; height: 470px !important; max-width: 58%; }
}

/* Mobile: compact right-aligned copy panel above the portrait. */
@media (max-width: 650px) {
  .hero, .hero-inner { min-height: 900px !important; height: 900px !important; }
  .hero .hero-kicker { left: 6% !important; top: 18px !important; font-size: 8px; letter-spacing: 1.8px; }
  .hero h1 { top: 48px !important; left: 6% !important; width: 88%; }
  .hero h1 .hero-title-word { font-size: clamp(51px, 13.2vw, 84px) !important; }
  .hero h1 > .hero-title-academy { font-size: clamp(36px, 8.5vw, 48px) !important; margin-right: 12% !important; }
  .hero .hero-copy {
    left: auto !important;
    right: 6% !important;
    top: 265px !important;
    width: 88% !important;
    max-width: none;
    padding: 15px 16px 13px !important;
    border: 1px solid rgba(255,255,255,.14);
    border-radius: 15px;
    background: linear-gradient(115deg,rgba(4,17,38,.84),rgba(7,24,47,.64));
    backdrop-filter: blur(7px);
    text-align: right !important;
  }
  .hero .hero-copy .copy-rule { margin: 0 0 9px auto !important; }
  .hero .hero-copy h2 { font-size: 16px !important; line-height: 1.2 !important; margin-bottom: 8px !important; }
  .hero .hero-copy > p:not(.hero-signoff) { max-width: 100% !important; font-size: 12px !important; line-height: 1.45 !important; }
  .hero .hero-stats { justify-content: flex-end !important; margin: 13px 0 0 auto !important; gap: 8px; }
  .hero .hero-stats div { min-width: 65px; }
  .hero .hero-stats strong { font-size: 12px; }
  .hero .hero-stats span { font-size: 8px; }
  .hero .hero-stats i { height: 29px; }
  .hero .hero-figure {
    left: auto !important;
    right: -3% !important;
    top: auto !important;
    bottom: 0 !important;
    height: 48% !important;
    max-width: 78%;
  }
}
@media (max-width: 420px) {
  .hero, .hero-inner { min-height: 850px !important; height: 850px !important; }
  .hero h1 .hero-title-word { font-size: clamp(48px, 13vw, 58px) !important; }
  .hero h1 > .hero-title-academy { font-size: 36px !important; }
  .hero .hero-copy { top: 245px !important; padding: 13px 13px 11px !important; }
  .hero .hero-copy h2 { font-size: 14px !important; }
  .hero .hero-copy > p:not(.hero-signoff) { font-size: 11px !important; }
  .hero .hero-figure { height: 46% !important; max-width: 82%; }
}
@media (prefers-reduced-motion: reduce) {
  .hero h1 .hero-title-word,
  .hero h1 > .hero-title-academy,
  .hero .hero-figure,
  .hero .hero-copy {
    animation: none !important;
    opacity: 1 !important;
    transform: none !important;
  }
}
"""

css_path.write_text(prefix + hero, encoding="utf-8")

html = html_path.read_text(encoding="utf-8")
html, n = re.subn(
    r'href="css/upgrade\.css(?:\?[^"]*)?"',
    'href="css/upgrade.css?v=hero-layout-fix-20261115-1"',
    html,
    count=1
)
if n != 1:
    raise SystemExit("Could not update the upgrade.css link; CSS was rewritten, but cache-busting link was not changed.")
html_path.write_text(html, encoding="utf-8")

print("Replaced conflicting hero overrides with one final responsive block.")
print("Added cache-busting stylesheet URL.")
print("CSS lines:", len((css_path.read_text(encoding="utf-8")).splitlines()))
print("CSS braces:", css_path.read_text(encoding="utf-8").count("{"), css_path.read_text(encoding="utf-8").count("}"))
