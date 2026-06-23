<?php
$base_path = '../';
$current_page = 'blog';
$page_title = 'SEO Blog — rankfyno';
$page_description = "Practical SEO guides and answers from the rankfyno team. Learn why your site isn't ranking, how to recover lost rankings, find low-competition keywords, and grow organic traffic.";

// --- Build the post registry ---
// Each entry: slug, tag, title, blurb.
// Discovery: any *.php in this directory that's not index.php is a post.
// Newest-first ordering: by file mtime, ties broken alphabetically by slug.
$posts = [];
foreach (glob(__DIR__ . '/*.php') as $path) {
  if (basename($path) === 'index.php') continue;
  $slug = basename($path, '.php');
  $posts[] = [
    'slug' => $slug,
    'mtime' => filemtime($path),
  ];
}
usort($posts, function ($a, $b) {
  if ($a['mtime'] === $b['mtime']) return strcmp($a['slug'], $b['slug']);
  return $b['mtime'] <=> $a['mtime'];
});

// --- Pagination ---
$per_page = 9;
$total = count($posts);
$total_pages = max(1, (int) ceil($total / $per_page));
$page_num = isset($_GET['page']) ? (int) $_GET['page'] : 1;
if ($page_num < 1) $page_num = 1;
if ($page_num > $total_pages) $page_num = $total_pages;
$offset = ($page_num - 1) * $per_page;
$page_posts = array_slice($posts, $offset, $per_page);

// ItemList schema for current page's posts
$itemlist_items = [];
foreach ($page_posts as $i => $p) {
    $slug = $p['slug'];
    $title = isset($meta[$slug]) ? $meta[$slug][1] : ucwords(str_replace('-', ' ', $slug));
    $itemlist_items[] = [
        "@type" => "ListItem",
        "position" => $i + 1,
        "url" => "https://rankfyno.com/blog/" . $slug,
        "name" => $title,
    ];
}
$itemlist_schema = [
    "@context" => "https://schema.org",
    "@type" => "ItemList",
    "itemListElement" => $itemlist_items,
];
$itemlist_json = json_encode($itemlist_schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
$itemlist_script = '<script type="application/ld+json">' . $itemlist_json . '</script>';

// --- Card metadata (tag + title + blurb) for the slug list ---
$meta = [
  'why-is-my-website-not-ranking'                              => ['Diagnosis', 'Why is my website not ranking?', 'The 8 most common reasons sites stall on page 2 — and the diagnostic steps to find which one is holding you back.'],
  'how-can-i-rank-higher-on-google'                            => ['Strategy', 'How can I rank higher on Google?', 'A 5-pillar framework for moving from page 2 to the top 3 — covering content, links, technical SEO, intent, and trust.'],
  'why-did-my-rankings-drop'                                   => ['Recovery', 'Why did my rankings drop?', 'How to triage a ranking drop: algorithm vs. technical vs. competitor. Includes a 7-step recovery checklist.'],
  'how-can-i-increase-organic-traffic'                         => ['Growth', 'How can I increase organic traffic?', 'Three durable plays to grow organic sessions: topical depth, search-intent matching, and digital-PR links.'],
  'what-keywords-should-i-target'                              => ['Research', 'What keywords should I target?', 'How to pick the right keyword mix: head, body, and long-tail. With a simple scoring sheet you can use today.'],
  'how-do-i-find-low-competition-keywords'                     => ['Research', 'How do I find low-competition keywords?', 'Where the winnable keywords hide, the metrics that actually predict difficulty, and a free workflow to find them.'],
  'how-many-pages-should-my-website-have'                      => ['Architecture', 'How many pages should my website have?', "There's no magic number — but there is a right ratio of money pages, supporting content, and trust assets for your niche."],
  'how-do-i-optimize-my-homepage'                              => ['On-page', 'How do I optimize my homepage?', 'Homepage SEO is different from blog SEO. The signals Google weighs, the elements to nail, and the ones to skip.'],
  'what-is-keyword-density'                                    => ['Fundamentals', 'What is keyword density?', 'The 2026 answer is more nuanced than "2%." How to think about keyword usage without stuffing or over-optimizing.'],
  'how-important-are-title-tags'                               => ['On-page', 'How important are title tags?', 'Still the single highest-leverage on-page element. What makes a title tag earn clicks in a crowded SERP.'],
  'how-rankfyno-can-help-your-business-grow-10x-online'        => ['Growth', 'How RankFyno can help your business grow 10X online', 'The system RankFyno builds to make organic visibility, qualified pipeline, and brand authority compound at once.'],
  'why-businesses-choose-rankfyno-for-digital-growth'          => ['Why RankFyno', 'Why businesses choose RankFyno for digital growth', 'Five reasons ambitious brands hire RankFyno over larger, older, or cheaper agencies.'],
  'how-rankfyno-generates-more-leads-and-sales-for-businesses' => ['Lead Gen', 'How RankFyno generates more leads and sales for businesses', 'The three-layer lead-generation system that turns organic traffic into qualified pipeline.'],
  'small-business-growth-strategies-powered-by-rankfyno'      => ['Small Business', 'Small business growth strategies powered by RankFyno', 'Practical SEO and content strategies that grow small businesses without enterprise budgets.'],
  'how-rankfyno-helps-local-businesses-dominate-google-search' => ['Local SEO', 'How RankFyno helps local businesses dominate Google Search', 'The local SEO playbook for putting small businesses on top of the map pack.'],
  'from-zero-to-hero-growing-your-brand-with-rankfyno'         => ['Brand', 'From zero to hero: growing your brand with RankFyno', 'The four-act arc of building a brand from invisible to category leader.'],
  'how-rankfyno-creates-high-converting-marketing-campaigns'   => ['Campaigns', 'How RankFyno creates high-converting marketing campaigns', "The campaign framework behind RankFyno's repeatable conversions."],
  'why-seo-by-rankfyno-delivers-long-term-business-growth'     => ['SEO', 'Why SEO by RankFyno delivers long-term business growth', 'Why SEO-led growth compounds where paid-only growth stalls — and how RankFyno engineers it.'],
  'how-rankfyno-builds-websites-that-generate-leads'           => ['Web Design', 'How RankFyno builds websites that generate leads', 'Web design built for SEO, conversion, and pipeline from day one.'],
  'rankfyno-vs-traditional-marketing-which-delivers-better-roi' => ['ROI', 'RankFyno vs traditional marketing: which delivers better ROI?', 'Why digital-first marketing consistently outperforms traditional advertising on measurable ROI.'],
  'how-rankfyno-helps-healthcare-businesses-grow-online'       => ['Healthcare', 'How RankFyno helps healthcare businesses grow online', 'HIPAA-aware SEO and content marketing for healthcare brands that need to grow compliantly.'],
  'why-startups-need-rankfyno-for-digital-marketing-success'   => ['Startups', 'Why startups need RankFyno for digital marketing success', 'How RankFyno helps seed-to-Series-B startups acquire users efficiently and build the brand that raises the next round.'],
  'how-rankfyno-uses-ai-to-scale-business-marketing'           => ['AI', 'How RankFyno uses AI to scale business marketing', 'The AI tools RankFyno uses to scale content, SEO research, and performance optimization without sacrificing quality.'],
  'the-complete-business-growth-blueprint-by-rankfyno'         => ['Blueprint', 'The complete business growth blueprint by RankFyno', 'The full RankFyno growth blueprint: positioning, demand generation, conversion, and retention.'],
  'how-rankfyno-helps-businesses-generate-qualified-leads'     => ['Lead Quality', 'How RankFyno helps businesses generate qualified leads', 'The qualification framework RankFyno uses to attract, filter, and deliver sales-ready leads.'],
  'rankfynos-local-seo-strategy-that-brings-more-customers'    => ['Local SEO', "RankFyno's local SEO strategy that brings more customers", 'The exact local SEO strategy RankFyno uses to put service-area businesses on top of the local pack.'],
  'why-businesses-trust-rankfyno-for-seo-and-performance-marketing' => ['Trust', 'Why businesses trust RankFyno for SEO and performance marketing', 'The trust signals that make RankFyno the agency ambitious brands choose.'],
  'how-rankfyno-improves-google-rankings-and-website-traffic'  => ['Rankings', 'How RankFyno improves Google rankings and website traffic', 'The technical and content work RankFyno does to lift Google rankings and compound organic traffic.'],
  'how-rankfyno-creates-powerful-brand-awareness-campaigns'    => ['Awareness', 'How RankFyno creates powerful brand awareness campaigns', 'The brand-awareness playbook RankFyno uses to put clients on the map and earn category recognition.'],
  'the-secret-behind-rankfynos-result-driven-marketing-approach' => ['Results', "The secret behind RankFyno's result-driven marketing approach", 'The principles and disciplines that make RankFyno consistently deliver measurable business results.'],
  'how-rankfyno-helps-businesses-increase-revenue-online'      => ['Revenue', 'How RankFyno helps businesses increase revenue online', 'The revenue-generation framework RankFyno uses to grow client businesses through compounding SEO and performance marketing.'],
  'why-rankfyno-is-the-best-digital-marketing-agency-for-growing-businesses' => ['Best Agency', 'Why RankFyno is the best digital marketing agency for growing businesses', "The differentiators that make RankFyno the agency growing businesses hire when they're done with commodity marketing work."],
  'how-rankfyno-combines-seo-ads-and-ai-for-maximum-growth'    => ['Stack', 'How RankFyno combines SEO, ads & AI for maximum growth', 'The integrated SEO + paid media + AI stack RankFyno runs to deliver compounding growth.'],
  'how-rankfyno-helps-businesses-build-authority-in-their-industry' => ['Authority', 'How RankFyno helps businesses build authority in their industry', 'The authority-building playbook RankFyno uses to make clients the reference point their competitors cite.'],
  'why-every-business-needs-a-growth-partner-like-rankfyno'    => ['Growth Partner', 'Why every business needs a growth partner like RankFyno', 'Why every ambitious business benefits from a senior growth partner — and what to look for in one.'],
  'how-rankfyno-turns-website-visitors-into-paying-customers'  => ['CRO', 'How RankFyno turns website visitors into paying customers', 'The conversion-rate optimization system RankFyno runs to turn more visitors into qualified customers.'],
  'case-study-how-rankfyno-helps-businesses-achieve-sustainable-growth' => ['Case Study', 'Case study: how RankFyno helps businesses achieve sustainable growth', "A representative case study showing how RankFyno's integrated approach delivers sustainable, compounding growth."],
  'why-businesses-across-industries-choose-rankfyno'           => ['Cross-Industry', 'Why businesses across industries choose RankFyno', 'The principles behind RankFyno\'s cross-industry effectiveness — and why ambitious brands in any category hire us.'],
  'the-future-of-digital-marketing-how-rankfyno-stays-ahead'   => ['Future', 'The future of digital marketing: how RankFyno stays ahead', 'Where digital marketing is heading — AI search, zero-click content, signal-rich SEO — and how RankFyno is built for it.'],
  'how-rankfyno-helps-businesses-scale-faster-with-data-driven-marketing' => ['Data-Driven', 'How RankFyno helps businesses scale faster with data-driven marketing', 'The data infrastructure and decision-making discipline RankFyno uses to make every marketing dollar accountable.'],
];

$canonical = $page_num <= 1
  ? 'https://rankfyno.com/blog/'
  : 'https://rankfyno.com/blog/?page=' . $page_num;

$custom_head = '
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <link rel="canonical" href="' . $canonical . '" />
  <meta property="og:type" content="website" />
  <meta property="og:site_name" content="rankfyno" />
  <meta property="og:title" content="SEO Blog — rankfyno" />
  <meta property="og:description" content="Practical SEO guides from the rankfyno team. Rank higher, recover traffic, and grow." />
  <meta property="og:url" content="' . $canonical . '" />
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
    .blog-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 32px; padding: 60px 0 40px; }
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
    .pagination {
      display: flex; justify-content: center; align-items: center; gap: 8px;
      padding: 40px 0 120px; flex-wrap: wrap;
    }
    .pagination a, .pagination span {
      display: inline-flex; align-items: center; justify-content: center;
      min-width: 44px; height: 44px; padding: 0 16px;
      border: 1px solid var(--line); border-radius: 10px;
      font-size: 14px; color: var(--ink-0); text-decoration: none;
      transition: background .2s, border-color .2s, color .2s;
    }
    .pagination a:hover { border-color: var(--accent); color: var(--accent); }
    .pagination .current {
      background: var(--ink-0); color: var(--bg-1); border-color: var(--ink-0);
      font-weight: 600;
    }
    .pagination .disabled {
      opacity: 0.4; cursor: not-allowed; pointer-events: none;
    }
    .pagination .gap {
      border: none; background: none; pointer-events: none;
      color: var(--ink-2);
    }
  </style>
';

$custom_head .= "\n" . $itemlist_script;
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
      <?php foreach ($page_posts as $post):
        $slug = $post['slug'];
        if (!isset($meta[$slug])) continue;
        [$tag, $title, $blurb] = $meta[$slug];
      ?>
        <a href="<?php echo $base_path; ?>blog/<?php echo $slug; ?>" class="blog-card" data-cursor-hover>
          <span class="tag"><?php echo htmlspecialchars($tag, ENT_QUOTES); ?></span>
          <h3><?php echo htmlspecialchars($title, ENT_QUOTES); ?></h3>
          <p><?php echo htmlspecialchars($blurb, ENT_QUOTES); ?></p>
        </a>
      <?php endforeach; ?>
    </div>

    <?php if ($total_pages > 1):
      // Build a compact page-number strip: show first, last, current ± 1, with gaps.
      $prev = max(1, $page_num - 1);
      $next = min($total_pages, $page_num + 1);
      $shown = [1, $total_pages];
      for ($i = max(1, $page_num - 1); $i <= min($total_pages, $page_num + 1); $i++) {
        $shown[] = $i;
      }
      $shown = array_unique($shown);
      sort($shown);
      $base_url = $base_path . 'blog/';
      $link = function ($p) use ($base_url) {
        return $p <= 1 ? $base_url : $base_url . '?page=' . $p;
      };
    ?>
      <nav class="pagination" aria-label="Blog pagination">
        <a href="<?php echo $link($prev); ?>" class="<?php echo $page_num <= 1 ? 'disabled' : ''; ?>" aria-label="Previous page">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M11 5l-7 7 7 7"/></svg>
        </a>
        <?php
        $prev_shown = 0;
        foreach ($shown as $p):
          if ($prev_shown && $p - $prev_shown > 1): ?>
            <span class="gap">&hellip;</span>
          <?php endif;
          if ($p === $page_num): ?>
            <span class="current" aria-current="page"><?php echo $p; ?></span>
          <?php else: ?>
            <a href="<?php echo $link($p); ?>"><?php echo $p; ?></a>
          <?php endif;
          $prev_shown = $p;
        endforeach; ?>
        <a href="<?php echo $link($next); ?>" class="<?php echo $page_num >= $total_pages ? 'disabled' : ''; ?>" aria-label="Next page">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </a>
      </nav>
    <?php endif; ?>
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