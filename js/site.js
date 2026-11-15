(() => {
  const menu = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.primary-nav');
  if (menu && nav) {
    menu.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      menu.setAttribute('aria-expanded', String(open));
      menu.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    });
    nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
      nav.classList.remove('is-open');
      menu.setAttribute('aria-expanded', 'false');
    }));
  }
  document.querySelectorAll('.current-year').forEach(node => node.textContent = new Date().getFullYear());
  const current = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.primary-nav a').forEach(link => {
    if ((link.getAttribute('href') || '').split('#')[0] === current) {
      link.classList.add('active');
      link.setAttribute('aria-current', 'page');
    }
  });
  document.querySelectorAll('[data-whatsapp-form]').forEach(form => {
    form.addEventListener('submit', event => {
      event.preventDefault();
      if (!form.reportValidity()) return;
      const data = new FormData(form);
      const message = [
        'Hello Amreen’s Academy, I would like to enquire about a course.',
        'Name: ' + (data.get('name') || ''),
        'Phone: ' + (data.get('phone') || ''),
        'Course: ' + (data.get('course') || ''),
        'Message: ' + (data.get('message') || 'Please share the current details.')
      ].join('\n');
      const url = 'https://wa.me/918123410118?text=' + encodeURIComponent(message);
      const status = form.querySelector('.form-status');
      if (status) status.textContent = 'Opening WhatsApp with your enquiry. Please send the prepared message there.';
      window.open(url, '_blank', 'noopener,noreferrer');
    });
  });
})();
