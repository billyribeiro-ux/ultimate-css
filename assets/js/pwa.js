/* ultimate-css — PWA registration.
   Each HTML page loads this script via its correct relative path
   (../assets/js/pwa.js, ../../assets/js/pwa.js, etc.). We resolve the
   service worker URL and scope relative to this script's own location,
   so the root sw.js controls every page regardless of nesting depth.
*/
(() => {
  if (!("serviceWorker" in navigator)) return;

  // document.currentScript is reliable during synchronous top-level execution.
  const scriptEl = document.currentScript;
  if (!scriptEl) return;

  // Script sits at <root>/assets/js/pwa.js — the site root is two levels up.
  const scriptUrl = new URL(scriptEl.src, window.location.href);
  const rootUrl = new URL("../../", scriptUrl);
  const swUrl = new URL("sw.js", rootUrl).href;
  const scope = rootUrl.pathname;

  window.addEventListener("load", () => {
    navigator.serviceWorker.register(swUrl, { scope }).catch(() => {
      /* Registration failures are non-fatal — the course still works. */
    });
  });

  // Surface Chrome/Edge's install prompt via an explicit button when the
  // browser offers it. Safari on macOS uses File → Add to Dock instead.
  let deferredPrompt = null;
  window.addEventListener("beforeinstallprompt", (e) => {
    e.preventDefault();
    deferredPrompt = e;
    const btn = document.querySelector("[data-install-app]");
    if (!btn) return;
    btn.hidden = false;
    btn.addEventListener("click", async () => {
      if (!deferredPrompt) return;
      deferredPrompt.prompt();
      await deferredPrompt.userChoice;
      deferredPrompt = null;
      btn.hidden = true;
    }, { once: true });
  });

  window.addEventListener("appinstalled", () => {
    const btn = document.querySelector("[data-install-app]");
    if (btn) btn.hidden = true;
  });
})();
