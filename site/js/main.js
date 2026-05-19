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

  document.querySelectorAll(".retro-disclosure-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const panel = document.getElementById(btn.getAttribute("aria-controls"));
      const wrap = btn.closest(".retro-disclosure");
      if (!panel || !wrap) return;
      const open = btn.getAttribute("aria-expanded") === "true";
      const next = !open;
      btn.setAttribute("aria-expanded", String(next));
      panel.hidden = !next;
      wrap.classList.toggle("is-open", next);
      const icon = btn.querySelector(".retro-disclosure-icon");
      if (icon) icon.textContent = next ? "\u2212" : "+";
    });
  });

  const retroTableBody = document.querySelector(".retro-table tbody");
  const retroRows = document.querySelectorAll(".retro-table tbody tr[data-phase]");
  const retroPhaseFilters = document.querySelectorAll(".retro-filter--phase");
  const retroDateFilters = document.querySelectorAll(".retro-filter--date");
  const retroSortBtns = document.querySelectorAll(".retro-sort-btn");

  if (retroTableBody && retroRows.length) {
    let currentPhase = "all";
    let currentMonth = "all";
    let currentSort = "asc";

    function parseRowTime(row) {
      const text = row.cells[3]?.textContent.trim() || "";
      const match = text.match(/(\d{1,2})[:h](\d{2})/);
      if (!match) return 0;
      return parseInt(match[1], 10) * 60 + parseInt(match[2], 10);
    }

    function getRowDate(row) {
      if (row.dataset.sortDate) return row.dataset.sortDate;
      const parts = row.cells[1]?.textContent.trim().split("/");
      if (parts?.length !== 3) return "";
      const [d, m, y] = parts;
      return `${y}-${m.padStart(2, "0")}-${d.padStart(2, "0")}`;
    }

    retroRows.forEach((row) => {
      const iso = getRowDate(row);
      if (iso) {
        row.dataset.sortDate = iso;
        row.dataset.sortMonth = iso.slice(0, 7);
      }
    });

    function applyRetroTable() {
      retroRows.forEach((row) => {
        const phaseMatch = currentPhase === "all" || row.dataset.phase === currentPhase;
        const month = row.dataset.sortMonth || getRowDate(row).slice(0, 7);
        const dateMatch = currentMonth === "all" || month === currentMonth;
        row.classList.toggle("is-hidden", !(phaseMatch && dateMatch));
      });

      const visible = Array.from(retroRows).filter((row) => !row.classList.contains("is-hidden"));
      visible.sort((a, b) => {
        const dateCmp = getRowDate(a).localeCompare(getRowDate(b));
        if (dateCmp !== 0) return currentSort === "asc" ? dateCmp : -dateCmp;
        const timeCmp = parseRowTime(a) - parseRowTime(b);
        return currentSort === "asc" ? timeCmp : -timeCmp;
      });

      visible.forEach((row) => retroTableBody.appendChild(row));
      Array.from(retroRows)
        .filter((row) => row.classList.contains("is-hidden"))
        .forEach((row) => retroTableBody.appendChild(row));
    }

    retroPhaseFilters.forEach((btn) => {
      btn.addEventListener("click", () => {
        currentPhase = btn.dataset.filter;
        retroPhaseFilters.forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        applyRetroTable();
      });
    });

    retroDateFilters.forEach((btn) => {
      btn.addEventListener("click", () => {
        currentMonth = btn.dataset.dateFilter;
        retroDateFilters.forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        applyRetroTable();
      });
    });

    retroSortBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        currentSort = btn.dataset.sort;
        retroSortBtns.forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        applyRetroTable();
      });
    });

    applyRetroTable();
  }

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
