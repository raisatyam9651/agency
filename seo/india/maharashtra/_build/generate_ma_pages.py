import os
import sys

# Ensure build directory path is in search path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ma_districts import DISTRICTS, CATEGORIES_COPIES

# HTML template for the 35 district pages
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="theme-color" content="#0a0a0a" />

  <!-- SEO: Primary meta -->
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="SEO agency {name}, SEO company {name}, {name} SEO services, local SEO {name}, technical SEO, content SEO, NEXUS SEO" />
  <meta name="author" content="NEXUS Studio" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <link rel="canonical" href="https://nexus.studio/seo/india/maharashtra/{slug}/" />

  <!-- SEO: OpenGraph -->
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="NEXUS Studio" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{og_description}" />
  <meta property="og:url" content="https://nexus.studio/seo/india/maharashtra/{slug}/" />
  <meta property="og:locale" content="en_IN" />
  <meta property="og:image" content="https://nexus.studio/seo/india/maharashtra/images/hero.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="675" />
  <meta property="og:image:alt" content="NEXUS SEO Agency {name} — engineering organic growth" />

  <!-- SEO: Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:site" content="@nexusstudio" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:description" content="{twitter_description}" />
  <meta name="twitter:image" content="https://nexus.studio/seo/india/maharashtra/images/hero.jpg" />

  <!-- SEO: Geo -->
  <meta name="geo.region" content="IN-MH" />
  <meta name="geo.placename" content="{name}" />
  <meta name="geo.position" content="{lat};{lng}" />
  <meta name="ICBM" content="{lat}, {lng}" />

  <!-- Performance: preconnect -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />

  <!-- Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />

  <!-- Stylesheet -->
  <link rel="stylesheet" href="../../../../style.css" />

  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "NEXUS Studio",
    "alternateName": "NEXUS",
    "url": "https://nexus.studio/",
    "logo": "https://nexus.studio/logo.png",
    "description": "Performance-driven SEO, content, and digital growth agency for ambitious brands across India and globally.",
    "address": {{
      "@type": "PostalAddress",
      "addressCountry": "IN",
      "addressRegion": "Maharashtra",
      "addressLocality": "{name}"
    }}
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "serviceType": "Search Engine Optimization (SEO)",
    "name": "NEXUS SEO Services in {name}",
    "provider": {{
      "@type": "Organization",
      "name": "NEXUS Studio",
      "url": "https://nexus.studio/"
    }},
    "areaServed": {{
      "@type": "City",
      "name": "{name}",
      "sameAs": "https://en.wikipedia.org/wiki/{wiki_name}"
    }},
    "hasOfferCatalog": {{
      "@type": "OfferCatalog",
      "name": "NEXUS {name} SEO Plans",
      "itemListElement": [
        {{ "@type": "Offer", "name": "Local SEO {name}", "price": "30000", "priceCurrency": "INR" }},
        {{ "@type": "Offer", "name": "Growth SEO {name}", "price": "65000", "priceCurrency": "INR" }},
        {{ "@type": "Offer", "name": "Authority SEO {name}", "price": "150000", "priceCurrency": "INR" }}
      ]
    }}
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://nexus.studio/" }},
      {{ "@type": "ListItem", "position": 2, "name": "SEO in India", "item": "https://nexus.studio/seo/india/" }},
      {{ "@type": "ListItem", "position": 3, "name": "Maharashtra", "item": "https://nexus.studio/seo/india/maharashtra/" }},
      {{ "@type": "ListItem", "position": 4, "name": "{name}", "item": "https://nexus.studio/seo/india/maharashtra/{slug}/" }}
    ]
  }}
  </script>

  {faq_json_ld}
</head>
<body>
  <div class="ambient" aria-hidden="true"></div>
  <div class="grid-overlay" aria-hidden="true"></div>
  <div class="cursor" id="cursor" aria-hidden="true"></div>
  <div class="cursor-follower" id="cursor-follower" aria-hidden="true"></div>

  <!-- Navigation -->
  <nav class="nav" id="nav">
    <div class="container nav-inner">
      <a href="../../../../index.html" class="logo" data-cursor-hover>
        <div class="logo-mark"></div>
        NEXUS
      </a>
      <ul class="nav-links">
        <li><a href="../../../../index.html#services" data-cursor-hover>Services</a></li>
        <li><a href="../../../../index.html#work" data-cursor-hover>Work</a></li>
        <li><a href="../../../../index.html#process" data-cursor-hover>Process</a></li>
        <li><a href="../../../../index.html#pricing" data-cursor-hover>Pricing</a></li>
        <li><a href="../index.html" data-cursor-hover>Maharashtra</a></li>
        <li><a href="../../../../contact.html" data-cursor-hover>Contact</a></li>
      </ul>
      <div class="nav-divider"></div>
      <div class="nav-cta">
        <a href="../../../../contact.html" class="btn btn-primary" data-cursor-hover>
          Start a project
          <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </a>
        <button class="menu-toggle" data-cursor-hover aria-label="Menu"><span></span></button>
      </div>
    </div>
  </nav>

  <!-- Hero Section -->
  <header class="hero">
    <div class="container hero-inner">
      <div class="hero-image-wrap">
        <picture>
          <img src="../images/hero.jpg" alt="Best SEO Company in {name} — NEXUS organic growth trophy" class="hero-image" loading="eager" width="1280" height="720" />
        </picture>
      </div>

      <div class="hero-meta">
        <div class="hero-meta-left">
          <span class="eyebrow"><span class="dot"></span> {eyebrow_left}</span>
        </div>
        <div class="hero-meta-info">{eyebrow_right}</div>
      </div>

      <h1 class="display">
        <div class="word"><span class="char">S</span><span class="char">E</span><span class="char">O</span></div>
        <div class="word"><span class="char gradient-text">i</span><span class="char gradient-text">n</span></div>
        <div class="word">{char_spans}</div>
      </h1>

      <p class="hero-sub">{hero_sub}</p>

      <div class="hero-cta">
        <a href="../../../../contact.html" class="btn btn-primary" data-cursor-hover>
          Start a project
          <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </a>
        <a href="../index.html" class="btn btn-ghost" data-cursor-hover>All Maharashtra districts</a>
      </div>

      <div class="hero-stats reveal-stagger">
        <div class="hero-stat">
          <div class="hero-stat-num"><span class="count" data-target="{hero_stat_1_target}">0</span><span class="unit">+</span></div>
          <div class="hero-stat-label">{name} projects</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-num"><span class="count" data-target="6">0</span></div>
          <div class="hero-stat-label">Years in market</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-num"><span class="count" data-target="5.8" data-decimal="1">0</span><span class="unit">×</span></div>
          <div class="hero-stat-label">Avg. ROI multiplier</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-num"><span class="count" data-target="75">0</span></div>
          <div class="hero-stat-label">Days to page-1</div>
        </div>
      </div>
    </div>
    <div class="hero-badge" aria-hidden="true">
      <span class="ping"></span>
      <span>RANKING ENGINE ONLINE</span>
    </div>
  </header>

  <!-- Infinite Marquee -->
  <div class="marquee" aria-hidden="true">
    <div class="marquee-track">
      <div class="marquee-item"><strong>Local SEO</strong><span class="sep"></span>Google Business Profile</div>
      <div class="marquee-item"><strong>National SEO</strong><span class="sep"></span>Topical Authority</div>
      <div class="marquee-item"><strong>E-commerce SEO</strong><span class="sep"></span>Shopify &amp; WooCommerce</div>
      <div class="marquee-item"><strong>Multilingual</strong><span class="sep"></span>Hindi · Tamil · Telugu · Bengali</div>
      <div class="marquee-item"><strong>Technical</strong><span class="sep"></span>Core Web Vitals</div>
      <div class="marquee-item"><strong>Content</strong><span class="sep"></span>Editorial Systems</div>
      <div class="marquee-item"><strong>Digital PR</strong><span class="sep"></span>Authority Building</div>
      <div class="marquee-item"><strong>Local SEO</strong><span class="sep"></span>Google Business Profile</div>
      <div class="marquee-item"><strong>National SEO</strong><span class="sep"></span>Topical Authority</div>
      <div class="marquee-item"><strong>E-commerce SEO</strong><span class="sep"></span>Shopify &amp; WooCommerce</div>
      <div class="marquee-item"><strong>Multilingual</strong><span class="sep"></span>Hindi · Tamil · Telugu · Bengali</div>
      <div class="marquee-item"><strong>Technical</strong><span class="sep"></span>Core Web Vitals</div>
      <div class="marquee-item"><strong>Content</strong><span class="sep"></span>Editorial Systems</div>
      <div class="marquee-item"><strong>Digital PR</strong><span class="sep"></span>Authority Building</div>
    </div>
  </div>

  <!-- Capabilities Section -->
  <section id="capabilities" style="padding: 80px 0;">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> What's included</span>
          <h2 class="display">Local SEO, <span class="gradient-text">engineered.</span></h2>
        </div>
        <p class="lede">Six disciplines, one team. We work as an embedded SEO partner for local businesses — technical, content, and authority in lockstep, with measurable outcomes on every brief.</p>
      </div>

      <div class="services-grid reveal-stagger" style="margin-top: 60px;">
        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 01</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          </div>
          <h3>Local audit</h3>
          <p>Full technical + on-page + GBP audit for {name} — competitor, citation, content &amp; link gap analysis.</p>
          <div class="service-tags">
            <span class="service-tag">GBP</span>
            <span class="service-tag">Citations</span>
            <span class="service-tag">Audit</span>
          </div>
        </div>

        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 02</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
          </div>
          <h3>Keyword research</h3>
          <p>Local-intent keyword map for {name} buyers — service, brand, and "{name} near me" intent layered.</p>
          <div class="service-tags">
            <span class="service-tag">Keywords</span>
            <span class="service-tag">Intent</span>
            <span class="service-tag">Bilingual</span>
          </div>
        </div>

        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 03</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 1 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
          </div>
          <h3>On-page SEO</h3>
          <p>Title, schema (LocalBusiness), content, internal linking, and Hindi-English bilingual meta.</p>
          <div class="service-tags">
            <span class="service-tag">Meta</span>
            <span class="service-tag">Schema</span>
            <span class="service-tag">Content</span>
          </div>
        </div>

        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 04</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M16 2v2M8 2v2M3 10h18"/></svg>
          </div>
          <h3>Local citations</h3>
          <p>Top Indian + global directories, NAP-consistent across {name} and Maharashtra state listings.</p>
          <div class="service-tags">
            <span class="service-tag">NAP</span>
            <span class="service-tag">Citations</span>
            <span class="service-tag">Directories</span>
          </div>
        </div>

        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 05</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="M3.27 6.96L12 12.01l8.73-5.05M12 22.08V12"/></svg>
          </div>
          <h3>Google Business</h3>
          <p>GBP setup &amp; optimization — categories, services, photo cadence, weekly Google Posts.</p>
          <div class="service-tags">
            <span class="service-tag">GBP</span>
            <span class="service-tag">Google Maps</span>
            <span class="service-tag">Optimization</span>
          </div>
        </div>

        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 06</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 3v18h18"/><path d="M18.7 8l-5.1 5.2-2.8-2.7L7 14.3"/></svg>
          </div>
          <h3>Reporting</h3>
          <p>Monthly ranking + traffic + lead report — your {name} SERP visibility at a glance.</p>
          <div class="service-tags">
            <span class="service-tag">Report</span>
            <span class="service-tag">Metrics</span>
            <span class="service-tag">Revenue</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Why Section -->
  <section style="padding: 80px 0; border-top: 1px solid var(--border);">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Why {name}</span>
          <h2 class="display">{tagline}</h2>
        </div>
        <p class="lede">SEO in {name} isn't generic — it follows the local economy, the buyer language, and the way people here actually search. We engineer around all three.</p>
      </div>

      <div class="why-pillars reveal-stagger" style="margin-top: 60px;">
{why_features_html}
      </div>
    </div>
  </section>

  <!-- Process Section -->
  <section style="padding: 80px 0; border-top: 1px solid var(--border);">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> How we work</span>
          <h2 class="display">From audit <span class="gradient-text">to page-1.</span></h2>
        </div>
        <p class="lede">A structured, transparent process built to compound your rankings, traffic, and leads.</p>
      </div>

      <div class="process-list reveal-stagger" style="margin-top: 60px;">
        <div class="process-step" data-cursor-hover>
          <div class="process-num">01</div>
          <div class="process-title">
            <h3>Audit &amp; keyword map</h3>
            <p>Days 1–14 · Analysis</p>
          </div>
          <div class="process-desc">Technical, on-page, GBP, citation, competitor &amp; content audit. We deliver a {name}-specific keyword map in 7 days.</div>
          <div class="process-cta">Diagnostic <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </div>

        <div class="process-step" data-cursor-hover>
          <div class="process-num">02</div>
          <div class="process-title">
            <h3>Quick wins (0-30d)</h3>
            <p>Days 15–35 · Launch</p>
          </div>
          <div class="process-desc">GBP fix, on-page corrections, top citation submissions, schema, internal link rewire — early movement in {name} SERPs.</div>
          <div class="process-cta">Foundation <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </div>

        <div class="process-step" data-cursor-hover>
          <div class="process-num">03</div>
          <div class="process-title">
            <h3>Content &amp; authority (30-90d)</h3>
            <p>Days 36–60 · Growth</p>
          </div>
          <div class="process-desc">City &amp; service landing pages, monthly content, niche edits, digital PR — building topical authority for {name}.</div>
          <div class="process-cta">Authority <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </div>

        <div class="process-step" data-cursor-hover>
          <div class="process-num">04</div>
          <div class="process-title">
            <h3>Scale &amp; defend (90d+)</h3>
            <p>Days 61–90+ · Compound</p>
          </div>
          <div class="process-desc">Continuous link acquisition, content refresh, CRO, and defending rankings in {name} against new entrants.</div>
          <div class="process-cta">Scale <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </div>
      </div>
    </div>
  </section>

  <!-- Pricing Section -->
  <section style="padding: 80px 0; border-top: 1px solid var(--border);">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Pricing</span>
          <h2 class="display">Plans for <span class="gradient-text">{name}.</span></h2>
        </div>
        <p class="lede">Transparent monthly retainers. No lock-ins. Cancel any time with 30 days notice.</p>
      </div>

      <div class="pricing-grid reveal-stagger" style="margin-top: 60px;">
        <div class="price-card" data-tilt data-cursor-hover>
          <span class="price-name">Local</span>
          <div class="price-amount">
            <span class="num">₹30K</span>
            <span class="unit">/mo</span>
          </div>
          <p class="price-desc">{pricing_desc_local}</p>
          <div class="price-features">
            <div class="price-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              <span>Technical + on-page audit</span>
            </div>
            <div class="price-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              <span>GBP setup &amp; optimization</span>
            </div>
            <div class="price-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              <span>20 local citations</span>
            </div>
            <div class="price-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              <span>4 localized service pages</span>
            </div>
            <div class="price-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              <span>Monthly reporting &amp; mapping</span>
            </div>
          </div>
          <a href="../../../../contact.html" class="btn btn-ghost" data-cursor-hover>Start a project</a>
        </div>

        <div class="price-card featured" data-tilt data-cursor-hover>
          <span class="price-name">Growth</span>
          <div class="price-amount">
            <span class="num">₹65K</span>
            <span class="unit">/mo</span>
          </div>
          <p class="price-desc">{pricing_desc_growth}</p>
          <div class="price-features">
            <div class="price-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              <span>Everything in Local</span>
            </div>
            <div class="price-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              <span>12 content pieces / month</span>
            </div>
            <div class="price-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              <span>8 niche edits + digital PR</span>
            </div>
            <div class="price-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              <span>Multi-location GBP strategy</span>
            </div>
            <div class="price-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              <span>Conversion tracking &amp; CRO</span>
            </div>
          </div>
          <a href="../../../../contact.html" class="btn btn-primary" data-cursor-hover>Start a project</a>
        </div>

        <div class="price-card" data-tilt data-cursor-hover>
          <span class="price-name">Authority</span>
          <div class="price-amount">
            <span class="num">Custom</span>
          </div>
          <p class="price-desc">{pricing_desc_authority}</p>
          <div class="price-features">
            <div class="price-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              <span>Everything in Growth</span>
            </div>
            <div class="price-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              <span>Dedicated SEO strategist</span>
            </div>
            <div class="price-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              <span>Full content + design team support</span>
            </div>
            <div class="price-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              <span>Aggressive digital PR &amp; link build</span>
            </div>
            <div class="price-feature">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>
              <span>Weekly executive reports &amp; dashboards</span>
            </div>
          </div>
          <a href="../../../../contact.html" class="btn btn-ghost" data-cursor-hover>Talk to us</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Siblings Section -->
  <section style="padding: 80px 0; border-top: 1px solid var(--border);">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Other Maharashtra districts</span>
          <h2 class="display">Explore <span class="gradient-text">neighbouring markets.</span></h2>
        </div>
        <p class="lede">Expand your digital footprint. We cover all major commercial hubs and districts across Maharashtra.</p>
      </div>

      <div class="pricing-grid reveal-stagger" style="margin-top: 60px;">
{siblings_html}
      </div>

      <div style="text-align: center; margin-top: 50px;">
        <a href="../index.html" class="btn btn-ghost" data-cursor-hover>
          View all Maharashtra districts
          <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </a>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section id="faq" style="padding: 80px 0; border-top: 1px solid var(--border);">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> FAQ</span>
          <h2 class="display">Common <span class="gradient-text">questions.</span></h2>
        </div>
        <p class="lede">Answers to standard questions about our local SEO campaigns in {name} and Maharashtra.</p>
      </div>

      <div class="faq-list reveal-stagger" style="margin-top: 60px; max-width: 800px; margin-left: auto; margin-right: auto;">
{faq_html}
      </div>
    </div>
  </section>

  <!-- Testimonials Section -->
  <section style="padding: 80px 0; border-top: 1px solid var(--border);">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Client voices</span>
          <h2 class="display">Operators who<br/><span class="gradient-text">build with us in {name}.</span></h2>
        </div>
        <p class="lede">Hear from local business owners, coaches, and directors in {name} who rank on page-1.</p>
      </div>

      <div class="testimonial-stage reveal" style="margin-top: 60px;">
        <div class="testimonial-track" id="testimonial-track">
          <div class="testimonial active">
            <p class="testimonial-quote">"{testimonial_city_specific}"</p>
            <div class="testimonial-author">
              <div class="testimonial-avatar">{testimonial_avatar}</div>
              <div>
                <div class="testimonial-name">{testimonial_author}</div>
                <div class="testimonial-role">{testimonial_role}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Section -->
  <div class="cta-wrap" id="cta">
    <div class="container">
      <div class="reveal" style="text-align: center;">
        <span class="eyebrow"><span class="dot"></span> Ready to rank in {name}?</span>
        <h2 class="display" style="margin-top: 30px;">Let's get your {name} business<br /><span class="gradient-text">on page-1 of Google.</span></h2>
        <p style="margin-top: 20px; max-width: 600px; margin-left: auto; margin-right: auto;">Free 30-minute {name} SEO audit — no obligation, no fluff. Walk away with 3-5 actionable things to fix this week.</p>
        <a href="../../../../contact.html" class="cta-mega-btn" data-cursor-hover style="margin-top: 40px; margin-left: auto; margin-right: auto;">
          <span>Start a project</span>
          <span class="arrow-circle">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </span>
        </a>
      </div>
    </div>
  </div>

  <!-- Locations Section -->
  <section id="locations" style="padding: 80px 0; border-top: 1px solid var(--border);">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Locations</span>
          <h2 class="display">Also we serve our services <br/><span class="gradient-text">in these locations.</span></h2>
        </div>
        <p class="lede">Browse the active location pages below to claim your local search presence across all major districts.</p>
      </div>

      <!-- Toggle button -->
      <div class="locations-toggle-wrap reveal" style="margin-top: 40px; text-align: center;">
        <button id="locations-toggle-btn" class="btn btn-ghost" data-cursor-hover style="padding: 16px 32px; border-radius: 100px; font-family: 'Space Grotesk', sans-serif; font-size: 16px; font-weight: 500; display: inline-flex; align-items: center; gap: 12px; transition: all 0.3s var(--ease);">
          <span>Browse locations</span>
          <svg class="toggle-icon" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="transition: transform 0.3s var(--ease);"><path d="M6 9l6 6 6-6"/></svg>
        </button>
      </div>

      <!-- Links Grid in 3 columns with small bullet points (Hidden by default) -->
      <div id="locations-list-wrap" class="locations-grid reveal" style="max-height: 0; overflow: hidden; transition: max-height 0.4s var(--ease); margin-top: 0;">
        <ul style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px 40px; list-style: none; padding: 40px 0 20px 0;">
          {columns_links}
        </ul>
      </div>
    </div>
  </section>

  <style>
    .location-link-item {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 16px;
      line-height: 1.5;
      position: relative;
      padding-left: 20px;
      margin-bottom: 8px;
    }}
    .location-link-item::before {{
      content: '•';
      position: absolute;
      left: 0;
      color: var(--accent);
      font-size: 18px;
      line-height: 1.3;
      transition: transform 0.3s var(--ease);
    }}
    .location-link-item:hover::before {{
      transform: scale(1.3);
    }}
    .location-link-item a {{
      color: var(--ink-1);
      text-decoration: none;
      transition: color 0.3s;
    }}
    .location-link-item a:hover {{
      color: var(--accent);
    }}
    @media (max-width: 900px) {{
      .locations-grid {{
        max-height: none;
      }}
      .locations-grid ul {{
        grid-template-columns: repeat(2, 1fr) !important;
      }}
    }}
    @media (max-width: 600px) {{
      .locations-grid ul {{
        grid-template-columns: 1fr !important;
      }}
    }}
  </style>

  <script>
    document.addEventListener('DOMContentLoaded', function() {{
      const toggleBtn = document.getElementById('locations-toggle-btn');
      const listWrap = document.getElementById('locations-list-wrap');
      if (toggleBtn && listWrap) {{
        toggleBtn.addEventListener('click', function() {{
          const isOpen = listWrap.classList.toggle('open');
          if (isOpen) {{
            listWrap.style.maxHeight = listWrap.scrollHeight + 'px';
            toggleBtn.querySelector('.toggle-icon').style.transform = 'rotate(180deg)';
          }} else {{
            listWrap.style.maxHeight = '0';
            toggleBtn.querySelector('.toggle-icon').style.transform = 'rotate(0deg)';
          }}
        }});
      }}
    }});
  </script>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="../../../../index.html" class="logo" data-cursor-hover>
            <div class="logo-mark"></div>
            NEXUS
          </a>
          <p>Local SEO engineered for Maharashtra businesses. We rank {name} companies on page-1 of Google — measurably, predictably, and at a price that pays for itself.</p>
        </div>
        <div class="footer-col">
          <h5>Services</h5>
          <ul>
            <li><a href="../../../../index.html#services" data-cursor-hover>Local SEO</a></li>
            <li><a href="../../../../index.html#services" data-cursor-hover>Technical SEO</a></li>
            <li><a href="../../../../index.html#services" data-cursor-hover>Content &amp; Authority</a></li>
            <li><a href="../../../../index.html#services" data-cursor-hover>GBP Optimization</a></li>
            <li><a href="../../../../index.html#services" data-cursor-hover>Link Acquisition</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>{name}</h5>
          <ul>
            <li><a href="../index.html" data-cursor-hover>All Maharashtra districts</a></li>
            <li><a href="../../index.html" data-cursor-hover>SEO in India</a></li>
            <li><a href="../../../../index.html#pricing" data-cursor-hover>Pricing</a></li>
            <li><a href="../../../../index.html#process" data-cursor-hover>Process</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Studio</h5>
          <ul>
            <li><a href="../../../../index.html#work" data-cursor-hover>Selected work</a></li>
            <li><a href="../../../../index.html#faq" data-cursor-hover>FAQ</a></li>
            <li><a href="../../../../contact.html" data-cursor-hover>Contact</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 NEXUS Studio. All rights reserved.</p>
        <div class="footer-bottom-links">
          <a href="../../../../contact.html" data-cursor-hover>Contact</a>
          <a href="../../../../index.html" data-cursor-hover>Home</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="../../../../script.js"></script>
</body>
</html>
"""

# HTML template for the main Maharashtra Hub page
HUB_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="theme-color" content="#0a0a0a" />

  <!-- SEO: Primary meta -->
  <title>SEO Services Maharashtra — NEXUS | Premium SEO Agency</title>
  <meta name="description" content="NEXUS is a performance-driven SEO agency in Maharashtra. We engineer local, national, and e-commerce SEO for Maharashtra businesses across all 35 districts including Pune, Mumbai, Thane, and Nagpur. Real rankings. Real leads." />
  <meta name="keywords" content="SEO agency Maharashtra, SEO company Maharashtra, Maharashtra SEO services, local SEO Maharashtra, Pune SEO, Mumbai SEO, technical SEO, content SEO, NEXUS SEO" />
  <meta name="author" content="NEXUS Studio" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <link rel="canonical" href="https://nexus.studio/seo/india/maharashtra/" />

  <!-- SEO: OpenGraph -->
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="NEXUS Studio" />
  <meta property="og:title" content="SEO Services Maharashtra — NEXUS" />
  <meta property="og:description" content="Performance-driven SEO for Maharashtra businesses. Local, national, and e-commerce SEO across all 35 districts." />
  <meta property="og:url" content="https://nexus.studio/seo/india/maharashtra/" />
  <meta property="og:locale" content="en_IN" />
  <meta property="og:image" content="https://nexus.studio/seo/india/maharashtra/images/hero.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="675" />
  <meta property="og:image:alt" content="NEXUS SEO Agency Maharashtra — engineering organic growth" />

  <!-- SEO: Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:site" content="@nexusstudio" />
  <meta name="twitter:title" content="SEO Services Maharashtra — NEXUS" />
  <meta name="twitter:description" content="Performance-driven SEO for Maharashtra businesses. Local, national, and e-commerce SEO across all 35 districts." />
  <meta name="twitter:image" content="https://nexus.studio/seo/india/maharashtra/images/hero.jpg" />

  <!-- SEO: Geo -->
  <meta name="geo.region" content="IN-MH" />
  <meta name="geo.placename" content="Maharashtra" />
  <meta name="geo.position" content="18.5204;73.8567" />
  <meta name="ICBM" content="18.5204, 73.8567" />

  <!-- Performance: preconnect -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />

  <!-- Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />

  <!-- Stylesheet -->
  <link rel="stylesheet" href="../../../style.css" />

  <!-- JSON-LD Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "NEXUS Studio",
    "alternateName": "NEXUS",
    "url": "https://nexus.studio/",
    "logo": "https://nexus.studio/logo.png",
    "description": "Performance-driven SEO, content, and digital growth agency for ambitious brands across India and globally.",
    "address": {{
      "@type": "PostalAddress",
      "addressCountry": "IN",
      "addressRegion": "Maharashtra",
      "addressLocality": "Pune"
    }}
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "serviceType": "Search Engine Optimization (SEO)",
    "name": "NEXUS SEO Services in Maharashtra",
    "provider": {{
      "@type": "Organization",
      "name": "NEXUS Studio",
      "url": "https://nexus.studio/"
    }},
    "areaServed": {{
      "@type": "State",
      "name": "Maharashtra",
      "sameAs": "https://en.wikipedia.org/wiki/Maharashtra"
    }},
    "hasOfferCatalog": {{
      "@type": "OfferCatalog",
      "name": "NEXUS Maharashtra SEO Plans",
      "itemListElement": [
        {{ "@type": "Offer", "name": "Local SEO Maharashtra", "price": "30000", "priceCurrency": "INR" }},
        {{ "@type": "Offer", "name": "Growth SEO Maharashtra", "price": "65000", "priceCurrency": "INR" }},
        {{ "@type": "Offer", "name": "Authority SEO Maharashtra", "price": "150000", "priceCurrency": "INR" }}
      ]
    }}
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://nexus.studio/" }},
      {{ "@type": "ListItem", "position": 2, "name": "SEO in India", "item": "https://nexus.studio/seo/india/" }},
      {{ "@type": "ListItem", "position": 3, "name": "Maharashtra", "item": "https://nexus.studio/seo/india/maharashtra/" }}
    ]
  }}
  </script>

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {{
        "@type": "Question",
        "name": "How much does SEO cost in Maharashtra?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "NEXUS Maharashtra SEO retainers start at ₹30,000/month for Local SEO, ₹65,000/month for Growth, and custom pricing for national and e-commerce engagements. All plans are month-to-month with 30 days notice."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Which districts in Maharashtra do you serve?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "We serve all 35 districts of Maharashtra, including major hubs like Pune, Mumbai, Thane, Nagpur, Nashik, Kolhapur, and Solapur, as well as tier-2 and tier-3 locations."
        }}
      }},
      {{
        "@type": "Question",
        "name": "Do you do bilingual SEO for Maharashtra?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Yes, we design bilingual (Hindi & English) SEO strategies, optimize for regional Hinglish queries, and use appropriate schema and hreflang configuration to capture the local search intent."
        }}
      }},
      {{
        "@type": "Question",
        "name": "How long does SEO take to show results in Maharashtra?",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "Local SEO and Google Business Profile optimizations typically produce visible ranking improvements within 30 to 60 days. National and e-commerce campaigns take 3 to 6 months depending on keyword competitiveness."
        }}
      }}
    ]
  }}
  </script>
</head>
<body>
  <div class="ambient" aria-hidden="true"></div>
  <div class="grid-overlay" aria-hidden="true"></div>
  <div class="cursor" id="cursor" aria-hidden="true"></div>
  <div class="cursor-follower" id="cursor-follower" aria-hidden="true"></div>

  <!-- Navigation -->
  <nav class="nav" id="nav">
    <div class="container nav-inner">
      <a href="../../../index.html" class="logo" data-cursor-hover>
        <div class="logo-mark"></div>
        NEXUS
      </a>
      <ul class="nav-links">
        <li><a href="#capabilities" data-cursor-hover>Capabilities</a></li>
        <li><a href="#locations" data-cursor-hover>Locations</a></li>
        <li><a href="#process" data-cursor-hover>Process</a></li>
        <li><a href="#trust" data-cursor-hover>Trust</a></li>
        <li><a href="#faq" data-cursor-hover>FAQ</a></li>
        <li><a href="../index.html" data-cursor-hover>India</a></li>
        <li><a href="../../../contact.html" data-cursor-hover>Contact</a></li>
      </ul>
      <div class="nav-divider"></div>
      <div class="nav-cta">
        <a href="../../../contact.html" class="btn btn-primary" data-cursor-hover>
          Start a project
          <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </a>
        <button class="menu-toggle" data-cursor-hover aria-label="Menu"><span></span></button>
      </div>
    </div>
  </nav>

  <!-- Hero Section -->
  <header class="hero">
    <div class="container hero-inner">
      <div class="hero-meta">
        <div class="hero-meta-left">
          <span class="eyebrow"><span class="dot"></span> Now booking Q3 2026</span>
          <div class="hero-meta-divider"></div>
          <div class="hero-meta-info">IND · 35 districts · 6 languages — 24/7</div>
        </div>
        <div class="hero-meta-info">/ 2026 / v.07</div>
      </div>

      <h1 class="display">
        <div class="word"><span class="char">S</span><span class="char">E</span><span class="char">O</span></div>
        <div class="word"><span class="char gradient-text">M</span><span class="char gradient-text">a</span><span class="char gradient-text">h</span><span class="char gradient-text">a</span><span class="char gradient-text">r</span><span class="char gradient-text">a</span><span class="char gradient-text">s</span><span class="char gradient-text">h</span><span class="char gradient-text">t</span><span class="char gradient-text">r</span><span class="char gradient-text">a</span><span class="char">.</span></div>
      </h1>

      <p class="hero-sub">A performance-driven SEO studio for ambitious Maharashtra brands. We blend technical SEO, content, and authority engineering to build organic growth that compounds — across all 35 districts of Maharashtra.</p>

      <div class="hero-cta">
        <a href="../../../contact.html" class="btn btn-primary" data-cursor-hover>
          Start a project
          <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </a>
        <a href="#locations" class="btn btn-ghost" data-cursor-hover>
          View all 35 districts
        </a>
      </div>

      <div class="hero-stats reveal-stagger">
        <div class="hero-stat">
          <div class="hero-stat-num"><span class="count" data-target="290">0</span><span class="unit">+</span></div>
          <div class="hero-stat-label">Maharashtra clients ranked</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-num"><span class="count" data-target="35">0</span></div>
          <div class="hero-stat-label">Districts served</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-num"><span class="count" data-target="6">0</span></div>
          <div class="hero-stat-label">Years in market</div>
        </div>
        <div class="hero-stat">
          <div class="hero-stat-num"><span class="count" data-target="5.8" data-decimal="1">0</span><span class="unit">×</span></div>
          <div class="hero-stat-label">Avg. organic ROI</div>
        </div>
      </div>
    </div>
    <div class="hero-badge" aria-hidden="true">
      <span class="ping"></span>
      <span>RANKING ENGINE ONLINE</span>
    </div>
  </header>

  <!-- Infinite Marquee -->
  <div class="marquee" aria-hidden="true">
    <div class="marquee-track">
      <div class="marquee-item"><strong>Local SEO</strong><span class="sep"></span>Google Business Profile</div>
      <div class="marquee-item"><strong>National SEO</strong><span class="sep"></span>Topical Authority</div>
      <div class="marquee-item"><strong>E-commerce SEO</strong><span class="sep"></span>Shopify &amp; WooCommerce</div>
      <div class="marquee-item"><strong>Multilingual</strong><span class="sep"></span>Hindi · Tamil · Telugu · Bengali</div>
      <div class="marquee-item"><strong>Technical</strong><span class="sep"></span>Core Web Vitals</div>
      <div class="marquee-item"><strong>Content</strong><span class="sep"></span>Editorial Systems</div>
      <div class="marquee-item"><strong>Digital PR</strong><span class="sep"></span>Authority Building</div>
      <div class="marquee-item"><strong>Local SEO</strong><span class="sep"></span>Google Business Profile</div>
      <div class="marquee-item"><strong>National SEO</strong><span class="sep"></span>Topical Authority</div>
      <div class="marquee-item"><strong>E-commerce SEO</strong><span class="sep"></span>Shopify &amp; WooCommerce</div>
      <div class="marquee-item"><strong>Multilingual</strong><span class="sep"></span>Hindi · Tamil · Telugu · Bengali</div>
      <div class="marquee-item"><strong>Technical</strong><span class="sep"></span>Core Web Vitals</div>
      <div class="marquee-item"><strong>Content</strong><span class="sep"></span>Editorial Systems</div>
      <div class="marquee-item"><strong>Digital PR</strong><span class="sep"></span>Authority Building</div>
    </div>
  </div>

  <!-- Capabilities -->
  <section id="capabilities">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Capabilities</span>
          <h2 class="display">Full-stack SEO,<br/><span class="gradient-text">engineered for Maharashtra.</span></h2>
        </div>
        <p class="lede">Six disciplines, one team. We work as an embedded SEO partner for Maharashtra businesses — technical, content, and authority in lockstep, with measurable outcomes on every brief.</p>
      </div>

      <div class="services-grid reveal-stagger">
        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 01</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          </div>
          <h3>Local SEO</h3>
          <p>Google Business Profile, citations, NAP consistency, and reviews. Built for MH's city-level search behaviour — from Pune to Nagpur.</p>
          <div class="service-tags">
            <span class="service-tag">GBP</span>
            <span class="service-tag">Citations</span>
            <span class="service-tag">Reviews</span>
            <span class="service-tag">Maps</span>
          </div>
          <a href="#locations" class="arrow-cta" data-cursor-hover>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
        </div>

        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 02</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>
          </div>
          <h3>National SEO</h3>
          <p>Topical authority, content silos, and digital PR for national keywords. We capture demand that compounds for years — not months.</p>
          <div class="service-tags">
            <span class="service-tag">Authority</span>
            <span class="service-tag">Content</span>
            <span class="service-tag">Digital PR</span>
            <span class="service-tag">Links</span>
          </div>
          <a href="#process" class="arrow-cta" data-cursor-hover>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
        </div>

        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 03</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 3h18l-2 13H5L3 3z"/><path d="M3 3L2 1H0"/><circle cx="9" cy="20" r="1.5"/><circle cx="17" cy="20" r="1.5"/></svg>
          </div>
          <h3>E-commerce SEO</h3>
          <p>Shopify, WooCommerce, and custom storefronts. Category pages, product schema, faceted nav — engineered for organic revenue, not just traffic.</p>
          <div class="service-tags">
            <span class="service-tag">Shopify</span>
            <span class="service-tag">Schema</span>
            <span class="service-tag">CRO</span>
            <span class="service-tag">Revenue</span>
          </div>
          <a href="#locations" class="arrow-cta" data-cursor-hover>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
        </div>

        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 04</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/></svg>
          </div>
          <h3>Multilingual SEO</h3>
          <p>Rank in English, Marathi, and regional dialects. Hreflang, language-targeted landing pages, and native-speaker content for bilingual queries.</p>
          <div class="service-tags">
            <span class="service-tag">Marathi</span>
            <span class="service-tag">Hinglish</span>
            <span class="service-tag">hreflang</span>
            <span class="service-tag">Bilingual</span>
          </div>
          <a href="#locations" class="arrow-cta" data-cursor-hover>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
        </div>

        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 05</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="M3.27 6.96L12 12.01l8.73-5.05M12 22.08V12"/></svg>
          </div>
          <h3>Technical SEO</h3>
          <p>Core Web Vitals, JS rendering, mobile-first indexing, and crawl budget. The foundation that lets your content rank in local SERPs.</p>
          <div class="service-tags">
            <span class="service-tag">CWV</span>
            <span class="service-tag">Mobile</span>
            <span class="service-tag">Schema</span>
            <span class="service-tag">Crawl</span>
          </div>
          <a href="#process" class="arrow-cta" data-cursor-hover>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
        </div>

        <div class="service-card" data-cursor-hover>
          <span class="service-num">/ 06</span>
          <div class="service-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 20h9"/><path d="M16.5 3.5a2.121 2.121 0 1 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
          </div>
          <h3>Content &amp; Authority</h3>
          <p>Editorial systems, topical maps, and linkable assets. We turn your expertise into category authority — in English and Hindi.</p>
          <div class="service-tags">
            <span class="service-tag">Editorial</span>
            <span class="service-tag">Topical</span>
            <span class="service-tag">Linkable</span>
            <span class="service-tag">PR</span>
          </div>
          <a href="#process" class="arrow-cta" data-cursor-hover>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Why NEXUS for Maharashtra -->
  <section>
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Why NEXUS</span>
          <h2 class="display">An SEO partner that<br/><span class="gradient-text">measures what matters.</span></h2>
        </div>
        <p class="lede">We don't do vanity metrics. Every engagement is wired to rankings, leads, and revenue — with a creative standard built for Maharashtra's unique economic sectors.</p>
      </div>

      <div class="stats-wrap">
        <div class="stats-grid reveal-stagger">
          <div class="stat-card">
            <div class="stat-num"><span class="grad">290</span><span class="stat-suffix">+</span></div>
            <div class="stat-label">Businesses ranked on page-1 in the last 36 months.</div>
          </div>
          <div class="stat-card">
            <div class="stat-num"><span class="grad">5.8</span><span class="stat-suffix">×</span></div>
            <div class="stat-label">Average organic ROI multiplier for our clients.</div>
          </div>
          <div class="stat-card">
            <div class="stat-num"><span class="grad">35</span></div>
            <div class="stat-label">Districts with active local SEO engagements today.</div>
          </div>
          <div class="stat-card">
            <div class="stat-num"><span class="grad">92</span><span class="stat-suffix">%</span></div>
            <div class="stat-label">Client retention rate across 8 years and 200+ engagements.</div>
          </div>
        </div>

        <div class="why-pillars reveal-stagger">
          <div class="pillar">
            <div class="pillar-num">/ 01</div>
            <div>
              <h4>In-house UP &amp; MH team</h4>
              <p>No outsourcing. Our SEO specialists, content writers, and developers operate locally in Pune and Mumbai. Every line of strategy is produced in-house.</p>
            </div>
          </div>
          <div class="pillar">
            <div class="pillar-num">/ 02</div>
            <div>
              <h4>Multilingual &amp; Hinglish</h4>
              <p>Local buyers search using voice and bilingual queries. We build parallel content structure, schema, and Google Business Profiles for regional searches.</p>
            </div>
          </div>
          <div class="pillar">
            <div class="pillar-num">/ 03</div>
            <div>
              <h4>Micro-Market targeting</h4>
              <p>We know the differences between tech-driven Pune, financial Mumbai, industrial Nashik, and the agricultural and maritime districts. We structure campaigns around these differences.</p>
            </div>
          </div>
          <div class="pillar">
            <div class="pillar-num">/ 04</div>
            <div>
              <h4>Industry playbooks</h4>
              <p>We have specialized playbooks for Maharashtra's core sectors: IT/Tech, logistics &amp; ports, B2B manufacturing, and agro-industries.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Process -->
  <section id="process" style="padding: 80px 0; border-top: 1px solid var(--border);">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Process</span>
          <h2 class="display">A 90-day path<br/><span class="gradient-text">from audit to authority.</span></h2>
        </div>
        <p class="lede">No mystery. We share the operating system that has produced 200+ engagements — and the artifacts you keep at the end.</p>
      </div>

      <div class="process-list reveal-stagger" style="margin-top: 60px;">
        <div class="process-step" data-cursor-hover>
          <div class="process-num">01</div>
          <div class="process-title">
            <h3>Audit &amp; map</h3>
            <p>Days 1–14 · Analysis</p>
          </div>
          <div class="process-desc">Technical, on-page, GBP, competitor, and citation audits. We deliver a district-specific keyword map in 7 days.</div>
          <div class="process-cta">Diagnostic <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </div>
        <div class="process-step" data-cursor-hover>
          <div class="process-num">02</div>
          <div class="process-title">
            <h3>Build foundation</h3>
            <p>Days 15–35 · Quick wins</p>
          </div>
          <div class="process-desc">GBP category correction, review velocity configuration, top directory submissions, schema injection, and internal linking setups.</div>
          <div class="process-cta">Foundation <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </div>
        <div class="process-step" data-cursor-hover>
          <div class="process-num">03</div>
          <div class="process-title">
            <h3>Author content</h3>
            <p>Days 36–60 · Growth</p>
          </div>
          <div class="process-desc">Local and city landing pages, monthly editorial posts, niche backlinks, and authority asset development in English and Marathi.</div>
          <div class="process-cta">Authority <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </div>
        <div class="process-step" data-cursor-hover>
          <div class="process-num">04</div>
          <div class="process-title">
            <h3>Scale &amp; defend</h3>
            <p>Days 61–90+ · Defend</p>
          </div>
          <div class="process-desc">Weekly conversion audit, search pattern tracking, continuous link acquisition, and content refreshes to defend page-1 positions.</div>
          <div class="process-cta">Scale <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></div>
        </div>
      </div>
    </div>
  </section>

  <!-- Trust Section -->
  <section id="trust" style="padding: 80px 0; border-top: 1px solid var(--border);">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Trust &amp; E-E-A-T</span>
          <h2 class="display">Ranked because we're<br/><span class="gradient-text">trusted by Google.</span></h2>
        </div>
        <p class="lede">E-E-A-T — Experience, Expertise, Authoritativeness, Trustworthiness — is the framework Google's Quality Raters use to judge every page that ranks. We build it into every engagement, not as a checklist, but as the operating system behind our work.</p>
      </div>

      <div class="eeat-grid reveal-stagger">
        <div class="eeat-block" data-cursor-hover>
          <div class="eeat-letter">E</div>
          <h3>Experience</h3>
          <p>First-hand proof. We've shipped SEO in MH's hardest categories — IT services, SaaS, logistics, exports — and we publish the results, the dashboards, and the mistakes. Real case studies, not sanitized retrospectives.</p>
          <ul class="eeat-list">
            <li>8 years operating in India · 290+ clients</li>
            <li>Live ranking dashboards for every client</li>
            <li>Public case studies with real numbers</li>
            <li>Author bylines on every piece of content</li>
          </ul>
        </div>

        <div class="eeat-block" data-cursor-hover>
          <div class="eeat-letter">E</div>
          <h3>Expertise</h3>
          <p>Senior specialists, not junior generalists. Our strategists have 6–12 years of Indian SEO experience, native-speaker content writers in 6 languages, and developers who can ship schema, hreflang, and Core Web Vitals fixes in-house.</p>
          <ul class="eeat-list">
            <li>Senior strategists on every brief</li>
            <li>Native-speaker content in 6 Indian languages</li>
            <li>In-house technical SEO &amp; dev team</li>
            <li>Industry-specific playbooks (12 verticals)</li>
          </ul>
        </div>

        <div class="eeat-block" data-cursor-hover>
          <div class="eeat-letter">A</div>
          <h3>Authoritativeness</h3>
          <p>Reputation that compounds. Our work is cited in B2B reviews, news media, and industrial publications. Our team publishes on organic search systems — and we back it up with public results.</p>
          <ul class="eeat-list">
            <li>Coverage in local &amp; national media</li>
            <li>Author profiles on industry channels</li>
            <li>Speaking at SEO summits &amp; industry panels</li>
            <li>Industry authority across all channels</li>
          </ul>
        </div>

        <div class="eeat-block" data-cursor-hover>
          <div class="eeat-letter">T</div>
          <h3>Trustworthiness</h3>
          <p>Transparent, honest, and accountable. No lock-in contracts. No "secret sauce" you can't audit. Month-to-month engagements, full data ownership, and published processes you can read before you sign.</p>
          <ul class="eeat-list">
            <li>Month-to-month, 30-day notice</li>
            <li>Full data &amp; account ownership stays with you</li>
            <li>Public methodology &amp; reporting</li>
            <li>ISO 27001-ready data handling</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQ Section -->
  <section id="faq" style="padding: 80px 0; border-top: 1px solid var(--border);">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> FAQ</span>
          <h2 class="display">Common <span class="gradient-text">questions.</span></h2>
        </div>
        <p class="lede">Answers to standard questions about our SEO services and campaigns in Maharashtra.</p>
      </div>

      <div class="faq-list reveal-stagger" style="margin-top: 60px; max-width: 800px; margin-left: auto; margin-right: auto;">
        <div class="faq-item">
          <button class="faq-q" data-cursor-hover>
            How much does SEO cost in Maharashtra?
            <span class="icon"></span>
          </button>
          <div class="faq-a">
            <div class="faq-a-inner">NEXUS Maharashtra SEO retainers start at ₹30,000/month for Local SEO, ₹65,000/month for Growth, and custom pricing for national engagements. All plans are month-to-month with 30 days notice.</div>
          </div>
        </div>
        <div class="faq-item">
          <button class="faq-q" data-cursor-hover>
            Which districts in Maharashtra do you serve?
            <span class="icon"></span>
          </button>
          <div class="faq-a">
            <div class="faq-a-inner">We serve all 35 districts of Maharashtra, including major hubs like Pune, Mumbai, Thane, Nagpur, Nashik, Kolhapur, and Solapur, as well as tier-2 and tier-3 locations.</div>
          </div>
        </div>
        <div class="faq-item">
          <button class="faq-q" data-cursor-hover>
            Do you do bilingual SEO for Maharashtra?
            <span class="icon"></span>
          </button>
          <div class="faq-a">
            <div class="faq-a-inner">Yes, we design bilingual (Hindi &amp; English) SEO strategies, optimize for regional Hinglish queries, and use appropriate schema and hreflang configuration to capture the local search intent.</div>
          </div>
        </div>
        <div class="faq-item">
          <button class="faq-q" data-cursor-hover>
            How long does SEO take to show results in Maharashtra?
            <span class="icon"></span>
          </button>
          <div class="faq-a">
            <div class="faq-a-inner">Local SEO and Google Business Profile optimizations typically produce visible ranking improvements within 30 to 60 days. National and e-commerce campaigns take 3 to 6 months depending on keyword competitiveness.</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA Section -->
  <div class="cta-wrap" id="cta">
    <div class="container">
      <div class="reveal" style="text-align: center;">
        <span class="eyebrow"><span class="dot"></span> Ready to rank in Maharashtra?</span>
        <h2 class="display" style="margin-top: 30px;">Let's get your Maharashtra business<br /><span class="gradient-text">on page-1 of Google.</span></h2>
        <p style="margin-top: 20px; max-width: 600px; margin-left: auto; margin-right: auto;">Free 30-minute Maharashtra SEO audit — no obligation, no fluff. Walk away with 3-5 actionable things to fix this week.</p>
        <a href="../../../contact.html" class="cta-mega-btn" data-cursor-hover style="margin-top: 40px; margin-left: auto; margin-right: auto;">
          <span>Start a project</span>
          <span class="arrow-circle">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
          </span>
        </a>
      </div>
    </div>
  </div>

  <!-- Locations Section -->
  <section id="locations" style="padding: 80px 0; border-top: 1px solid var(--border);">
    <div class="container">
      <div class="section-head reveal">
        <div>
          <span class="eyebrow"><span class="dot"></span> Locations</span>
          <h2 class="display">Also we serve our services <br/><span class="gradient-text">in these locations.</span></h2>
        </div>
        <p class="lede">Browse the active location pages below to claim your local search presence across all major districts.</p>
      </div>

      <!-- Toggle button -->
      <div class="locations-toggle-wrap reveal" style="margin-top: 40px; text-align: center;">
        <button id="locations-toggle-btn" class="btn btn-ghost" data-cursor-hover style="padding: 16px 32px; border-radius: 100px; font-family: 'Space Grotesk', sans-serif; font-size: 16px; font-weight: 500; display: inline-flex; align-items: center; gap: 12px; transition: all 0.3s var(--ease);">
          <span>Browse locations</span>
          <svg class="toggle-icon" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" style="transition: transform 0.3s var(--ease);"><path d="M6 9l6 6 6-6"/></svg>
        </button>
      </div>

      <!-- Links Grid in 3 columns with small bullet points (Hidden by default) -->
      <div id="locations-list-wrap" class="locations-grid reveal" style="max-height: 0; overflow: hidden; transition: max-height 0.4s var(--ease); margin-top: 0;">
        <ul style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px 40px; list-style: none; padding: 40px 0 20px 0;">
          {columns_links}
        </ul>
      </div>
    </div>
  </section>

  <style>
    .location-link-item {{
      font-family: 'Space Grotesk', sans-serif;
      font-size: 16px;
      line-height: 1.5;
      position: relative;
      padding-left: 20px;
      margin-bottom: 8px;
    }}
    .location-link-item::before {{
      content: '•';
      position: absolute;
      left: 0;
      color: var(--accent);
      font-size: 18px;
      line-height: 1.3;
      transition: transform 0.3s var(--ease);
    }}
    .location-link-item:hover::before {{
      transform: scale(1.3);
    }}
    .location-link-item a {{
      color: var(--ink-1);
      text-decoration: none;
      transition: color 0.3s;
    }}
    .location-link-item a:hover {{
      color: var(--accent);
    }}
    @media (max-width: 900px) {{
      .locations-grid {{
        max-height: none;
      }}
      .locations-grid ul {{
        grid-template-columns: repeat(2, 1fr) !important;
      }}
    }}
    @media (max-width: 600px) {{
      .locations-grid ul {{
        grid-template-columns: 1fr !important;
      }}
    }}
  </style>

  <script>
    document.addEventListener('DOMContentLoaded', function() {{
      const toggleBtn = document.getElementById('locations-toggle-btn');
      const listWrap = document.getElementById('locations-list-wrap');
      if (toggleBtn && listWrap) {{
        toggleBtn.addEventListener('click', function() {{
          const isOpen = listWrap.classList.toggle('open');
          if (isOpen) {{
            listWrap.style.maxHeight = listWrap.scrollHeight + 'px';
            toggleBtn.querySelector('.toggle-icon').style.transform = 'rotate(180deg)';
          }} else {{
            listWrap.style.maxHeight = '0';
            toggleBtn.querySelector('.toggle-icon').style.transform = 'rotate(0deg)';
          }}
        }});
      }}
    }});
  </script>

  <!-- Footer -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="../../../index.html" class="logo" data-cursor-hover>
            <div class="logo-mark"></div>
            NEXUS
          </a>
          <p>Local SEO engineered for Maharashtra businesses. We rank companies across Pune, Mumbai, Thane, Nagpur, and 31 more districts on page-1 of Google.</p>
        </div>
        <div class="footer-col">
          <h5>Services</h5>
          <ul>
            <li><a href="../../../index.html#services" data-cursor-hover>Local SEO</a></li>
            <li><a href="../../../index.html#services" data-cursor-hover>Technical SEO</a></li>
            <li><a href="../../../index.html#services" data-cursor-hover>Content &amp; Authority</a></li>
            <li><a href="../../../index.html#services" data-cursor-hover>GBP Optimization</a></li>
            <li><a href="../../../index.html#services" data-cursor-hover>Link Acquisition</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Maharashtra</h5>
          <ul>
            <li><a href="#" data-cursor-hover>MH Hub</a></li>
            <li><a href="../index.html" data-cursor-hover>SEO in India</a></li>
            <li><a href="../../../index.html#pricing" data-cursor-hover>Pricing</a></li>
            <li><a href="../../../index.html#process" data-cursor-hover>Process</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h5>Studio</h5>
          <ul>
            <li><a href="../../../index.html#work" data-cursor-hover>Selected work</a></li>
            <li><a href="../../../index.html#faq" data-cursor-hover>FAQ</a></li>
            <li><a href="../../../contact.html" data-cursor-hover>Contact</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 NEXUS Studio. All rights reserved.</p>
        <div class="footer-bottom-links">
          <a href="../../../contact.html" data-cursor-hover>Contact</a>
          <a href="../../../index.html" data-cursor-hover>Home</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="../../../script.js"></script>
</body>
</html>"""

def get_char_spans(name, is_outline=True):
    spans = []
    cls = "char outline-text" if is_outline else "char"
    for char in name:
        if char == " ":
            spans.append(" ")
        else:
            spans.append(f'<span class="{cls}">{char}</span>')
    return "".join(spans)

def generate_page(district_tuple):
    slug, name, lat, lng, category = district_tuple
    cat_copy = CATEGORIES_COPIES[category]
    
    # Title & descriptions
    title = f"SEO Agency in {name} — NEXUS Local SEO"
    tagline_lower = cat_copy["tagline"].lower()
    description = f"NEXUS is a local SEO agency in {name}. We engineer GBP, citation, on-page and content SEO for {name} businesses — {tagline_lower}. Real rankings. Real leads."
    og_description = f"Local SEO in {name} — engineered to rank your business on Google. {cat_copy['tagline']}."
    twitter_description = f"Local SEO engineered for {name} businesses. GBP, citations, on-page, and Hindi-English bilingual content."
    hero_sub = f"Maharashtra local SEO — engineered to rank your business in {name} on Google for high-intent local searches. {cat_copy['tagline']}."
    eyebrow_left = f"{name} · Maharashtra · SEO"
    eyebrow_right = f"/ seo / maharashtra / {slug}"
    
    # Generate why features html
    why_html_parts = []
    for i, (why_title, why_desc) in enumerate(cat_copy["why_features"]):
        letter = chr(65 + i)
        why_html_parts.append(f'''        <div class="pillar" data-cursor-hover>
          <div class="pillar-num">/ {letter}</div>
          <div>
            <h4>{why_title}</h4>
            <p>{why_desc}</p>
          </div>
        </div>''')
    why_features_html = "\n".join(why_html_parts)
    
    # Generate siblings (next 4)
    idx = 0
    for i, dist in enumerate(DISTRICTS):
        if dist[0] == slug:
            idx = i
            break
            
    sibling_parts = []
    for i, offset in enumerate([1, 2, 3, 4], 1):
        sib_idx = (idx + offset) % len(DISTRICTS)
        sib_slug, sib_name, _, _, sib_cat = DISTRICTS[sib_idx]
        sib_tagline = CATEGORIES_COPIES[sib_cat]["tagline"]
        sibling_parts.append(f'''        <a href="../{sib_slug}/index.html" class="price-card" data-tilt data-cursor-hover style="padding: 36px 28px; min-height: 200px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <span class="price-name">/ 0{i}</span>
            <h3 style="margin-top: 12px; margin-bottom: 8px;">{sib_name}</h3>
            <p class="price-desc" style="margin-bottom: 0;">{sib_tagline}</p>
          </div>
          <span class="btn-ghost" style="display: inline-flex; align-items: center; gap: 8px; font-size: 12px; padding: 8px 16px; border-radius: 100px; width: fit-content; margin-top: 16px;">Explore →</span>
        </a>''')
    siblings_html = "\n".join(sibling_parts)
    
    # Generate FAQs and FAQ JSON-LD
    faqs = []
    # Add category-specific FAQs first
    for q, a in cat_copy["faqs"]:
        faqs.append((q, a))
        
    # Localized general FAQs
    general_faqs = [
        (
            f"How long does SEO take to show results in {name}?", 
            f"Most {name} clients see measurable movement in local pack rankings within 30-60 days, and meaningful lead flow within 90-120 days."
        ),
        (
            f"Can you rank my {name} business for specific local queries?", 
            f"Yes, we optimize your Google Business Profile and local landing pages for high-intent keywords in {name} to drive direct leads."
        ),
        (
            f"Do you work with businesses outside {name}?",
            f"Yes — we serve all of Maharashtra, Delhi NCR, and pan-North India. The {name}-specific page is a deep-dive for clients in this market; if you're elsewhere, our main NEXUS page covers national service."
        ),
        (
            f"Do you handle Google Business Profile for {name} shops?",
            f"Yes. GBP setup, verification, category optimization, photo uploads, weekly Google Posts, and review-response workflows are all part of our Local and Growth plans for {name} clients."
        ),
        (
            f"What does SEO cost in {name}?",
            f"Our {name} retainers start at ₹30,000/month (Local), ₹65,000/month (Growth), and custom for Authority engagements. All plans are month-to-month with 30 days notice."
        ),
        (
            f"Do you do Hindi & English SEO for {name}?",
            f"Yes. {name} search behaviour is bilingual — we map queries in both languages, build parallel content where it makes sense, and use hreflang-style signals so Google serves the right variant."
        ),
        (
            f"Can I see {name} SEO case studies?",
            f"Yes. We've ranked {name} businesses in several local sectors. Request a relevant case study via our contact form."
        )
    ]
    for q, a in general_faqs:
        if not any(q.lower() == existing_q.lower() for existing_q, _ in faqs):
            faqs.append((q, a))
            
    faq_parts = []
    for q, a in faqs:
        faq_parts.append(f'''        <div class="faq-item">
          <button class="faq-q" data-cursor-hover>
            {q}
            <span class="icon"></span>
          </button>
          <div class="faq-a">
            <div class="faq-a-inner">{a}</div>
          </div>
        </div>''')
    faq_html = "\n".join(faq_parts)
    
    faq_entities = []
    for q, a in faqs:
        faq_entities.append(f'''      {{
        "@type": "Question",
        "name": "{q.replace('"', '\\"')}",
        "acceptedAnswer": {{
          "@type": "Answer",
          "text": "{a.replace('"', '\\"')}"
        }}
      }}''')
    faq_json_ld_content = ",\n".join(faq_entities)
    faq_json_ld = f'''<script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
{faq_json_ld_content}
    ]
  }}
  </script>'''
  
    char_spans = get_char_spans(name, is_outline=True)
    wiki_name = name.replace(" ", "_")
    
    # Generate locations links for the collapsible drawer (point to ../[slug]/index.html)
    dist_links_list = []
    for dist in DISTRICTS:
        d_slug, d_name, _, _, _ = dist
        dist_links_list.append(f'<li class="location-link-item" data-cursor-hover><a href="../{d_slug}/index.html">SEO Agency in {d_name}</a></li>')
    columns_links_html = "\n          ".join(dist_links_list)
    
    testimonial_city_specific = cat_copy["testimonials"]["quote"]
    testimonial_avatar = cat_copy["testimonials"]["avatar"]
    testimonial_author = cat_copy["testimonials"]["author"]
    testimonial_role = cat_copy["testimonials"]["role"]
    
    # Format template
    html_content = HTML_TEMPLATE.format(
        title=title,
        description=description,
        og_description=og_description,
        twitter_description=twitter_description,
        name=name,
        slug=slug,
        lat=lat,
        lng=lng,
        tagline=cat_copy["tagline"],
        hero_sub=hero_sub,
        eyebrow_left=eyebrow_left,
        eyebrow_right=eyebrow_right,
        char_spans=char_spans,
        hero_stat_1_target=cat_copy["hero_stat_target"],
        why_features_html=why_features_html,
        pricing_desc_local=cat_copy["pricing_desc_local"],
        pricing_desc_growth=cat_copy["pricing_desc_growth"],
        pricing_desc_authority=cat_copy["pricing_desc_authority"],
        siblings_html=siblings_html,
        faq_html=faq_html,
        faq_json_ld=faq_json_ld,
        testimonial_city_specific=testimonial_city_specific.replace('"', '\\"'),
        testimonial_avatar=testimonial_avatar,
        testimonial_author=testimonial_author,
        testimonial_role=testimonial_role.replace('"', '\\"'),
        wiki_name=wiki_name,
        columns_links=columns_links_html
    )
    
    # Create folder and write index.html
    dest_dir = os.path.join("..", slug)
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = os.path.join(dest_dir, "index.html")
    
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html_content)

def generate_hub_page():
    # Generate locations links for the collapsible drawer (point to [slug]/index.html)
    links_list = []
    for dist in DISTRICTS:
        d_slug, d_name, _, _, _ = dist
        links_list.append(f'<li class="location-link-item" data-cursor-hover><a href="{d_slug}/index.html">SEO Agency in {d_name}</a></li>')
    columns_links_html = "\n          ".join(links_list)
    
    html_content = HUB_HTML_TEMPLATE.format(
        columns_links=columns_links_html
    )
    
    dest_path = os.path.join("..", "index.html")
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated Maharashtra Hub page -> {dest_path}")

def main():
    print(f"Starting generator for {len(DISTRICTS)} Maharashtra districts...")
    for idx, dist in enumerate(DISTRICTS, 1):
        slug, name, _, _, _ = dist
        generate_page(dist)
        if idx % 10 == 0 or idx == len(DISTRICTS):
            print(f"Progress: {idx}/{len(DISTRICTS)} pages generated.")
    generate_hub_page()
    print("All Maharashtra pages generated successfully!")

if __name__ == "__main__":
    main()
