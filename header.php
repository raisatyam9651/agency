<?php
// Set layout variables defaults
$base_path = isset($base_path) ? $base_path : '';
$page_title = isset($page_title) ? $page_title : 'rankfyno — Engineering Digital Growth';
$page_description = isset($page_description) ? $page_description : 'rankfyno — Engineering digital growth for the world\'s most ambitious brands. A premium 3D digital marketing agency.';
$current_page = isset($current_page) ? $current_page : '';
$is_home = ($current_page === 'home');
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="<?php echo htmlspecialchars($page_description); ?>" />
  <title><?php echo htmlspecialchars($page_title); ?></title>
  
  <?php include __DIR__ . '/header-include.php'; ?>

  <?php if (isset($custom_head)) { echo $custom_head; } ?>
</head>
<body>
  <div class="ambient" aria-hidden="true"></div>
  <div class="grid-overlay" aria-hidden="true"></div>
  
  <?php if (isset($custom_body_elements)) { echo $custom_body_elements; } ?>

  <div class="cursor" id="cursor" aria-hidden="true"></div>
  <div class="cursor-follower" id="cursor-follower" aria-hidden="true"></div>

  <!-- =========================
       Navigation
       ========================= -->
  <nav class="nav" id="nav">
    <div class="container nav-inner">
      <a href="<?php echo $base_path ?: './'; ?>" class="logo" data-cursor-hover>
        <img src="<?php echo $base_path; ?>Rankfyno.png" alt="rankfyno" class="logo-img" />
        rankfyno
      </a>
      <ul class="nav-links">
        <li><a href="<?php echo $is_home ? '#services' : ($base_path ?: './') . '#services'; ?>" data-cursor-hover>Services</a></li>
        <li><a href="<?php echo $is_home ? '#work' : ($base_path ?: './') . '#work'; ?>" data-cursor-hover>Work</a></li>
        <li><a href="<?php echo $is_home ? '#process' : ($base_path ?: './') . '#process'; ?>" data-cursor-hover>Process</a></li>
        <li><a href="<?php echo $is_home ? '#pricing' : ($base_path ?: './') . '#pricing'; ?>" data-cursor-hover>Pricing</a></li>
        <li><a href="<?php echo $is_home ? '#faq' : ($base_path ?: './') . '#faq'; ?>" data-cursor-hover>FAQ</a></li>
        <li><a href="<?php echo $base_path; ?>team.php" class="<?php echo ($current_page === 'team') ? 'active' : ''; ?>" data-cursor-hover>Team</a></li>
        <li><a href="<?php echo $base_path; ?>blog" class="<?php echo ($current_page === 'blog') ? 'active' : ''; ?>" data-cursor-hover>Blog</a></li>
        <li><a href="<?php echo $base_path; ?>contact.php" class="<?php echo ($current_page === 'contact') ? 'active' : ''; ?>" data-cursor-hover>Contact</a></li>
      </ul>
      <div class="nav-divider"></div>
      <div class="nav-cta">
        <a href="<?php echo $base_path; ?>contact.php" class="btn btn-primary" data-cursor-hover>
          Start a project
          <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </a>
        <button class="menu-toggle" data-cursor-hover aria-label="Menu"><span></span></button>
      </div>
    </div>
  </nav>
