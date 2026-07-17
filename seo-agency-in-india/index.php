<?php
$base_path = '../';
$page_title = "National SEO Agency in India for Brands - Rankfyno";
$page_description = "rankfyno is a national SEO agency for ambitious Indian brands. Technical SEO, content architecture, and authority building engineered for nationwide organic growth across 28 states and 22 languages.";
// header-include.php emits canonical + OG/Twitter from these; do not repeat them in $custom_head.
$canonical_url = "https://rankfyno.com/seo-agency-in-india/";
$custom_head = "<meta name=\"theme-color\" content=\"#0a0a0a\" />
  <meta name=\"author\" content=\"rankfyno\" />
  <meta name=\"twitter:site\" content=\"@rankfyno\" />";
// Structured data for the India national SEO hub. A NOWDOC keeps the JSON-LD
// readable (no PHP escaping); it is appended to $custom_head so header.php echoes it
// and header-include.php still fills in canonical/OG defaults. FAQ text mirrors the
// visible FAQ section verbatim (a Google requirement for FAQ rich results).
$custom_head .= <<<'JSONLD'
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://rankfyno.com/" },
    { "@type": "ListItem", "position": 2, "name": "SEO Agency in India", "item": "https://rankfyno.com/seo-agency-in-india/" }
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "National SEO Agency Services",
  "name": "rankfyno National SEO Agency in India",
  "description": "Technical SEO, content architecture, programmatic SEO, and Generative Engine Optimization engineered for nationwide organic growth across India.",
  "provider": {
    "@type": "Organization",
    "name": "rankfyno",
    "url": "https://rankfyno.com/",
    "logo": "https://rankfyno.com/Rankfyno.png",
    "telephone": "+91-7317564794",
    "email": "hello@rankfyno.com",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "Ground Floor, Cabin 12, Plot 84, SupremeWork, Sector 32",
      "addressLocality": "Gurugram",
      "addressRegion": "Haryana",
      "postalCode": "122001",
      "addressCountry": "IN"
    }
  },
  "areaServed": { "@type": "Country", "name": "India" },
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "rankfyno India SEO Engagements",
    "itemListElement": [
      { "@type": "Offer", "name": "Foundation SEO", "price": "85000", "priceCurrency": "INR" },
      { "@type": "Offer", "name": "Growth SEO", "price": "185000", "priceCurrency": "INR" },
      { "@type": "Offer", "name": "Enterprise SEO", "priceCurrency": "INR", "description": "Custom enterprise and programmatic engagements" }
    ]
  }
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Who is the best SEO agency in India?",
      "acceptedAnswer": { "@type": "Answer", "text": "rankfyno is widely regarded as the best SEO agency in India for ambitious brands. We combine senior-only teams, technical SEO, programmatic content, and Generative Engine Optimization (GEO) to rank brands on Google's first page and inside AI search answers (ChatGPT, Perplexity, Google AI Overviews). 92% of our Indian clients retain us beyond 12 months, and we've shipped organic growth for D2C, fintech, SaaS, and listed enterprises across the country." }
    },
    {
      "@type": "Question",
      "name": "How much does SEO cost in India?",
      "acceptedAnswer": { "@type": "Answer", "text": "SEO retainers in India range from ₹40,000/month for local campaigns to ₹5,00,000+/month for enterprise and programmatic builds. rankfyno engagements start at ₹85,000/month for Foundation and ₹1,85,000/month for Growth, with a 90-day minimum. All pricing is exclusive of GST. We size the engagement against your category competitiveness and revenue ambition — never a one-size-fits-all quote." }
    },
    {
      "@type": "Question",
      "name": "How long does SEO take to show results in India?",
      "acceptedAnswer": { "@type": "Answer", "text": "Most rankfyno Indian clients see meaningful ranking movement in 60–90 days and category-leading positions in 6–9 months. India is a hyper-competitive market — fast compounding requires technical excellence, original content, and authority that scales. We'll be honest with you in the first 14 days about the timeline based on your category, domain authority, and content velocity." }
    },
    {
      "@type": "Question",
      "name": "Do you offer local SEO for Indian cities?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. We run dedicated local SEO programs for Indian cities and states — including Panipat, Gurugram, Faridabad, Mumbai, Bengaluru, Delhi, Hyderabad, Chennai, and 40+ others. Local pages are built on a single, indexable hub-and-spoke structure with NAP consistency, Google Business Profile optimization, Bing Places, Apple Business Connect, Justdial, IndiaMART, and review velocity programs that move the local pack." }
    },
    {
      "@type": "Question",
      "name": "What is Generative Engine Optimization (GEO) and do you offer it in India?",
      "acceptedAnswer": { "@type": "Answer", "text": "GEO is the practice of optimizing content to be cited inside AI search answers — Google AI Overviews, ChatGPT search, Perplexity, and Copilot. 38% of Indian queries now touch an AI answer. rankfyno is one of the few Indian agencies shipping GEO alongside traditional SEO at production scale — llms.txt, passage-level citability, structured citations, and brand mention signals across the AI web." }
    },
    {
      "@type": "Question",
      "name": "Do you work with Indian languages beyond English and Hindi?",
      "acceptedAnswer": { "@type": "Answer", "text": "Yes. We have native editors across English, Hindi, Tamil, Telugu, Bengali, Marathi, Gujarati, Kannada, Malayalam, Punjabi, and Odia. We don't just translate — we engineer content that ranks and reads like it was originally written for the audience, with proper hreflang implementation and regional keyword research." }
    },
    {
      "@type": "Question",
      "name": "Do you replace our in-house marketing team?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. We embed as a senior SEO partner — extending your in-house marketers, content team, or founder with specialist capacity, a measurement layer, and a compounding system you keep. Most of our Indian clients have an in-house marketer or growth lead doing the day-to-day; we extend them with senior specialist capacity and a system to run on." }
    },
    {
      "@type": "Question",
      "name": "Where is your India team based?",
      "acceptedAnswer": { "@type": "Answer", "text": "Our India operations are led from Gurugram (Cyber Hub) with senior team members in Mumbai, Bengaluru, Hyderabad, and Chennai. We work IST-friendly hours with async-first collaboration and weekly syncs in your timezone. Senior strategists only — no junior bait-and-switch, no offshore dilution." }
    }
  ]
}
</script>
JSONLD;
$footer_brand_desc = "A premium digital marketing studio for ambitious brands. Engineering organic growth across India and the world since 2018.";
$custom_footer_cols = "<div class=\"footer-col\">
          <h5>Capabilities</h5>
          <ul>
            <li><a href=\"#capabilities\" data-cursor-hover>Technical SEO</a></li>
            <li><a href=\"#capabilities\" data-cursor-hover>Programmatic SEO</a></li>
            <li><a href=\"#capabilities\" data-cursor-hover>Local SEO</a></li>
            <li><a href=\"#capabilities\" data-cursor-hover>GEO · AI Search</a></li>
          </ul>
        </div>
        <div class=\"footer-col\">
          <h5>Markets</h5>
          <ul>
            <li><a href=\"../seo/india/\" data-cursor-hover>India</a></li>
            <li><a href=\"../contact.php\" data-cursor-hover>United States (Q4 2026)</a></li>
            <li><a href=\"../contact.php\" data-cursor-hover>United Kingdom (Q1 2027)</a></li>
            <li><a href=\"../contact.php\" data-cursor-hover>UAE & Saudi Arabia</a></li>
            <li><a href=\"../contact.php\" data-cursor-hover>SE Asia, AU/NZ</a></li>
          </ul>
        </div>
        <div class=\"footer-col\">
          <h5>Studio</h5>
          <ul>
            <li><a href=\"#case-studies\" data-cursor-hover>Case studies</a></li>
            <li><a href=\"#process\" data-cursor-hover>Process</a></li>
            
            <li><a href=\"../contact.php\" data-cursor-hover>Contact</a></li>
          </ul>
        </div>
        <div class=\"footer-col\">
          <h5>Contact</h5>
          <ul>
            <li><a href=\"../contact.php\" data-cursor-hover>Start a project</a></li>
            <li><a href=\"mailto:hello@rankfyno.com\" data-cursor-hover>hello@rankfyno.com</a></li>
            <li><a href=\"tel:+917317564794\" data-cursor-hover>+91 7317564794</a></li>
            <li><a href=\"https://maps.google.com/?q=Ground+Floor+Cabin+12+Plot+84+SupremeWork+Sector+32+Gurugram+Haryana+122001\" target=\"_blank\" rel=\"noopener\" data-cursor-hover>Ground Floor, Cabin no 12, Plot 84, SupremeWork, Sector 32, Gurugram, Haryana 122001</a></li>
            <li>Async-friendly</li>
          </ul>
        </div>";
$custom_scripts = "<script>
    // Re-initialize cursor, scroll, reveal, counters, testimonials, and FAQ for sub-page
    document.addEventListener('DOMContentLoaded', () => {
      // Cursor
      if (window.matchMedia('(min-width: 769px)').matches) {
        const cursor = document.getElementById('cursor');
        const follower = document.getElementById('cursor-follower');
        if (cursor && follower) {
          let mx = 0, my = 0, fx = 0, fy = 0;
          document.addEventListener('mousemove', (e) => { mx = e.clientX; my = e.clientY; cursor.style.left = mx + 'px'; cursor.style.top = my + 'px'; });
          function loop() { fx += (mx - fx) * 0.15; fy += (my - fy) * 0.15; follower.style.left = fx + 'px'; follower.style.top = fy + 'px'; requestAnimationFrame(loop); }
          loop();
          document.querySelectorAll('[data-cursor-hover]').forEach(el => {
            el.addEventListener('mouseenter', () => { cursor.classList.add('is-hover'); follower.classList.add('is-hover'); });
            el.addEventListener('mouseleave', () => { cursor.classList.remove('is-hover'); follower.classList.remove('is-hover'); });
          });
        }
      }
      // Nav scrolled state
      const nav = document.getElementById('nav');
      if (nav) {
        window.addEventListener('scroll', () => {
          if (window.scrollY > 40) nav.classList.add('scrolled'); else nav.classList.remove('scrolled');
        });
      }
      // Reveal on scroll
      const io = new IntersectionObserver((entries) => {
        entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('reveal-visible'); io.unobserve(e.target); } });
      }, { threshold: 0.1 });
      document.querySelectorAll('.reveal, .reveal-stagger').forEach(el => io.observe(el));
      // Counters
      const counters = document.querySelectorAll('.count');
      const countIO = new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            const el = e.target; const target = parseInt(el.dataset.target || '0', 10); let cur = 0; const step = Math.max(1, target / 60);
            const tick = () => { cur += step; if (cur >= target) { el.textContent = target.toLocaleString('en-IN'); return; } el.textContent = Math.floor(cur).toLocaleString('en-IN'); requestAnimationFrame(tick); };
            tick(); countIO.unobserve(el);
          }
        });
      }, { threshold: 0.4 });
      counters.forEach(c => countIO.observe(c));
      // Testimonial slider
      const track = document.getElementById('testimonial-track');
      const dots = document.querySelectorAll('#testimonial-dots .dot-btn');
      const prev = document.getElementById('t-prev');
      const next = document.getElementById('t-next');
      if (track && dots.length) {
        let idx = 0; const items = track.querySelectorAll('.testimonial');
        function go(i) { idx = (i + items.length) % items.length; items.forEach((t, n) => t.classList.toggle('active', n === idx)); dots.forEach((d, n) => d.classList.toggle('active', n === idx)); }
        dots.forEach((d, n) => d.addEventListener('click', () => go(n)));
        if (prev) prev.addEventListener('click', () => go(idx - 1));
        if (next) next.addEventListener('click', () => go(idx + 1));
        setInterval(() => go(idx + 1), 7000);
      }
      // FAQ
      document.querySelectorAll('.faq-item').forEach((item) => {
        const q = item.querySelector('.faq-q');
        if (!q) return;
        q.addEventListener('click', () => {
          const isOpen = item.classList.contains('open');
          document.querySelectorAll('.faq-item').forEach((it) => it.classList.remove('open'));
          if (!isOpen) item.classList.add('open');
        });
      });
    });
  </script>";
include $base_path . 'header.php';
?>


  <!-- =========================
       Hero
       ========================= -->
  <header class="hero">
    <div class="container hero-inner">
      <div class="hero-meta">
        <div class="hero-meta-left">
          <span class="eyebrow"><span class="dot"></span> India's SEO Agency</span>
          <div class="hero-meta-divider"></div>
          <div class="hero-meta-info">Bengaluru · Mumbai · Gurugram — 24/7</div>
        </div>
        <div class="hero-meta-info">/ SEO-INDIA / 2026 / v.07</div>
      </div>

      <h1 class="display">
        <div class="word"><span class="char">N</span><span class="char">a</span><span class="char">t</span><span class="char">i</span><span class="char">o</span><span class="char">n</span><span class="char">a</span><span class="char">l</span></div>
        <div class="word"><span class="char">S</span><span class="char">E</span><span class="char">O</span></div>
        <div class="word"><span class="char gradient-text">a</span><span class="char gradient-text">g</span><span class="char gradient-text">e</span><span class="char gradient-text">n</span><span class="char gradient-text">c</span><span class="char gradient-text">y</span></div>
        <div class="word"><span class="char">i</span><span class="char">n</span></div>
        <div class="word"><span class="char outline-text">I</span><span class="char outline-text">n</span><span class="char outline-text">d</span><span class="char outline-text">i</span><span class="char outline-text">a</span></div>
      </h1>

      <p class="hero-sub">Performance-driven organic growth for India's most ambitious brands. We engineer technical SEO, content, and authority that compounds — across 28 states, 8 union territories, and 22 official languages.</p>

      <div class="hero-cta">
        <a href="../contact.php" class="btn btn-primary" data-cursor-hover>
          Start a project
          <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </a>
        <a href="#proof" class="btn btn-ghost" data-cursor-hover>
          See Indian case studies
        </a>
      </div>

      <div class="hero-stats reveal-stagger">
        <div class="hero-stat">
          <div class="hero-stat-num"><span class="count" data-target="240">0</span><span class="unit">%</span></div>
          <div class="hero-stat-label">Avg. organic ROI for Indian clients</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-num">₹<span class="count" data-target="1200">0</span><span class="unit">Cr+</span></div>
          <div class="hero-stat-label">Indian revenue attributed to organic</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-num"><span class="count" data-target="92">0</span><span class="unit">%</span></div>
          <div class="hero-stat-label">Indian client retention</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-num"><span class="count" data-target="1200">0</span><span class="unit">+</span></div>
          <div class="hero-stat-label">Indian keywords ranking #1–3</div>
        </div>
      </div>
    </div>
    <div class="hero-badge" aria-hidden="true">
      <span class="ping"></span>
      <span>RANKING · INDIA · 24/7</span>
    </div>
  </header>

  <!-- =========================
       Marquee
       ========================= -->
  <div class="marquee" aria-hidden="true">
    <div class="marquee-track">
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Mumbai</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Bengaluru</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Delhi NCR</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Hyderabad</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Chennai</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Pune</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Kolkata</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Ahmedabad</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Gurugram</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Jaipur</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Lucknow</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Indore</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Kochi</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Chandigarh</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Mumbai</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Bengaluru</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Delhi NCR</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Hyderabad</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Chennai</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Pune</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Kolkata</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Ahmedabad</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Gurugram</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Jaipur</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Lucknow</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Indore</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Kochi</div>
      <div class="marquee-item"><strong>SEO</strong><span class="sep"></span>Chandigarh</div>
    </div>
  </div>

  <!-- =========================
       Capabilities
       ========================= -->
  <section id="capabilities">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Capabilities</span>
          <h2 class="display">Full-stack SEO,<br/><span class="gradient-text">engineered for India.</span></h2>
        </div>
        <p class="lede">Six disciplines. One team. We work as an embedded SEO partner — technical, content, authority, and GEO in lockstep, with measurable outcomes on every brief.</p>
      </div>

      <div class="services-grid reveal-stagger">
        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 01</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 3v18h18"/><path d="M7 14l4-4 4 4 5-5"/></svg>
          </div>
          <h3>Technical SEO for Indian scale</h3>
          <p>Crawl, render, index, and ship speed at Indian scale. Core Web Vitals tuned for 4G/5G, JavaScript rendering, schema.org, and CDN architecture for the subcontinent.</p>
          <div class="service-tags">
            <span class="service-tag">CWV</span>
            <span class="service-tag">Schema</span>
            <span class="service-tag">Hreflang</span>
            <span class="service-tag">JS SEO</span>
          </div>
          <a href="../contact.php" class="arrow-cta" data-cursor-hover aria-label="Start a project with rankfyno">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
        </div>

        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 02</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a13 13 0 010 18M12 3a13 13 0 000 18"/></svg>
          </div>
          <h3>Programmatic SEO, done right</h3>
          <p>Build thousands of high-intent pages without thin content. We've shipped 50,000+ programmatic URLs for Indian D2C, fintech, and marketplace clients.</p>
          <div class="service-tags">
            <span class="service-tag">Templates</span>
            <span class="service-tag">Datasets</span>
            <span class="service-tag">pSEO</span>
          </div>
          <a href="../contact.php" class="arrow-cta" data-cursor-hover aria-label="Start a project with rankfyno">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
        </div>

        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 03</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 1118 0z"/><circle cx="12" cy="10" r="3"/></svg>
          </div>
          <h3>Local SEO across 28 states</h3>
          <p>Google Business Profile, Bing Places, Apple Business Connect, Justdial, IndiaMART, and 80+ Indian directories. NAP consistency at scale, multilingual location pages.</p>
          <div class="service-tags">
            <span class="service-tag">GBP</span>
            <span class="service-tag">Citations</span>
            <span class="service-tag">Reviews</span>
          </div>
          <a href="#markets" class="arrow-cta" data-cursor-hover>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
        </div>

        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 04</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 2l3 7h7l-5.5 4.5L18 21l-6-4-6 4 1.5-7.5L2 9h7z"/></svg>
          </div>
          <h3>AI Search Optimization (GEO)</h3>
          <p>The first Indian agency shipping Generative Engine Optimization at production scale. Cited inside Google AI Overviews, ChatGPT, Perplexity, and Copilot.</p>
          <div class="service-tags">
            <span class="service-tag">AIO</span>
            <span class="service-tag">LLM</span>
            <span class="service-tag">llms.txt</span>
          </div>
          <a href="../contact.php" class="arrow-cta" data-cursor-hover aria-label="Start a project with rankfyno">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
        </div>

        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 05</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
          </div>
          <h3>Content in 11 languages</h3>
          <p>Native editors across English, Hindi, Tamil, Telugu, Bengali, Marathi, Gujarati, Kannada, Malayalam, Punjabi, and Odia. We engineer content that ranks AND reads native.</p>
          <div class="service-tags">
            <span class="service-tag">EN</span>
            <span class="service-tag">HI</span>
            <span class="service-tag">+9 more</span>
          </div>
          <a href="../contact.php" class="arrow-cta" data-cursor-hover aria-label="Start a project with rankfyno">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
        </div>

        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 06</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="1.5" stroke="currentColor"><path d="M10 13a5 5 0 007.54.54l3-3a5 5 0 00-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 00-7.54-.54l-3 3a5 5 0 007.07 7.07l1.71-1.71"/></svg>
          </div>
          <h3>Authority & Digital PR India</h3>
          <p>Backlinks from Livemint, Economic Times, Moneycontrol, YourStory, Inc42, Entrackr, and 200+ Indian publishers. Editorial coverage that moves the needle.</p>
          <div class="service-tags">
            <span class="service-tag">Digital PR</span>
            <span class="service-tag">Editorial</span>
            <span class="service-tag">HARO India</span>
          </div>
          <a href="../contact.php" class="arrow-cta" data-cursor-hover aria-label="Start a project with rankfyno">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- =========================
       Proof / Stats
       ========================= -->
  <section id="proof">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Proof in India</span>
          <h2 class="display">Eight years of<br/><span class="gradient-text">organic compounding in India.</span></h2>
        </div>
        <p class="lede">We don't do vanity metrics. Every campaign is wired to revenue, retention, and lifetime value — with reporting Indian leadership actually opens.</p>
      </div>

      <div class="stats-wrap">
        <div class="stats-grid reveal-stagger">
          <div class="stat-card">
            <div class="stat-num"><span class="grad">240</span><span class="stat-suffix">%</span></div>
            <div class="stat-label">Average return on organic investment for Indian clients in their first two quarters.</div>
          </div>
          <div class="stat-card">
            <div class="stat-num">₹<span class="grad">1,200</span><span class="stat-suffix">Cr+</span></div>
            <div class="stat-label">Indian revenue attributed to organic channels we've engineered since 2018.</div>
          </div>
          <div class="stat-card">
            <div class="stat-num"><span class="grad">92</span><span class="stat-suffix">%</span></div>
            <div class="stat-label">Retention rate across 8 years and 350+ Indian engagements.</div>
          </div>
          <div class="stat-card">
            <div class="stat-num"><span class="grad">1,200</span><span class="stat-suffix">+</span></div>
            <div class="stat-label">Indian keywords ranking in positions 1–3 on Google.co.in and Bing India.</div>
          </div>
        </div>

        <div class="why-pillars reveal-stagger">
          <div class="pillar">
            <div class="pillar-num">/ 01</div>
            <div>
              <h4>India-first, not India-translated</h4>
              <p>Native editors, regional keyword research, and content that understands Bharat — Tier 2/3 search behaviour, festival seasonality, and the language-mix reality of Indian search.</p>
            </div>
          </div>
          <div class="pillar">
            <div class="pillar-num">/ 02</div>
            <div>
              <h4>Senior strategists, no juniors</h4>
              <p>The strategist who pitches your audit is the same person shipping the work. No bait-and-switch, no offshore dilution. You get a senior SEO partner with 8+ years shipping for Indian brands.</p>
            </div>
          </div>
          <div class="pillar">
            <div class="pillar-num">/ 03</div>
            <div>
              <h4>Compounding, not chasing</h4>
              <p>We build owned organic channels that pay back for years — content assets, technical foundations, and a measurement layer you keep. Not rented rankings that vanish when the contract ends.</p>
            </div>
          </div>
          <div class="pillar">
            <div class="pillar-num">/ 04</div>
            <div>
              <h4>AI-search ready from day one</h4>
              <p>Every site we ship is optimized for Google AI Overviews, ChatGPT, Perplexity, and Copilot. As Indian search shifts to AI answers, your brand gets cited — not deprioritized.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- =========================
       India case studies
       ========================= -->
  <section id="case-studies">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> India case studies</span>
          <h2 class="display">Rankings that<br/><span class="gradient-text">moved Indian revenue.</span></h2>
        </div>
        <p class="lede">Three of dozens. Ask for the full Indian portfolio — D2C, B2B SaaS, fintech, healthcare, and listed enterprises.</p>
      </div>

      <div class="portfolio-grid reveal-stagger">
        <div class="project tall project-1" data-cursor-hover>
          <div class="project-bg"></div>
          <div class="project-inner">
            <div class="project-meta">
              <span class="project-tag">D2C · Programmatic SEO</span>
              <span class="project-year">Bengaluru · 2025</span>
            </div>
            <div class="project-content">
              <h3>12,400 SKUs to category #1 in 9 months</h3>
              <p>Built a programmatic SEO engine for a Bengaluru D2C brand — 12,400 unique product pages, original data, and 240 supporting articles. Outranked the category leader across 480 commercial keywords.</p>
              <div class="project-metric">
                <span class="project-metric-num">+412%</span>
                <span class="project-metric-label">organic revenue / 9 mo</span>
              </div>
            </div>
          </div>
        </div>

        <div class="project project-2" data-cursor-hover>
          <div class="project-bg"></div>
          <div class="project-inner">
            <div class="project-meta">
              <span class="project-tag">Fintech · Technical SEO</span>
              <span class="project-year">Mumbai · 2025</span>
            </div>
            <div class="project-content">
              <h3>From index bloat to 89 #1 rankings</h3>
              <p>Audited a listed fintech with 4M URLs, fixed JavaScript rendering, and consolidated authority into 2,400 strategic pages. Six months later, 89 keywords ranking #1 on Google.co.in.</p>
              <div class="project-metric">
                <span class="project-metric-num">+71%</span>
                <span class="project-metric-label">non-brand organic traffic</span>
              </div>
            </div>
          </div>
        </div>

        <div class="project project-3" data-cursor-hover>
          <div class="project-bg"></div>
          <div class="project-inner">
            <div class="project-meta">
              <span class="project-tag">Healthcare · Local SEO</span>
              <span class="project-year">Pan India · 2026</span>
            </div>
            <div class="project-content">
              <h3>240-clinic network, 1,200 GMB profiles</h3>
              <p>Standardized NAP across 240 clinics in 14 Indian cities, built city and condition pages in English + 6 regional languages, and shipped a review velocity engine. 3.4x lead volume from the local pack.</p>
              <div class="project-metric">
                <span class="project-metric-num">3.4×</span>
                <span class="project-metric-label">local pack leads</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- =========================
       India SEO Process
       ========================= -->
  <section id="process">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Our India SEO process</span>
          <h2 class="display">A 90-day path<br/><span class="gradient-text">from audit to #1 rankings.</span></h2>
        </div>
        <p class="lede">The same operating system that has produced 350+ Indian engagements. No mystery, no black box — and the measurement layer you keep is yours forever.</p>
      </div>

      <div class="process-list reveal-stagger">
        <div class="process-step" data-cursor-hover>
          <div class="process-num">01</div>
          <div class="process-title">
            <h3>Diagnose</h3>
            <p>Days 1–14 · India SEO audit</p>
          </div>
          <div class="process-desc">Full technical crawl of your Indian site, Google.co.in + Bing India SERP analysis, backlink profile audit, content gap mapping against the top 3 competitors, and a 40-page diagnostic with the 3 biggest unlocks sized in ₹.</div>
          <div class="process-cta">Audit <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </div>
        <div class="process-step" data-cursor-hover>
          <div class="process-num">02</div>
          <div class="process-title">
            <h3>Architect</h3>
            <p>Days 15–35 · Strategy & content plan</p>
          </div>
          <div class="process-desc">Keyword universe (10k–100k+ terms), search intent mapping, content architecture, programmatic SEO blueprint, internal linking graph, and a 12-month content calendar in EN + HI + relevant regional languages.</div>
          <div class="process-cta">Strategy <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </div>
        <div class="process-step" data-cursor-hover>
          <div class="process-num">03</div>
          <div class="process-title">
            <h3>Build</h3>
            <p>Days 36–60 · Ship technical, content, and authority</p>
          </div>
          <div class="process-desc">Core Web Vitals, schema, hreflang, internal linking, and template engines. Content produced by senior editors, not interns. Digital PR campaigns in parallel — 8–12 high-authority Indian placements in the first 60 days.</div>
          <div class="process-cta">Build <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </div>
        <div class="process-step" data-cursor-hover>
          <div class="process-num">04</div>
          <div class="process-title">
            <h3>Compound</h3>
            <p>Days 61–90+ · Optimize, scale, dominate</p>
          </div>
          <div class="process-desc">Weekly experiments, monthly review with your leadership, and a quarterly compounding plan. We stay as long as the math keeps working — most Indian clients retain us 2+ years.</div>
          <div class="process-cta">Scale <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </div>
      </div>
    </div>
  </section>

  <!-- =========================
       Testimonials — India
       ========================= -->
  <section>
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Indian client voices</span>
          <h2 class="display">Founders & CMOs<br/><span class="gradient-text">who build with us.</span></h2>
        </div>
        <p class="lede">From listed enterprises in Mumbai to D2C founders in Bengaluru — the leaders who keep rankfyno on retainer.</p>
      </div>

      <div class="testimonial-stage reveal">
        <div class="testimonial-track" id="testimonial-track">
          <div class="testimonial active">
            <p class="testimonial-quote">"rankfyno rebuilt our organic engine in 6 months. We went from 80k to 1.2M monthly organic sessions, with 38% of new pipeline now coming from SEO. The senior team is genuinely senior — no bait-and-switch, no offshore dilution. Best SEO partner we've worked with in India."</p>
            <div class="testimonial-author">
              <div class="testimonial-avatar">RM</div>
              <div>
                <div class="testimonial-name">Rohan Mehta</div>
                <div class="testimonial-role">CMO, Bharat fintech unicorn · Mumbai</div>
              </div>
            </div>
          </div>
          <div class="testimonial">
            <p class="testimonial-quote">"We're a 12-person D2C brand out of Bengaluru. rankfyno runs programmatic SEO for our 12,400 SKUs and a content engine in EN + HI. 9 months in, we outrank the category leader on 480 commercial keywords. The compounding math just works."</p>
            <div class="testimonial-author">
              <div class="testimonial-avatar">PS</div>
              <div>
                <div class="testimonial-name">Priya Subramanian</div>
                <div class="testimonial-role">Founder & CEO, D2C home brand · Bengaluru</div>
              </div>
            </div>
          </div>
          <div class="testimonial">
            <p class="testimonial-quote">"We hired rankfyno for technical SEO, but what we got was an organic growth system. Their GEO work put us inside ChatGPT and Google AI Overviews ahead of every listed competitor. The team understands AI search in a way no other Indian agency does."</p>
            <div class="testimonial-author">
              <div class="testimonial-avatar">AK</div>
              <div>
                <div class="testimonial-name">Arjun Kapoor</div>
                <div class="testimonial-role">VP Growth, listed SaaS company · Gurugram</div>
              </div>
            </div>
          </div>
          <div class="testimonial">
            <p class="testimonial-quote">"We've worked with 4 SEO agencies in India over 6 years. rankfyno is the first one that actually moved the number. They treat our brand like it's theirs, push back when we ask for the wrong things, and ship like a senior team should."</p>
            <div class="testimonial-author">
              <div class="testimonial-avatar">VD</div>
              <div>
                <div class="testimonial-name">Vikram Desai</div>
                <div class="testimonial-role">Founder, healthcare network · Pan-India</div>
              </div>
            </div>
          </div>
        </div>
        <div class="testimonial-controls">
          <div class="testimonial-dots" id="testimonial-dots">
            <button class="dot-btn active" data-cursor-hover aria-label="Quote 1"></button>
            <button class="dot-btn" data-cursor-hover aria-label="Quote 2"></button>
            <button class="dot-btn" data-cursor-hover aria-label="Quote 3"></button>
            <button class="dot-btn" data-cursor-hover aria-label="Quote 4"></button>
          </div>
          <div class="testimonial-nav">
            <button class="nav-btn" id="t-prev" data-cursor-hover aria-label="Previous">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            </button>
            <button class="nav-btn" id="t-next" data-cursor-hover aria-label="Next">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>

  

  <!-- =========================
       Markets we serve
       ========================= -->
  <section id="markets">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Markets we serve</span>
          <h2 class="display">Local SEO hubs<br/><span class="gradient-text">in every market we enter.</span></h2>
        </div>
        <p class="lede">When we open a market, we open it properly — dedicated local SEO programs, country-level landing pages, GBP optimization, and market-specific case studies. Each market runs on a single, indexable hub-and-spoke architecture.</p>
      </div>

      <h3 class="reveal" style="font-family: 'Space Grotesk', sans-serif; font-size: 22px; margin: 40px 0 24px; color: var(--ink-0); letter-spacing: -0.01em;">/ Active markets</h3>
      <div class="city-grid reveal-stagger">
        <a href="../seo/india/" class="city-card" data-cursor-hover>
          <span class="city-tier">Live</span>
          <h3>India</h3>
          <p>28 states · 8 union territories · 22 official languages · 22 Haryana districts live. Our flagship market — 350+ engagements, ₹1,200 Cr+ attributed revenue.</p>
          <div class="city-cta">Explore India <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </a>
        <a href="../contact.php" class="city-card" data-cursor-hover>
          <span class="city-tier">Q4 2026</span>
          <h3>United States</h3>
          <p>Coast-to-coast coverage. New York, San Francisco, Austin, Miami, Chicago. EN + ES multi-lingual from day one.</p>
          <div class="city-cta">Get notified <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </a>
        <a href="../contact.php" class="city-card" data-cursor-hover>
          <span class="city-tier">Q1 2027</span>
          <h3>United Kingdom</h3>
          <p>London, Manchester, Edinburgh, Bristol. EN-native editors, GBP + Bing Places + Apple Business Connect from day one.</p>
          <div class="city-cta">Get notified <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </a>
      </div>

      <h3 class="reveal" style="font-family: 'Space Grotesk', sans-serif; font-size: 22px; margin: 56px 0 24px; color: var(--ink-0); letter-spacing: -0.01em;">/ Pipeline — 2027</h3>
      <div class="city-grid reveal-stagger">
        <a href="../contact.php" class="city-card" data-cursor-hover>
          <span class="city-tier">Pipeline</span>
          <h3>UAE &amp; Saudi Arabia</h3>
          <p>Dubai, Abu Dhabi, Riyadh, Jeddah. EN + AR + HI editors, regional search-engine optimization for 35M+ expat population.</p>
          <div class="city-cta">Express interest <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </a>
        <a href="../contact.php" class="city-card" data-cursor-hover>
          <span class="city-tier">Pipeline</span>
          <h3>Singapore &amp; Southeast Asia</h3>
          <p>Singapore, Kuala Lumpur, Jakarta, Bangkok. EN-native with regional SEA language support. Fintech, B2B SaaS, and D2C focus.</p>
          <div class="city-cta">Express interest <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </a>
        <a href="../contact.php" class="city-card" data-cursor-hover>
          <span class="city-tier">Pipeline</span>
          <h3>Australia &amp; New Zealand</h3>
          <p>Sydney, Melbourne, Auckland. EN-native, AU/NZ-specific search behavior, Bing + Google parity optimization.</p>
          <div class="city-cta">Express interest <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </a>
      </div>

      <p style="margin-top: 56px; font-family: 'JetBrains Mono', monospace; font-size: 13px; color: var(--ink-1); letter-spacing: 0.02em;">Don't see your market? <a href="../contact.php" style="color: var(--accent); text-decoration: underline; text-underline-offset: 4px;">Tell us where you operate</a> — we open 2–3 new markets per year based on client demand.</p>
    </div>
  </section>

  <!-- =========================
       FAQ
       ========================= -->
  <section id="faq">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> FAQ — India SEO</span>
          <h2 class="display">The questions<br/><span class="gradient-text">Indian leaders ask first.</span></h2>
        </div>
        <p class="lede">If you don't see your question here, send a note — we usually reply the same day, IST-friendly hours.</p>
      </div>

      <div class="faq-list reveal-stagger">
        <div class="faq-item open">
          <button class="faq-q" data-cursor-hover>
            Who is the best SEO agency in India?
            <span class="icon"></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner">rankfyno is widely regarded as the best SEO agency in India for ambitious brands. We combine senior-only teams, technical SEO, programmatic content, and Generative Engine Optimization (GEO) to rank brands on Google's first page and inside AI search answers (ChatGPT, Perplexity, Google AI Overviews). 92% of our Indian clients retain us beyond 12 months, and we've shipped organic growth for D2C, fintech, SaaS, and listed enterprises across the country.</div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" data-cursor-hover>
            How much does SEO cost in India?
            <span class="icon"></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner">SEO retainers in India range from ₹40,000/month for local campaigns to ₹5,00,000+/month for enterprise and programmatic builds. rankfyno engagements start at ₹85,000/month for Foundation and ₹1,85,000/month for Growth, with a 90-day minimum. All pricing is exclusive of GST. We size the engagement against your category competitiveness and revenue ambition — never a one-size-fits-all quote.</div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" data-cursor-hover>
            How long does SEO take to show results in India?
            <span class="icon"></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner">Most rankfyno Indian clients see meaningful ranking movement in 60–90 days and category-leading positions in 6–9 months. India is a hyper-competitive market — fast compounding requires technical excellence, original content, and authority that scales. We'll be honest with you in the first 14 days about the timeline based on your category, domain authority, and content velocity.</div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" data-cursor-hover>
            Do you offer local SEO for Indian cities?
            <span class="icon"></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner">Yes. We run dedicated local SEO programs for Indian cities and states — including Panipat, Gurugram, Faridabad, Mumbai, Bengaluru, Delhi, Hyderabad, Chennai, and 40+ others. Local pages are built on a single, indexable hub-and-spoke structure with NAP consistency, Google Business Profile optimization, Bing Places, Apple Business Connect, Justdial, IndiaMART, and review velocity programs that move the local pack.</div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" data-cursor-hover>
            What is Generative Engine Optimization (GEO) and do you offer it in India?
            <span class="icon"></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner">GEO is the practice of optimizing content to be cited inside AI search answers — Google AI Overviews, ChatGPT search, Perplexity, and Copilot. 38% of Indian queries now touch an AI answer. rankfyno is one of the few Indian agencies shipping GEO alongside traditional SEO at production scale — llms.txt, passage-level citability, structured citations, and brand mention signals across the AI web.</div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" data-cursor-hover>
            Do you work with Indian languages beyond English and Hindi?
            <span class="icon"></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner">Yes. We have native editors across English, Hindi, Tamil, Telugu, Bengali, Marathi, Gujarati, Kannada, Malayalam, Punjabi, and Odia. We don't just translate — we engineer content that ranks and reads like it was originally written for the audience, with proper hreflang implementation and regional keyword research.</div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" data-cursor-hover>
            Do you replace our in-house marketing team?
            <span class="icon"></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner">No. We embed as a senior SEO partner — extending your in-house marketers, content team, or founder with specialist capacity, a measurement layer, and a compounding system you keep. Most of our Indian clients have an in-house marketer or growth lead doing the day-to-day; we extend them with senior specialist capacity and a system to run on.</div></div>
        </div>
        <div class="faq-item">
          <button class="faq-q" data-cursor-hover>
            Where is your India team based?
            <span class="icon"></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner">Our India operations are led from Gurugram (Cyber Hub) with senior team members in Mumbai, Bengaluru, Hyderabad, and Chennai. We work IST-friendly hours with async-first collaboration and weekly syncs in your timezone. Senior strategists only — no junior bait-and-switch, no offshore dilution.</div></div>
        </div>
      </div>
    </div>
  </section>

  <!-- =========================
       CTA
       ========================= -->
  <div class="cta-wrap" id="cta">
    <div class="container">
      <div class="reveal">
        <span class="eyebrow"><span class="dot"></span> Ready when you are</span>
        <h2 class="display">Let's rank your brand<br/><span class="gradient-text">#1 across India.</span></h2>
        <p>Tell us about your business. We'll come back inside 24 hours with a 2-page India SEO audit and a 90-day plan — even if we end up referring you somewhere else.</p>
        <a href="../contact.php" class="cta-mega-btn" data-cursor-hover>
          <span>Start a project</span>
          <span class="arrow-circle">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </span>
        </a>
      </div>
    </div>
  </div>

  <!-- =========================
       Footer
       ========================= -->
  <?php
include $base_path . 'footer.php';
?>
