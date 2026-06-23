<?php
$base_path = isset($base_path) ? $base_path : '';
?>
  <!-- =========================
       Footer
       ========================= -->
  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="<?php echo $base_path ?: './'; ?>" class="logo">
            <img src="<?php echo $base_path; ?>Rankfyno.svg" alt="rankfyno — Digital Marketing Agency" class="logo-img" width="32" height="32" />
            rankfyno
          </a>
          <p><?php echo isset($footer_brand_desc) ? $footer_brand_desc : 'A premium digital marketing studio for ambitious brands. Engineering growth since 2018.'; ?></p>
          <div class="footer-socials">
            <a href="https://twitter.com/rankfyno" target="_blank" rel="noopener" class="footer-social" data-cursor-hover aria-label="X / Twitter">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
            </a>
            <a href="https://www.linkedin.com/company/rankfyno" target="_blank" rel="noopener" class="footer-social" data-cursor-hover aria-label="LinkedIn">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
            </a>
            <a href="https://www.instagram.com/rankfyno" target="_blank" rel="noopener" class="footer-social" data-cursor-hover aria-label="Instagram">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>
            </a>
            <a href="https://github.com/rankfyno" target="_blank" rel="noopener" class="footer-social" data-cursor-hover aria-label="GitHub">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.4 3-.405 1.02.005 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
            </a>
          </div>
        </div>
        <?php if (isset($custom_footer_cols)): ?>
          <?php echo $custom_footer_cols; ?>
        <?php else: ?>
          <div class="footer-col">
            <h5>Capabilities</h5>
            <ul>
              <li><a href="<?php echo ($base_path ?: './') . '#services'; ?>" data-cursor-hover>Performance Marketing</a></li>
              <li><a href="<?php echo ($base_path ?: './') . '#services'; ?>" data-cursor-hover>SEO &amp; Organic</a></li>
              <li><a href="<?php echo ($base_path ?: './') . '#services'; ?>" data-cursor-hover>Brand &amp; Identity</a></li>
              <li><a href="<?php echo ($base_path ?: './') . '#services'; ?>" data-cursor-hover>AI Marketing</a></li>
              <li><a href="<?php echo ($base_path ?: './') . '#services'; ?>" data-cursor-hover>Web &amp; Product</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h5>Studio</h5>
            <ul>
              <li><a href="<?php echo ($base_path ?: './') . '#work'; ?>" data-cursor-hover>Selected work</a></li>
              <li><a href="<?php echo ($base_path ?: './') . '#process'; ?>" data-cursor-hover>Process</a></li>
              <li><a href="<?php echo ($base_path ?: './') . '#pricing'; ?>" data-cursor-hover>Pricing</a></li>
              <li><a href="<?php echo $base_path; ?>team.php" data-cursor-hover>Team</a></li>
              <li><a href="<?php echo $base_path; ?>blog" data-cursor-hover>Blog</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h5>Contact</h5>
            <ul>
              <li><a href="<?php echo $base_path; ?>contact.php" data-cursor-hover>Start a project</a></li>
              <li><a href="mailto:hello@rankfyno.com" data-cursor-hover>hello@rankfyno.com</a></li>
              <li><a href="tel:+917317564794" data-cursor-hover>+91 7317564794</a></li>
              <li><a href="https://maps.google.com/?q=Ground+Floor+Cabin+12+Plot+84+SupremeWork+Sector+32+Gurugram+Haryana+122001" target="_blank" rel="noopener" data-cursor-hover>Ground Floor, Cabin no 12, Plot 84, SupremeWork, Sector 32, Gurugram, Haryana 122001</a></li>
            </ul>
          </div>
        <?php endif; ?>
      </div>
      <div class="footer-map">
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3709.116323810718!2d77.03994080000001!3d28.445505599999997!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390d19448cf31c3d%3A0xcc37d1bd76d90887!2sRankfyno!5e1!3m2!1sen!2sin!4v1782195027075!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>
      <div class="footer-bottom">
        <p>© 2026 rankfyno. All rights reserved.</p>
      </div>
    </div>
  </footer>

  <script src="<?php echo $base_path; ?>script.js"></script>
  <?php if (isset($custom_scripts)) { echo $custom_scripts; } ?>
</body>
</html>
