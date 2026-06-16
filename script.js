// =========================
// Custom Cursor
// =========================
(function() {
  const cursor = document.getElementById('cursor');
  const follower = document.getElementById('cursor-follower');
  if (!cursor || !follower || window.matchMedia('(max-width: 768px)').matches) return;
  let mx = 0, my = 0, fx = 0, fy = 0;
  document.addEventListener('mousemove', (e) => { mx = e.clientX; my = e.clientY; });
  document.querySelectorAll('[data-cursor-hover]').forEach(el => {
    el.addEventListener('mouseenter', () => { cursor.classList.add('is-hover'); follower.classList.add('is-hover'); });
    el.addEventListener('mouseleave', () => { cursor.classList.remove('is-hover'); follower.classList.remove('is-hover'); });
  });
  function tick() {
    cursor.style.transform = `translate(${mx}px, ${my}px) translate(-50%, -50%)`;
    fx += (mx - fx) * 0.15; fy += (my - fy) * 0.15;
    follower.style.transform = `translate(${fx}px, ${fy}px) translate(-50%, -50%)`;
    requestAnimationFrame(tick);
  }
  tick();
})();

// =========================
// Nav scroll
// =========================
(function() {
  const nav = document.getElementById('nav');
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 30);
  });
})();

// =========================
// Reveal on scroll
// =========================
(function() {
  const els = document.querySelectorAll('.reveal, .reveal-stagger');
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -80px 0px' });
  els.forEach(el => io.observe(el));
})();

// =========================
// Animated counters
// =========================
(function() {
  const counters = document.querySelectorAll('.count');
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        const el = e.target;
        const target = +el.dataset.target;
        const dur = 1600;
        const start = performance.now();
        function step(now) {
          const p = Math.min(1, (now - start) / dur);
          const eased = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.floor(target * eased);
          if (p < 1) requestAnimationFrame(step);
          else el.textContent = target;
        }
        requestAnimationFrame(step);
        io.unobserve(el);
      }
    });
  }, { threshold: 0.5 });
  counters.forEach(c => io.observe(c));
})();

// =========================
// Service card cursor spotlight
// =========================
(function() {
  document.querySelectorAll('.service-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width) * 100;
      const y = ((e.clientY - rect.top) / rect.height) * 100;
      card.style.setProperty('--mx', x + '%');
      card.style.setProperty('--my', y + '%');
    });
  });
})();

// =========================
// Pricing card 3D tilt
// =========================
(function() {
  document.querySelectorAll('[data-tilt]').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      card.style.transform = `perspective(1000px) rotateX(${y * -6}deg) rotateY(${x * 6}deg) translateY(-4px)`;
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
    });
  });
})();

// =========================
// FAQ accordion
// =========================
(function() {
  document.querySelectorAll('.faq-q').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.parentElement;
      const wasOpen = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
      if (!wasOpen) item.classList.add('open');
    });
  });
})();

// =========================
// Testimonial carousel
// =========================
(function() {
  const track = document.getElementById('testimonial-track');
  if (!track) return;
  const items = track.querySelectorAll('.testimonial');
  const dots = document.querySelectorAll('#testimonial-dots .dot-btn');
  let current = 0;
  let timer;
  function go(i) {
    current = (i + items.length) % items.length;
    items.forEach((el, idx) => el.classList.toggle('active', idx === current));
    dots.forEach((d, idx) => d.classList.toggle('active', idx === current));
  }
  function next() { go(current + 1); reset(); }
  function prev() { go(current - 1); reset(); }
  function reset() { clearInterval(timer); timer = setInterval(next, 6000); }
  document.getElementById('t-next').addEventListener('click', next);
  document.getElementById('t-prev').addEventListener('click', prev);
  dots.forEach((d, i) => d.addEventListener('click', () => { go(i); reset(); }));
  reset();
})();
