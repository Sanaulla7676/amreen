(() => {
  const menuToggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.primary-nav');
  if (menuToggle && nav) {
    menuToggle.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      menuToggle.setAttribute('aria-expanded', String(open));
      menuToggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    });
    nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
      nav.classList.remove('is-open');
      menuToggle.setAttribute('aria-expanded', 'false');
      menuToggle.setAttribute('aria-label', 'Open navigation');
    }));
  }
  const dialog = document.getElementById('enquiry-dialog');
  document.querySelectorAll('a[href="#contact"]').forEach(link => {
    link.addEventListener('click', event => {
      if (dialog && typeof dialog.showModal === 'function') {
        event.preventDefault();
        dialog.showModal();
      }
    });
  });
  if (dialog) {
    dialog.addEventListener('click', event => {
      const rect = dialog.getBoundingClientRect();
      const outside = event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom;
      if (outside) dialog.close();
    });
  }
  const form = document.getElementById('enquiry-form');
  const note = document.getElementById('form-note');
  if (form && note) {
    form.addEventListener('submit', event => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      const data = new FormData(form);
      const msg = [
        'Hello Amreen’s Academy, I would like to enquire about a course.',
        'Name: ' + (data.get('name') || ''),
        'Phone: ' + (data.get('phone') || ''),
        'Course: ' + (data.get('course') || ''),
        'Area of interest: ' + (data.get('interest') || 'Not specified'),
        'Please share the latest details, batch dates and fees.'
      ].join('\n');
      note.textContent = 'Opening WhatsApp with your enquiry. Please send the prepared message there.';
      note.classList.add('form-note-highlight');
      window.open('https://wa.me/918123410118?text=' + encodeURIComponent(msg), '_blank', 'noopener,noreferrer');
    });
  }
  const grid = document.getElementById('course-grid');
  document.querySelectorAll('[data-scroll-cards]').forEach(button => {
    button.addEventListener('click', () => {
      if (!grid) return;
      const firstCard = grid.querySelector('.course-card');
      const distance = firstCard ? firstCard.getBoundingClientRect().width + 12 : 210;
      grid.scrollBy({ left: Number(button.dataset.scrollCards) * distance, behavior: 'smooth' });
    });
  });
  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
