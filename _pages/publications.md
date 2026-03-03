---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% assign scholar_publications = site.data.google_scholar_publications | default: empty %}

{% if author.googlescholar %}
You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% if scholar_publications and scholar_publications.size > 0 %}
  {% for publication in scholar_publications %}
  <article class="archive__item" itemscope itemtype="http://schema.org/CreativeWork">
    <h2 class="archive__item-title" itemprop="headline">
      {% if publication.scholar_url and publication.scholar_url != "" %}
      <a href="{{ publication.scholar_url }}" target="_blank" rel="noopener">{{ publication.title }}</a>
      {% else %}
      {{ publication.title }}
      {% endif %}
    </h2>

    {% if publication.authors %}
    <p>{{ publication.authors }}</p>
    {% endif %}

    {% if publication.venue or publication.year %}
    <p>
      {% if publication.venue %}{{ publication.venue }}{% endif %}
      {% if publication.venue and publication.year %}, {% endif %}
      {% if publication.year %}{{ publication.year }}{% endif %}
    </p>
    {% endif %}
  </article>
  {% endfor %}
{% else %}
  <p>Publication data is being synced from Google Scholar. Please check back soon.</p>
{% endif %}
