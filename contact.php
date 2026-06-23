<?php
$base_path = '';
$current_page = 'contact';
$page_title = 'Contact — rankfyno';
$page_description = "Get in touch with rankfyno — start a project, request a proposal, or just say hello. We respond within 24 hours, every time.";
$custom_body_elements = '<canvas id="webgl-canvas" aria-hidden="true"></canvas>';
include __DIR__ . '/header.php';
?>

  <!-- =========================
       Hero
       ========================= -->
  <header class="hero" style="min-height: 70vh; padding: 180px 0 60px;">
    <div class="container hero-inner">
      <div class="hero-meta">
        <div class="hero-meta-left">
          <span class="eyebrow"><span class="dot"></span> Now booking Q3 2026</span>
          <div class="hero-meta-divider"></div>
          <div class="hero-meta-info">SFO · NYC · LDN — 24/7</div>
        </div>
        <div class="hero-meta-info">/ contact / v.07</div>
      </div>

      <h1 class="display">
        <div class="word"><span class="char">L</span><span class="char">e</span><span class="char">t</span><span class="char">'</span><span class="char">s</span></div>
        <div class="word"><span class="char gradient-text">s</span><span class="char gradient-text">t</span><span class="char gradient-text">a</span><span class="char gradient-text">r</span><span class="char gradient-text">t</span></div>
        <div class="word"><span class="char outline-text">s</span><span class="char outline-text">o</span><span class="char outline-text">m</span><span class="char outline-text">e</span><span class="char outline-text">t</span><span class="char outline-text">h</span><span class="char outline-text">i</span><span class="char outline-text">n</span><span class="char outline-text">g</span><span class="char">.</span></div>
      </h1>

      <p class="hero-sub">Tell us about the brief. We respond within 24 hours with a 2-page plan — even if we end up referring you somewhere else. No fluff, no chase, no pressure.</p>

      <div class="hero-cta">
        <a href="#contact-form" class="btn btn-primary" data-cursor-hover>
          Start a project
          <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </a>
        <a href="mailto:hello@rankfyno.com" class="btn btn-ghost" data-cursor-hover>
          Email us directly
        </a>
      </div>
    </div>
  </header>

  <!-- =========================
       Contact Section
       ========================= -->
  <section id="contact-form" style="padding: 100px 0 120px;">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Get in touch</span>
          <h2 class="display">Tell us about <br/><span class="gradient-text">your project.</span></h2>
        </div>
        <p class="lede">The more you share, the better we can prepare. We read every form ourselves — no auto-replies, no SDR funnels.</p>
      </div>

      <div class="contact-grid reveal-stagger">
        <!-- Form -->
        <form class="contact-form" onsubmit="event.preventDefault(); alert('Thanks! We\'ll be in touch within 24 hours.');">
          <div class="form-row">
            <div class="form-field">
              <label for="name">Your name *</label>
              <input type="text" id="name" name="name" required placeholder="Jane Cooper" />
            </div>
            <div class="form-field">
              <label for="email">Email *</label>
              <input type="email" id="email" name="email" required placeholder="jane@company.com" />
            </div>
          </div>

          <div class="form-row">
            <div class="form-field">
              <label for="company">Company</label>
              <input type="text" id="company" name="company" placeholder="Acme Inc." />
            </div>
            <div class="form-field">
              <label for="budget">Budget range</label>
              <select id="budget" name="budget">
                <option value="">Select a range</option>
                <option value="10-25k">$10k – $25k</option>
                <option value="25-50k">$25k – $50k</option>
                <option value="50-100k">$50k – $100k</option>
                <option value="100k+">$100k+</option>
                <option value="not-sure">Not sure yet</option>
              </select>
            </div>
          </div>

          <div class="form-field">
            <label for="service">What do you need help with? *</label>
            <select id="service" name="service" required>
              <option value="">Select a service</option>
              <option value="performance">Performance Marketing</option>
              <option value="seo">SEO & Organic Growth</option>
              <option value="brand">Brand & Identity</option>
              <option value="ai">AI Marketing & Automation</option>
              <option value="web">Web & Product Design</option>
              <option value="other">Something else</option>
            </select>
          </div>

          <div class="form-field">
            <label for="message">Tell us about the project *</label>
            <textarea id="message" name="message" rows="6" required placeholder="What are you working on? Goals, timeline, anything that helps us prepare a useful reply."></textarea>
          </div>

          <button type="submit" class="btn btn-primary form-submit" data-cursor-hover>
            Send the brief
            <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </button>

          <p class="form-note">We reply within 24 hours, Monday–Friday. Your details stay with us — we never share or sell.</p>
        </form>

        <!-- Sidebar -->
        <aside class="contact-aside">
          <div class="contact-card">
            <h5>Direct line</h5>
            <a href="mailto:hello@rankfyno.com" class="contact-link" data-cursor-hover>hello@rankfyno.com</a>
            <a href="tel:+917317564794" class="contact-link" data-cursor-hover>+91 7317564794</a>
          </div>

          <div class="contact-card">
            <h5>Studio</h5>
            <div class="contact-locations">
              <div>
                <strong>Gurugram</strong>
                <p>Ground Floor, Cabin no 12, Plot 84, SupremeWork, Sector 32, Gurugram, Haryana 122001</p>
              </div>
            </div>
          </div>

          <div class="contact-card">
            <h5>For press</h5>
            <a href="mailto:hello@rankfyno.com" class="contact-link" data-cursor-hover>hello@rankfyno.com</a>
          </div>

          <div class="contact-card">
            <h5>For careers</h5>
            <a href="mailto:careers@rankfyno.com" class="contact-link" data-cursor-hover>careers@rankfyno.com</a>
            <p class="contact-sub">We're hiring across strategy, design, and engineering.</p>
          </div>
        </aside>
      </div>
    </div>
  </section>

<?php
include __DIR__ . '/footer.php';
?>
