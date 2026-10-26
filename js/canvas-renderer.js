/**
 * High-DPI HTML5 Canvas Rendering Engine for 365-Day Health Poster Studio
 * Modern Indian Clinical Editorial Style
 * 
 * Features:
 * - Square 1080x1080 (WhatsApp post / Instagram feed)
 * - Vertical 1080x1920 (WhatsApp Status / Instagram Story)
 * - Dynamic Header: Smooth date pill, WHO / MoHFW Observance badge, bilingual title
 * - Modern 4-Card Visual Grid: Independent 4:3 high-res photos, subtle `#284454` clinical border,
 *   soft shadow, distinct Action Badges (માર્ગદર્શન #૧, #૨, #૩, #૪), bilingual headers & captions
 * - Bottom Footer Bar: Dynamic Public Interest notice or Custom Doctor Branding box
 */

// Per-image framing for the wide square photo boxes. y: vertical focus of the cover crop (0 = top, 0.5 = centre, 1 = bottom).
// fit:'contain' shows the whole image (aspect kept); align:'right' keeps the left dark bar wide enough to hold the ACTION badge.
// badge: corner for the ACTION badge ('tl' default, 'tr', 'bl', 'br') to keep it off faces and key objects.
// Only the images listed here change; every other photo keeps the centred crop. Source images are never modified,
// and user-swapped photos are never affected. Aspect ratio is always preserved.
const PHOTO_FOCUS = {
  'cphc_anc_care_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_anc_care_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_anc_care_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'br'},
  'cphc_anc_care_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_anemia_mukt_bharat_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_anemia_mukt_bharat_card2.png': {'y': 0.5, 'verticalBadge': 'tl'},
  'cphc_anemia_mukt_bharat_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_anemia_mukt_bharat_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_antibiotic_stewardship_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_antibiotic_stewardship_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_antibiotic_stewardship_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_antibiotic_stewardship_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_breast_cervical_cancer_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_breast_cervical_cancer_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_breast_cervical_cancer_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_breast_cervical_cancer_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_cardio_stroke_fast_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_cardio_stroke_fast_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_cardio_stroke_fast_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_cardio_stroke_fast_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'br'},
  'cphc_childhood_idcf_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_childhood_idcf_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_childhood_idcf_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_childhood_idcf_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_copd_asthma_card1.png': {'y': 0, 'badge': 'bl', 'verticalBadge': 'bl'},
  'cphc_copd_asthma_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_copd_asthma_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_copd_asthma_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_delivery_dakshata_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_delivery_dakshata_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_delivery_dakshata_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_delivery_dakshata_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_dementia_falls_epmns_card1.png': {'y': 0.5, 'verticalBadge': 'tr'},
  'cphc_dementia_falls_epmns_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_dementia_falls_epmns_card3.png': {'y': 0.5, 'verticalBadge': 'tl'},
  'cphc_dementia_falls_epmns_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_diabetes_care_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_diabetes_care_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_diabetes_care_card3.png': {'y': 0.5, 'verticalBadge': 'tr'},
  'cphc_diabetes_care_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_elderly_cga_epmns_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_elderly_cga_epmns_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_elderly_cga_epmns_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_elderly_cga_epmns_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_emergency_snakebite_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_emergency_snakebite_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_emergency_snakebite_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'br'},
  'cphc_emergency_snakebite_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_emergency_trauma_108_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_emergency_trauma_108_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_emergency_trauma_108_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_emergency_trauma_108_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_ent_care_oeee_card1.png': {'y': 0, 'badge': 'bl', 'verticalBadge': 'tr'},
  'cphc_ent_care_oeee_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_ent_care_oeee_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_ent_care_oeee_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_ert_balanced_thali_millets_card1.png': {'y': 0.5, 'verticalBadge': 'tr'},
  'cphc_ert_balanced_thali_millets_card2.png': {'y': 0.5, 'verticalBadge': 'tl'},
  'cphc_ert_balanced_thali_millets_card3.png': {'y': 0.5, 'verticalBadge': 'tl'},
  'cphc_ert_balanced_thali_millets_card4.png': {'y': 0.5, 'verticalBadge': 'tr'},
  'cphc_ert_less_salt_sugar_oil_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_ert_less_salt_sugar_oil_card2.png': {'y': 0.5, 'verticalBadge': 'tl'},
  'cphc_ert_less_salt_sugar_oil_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_ert_less_salt_sugar_oil_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_eye_care_oeee_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_eye_care_oeee_card2.png': {'y': 0, 'badge': 'bl', 'verticalBadge': 'bl'},
  'cphc_eye_care_oeee_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_eye_care_oeee_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_family_planning_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_family_planning_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_family_planning_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_family_planning_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_hbyc_childcare_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_hbyc_childcare_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_hbyc_childcare_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_hbyc_childcare_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_hepatitis_waterborne_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_hepatitis_waterborne_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_hepatitis_waterborne_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'br'},
  'cphc_hepatitis_waterborne_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_hypertension_ncd_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_hypertension_ncd_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_hypertension_ncd_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_hypertension_ncd_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_iycf_nutrition_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'br'},
  'cphc_iycf_nutrition_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_iycf_nutrition_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_iycf_nutrition_card4.png': {'y': 0.5, 'verticalBadge': 'tr'},
  'cphc_leprosy_nlep_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_leprosy_nlep_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_leprosy_nlep_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_leprosy_nlep_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_mental_telemanas_epmns_card1.png': {'y': 0, 'badge': 'bl', 'verticalBadge': 'bl'},
  'cphc_mental_telemanas_epmns_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_mental_telemanas_epmns_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_mental_telemanas_epmns_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_newborn_nssk_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_newborn_nssk_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_newborn_nssk_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_newborn_nssk_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_oral_cancer_ntcp_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_oral_cancer_ntcp_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_oral_cancer_ntcp_card3.png': {'y': 0.5, 'verticalBadge': 'tl'},
  'cphc_oral_cancer_ntcp_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_oral_dental_oeee_card1.png': {'y': 0, 'badge': 'bl', 'verticalBadge': 'bl'},
  'cphc_oral_dental_oeee_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_oral_dental_oeee_card3.png': {'y': 0.5, 'verticalBadge': 'tl'},
  'cphc_oral_dental_oeee_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_palliative_epmns_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'br'},
  'cphc_palliative_epmns_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_palliative_epmns_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_palliative_epmns_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_rbsk_screening_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_rbsk_screening_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_rbsk_screening_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_rbsk_screening_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_rksk_adolescent_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_rksk_adolescent_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_rksk_adolescent_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_rksk_adolescent_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_substance_audit_epmns_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_substance_audit_epmns_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_substance_audit_epmns_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_substance_audit_epmns_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_tb_elimination_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_tb_elimination_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_tb_elimination_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_tb_elimination_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_uip_vaccination_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_uip_vaccination_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_uip_vaccination_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_uip_vaccination_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_vector_malaria_dengue_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_vector_malaria_dengue_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_vector_malaria_dengue_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'br'},
  'cphc_vector_malaria_dengue_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'bl'},
  'cphc_wash_infection_control_card1.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_wash_infection_control_card2.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tr'},
  'cphc_wash_infection_control_card3.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'cphc_wash_infection_control_card4.png': {'fit': 'contain', 'align': 'right', 'verticalBadge': 'tl'},
  'apr11_motherhood_card1_anc.jpg': { y: 0.11 },
  'apr11_motherhood_card2_danger.jpg': { y: 0.22, badge: 'bl' },
  'apr11_motherhood_card3_plan.jpg': { y: 0.16 },
  'apr11_motherhood_card4_medicines.jpg': { y: 0.0 },
  'apr17_haemophilia_card1_centre.jpg': { y: 0.0 },
  'apr17_haemophilia_card3_medicine.jpg': { y: 0.09, badge: 'bl' },
  'apr17_haemophilia_card4_activity.jpg': { y: 0.0 },
  'aug20_mosquito_card1_dryday.jpg': { fit: 'contain', align: 'right' },
  'aug20_mosquito_card4_fever.jpg': { y: 0.06 },
  'mar16_vaccination_card1_schedule.jpg': { y: 0.11 },
  'mar16_vaccination_card2_card.jpg': { y: 0.19, badge: 'bl' },
  'mar16_vaccination_card3_followup.jpg': { y: 0.0 },
  'mar16_vaccination_card4_observation.jpg': { y: 0.11, badge: 'bl' },
  'may25_thyroid_card1_symptoms.jpg': { y: 0.11, badge: 'bl' },
  'may25_thyroid_card2_test.jpg': { y: 0.11 },
  'may25_thyroid_card3_medicine.jpg': { y: 0.07 },
  'may28_menstrual_card1_change.jpg': { y: 0.15 },
  'may28_menstrual_card2_hygiene.jpg': { y: 0.22, badge: 'bl' },
  'oct15_do2.png': { y: 0.28 },
  'oct17_dont2.png': { y: 0.2, badge: 'bl' },
  'oct18_do2.png': { y: 0.1 },
  'oct20_do1.png': { y: 0.0, badge: 'tr' },
  'oct21_do2.png': { y: 0.0 },
  'oct21_dont1.png': { y: 0.11, badge: 'bl' },
  'oct22_stuttering_card1_listen.jpg': { y: 0.15 },
  'oct22_stuttering_card2_respect.jpg': { y: 0.18 },
  'oct22_stuttering_card3_slp.jpg': { y: 0.15 },
  'oct24_polio_card1_drops.jpg': { y: 0.12 },
  'oct24_polio_card2_routine.jpg': { y: 0.24, badge: 'bl' },
  'oct29_stroke_card1_fast.jpg': { y: 0.1 },
  'oct29_stroke_card2_ambulance.jpg': { y: 0.18 },
  'oct29_stroke_card3_nofood.jpg': { y: 0.17 },
  'oct29_stroke_card4_prevention.jpg': { y: 0.12 },
  'sep21_alzheimer_card2_communication.jpg': { y: 0.22 },
  'apr17_haemophilia_card2_joint.jpg': { fit: 'contain', align: 'right' },
  'may25_thyroid_card4_iodine.jpg': { fit: 'contain', align: 'right' },
  'oct16_dont2.png': { fit: 'contain', align: 'right' },
  'oct18_dont1.png': { fit: 'contain', align: 'right' },
  'oct18_dont2.png': { fit: 'contain', align: 'right' },
  'oct20_do2.png': { fit: 'contain', align: 'right' },
  'oct24_polio_card4_weakness.jpg': { fit: 'contain', align: 'right' },
  'oct20_dont1.png': { fit: 'contain', align: 'right' }
};

class HealthPosterRenderer {
  constructor() {
    this.canvas = document.createElement('canvas');
    this.ctx = this.canvas.getContext('2d');
    this.imageCache = new Map();
  }

  // Pre-load an image from URL or dataURL
  async loadImage(src) {
    if (!src) return null;
    if (this.imageCache.has(src)) {
      return this.imageCache.get(src);
    }
    return new Promise((resolve) => {
      const img = new Image();
      if (window.location.protocol !== 'file:') {
        img.crossOrigin = 'anonymous';
      }
      img.onload = () => {
        this.imageCache.set(src, img);
        resolve(img);
      };
      img.onerror = () => {
        console.warn('Failed to load image with safe CORS policy:', src);
        resolve(null);
      };
      img.src = src;
    });
  }

  // Ensure Gujarati and English fonts are loaded
  async ensureFontsReady() {
    try {
      if (document.fonts) {
        await Promise.all([
          document.fonts.load('bold 24px "Noto Sans Gujarati"'),
          document.fonts.load('bold 24px "Plus Jakarta Sans"'),
          document.fonts.load('600 18px "Noto Sans Gujarati"'),
          document.fonts.load('600 18px "Plus Jakarta Sans"')
        ]);
        await document.fonts.ready;
      }
    } catch (e) {
      console.warn('Font loading check non-critical warning:', e);
    }
  }

  // Draw rounded rectangle helper
  drawRoundRect(ctx, x, y, width, height, radius, fill = true, stroke = true) {
    if (typeof radius === 'number') {
      radius = { tl: radius, tr: radius, br: radius, bl: radius };
    }
    ctx.beginPath();
    ctx.moveTo(x + radius.tl, y);
    ctx.lineTo(x + width - radius.tr, y);
    ctx.quadraticCurveTo(x + width, y, x + width, y + radius.tr);
    ctx.lineTo(x + width, y + height - radius.br);
    ctx.quadraticCurveTo(x + width, y + height, x + width - radius.br, y + height);
    ctx.lineTo(x + radius.bl, y + height);
    ctx.quadraticCurveTo(x, y + height, x, y + height - radius.bl);
    ctx.lineTo(x, y + radius.tl);
    ctx.quadraticCurveTo(x, y, x + radius.tl, y);
    ctx.closePath();
    if (fill) ctx.fill();
    if (stroke) ctx.stroke();
  }

  // Draw image with cover aspect ratio inside a bounding box
  drawImageCover(ctx, img, x, y, w, h, radius = 0) {
    if (!img) return;
    ctx.save();
    if (radius > 0) {
      this.drawRoundRect(ctx, x, y, w, h, radius, false, false);
      ctx.clip();
    }
    const imgRatio = img.width / img.height;
    const boxRatio = w / h;
    const focus = img.photoFocus || null;
    let sWidth, sHeight, sx, sy;

    if (focus && focus.fit === 'contain' && boxRatio > 1.6) {
      // whole image, aspect preserved, centred on the card background (no stretch, no crop)
      const k = Math.min(w / img.width, h / img.height);
      const dw = img.width * k, dh = img.height * k;
      ctx.fillStyle = '#0B1726';
      ctx.fillRect(x, y, w, h);
      const dx = focus.align === 'right' ? x + (w - dw) : x + (w - dw) / 2;
      ctx.drawImage(img, dx, y + (h - dh) / 2, dw, dh);
      ctx.restore();
      return;
    }

    if (imgRatio > boxRatio) {
      sHeight = img.height;
      sWidth = img.height * boxRatio;
      sx = (img.width - sWidth) / 2;
      sy = 0;
    } else {
      sWidth = img.width;
      sHeight = img.width / boxRatio;
      sx = 0;
      sy = (img.height - sHeight) * (focus && typeof focus.y === 'number' ? focus.y : 0.5);
    }

    ctx.drawImage(img, sx, sy, sWidth, sHeight, x, y, w, h);
    ctx.restore();
  }

  // Word-wrapping text on canvas with optional truncation ellipsis
  wrapText(ctx, text, x, y, maxWidth, lineHeight, maxLines = 3) {
    if (!text) return 0;
    const words = text.split(' ');
    let line = '';
    const lines = [];

    for (let n = 0; n < words.length; n++) {
      const testLine = line + words[n] + ' ';
      const metrics = ctx.measureText(testLine);
      if (metrics.width > maxWidth && n > 0) {
        lines.push(line.trim());
        line = words[n] + ' ';
        if (lines.length >= maxLines) break;
      } else {
        line = testLine;
      }
    }
    if (lines.length < maxLines && line.trim().length > 0) {
      lines.push(line.trim());
    }

    for (let i = 0; i < lines.length; i++) {
      ctx.fillText(lines[i], x, y + (i * lineHeight));
    }
    return lines.length * lineHeight;
  }

  // Lines wrapText would produce for `text` at the current font (same breaking rule, no cap)
  countLines(ctx, text, maxWidth) {
    if (!text) return 0;
    const words = text.split(' ');
    let line = '';
    let count = 0;
    for (let n = 0; n < words.length; n++) {
      const testLine = line + words[n] + ' ';
      if (ctx.measureText(testLine).width > maxWidth && n > 0) {
        count++;
        line = words[n] + ' ';
      } else {
        line = testLine;
      }
    }
    return line.trim().length > 0 ? count + 1 : count;
  }

  // Single-line title; if it is wider than the box it wraps to a second line (never clipped).
  // Returns the height used (lineHeight for one line, 2x for two).
  drawTitleFitted(ctx, text, x, y, maxWidth, lineHeight) {
    // 8px of slack: titles may sit in the card's 14px side padding, but must stay clear of its edge
    if (ctx.measureText(text).width <= maxWidth + 8) {
      ctx.fillText(text, x, y);
      return lineHeight;
    }
    return this.wrapText(ctx, text, x, y, maxWidth, lineHeight, 2);
  }

  // Shrink the current font only as far as needed for `text` to fit maxWidth (no-op when it already fits)
  fitFont(ctx, text, maxWidth, minPx) {
    if (!text) return;
    const size = /(\d+(?:\.\d+)?)px/.exec(ctx.font);
    const width = ctx.measureText(text).width;
    if (!size || width <= maxWidth) return;
    const px = Math.max(minPx, Math.floor(parseFloat(size[1]) * maxWidth / width * 10) / 10);
    ctx.font = ctx.font.replace(size[0], `${px}px`);
  }

  // Gujarati Numerals Helper
  toGuNum(num) {
    const guMap = { '0': '૦', '1': '૧', '2': '૨', '3': '૩', '4': '૪', '5': '૫', '6': '૬', '7': '૭', '8': '૮', '9': '૯' };
    return String(num).split('').map(c => guMap[c] || c).join('');
  }

  // Draw a platform-independent calendar icon with the selected poster's day.
  // Unicode calendar emoji are avoided because most platforms hardcode "17".
  drawCalendarDateIcon(ctx, x, y, dayNumber, useGujaratiNumerals = false) {
    const width = 24;
    const height = 24;
    const dayText = useGujaratiNumerals ? this.toGuNum(dayNumber) : String(dayNumber);

    ctx.save();
    ctx.fillStyle = '#f8fafc';
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 1.2;
    this.drawRoundRect(ctx, x, y, width, height, 4, true, true);

    ctx.fillStyle = '#0ea5e9';
    ctx.fillRect(x + 1, y + 1, width - 2, 6);
    ctx.fillStyle = '#0B1726';
    ctx.font = `800 ${dayText.length > 1 ? 10 : 11}px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(dayText, x + (width / 2), y + 16);
    ctx.restore();
  }

  /**
   * Main Poster Render Method
   * @param {Object} dayData - The day object from health_365.json
   * @param {Object} options - { format: 'square' | 'vertical', language: 'bilingual' | 'gujarati' | 'english', settings: {...}, customPhotos: {1: '...', 2: '...'} }
   */
  async renderPoster(dayData, options = {}) {
    await this.ensureFontsReady();

    const format = options.format || 'square';
    const language = options.language || 'bilingual';
    const settings = options.settings || {};
    const customPhotos = options.customPhotos || {};

    const isVertical = format === 'vertical';
    const WIDTH = 1080;
    const HEIGHT = isVertical ? 1920 : 1080;

    this.canvas.width = WIDTH;
    this.canvas.height = HEIGHT;
    const ctx = this.ctx;

    // -------------------------------------------------------------
    // 1. DEEP CLINICAL SLATE BACKGROUND WITH EDITORIAL LIGHTING
    // -------------------------------------------------------------
    const bgGrad = ctx.createLinearGradient(0, 0, 0, HEIGHT);
    bgGrad.addColorStop(0, '#061320');
    bgGrad.addColorStop(0.3, '#091b2e');
    bgGrad.addColorStop(0.7, '#071624');
    bgGrad.addColorStop(1, '#030a12');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, WIDTH, HEIGHT);

    // Ambient medical soft glow in upper left and lower right
    const glow1 = ctx.createRadialGradient(120, 120, 20, 120, 120, 500);
    glow1.addColorStop(0, 'rgba(14, 165, 233, 0.12)');
    glow1.addColorStop(1, 'transparent');
    ctx.fillStyle = glow1;
    ctx.fillRect(0, 0, 700, 700);

    const glow2 = ctx.createRadialGradient(WIDTH - 120, HEIGHT - 140, 20, WIDTH - 120, HEIGHT - 140, 550);
    glow2.addColorStop(0, 'rgba(16, 185, 129, 0.10)');
    glow2.addColorStop(1, 'transparent');
    ctx.fillStyle = glow2;
    ctx.fillRect(WIDTH - 700, HEIGHT - 700, 700, 700);

    // Subtle framing border
    ctx.save();
    ctx.strokeStyle = '#284454';
    ctx.lineWidth = 1.5;
    this.drawRoundRect(ctx, 16, 16, WIDTH - 32, HEIGHT - 32, 22, false, true);
    ctx.restore();

    // -------------------------------------------------------------
    // 2. PRELOAD ALL 4 CARD PHOTOS
    // -------------------------------------------------------------
    const failedCards = [];
    const loadedImages = await Promise.all(
      dayData.cards.map(async (card) => {
        const customSrc = customPhotos[card.index];
        const src = customSrc || card.photo;
        const img = await this.loadImage(src);
        if (img) img.photoFocus = customSrc ? null : (PHOTO_FOCUS[(card.photo || '').split('/').pop()] || null);
        if (!img) {
          failedCards.push({
            index: card.index,
            title: card.title_en || `Card #${card.index}`,
            src: src || 'no photo specified'
          });
        }
        return img;
      })
    );
    this.lastRenderFailedCards = failedCards;

    // -------------------------------------------------------------
    // 3. HEADER RENDERING
    // -------------------------------------------------------------
    const headerY = isVertical ? 44 : 34;

    // A. Date Badge (Left Pill)
    // Format: dynamic calendar icon + e.g. "15 OCTOBER | ૧૫ ઓક્ટોબર"
    let datePillText = '';
    const upperDateEn = (dayData.date_en || '').toUpperCase();
    if (language === 'gujarati') {
      datePillText = dayData.date_gu;
    } else if (language === 'english') {
      datePillText = upperDateEn;
    } else {
      datePillText = `${upperDateEn} | ${dayData.date_gu}`;
    }

    ctx.save();
    ctx.font = 'bold 18px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
    const dateWidth = ctx.measureText(datePillText).width + 62;
    
    // Smooth pill border with subtle cyan fill
    ctx.fillStyle = 'rgba(11, 30, 48, 0.85)';
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 1.5;
    this.drawRoundRect(ctx, 40, headerY, dateWidth, 38, 19, true, true);
    this.drawCalendarDateIcon(ctx, 53, headerY + 7, dayData.day, language === 'gujarati');
    ctx.fillStyle = '#ffffff';
    ctx.fillText(datePillText, 88, headerY + 25);
    ctx.restore();

    // B. Observance Badge (Right Pill) with Sourced Provenance Verification
    // Badges are derived strictly from verified authority metadata (zero hard-coded ID allowlists).
    // Verified WHO/UN days get gold badges, verified MoHFW days get orange badges,
    // verified global health days get sky blue badges, and rotational guidance gets emerald badges.
    let tierLabel = '';
    let tierColor = '#a7f3d0';
    let tierBg = 'rgba(16, 185, 129, 0.18)';
    let tierBorder = '#10b981';

    const prov = dayData.provenance;
    if (prov && prov.status === 'VERIFIED') {
      const tier = prov.authority_tier;
      if (tier === 'UN_AGENCY' || tier === 'INTERNATIONAL_SOCIETY_WHO' || tier === 'GLOBAL_PARTNERSHIP') {
        tierColor = '#fef08a';
        tierBg = 'rgba(234, 179, 8, 0.22)';
        tierBorder = '#eab308';
      } else if (tier === 'MoHFW_NATIONAL_PROGRAMME') {
        tierColor = '#fed7aa';
        tierBg = 'rgba(249, 115, 22, 0.22)';
        tierBorder = '#f97316';
      } else {
        // Non-governmental accredited global health bodies
        tierColor = '#bae6fd';
        tierBg = 'rgba(14, 165, 233, 0.22)';
        tierBorder = '#0ea5e9';
      }
      tierLabel = language === 'gujarati' ? (prov.badge_gu || '🌐 વિશ્વ આરોગ્ય દિવસ') : (prov.badge_en || '🌐 Global Health Day');
    } else {
      tierColor = '#a7f3d0';
      tierBg = 'rgba(16, 185, 129, 0.18)';
      tierBorder = '#10b981';
      tierLabel = language === 'gujarati' ? '🛡️ દૈનિક આરોગ્ય માર્ગદર્શન' : '🛡️ Daily Health Guidance';
    }

    ctx.save();
    ctx.font = 'bold 17px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
    const tierWidth = ctx.measureText(tierLabel).width + 36;
    const tierX = WIDTH - tierWidth - 40;
    ctx.fillStyle = tierBg;
    ctx.strokeStyle = tierBorder;
    ctx.lineWidth = 1.5;
    this.drawRoundRect(ctx, tierX, headerY, tierWidth, 38, 19, true, true);
    ctx.fillStyle = tierColor;
    ctx.fillText(tierLabel, tierX + 18, headerY + 25);
    ctx.restore();

    // C. Large Bold Bilingual Title (Center)
    let currentY = headerY + 70;
    ctx.save();
    ctx.textAlign = 'center';

    if (language === 'bilingual') {
      // English Title
      ctx.font = 'bold 28px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#38bdf8';
      this.fitFont(ctx, dayData.title_en.toUpperCase(), WIDTH - 80, 20);
      ctx.fillText(dayData.title_en.toUpperCase(), WIDTH / 2, currentY);

      // Gujarati Title (Hero Font)
      currentY += 38;
      ctx.font = 'bold 34px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#ffffff';
      ctx.shadowColor = 'rgba(0, 0, 0, 0.6)';
      ctx.shadowBlur = 8;
      this.fitFont(ctx, dayData.title_gu, WIDTH - 80, 24);
      ctx.fillText(dayData.title_gu, WIDTH / 2, currentY);
      ctx.shadowBlur = 0;
    } else if (language === 'gujarati') {
      ctx.font = 'bold 40px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#ffffff';
      ctx.shadowColor = 'rgba(0, 0, 0, 0.6)';
      ctx.shadowBlur = 8;
      this.fitFont(ctx, dayData.title_gu, WIDTH - 80, 26);
      ctx.fillText(dayData.title_gu, WIDTH / 2, currentY + 12);
      ctx.shadowBlur = 0;
      currentY += 24;
    } else {
      ctx.font = 'bold 36px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#ffffff';
      ctx.shadowColor = 'rgba(0, 0, 0, 0.6)';
      ctx.shadowBlur = 8;
      this.fitFont(ctx, dayData.title_en.toUpperCase(), WIDTH - 80, 24);
      ctx.fillText(dayData.title_en.toUpperCase(), WIDTH / 2, currentY + 12);
      ctx.shadowBlur = 0;
      currentY += 24;
    }

    // D. Theme Subtitle Capsule
    currentY += 28;
    const themeText = language === 'gujarati' ? dayData.theme_gu : (language === 'english' ? dayData.theme_en : `${dayData.theme_en} • ${dayData.theme_gu}`);
    ctx.font = '500 17px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
    this.fitFont(ctx, themeText, WIDTH - 124, 12);
    const themeMetrics = ctx.measureText(themeText);
    const themeBoxW = Math.min(WIDTH - 80, themeMetrics.width + 44);
    const themeBoxX = (WIDTH - themeBoxW) / 2;

    ctx.fillStyle = 'rgba(11, 23, 38, 0.85)';
    ctx.strokeStyle = 'rgba(148, 163, 184, 0.35)';
    ctx.lineWidth = 1;
    this.drawRoundRect(ctx, themeBoxX, currentY - 20, themeBoxW, 32, 16, true, true);
    ctx.fillStyle = '#a7f3d0';
    ctx.fillText(themeText, WIDTH / 2, currentY + 3);
    ctx.restore();

    // -------------------------------------------------------------
    // 4. MODERN 4-CARD VISUAL GRID
    // -------------------------------------------------------------
    if (!isVertical) {
      // SQUARE FORMAT (1080 x 1080)
      const gridStartY = currentY + 22;
      const cardW = 485;
      const cardH = 380;
      const gapX = 30;
      const leftX = 40;
      const rightX = leftX + cardW + gapX;

      const cardPositions = [
        { x: leftX, y: gridStartY, index: 1, card: dayData.cards[0], img: loadedImages[0] },
        { x: rightX, y: gridStartY, index: 2, card: dayData.cards[1], img: loadedImages[1] },
        { x: leftX, y: gridStartY + cardH + 16, index: 3, card: dayData.cards[2], img: loadedImages[2] },
        { x: rightX, y: gridStartY + cardH + 16, index: 4, card: dayData.cards[3], img: loadedImages[3] },
      ];

      for (const pos of cardPositions) {
        this.renderClinicalCardSquare(ctx, pos, language);
      }
    } else {
      // VERTICAL FORMAT (1080 x 1920)
      const gridStartY = currentY + 32;
      const cardW = 485;
      const cardH = 786;
      const gapX = 30;
      const leftX = 40;
      const rightX = leftX + cardW + gapX;

      const cardPositions = [
        { x: leftX, y: gridStartY, index: 1, card: dayData.cards[0], img: loadedImages[0] },
        { x: rightX, y: gridStartY, index: 2, card: dayData.cards[1], img: loadedImages[1] },
        { x: leftX, y: gridStartY + cardH + 26, index: 3, card: dayData.cards[2], img: loadedImages[2] },
        { x: rightX, y: gridStartY + cardH + 26, index: 4, card: dayData.cards[3], img: loadedImages[3] },
      ];

      for (const pos of cardPositions) {
        this.renderClinicalCardVertical(ctx, pos, language);
      }
    }

    // -------------------------------------------------------------
    // 5. BOTTOM FOOTER BAR - REMOVED 2026-10-18 by request.
    // Posters render with no bottom attribution/branding bar in either
    // format. renderFooter() is retained below but unused, so the bar can
    // be restored by re-enabling this single call.
    // -------------------------------------------------------------
    // this.renderFooter(ctx, WIDTH, HEIGHT, isVertical, settings, language);

    return this.canvas;
  }

  /**
   * Render individual card in Square Mode (w: 485, h: 380)
   * Modern Indian Clinical Editorial layout with 4:3 photo and distinct Action Badge
   */
  renderClinicalCardSquare(ctx, pos, language) {
    const { x, y, index, card, img } = pos;
    const w = 485;
    const h = 380;

    ctx.save();

    // 1. Clean rounded container with subtle border (#284454) and soft shadow
    ctx.shadowColor = 'rgba(0, 0, 0, 0.45)';
    ctx.shadowBlur = 14;
    ctx.shadowOffsetX = 0;
    ctx.shadowOffsetY = 6;

    ctx.fillStyle = '#0B1726';
    ctx.strokeStyle = '#284454';
    ctx.lineWidth = 1.5;
    this.drawRoundRect(ctx, x, y, w, h, 18, true, true);
    ctx.shadowBlur = 0;
    ctx.shadowOffsetX = 0;
    ctx.shadowOffsetY = 0;
    ctx.shadowColor = 'transparent';

    // 2. High-res Photo Box
    const photoMargin = 8;
    const photoX = x + photoMargin;
    const photoY = y + photoMargin;
    const photoW = w - (photoMargin * 2);
    const photoH = 215;

    if (img) {
      this.drawImageCover(ctx, img, photoX, photoY, photoW, photoH, 14);
    } else {
      // Editorial clinical fallback
      ctx.fillStyle = '#112233';
      this.drawRoundRect(ctx, photoX, photoY, photoW, photoH, 14, true, false);
      ctx.fillStyle = '#64748b';
      ctx.font = '15px "Plus Jakarta Sans", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('📷 High-Res Photo', photoX + (photoW / 2), photoY + (photoH / 2) + 5);
      ctx.textAlign = 'left';
    }

    // 3. Distinct Action Badge (e.g. "માર્ગદર્શન #૧" or "ACTION #1 • માર્ગદર્શન #૧")
    let badgeY = photoY + 10;
    let badgeX = photoX + 10;
    const guNum = this.toGuNum(index);
    let badgeText = '';
    if (language === 'gujarati') {
      badgeText = `માર્ગદર્શન #${guNum}`;
    } else if (language === 'english') {
      badgeText = `ACTION #${index}`;
    } else {
      badgeText = `ACTION #${index} • માર્ગદર્શન #${guNum}`;
    }

    ctx.font = 'bold 13px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
    const badgeW = ctx.measureText(badgeText).width + 24;
    const badgeH = 26;
    const corner = (img && img.photoFocus && img.photoFocus.badge) || 'tl';
    if (corner === 'tr' || corner === 'br') badgeX = photoX + photoW - 10 - badgeW;
    if (corner === 'bl' || corner === 'br') badgeY = photoY + photoH - 10 - badgeH;

    // Smooth pill overlay with dark glass background & cyan accent
    ctx.fillStyle = 'rgba(7, 19, 32, 0.90)';
    ctx.strokeStyle = '#0ea5e9';
    ctx.lineWidth = 1.2;
    this.drawRoundRect(ctx, badgeX, badgeY, badgeW, badgeH, 13, true, true);

    ctx.fillStyle = '#38bdf8';
    ctx.fillText(badgeText, badgeX + 12, badgeY + 18);

    // 4. Content Area below photo
    const contentX = x + 14;
    const contentY = photoY + photoH + 18;
    const maxTextW = w - 28;

    // Bilingual Action Header
    if (language === 'bilingual') {
      // English Title
      ctx.font = 'bold 16px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#38bdf8';
      const enTitle = card.title_en || '';
      this.fitFont(ctx, enTitle, maxTextW + 8, 13);
      ctx.fillText(enTitle, contentX, contentY);

      // Gujarati Title
      ctx.font = 'bold 18px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#ffffff';
      const guTitle = card.title_gu || '';
      this.fitFont(ctx, guTitle, maxTextW + 8, 15);
      ctx.fillText(guTitle, contentX, contentY + 22);

      // Medical Caption (Concise): 2 lines each; a 3rd line is added only where the text would
      // otherwise be cut off, and the English caption then sits 12px lower to stay inside the card.
      ctx.font = '400 13.5px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#cbd5e1';
      const guCapLines = Math.min(3, Math.max(2, this.countLines(ctx, card.desc_gu || '', maxTextW)));
      this.wrapText(ctx, card.desc_gu || '', contentX, contentY + 44, maxTextW, 18, guCapLines);

      ctx.font = '400 12.5px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#94a3b8';
      const enCapLines = Math.min(3, Math.max(2, this.countLines(ctx, card.desc_en || '', maxTextW)));
      this.wrapText(ctx, card.desc_en || '', contentX, contentY + (guCapLines > 2 ? 96 : 84), maxTextW, 16, enCapLines);

    } else if (language === 'gujarati') {
      ctx.font = 'bold 20px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#ffffff';
      const tGuH = this.drawTitleFitted(ctx, card.title_gu || '', contentX, contentY + 4, maxTextW, 22);

      ctx.font = '400 14px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#cbd5e1';
      const guY = contentY + 34 + (tGuH - 22);
      this.wrapText(ctx, card.desc_gu || '', contentX, guY, maxTextW, 20, Math.max(3, Math.floor((y + h - 10 - guY) / 20) + 1));

    } else {
      ctx.font = 'bold 19px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#38bdf8';
      const tEnH = this.drawTitleFitted(ctx, card.title_en || '', contentX, contentY + 4, maxTextW, 22);

      ctx.font = '400 14px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#cbd5e1';
      const enY = contentY + 34 + (tEnH - 22);
      this.wrapText(ctx, card.desc_en || '', contentX, enY, maxTextW, 20, Math.max(3, Math.floor((y + h - 10 - enY) / 20) + 1));
    }

    ctx.restore();
  }

  /**
   * Render individual card in Vertical Mode (w: 485, h: 725)
   * High-impact 4:3 high-res photo with clean clinical typography
   */
  renderClinicalCardVertical(ctx, pos, language) {
    const { x, y, index, card, img } = pos;
    const w = 485;
    const h = 786;

    ctx.save();

    // 1. Clean rounded container with subtle border (#284454) and soft shadow
    ctx.shadowColor = 'rgba(0, 0, 0, 0.50)';
    ctx.shadowBlur = 18;
    ctx.shadowOffsetX = 0;
    ctx.shadowOffsetY = 8;

    ctx.fillStyle = '#0B1726';
    ctx.strokeStyle = '#284454';
    ctx.lineWidth = 1.8;
    this.drawRoundRect(ctx, x, y, w, h, 22, true, true);
    ctx.shadowBlur = 0;
    ctx.shadowOffsetX = 0;
    ctx.shadowOffsetY = 0;
    ctx.shadowColor = 'transparent';

    // 2. High-res Photo Box (4:3 aspect ratio: 465w x 348h)
    const photoMargin = 10;
    const photoX = x + photoMargin;
    const photoY = y + photoMargin;
    const photoW = w - (photoMargin * 2);
    const photoH = 350; // Exact 4:3 ratio: 465 / 4 * 3 = 348.75 ~ 350px

    if (img) {
      this.drawImageCover(ctx, img, photoX, photoY, photoW, photoH, 16);
    } else {
      ctx.fillStyle = '#112233';
      this.drawRoundRect(ctx, photoX, photoY, photoW, photoH, 16, true, false);
      ctx.fillStyle = '#64748b';
      ctx.font = '18px "Plus Jakarta Sans", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('📷 4:3 High-Res Photo', photoX + (photoW / 2), photoY + (photoH / 2) + 5);
      ctx.textAlign = 'left';
    }

    // 3. Distinct Action Badge
    let badgeY = photoY + 12;
    let badgeX = photoX + 12;
    const guNum = this.toGuNum(index);
    let badgeText = '';
    if (language === 'gujarati') {
      badgeText = `માર્ગદર્શન #${guNum}`;
    } else if (language === 'english') {
      badgeText = `ACTION #${index}`;
    } else {
      badgeText = `ACTION #${index} • માર્ગદર્શન #${guNum}`;
    }

    ctx.font = 'bold 15px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
    const badgeW = ctx.measureText(badgeText).width + 28;
    const badgeH = 32;
    const verticalCorner = (img && img.photoFocus && img.photoFocus.verticalBadge) || 'tl';
    if (verticalCorner === 'tr' || verticalCorner === 'br') badgeX = photoX + photoW - 12 - badgeW;
    if (verticalCorner === 'bl' || verticalCorner === 'br') badgeY = photoY + photoH - 12 - badgeH;

    ctx.fillStyle = 'rgba(7, 19, 32, 0.92)';
    ctx.strokeStyle = '#0ea5e9';
    ctx.lineWidth = 1.4;
    this.drawRoundRect(ctx, badgeX, badgeY, badgeW, badgeH, 16, true, true);

    ctx.fillStyle = '#38bdf8';
    ctx.fillText(badgeText, badgeX + 14, badgeY + 22);

    // 4. Content Area below photo
    const contentX = x + 18;
    const contentY = photoY + photoH + 26;
    const maxTextW = w - 36;

    if (language === 'bilingual') {
      // English Title
      ctx.font = 'bold 24px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#38bdf8';
      const titleEnH = this.wrapText(ctx, card.title_en || '', contentX, contentY, maxTextW, 29, 2);

      // Gujarati Title (wrapped: long titles previously overflowed the card edge)
      ctx.font = 'bold 26px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#ffffff';
      const titleGuH = this.wrapText(ctx, card.title_gu || '', contentX, contentY + titleEnH, maxTextW, 32, 2);

      // Gujarati Description - flows below the actual title height
      ctx.font = '400 19px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#e2e8f0';
      const descY = contentY + titleEnH + titleGuH + 16;
      const guLinesH = this.wrapText(ctx, card.desc_gu || '', contentX, descY, maxTextW, 27, 5);

      // English Description
      ctx.font = '400 17px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#94a3b8';
      this.wrapText(ctx, card.desc_en || '', contentX, descY + guLinesH + 12, maxTextW, 24, 5);

    } else if (language === 'gujarati') {
      ctx.font = 'bold 29px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#ffffff';
      const tGuOnlyH = this.wrapText(ctx, card.title_gu || '', contentX, contentY + 10, maxTextW, 36, Math.min(3, Math.max(2, this.countLines(ctx, card.title_gu || '', maxTextW))));

      ctx.font = '400 21px "Noto Sans Gujarati", sans-serif';
      ctx.fillStyle = '#e2e8f0';
      const guOnlyY = contentY + 10 + tGuOnlyH + 18;
      this.wrapText(ctx, card.desc_gu || '', contentX, guOnlyY, maxTextW, 31, Math.max(8, Math.floor((y + h - 16 - guOnlyY) / 31) + 1));

    } else {
      ctx.font = 'bold 28px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#38bdf8';
      const tEnOnlyH = this.wrapText(ctx, card.title_en || '', contentX, contentY + 10, maxTextW, 34, Math.min(3, Math.max(2, this.countLines(ctx, card.title_en || '', maxTextW))));

      ctx.font = '400 21px "Plus Jakarta Sans", sans-serif';
      ctx.fillStyle = '#e2e8f0';
      const enOnlyY = contentY + 10 + tEnOnlyH + 18;
      this.wrapText(ctx, card.desc_en || '', contentX, enOnlyY, maxTextW, 31, Math.max(8, Math.floor((y + h - 16 - enOnlyY) / 31) + 1));
    }

    ctx.restore();
  }

  /**
   * Render Footer Bar (Public Interest vs Custom Doctor Branding)
   */
  renderFooter(ctx, width, height, isVertical, settings, language) {
    ctx.save();
    const useDoctor = settings.useDoctorBranding && settings.doctorName;

    if (!isVertical) {
      // SQUARE FOOTER (y: 1012 to 1062)
      const footerY = 1012;
      const footerH = 50;
      const footerW = width - 80;
      const footerX = 40;

      // Dark clinical container
      ctx.fillStyle = 'rgba(11, 23, 38, 0.95)';
      ctx.strokeStyle = useDoctor ? '#10b981' : '#284454';
      ctx.lineWidth = 1.5;
      this.drawRoundRect(ctx, footerX, footerY, footerW, footerH, 14, true, true);

      ctx.textAlign = 'center';
      if (!useDoctor) {
        ctx.font = 'bold 16px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
        ctx.fillStyle = '#38bdf8';
        const msg = language === 'gujarati'
          ? '🏛️ જાહેર આરોગ્ય હિતમાં પ્રસારિત | નિરોગી ભારત અભિયાન'
          : (language === 'english'
            ? '🏛️ Issued in Public Interest for Health Awareness | Healthy India Mission'
            : '🏛️ Issued in Public Interest for Health Awareness | જાહેર આરોગ્ય હિતમાં પ્રસારિત');
        ctx.fillText(msg, width / 2, footerY + 31);
      } else {
        ctx.font = 'bold 16px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
        ctx.fillStyle = '#34d399';
        const clinicPart = settings.clinicName ? ` • ${settings.clinicName}` : '';
        const phonePart = settings.contactInfo ? ` • 💬 WhatsApp: ${settings.contactInfo}` : '';
        const line = `🩺 ${settings.doctorName} (${settings.doctorDegree || 'Medical Consultant'})${clinicPart}${phonePart}`;
        ctx.fillText(line, width / 2, footerY + 31);
      }
    } else {
      // VERTICAL FOOTER (y: 1755 to 1890) - WhatsApp Status & Story Bar
      const footerY = 1755;
      const footerH = 135;
      const footerW = width - 80;
      const footerX = 40;

      // Gradient medical container
      const footerGrad = ctx.createLinearGradient(footerX, footerY, footerX + footerW, footerY + footerH);
      footerGrad.addColorStop(0, 'rgba(11, 23, 38, 0.95)');
      footerGrad.addColorStop(1, 'rgba(6, 30, 48, 0.95)');
      ctx.fillStyle = footerGrad;
      ctx.strokeStyle = useDoctor ? '#10b981' : '#284454';
      ctx.lineWidth = 2;
      this.drawRoundRect(ctx, footerX, footerY, footerW, footerH, 20, true, true);

      if (!useDoctor) {
        ctx.textAlign = 'center';
        ctx.font = 'bold 22px "Plus Jakarta Sans", sans-serif';
        ctx.fillStyle = '#38bdf8';
        ctx.fillText('ISSUED IN PUBLIC INTEREST FOR HEALTH AWARENESS', width / 2, footerY + 44);

        ctx.font = 'bold 22px "Noto Sans Gujarati", sans-serif';
        ctx.fillStyle = '#ffffff';
        ctx.fillText('જાહેર જનતાના આરોગ્ય અને સુખાકારીના હિતમાં પ્રસારિત', width / 2, footerY + 80);

        ctx.font = '500 16px "Plus Jakarta Sans", sans-serif';
        ctx.fillStyle = '#94a3b8';
        ctx.fillText('National Health Mission • Preventive Healthcare India • 365 Days Health Calendar', width / 2, footerY + 112);
      } else {
        // High-end Doctor Profile Card in Footer
        // Doctor Icon Circle
        ctx.fillStyle = '#10b981';
        this.drawRoundRect(ctx, footerX + 25, footerY + 25, 85, 85, 42, true, false);
        ctx.font = '42px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('🩺', footerX + 67, footerY + 82);

        // Doctor Name & Degree
        ctx.textAlign = 'left';
        ctx.font = 'bold 24px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
        ctx.fillStyle = '#ffffff';
        ctx.fillText(settings.doctorName, footerX + 130, footerY + 46);

        ctx.font = '600 17px "Plus Jakarta Sans", sans-serif';
        ctx.fillStyle = '#34d399';
        ctx.fillText(settings.doctorDegree || 'Medical Specialist', footerX + 130, footerY + 74);

        // Clinic & Contact
        ctx.font = '500 16px "Plus Jakarta Sans", "Noto Sans Gujarati", sans-serif';
        ctx.fillStyle = '#cbd5e1';
        const contactLine = `${settings.clinicName || 'Clinic'}  |  💬 WhatsApp: ${settings.contactInfo || ''}`;
        ctx.fillText(contactLine, footerX + 130, footerY + 104);
      }
    }
    ctx.restore();
  }

  /**
   * Export Poster Method with Mandatory Image Failure Guard
   * Throws an error and halts export if any required card photo failed to load.
   */
  async exportPoster(dayData, options = {}) {
    const canvas = await this.renderPoster(dayData, options);
    if (this.lastRenderFailedCards && this.lastRenderFailedCards.length > 0) {
      const details = this.lastRenderFailedCards
        .map(c => `Card #${c.index} (${c.title}): ${c.src}`)
        .join(', ');
      throw new Error(`Export blocked: Required card photo assets failed to load: ${details}`);
    }
    return canvas;
  }
}

window.HealthPosterRenderer = HealthPosterRenderer;
