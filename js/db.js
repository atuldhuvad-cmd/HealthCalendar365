/**
 * IndexedDB & Local Storage Manager for 365-Day Health Poster Studio
 * Persists custom swapped photos and doctor branding offline.
 */

const DB_NAME = 'HealthPosterStudioDB';
const DB_VERSION = 1;
const STORE_PHOTOS = 'custom_photos';
const STORE_SETTINGS = 'app_settings';

class StorageManager {
  constructor() {
    this.db = null;
    this.initPromise = this.init();
  }

  async init() {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open(DB_NAME, DB_VERSION);

      request.onupgradeneeded = (event) => {
        const db = event.target.result;
        if (!db.objectStoreNames.contains(STORE_PHOTOS)) {
          db.createObjectStore(STORE_PHOTOS, { keyPath: 'key' });
        }
        if (!db.objectStoreNames.contains(STORE_SETTINGS)) {
          db.createObjectStore(STORE_SETTINGS, { keyPath: 'id' });
        }
      };

      request.onsuccess = (event) => {
        this.db = event.target.result;
        resolve(this.db);
      };

      request.onerror = (event) => {
        console.error('IndexedDB error:', event.target.error);
        resolve(null); // Fallback gracefully to localStorage
      };
    });
  }

  // Save custom uploaded photo for a specific day and card slot
  async savePhoto(dayId, cardIndex, dataUrl) {
    await this.initPromise;
    const key = `${dayId}_card_${cardIndex}`;
    
    if (this.db) {
      return new Promise((resolve, reject) => {
        const tx = this.db.transaction(STORE_PHOTOS, 'readwrite');
        const store = tx.objectStore(STORE_PHOTOS);
        store.put({ key, dataUrl, timestamp: Date.now() });
        tx.oncomplete = () => resolve(true);
        tx.onerror = () => resolve(false);
      });
    } else {
      try {
        localStorage.setItem(`photo_${key}`, dataUrl);
        return true;
      } catch (e) {
        console.warn('LocalStorage quota exceeded for photo:', e);
        return false;
      }
    }
  }

  // Get custom photo if user has uploaded one
  async getPhoto(dayId, cardIndex) {
    await this.initPromise;
    const key = `${dayId}_card_${cardIndex}`;

    if (this.db) {
      return new Promise((resolve) => {
        const tx = this.db.transaction(STORE_PHOTOS, 'readonly');
        const store = tx.objectStore(STORE_PHOTOS);
        const req = store.get(key);
        req.onsuccess = () => {
          resolve(req.result ? req.result.dataUrl : null);
        };
        req.onerror = () => resolve(null);
      });
    } else {
      return localStorage.getItem(`photo_${key}`) || null;
    }
  }

  // Remove custom photo (reset to default illustration)
  async removePhoto(dayId, cardIndex) {
    await this.initPromise;
    const key = `${dayId}_card_${cardIndex}`;

    if (this.db) {
      return new Promise((resolve) => {
        const tx = this.db.transaction(STORE_PHOTOS, 'readwrite');
        const store = tx.objectStore(STORE_PHOTOS);
        store.delete(key);
        tx.oncomplete = () => resolve(true);
        tx.onerror = () => resolve(false);
      });
    } else {
      localStorage.removeItem(`photo_${key}`);
      return true;
    }
  }

  // Get Doctor Branding Settings
  async getSettings() {
    await this.initPromise;
    const defaultSettings = {
      useDoctorBranding: false,
      doctorName: 'Dr. Rajesh Patel',
      doctorDegree: 'M.B.B.S., M.D. (Internal Medicine)',
      clinicName: 'Patel Hospital & Wellness Clinic',
      contactInfo: '+91 98765 43210 • info@drpatelclinic.org',
      city: 'Ahmedabad, Gujarat'
    };

    try {
      const saved = localStorage.getItem('doctor_branding_settings');
      if (saved) {
        return { ...defaultSettings, ...JSON.parse(saved) };
      }
    } catch (e) {
      console.error(e);
    }
    return defaultSettings;
  }

  // Save Doctor Branding Settings
  async saveSettings(settings) {
    try {
      localStorage.setItem('doctor_branding_settings', JSON.stringify(settings));
      return true;
    } catch (e) {
      console.error(e);
      return false;
    }
  }
}

window.appStorage = new StorageManager();
