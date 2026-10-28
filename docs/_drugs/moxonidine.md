---
layout: default
title: Moxonidine
parent: Model Prediction Only (L5)
nav_order: 572
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Moxonidine"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "primary hereditary glaucoma"]
description: "Moxonidine: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Not recorded in the local data"
---

# Moxonidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Moxonidine: Hypotrichosis simplex of the scalp
{: .text-alpha }

## One-Sentence Summary

Moxonidine is a centrally acting antihypertensive, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**,
but **no clinical trials and no drug-specific publications** currently support this prediction. It is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, moxonidine is a centrally acting antihypertensive that lowers blood pressure by reducing sympathetic outflow. It is understood to act as an imidazoline I1 / alpha-2 adrenergic agonist, and pharmacology data show it binds the alpha-2A, alpha-2B and alpha-2C adrenoceptors.

No plausible link between this mechanism and hair follicle biology or the genes behind hereditary hypotrichosis (e.g., CDSN, APCDD1) is evident. The original indication (hypertension) and the predicted indication (a hereditary hair-growth disorder) are unrelated. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so the prediction cannot be mechanistically verified.

**Other predictions in the same run** (all L5, all Hold, none with clinical trials):

| Rank | Predicted Indication | Score | Assessment |
|---|---|---|---|
| 2 | Congenital hypotrichosis milia | 0.9994 | No pathway linking sympatholytic activity to this genetic hair disorder; likely a TxGNN model (deep learning) artifact |
| 3 | Diffuse alopecia areata | 0.9991 | Autoimmune (JAK/T-cell) condition; no established immunomodulatory mechanism for moxonidine |
| 4 | Alopecia | 0.9990 | The only retrieved paper is a case report that does not involve moxonidine |
| 6 | Malignant hypertensive renal disease | 0.9967 | Near-duplicate of rank 5 (identical score); overlaps the approved indication |
| 7 | Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9966 | Likely driven by name similarity; distinct pathophysiology |
| 8 | Pulmonary hypertension, unclear multifactorial mechanism | 0.9966 | Same concerns as rank 7 |
| 9 | Braddock syndrome | 0.9962 | Ultra-rare disorder; any link is indirect via the pulmonary hypertension phenotype |
| 10 | Primary hereditary glaucoma | 0.9954 | Class-level rationale (alpha-2 agonists lower intraocular pressure), but moxonidine is I1-selective and systemic. Most mechanistically credible, though unsupported by clinical data |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature directly supports moxonidine for the top predicted indication. For the related prediction "alopecia" (rank 4), one publication was retrieved, but it is not drug-specific:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40007390](https://pubmed.ncbi.nlm.nih.gov/40007390/) | 2024 | Case report | Georgian Medical News | Case of Graham-Little-Piccardi-Lasseur syndrome (a rare lichenoid scarring alopecia) in a 64-year-old woman; does not involve moxonidine, so it is not evidence for the drug |

## India Market Information

Moxonidine is marketed in India with 20 valid single-ingredient registrations. Approved indication text was not available for these registrations. Main examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 22011 | Arkamox 0.3 Tablet (ADN Life Sciences) | Strip of 10 tablets | Not available |
| 108298 | Ifimox 0.3 Tablet (J B Chemicals and Pharmaceuticals) | Strip of 10 tablets | Not available |
| 134367 | Moxocard 0.3 Tablet (Lupin) | Strip of 10 tablets | Not available |
| 134160 | Moxon 0.3 Tablet (Abbott) | Strip of 10 tablets | Not available |
| 134799 | Moxilong 0.2 Tablet (Micro Labs) | Strip of 15 tablets | Not available |

## Safety Considerations

Please refer to the package insert for safety information.

Receptor pharmacology data confirm that moxonidine binds the alpha-2A, alpha-2B and alpha-2C adrenoceptors. No specific drug-drug interactions were identified in the data compiled for this report. Moxonidine is not approved by the FDA, although it is approved in many other countries as an antihypertensive.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a computational score (0.9995) with no clinical trials and no drug-specific literature. There is no plausible mechanistic link between a centrally acting sympatholytic antihypertensive and hereditary hair-growth disorders, so it is likely a TxGNN model (deep learning) artifact. Among all predictions, only primary hereditary glaucoma (alpha-2 class rationale) and the hypertension-related entries have some biological plausibility, and these also lack direct evidence.

**To proceed, the following is needed:**
- Detailed mechanism of action data for moxonidine
- Package insert warnings and contraindications from the India registrations, to enable safety screening
- A targeted literature search on moxonidine and hair follicle biology or hair loss
- For a more credible alternative direction, preclinical or literature follow-up on primary hereditary glaucoma (intraocular pressure effects of I1 / alpha-2 agonists)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

