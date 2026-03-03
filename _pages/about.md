---
permalink: /
title: "About"
author_profile: true
show_title: false
redirect_from:
  - /about/
  - /about.html
---

<div class="home-architecture" role="region" aria-label="Homepage architecture">
  <div class="home-architecture-top">
    <section class="home-card home-card-about" aria-labelledby="home-about-title">
      <h2 id="home-about-title">About</h2>
      <p>
        I’m Sudeera, a doctoral researcher at the Institute of Science Tokyo working across AI,
        quantum-inspired optimization, and scalable HPC systems.
      </p>
      <p>
        This website shares my research journey, publications, talks, and experiments.
      </p>
      <a class="home-card-cta" href="/about/">Read More</a>
    </section>

    <aside class="home-card home-card-publications" aria-labelledby="home-publications-title">
      <h2 id="home-publications-title">Publications</h2>
      <div class="home-publications-track">
        {% assign publication_posts = site.publications | sort: "date" | reverse %}
        {% for post in publication_posts limit: 10 %}
          <article class="home-publication-item">
            <p class="home-publication-year">{{ post.date | date: "%Y" }}</p>
            <h3><a href="{{ post.url | relative_url }}">{{ post.title | strip }}</a></h3>
          </article>
        {% endfor %}
      </div>
      <a class="home-card-cta" href="/publications/">View All</a>
    </aside>
  </div>

  <section class="home-card home-card-news" aria-labelledby="home-news-title">
    <h2 id="home-news-title">News</h2>
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
      </ul>
    </div>
    <a class="home-card-cta" href="/year-archive/">All Posts</a>
  </section>
</div>
