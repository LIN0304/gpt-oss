self.addEventListener('install', (event) => {
  event.waitUntil(caches.open('edgesage').then((cache) => cache.add('/')));
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => cached || fetch(event.request))
  );
});
