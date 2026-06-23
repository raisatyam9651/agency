<?php
$base_path = '';
$current_page = '404';
$page_title = 'Page not found — rankfyno';
$page_description = 'The page you are looking for does not exist. Return to the rankfyno homepage or browse our SEO blog.';
$canonical_url = 'https://rankfyno.com/404.php';
http_response_code(404);
include __DIR__ . '/header.php';
?>

  <section class="hero" style="min-height: 80vh; padding: 180px 0 60px; text-align: center;">
    <div class="container">
      <span class="eyebrow"><span class="dot"></span> 404</span>
      <h1 class="display" style="margin: 24px 0 16px;">We couldn't find that page.</h1>
      <p class="hero-sub" style="margin: 0 auto 32px; max-width: 560px;">
        The link may be broken, or the page may have moved. Try one of these instead:
      </p>
      <div style="display: flex; gap: 12px; justify-content: center; flex-wrap: wrap; margin-top: 32px;">
        <a href="<?php echo $base_path; ?>" class="btn btn-primary" data-cursor-hover>
          Home
          <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </a>
        <a href="<?php echo $base_path; ?>blog" class="btn btn-ghost" data-cursor-hover>SEO Blog</a>
        <a href="<?php echo $base_path; ?>contact.php" class="btn btn-ghost" data-cursor-hover>Contact</a>
      </div>
    </div>
  </section>

<?php include __DIR__ . '/footer.php'; ?>