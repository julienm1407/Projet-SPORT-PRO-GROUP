(function () {
  const header = document.querySelector(".site-header");
  const navQuickLinks = document.querySelectorAll(".nav-quick a");
  const scrollCue = document.getElementById("scroll-cue");
  const sections = document.querySelectorAll("section[id]");

  const platformTabs = document.querySelectorAll(".platform-tab");
  const platformPanels = document.querySelectorAll(".platform-panel");
  const lightbox = document.getElementById("lightbox");
  const lightboxImg = document.getElementById("lightbox-img");
  const lightboxCaption = document.getElementById("lightbox-caption");
  const lightboxClose = document.querySelector(".lightbox-close");

  window.addEventListener("scroll", () => {
    header?.classList.toggle("scrolled", window.scrollY > 40);
    scrollCue?.classList.toggle("hidden", window.scrollY > 120);

    let current = "";
    sections.forEach((section) => {
      const top = section.offsetTop - 120;
      if (window.scrollY >= top) current = section.id;
    });
    navQuickLinks.forEach((link) => {
      link.classList.toggle("active", link.getAttribute("href") === "#" + current);
    });
  });

  platformTabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      const target = tab.dataset.platform;
      platformTabs.forEach((t) => t.classList.remove("active"));
      platformPanels.forEach((p) => p.classList.remove("active"));
      tab.classList.add("active");
      document.getElementById("panel-" + target)?.classList.add("active");
    });
  });

  document.querySelectorAll("[data-lightbox]").forEach((el) => {
    el.addEventListener("click", () => {
      const img = el.querySelector("img") || el;
      const src = img.dataset.full || img.src;
      const caption = el.dataset.caption || img.alt || "";
      lightboxImg.src = src;
      lightboxCaption.textContent = caption;
      lightbox.classList.add("open");
      document.body.style.overflow = "hidden";
    });
  });

  function closeLightbox() {
    lightbox.classList.remove("open");
    lightboxImg.src = "";
    document.body.style.overflow = "";
  }

  lightboxClose?.addEventListener("click", closeLightbox);
  lightbox?.addEventListener("click", (e) => {
    if (e.target === lightbox) closeLightbox();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeLightbox();
  });

  const retroFilters = document.querySelectorAll(".retro-filter");
  const retroRows = document.querySelectorAll(".retro-table tbody tr[data-phase]");

  retroFilters.forEach((btn) => {
    btn.addEventListener("click", () => {
      const phase = btn.dataset.filter;
      retroFilters.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      retroRows.forEach((row) => {
        const match = phase === "all" || row.dataset.phase === phase;
        row.classList.toggle("is-hidden", !match);
      });
    });
  });

  const kpiDashboard = document.getElementById("kpi-dashboard");
  if (kpiDashboard && "IntersectionObserver" in window) {
    const kpiObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            kpiDashboard.classList.add("is-visible");
            kpiObserver.unobserve(kpiDashboard);
          }
        });
      },
      { threshold: 0.2 }
    );
    kpiObserver.observe(kpiDashboard);
  } else if (kpiDashboard) {
    kpiDashboard.classList.add("is-visible");
  }
})();
