<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link
    rel="stylesheet"
    media="print"
    onload="this.media='all'"
    href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" />
<noscript>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" />
</noscript>
<link rel="icon" type="image/svg+xml" href="<?php echo isset($base_path) ? $base_path : ''; ?>Rankfyno.svg" />
<link rel="preload" href="<?php echo isset($base_path) ? $base_path : ''; ?>style.css" as="style" />
<link rel="stylesheet" href="<?php echo isset($base_path) ? $base_path : ''; ?>style.css" media="print" onload="this.media='all'" />
<noscript><link rel="stylesheet" href="<?php echo isset($base_path) ? $base_path : ''; ?>style.css" /></noscript>
<meta name="google-site-verification" content="FzZzS2kZwMQ43aZoC4qPO4_1CDOvCB4-Ix2YWu5Y1Mk" />
<?php
// Default SEO meta — overridable per page via $page_title, $page_description,
// $canonical_url, $og_image. Each root page sets these via $custom_head.
$bp = isset($base_path) ? $base_path : '';
$def_title = isset($page_title) ? $page_title : 'rankfyno — Digital Marketing Agency';
$def_desc  = isset($page_description) ? $page_description : 'rankfyno is a premium digital marketing studio for ambitious brands. SEO, performance marketing, AI marketing, brand & web — engineered to compound.';
$canon     = isset($canonical_url) ? $canonical_url : 'https://rankfyno.com/';
$og_img    = isset($og_image) ? $og_image : 'https://rankfyno.com/og-default.jpg';
$ptype     = isset($page_type) ? $page_type : 'website';
$pub_name  = 'rankfyno';
?>
<meta name="robots" content="index, follow, max-image-preview:large" />
<link rel="canonical" href="<?php echo htmlspecialchars($canon, ENT_QUOTES); ?>" />
<meta property="og:type" content="<?php echo htmlspecialchars($ptype, ENT_QUOTES); ?>" />
<meta property="og:site_name" content="<?php echo htmlspecialchars($pub_name, ENT_QUOTES); ?>" />
<meta property="og:title" content="<?php echo htmlspecialchars($def_title, ENT_QUOTES); ?>" />
<meta property="og:description" content="<?php echo htmlspecialchars($def_desc, ENT_QUOTES); ?>" />
<meta property="og:url" content="<?php echo htmlspecialchars($canon, ENT_QUOTES); ?>" />
<meta property="og:image" content="<?php echo htmlspecialchars($og_img, ENT_QUOTES); ?>" />
<meta property="og:locale" content="en_IN" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="<?php echo htmlspecialchars($def_title, ENT_QUOTES); ?>" />
<meta name="twitter:description" content="<?php echo htmlspecialchars($def_desc, ENT_QUOTES); ?>" />
<meta name="twitter:image" content="<?php echo htmlspecialchars($og_img, ENT_QUOTES); ?>" />
<link rel="preload" as="image" href="<?php echo $bp; ?>Rankfyno.svg" fetchpriority="high" />