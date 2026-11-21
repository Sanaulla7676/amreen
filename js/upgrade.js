(() => {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Scroll reveal: blur, lift, scale and stagger. All elements remain readable without JS.
  const revealSelectors = [
    '.films-heading', '.film-card', '.films-footer', '.instagram-live',
    '.review-strip__lead', '.review-quote-grid blockquote',
    '.page-course-card', '.featured-course', '.course-investment',
    '.contact-panel', '.map-panel', '.faq-item', '.article-card', '.page-cta',
    '.program-offer-cell'
  ].join(',');
  const revealItems = document.querySelectorAll(revealSelectors);
  revealItems.forEach((element, index) => {
    element.classList.add('motion-reveal');
    element.style.setProperty('--motion-delay', (index % 4) * 85 + 'ms');
  });

  if (reduce || !('IntersectionObserver' in window)) {
    revealItems.forEach(element => element.classList.add('is-motion-visible'));
  } else {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-motion-visible');
        observer.unobserve(entry.target);
      });
    }, { threshold: .13, rootMargin: '0px 0px -5% 0px' });
    revealItems.forEach(element => revealObserver.observe(element));
  }

  // Spotlight/glare follows the pointer on the real academy video cards.
  if (!reduce && window.matchMedia('(pointer:fine)').matches) {
    document.querySelectorAll('.film-card').forEach(card => {
      card.addEventListener('pointermove', event => {
        const rect = card.getBoundingClientRect();
        card.style.setProperty('--film-x', (event.clientX - rect.left) + 'px');
        card.style.setProperty('--film-y', (event.clientY - rect.top) + 'px');
      });
    });
  }

  // Keep one academy video playing at a time.
  const videos = Array.from(document.querySelectorAll('.film-frame video'));
  videos.forEach(video => {
    video.addEventListener('play', () => videos.forEach(other => {
      if (other !== video && !other.paused) other.pause();
    }));
  });

  // Count from 0 to 40 on the sign the presenter is holding.
  const banner = document.querySelector('.program-banner');
  const counter = document.querySelector('.program-count[data-count-up]');
  const burst = banner && banner.querySelector('.confetti-burst');
  let hasRun = false;
  let celebrationTimer = 0;

  function buildConfetti() {
    if (!burst || burst.childElementCount) return;
    const palette = ['#f7d68a', '#ef4f7c', '#ffffff', '#9fc8f4', '#b21a4a', '#f4a1ba', '#e8c18a'];
    for (let i = 0; i < 34; i++) {
      const bit = document.createElement('span');
      bit.className = 'confetti-bit';
      const angle = (Math.PI * 2 * i) / 34 + (i % 4) * .11;
      const distance = 55 + (i % 7) * 13;
      bit.style.setProperty('--start-x', (35 + (i % 5) * 7) + '%');
      bit.style.setProperty('--start-y', (34 + (i % 4) * 6) + '%');
      bit.style.setProperty('--w', (5 + (i % 4) * 2) + 'px');
      bit.style.setProperty('--h', (7 + (i % 3) * 3) + 'px');
      bit.style.setProperty('--confetti', palette[i % palette.length]);
      bit.style.setProperty('--dx', (Math.cos(angle) * distance) + 'px');
      bit.style.setProperty('--dy', (Math.sin(angle) * distance - 28) + 'px');
      bit.style.setProperty('--spin', (180 + (i % 5) * 120) + 'deg');
      bit.style.setProperty('--delay', ((i % 9) * 22) + 'ms');
      burst.appendChild(bit);
    }
  }

  function celebrate() {
    if (!banner) return;
    buildConfetti();
    banner.classList.remove('is-celebrating');
    void banner.offsetWidth;
    banner.classList.add('is-celebrating');
    window.clearTimeout(celebrationTimer);
    celebrationTimer = window.setTimeout(() => banner.classList.remove('is-celebrating'), 2600);
  }

  function countUp(replay = false) {
    if (!counter || !banner) return;
    if (hasRun && !replay) return;
    hasRun = true;
    const target = Number(counter.dataset.countUp || 40);
    if (reduce) {
      counter.textContent = String(target);
      return;
    }
    banner.classList.remove('is-celebrating');
    counter.textContent = '0';
    const duration = replay ? 1250 : 1950;
    const start = performance.now();
    const tick = now => {
      const progress = Math.min(1, (now - start) / duration);
      const eased = 1 - Math.pow(1 - progress, 4);
      counter.textContent = String(Math.min(target, Math.round(target * eased)));
      if (progress < 1) {
        requestAnimationFrame(tick);
      } else {
        counter.textContent = String(target);
        celebrate();
      }
    };
    requestAnimationFrame(tick);
  }

  if (counter && banner) {
    // A no-JS fallback is 40; JS changes it to 0 until the counter enters view.
    counter.textContent = '0';
    if (reduce || !('IntersectionObserver' in window)) {
      countUp();
    } else {
      const counterObserver = new IntersectionObserver(entries => {
        if (entries.some(entry => entry.isIntersecting)) {
          countUp();
          counterObserver.disconnect();
        }
      }, { threshold: .32 });
      counterObserver.observe(banner);
    }

    const replayButton = counter.closest('.animated-number-panel');
    if (replayButton) {
      replayButton.addEventListener('click', () => countUp(true));
    }
  }
})();
