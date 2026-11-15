from pathlib import Path
p=Path(__file__).resolve().parent/"js"/"upgrade.js"
s=p.read_text(encoding="utf-8")
if "Horizontal Instagram Reel carousel" not in s:
    pos=s.rfind("})();")
    if pos<0: raise SystemExit("Could not find the upgrade.js IIFE end.")
    patch = r"""  // Horizontal Instagram Reel carousel. Cards open their exact Reel on Instagram.
  const instagramReelsTrack = document.getElementById('instagram-reels-track');
  if (instagramReelsTrack) {
    const reelCard = instagramReelsTrack.querySelector('.instagram-reel-card');
    const reelGap = 16;
    const reelStep = () => reelCard
      ? (reelCard.getBoundingClientRect().width + reelGap) * 2
      : instagramReelsTrack.clientWidth * 0.82;

    document.querySelectorAll('[data-reel-step]').forEach(button => {
      button.addEventListener('click', () => {
        const direction = Number(button.dataset.reelStep || 1);
        instagramReelsTrack.scrollBy({
          left: direction * reelStep(),
          behavior: reduce ? 'auto' : 'smooth'
        });
      });
    });
  }

"""
    s=s[:pos]+patch+s[pos:]
    p.write_text(s,encoding="utf-8")
    print("Added previous/next carousel controls.")
else:
    print("Carousel controls already present.")
