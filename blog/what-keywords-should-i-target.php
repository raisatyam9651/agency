<?php
$base_path = '../';
$current_page = 'blog';
$page_title = 'What keywords should I target? A practical scoring framework — rankfyno';
$page_description = "How to pick the right keyword mix: head, body, and long-tail. With a simple scoring sheet you can use today to prioritize your content roadmap.";
$custom_head = '
  <link rel="canonical" href="https://rankfyno.com/blog/what-keywords-should-i-target" />
  <meta name="robots" content="index, follow" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="What keywords should I target? A practical scoring framework" />
  <meta property="og:description" content="Head, body, and long-tail keyword targeting with a simple scoring sheet." />
  <meta property="og:url" content="https://rankfyno.com/blog/what-keywords-should-i-target" />
  <meta property="og:image" content="https://rankfyno.com/og-default.jpg" />
  <meta name="twitter:card" content="summary_large_image" />
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"Article","headline":"What keywords should I target?","datePublished":"2026-06-22","dateModified":"2026-06-22","author":{"@type":"Person","name":"rankfyno editorial team","jobTitle":"SEO Editorial","worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},"publisher":{"@type":"Organization","name":"rankfyno","logo":{"@type":"ImageObject","url":"https://rankfyno.com/Rankfyno.png"}},"mainEntityOfPage":"https://rankfyno.com/blog/what-keywords-should-i-target"}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
    {"@type":"Question","name":"How many keywords should a page target?","acceptedAnswer":{"@type":"Answer","text":"One primary keyword per page, supported by 3-5 closely related secondary terms. Targeting more than that dilutes the page\'s topical focus and almost always hurts rankings."}},
    {"@type":"Question","name":"What is keyword difficulty and what is a good score?","acceptedAnswer":{"@type":"Answer","text":"Keyword difficulty is a tool-relative score (0-100) estimating how hard a term is to rank for. A score under 30 is generally winnable for newer sites. Scores above 60 require significant authority."}},
    {"@type":"Question","name":"Should I target zero-volume keywords?","acceptedAnswer":{"@type":"Answer","text":"Yes, if they signal strong commercial intent. A keyword with 10 monthly searches from people ready to buy can outperform a 10,000-volume informational term."}},
    {"@type":"Question","name":"How do I know if a keyword has business value?","acceptedAnswer":{"@type":"Answer","text":"Look at the SERP — what are the top results selling? If they\'re tools, services, or product pages, the keyword has commercial value. If they\'re blog posts and Wikipedia, the intent is informational."}}
  ]}
  </script>
  <style>
    .post-hero { padding: 180px 0 40px; border-bottom: 1px solid var(--line); }
    .post-hero h1 { font-size: clamp(36px, 5vw, 60px); line-height: 1.05; margin: 20px 0 20px; max-width: 820px; }
    .post-meta { color: var(--ink-1); font-size: 14px; letter-spacing: .04em; }
    .post-body { max-width: 760px; margin: 0 auto; padding: 80px 0 60px; font-size: 18px; line-height: 1.75; }
    .post-body h2 { font-size: 30px; line-height: 1.2; margin: 60px 0 16px; }
    .post-body p, .post-body li { color: var(--ink-0); }
    .post-body a { color: #2563eb; text-decoration: underline; text-underline-offset: 2px; transition: color 0.2s; }
    .post-body a:hover { color: #1d4ed8; }
    .post-body ol, .post-body ul { padding-left: 22px; }
    .post-body li { margin-bottom: 8px; }
    .post-faq { max-width: 760px; margin: 0 auto; padding: 40px 0 120px; }
    .post-faq h2 { font-size: 32px; margin-bottom: 24px; }
    .faq-item { border-top: 1px solid var(--line); padding: 20px 0; }
    .faq-item:last-child { border-bottom: 1px solid var(--line); }
    .faq-item h3 { font-size: 19px; margin: 0 0 8px; }
    .faq-item p { color: var(--ink-1); margin: 0; font-size: 16px; line-height: 1.65; }
    .post-cta { max-width: 760px; margin: 0 auto 120px; padding: 40px; border: 1px solid var(--line); border-radius: 16px; text-align: center; background: var(--bg-0); }
    .post-cta p { color: var(--ink-1); margin: 0 0 20px; }
  </style>
';
include __DIR__ . '/../header.php';
?>

  <header class="post-hero">
    <div class="container">
      <span class="eyebrow"><span class="dot"></span> Keyword Research</span>
      <h1 class="display">
        <div class="word"><span class="char">L</span><span class="char">o</span><span class="char">c</span><span class="char">a</span><span class="char">l</span></div>
        <div class="word"><span class="char">S</span><span class="char">E</span><span class="char">O</span></div>
        <div class="word"><span class="char gradient-text">a</span><span class="char gradient-text">g</span><span class="char gradient-text">e</span><span class="char gradient-text">n</span><span class="char gradient-text">c</span><span class="char gradient-text">y</span></div>
        <div class="word"><span class="char">i</span><span class="char">n</span></div>
        <div class="word"><span class="char outline-text">B</span><span class="char outline-text">l</span><span class="char outline-text">o</span><span class="char outline-text">g</span></div>
      </h1>
      <p class="post-meta">Updated 22 June 2026 · 7 min read · Written by the rankfyno team</p>
    </div>
  </header>

  <article class="container post-body">
    <p>The wrong keywords waste months of effort. The right ones can pay back for years. Here's the framework we use to build a keyword list that actually drives revenue.</p>

    <h2>Step 1: Categorize every keyword by intent</h2>
    <p>Before volume or difficulty, decide what the searcher wants. Three buckets cover most cases:</p>
    <ul>
      <li><strong>Informational</strong> — "what is X" or "how to do Y." Top of funnel. Rarely converts directly.</li>
      <li><strong>Commercial</strong> — "best X" or "X vs Y." Middle of funnel. High conversion potential.</li>
      <li><strong>Transactional</strong> — "buy X" or "X service near me." Bottom of funnel. The highest intent.</li>
    </ul>

    <h2>Step 2: Use a simple 4-axis scoring sheet</h2>
    <p>For each candidate keyword, score 1-5 on:</p>
    <ol>
      <li><strong>Search volume</strong> — not too low, not insanely high (sub-1,000 is fine for niche sites).</li>
      <li><strong>Business relevance</strong> — does ranking for it lead to revenue?</li>
      <li><strong>Competition</strong> — can you realistically win this term in 6-12 months?</li>
      <li><strong>Conversion potential</strong> — does the SERP show buyers, or just researchers?</li>
    </ol>
    <p>Multiply the four scores. Anything above 300 is worth pursuing. Anything below 100 is a stretch or distraction.</p>

    <h2>Step 3: Build a mix, not a single target</h2>
    <p>Don't try to rank for one term. Build a portfolio:</p>
    <ul>
      <li>2-3 head terms (high volume, high difficulty, takes 12+ months)</li>
      <li>8-12 body terms (medium volume, medium difficulty, 4-8 months)</li>
      <li>20+ long-tail terms (low volume, low difficulty, 1-3 months)</li>
    </ul>
    <p>The long-tail terms drive early traffic while the head terms mature. For finding those long-tail terms, see <a href="<?php echo $base_path; ?>blog/how-do-i-find-low-competition-keywords">our low-competition guide</a>.</p>

    <h2>Step 4: Re-score quarterly</h2>
    <p>Search behavior changes. A keyword that converted well in Q1 may not in Q4. Re-run the scoring sheet every 90 days and prune terms that have stopped paying back.</p>
  </article>

  <section class="container post-faq">
    <h2>Frequently asked questions</h2>
    <div class="faq-item"><h3>How many keywords should a page target?</h3><p>One primary keyword per page, supported by 3-5 closely related secondary terms. More than that dilutes topical focus.</p></div>
    <div class="faq-item"><h3>What is a good keyword difficulty score?</h3><p>A score under 30 is generally winnable for newer sites. Scores above 60 require significant authority.</p></div>
    <div class="faq-item"><h3>Should I target zero-volume keywords?</h3><p>Yes, if they signal strong commercial intent. A keyword with 10 monthly searches from buyers can outperform a 10,000-volume informational term.</p></div>
    <div class="faq-item"><h3>How do I know if a keyword has business value?</h3><p>Look at the SERP — if the top results are tools, services, or product pages, the keyword has commercial value.</p></div>
  </section>

  <section class="container">
    <div class="post-cta">
      <p>Need a keyword list built for your business? We do the research and ship the brief.</p>
      <a href="<?php echo $base_path; ?>contact.php" class="btn btn-primary" data-cursor-hover>Get a keyword list <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg></a>
    </div>
  </section>

<?php include __DIR__ . '/../footer.php'; ?>
