---
layout: default
title: Budesonide
parent: Model Prediction Only (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Budesonide: predicted new indication Atopic eczema (evidence level L5). Approved use: Crohn's disease, inflammatory bowel disease, Crohn's colitis, asthma…"
monitor_inn: "Budesonide"
predicted_indications: ["atopic eczema", "bronchitis", "dermatitis, atopic", "polyp of vocal cord", "polyp of middle ear", "epulis", "fibroepithelial polyp", "uterine polyp", "polyp of frontal sinus", "polyp of external auditory canal"]
---

# Budesonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Budesonide: From Crohn's Disease and Asthma to Atopic Eczema
{: .text-alpha }

## One-Sentence Summary

Budesonide is a glucocorticoid originally used for Crohn's disease, inflammatory bowel disease, asthma and allergic rhinitis.
The TxGNN model predicts it may be effective for **atopic eczema**, but **no clinical trials** and only **indirect or preclinical publications** currently support this prediction.
The top-ranked prediction is therefore a research question rather than an actionable candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Crohn's disease, inflammatory bowel disease, Crohn's colitis, asthma, allergic rhinitis (approved indication text is not available in the India records) |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 (preclinical and indirect evidence only) |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for budesonide: "Budesonide is an anti-inflammatory corticosteroid that exhibits potent glucocorticoid activity and weak mineralocorticoid activity. In standard in vitro and animal models, budesonide has approximately a 200-fold higher affinity for the glucocorticoid receptor and a 1000-fold higher topical anti-inflammatory potency than cortisol (rat croton oil ear edema assay)." ([DailyMed: Budesonide Inhalation Suspension (budesonide) prescribing information, Cipla USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c52c5382-1400-44b9-95be-a30e1cf706da), label version 2026-06-10; accessed 2026-11-19.) Based on known pharmacology, budesonide is a glucocorticoid with broad anti-inflammatory and immunosuppressive activity. It suppresses Th2 cytokines and reduces eosinophil and mast cell activity. Its efficacy in allergic airway disease (asthma, allergic rhinitis) and inflammatory bowel disease is established.

Atopic eczema is a Th2-driven allergic inflammatory skin disease, which overlaps with the allergic and eosinophilic inflammation budesonide already treats. Topical corticosteroids are already standard therapy for this condition, so the mechanistic link is plausible.

However, the high TxGNN score is a computational prediction only. No clinical trial of budesonide in atopic eczema was found. The available literature consists of a preclinical formulation study of budesonide nanoparticle hydrogels, plus papers on corticosteroid contact allergy and adrenal suppression, which speak to risk rather than efficacy.

Of the other predictions, **bronchitis** has the most clinical activity (L2): small Phase 2 trials of budesonide/formoterol in post-transplant bronchiolitis obliterans (NCT00624754, NCT01560689). However, the "bronchitis" label covers a mix of different conditions, and no efficacy results were provided. **Polyp of the frontal sinus** has a plausible mechanism (intranasal budesonide is used in nasal polyps) but only older, indirect literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for atopic eczema.

For reference, the trials identified for the second-ranked prediction, bronchitis:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00624754](https://clinicaltrials.gov/study/NCT00624754) | Phase 2 | Completed | 32 | Budesonide/formoterol in bronchiolitis obliterans after allogeneic stem cell transplant; no results provided |
| [NCT01560689](https://clinicaltrials.gov/study/NCT01560689) | Phase 2 | Completed | 32 | Open-label budesonide/formoterol in bronchiolitis obliterans after stem cell transplant; uncontrolled design |
| [NCT03436225](https://clinicaltrials.gov/study/NCT03436225) | Phase 1 | Unknown | 80 | Steroid therapy in acute bronchiolitis in children; may not be budesonide-specific |
| [NCT02002715](https://clinicaltrials.gov/study/NCT02002715) | Phase 4 | Completed | 106 | Different inhaled corticosteroid treatment courses in eosinophilic bronchitis |
| [NCT00483743](https://clinicaltrials.gov/study/NCT00483743) | Phase 2 | Completed | 62 | Inhaled TPI 1020 vs budesonide vs placebo in COPD; link to bronchitis unclear |
| [NCT00202189](https://clinicaltrials.gov/study/NCT00202189) | Phase 4 | Completed | 4 | Acute effects of inhaled corticosteroids on airway function in COPD; physiological study |

---

## Literature Evidence

No literature directly shows efficacy of budesonide in atopic eczema. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38275852](https://pubmed.ncbi.nlm.nih.gov/38275852/) | 2024 | Preclinical formulation study | Gels | Budesonide-loaded pH-sensitive nanoparticles in hydrogels for local therapy of atopic dermatitis |
| [35056927](https://pubmed.ncbi.nlm.nih.gov/35056927/) | 2021 | Formulation study | Pharmaceutics | Strategies to improve budesonide skin retention (cyclodextrin and poloxamer hydrogels) |
| [9496795](https://pubmed.ncbi.nlm.nih.gov/9496795/) | 1998 | Open longitudinal study | Pediatr Dermatol | Knemometry in 14 children with atopic dermatitis on topical budesonide, assessing short-term growth effects |
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Adrenal suppression with intranasal corticosteroids |
| [14616123](https://pubmed.ncbi.nlm.nih.gov/14616123/) | 2003 | Review | Allergy | Corticosteroid allergy in asthma patients |
| [33931866](https://pubmed.ncbi.nlm.nih.gov/33931866/) | 2021 | Patch-test study | Contact Dermatitis | Budesonide as a marker of corticosteroid hypersensitivity; allergy trend declining |
| [16428071](https://pubmed.ncbi.nlm.nih.gov/16428071/) | 2006 | Laboratory study | Int Immunopharmacol | Budesonide, but not tacrolimus, affects immune functions of normal human keratinocytes |
| [37927648](https://pubmed.ncbi.nlm.nih.gov/37927648/) | 2023 | Case report | Cureus | Steroid-induced angioedema and urticaria |

---

## India Market Information

Twenty valid single-ingredient registrations were found, and none has approved indication text on record.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 8652 | Airwin-B 1.0 Respules (2ml Each) | Packet of 5 respules | Valid |
| 9569 | Airwin-B 0.5 Respules (2ml Each) | Packet of 5 respules | Valid |
| 25841 | Budez CR Capsule | Strip of 10 capsule cr | Valid |
| 25872 | Budate Transpules | Packet of 2 ml Transpules | Valid |
| 25931 | Budecort 200 Rotacap | Packet of 30 rotacaps | Valid |
| 26233 | Budate Transpules | Packet of 7 transpules | Valid |
| 26300 | Budate Forte Transpules 2ml | Packet of 5 transpules | Valid |
| 26617 | Bunase 1mg Respules | Strip of 2 ml Respules | Valid |
| 26640 | Budate 400 Transcaps | Bottle of 30 transcaps | Valid |
| 27041 | Budate 200 Transcaps | Bottle of 30 transcaps | Valid |
| 28230 | Bunase 200mcg Rotacap | Packet of 30 rotacaps | Valid |
| 28496 | Budeste 1mg Respules 2ml | Packet of 5 respules | Valid |
| 28900 | Budesine Respules | Packet of 2 ml Respules | Valid |
| 30886 | Budvent 100mcg Easecaps | Strip of 30 capsules | Valid |
| 35579 | Cortirowa OD 9mg Tablet PR | Strip of 10 Tablet pr | Valid |
| 63173 | Derinide 0.5mg Respules 2ml | Packet of 14 respules | Valid |
| 67873 | Derinide 200mcg Respicap | Strip of 30 respicaps | Valid |
| 150760 | Nebzmart B 0.5mg Smartules 2ml | Packet of 7 respules | Valid |
| 175157 | Pulmicort 100mcg Inhaler | Packet of 1 Inhaler | Valid |
| 181982 | Pneumabud 0.5mg Respules (2ml Each) | Box of 5 respules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

The registered products are inhalation and nebulised forms plus oral controlled-release forms. None of the registered forms is a topical dermatological product, so atopic eczema would require a new formulation and route.

---

## Safety Considerations

- **Contraindications (not label text)**: hypertension, epilepsy, liver disease, gallbladder disease, hyperglycaemia, congestive heart failure, measles, herpes simplex keratitis, and several pituitary deficiency conditions (e.g. hypopituitarism, growth hormone deficiency, hypogonadotropic hypogonadism).
- **Drug Interactions**: 599 interactions were identified. Major interactions include **adalimumab** and **fosamprenavir**. Moderate interactions include zidovudine, isotretinoin, ketorolac, ibuprofen, nifedipine, ethinylestradiol and fluvoxamine. Minor interactions include formoterol and salbutamol.
- **Relevant risks from the literature**: corticosteroid contact allergy and hypersensitivity, adrenal (HPA axis) suppression, and possible effects on short-term growth in children.

Please refer to the package insert for warnings and label contraindications, which were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for atopic eczema is very high, but it is a computational prediction with no supporting clinical trials. The literature is preclinical or addresses risk (contact allergy, adrenal suppression) rather than efficacy. Topical corticosteroids already serve as standard therapy, so a budesonide product would need to show a clear advantage. The India registrations are inhaled and oral products, with no topical form.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-registered products
- Detailed mechanism of action data
- Clinical evidence in atopic eczema, such as a controlled trial of topical budesonide versus established topical corticosteroids
- A topical formulation and route-compatibility assessment
- A safety plan covering systemic absorption, adrenal suppression, growth in children and contact sensitisation
- Alternative lead: the bronchitis/bronchiolitis and nasal polyp indications (L2 and L4) could be reviewed separately, once a defined patient population and efficacy results are available

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not currently available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Budesonide Inhalation Suspension (budesonide) prescribing information, Cipla USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c52c5382-1400-44b9-95be-a30e1cf706da) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

