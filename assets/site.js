// Paddle buttons for the screenshot gallery. Scrolling by touch, trackpad
// and keyboard works without this; it only adds the prev/next controls.
document.querySelectorAll("[data-gallery]").forEach((gallery) => {
  const track = gallery.querySelector(".gallery-track");
  const prev = gallery.querySelector("[data-prev]");
  const next = gallery.querySelector("[data-next]");
  const step = () => track.clientWidth * 0.8;

  const update = () => {
    prev.disabled = track.scrollLeft <= 4;
    next.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - 4;
  };

  prev.addEventListener("click", () => track.scrollBy({ left: -step(), behavior: "smooth" }));
  next.addEventListener("click", () => track.scrollBy({ left: step(), behavior: "smooth" }));
  track.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", update);
  update();
});

// Light/Dark switch for galleries that have a dark-mode screenshot set.
document.querySelectorAll("[data-appearance]").forEach((button) => {
  button.addEventListener("click", () => {
    const gallery = button.closest("[data-gallery]");
    const mode = button.dataset.appearance;
    gallery.querySelectorAll("[data-appearance]").forEach((b) => {
      b.setAttribute("aria-pressed", String(b === button));
    });
    gallery.querySelectorAll("img[data-dark]").forEach((img) => {
      img.src = img.dataset[mode];
    });
  });
});
