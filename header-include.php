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
// $canonical_url, $og_image, $page_type.
//
// Most pages also hand-roll these tags inside $custom_head, which header.php echoes
// straight after this file. Emitting a default unconditionally would then put two of
// each tag on the page — and two conflicting rel=canonical means Google honours
// neither. $custom_head is already an evaluated PHP string here (its \" escapes are
// real quotes by now), so we can just ask whether the page supplies a tag itself and
// stand down if it does. Page-supplied wins; the default only fills a genuine gap.
$bp = isset($base_path) ? $base_path : '';
$def_title = isset($page_title) ? $page_title : 'rankfyno — Digital Marketing Agency';
$def_desc  = isset($page_description) ? $page_description : 'rankfyno is a premium digital marketing studio for ambitious brands. SEO, performance marketing, AI marketing, brand & web — engineered to compound.';
$canon     = isset($canonical_url) ? $canonical_url : 'https://rankfyno.com/';
$og_img    = isset($og_image) ? $og_image : 'https://rankfyno.com/og-default.jpg';
$ptype     = isset($page_type) ? $page_type : 'website';
$pub_name  = 'rankfyno';

$__ch = isset($custom_head) ? $custom_head : '';
// True when $custom_head already emits this tag, e.g. $page_has('rel="canonical"').
// A closure rather than a named function: this file is included once per request today,
// but a named function would fatal on redeclare if that ever stopped being true.
$page_has = function ($needle) use ($__ch) {
  return $__ch !== '' && strpos($__ch, $needle) !== false;
};
?>
<?php if (!$page_has('name="robots"')): ?>
<meta name="robots" content="index, follow, max-image-preview:large" />
<?php endif; ?>
<?php if (!$page_has('rel="canonical"')): ?>
<link rel="canonical" href="<?php echo htmlspecialchars($canon, ENT_QUOTES); ?>" />
<?php endif; ?>
<?php if (!$page_has('property="og:type"')): ?>
<meta property="og:type" content="<?php echo htmlspecialchars($ptype, ENT_QUOTES); ?>" />
<?php endif; ?>
<?php if (!$page_has('property="og:site_name"')): ?>
<meta property="og:site_name" content="<?php echo htmlspecialchars($pub_name, ENT_QUOTES); ?>" />
<?php endif; ?>
<?php if (!$page_has('property="og:title"')): ?>
<meta property="og:title" content="<?php echo htmlspecialchars($def_title, ENT_QUOTES); ?>" />
<?php endif; ?>
<?php if (!$page_has('property="og:description"')): ?>
<meta property="og:description" content="<?php echo htmlspecialchars($def_desc, ENT_QUOTES); ?>" />
<?php endif; ?>
<?php if (!$page_has('property="og:url"')): ?>
<meta property="og:url" content="<?php echo htmlspecialchars($canon, ENT_QUOTES); ?>" />
<?php endif; ?>
<?php if (!$page_has('property="og:image"')): ?>
<meta property="og:image" content="<?php echo htmlspecialchars($og_img, ENT_QUOTES); ?>" />
<?php endif; ?>
<?php if (!$page_has('property="og:locale"')): ?>
<meta property="og:locale" content="en_IN" />
<?php endif; ?>
<?php if (!$page_has('name="twitter:card"')): ?>
<meta name="twitter:card" content="summary_large_image" />
<?php endif; ?>
<?php if (!$page_has('name="twitter:title"')): ?>
<meta name="twitter:title" content="<?php echo htmlspecialchars($def_title, ENT_QUOTES); ?>" />
<?php endif; ?>
<?php if (!$page_has('name="twitter:description"')): ?>
<meta name="twitter:description" content="<?php echo htmlspecialchars($def_desc, ENT_QUOTES); ?>" />
<?php endif; ?>
<?php if (!$page_has('name="twitter:image"')): ?>
<meta name="twitter:image" content="<?php echo htmlspecialchars($og_img, ENT_QUOTES); ?>" />
<?php endif; ?>
<link rel="preload" as="image" href="<?php echo $bp; ?>Rankfyno.svg" fetchpriority="high" />