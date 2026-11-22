(() => {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const progress = document.querySelector('.scroll-progress span');
  const header = document.querySelector('.site-header');
  const revealTargets = document.querySelectorAll('.section-heading,.course-card,.career-heading,.career-description,.benefit-item,.academy-row,.why-item,.student-grid figure,.program-banner,.page-hero__copy,.page-hero__visual,.section-intro,.split-feature__image,.split-feature__copy,.value-card,.page-course-card,.featured-course,.program-detail,.teaching-card,.mentor-feature,.question-grid>div,.portfolio-item,.article-card,.contact-panel,.map-panel,.contact-ribbon,.social-follow,.page-cta');
  revealTargets.forEach((node, i) => {
    if (!node.hasAttribute('data-reveal') && !node.hasAttribute('data-stagger')) {
      node.setAttribute('data-reveal', i % 5 === 0 ? 'left' : 'up');
      node.style.setProperty('--reveal-delay', ((i % 4) * 65) + 'ms');
    }
  });
  document.querySelectorAll('[data-stagger]').forEach(group => {
    Array.from(group.children).forEach((child, i) => child.style.setProperty('--item-index', i));
  });
  if (reduce || !('IntersectionObserver' in window)) {
    document.querySelectorAll('[data-reveal],[data-stagger]').forEach(n => n.classList.add('is-inview'));
  } else {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-inview');
        observer.unobserve(entry.target);
      });
    }, { threshold: .14, rootMargin: '0px 0px -5% 0px' });
    document.querySelectorAll('[data-reveal],[data-stagger]').forEach(n => observer.observe(n));
  }
  let raf = 0;
  const updateScroll = () => {
    raf = 0;
    const max = document.documentElement.scrollHeight - window.innerHeight;
    const ratio = max > 0 ? window.scrollY / max : 0;
    if (progress) progress.style.width = (ratio * 100) + '%';
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 18);
    document.documentElement.style.setProperty('--scroll-progress', ratio.toFixed(4));
  };
  window.addEventListener('scroll', () => {
    if (!raf) raf = requestAnimationFrame(updateScroll);
  }, { passive: true });
  updateScroll();
  if (!reduce && window.matchMedia('(pointer:fine)').matches) {
    document.querySelectorAll('.course-card').forEach(card => {
      card.addEventListener('pointermove', event => {
        const r = card.getBoundingClientRect();
        const x = (event.clientX - r.left) / r.width - .5;
        const y = (event.clientY - r.top) / r.height - .5;
        card.style.setProperty('--tilt-x', (-y * 3.2) + 'deg');
        card.style.setProperty('--tilt-y', (x * 3.2) + 'deg');
      });
      card.addEventListener('pointerleave', () => {
        card.style.setProperty('--tilt-x', '0deg');
        card.style.setProperty('--tilt-y', '0deg');
      });
    });
  }
  const current = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.primary-nav a').forEach(link => {
    const href = link.getAttribute('href');
    if (href && href.split('#')[0] === current) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });
})();
