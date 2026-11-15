from pathlib import Path
import re
p=Path(__file__).resolve().parent/"index.html"
s=p.read_text(encoding="utf-8-sig")
start=s.find('<div class="instagram-reels-panel"')
if start<0: raise SystemExit("Instagram Reels panel was not found.")
# Find the matching close div for the panel without disturbing the enclosing films-shell/section.
tag_re=re.compile(r'<div\b[^>]*>|</div\s*>',re.I)
depth=0
end=None
for m in tag_re.finditer(s,start):
    if m.group(0).lower().startswith('</div'):
        depth-=1
        if depth==0:
            end=m.end()
            break
    else:
        depth+=1
if end is None: raise SystemExit("Could not find the end of the current Instagram panel.")
reels=[
("Dfug-TKSKzl","14 Nov 2026"),
("DftyC_7yDX4","14 Nov 2026"),
("DfrbBDeSn0C","13 Nov 2026"),
("Dfp1GYazrM3","12 Nov 2026"),
("DfnHp2fSJzE","11 Nov 2026"),
("DfmtpI1S5w-","11 Nov 2026"),
("DfmsAc5yFhn","11 Nov 2026"),
("DfmgPhqyMxi","11 Nov 2026"),
("DfmUBMky2gW","11 Nov 2026"),
]
def group(duplicate=False):
    pieces=['      <div class="instagram-marquee-group"'+(' aria-hidden="true"' if duplicate else '')+'>']
    for shortcode,date in reels:
        href=f"https://www.instagram.com/amreenkhanum60/reel/{shortcode}/"
        tabindex=' tabindex="-1"' if duplicate else ''
        pieces.append(f'''        <a class="instagram-marquee-item" href="{href}" target="_blank" rel="noopener noreferrer" aria-label="Open Amreen's Instagram Reel from {date}"{tabindex}>
          <iframe src="https://www.instagram.com/reel/{shortcode}/embed/" title="Instagram Reel by Amreen, {date}" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" scrolling="no" tabindex="-1" aria-hidden="true"></iframe>
        </a>''')
    pieces.append('      </div>')
    return "\n".join(pieces)
replacement='''<div class="instagram-reels-panel" id="instagram-reels">
      <div class="instagram-reels-copy">
        <span class="mini-label">LATEST FROM INSTAGRAM</span>
        <h3>Recent Reels from Amreen.</h3>
        <p>Amreen's latest Instagram videos, moving continuously from left to right. Click any video to open that Reel on Instagram.</p>
        <a class="instagram-profile-link" href="https://www.instagram.com/amreenkhanum60/" target="_blank" rel="noopener noreferrer">Visit Instagram Profile ↗</a>
      </div>
    </div>
    <div class="instagram-marquee" role="region" aria-label="Continuously moving recent Instagram videos">
      <div class="instagram-marquee-track">
''' + group(False) + "\n" + group(True) + '''
      </div>
    </div>
    <p class="instagram-reels-note">Select any moving video to watch the original Reel on Instagram.</p>'''
s=s[:start]+replacement+s[end:]
p.write_text(s,encoding="utf-8-sig")
print("Replaced carousel cards with 9 individual Reel videos in a duplicated seamless moving strip.")
print("Direction: left edge to right edge. Each video links to its own Instagram Reel.")
print("Removed carousel arrows, card dates, numbers and watch buttons.")
