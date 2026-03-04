(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {
    var root = document.documentElement;
    var body = document.body;
    var prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    if (!prefersReducedMotion) {
      document.addEventListener(
        "pointermove",
        function (event) {
          root.style.setProperty("--cursor-x", event.clientX + "px");
          root.style.setProperty("--cursor-y", event.clientY + "px");
        },
        { passive: true }
      );

      var techCards = document.querySelectorAll(
        ".about-hero-card, .about-hero-stat-card, .publication-panel, .archive__item"
      );

      techCards.forEach(function (card) {
        card.classList.add("fx-tilt-ready");

        card.addEventListener("pointermove", function (event) {
          var rect = card.getBoundingClientRect();
          var localX = event.clientX - rect.left;
          var localY = event.clientY - rect.top;
          var rotateX = ((localY / rect.height) - 0.5) * -7;
          var rotateY = ((localX / rect.width) - 0.5) * 7;

          card.style.setProperty("--tilt-rotate-x", rotateX.toFixed(2) + "deg");
          card.style.setProperty("--tilt-rotate-y", rotateY.toFixed(2) + "deg");
          card.style.setProperty("--tilt-glow-x", localX.toFixed(0) + "px");
          card.style.setProperty("--tilt-glow-y", localY.toFixed(0) + "px");
        });

        card.addEventListener("pointerleave", function () {
          card.style.removeProperty("--tilt-rotate-x");
          card.style.removeProperty("--tilt-rotate-y");
        });
      });
    }

    var sections = document.querySelectorAll(".page__content h2, .page__content h3");
    sections.forEach(function (heading) {
      if (heading.querySelector(".heading-accent")) {
        return;
      }

      var accent = document.createElement("span");
      accent.className = "heading-accent";
      accent.setAttribute("aria-hidden", "true");
      heading.appendChild(accent);
    });

    if (body) {
      body.classList.add("fx-ready");
    }
  });
})();
