<?php
$base_path = '../../../';
$page_title = "YouTube Marketing agency in Haryana - Rankfyno";
$page_description = "rankfyno is a YouTube marketing agency for Haryana businesses. Channel growth, video SEO, thumbnails, Shorts, and YouTube Ads across all 22 districts including Gurugram, Faridabad, Panipat, and Karnal.";
$current_page = '';
// header-include.php emits rel=canonical, robots and og:url from $canonical_url —
// setting it here instead of in $custom_head keeps exactly one canonical on the page.
$canonical_url = "https://rankfyno.com/youtube-marketing/india/haryana/";
$og_image = "https://rankfyno.com/youtube-marketing/india/haryana/images/hero.jpg";
$custom_head = "<meta name=\"theme-color\" content=\"#0a0a0a\" />
  <meta name=\"keywords\" content=\"YouTube marketing Haryana, YouTube marketing agency Haryana, video marketing Haryana, YouTube channel growth Haryana, YouTube ads Haryana, rankfyno\" />
  <meta name=\"author\" content=\"rankfyno\" />
  <meta property=\"og:type\" content=\"website\" />
  <meta property=\"og:site_name\" content=\"rankfyno\" />
  <meta property=\"og:title\" content=\"YouTube Marketing agency in Haryana - rankfyno\" />
  <meta property=\"og:description\" content=\"YouTube marketing for Haryana businesses - channel growth, video SEO, Shorts, and YouTube Ads across all 22 districts.\" />
  <meta property=\"og:url\" content=\"https://rankfyno.com/youtube-marketing/india/haryana/\" />
  <meta property=\"og:locale\" content=\"en_IN\" />
  <meta property=\"og:image\" content=\"https://rankfyno.com/youtube-marketing/india/haryana/images/hero.jpg\" />
  <meta property=\"og:image:width\" content=\"1200\" />
  <meta property=\"og:image:height\" content=\"675\" />
  <meta property=\"og:image:alt\" content=\"rankfyno YouTube Marketing Haryana\" />
  <meta name=\"twitter:card\" content=\"summary_large_image\" />
  <meta name=\"twitter:title\" content=\"YouTube Marketing agency in Haryana - rankfyno\" />
  <meta name=\"twitter:description\" content=\"YouTube marketing for Haryana businesses across all 22 districts.\" />
  <meta name=\"twitter:image\" content=\"https://rankfyno.com/youtube-marketing/india/haryana/images/hero.jpg\" />
  <meta name=\"geo.region\" content=\"IN-HR\" />
  <meta name=\"geo.placename\" content=\"Haryana\" />
  <script type=\"application/ld+json\">
  {
    \"@context\": \"https://schema.org\", \"@type\": \"Service\", \"serviceType\": \"YouTube Marketing\", \"name\": \"rankfyno YouTube Marketing in Haryana\",
    \"provider\": { \"@type\": \"Organization\", \"name\": \"rankfyno\", \"url\": \"https://rankfyno.com/\" },
    \"areaServed\": { \"@type\": \"State\", \"name\": \"Haryana\" },
    \"description\": \"YouTube channel setup, video SEO, thumbnails, Shorts strategy, YouTube Ads and monetization for businesses across Haryana.\"
  }
  </script>
  <script type=\"application/ld+json\">
  {
    \"@context\": \"https://schema.org\", \"@type\": \"BreadcrumbList\", \"itemListElement\": [
      { \"@type\": \"ListItem\", \"position\": 1, \"name\": \"Home\", \"item\": \"https://rankfyno.com/\" },
      { \"@type\": \"ListItem\", \"position\": 2, \"name\": \"YouTube Marketing\", \"item\": \"https://rankfyno.com/youtube-marketing/india/\" },
      { \"@type\": \"ListItem\", \"position\": 3, \"name\": \"Haryana\", \"item\": \"https://rankfyno.com/youtube-marketing/india/haryana/\" }
    ]
  }
  </script>";
$footer_brand_desc = "YouTube marketing engineered for Haryana businesses - channel growth, video SEO, and paid video that turns watch-time into leads across all 22 districts.";
$custom_footer_cols = "<div class=\"footer-col\"><h5>YouTube services</h5><ul><li><a href=\"../../../contact.php\" data-cursor-hover>Channel setup and branding</a></li><li><a href=\"../../../contact.php\" data-cursor-hover>Video SEO</a></li><li><a href=\"../../../contact.php\" data-cursor-hover>Thumbnails and packaging</a></li><li><a href=\"../../../contact.php\" data-cursor-hover>Shorts strategy</a></li><li><a href=\"../../../contact.php\" data-cursor-hover>YouTube Ads</a></li></ul></div>
        <div class=\"footer-col\"><h5>Coverage</h5><ul><li><a href=\"#districts\" data-cursor-hover>All 22 Haryana districts</a></li><li><a href=\"../../../seo/india/haryana/\" data-cursor-hover>SEO in Haryana</a></li><li><a href=\"../../../index.php#process\" data-cursor-hover>Process</a></li></ul></div>
        <div class=\"footer-col\"><h5>Studio</h5><ul><li><a href=\"../../../index.php#work\" data-cursor-hover>Selected work</a></li><li><a href=\"../../../team.php\" data-cursor-hover>Team</a></li><li><a href=\"../../../contact.php\" data-cursor-hover>Contact</a></li></ul></div>";
include $base_path . 'header.php';
?>
<style>
/* =============================================================
   YouTube Marketing pages - scoped styles (.ytm namespace)
   Reuses site design tokens (--accent, --ink-0, --bg-*, Space Grotesk)
   Adds a video / play-button motif harmonised with the warm palette.
   ============================================================= */
.ytm { --yt-red: #ff2d2d; --yt-red-deep: #c81e1e; }
.ytm .eyebrow .dot { background: var(--yt-red); }

/* ---- Hero ---- */
.ytm-hero { padding: 150px 0 70px; position: relative; overflow: hidden; }
.ytm-hero-grid { display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 56px; align-items: center; }
.ytm-hero h1 { font-family: 'Space Grotesk', sans-serif; font-weight: 600; line-height: 0.98; letter-spacing: -0.03em; font-size: clamp(40px, 6vw, 76px); margin: 22px 0 0; }
.ytm-hero h1 .play-word { color: var(--yt-red); }
.ytm-hero .hero-sub { color: var(--ink-1); font-size: clamp(16px, 1.5vw, 19px); line-height: 1.55; margin-top: 22px; max-width: 34em; }
.ytm-hero-cta { display: flex; gap: 14px; flex-wrap: wrap; margin-top: 32px; }

/* stat strip */
.ytm-stats { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-top: 46px; border-top: 1px solid var(--line); padding-top: 26px; }
.ytm-stat .n { font-family: 'Space Grotesk', sans-serif; font-weight: 600; font-size: clamp(24px, 3vw, 34px); letter-spacing: -0.02em; }
.ytm-stat .l { color: var(--ink-2); font-size: 12.5px; margin-top: 4px; letter-spacing: 0.01em; }

/* ---- Hero player mockup (pure CSS) ---- */
.ytm-player { border-radius: 18px; overflow: hidden; border: 1px solid var(--line-strong); background: var(--bg-1); box-shadow: 0 30px 70px -30px rgba(15,15,20,0.35); }
.ytm-player-screen { position: relative; aspect-ratio: 16 / 9; background:
    radial-gradient(120% 120% at 30% 20%, #2a2a33 0%, #14141a 55%, #0c0c11 100%); }
.ytm-player-screen::after { content: ""; position: absolute; inset: 0;
    background: repeating-linear-gradient(115deg, rgba(255,255,255,0.03) 0 2px, transparent 2px 26px); }
.ytm-play { position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%);
    width: 74px; height: 74px; border-radius: 50%; background: var(--yt-red); display: grid; place-items: center;
    box-shadow: 0 12px 34px -6px rgba(255,45,45,0.65); z-index: 2; transition: transform .35s var(--ease); }
.ytm-player:hover .ytm-play { transform: translate(-50%,-50%) scale(1.08); }
.ytm-play svg { width: 26px; height: 26px; fill: #fff; margin-left: 4px; }
.ytm-badge { position: absolute; right: 12px; bottom: 12px; background: rgba(0,0,0,0.82); color: #fff;
    font-size: 12px; font-weight: 600; padding: 3px 8px; border-radius: 6px; z-index: 2; letter-spacing: 0.02em; }
.ytm-scrub { position: absolute; left: 0; right: 0; bottom: 0; height: 4px; background: rgba(255,255,255,0.22); z-index: 2; }
.ytm-scrub i { display: block; height: 100%; width: 38%; background: var(--yt-red); }
.ytm-player-meta { display: flex; gap: 12px; padding: 16px 18px; align-items: flex-start; }
.ytm-avatar { width: 40px; height: 40px; border-radius: 50%; flex: none; background: var(--grad-1); display: grid; place-items: center; color: #fff; font-weight: 600; font-size: 14px; }
.ytm-player-meta h4 { font-size: 15px; font-weight: 600; line-height: 1.3; margin: 0; }
.ytm-player-meta p { color: var(--ink-2); font-size: 13px; margin: 4px 0 0; }

/* ---- generic section rhythm ---- */
.ytm-section { padding: 84px 0; border-top: 1px solid var(--line); }

/* ---- service cards ---- */
.ytm-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px; margin-top: 56px; }
.ytm-card { background: var(--bg-1); border: 1px solid var(--line); border-radius: 16px; padding: 30px 26px; transition: transform .4s var(--ease), border-color .4s var(--ease), box-shadow .4s var(--ease); }
.ytm-card:hover { transform: translateY(-4px); border-color: var(--line-strong); box-shadow: 0 24px 50px -30px rgba(15,15,20,0.3); }
.ytm-icon { width: 46px; height: 46px; border-radius: 12px; display: grid; place-items: center; background: rgba(255,45,45,0.09); color: var(--yt-red); margin-bottom: 18px; }
.ytm-icon svg { width: 23px; height: 23px; }
.ytm-card h3 { font-size: 18px; font-weight: 600; margin: 0 0 8px; }
.ytm-card p { color: var(--ink-1); font-size: 14.5px; line-height: 1.6; margin: 0; }
.ytm-num { color: var(--ink-2); font-size: 12px; font-weight: 600; letter-spacing: 0.08em; }

/* ---- why pillars ---- */
.ytm-pillars { display: grid; grid-template-columns: repeat(2, 1fr); gap: 22px; margin-top: 56px; }
.ytm-pillar { display: flex; gap: 18px; padding: 26px; border: 1px solid var(--line); border-radius: 16px; background: var(--bg-1); }
.ytm-pillar .pk { font-family: 'Space Grotesk', sans-serif; color: var(--yt-red); font-weight: 600; font-size: 15px; flex: none; }
.ytm-pillar h4 { font-size: 16.5px; font-weight: 600; margin: 0 0 7px; }
.ytm-pillar p { color: var(--ink-1); font-size: 14.5px; line-height: 1.6; margin: 0; }

/* ---- process ---- */
.ytm-steps { margin-top: 56px; border-top: 1px solid var(--line); }
.ytm-step { display: grid; grid-template-columns: 90px 1.1fr 1.4fr; gap: 24px; padding: 26px 0; border-bottom: 1px solid var(--line); align-items: start; }
.ytm-step .sn { font-family: 'Space Grotesk', sans-serif; font-size: 30px; font-weight: 600; color: var(--ink-0); opacity: 0.25; }
.ytm-step h3 { font-size: 17px; font-weight: 600; margin: 0 0 4px; }
.ytm-step .sp { color: var(--ink-2); font-size: 13px; }
.ytm-step .sd { color: var(--ink-1); font-size: 14.5px; line-height: 1.6; }

/* ---- formats showcase (video-card grid) ---- */
.ytm-formats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px; margin-top: 56px; }
.ytm-vcard { border: 1px solid var(--line); border-radius: 14px; overflow: hidden; background: var(--bg-1); transition: transform .4s var(--ease), box-shadow .4s var(--ease); }
.ytm-vcard:hover { transform: translateY(-4px); box-shadow: 0 24px 50px -30px rgba(15,15,20,0.3); }
.ytm-thumb { position: relative; aspect-ratio: 16 / 9; display: grid; place-items: center; }
.ytm-thumb .ytm-play { position: static; transform: none; width: 54px; height: 54px; box-shadow: 0 8px 22px -6px rgba(255,45,45,0.6); }
.ytm-vcard:hover .ytm-thumb .ytm-play { transform: scale(1.08); }
.ytm-thumb .ytm-play svg { width: 19px; height: 19px; }
.ytm-vbody { padding: 16px 18px 20px; }
.ytm-vbody h4 { font-size: 15.5px; font-weight: 600; margin: 0 0 6px; }
.ytm-vbody p { color: var(--ink-1); font-size: 13.5px; line-height: 1.55; margin: 0; }
.ytm-t1 { background: linear-gradient(135deg, #ff5b2e 0%, #ff2d2d 100%); }
.ytm-t2 { background: linear-gradient(135deg, #1a4d3a 0%, #0f0f14 100%); }
.ytm-t3 { background: linear-gradient(135deg, #2a2a33 0%, #0c0c11 100%); }
.ytm-t4 { background: linear-gradient(135deg, #d4b896 0%, #a97f52 100%); }
.ytm-t5 { background: linear-gradient(135deg, #ff8a5b 0%, #ff2d2d 100%); }
.ytm-t6 { background: linear-gradient(135deg, #14324a 0%, #0c0c11 100%); }

/* ---- district / sibling cards ---- */
.ytm-loc-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; margin-top: 48px; }
.ytm-loc { display: block; padding: 22px 20px; border: 1px solid var(--line); border-radius: 14px; background: var(--bg-1); text-decoration: none; color: var(--ink-0); transition: transform .35s var(--ease), border-color .35s var(--ease); }
.ytm-loc:hover { transform: translateY(-3px); border-color: var(--yt-red); }
.ytm-loc strong { display: block; font-size: 15.5px; font-weight: 600; }
.ytm-loc span { display: block; color: var(--ink-2); font-size: 12.5px; margin-top: 6px; line-height: 1.5; }
.ytm-loc .go { color: var(--yt-red); font-size: 13px; font-weight: 600; margin-top: 12px; display: inline-block; }

/* ---- FAQ (reuses site faq classes; minor accent) ---- */
.ytm .faq-q:hover { color: var(--yt-red); }

/* ---- CTA ---- */
.ytm-cta { padding: 96px 0; border-top: 1px solid var(--line); text-align: center; }
.ytm-cta .display { margin-top: 22px; }

@media (max-width: 900px) {
  .ytm-hero-grid { grid-template-columns: 1fr; gap: 40px; }
  .ytm-grid, .ytm-formats { grid-template-columns: 1fr; }
  .ytm-pillars { grid-template-columns: 1fr; }
  .ytm-loc-grid { grid-template-columns: repeat(2, 1fr); }
  .ytm-step { grid-template-columns: 60px 1fr; }
  .ytm-step .sd { grid-column: 1 / -1; }
  .ytm-stats { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 560px) { .ytm-loc-grid { grid-template-columns: 1fr; } }

</style>
<main class="ytm">

  <header class="ytm-hero">
    <div class="container ytm-hero-grid">
      <div class="reveal">
        <span class="eyebrow"><span class="dot"></span> Haryana · YouTube Marketing</span>
        <h1>YouTube Marketing <span class="play-word">agency</span><br/>in Haryana</h1>
        <p class="hero-sub">From Gurugram's SaaS boardrooms to Panipat's textile mills and Karnal's rice exporters, we build YouTube channels that turn Haryana's local demand into watch-time, subscribers, and leads.</p>
        <div class="ytm-hero-cta">
          <a href="../../../contact.php" class="btn btn-primary" data-cursor-hover>Grow my channel <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></a>
          <a href="#districts" class="btn btn-ghost" data-cursor-hover>Browse districts</a>
        </div>
        <div class="ytm-stats reveal-stagger">
          <div class="ytm-stat"><div class="n">22</div><div class="l">Districts covered</div></div>
          <div class="ytm-stat"><div class="n">6</div><div class="l">YouTube disciplines</div></div>
          <div class="ytm-stat"><div class="n">7</div><div class="l">Content formats</div></div>
          <div class="ytm-stat"><div class="n">2</div><div class="l">Languages: Hindi, English</div></div>
        </div>
      </div>
      <div class="reveal">
        <div class="ytm-player">
          <div class="ytm-player-screen">
            <div class="ytm-play"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></div>
            <span class="ytm-badge">14:22</span>
            <div class="ytm-scrub"><i></i></div>
          </div>
          <div class="ytm-player-meta">
            <div class="ytm-avatar">HR</div>
            <div>
              <h4>YouTube growth for Haryana businesses</h4>
              <p>rankfyno - YouTube Marketing - Haryana</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>

  <section class="ytm-section" id="services">
    <div class="container">
      <div class="section-head reveal">
        <div><span class="eyebrow"><span class="dot"></span> What we run on your channel</span>
        <h2 class="display">YouTube growth, <span class="gradient-text">engineered.</span></h2></div>
        <p class="lede">Six disciplines, one team - from channel architecture to paid video - built for Haryana's businesses.</p>
      </div>
      <div class="ytm-grid reveal-stagger">
        <div class="ytm-card"><span class="ytm-num">/ 01</span><div class="ytm-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="2" y="7" width="20" height="14" rx="3"/><path d="M8 3v4M16 3v4M2 11h20"/></svg></div><h3>Channel setup and branding</h3><p>Channel architecture, banner and logo, section layout, keyword-led about page, and playlists structured so first-time visitors subscribe.</p></div>
        <div class="ytm-card"><span class="ytm-num">/ 02</span><div class="ytm-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg></div><h3>Video SEO and discovery</h3><p>Title, description, tags, chapters, and transcript optimisation so your videos surface in YouTube and Google search for high-intent local queries.</p></div>
        <div class="ytm-card"><span class="ytm-num">/ 03</span><div class="ytm-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="4" width="18" height="14" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 15l-5-4-9 7"/></svg></div><h3>Thumbnails and packaging</h3><p>Click-worthy thumbnails, title-thumbnail A/B testing, and a packaging system that lifts click-through-rate without clickbait.</p></div>
        <div class="ytm-card"><span class="ytm-num">/ 04</span><div class="ytm-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/></svg></div><h3>Shorts engine</h3><p>A repeatable Shorts pipeline that mines your long-form for vertical clips, drives new subscribers, and feeds the algorithm daily.</p></div>
        <div class="ytm-card"><span class="ytm-num">/ 05</span><div class="ytm-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 2l2.4 7.4H22l-6 4.6 2.3 7.4L12 17l-6.3 4.4L8 14 2 9.4h7.6z"/></svg></div><h3>YouTube Ads</h3><p>In-stream, in-feed, and Shorts ad campaigns with audience targeting, so you reach Haryana buyers with measurable cost-per-lead.</p></div>
        <div class="ytm-card"><span class="ytm-num">/ 06</span><div class="ytm-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg></div><h3>Analytics and monetization</h3><p>Retention analysis, monthly reporting, and a path to monetization - memberships, brand deals, and lead capture off the channel.</p></div>
      </div>
    </div>
  </section>

  <section class="ytm-section" id="districts">
    <div class="container">
      <div class="section-head reveal">
        <div><span class="eyebrow"><span class="dot"></span> Coverage</span>
        <h2 class="display">YouTube marketing in <span class="gradient-text">every Haryana district.</span></h2></div>
        <p class="lede">Pick your district for a page built around its real local economy and the videos its businesses need.</p>
      </div>
      <div class="ytm-loc-grid reveal-stagger">
        <a href="ambala/" class="ytm-loc" data-cursor-hover><strong>Ambala</strong><span>Multi-specialty hospitals, Scientific instrument makers, Cross-border logistics and Cantonment retail</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="bhiwani/" class="ytm-loc" data-cursor-hover><strong>Bhiwani</strong><span>Wrestling and boxing academies, Cotton and mustard trade, Agri-input dealers and Local service shops</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="charkhi-dadri/" class="ytm-loc" data-cursor-hover><strong>Charkhi Dadri</strong><span>Stone crushing units, Quarrying operators, Farm produce trade and Local service shops</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="faridabad/" class="ytm-loc" data-cursor-hover><strong>Faridabad</strong><span>Auto component makers, Industrial manufacturers, Real estate developers and BPO and service exporters</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="fatehabad/" class="ytm-loc" data-cursor-hover><strong>Fatehabad</strong><span>Agri-input retailers, Cotton and wheat trade, Cooperative societies and Local farm services</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="gurugram/" class="ytm-loc" data-cursor-hover><strong>Gurugram</strong><span>B2B SaaS companies, Fintech firms, Real estate developers and Premium B2C services</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="hisar/" class="ytm-loc" data-cursor-hover><strong>Hisar</strong><span>Coaching institutes, Test-prep academies, Agricultural mandi trade and High-street retail</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="jhajjar/" class="ytm-loc" data-cursor-hover><strong>Jhajjar</strong><span>Hospitals and diagnostics, Auto component suppliers, Footwear and ceramics units and Agri and allied trade</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="jind/" class="ytm-loc" data-cursor-hover><strong>Jind</strong><span>Cotton and wheat trade, Cooperative societies, Agri input dealers and Local service providers</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="kaithal/" class="ytm-loc" data-cursor-hover><strong>Kaithal</strong><span>Wheat and rice trade, Mustard and oil, Cooperative credit societies and Local retail and services</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="karnal/" class="ytm-loc" data-cursor-hover><strong>Karnal</strong><span>Basmati rice export, Agricultural research, K-12 schools and Coaching institutes</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="kurukshetra/" class="ytm-loc" data-cursor-hover><strong>Kurukshetra</strong><span>Pilgrimage tourism, Hotels and dharamshalas, University and coaching and Agriculture</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="mahendragarh/" class="ytm-loc" data-cursor-hover><strong>Mahendragarh</strong><span>Mining and minerals, Agriculture, Aravalli tourism and Local trade and services</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="nuh/" class="ytm-loc" data-cursor-hover><strong>Nuh</strong><span>Mewat handicrafts, Hospitality and hotels, Development-zone services and Local trade and services</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="palwal/" class="ytm-loc" data-cursor-hover><strong>Palwal</strong><span>Agriculture and trade, Highway logistics, Warehousing and transport and NCR retail spillover</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="panchkula/" class="ytm-loc" data-cursor-hover><strong>Panchkula</strong><span>Premium real estate, Hospitality and dining, Retail and lifestyle and Professional services</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="panipat/" class="ytm-loc" data-cursor-hover><strong>Panipat</strong><span>Home textile mills, Handloom weavers, Blanket and carpet units and Textile export houses</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="rewari/" class="ytm-loc" data-cursor-hover><strong>Rewari</strong><span>Brass product makers, Auto-ancillary units, Logistics and warehousing and Agriculture and agri-trade</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="rohtak/" class="ytm-loc" data-cursor-hover><strong>Rohtak</strong><span>Coaching institutes, Universities and colleges, Hospitals and clinics and Retail and showrooms</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="sirsa/" class="ytm-loc" data-cursor-hover><strong>Sirsa</strong><span>Cotton and agri-trade, Kinnow citrus growers, Local retail and services and Border cross-state trade</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="sonipat/" class="ytm-loc" data-cursor-hover><strong>Sonipat</strong><span>Universities and institutes, Real estate builders, Food processing units and Agri-tech businesses</span><span class="go">YouTube marketing -&gt;</span></a>
        <a href="yamunanagar/" class="ytm-loc" data-cursor-hover><strong>Yamunanagar</strong><span>Plywood manufacturers, Timber and veneer traders, Metal and sugar units and Agriculture and farming</span><span class="go">YouTube marketing -&gt;</span></a>
      </div>
    </div>
  </section>

  <!-- Related services -->
  <section class="ytm-section">
    <div class="container">
      <div class="section-head reveal">
        <div><span class="eyebrow"><span class="dot"></span> Related services</span>
        <h2 class="display">Pair YouTube with <span class="gradient-text">search.</span></h2></div>
        <p class="lede">Video builds demand; search captures it. Most Haryana clients run both together.</p>
      </div>
      <div class="ytm-loc-grid reveal-stagger">
        <a href="<?php echo $base_path; ?>seo/india/haryana/" class="ytm-loc" data-cursor-hover><strong>Local SEO agency in Haryana</strong><span>District-level local SEO across all 22 Haryana districts - Google Maps, local search, and location pages.</span><span class="go">Local SEO in Haryana -&gt;</span></a>
        <a href="<?php echo $base_path; ?>seo/india/" class="ytm-loc" data-cursor-hover><strong>Local SEO services in India</strong><span>City and district-level local SEO coverage across 28 Indian states.</span><span class="go">Local SEO in India -&gt;</span></a>
        <a href="<?php echo $base_path; ?>seo-agency-in-india/" class="ytm-loc" data-cursor-hover><strong>National SEO agency in India</strong><span>Nationwide organic growth for ambitious Indian brands - technical SEO, content, and authority.</span><span class="go">National SEO in India -&gt;</span></a>
        <a href="<?php echo $base_path; ?>seo-services/saas-seo/" class="ytm-loc" data-cursor-hover><strong>SaaS SEO for B2B software</strong><span>Product-led organic growth for software companies - trials, demos, and pipeline that compound.</span><span class="go">SaaS SEO services -&gt;</span></a>
      </div>
    </div>
  </section>

  <div class="ytm-cta">
    <div class="container reveal">
      <span class="eyebrow"><span class="dot"></span> Ready to grow on YouTube in Haryana?</span>
      <h2 class="display">Let's turn Haryana viewers<br/><span class="gradient-text">into customers.</span></h2>
      <p style="margin-top: 18px; max-width: 600px; margin-left: auto; margin-right: auto;">Free 30-minute YouTube strategy session - channel review plus 3 content ideas you can ship this month.</p>
      <a href="../../../contact.php" class="cta-mega-btn" data-cursor-hover style="margin-top: 34px; margin-left: auto; margin-right: auto;"><span>Book a strategy call</span><span class="arrow-circle"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></span></a>
    </div>
  </div>

</main>
<?php include $base_path . 'footer.php'; ?>
