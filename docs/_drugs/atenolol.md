---
layout: default
title: Atenolol
parent: Model Prediction Only (L5)
nav_order: 77
evidence_level: L5
indication_count: 5
monitor_inn: "Atenolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-11-24
description: "Atenolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension and myocardial infarction"
---

# Atenolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Atenolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Atenolol is a beta-1 selective blocker whose original uses recorded in the knowledge graph are hypertension and myocardial infarction.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**,
but **no clinical trials and no publications** directly studying this disease were found, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and myocardial infarction (relations recorded in the knowledge graph; the licence records contain no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for atenolol: "TENORMIN is a beta 1 -selective (cardioselective) beta-adrenergic receptor blocking agent without membrane stabilizing or intrinsic sympathomimetic (partial agonist) activities. This preferential effect is not absolute, however, and at higher doses, TENORMIN inhibits beta 2 -adrenoreceptors, chiefly located in the bronchial and vascular musculature." ([DailyMed: Tenormin (atenolol) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e850b1e-28a4-4ff8-8ed7-bb0b29faa28a), label version 2025-09-18; accessed 2026-11-19.) Based on general pharmacology, atenolol is a beta-1 selective blocker. It lowers blood pressure by reducing cardiac output and renin release.

Hypertension is a relation recorded in the knowledge graph for atenolol, and malignant hypertensive renal disease is kidney injury caused by severely elevated blood pressure. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Mechanistically, lowering blood pressure and renin release is biologically plausible for this condition.

However, malignant hypertension is usually managed with parenteral antihypertensives and renin-angiotensin system blockade. Nothing in the data compiled for this report supports a role for atenolol in this disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

For context, the other predicted indications drew only indirect literature. The pulmonary hypertension and chronic pulmonary heart disease searches returned mostly animal, mechanistic or general beta-blocker papers. These do not study atenolol in those diseases directly, and some findings conflict. For example, one rat study (PMID 8590992) reported reduced hypoxia-induced right heart hypertrophy with beta-blockade, while a rabbit study (PMID 6212672) found no such effect. Evidence for these diseases is therefore not strong enough to change the decision here.

---

## India Market Information

At least 20 atenolol registrations are valid, and the list may be partial. The records contain no approved-indication text.

<!-- review:begin in-lic-20261124c-atenolol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "At least 20 single-ingredient atenolol registrations are valid, and the list may be partial." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-atenolol-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 3862 | AT Tablet | Strip of 10 tablets | Valid |
| 6987 | Anten 50mg Tablet | Strip of 10 tablets | Valid |
| 12255 | Atavale 25mg Tablet | Strip of 10 tablets | Valid |
| 16571 | Atenil 100mg Tablet | Strip of 10 tablets | Valid |
| 20349 | Alinor 100mg Tablet | Strip of 10 tablets | Valid |
| 24002 | Atwa 50mg Tablet | Strip of 10 tablets | Valid |
| 26811 | Betanol 25mg Tablet | Strip of 10 tablets | Valid |
| 28378 | BP-Nol 100mg Tablet | Strip of 10 tablets | Valid |
| 54419 | Cadpres 100mg Tablet | Strip of 14 tablets | Valid |
| 105077 | Hyten 50mg Tablet | Strip of 10 tablets | Valid |
| 111448 | Indap AT 50 mg/1.25 mg Tablet | Strip of 10 tablets | Valid |
| 152855 | Nifetex TR 50mg/20mg Tablet | Strip of 10 tablets | Valid |
| 154189 | Novaten 50mg Tablet | Strip of 10 tablets | Valid |
| 156847 | NIFTENE 50MG/20MG TABLET | Strip of 10 tablets | Valid |
| 169344 | Olate 50mg Tablet | Strip of 10 tablets | Valid |
| 183953 | Quinoten 50mg Tablet | Strip of 14 tablets | Valid |
| 218444 | Tenil 50 Tablet | Strip of 10 tablets | Valid |
| 220767 | Tensimin 50mg Tablet | Strip of 14 tablets | Valid |
| 242876 | Winten 50mg Tablet | Strip of 14 tablets | Valid |
| 246870 | Ziblok 25 Tablet | Strip of 14 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Contraindication relations recorded in the knowledge graph (not label text):** liver failure, asthma (including intrinsic and allergic asthma), atrioventricular block, Raynaud disease, anaphylaxis, diabetes mellitus (types 1 and 2) and diabetic ketoacidosis, systemic lupus erythematosus, psoriasis, gout, pancreatitis, anuria, and several metabolic or mood disorders (anxiety, dysthymic and neurotic disorders, potassium deficiency, hypercalcaemia, nephrocalcinosis).
- **Drug Interactions:** 293 interactions are recorded. Examples at Moderate level include epinephrine, hydrocortisone, morphine, bupropion, atropine, calcium salts and several corticosteroids. Acetylsalicylic acid, aluminium hydroxide and attapulgite are Minor.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials or publications that directly study atenolol in malignant hypertensive renal disease, so the evidence level is L5. Standard care for this condition relies on other drug classes. The knowledge graph also records several contraindications relevant to patients with kidney or metabolic disease.

**To proceed, the following is needed:**
- Clinical or observational data on atenolol in malignant hypertension with renal involvement
- Mechanism of action data and package insert warnings and contraindications (not yet available)
- Comparison against current standard therapy for this condition
- A safety plan covering the contraindication signals and interactions listed above

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Tenormin (atenolol) prescribing information, Upsher-Smith Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6e850b1e-28a4-4ff8-8ed7-bb0b29faa28a) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

