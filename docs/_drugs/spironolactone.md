---
layout: default
title: Spironolactone
parent: Model Prediction Only (L5)
nav_order: 787
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Spironolactone"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
description: "Spironolactone: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). In India: at least 20 listed products"
---

# Spironolactone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Spironolactone: Hypotrichosis simplex of the scalp
{: .text-alpha }

## One-Sentence Summary

Spironolactone was originally used to treat hypertension, congestive heart failure and primary aldosteronism.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**,
but **no clinical trials or publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

A second prediction, **congenital hypotrichosis milia** (score 0.9904), is also evidence level L5 with a Hold recommendation.

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for spironolactone: "Spironolactone and its active metabolites are specific pharmacologic antagonists of aldosterone, acting primarily through competitive binding of receptors at the aldosterone-dependent sodium-potassium exchange site in the distal convoluted renal tubule. Spironolactone causes increased amounts of sodium and water to be excreted, while potassium is retained." ([DailyMed: Aldactone (spironolactone) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0fed2822-3a03-4b64-9857-c682fcd462bc), label version 2025-11-28; accessed 2026-11-19.) Based on known information, spironolactone is an aldosterone-antagonist diuretic used in cardiovascular and endocrine conditions. Its efficacy there is established, but that does not directly carry over to a hair disorder.

One plausible but unverified link is spironolactone's anti-androgenic activity (androgen receptor blockade and reduced androgen synthesis). This is why it is used off-label in female pattern hair loss. However, hypotrichosis simplex is a rare hereditary hair loss disorder, linked to variants such as CDSN, APCDD1 and RPL21, and is not primarily androgen-driven. The mechanistic link is therefore weak and speculative.

The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The same caution applies even more strongly to congenital hypotrichosis milia, an ultra-rare condition more likely to have a genetic or developmental cause than a hormonal one.

## India Market Information

No approved indication text is recorded for any of them.

<!-- review:begin in-lic-20261124-spironolactone-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Showing 5 of 20 valid registrations (all single-ingredient category, oral tablets). No approved indication text is recorded for any of them." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-spironolactone-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 3903 | Aldactone Plus 50mg/10mg Tablet | Strip of 10 tablets | Valid |
| 58437 | Dytor Plus 20 Tablet | Strip of 15 tablets | Valid |
| 201005 | Semitor Plus 50mg/20mg Tablet | Strip of 15 tablets | Valid |
| 201693 | Spirix 25mg Tablet | Strip of 10 tablets | Valid |
| 203695 | Silectone 25 Tablet | Strip of 10 tablets | Valid |
| 204333 | Spironot 25 Tablet | Strip of 10 tablets | Valid |
| 208836 | Spirom T 50mg/10mg Tablet | Strip of 10 tablets | Valid |
| 211631 | StayHappi Spironolactone+Torasemide 50mg/20mg Tablet | Strip of 10 tablets | Valid |
| 215041 | Torsid Plus 10/50 Tablet | Strip of 10 tablets | Valid |
| 215296 | Torsinex Plus Tablet | Strip of 10 tablets | Valid |
| 216550 | Tormax Plus LS 25mg/10mg Tablet | Strip of 10 tablets | Valid |
| 216674 | Tores Plus Tablet | Strip of 10 tablets | Valid |
| 217643 | Tortone 25mg/10mg Tablet | Strip of 10 tablets | Valid |
| 218118 | Torzest Plus 50mg/10mg Tablet | Strip of 10 tablets | Valid |
| 218949 | Toriflow S 50mg/10mg Tablet | Strip of 10 tablets | Valid |
| 219026 | Tornova Plus 50mg/10mg Tablet | Strip of 10 tablets | Valid |
| 219349 | Tormax Plus 50mg/5mg Tablet | Strip of 10 tablets | Valid |
| 220463 | Tor Plus 50mg/20mg Tablet | Strip of 10 tablets | Valid |
| 220833 | Torsinex Forte Tablet | Strip of 10 tablets | Valid |
| 227247 | Ticomide S 50mg/20mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications (from knowledge-graph drug-disease links, not label text):** kidney disease, anuria, pyoureter, pancreatitis, systemic lupus erythematosus (including paediatric), potassium deficiency, diabetes mellitus, diabetic ketoacidosis, hyperuricaemia, gout, hyperparathyroidism, osteitis fibrosa, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, hepatic coma, hepatic encephalopathy and neonatal jaundice.
- **Drug Interactions:** 272 interactions were identified in total. Among the 20 listed, the one **Major** interaction is with **loperamide**. **Moderate** interactions include:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
  - Antidiabetic agents: metformin, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, exenatide
  - Others: bupropion, morphine, bisacodyl, castor oil, dronabinol

  **Minor** interactions include doxycycline, acetylsalicylic acid and fidaxomicin.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for the full safety profile.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score, with no clinical trials or literature (evidence level L5). The proposed anti-androgen mechanism is weak for hereditary hypotrichosis, which is not mainly hormone-driven.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source, which are required before safety screening
- Mechanism of action data (for example from DrugBank) to test the proposed link to hair follicle biology
- Literature and trial searches, including case reports or genotype-specific data in hereditary hypotrichosis
- Assessment of whether a systemic anti-androgen and diuretic is appropriate for a rare genetic hair disorder, given the contraindications and interactions above, and whether a topical formulation could be considered

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Aldactone (spironolactone) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0fed2822-3a03-4b64-9857-c682fcd462bc) |
| 2026-11-24 | Removed: the sentence about the old table that called all products single-ingredient | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

