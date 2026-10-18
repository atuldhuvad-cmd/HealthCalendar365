/**
 * Service Worker for 365-Day Health Poster Studio (India)
 * Complete offline caching for all assets, fonts, JSON, and photo graphics.
 */

const CACHE_NAME = 'health-poster-v1.6';

const PRECACHE_ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './css/styles.css',
  './css/fonts.css',
  './js/app.js',
  './js/canvas-renderer.js',
  './js/db.js',
  './js/calendar-data.js',
  './data/health_365.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './fonts/noto_sans_gujarati_400_gujarati_12e87d67.woff2',
  './fonts/noto_sans_gujarati_400_latin_824de553.woff2',
  './fonts/noto_sans_gujarati_400_latinext_ba716cb8.woff2',
  './fonts/noto_sans_gujarati_400_math_147dbab2.woff2',
  './fonts/noto_sans_gujarati_400_symbols_bcb77dc5.woff2',
  './fonts/noto_sans_gujarati_600_gujarati_12e87d67.woff2',
  './fonts/noto_sans_gujarati_600_latin_824de553.woff2',
  './fonts/noto_sans_gujarati_600_latinext_ba716cb8.woff2',
  './fonts/noto_sans_gujarati_600_math_147dbab2.woff2',
  './fonts/noto_sans_gujarati_600_symbols_bcb77dc5.woff2',
  './fonts/noto_sans_gujarati_700_gujarati_12e87d67.woff2',
  './fonts/noto_sans_gujarati_700_latin_824de553.woff2',
  './fonts/noto_sans_gujarati_700_latinext_ba716cb8.woff2',
  './fonts/noto_sans_gujarati_700_math_147dbab2.woff2',
  './fonts/noto_sans_gujarati_700_symbols_bcb77dc5.woff2',
  './fonts/noto_sans_gujarati_800_cyrillicext_12e87d67.woff2',
  './fonts/noto_sans_gujarati_800_latin_824de553.woff2',
  './fonts/noto_sans_gujarati_800_latinext_ba716cb8.woff2',
  './fonts/noto_sans_gujarati_800_math_147dbab2.woff2',
  './fonts/noto_sans_gujarati_800_symbols_bcb77dc5.woff2',
  './fonts/plus_jakarta_sans_400_cyrillicext_fdb05bf0.woff2',
  './fonts/plus_jakarta_sans_400_latin_9f6257e3.woff2',
  './fonts/plus_jakarta_sans_400_latinext_fdf1d5c3.woff2',
  './fonts/plus_jakarta_sans_400_vietnamese_fccbe4fa.woff2',
  './fonts/plus_jakarta_sans_500_cyrillicext_fdb05bf0.woff2',
  './fonts/plus_jakarta_sans_500_latin_9f6257e3.woff2',
  './fonts/plus_jakarta_sans_500_latinext_fdf1d5c3.woff2',
  './fonts/plus_jakarta_sans_500_vietnamese_fccbe4fa.woff2',
  './fonts/plus_jakarta_sans_600_cyrillicext_fdb05bf0.woff2',
  './fonts/plus_jakarta_sans_600_latin_9f6257e3.woff2',
  './fonts/plus_jakarta_sans_600_latinext_fdf1d5c3.woff2',
  './fonts/plus_jakarta_sans_600_vietnamese_fccbe4fa.woff2',
  './fonts/plus_jakarta_sans_700_cyrillicext_fdb05bf0.woff2',
  './fonts/plus_jakarta_sans_700_latin_9f6257e3.woff2',
  './fonts/plus_jakarta_sans_700_latinext_fdf1d5c3.woff2',
  './fonts/plus_jakarta_sans_700_vietnamese_fccbe4fa.woff2',
  './fonts/plus_jakarta_sans_800_all_fdb05bf0.woff2',
  './fonts/plus_jakarta_sans_800_latin_9f6257e3.woff2',
  './fonts/plus_jakarta_sans_800_latinext_fdf1d5c3.woff2',
  './fonts/plus_jakarta_sans_800_vietnamese_fccbe4fa.woff2',
  './photos/cat_cardio.png',
  './photos/cat_infection.png',
  './photos/cat_mental.png',
  './photos/cat_nutrition.png',
  './photos/cat_yoga.png',
  './photos/oct15_cane_card1.png',
  './photos/oct15_cane_card2.png',
  './photos/oct15_cane_card3.png',
  './photos/oct15_cane_card4.png',
  './photos/oct15_card1_soap.png',
  './photos/oct15_card2_scrub.png',
  './photos/oct15_card3_keymoments.png',
  './photos/oct15_card4_dry.png',
  './photos/oct16_food_card1.png',
  './photos/oct16_food_card2.png',
  './photos/oct16_food_card3.png',
  './photos/oct16_food_card4.png',
  './photos/oct16_spine_card1.png',
  './photos/oct16_spine_card2.png',
  './photos/oct16_spine_card3.png',
  './photos/oct16_spine_card4.png',
  './photos/oct17_do1.png',
  './photos/oct17_do2.png',
  './photos/oct17_dont1.png',
  './photos/oct17_dont2.png',
  './photos/oct18_do1.png',
  './photos/oct18_do2.png',
  './photos/oct18_dont1.png',
  './photos/oct18_dont2.png',
  './photos/oct19_ear_card1.png',
  './photos/oct19_ear_card2.png',
  './photos/oct19_ear_card3.png',
  './photos/oct19_ear_card4.png',
  './photos/oct19_oral_card1.png',
  './photos/oct19_oral_card2.png',
  './photos/oct19_oral_card3.png',
  './photos/oct19_oral_card4.png',
  './photos/oct20_do1.png',
  './photos/oct20_do2.png',
  './photos/oct20_dont1.png',
  './photos/oct20_dont2.png',
  './photos/oct21_do1.png',
  './photos/oct21_do2.png',
  './photos/oct21_dont1.png',
  './photos/oct21_dont2.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      console.log('[ServiceWorker] Precaching offline assets...');
      return cache.addAll(PRECACHE_ASSETS);
    }).then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key.startsWith('health-poster-') && key !== CACHE_NAME) {
            console.log('[ServiceWorker] Removing stale health poster cache:', key);
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Cache-First strategy with background network fallback & caching
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        return cachedResponse;
      }

      return fetch(event.request).then((networkResponse) => {
        if (!networkResponse || networkResponse.status !== 200 || networkResponse.type !== 'basic') {
          return networkResponse;
        }

        const responseToCache = networkResponse.clone();
        caches.open(CACHE_NAME).then((cache) => {
          cache.put(event.request, responseToCache);
        });

        return networkResponse;
      }).catch(() => {
        // Fallback for navigation requests if offline
        if (event.request.mode === 'navigate') {
          return caches.match('./index.html');
        }
      });
    })
  );
});
