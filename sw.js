/* ultimate-css service worker
   Cache-first for CSS/JS/icons (the shell), network-first for HTML lessons
   so that edits to a lesson show up immediately when online.
*/
const VERSION = "v1";
const SHELL_CACHE = `ultimate-css-shell-${VERSION}`;
const PAGE_CACHE  = `ultimate-css-pages-${VERSION}`;

const SHELL_ASSETS = [
  "./",
  "./index.html",
  "./manifest.webmanifest",
  "./assets/css/main.css",
  "./assets/css/reset.css",
  "./assets/css/tokens.css",
  "./assets/css/base.css",
  "./assets/css/layout.css",
  "./assets/css/components.css",
  "./assets/css/animations.css",
  "./assets/js/editor.js",
  "./assets/icons/icon.svg",
  "./assets/icons/icon-192.png",
  "./assets/icons/icon-512.png",
  "./assets/icons/apple-touch-icon.png",
  "./assets/icons/favicon-32.png"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(SHELL_CACHE).then((cache) => cache.addAll(SHELL_ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys
          .filter((k) => k !== SHELL_CACHE && k !== PAGE_CACHE)
          .map((k) => caches.delete(k))
      )
    ).then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  if (req.method !== "GET") return;

  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  const accept = req.headers.get("accept") || "";
  const isHTML = req.mode === "navigate" || accept.includes("text/html");

  if (isHTML) {
    // Network-first for HTML, fall back to cache.
    event.respondWith(
      fetch(req)
        .then((res) => {
          const copy = res.clone();
          caches.open(PAGE_CACHE).then((cache) => cache.put(req, copy));
          return res;
        })
        .catch(() =>
          caches.match(req).then((cached) => cached || caches.match("./index.html"))
        )
    );
    return;
  }

  // Cache-first for everything else (CSS, JS, icons).
  event.respondWith(
    caches.match(req).then((cached) => {
      if (cached) return cached;
      return fetch(req).then((res) => {
        const copy = res.clone();
        caches.open(SHELL_CACHE).then((cache) => cache.put(req, copy));
        return res;
      });
    })
  );
});
