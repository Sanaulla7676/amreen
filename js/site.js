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
      const name = String(data.get('name') || '').trim();
      const phone = String(data.get('phone') || '').trim();
      const course = String(data.get('course') || '').trim();
      const email = String(data.get('email') || '').trim();
      const enquiry = String(data.get('message') || '').trim();
      const message = [
        'Hello Amreen’s Academy, I would like to enquire about a course.',
        'Name: ' + name,
        'Phone: ' + phone,
        'Course: ' + course,
        'Message: ' + (enquiry || 'Please share the current details.')
      ].join('\n');
      const url = 'https://wa.me/918123410118?text=' + encodeURIComponent(message);
      const status = form.querySelector('.form-status');
      window.open(url, '_blank', 'noopener,noreferrer');
      if (status) status.textContent = 'Your WhatsApp message is ready. Saving this enquiry to the academy follow-up list…';

      const saveLead = async () => {
        const config = window.ACADEMY_SUPABASE_CONFIG;
        if (!config?.url || !config?.publishableKey) return false;
        try {
          const { createClient } = await import('https://esm.sh/@supabase/supabase-js@2');
          const client = createClient(config.url, config.publishableKey, {
            auth: { persistSession: false, autoRefreshToken: false }
          });
          const { error } = await client.from('leads').insert({
            name,
            phone,
            ...(email ? { email } : {}),
            course_interest: course,
            message: enquiry
          });
          return !error;
        } catch {
          return false;
        }
      };

      saveLead().then(saved => {
        if (!status) return;
        status.textContent = saved
          ? 'Enquiry saved. Please send the prepared WhatsApp message to complete your request.'
          : 'WhatsApp is ready, but the enquiry could not be saved. Please send the prepared message so the academy can follow up.';
      });
    });
  });
})();
