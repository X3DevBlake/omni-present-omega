const CACHE_NAME = 'opo-cache-v1';
const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/godseye.html',
  '/architecture.html',
  '/crdt-lab.html',
  '/gemini-studio.html',
  '/sentient-radar.html',
  '/whitepaper.html',
  '/deploy.html',
  '/learn.html',
  '/deeptech-fusion.html',
  '/deeptech-quantum.html',
  '/deeptech-battery.html',
  '/deeptech-genomic.html',
  '/deeptech-neural.html',
  '/deeptech-robotics.html',
  '/css/liquid-glass.css',
  '/js/app.js',
  '/js/godseye-engine.js',
  '/js/neural-brain.js',
  '/js/web3-staking.js',
  '/js/kronos-terminal.js',
  '/manifest.json',
  '/svg/opo-symbol.svg',
  '/svg/godseye-spatial.svg',
  '/svg/gemini-sparkle.svg',
  '/svg/gemini-argon-3d.svg',
  '/svg/swarm-intelligence.svg',
  '/svg/sentient-radar.svg',
  '/svg/crdt-lattice.svg',
  '/svg/scion-routing.svg'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(STATIC_ASSETS);
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  // Only handle GET requests
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);

  // Ignore API calls to localhost daemons
  if (url.port === '8001' || url.port === '9001') return;

  event.respondWith(
    fetch(event.request)
      .then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200) {
          const clone = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
        }
        return networkResponse;
      })
      .catch(() => {
        return caches.match(event.request).then((cachedResponse) => {
          if (cachedResponse) return cachedResponse;
          if (event.request.headers.get('accept')?.includes('text/html')) {
            return caches.match('/index.html');
          }
        });
      })
  );
});
