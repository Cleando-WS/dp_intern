// dp_intern/sw.js
const SW_VERSION = '01'; // bei Änderungen hochzählen

self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', (e) => e.waitUntil(self.clients.claim()));

// Keine Offline-Caches nötig – Requests durchreichen
self.addEventListener('fetch', () => {});
