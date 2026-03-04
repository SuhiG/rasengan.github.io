---
permalink: /
title: "About"
author_profile: true
show_title: false
redirect_from:
  - /about/
  - /about.html
---


<div class="about-hero-card" role="region" aria-label="About section introduction">
  <figure class="about-hero-media">
    <img src="{{ '/IMG_1870.jpeg' | absolute_url }}" alt="Sudeera's creative workspace">
  </figure>

  <div class="about-hero-content">
    <div class="quantum-visual" aria-hidden="true">
      <span class="quantum-node quantum-node--core"></span>
      <span class="quantum-node quantum-node--orbit-a"></span>
      <span class="quantum-node quantum-node--orbit-b"></span>
      <span class="quantum-ring quantum-ring--one"></span>
      <span class="quantum-ring quantum-ring--two"></span>
      <span class="quantum-ring quantum-ring--three"></span>
    </div>

    <h1>ආයුබෝවන්!<span aria-hidden="true">👋</span></h1>
    <p class="about-hero-tagline">LLMs, Quantum, and Supercomputers.</p>

    <p>
      Research scientist at AIST’s G-QuAT with a Ph.D. in AI from Institute of Science Tokyo, I develop optimization, simulation, and machine learning methods across quantum and high-performance computing systems. My work spans LLMs, CIMs, image reconstruction, and real-world applications.
    </p>

    {% assign scholar_link = site.author.googlescholar | default: 'https://scholar.google.com/citations?user=AoeGGVQAAAAJ&hl=en' %}
    {% assign linkedin_handle = site.author.linkedin | default: '' %}
    {% assign linkedin_link = linkedin_handle %}
    {% unless linkedin_link contains 'http' %}
      {% assign linkedin_link = 'https://www.linkedin.com/in/' | append: linkedin_handle %}
    {% endunless %}
    {% if linkedin_handle == '' %}
      {% assign linkedin_link = 'https://www.linkedin.com/' %}
    {% endif %}
    {% assign twitter_handle = site.author.twitter | default: '' %}
    {% assign twitter_link = twitter_handle %}
    {% unless twitter_link contains 'http' %}
      {% assign twitter_link = 'https://x.com/' | append: twitter_handle %}
    {% endunless %}
    {% if twitter_handle == '' %}
      {% assign twitter_link = 'https://x.com/' %}
    {% endif %}
    {% assign github_handle = site.author.github | default: '' %}
    {% assign github_link = github_handle %}
    {% unless github_link contains 'http' %}
      {% assign github_link = 'https://github.com/' | append: github_handle %}
    {% endunless %}
    {% if github_handle == '' %}
      {% assign github_link = 'https://github.com/' %}
    {% endif %}
    {% assign gquat_link = site.author.gquat | default: 'https://unit.aist.go.jp/g-quat/index_en.html' %}

    <div class="about-hero-actions" aria-label="Profile links">
      <a class="about-hero-action-btn" href="{{ scholar_link }}" target="_blank" rel="noopener">
        <span>Google Scholar</span>
      </a>
      <a class="about-hero-action-btn about-hero-action-btn--linkedin" href="{{ linkedin_link }}" target="_blank" rel="noopener">
        <span>LinkedIn</span>
      </a>
      <a class="about-hero-action-btn about-hero-action-btn--twitter" href="{{ twitter_link }}" target="_blank" rel="noopener">
        <span>Twitter</span>
      </a>
      <a class="about-hero-action-btn about-hero-action-btn--github" href="{{ github_link }}" target="_blank" rel="noopener">
        <span>GitHub</span>
      </a>
      <a class="about-hero-action-btn about-hero-action-btn--gquat" href="{{ gquat_link }}" target="_blank" rel="noopener">
        <span>G-QuAT</span>
      </a>
    </div>

    {% assign scholar_stats = site.data.google_scholar_stats %}
    {% assign papers_published_count = site.data.google_scholar_publications | size %}
    <div class="about-hero-stats" role="group" aria-label="Google Scholar metrics">
      <article class="about-hero-stat-card">
        <p class="about-hero-stat-label">Citations</p>
        <p class="about-hero-stat-value">{{ scholar_stats.citations | default: '--' }}</p>
      </article>
      <article class="about-hero-stat-card">
        <p class="about-hero-stat-label">h-index</p>
        <p class="about-hero-stat-value">{{ scholar_stats.h_index | default: '--' }}</p>
      </article>
      <article class="about-hero-stat-card">
        <p class="about-hero-stat-label">i10-index</p>
        <p class="about-hero-stat-value">{{ scholar_stats.i10_index | default: '--' }}</p>
      </article>
      <article class="about-hero-stat-card">
        <p class="about-hero-stat-label">Papers Published</p>
        <p class="about-hero-stat-value">{{ papers_published_count | default: '--' }}</p>
      </article>
    </div>
  </div>
</div>

## News

<div class="home-feed-layout">
  <div class="news-panel" role="region" aria-label="Recent academic news">
    <ul class="news-list">
      <li><strong>2024-10-18:</strong> Presented at <a href="https://www.ucl.ac.uk/quantum/innovation/inqa/inqa-conference/inqa-conference-2024" target="_blank">International Network on Quantum Annealing 2024 (INQA 2024)</a> (Tokyo, Japan).</li>
      <li><strong>2024-10-01:</strong> Tokyo Institute of Technology became the <a href="https://www.isct.ac.jp/ja" target="_blank">Institute of Science Tokyo</a>.</li>
      <li><strong>2024-08-11:</strong> Presented at <a href="https://www.aisf.or.jp/AFC/2024/category/news-ja/" target="_blank">Asia Future Conference (AFC) 2024</a>; received Best Presentation Award (Bangkok, Thailand).</li>
      <li><strong>2024-07-08:</strong> Preliminary doctoral defense (Day 2).</li>
      <li><strong>2024-07-03:</strong> Preliminary doctoral defense (Day 1).</li>
      <li><strong>2024-04-21:</strong> One talk and one poster accepted at <a href="https://iop.eventsair.com/aqc2024/" target="_blank">Adiabatic Quantum Computing (AQC) 2024</a> (Glasgow, UK).</li>
      <li><strong>2024-04-12:</strong> Presented at the 2024 NTT Retreat meeting (San Francisco, USA).</li>
      <li><strong>2024-03-18:</strong> Presented at the 2024 Spring Meeting of the <a href="https://onsite.gakkai-web.net/jps/jps_search/2024sp/index.html" target="_blank">Physical Society of Japan</a>.</li>
      <li><strong>2024-02-09:</strong> Invited talk at the NTT-RIKEN workshop on photonics, neural networks, and specialized hardware for combinatorial optimization.</li>
      <li><strong>2024-01-16:</strong> Two contributed talks (2nd author) accepted at the 2024 Spring Meeting of the <a href="https://onsite.gakkai-web.net/jps/jps_search/2024sp/index.html" target="_blank">Physical Society of Japan</a>.</li>
      <li><strong>2023-12-27:</strong> Talk accepted for <a href="https://www.qcomp.irfi.titech.ac.jp/quantum_annealing_workshop2024.html" target="_blank">第2回量子アニーリング及び関連技術に関する研究会</a>.</li>
      <li><strong>2023-12-08:</strong> Awarded scholarship from the <a href="https://www.aisf.or.jp/jp/" target="_blank">Atsumi International Foundation</a>.</li>
      <li><strong>2023-11-17:</strong> Poster accepted for <a href="https://qip2024.tw/site/page.aspx?pid=901&sid=1522&lang=en" target="_blank">Quantum Information Processing (QIP) 2024</a> (Taipei, Taiwan).</li>
      <li><strong>2023-11-17:</strong> Paper published in <a href="https://doi.org/10.1063/5.0176248" target="_blank">Journal of Applied Physics</a>.</li>
      <li><strong>2023-09-26:</strong> Paper published in <a href="https://doi.org/10.1038/s41598-023-43364-8" target="_blank">Scientific Reports</a>.</li>
      <li><strong>2023-08-30:</strong> Mid-term doctoral evaluation (Day 2).</li>
      <li><strong>2023-08-24:</strong> Mid-term doctoral evaluation (Day 1).</li>
      <li><strong>2023-08-08:</strong> Poster presentation at <a href="https://statphys28.org/index.html" target="_blank">StatPhys28</a>, University of Tokyo.</li>
      <li><strong>2023-06-22:</strong> Talk and field visit at NTT Basic Research Laboratories, Atsugi, Kanagawa.</li>
      <li><strong>2023-06-07:</strong> Tokyo Tech Student Ambassador kick-off meeting.</li>
      <li><strong>2022-10-24:</strong> Poster presentation at Stanford University for CNC22.</li>
      <li><strong>2022-06-15:</strong> Paper published in Nature Communications Physics.</li>
    </ul>
  </div>

  <aside class="publication-rail" role="complementary" aria-label="Publication panels">
    <h2>Publications</h2>
    <div class="publication-rail-track">
      {% assign scholar_publications = site.data.google_scholar_publications | default: empty %}
      {% if scholar_publications and scholar_publications.size > 0 %}
        {% for publication in scholar_publications limit: 12 %}
          <article class="publication-panel">
            <p class="publication-panel-year">{{ publication.year }}</p>
            <h3>
              {% if publication.scholar_url and publication.scholar_url != "" %}
                <a href="{{ publication.scholar_url }}" target="_blank" rel="noopener">{{ publication.title }}</a>
              {% else %}
                {{ publication.title }}
              {% endif %}
            </h3>
            {% if publication.venue %}
              <p class="publication-panel-venue">{{ publication.venue }}</p>
            {% elsif publication.scholar_url and publication.scholar_url != "" %}
              <p class="publication-panel-venue">{{ publication.scholar_url }}</p>
            {% endif %}
            <p class="publication-panel-citations">Citations: {{ publication.citations | default: 0 }}</p>
          </article>
        {% endfor %}
      {% else %}
        <article class="publication-panel">
          <p class="publication-panel-year">--</p>
          <h3>Syncing publications from Google Scholar...</h3>
        </article>
      {% endif %}
    </div>
  </aside>
</div>

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const ticker = document.getElementById("news-ticker-content");
    const tickerShell = document.querySelector(".news-ticker");
    const entries = document.querySelectorAll(".news-list li");

    function syncTickerHeight() {
      if (!tickerShell) {
        return;
      }

      const tickerHeight = Math.ceil(tickerShell.getBoundingClientRect().height);
      document.documentElement.style.setProperty("--news-ticker-height", tickerHeight + "px");
    }

    if (!ticker || entries.length === 0) {
      syncTickerHeight();
      return;
    }

    const serialized = Array.from(entries).map(function (item) {
      return '<span class="news-ticker-item">' + item.innerHTML + "</span>";
    });

    const stream = serialized.join('<span class="news-ticker-separator" aria-hidden="true">•</span>');
    ticker.innerHTML = stream + '<span class="news-ticker-separator" aria-hidden="true">•</span>' + stream;

    syncTickerHeight();

    if (window.ResizeObserver && tickerShell) {
      const tickerObserver = new ResizeObserver(syncTickerHeight);
      tickerObserver.observe(tickerShell);
    }

    const revealTargets = document.querySelectorAll(
      ".about-hero-card, .about-hero-stat-card, .about-hero-action-btn, .news-list li, .publication-panel"
    );
    const spotlightHost = document.querySelector(".about-hero-card");
    const publicationPanels = document.querySelectorAll(".publication-panel");

    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    if (revealTargets.length > 0 && !prefersReducedMotion) {
      revealTargets.forEach(function (element) {
        element.classList.add("is-reveal");
      });

      if ("IntersectionObserver" in window) {
        const revealObserver = new IntersectionObserver(
          function (items) {
            items.forEach(function (entry) {
              if (!entry.isIntersecting) {
                return;
              }

              entry.target.classList.add("is-reveal-visible");
              revealObserver.unobserve(entry.target);
            });
          },
          {
            threshold: 0.15,
            rootMargin: "0px 0px -8% 0px"
          }
        );

        revealTargets.forEach(function (element) {
          revealObserver.observe(element);
        });
      } else {
        revealTargets.forEach(function (element) {
          element.classList.add("is-reveal-visible");
        });
      }
    }

    if (spotlightHost && !prefersReducedMotion) {
      spotlightHost.addEventListener("pointermove", function (event) {
        const bounds = spotlightHost.getBoundingClientRect();
        const x = ((event.clientX - bounds.left) / bounds.width) * 100;
        const y = ((event.clientY - bounds.top) / bounds.height) * 100;

        spotlightHost.style.setProperty("--hero-glow-x", x + "%");
        spotlightHost.style.setProperty("--hero-glow-y", y + "%");
      });
    }

    if (publicationPanels.length > 0 && !prefersReducedMotion) {
      publicationPanels.forEach(function (panel) {
        panel.addEventListener("pointermove", function (event) {
          const bounds = panel.getBoundingClientRect();
          const x = event.clientX - bounds.left;
          const y = event.clientY - bounds.top;
          panel.style.setProperty("--panel-spotlight", x + "px " + y + "px");
        });
      });
    }

    window.addEventListener("resize", syncTickerHeight);
  });
</script>
