<?php
$base_path = '../';
$current_page = 'blog';
$page_title = 'SEO Blog — rankfyno';
$page_description = "Practical SEO guides and answers from the rankfyno team. Learn why your site isn't ranking, how to recover lost rankings, find low-competition keywords, and grow organic traffic.";

$custom_head = '
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <link rel="canonical" href="https://rankfyno.com/blog/" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="rankfyno" />
  <meta property="og:title" content="SEO Blog — rankfyno" />
  <meta property="og:description" content="Practical SEO guides from the rankfyno team. Rank higher, recover traffic, and grow." />
  <meta property="og:url" content="https://rankfyno.com/blog/" />
  <meta property="og:locale" content="en_IN" />
  <meta property="og:image" content="https://rankfyno.com/og-default.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="SEO Blog — rankfyno" />
  <meta name="twitter:description" content="Practical SEO guides from the rankfyno team." />
  <meta name="twitter:image" content="https://rankfyno.com/og-default.jpg" />
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Blog",
    "name": "rankfyno SEO Blog",
    "url": "https://rankfyno.com/blog/",
    "description": "Practical SEO guides and answers from the rankfyno team.",
    "publisher": {
      "@type": "Organization",
      "name": "rankfyno",
      "url": "https://rankfyno.com/",
      "logo": { "@type": "ImageObject", "url": "https://rankfyno.com/Rankfyno.png" }
    }
  }
  </script>
  <style>
    .blog-hero { padding: 180px 0 60px; }
    .blog-hero h1 { font-size: clamp(40px, 6vw, 72px); line-height: 1.05; margin: 20px 0 24px; }
    .blog-hero p { color: var(--ink-1); max-width: 640px; font-size: 18px; }
    .blog-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 32px; padding: 60px 0 120px; }
    @media (max-width: 800px) { .blog-grid { grid-template-columns: 1fr; } }
    .blog-card {
      display: block; padding: 32px; border: 1px solid var(--line);
      border-radius: 16px; background: var(--bg-0);
      transition: transform .3s, border-color .3s, background .3s;
      text-decoration: none; color: inherit;
    }
    .blog-card:hover { transform: translateY(-4px); border-color: var(--accent, #ff5b1f); }
    .blog-card h3 { font-size: 24px; line-height: 1.25; margin: 0 0 12px; }
    .blog-card p { color: var(--ink-1); margin: 0; font-size: 15px; }
    .blog-card .tag {
      display: inline-block; font-size: 12px; letter-spacing: .08em;
      text-transform: uppercase; color: var(--ink-1); margin-bottom: 16px;
    }
  </style>
';

include __DIR__ . '/../header.php';
?>

  <section class="blog-hero">
    <div class="container">
      <span class="eyebrow"><span class="dot"></span> SEO Blog</span>
      <h1 class="display">Practical SEO, <span class="gradient-text">answered.</span></h1>
      <p>Guides and answers from the rankfyno team. No fluff, no outdated tactics — just what works in 2026.</p>
    </div>
  </section>

  <section class="container">
    <div class="blog-grid">
      <a href="<?php echo $base_path; ?>blog/why-is-my-website-not-ranking" class="blog-card" data-cursor-hover>
        <span class="tag">Diagnosis</span>
        <h3>Why is my website not ranking?</h3>
        <p>The 8 most common reasons sites stall on page 2 — and the diagnostic steps to find which one is holding you back.</p>
      </a>
      <a href="<?php echo $base_path; ?>blog/how-can-i-rank-higher-on-google" class="blog-card" data-cursor-hover>
        <span class="tag">Strategy</span>
        <h3>How can I rank higher on Google?</h3>
        <p>A 5-pillar framework for moving from page 2 to the top 3 — covering content, links, technical SEO, intent, and trust.</p>
      </a>
      <a href="<?php echo $base_path; ?>blog/why-did-my-rankings-drop" class="blog-card" data-cursor-hover>
        <span class="tag">Recovery</span>
        <h3>Why did my rankings drop?</h3>
        <p>How to triage a ranking drop: algorithm vs. technical vs. competitor. Includes a 7-step recovery checklist.</p>
      </a>
      <a href="<?php echo $base_path; ?>blog/how-can-i-increase-organic-traffic" class="blog-card" data-cursor-hover>
        <span class="tag">Growth</span>
        <h3>How can I increase organic traffic?</h3>
        <p>Three durable plays to grow organic sessions: topical depth, search-intent matching, and digital-PR links.</p>
      </a>
      <a href="<?php echo $base_path; ?>blog/what-keywords-should-i-target" class="blog-card" data-cursor-hover>
        <span class="tag">Research</span>
        <h3>What keywords should I target?</h3>
        <p>How to pick the right keyword mix: head, body, and long-tail. With a simple scoring sheet you can use today.</p>
      </a>
      <a href="<?php echo $base_path; ?>blog/how-do-i-find-low-competition-keywords" class="blog-card" data-cursor-hover>
        <span class="tag">Research</span>
        <h3>How do I find low-competition keywords?</h3>
        <p>Where the winnable keywords hide, the metrics that actually predict difficulty, and a free workflow to find them.</p>
      </a>
      <a href="<?php echo $base_path; ?>blog/how-many-pages-should-my-website-have" class="blog-card" data-cursor-hover>
        <span class="tag">Architecture</span>
        <h3>How many pages should my website have?</h3>
        <p>There's no magic number — but there is a right ratio of money pages, supporting content, and trust assets for your niche.</p>
      </a>
      <a href="<?php echo $base_path; ?>blog/how-do-i-optimize-my-homepage" class="blog-card" data-cursor-hover>
        <span class="tag">On-page</span>
        <h3>How do I optimize my homepage?</h3>
        <p>Homepage SEO is different from blog SEO. The signals Google weighs, the elements to nail, and the ones to skip.</p>
      </a>
      <a href="<?php echo $base_path; ?>blog/what-is-keyword-density" class="blog-card" data-cursor-hover>
        <span class="tag">Fundamentals</span>
        <h3>What is keyword density?</h3>
        <p>The 2026 answer is more nuanced than "2%." How to think about keyword usage without stuffing or over-optimizing.</p>
      </a>
      <a href="<?php echo $base_path; ?>blog/how-important-are-title-tags" class="blog-card" data-cursor-hover>
        <span class="tag">On-page</span>
        <h3>How important are title tags?</h3>
        <p>Still the single highest-leverage on-page element. What makes a title tag earn clicks in a crowded SERP.</p>
      </a>
    </div>
  </section>

  <section class="container" style="padding: 0 0 120px;">
    <div style="padding: 48px; border: 1px solid var(--line); border-radius: 16px; text-align: center; background: var(--bg-0);">
      <h2 style="margin: 0 0 12px;">Want someone to do this for you?</h2>
      <p style="color: var(--ink-1); margin: 0 0 24px;">rankfyno ranks ambitious brands on page 1 of Google. Tell us your goal — we'll tell you how to get there.</p>
      <a href="<?php echo $base_path; ?>contact.php" class="btn btn-primary" data-cursor-hover>
        Start a project
        <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
      </a>
    </div>
  </section>

<?php include __DIR__ . '/../footer.php'; ?>
