/**
 * Service Worker for 365-Day Health Poster Studio (India)
 * Complete offline caching for all assets, fonts, JSON, and photo graphics.
 */

const CACHE_NAME = 'health-poster-v1.29';

const PRECACHE_ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './css/styles.css',
  './css/review.css',
  './css/fonts.css',
  './js/app.js',
  './js/canvas-renderer.js',
  './js/db.js',
  './js/calendar-data.js',
  './js/review-data.js',
  './js/review.js',
  './data/health_365.json',
  './data/annual_review_2026.json',
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
  './photos/apr11_motherhood_card1_anc.jpg',
  './photos/apr11_motherhood_card2_danger.jpg',
  './photos/apr11_motherhood_card3_plan.jpg',
  './photos/apr11_motherhood_card4_medicines.jpg',
  './photos/apr17_haemophilia_card1_centre.jpg',
  './photos/apr17_haemophilia_card2_joint.jpg',
  './photos/apr17_haemophilia_card3_medicine.jpg',
  './photos/apr17_haemophilia_card4_activity.jpg',
  './photos/aug20_mosquito_card1_dryday.jpg',
  './photos/aug20_mosquito_card2_cover.jpg',
  './photos/aug20_mosquito_card3_protection.jpg',
  './photos/aug20_mosquito_card4_fever.jpg',
  './photos/cphc_anc_care_card1.png',
  './photos/cphc_anc_care_card2.png',
  './photos/cphc_anc_care_card3.png',
  './photos/cphc_anc_care_card4.png',
  './photos/cphc_anemia_mukt_bharat_card1.png',
  './photos/cphc_anemia_mukt_bharat_card2.png',
  './photos/cphc_anemia_mukt_bharat_card3.png',
  './photos/cphc_anemia_mukt_bharat_card4.png',
  './photos/cphc_antibiotic_stewardship_card1.png',
  './photos/cphc_antibiotic_stewardship_card2.png',
  './photos/cphc_antibiotic_stewardship_card3.png',
  './photos/cphc_antibiotic_stewardship_card4.png',
  './photos/cphc_breast_cervical_cancer_card1.png',
  './photos/cphc_breast_cervical_cancer_card2.png',
  './photos/cphc_breast_cervical_cancer_card3.png',
  './photos/cphc_breast_cervical_cancer_card4.png',
  './photos/cphc_cardio_stroke_fast_card1.png',
  './photos/cphc_cardio_stroke_fast_card2.png',
  './photos/cphc_cardio_stroke_fast_card3.png',
  './photos/cphc_cardio_stroke_fast_card4.png',
  './photos/cphc_childhood_idcf_card1.png',
  './photos/cphc_childhood_idcf_card2.png',
  './photos/cphc_childhood_idcf_card3.png',
  './photos/cphc_childhood_idcf_card4.png',
  './photos/cphc_copd_asthma_card1.png',
  './photos/cphc_copd_asthma_card2.png',
  './photos/cphc_copd_asthma_card3.png',
  './photos/cphc_copd_asthma_card4.png',
  './photos/cphc_delivery_dakshata_card1.png',
  './photos/cphc_delivery_dakshata_card2.png',
  './photos/cphc_delivery_dakshata_card3.png',
  './photos/cphc_delivery_dakshata_card4.png',
  './photos/cphc_dementia_falls_epmns_card1.png',
  './photos/cphc_dementia_falls_epmns_card2.png',
  './photos/cphc_dementia_falls_epmns_card3.png',
  './photos/cphc_dementia_falls_epmns_card4.png',
  './photos/cphc_diabetes_care_card1.png',
  './photos/cphc_diabetes_care_card2.png',
  './photos/cphc_diabetes_care_card3.png',
  './photos/cphc_diabetes_care_card4.png',
  './photos/cphc_elderly_cga_epmns_card1.png',
  './photos/cphc_elderly_cga_epmns_card2.png',
  './photos/cphc_elderly_cga_epmns_card3.png',
  './photos/cphc_elderly_cga_epmns_card4.png',
  './photos/cphc_emergency_snakebite_card1.png',
  './photos/cphc_emergency_snakebite_card2.png',
  './photos/cphc_emergency_snakebite_card3.png',
  './photos/cphc_emergency_snakebite_card4.png',
  './photos/cphc_emergency_trauma_108_card1.png',
  './photos/cphc_emergency_trauma_108_card2.png',
  './photos/cphc_emergency_trauma_108_card3.png',
  './photos/cphc_emergency_trauma_108_card4.png',
  './photos/cphc_ent_care_oeee_card1.png',
  './photos/cphc_ent_care_oeee_card2.png',
  './photos/cphc_ent_care_oeee_card3.png',
  './photos/cphc_ent_care_oeee_card4.png',
  './photos/cphc_ert_balanced_thali_millets_card1.png',
  './photos/cphc_ert_balanced_thali_millets_card2.png',
  './photos/cphc_ert_balanced_thali_millets_card3.png',
  './photos/cphc_ert_balanced_thali_millets_card4.png',
  './photos/cphc_ert_less_salt_sugar_oil_card1.png',
  './photos/cphc_ert_less_salt_sugar_oil_card2.png',
  './photos/cphc_ert_less_salt_sugar_oil_card3.png',
  './photos/cphc_ert_less_salt_sugar_oil_card4.png',
  './photos/cphc_eye_care_oeee_card1.png',
  './photos/cphc_eye_care_oeee_card2.png',
  './photos/cphc_eye_care_oeee_card3.png',
  './photos/cphc_eye_care_oeee_card4.png',
  './photos/cphc_family_planning_card1.png',
  './photos/cphc_family_planning_card2.png',
  './photos/cphc_family_planning_card3.png',
  './photos/cphc_family_planning_card4.png',
  './photos/cphc_hbyc_childcare_card1.png',
  './photos/cphc_hbyc_childcare_card2.png',
  './photos/cphc_hbyc_childcare_card3.png',
  './photos/cphc_hbyc_childcare_card4.png',
  './photos/cphc_hepatitis_waterborne_card1.png',
  './photos/cphc_hepatitis_waterborne_card2.png',
  './photos/cphc_hepatitis_waterborne_card3.png',
  './photos/cphc_hepatitis_waterborne_card4.png',
  './photos/cphc_hypertension_ncd_card1.png',
  './photos/cphc_hypertension_ncd_card2.png',
  './photos/cphc_hypertension_ncd_card3.png',
  './photos/cphc_hypertension_ncd_card4.png',
  './photos/cphc_iycf_nutrition_card1.png',
  './photos/cphc_iycf_nutrition_card2.png',
  './photos/cphc_iycf_nutrition_card3.png',
  './photos/cphc_iycf_nutrition_card4.png',
  './photos/cphc_leprosy_nlep_card1.png',
  './photos/cphc_leprosy_nlep_card2.png',
  './photos/cphc_leprosy_nlep_card3.png',
  './photos/cphc_leprosy_nlep_card4.png',
  './photos/cphc_mental_telemanas_epmns_card1.png',
  './photos/cphc_mental_telemanas_epmns_card2.png',
  './photos/cphc_mental_telemanas_epmns_card3.png',
  './photos/cphc_mental_telemanas_epmns_card4.png',
  './photos/cphc_newborn_nssk_card1.png',
  './photos/cphc_newborn_nssk_card2.png',
  './photos/cphc_newborn_nssk_card3.png',
  './photos/cphc_newborn_nssk_card4.png',
  './photos/cphc_oral_cancer_ntcp_card1.png',
  './photos/cphc_oral_cancer_ntcp_card2.png',
  './photos/cphc_oral_cancer_ntcp_card3.png',
  './photos/cphc_oral_cancer_ntcp_card4.png',
  './photos/cphc_oral_dental_oeee_card1.png',
  './photos/cphc_oral_dental_oeee_card2.png',
  './photos/cphc_oral_dental_oeee_card3.png',
  './photos/cphc_oral_dental_oeee_card4.png',
  './photos/cphc_palliative_epmns_card1.png',
  './photos/cphc_palliative_epmns_card2.png',
  './photos/cphc_palliative_epmns_card3.png',
  './photos/cphc_palliative_epmns_card4.png',
  './photos/cphc_rbsk_screening_card1.png',
  './photos/cphc_rbsk_screening_card2.png',
  './photos/cphc_rbsk_screening_card3.png',
  './photos/cphc_rbsk_screening_card4.png',
  './photos/cphc_rksk_adolescent_card1.png',
  './photos/cphc_rksk_adolescent_card2.png',
  './photos/cphc_rksk_adolescent_card3.png',
  './photos/cphc_rksk_adolescent_card4.png',
  './photos/cphc_substance_audit_epmns_card1.png',
  './photos/cphc_substance_audit_epmns_card2.png',
  './photos/cphc_substance_audit_epmns_card3.png',
  './photos/cphc_substance_audit_epmns_card4.png',
  './photos/cphc_tb_elimination_card1.png',
  './photos/cphc_tb_elimination_card2.png',
  './photos/cphc_tb_elimination_card3.png',
  './photos/cphc_tb_elimination_card4.png',
  './photos/cphc_uip_vaccination_card1.png',
  './photos/cphc_uip_vaccination_card2.png',
  './photos/cphc_uip_vaccination_card3.png',
  './photos/cphc_uip_vaccination_card4.png',
  './photos/cphc_vector_malaria_dengue_card1.png',
  './photos/cphc_vector_malaria_dengue_card2.png',
  './photos/cphc_vector_malaria_dengue_card3.png',
  './photos/cphc_vector_malaria_dengue_card4.png',
  './photos/cphc_wash_infection_control_card1.png',
  './photos/cphc_wash_infection_control_card2.png',
  './photos/cphc_wash_infection_control_card3.png',
  './photos/cphc_wash_infection_control_card4.png',
  './photos/mar16_vaccination_card1_schedule.jpg',
  './photos/mar16_vaccination_card2_card.jpg',
  './photos/mar16_vaccination_card3_followup.jpg',
  './photos/mar16_vaccination_card4_observation.jpg',
  './photos/may25_thyroid_card1_symptoms.jpg',
  './photos/may25_thyroid_card2_test.jpg',
  './photos/may25_thyroid_card3_medicine.jpg',
  './photos/may25_thyroid_card4_iodine.jpg',
  './photos/may28_menstrual_card1_change.jpg',
  './photos/may28_menstrual_card2_hygiene.jpg',
  './photos/may28_menstrual_card3_reusable.jpg',
  './photos/may28_menstrual_card4_consult.jpg',
  './photos/oct15_do1.png',
  './photos/oct15_do2.png',
  './photos/oct15_dont1.png',
  './photos/oct15_dont2.png',
  './photos/oct16_do1.png',
  './photos/oct16_do2.png',
  './photos/oct16_dont1.png',
  './photos/oct16_dont2.png',
  './photos/oct17_do1.png',
  './photos/oct17_do2.png',
  './photos/oct17_dont1.png',
  './photos/oct17_dont2.png',
  './photos/oct18_do1.png',
  './photos/oct18_do2.png',
  './photos/oct18_dont1.png',
  './photos/oct18_dont2.png',
  './photos/oct19_ear_card1.png',
  './photos/oct19_ear_card3.png',
  './photos/oct19_oral_card1.png',
  './photos/oct19_oral_card3.png',
  './photos/oct20_do1.png',
  './photos/oct20_do2.png',
  './photos/oct20_dont1.png',
  './photos/oct20_dont2.png',
  './photos/oct21_do1.png',
  './photos/oct21_do2.png',
  './photos/oct21_dont1.png',
  './photos/oct21_dont2.png',
  './photos/oct22_stuttering_card1_listen.jpg',
  './photos/oct22_stuttering_card2_respect.jpg',
  './photos/oct22_stuttering_card3_slp.jpg',
  './photos/oct22_stuttering_card4_inclusion.jpg',
  './photos/oct24_polio_card1_drops.jpg',
  './photos/oct24_polio_card2_routine.jpg',
  './photos/oct24_polio_card3_booth.jpg',
  './photos/oct24_polio_card4_weakness.jpg',
  './photos/oct29_stroke_card1_fast.jpg',
  './photos/oct29_stroke_card2_ambulance.jpg',
  './photos/oct29_stroke_card3_nofood.jpg',
  './photos/oct29_stroke_card4_prevention.jpg',
  './photos/sep21_alzheimer_card1_assessment.jpg',
  './photos/sep21_alzheimer_card2_communication.jpg',
  './photos/sep21_alzheimer_card3_safety.jpg',
  './photos/sep21_alzheimer_card4_caregiver.jpg'
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

// A host may redirect index.html to the directory root during precaching.
// Navigation requests cannot consume a cached response marked redirected.
function navigationResponse(response) {
  if (!response || !response.redirected) return response;
  const headers = new Headers(response.headers);
  headers.delete('content-encoding');
  headers.delete('content-length');
  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers
  });
}

// Cache-First strategy with background network fallback & caching
self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      if (cachedResponse) {
        return event.request.mode === 'navigate' ? navigationResponse(cachedResponse) : cachedResponse;
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
          return caches.match('./index.html').then((response) => {
            if (response) return navigationResponse(response);
            return caches.match('./').then((root) => root ? navigationResponse(root) :
              new Response('Offline files are unavailable. Connect to the internet and reopen the app.', {
                status: 503, headers: { 'Content-Type': 'text/plain; charset=utf-8' }
              }));
          });
        }
      });
    })
  );
});
