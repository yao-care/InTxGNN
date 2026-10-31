---
layout: default
title: Spironolactone
parent: Model Prediction Only (L5)
nav_order: 787
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
monitor_inn: "Spironolactone"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
description: "Spironolactone: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Not recorded in the local data"
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

Currently, detailed mechanism of action data is not available. Based on known information, spironolactone is an aldosterone-antagonist diuretic used in cardiovascular and endocrine conditions. Its efficacy there is established, but that does not directly carry over to a hair disorder.

One plausible but unverified link is spironolactone's anti-androgenic activity (androgen receptor blockade and reduced androgen synthesis). This is why it is used off-label in female pattern hair loss. However, hypotrichosis simplex is a rare hereditary hair loss disorder, linked to variants such as CDSN, APCDD1 and RPL21, and is not primarily androgen-driven. The mechanistic link is therefore weak and speculative.

The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The same caution applies even more strongly to congenital hypotrichosis milia, an ultra-rare condition more likely to have a genetic or developmental cause than a hormonal one.

## India Market Information

Showing 5 of 20 valid registrations (all single-ingredient category, oral tablets). No approved indication text is recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 58437 | Dytor Plus 20 Tablet | Strip of 15 tablets | Cipla Ltd |
| 217643 | Tortone 25mg/10mg Tablet | Strip of 10 tablets | Shrrishti Health Care Products Pvt Ltd |
| 220463 | Tor Plus 50mg/20mg Tablet | Strip of 10 tablets | Intas Pharmaceuticals Ltd |
| 3903 | Aldactone Plus 50mg/10mg Tablet | Strip of 10 tablets | RPG Life Sciences Ltd |
| 201693 | Spirix 25mg Tablet | Strip of 10 tablets | Psychocare Health Pvt Ltd |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

