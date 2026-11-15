from pathlib import Path
import re

root = Path(__file__).resolve().parent
html_path = root / "index.html"
html = html_path.read_text(encoding="utf-8-sig")

start = html.find('<section class="academy-films"')
if start < 0:
    raise SystemExit("Could not find the Inside the Academy section.")
end = html.find('</section>', start)
if end < 0:
    raise SystemExit("Could not find the end of the Inside the Academy section.")
end += len('</section>')
films = html[start:end]

# Replace the giant Instagram profile iframe with a compact horizontal row of real Reel embeds.
old_start = films.find('    <div class="instagram-live"')
old_end_marker = '    <p class="instagram-feed-fallback">'
old_end = films.find(old_end_marker, old_start)
if old_start < 0 or old_end < 0:
    raise SystemExit("Could not find the existing Instagram embed block.")
old_end = films.find('</p>', old_end) + len('</p>')
if old_end < len('</p>'):
    raise SystemExit("Could not find the Instagram fallback paragraph end.")

reels = [
    ("Dfug-TKSKzl", "14 NOV 2026"),
    ("DftyC_7yDX4", "14 NOV 2026"),
    ("DfrbBDeSn0C", "13 NOV 2026"),
    ("Dfp1GYazrM3", "12 NOV 2026"),
    ("DfnHp2fSJzE", "11 NOV 2026"),
    ("DfmtpI1S5w-", "11 NOV 2026"),
    ("DfmsAc5yFhn", "11 NOV 2026"),
    ("DfmgPhqyMxi", "11 NOV 2026"),
    ("DfmUBMky2gW", "11 NOV 2026"),
]
cards = []
for number, (shortcode, date) in enumerate(reels, start=1):
    url = f"https://www.instagram.com/amreenkhanum60/reel/{shortcode}/"
    cards.append(f'''      <article class="instagram-reel-card">
        <div class="instagram-reel-embed">
          <iframe src="https://www.instagram.com/reel/{shortcode}/embed/" title="Amreen's Instagram Reel, {date}" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" scrolling="no" tabindex="-1" aria-hidden="true"></iframe>
          <span class="instagram-reel-number">REEL {number:02d}</span>
        </div>
        <a class="instagram-reel-link" href="{url}" target="_blank" rel="noopener noreferrer" aria-label="Open Amreen's Instagram Reel from {date}">
          <span class="instagram-reel-date">{date}</span>
          <span class="instagram-reel-open">WATCH ON INSTAGRAM ↗</span>
        </a>
      </article>''')
carousel = '''    <div class="instagram-reels-panel" aria-label="Recent Instagram Reels">
      <div class="instagram-reels-heading">
        <div class="instagram-reels-copy">
          <span class="mini-label">LATEST FROM INSTAGRAM</span>
          <h3>Recent Reels from Amreen.</h3>
          <p>Browse the latest videos from @amreenkhanum60. Select any preview to open that Reel directly on Instagram.</p>
          <a class="instagram-profile-link" href="https://www.instagram.com/amreenkhanum60/" target="_blank" rel="noopener noreferrer">Visit Instagram Profile ↗</a>
        </div>
        <div class="instagram-reels-controls" aria-label="Instagram Reel carousel controls">
          <button type="button" data-reel-step="-1" aria-label="Scroll to previous Instagram Reels">←</button>
          <button type="button" data-reel-step="1" aria-label="Scroll to next Instagram Reels">→</button>
        </div>
      </div>
      <div class="instagram-reels-track" id="instagram-reels-track" tabindex="0" aria-label="Recent Instagram Reels, scroll horizontally">
''' + "\n".join(cards) + '''
      </div>
      <p class="instagram-reels-note">Reel previews are provided by Instagram. If a preview is unavailable in your browser, select the card to watch the video on Instagram.</p>
    </div>'''
films = films[:old_start] + carousel + films[old_end:]

# Remove the section from directly after the hero and insert it at the end of main content, before the footer.
html = html[:start] + html[end:]
main_end = html.rfind('</main>')
if main_end < 0:
    raise SystemExit("Could not find the end of the homepage main content.")
html = html[:main_end] + "\n\n" + films + "\n\n  " + html[main_end:]
html_path.write_text(html, encoding="utf-8-sig")

print("Moved Inside the Academy from after the hero to the end of main content, before the footer.")
print("Replaced the single Instagram profile iframe with", len(reels), "latest Reel cards.")
print("The two existing academy video cards were preserved.")
