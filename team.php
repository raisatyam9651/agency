<?php
$base_path = '';
$current_page = 'team';
$page_title = 'Our Team — rankfyno';
$page_description = "Meet the rankfyno team — 21 specialists across SEO, sales, web development, design, HR, AI automation, client servicing, and YouTube SEO. The people who rank your business on page-1 of Google.";
$canonical_url = 'https://rankfyno.com/team.php';
$og_image = 'https://rankfyno.com/og-default.jpg';

$custom_head = '
  <!-- Team page styles moved to /style.css (TEAM PAGE STYLES section) -->';

$team_schema = '<script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":"https://rankfyno.com/#organization","name":"rankfyno","url":"https://rankfyno.com/"},{"@type":"Person","name":"Suraj Punia","jobTitle":"SEO Team Lead","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/suraj-punia.webp","contentUrl":"https://rankfyno.com/team/photos/suraj-punia.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Satyam Rai","jobTitle":"Senior SEO Executive","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/satyam-rai.webp","contentUrl":"https://rankfyno.com/team/photos/satyam-rai.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Amit Yadav","jobTitle":"SEO Executive","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/amit-yadav.webp","contentUrl":"https://rankfyno.com/team/photos/amit-yadav.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Shivant Chaurasiya","jobTitle":"SEO Executive","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/shivant-chaurasiya.webp","contentUrl":"https://rankfyno.com/team/photos/shivant-chaurasiya.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Abhishek Singh","jobTitle":"Sales Executive","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/abhishek-singh.webp","contentUrl":"https://rankfyno.com/team/photos/abhishek-singh.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Jaivijay Paswan","jobTitle":"Sales Executive","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/jaivijay-paswan.webp","contentUrl":"https://rankfyno.com/team/photos/jaivijay-paswan.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Bhanu Pratap","jobTitle":"Meta Ads Specialist","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/bhanu-pratap.webp","contentUrl":"https://rankfyno.com/team/photos/bhanu-pratap.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Manish Kushwaha","jobTitle":"Web Team Lead","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/manish-kushwaha.webp","contentUrl":"https://rankfyno.com/team/photos/manish-kushwaha.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Shivam Kumar","jobTitle":"Senior UI/UX Designer","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/shivam-kumar.webp","contentUrl":"https://rankfyno.com/team/photos/shivam-kumar.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Chitransh Saxena","jobTitle":"Web Developer","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/chitransh-saxena.webp","contentUrl":"https://rankfyno.com/team/photos/chitransh-saxena.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Nitest Agnihotri","jobTitle":"Graphic Designer","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/nitest-agnihotri.webp","contentUrl":"https://rankfyno.com/team/photos/nitest-agnihotri.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Tanmay","jobTitle":"Graphic Designer","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/tanmay.webp","contentUrl":"https://rankfyno.com/team/photos/tanmay.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Priya Bisht","jobTitle":"HR Manager","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/priya-bisht.webp","contentUrl":"https://rankfyno.com/team/photos/priya-bisht.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Ranveer Jaiswal","jobTitle":"AI Automation Engineer","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/ranveer-jaiswal.webp","contentUrl":"https://rankfyno.com/team/photos/ranveer-jaiswal.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Adit Singh","jobTitle":"Client Servicing","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/adit-singh.webp","contentUrl":"https://rankfyno.com/team/photos/adit-singh.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Om Nath Tripathi","jobTitle":"Client Servicing","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/om-nath-tripathi.webp","contentUrl":"https://rankfyno.com/team/photos/om-nath-tripathi.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Ichha Kumari","jobTitle":"Client Servicing","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/ichha-kumari.webp","contentUrl":"https://rankfyno.com/team/photos/ichha-kumari.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Himanshu Silori","jobTitle":"Studio Manager","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/himanshu-silori.webp","contentUrl":"https://rankfyno.com/team/photos/himanshu-silori.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Kishan Yadav","jobTitle":"YouTube SEO Specialist","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/kishan-yadav.webp","contentUrl":"https://rankfyno.com/team/photos/kishan-yadav.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}},{"@type":"Person","name":"Ansh Singh","jobTitle":"YouTube SEO Specialist","image":{"@type":"ImageObject","url":"https://rankfyno.com/team/photos/ansh-singh.webp","contentUrl":"https://rankfyno.com/team/photos/ansh-singh.jpg","width":400,"height":400},"worksFor":{"@type":"Organization","name":"rankfyno","url":"https://rankfyno.com/"}}]}</script>';
$custom_head .= $team_schema;


include __DIR__ . '/header.php';
?>

  <header class="hero" style="min-height: 70vh; padding: 180px 0 60px;">
    <div class="container hero-inner">
      <div class="hero-meta">
        <div class="hero-meta-left">
          <span class="eyebrow"><span class="dot"></span> The people behind the rankings</span>
        </div>
        <div class="hero-meta-info">/ team / about</div>
      </div>
      <h1 class="display">
        <div class="word"><span class="char">O</span><span class="char">u</span><span class="char">r</span></div>
        <div class="word"><span class="char gradient-text">t</span><span class="char gradient-text">e</span><span class="char gradient-text">a</span><span class="char gradient-text">m</span><span class="char">.</span></div>
        <div class="word"><span class="char outline-text">22 specialists.</span></div>
      </h1>
      <p class="hero-sub">A multidisciplinary team of SEO strategists, designers, developers, AI engineers, paid-media specialists, and client partners — built to rank businesses on page-1 of Google and keep them there.</p>
      <div class="hero-cta">
        <a href="#departments" class="btn btn-primary">Meet the team
          <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </a>
        <a href="contact.php" class="btn btn-ghost">Join us</a>
      </div>
    </div>
  </header>

  <section class="team-dept">
    <div class="container">
      <div class="team-stats">
        <div class="team-stat">
          <span class="num">22<span style="color: var(--accent);">+</span></span>
          <span class="lbl">Specialists on the team</span>
        </div>
        <div class="team-stat">
          <span class="num">10</span>
          <span class="lbl">Departments, one mission</span>
        </div>
        <div class="team-stat">
          <span class="num">6<span class="gradient-text">y</span></span>
          <span class="lbl">Average domain experience</span>
        </div>
        <div class="team-stat">
          <span class="num">24<span style="color: var(--accent);">/</span>7</span>
          <span class="lbl">Coverage across time zones</span>
        </div>
      </div>
    </div>
  </section>

  <section id="departments" class="team-dept">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow"><span class="dot"></span> Departments</span>
        <h2 class="display">Ten teams. <span class="gradient-text">One studio.</span></h2>
        <p class="section-sub">Every rankfyno project is staffed with specialists from across these departments — no generalists, no juniors learning on your account.</p>
      </div>

      <!-- 1. SEO -->
      <div class="dept-head" style="margin-top: 80px;">
        <div class="dept-head-left">
          <span class="eyebrow"><span class="dot"></span> 01 — Search</span>
          <h2 class="display">SEO</h2>
          <p class="dept-desc">The team that ranks your business. Audits, keyword research, on-page, content, links, and the reporting that proves it's working.</p>
        </div>
        <div class="dept-meta">
          <span class="count">04</span>
          <span>team members</span>
        </div>
      </div>
      <div class="team-grid">
        <div class="team-card tl">
          <div class="team-photo">
            <picture><source srcset="team/photos/suraj-punia.webp" type="image/webp"><img src="team/photos/suraj-punia.jpg" alt="Suraj Punia — SEO Team Lead at rankfyno" loading="lazy"/></picture>
                        <span class="initials">SP</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/mr-suraj-385071214/" class="team-linkedin" aria-label="Suraj Punia on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Suraj Punia</div>
            <div class="role">SEO Team Lead</div>
            <div class="tags">
              <span class="tag tag--accent">Team Lead</span>
              <span class="tag">Strategy</span>
            </div>
          </div>
        </div>
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/satyam-rai.webp" type="image/webp"><img src="team/photos/satyam-rai.jpg" alt="Satyam Rai — Senior SEO Executive at rankfyno" loading="lazy"/></picture>
                        <span class="initials">SR</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/rai-satyam-rai/" class="team-linkedin" aria-label="Satyam Rai on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Satyam Rai</div>
            <div class="role">Senior SEO Executive</div>
            <div class="tags">
              <span class="tag tag--lead">Senior</span>
              <span class="tag">On-page</span>
            </div>
          </div>
        </div>
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/amit-yadav.webp" type="image/webp"><img src="team/photos/amit-yadav.jpg" alt="Amit Yadav — SEO Executive at rankfyno" loading="lazy"/></picture>
                        <span class="initials">AY</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/amit-yadav-6924172a4/?skipRedirect=true" class="team-linkedin" aria-label="Amit Yadav on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Amit Yadav</div>
            <div class="role">SEO Executive</div>
            <div class="tags">
              <span class="tag">Execution</span>
            </div>
          </div>
        </div>
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/shivant-chaurasiya.webp" type="image/webp"><img src="team/photos/shivant-chaurasiya.jpg" alt="Shivant Chaurasiya — SEO Executive at rankfyno" loading="lazy"/></picture>
                        <span class="initials">SY</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/shivant-chaurasiya-b82000252/" class="team-linkedin" aria-label="Shivant Chaurasiya on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Shivant Chaurasiya</div>
            <div class="role">SEO Executive</div>
            <div class="tags">
              <span class="tag">Execution</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 2. SALES -->
      <div class="dept-head" style="margin-top: 100px;">
        <div class="dept-head-left">
          <span class="eyebrow"><span class="dot"></span> 02 — Revenue</span>
          <h2 class="display">Sales</h2>
          <p class="dept-desc">The first voice you hear. Discovery, qualification, and proposals — they turn "we need SEO" into a signed scope.</p>
        </div>
        <div class="dept-meta">
          <span class="count">02</span>
          <span>team members</span>
        </div>
      </div>
      <div class="team-grid">
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/abhishek-singh.webp" type="image/webp"><img src="team/photos/abhishek-singh.jpg" alt="Abhishek Singh — Sales Executive at rankfyno" loading="lazy"/></picture>
                        <span class="initials">AY</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/abhishek-singh-47684b215/" class="team-linkedin" aria-label="Abhishek Singh on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Abhishek Singh</div>
            <div class="role">Sales Executive</div>
            <div class="tags">
              <span class="tag">Closers</span>
            </div>
          </div>
        </div>
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/jaivijay-paswan.webp" type="image/webp"><img src="team/photos/jaivijay-paswan.jpg" alt="Jaivijay Paswan — Sales Executive at rankfyno" loading="lazy"/></picture>
                        <span class="initials">JP</span>
                        <span class="photo-hint">add photo</span>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Jaivijay Paswan</div>
            <div class="role">Sales Executive</div>
            <div class="tags">
              <span class="tag">Discovery</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 2.5 PAID MEDIA -->
      <div class="dept-head" style="margin-top: 100px;">
        <div class="dept-head-left">
          <span class="eyebrow"><span class="dot"></span> 03 — Acquisition</span>
          <h2 class="display">Paid Media</h2>
          <p class="dept-desc">Meta Ads, paid social, and the performance campaigns that put your brand in front of the right audience — fast.</p>
        </div>
        <div class="dept-meta">
          <span class="count">01</span>
          <span>team member</span>
        </div>
      </div>
      <div class="team-grid">
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/bhanu-pratap.webp" type="image/webp"><img src="team/photos/bhanu-pratap.jpg" alt="Bhanu Pratap — Meta Ads Specialist at rankfyno" loading="lazy"/></picture>
            <span class="initials">BP</span>
            <span class="photo-hint">add photo</span>
            <a href="https://www.linkedin.com/in/bhanu-pratap-61a7b72b6/" class="team-linkedin" aria-label="Bhanu Pratap on LinkedIn" target="_blank" rel="noopener">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
            </a>
            <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Bhanu Pratap</div>
            <div class="role">Meta Ads Specialist</div>
            <div class="tags">
              <span class="tag">Meta Ads</span>
              <span class="tag">Paid Social</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 3. WEB TEAM -->
      <div class="dept-head" style="margin-top: 100px;">
        <div class="dept-head-left">
          <span class="eyebrow"><span class="dot"></span> 04 — Engineering</span>
          <h2 class="display">Web Team</h2>
          <p class="dept-desc">Design, UX, and engineering. The team that builds the sites, funnels, and interfaces our SEO strategy is measured against.</p>
        </div>
        <div class="dept-meta">
          <span class="count">04</span>
          <span>team members</span>
        </div>
      </div>
      <div class="team-grid">
        <div class="team-card tl">
          <div class="team-photo">
            <picture><source srcset="team/photos/manish-kushwaha.webp" type="image/webp"><img src="team/photos/manish-kushwaha.jpg" alt="Manish Kushwaha — Web Team Lead at rankfyno" loading="lazy"/></picture>
                        <span class="initials">MK</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/manish-kushwahaa/" class="team-linkedin" aria-label="Manish Kushwaha on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Manish Kushwaha</div>
            <div class="role">Web Team Lead</div>
            <div class="tags">
              <span class="tag tag--accent">Team Lead</span>
              <span class="tag">Full-stack</span>
            </div>
          </div>
        </div>
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/shivam-kumar.webp" type="image/webp"><img src="team/photos/shivam-kumar.jpg" alt="Shivam Kumar — Senior UI/UX Designer at rankfyno" loading="lazy"/></picture>
                        <span class="initials">SV</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/shivam-kumar-4b334b210/" class="team-linkedin" aria-label="Shivam Kumar on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Shivam Kumar</div>
            <div class="role">Senior UI/UX Designer</div>
            <div class="tags">
              <span class="tag tag--lead">Senior</span>
              <span class="tag">Figma</span>
            </div>
          </div>
        </div>
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/chitransh-saxena.webp" type="image/webp"><img src="team/photos/chitransh-saxena.jpg" alt="Chitransh Saxena — Web Developer at rankfyno" loading="lazy"/></picture>
                        <span class="initials">CT</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/chitransh-saxena-699414229/" class="team-linkedin" aria-label="Chitransh Saxena on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Chitransh Saxena</div>
            <div class="role">Web Developer</div>
            <div class="tags">
              <span class="tag">Frontend</span>
              <span class="tag">Performance</span>
            </div>
          </div>
        </div>
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/nitest-agnihotri.webp" type="image/webp"><img src="team/photos/nitest-agnihotri.jpg" alt="Nitest Agnihotri — Graphic Designer at rankfyno" loading="lazy"/></picture>
                        <span class="initials">NA</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/nitesh-agnihotri/" class="team-linkedin" aria-label="Nitest Agnihotri on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Nitest Agnihotri</div>
            <div class="role">Graphic Designer</div>
            <div class="tags">
              <span class="tag">Branding</span>
            </div>
          </div>
        </div>
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/tanmay.webp" type="image/webp"><img src="team/photos/tanmay.jpg" alt="Tanmay — Graphic Designer at rankfyno" loading="lazy"/></picture>
                        <span class="initials">TM</span>
                        <span class="photo-hint">add photo</span>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Tanmay</div>
            <div class="role">Graphic Designer</div>
            <div class="tags">
              <span class="tag">Motion</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 4. HR -->
      <div class="dept-head" style="margin-top: 100px;">
        <div class="dept-head-left">
          <span class="eyebrow"><span class="dot"></span> 05 — People</span>
          <h2 class="display">Human Resources</h2>
          <p class="dept-desc">Hiring, culture, and the operational glue that keeps 21 specialists shipping on time.</p>
        </div>
        <div class="dept-meta">
          <span class="count">01</span>
          <span>team member</span>
        </div>
      </div>
      <div class="team-grid">
        <div class="team-card hr">
          <div class="team-photo">
            <picture><source srcset="team/photos/priya-bisht.webp" type="image/webp"><img src="team/photos/priya-bisht.jpg" alt="Priya Bisht — HR Manager at rankfyno" loading="lazy"/></picture>
                        <span class="initials">PB</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/priya-bisht-b5ab3322a/" class="team-linkedin" aria-label="Priya Bisht on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Priya Bisht</div>
            <div class="role">HR Manager</div>
            <div class="tags">
              <span class="tag tag--accent">People Ops</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 5. AI AUTOMATION -->
      <div class="dept-head" style="margin-top: 100px;">
        <div class="dept-head-left">
          <span class="eyebrow"><span class="dot"></span> 06 — Future</span>
          <h2 class="display">AI Automation</h2>
          <p class="dept-desc">Internal tooling, AI-driven reporting, and workflow automation — so the rest of the team can ship 10x faster.</p>
        </div>
        <div class="dept-meta">
          <span class="count">01</span>
          <span>team member</span>
        </div>
      </div>
      <div class="team-grid">
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/ranveer-jaiswal.webp" type="image/webp"><img src="team/photos/ranveer-jaiswal.jpg" alt="Ranveer Jaiswal — AI Automation Engineer at rankfyno" loading="lazy"/></picture>
                        <span class="initials">RJ</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/ranveer-jaiswal-966289238/" class="team-linkedin" aria-label="Ranveer Jaiswal on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Ranveer Jaiswal</div>
            <div class="role">AI Automation Engineer</div>
            <div class="tags">
              <span class="tag">LLMs</span>
              <span class="tag">Workflows</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 6. CLIENT SERVICING -->
      <div class="dept-head" style="margin-top: 100px;">
        <div class="dept-head-left">
          <span class="eyebrow"><span class="dot"></span> 07 — Relationships</span>
          <h2 class="display">Client Servicing</h2>
          <p class="dept-desc">Your daily point of contact. Briefs in, deliverables out, status calls scheduled, and the bridge between you and execution.</p>
        </div>
        <div class="dept-meta">
          <span class="count">03</span>
          <span>team members</span>
        </div>
      </div>
      <div class="team-grid">
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/adit-singh.webp" type="image/webp"><img src="team/photos/adit-singh.jpg" alt="Adit Singh — Client Servicing at rankfyno" loading="lazy"/></picture>
                        <span class="initials">AS</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/aditisingh2001/?skipRedirect=true" class="team-linkedin" aria-label="Adit Singh on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Adit Singh</div>
            <div class="role">Client Servicing</div>
            <div class="tags">
              <span class="tag">Account Lead</span>
            </div>
          </div>
        </div>
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/om-nath-tripathi.webp" type="image/webp"><img src="team/photos/om-nath-tripathi.jpg" alt="Om Nath Tripathi — Client Servicing at rankfyno" loading="lazy"/></picture>
                        <span class="initials">OT</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/om-nath-tripathi-693a10195/" class="team-linkedin" aria-label="Om Nath Tripathi on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Om Nath Tripathi</div>
            <div class="role">Client Servicing</div>
            <div class="tags">
              <span class="tag">Account Lead</span>
            </div>
          </div>
        </div>
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/ichha-kumari.webp" type="image/webp"><img src="team/photos/ichha-kumari.jpg" alt="Ichha Kumari — Client Servicing at rankfyno" loading="lazy"/></picture>
                        <span class="initials">IK</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/ichha-kumari/?skipRedirect=true" class="team-linkedin" aria-label="Ichha Kumari on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Ichha Kumari</div>
            <div class="role">Client Servicing</div>
            <div class="tags">
              <span class="tag">Account Lead</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 7. MANAGER -->
      <div class="dept-head" style="margin-top: 100px;">
        <div class="dept-head-left">
          <span class="eyebrow"><span class="dot"></span> 08 — Leadership</span>
          <h2 class="display">Management</h2>
          <p class="dept-desc">Strategic direction, cross-department coordination, and the final word on delivery quality.</p>
        </div>
        <div class="dept-meta">
          <span class="count">01</span>
          <span>team member</span>
        </div>
      </div>
      <div class="team-grid">
        <div class="team-card manager">
          <div class="team-photo">
            <picture><source srcset="team/photos/himanshu-silori.webp" type="image/webp"><img src="team/photos/himanshu-silori.jpg" alt="Himanshu Silori — Studio Manager at rankfyno" loading="lazy"/></picture>
                        <span class="initials">HS</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/himanshu-silori-570b821b1/" class="team-linkedin" aria-label="Himanshu Silori on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Himanshu Silori</div>
            <div class="role">Studio Manager</div>
            <div class="tags">
              <span class="tag tag--accent">Studio Manager</span>
              <span class="tag">Strategy</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 8. YOUTUBE SEO -->
      <div class="dept-head" style="margin-top: 100px;">
        <div class="dept-head-left">
          <span class="eyebrow"><span class="dot"></span> 09 — Video</span>
          <h2 class="display">YouTube SEO</h2>
          <p class="dept-desc">Channel growth, video optimization, and the second-screen search that drives 40%+ of discovery for our creator and D2C clients.</p>
        </div>
        <div class="dept-meta">
          <span class="count">02</span>
          <span>team members</span>
        </div>
      </div>
      <div class="team-grid">
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/kishan-yadav.webp" type="image/webp"><img src="team/photos/kishan-yadav.jpg" alt="Kishan Yadav — YouTube SEO Specialist at rankfyno" loading="lazy"/></picture>
                        <span class="initials">KY</span>
                        <span class="photo-hint">add photo</span>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Kishan Yadav</div>
            <div class="role">YouTube SEO Specialist</div>
            <div class="tags">
              <span class="tag">Titles</span>
              <span class="tag">Retention</span>
            </div>
          </div>
        </div>
        <div class="team-card">
          <div class="team-photo">
            <picture><source srcset="team/photos/ansh-singh.webp" type="image/webp"><img src="team/photos/ansh-singh.jpg" alt="Ansh Singh — YouTube SEO Specialist at rankfyno" loading="lazy"/></picture>
                        <span class="initials">AS</span>
                        <span class="photo-hint">add photo</span>
                        <a href="https://www.linkedin.com/in/ansh-singh-800760214/" class="team-linkedin" aria-label="Ansh Singh on LinkedIn" target="_blank" rel="noopener">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"/></svg>
                        </a>
                        <span class="status"></span>
          </div>
          <div class="body">
            <div class="name">Ansh Singh</div>
            <div class="role">YouTube SEO Specialist</div>
            <div class="tags">
              <span class="tag">Shorts</span>
              <span class="tag">Analytics</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- VALUES -->
  <section class="team-dept">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow"><span class="dot"></span> How we work</span>
        <h2 class="display">The rankfyno <span class="gradient-text">operating principles.</span></h2>
        <p class="section-sub">Four rules every team member signs onto. They define what it\'s like to work with us — and inside us.</p>
      </div>
      <div class="value-grid">
        <div class="value-card">
          <div class="icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3v18h18"/><path d="M7 14l4-4 4 4 5-5"/></svg>
          </div>
          <h3>Numbers, not narratives</h3>
          <p>If it can\'t be measured, it doesn\'t ship. Every report we send has rankings, traffic, leads, and revenue — not adjectives.</p>
        </div>
        <div class="value-card">
          <div class="icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87L18.18 22 12 18.27 5.82 22 7 14.14l-5-4.87 6.91-1.01L12 2z"/></svg>
          </div>
          <h3>Senior on every account</h3>
          <p>No juniors learning on your budget. Every rankfyno project has at least one senior strategist reviewing every output.</p>
        </div>
        <div class="value-card">
          <div class="icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
          </div>
          <h3>Speed compounds</h3>
          <p>A 24-hour turnaround beats a perfect 5-day one. We optimise for shipping — then iterate toward perfection.</p>
        </div>
        <div class="value-card">
          <div class="icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <h3>Cross-team by default</h3>
          <p>SEO alone doesn\'t ship. Every project pulls from SEO, web, design, and AI teams in parallel — not in sequence.</p>
        </div>
        <div class="value-card">
          <div class="icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>
          </div>
          <h3>Direct, never evasive</h3>
          <p>Bad news travels first. We\'d rather tell you a campaign is failing on day 14 than day 90 — so we can fix it together.</p>
        </div>
        <div class="value-card">
          <div class="icon">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
          </div>
          <h3>Build, don\'t borrow</h3>
          <p>Our tools, our frameworks, our reporting. We don\'t resell other agencies\' playbooks — we engineer ours.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- JOIN US -->
  <section class="cta-section" style="padding: 100px 0; border-top: 1px solid var(--border);">
    <div class="container" style="text-align: center;">
      <span class="eyebrow"><span class="dot"></span> Joining rankfyno</span>
      <h2 class="display" style="margin-top: 30px;">We\'re hiring across<br /><span class="gradient-text">SEO, design, and AI.</span></h2>
      <p class="section-sub" style="margin-top: 30px; max-width: 620px; margin-left: auto; margin-right: auto;">If you\'d ship better work with 20 other specialists backing you up — and you\'d rather be paid for outcomes than hours — we should talk.</p>
      <div class="hero-cta" style="margin-top: 50px; justify-content: center;">
        <a href="contact.php" class="btn btn-primary">Apply now
          <svg class="arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </a>
        <a href="./" class="btn btn-ghost">Back to home</a>
      </div>
    </div>
  </section>

<?php
include __DIR__ . '/footer.php';
?>
