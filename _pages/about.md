---
permalink: /
title: "About"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<div class="news-ticker" role="region" aria-label="Live news ticker">
  <span class="news-ticker-label">Live News</span>
  <div class="news-ticker-track" aria-live="polite">
    <div class="news-ticker-content" id="news-ticker-content">Loading latest news…</div>
  </div>
</div>

<div class="about-hero-card" role="region" aria-label="About section introduction">
  <figure class="about-hero-media">
    <img src="/images/CR5_9271_Sudeera_size2.jpg" alt="Creative desk with monitor, microphone, and ambient lighting">
    <figcaption>My creative cockpit where ideas take flight ✈️</figcaption>
  </figure>

  <div class="about-hero-content">
    <img class="about-hero-avatar" src="/images/profile.png" alt="Portrait photo of Sudeera">

    <h1>Hi! I'm Sudeera <span aria-hidden="true">👋</span></h1>
    <p class="about-hero-tagline">AI researcher, quantum computing enthusiast, and HPC builder.</p>

    <p>
      I’m a doctoral candidate at the Institute of Science Tokyo, affiliated with NTT Physics and Informatics Laboratories.
      I explore how intelligent algorithms, quantum-inspired systems, and high-performance computing can solve hard optimization and scientific computing challenges.
    </p>

    <p>
      My current work focuses on AI for discovery, quantum and coherent Ising approaches, and scalable GPU-first simulation pipelines.
      This site is my knowledge hangar where I share papers, experiments, tools, and lessons from research in flight.
    </p>

    <a class="about-hero-cta" href="/contact/">Let’s Work Together</a>
  </div>
</div>

## News

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

<script>
  document.addEventListener("DOMContentLoaded", function () {
    const ticker = document.getElementById("news-ticker-content");
    const entries = document.querySelectorAll(".news-list li");

    if (!ticker || entries.length === 0) {
      return;
    }

    const serialized = Array.from(entries).map(function (item) {
      return '<span class="news-ticker-item">' + item.innerHTML + "</span>";
    });

    const stream = serialized.join('<span class="news-ticker-separator" aria-hidden="true">•</span>');
    ticker.innerHTML = stream + '<span class="news-ticker-separator" aria-hidden="true">•</span>' + stream;
  });
</script>
