---
layout: default
title: Clindamycin
parent: Model Prediction Only (L5)
nav_order: 194
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
description: "Clindamycin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Acne, streptococcal and staphylococcal infections…"
monitor_inn: "Clindamycin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "exposure keratitis", "non-human animal disease", "neurotrophic keratopathy", "epidemic keratoconjunctivitis", "postmenopausal atrophic vaginitis"]
---

# Clindamycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Clindamycin: From Bacterial Infections and Acne to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Clindamycin is a lincosamide antibiotic originally used for bacterial infections (streptococcal, staphylococcal and anaerobic infections), bacterial vaginosis and acne.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, streptococcal and staphylococcal infections, anaerobic bacterial infections, bacterial vaginosis (the India licence records contain no approved indication text) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for clindamycin: "Clindamycin inhibits bacterial protein synthesis by binding to the 23S RNA of the 50S subunit of the ribosome. Clindamycin is bacteriostatic." ([DailyMed: Cleocin Hydrochloride (clindamycin hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df9a2a41-b132-4f43-8940-b2d773b1369a), label version 2026-09-16; accessed 2026-11-19.) Based on known information, clindamycin is a lincosamide antibiotic that inhibits bacterial protein synthesis. Its efficacy in Gram-positive and anaerobic bacterial infections is established, so any benefit would be limited to a bacterial component of an eye surface disease.

The link to the predicted indication is weak. Punctate epithelial keratoconjunctivitis is often viral or inflammatory rather than bacterial, so an antibacterial mechanism is not established. The very high score (0.9997) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predictions for this drug show the same pattern. Exposure keratitis has only indirect literature on bacterial keratitis. Epidemic keratoconjunctivitis is adenoviral, and clindamycin has no antiviral activity. Postmenopausal atrophic vaginitis is driven by oestrogen deficiency. "Non-human animal disease" is not a usable human indication. Neurotrophic keratopathy is not primarily bacterial.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction (punctate epithelial keratoconjunctivitis).

For the second-ranked prediction, exposure keratitis, only indirect papers were retrieved. None addresses exposure keratitis or clindamycin treatment:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24244625](https://pubmed.ncbi.nlm.nih.gov/24244625/) | 2013 | Retrospective cohort | PLoS One | Hospital review of *S. aureus* keratitis comparing MRSA and MSSA isolates (demographics, antibiotic susceptibility, outcomes) |
| [22880135](https://pubmed.ncbi.nlm.nih.gov/22880135/) | 2012 | Retrospective cohort | PLoS One | Prevalence, clinical features and antibiotic susceptibility of ocular MRSA vs MSSA infections |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | Case report | Ophthalmology | Contact lens-related *Bacillus cereus* keratitis and ulcer linked to a contaminated lens case |
| [42763505](https://pubmed.ncbi.nlm.nih.gov/42763505/) | 2026 | Case report | IDCases | Vision-threatening ocular toxoplasmosis involving the fovea, diagnosed by intraocular fluid mNGS (not relevant to clindamycin use here) |

## India Market Information

Twenty valid licences are registered. The licence records contain no approved indication text.

<!-- review:begin in-lic-20261124c-clindamycin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Twenty valid single-ingredient licences are registered." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-clindamycin-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 35292 | Clotrimol 100mg/200mg Vaginal Capsule | Packet of 3 Vaginal Capsules | Valid |
| 35710 | Clid 300mg Injection | Vial of 4 ml Injection | Valid |
| 39034 | Clindamax 300mg Capsule | Strip of 10 capsules | Valid |
| 39324 | Canfree V7 100mg/200mg Suppository | Strip of 7 suppositories | Valid |
| 40533 | Cliford-CT Softgel Capsule | Strip of 7 Vaginal Capsules | Valid |
| 43999 | Clindasure 150mg Capsule | Strip of 10 capsules | Valid |
| 44340 | Clearbet Soft Gelatin Capsule | Strip of 10 soft gelatin capsules | Valid |
| 47373 | Clindazac 300mg Capsule | Strip of 10 capsules | Valid |
| 53040 | Clindamax 150mg Capsule | Strip of 10 capsules | Valid |
| 58772 | Dalacin C 150mg Capsule | Strip of 10 capsules | Valid |
| 63269 | Damclid 300mg Capsule | Strip of 10 capsules | Valid |
| 63474 | Dalcap 150mg Capsule | Strip of 4 capsules | Valid |
| 65767 | Damcin 300mg Injection | Vial of 2 ml Injection | Valid |
| 106481 | Humclid 600mg Injection | Vial of 4 ml Injection | Valid |
| 120122 | Klindark 300mg Injection | Vial of 2 ml Injection | Valid |
| 121426 | Leezole VG Vaginal Softgel Capsule | Strip of 3 Vaginal Suppository | Valid |
| 137725 | Mcin 300mg Tablet | Strip of 10 tablets | Valid |
| 141344 | Mazocan Suppository | Packet of 3 suppositories | Valid |
| 216339 | Triben V 100mg/100mg Tablet VT | Strip of 7 tablet vt | Valid |
| 221404 | Taboclin 300mg Capsule | Strip of 10 capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Available routes include oral capsules and tablets, injectables and vaginal capsules or suppositories. No ophthalmic formulation appears among the registrations.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: liver failure, sunburn, Crohn disease, inflammatory bowel disease, Crohn's colitis, ulcerative colitis, atopic eczema/dermatitis, exfoliative dermatitis, diarrhoeal disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, vulvovaginal candidiasis.
- **Drug Interactions**: 320 interactions are recorded. Moderate-level interactions include balsalazide, clarithromycin, picosulfuric acid, attapulgite and kaolin. Others are of unknown severity, including amphotericin B, aspirin, amoxicillin, bupropion, pantoprazole, metformin, omeprazole, sucralfate, vancomycin and morphine.

Package insert warnings and contraindications were not obtained. Please refer to the package insert for full safety information. Clindamycin is also a well-known risk factor for *C. difficile* infection.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials or literature, and the proposed disease is often viral or inflammatory, so an antibacterial mechanism is not plausible. The knowledge graph also flags several gastrointestinal and dermatological contraindications, and there is no ophthalmic formulation registered in India.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently blocking safety screening)
- Mechanism of action data from DrugBank
- Evidence that a bacterial component exists in punctate epithelial keratoconjunctivitis, or a re-ranking toward better-supported ocular bacterial indications (for example bacterial keratitis)
- Assessment of ocular route feasibility and formulation, since only oral, injectable and vaginal products are registered
- Exclusion of non-actionable terms ("non-human animal disease") and name-matching false positives (epidemic keratoconjunctivitis) from the candidate list

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cleocin Hydrochloride (clindamycin hydrochloride) prescribing information, Pharmacia & Upjohn Company LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=df9a2a41-b132-4f43-8940-b2d773b1369a) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

