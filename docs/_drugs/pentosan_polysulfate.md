---
layout: default
title: Pentosan Polysulfate
parent: Model Prediction Only (L5)
nav_order: 656
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
monitor_inn: "Pentosan polysulfate"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease"]
description: "Pentosan Polysulfate: predicted new indication Primary release disorder of platelets (evidence level L5). In India: 6 listed products (6 not discontinued)"
---

# Pentosan Polysulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Pentosan Polysulfate: Primary release disorder of platelets
{: .text-alpha }

## One-Sentence Summary

Pentosan polysulfate is a heparin-like sulfated polysaccharide, originally used to treat **interstitial cystitis**.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no clinical trials and no publications** currently support this prediction.
The prediction rests on the model score alone, and the available data point to a bleeding-risk concern rather than a therapeutic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (6 of 6) – CDSCO approval status is not included in this data |
| Number of Listed Products | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for pentosan polysulfate: "The mechanism of action of pentosan polysulfate sodium in interstitial cystitis is not known." ([DailyMed: Elmiron (pentosan polysulfate sodium) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f0ba651e-3d8a-11df-8fbe-119855d89593), label version 2024-09-18; accessed 2026-11-19.) Based on known information, pentosan polysulfate is a heparin-like sulfated polysaccharide with weak anticoagulant activity. It is established in interstitial cystitis, but no mechanism has been verified that would apply to a platelet disorder.

The connection to the new indication is weak. A platelet release (secretion) defect involves impaired granule release by platelets. A drug with anticoagulant properties would be expected to worsen, not improve, a bleeding tendency. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other two top predictions, Glanzmann thrombasthenia (0.9965) and pseudo-von Willebrand disease (0.9962), also have no supporting trials or literature. Pseudo-von Willebrand disease has a theoretical link, since sulfated polysaccharides can interact with VWF/GPIb binding. However, the direction of any effect is unknown and would need preclinical validation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 34200 | Cystopen Capsule | Strip of 10 capsules | Valid |
| 34943 | Comfora Capsule | Strip of 10 capsules | Valid |
| 36228 | Comfora Capsule | Bottle of 90 capsules | Valid |
| 84495 | For-IC Capsule | Strip of 10 capsules | Valid |
| 176373 | Pentossan 100 Capsule | Bottle of 90 capsules | Valid |
| 178096 | Pentossan 100 Capsule | Strip of 10 capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

All registrations are single-ingredient oral capsules and all are valid. The approved indication text is not available in the compiled data.

<!-- review:begin in-lic-20261124b-pentosan_polysulfate-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All six registrations are single-ingredient oral capsules and all are valid. A sixth registration (36228, Comfora Capsule, bottle of 90 capsules, Swati Spentose Pvt Ltd) is not shown in the table above." Revised: the sentence referred to the earlier table on this page, which showed only some of the products, and described other products as additional, further, remaining or not shown. The product table under India Market Information now lists every product held in the data, so that relative wording and the hard-coded counts were dropped; current figures are in the Quick Overview and that table. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124b-pentosan_polysulfate-1 -->

## Safety Considerations

- **Contraindications (from drug-disease associations in the knowledge graph, not label text)**: liver disease, gallbladder disease, thrombocytopenia, blood coagulation disease, hemophilia, heparin-induced thrombocytopenia.
- **Drug Interactions**: 58 interactions recorded. The 20 retrieved are all Moderate and mostly involve agents affecting coagulation or platelet function, which suggests additive bleeding risk. Examples:
  - Antiplatelet agents: acetylsalicylic acid, clopidogrel, cilostazol, dipyridamole, abciximab, cangrelor
  - Anticoagulants: warfarin, apixaban, edoxaban, betrixaban, dalteparin, bivalirudin, antithrombin III
  - Thrombolytics: alteplase, anistreplase
  - Others: defibrotide, caplacizumab, ibritumomab tiuxetan, tositumomab

The knowledge-graph contraindications (coagulation disorders, hemophilia, thrombocytopenia) overlap directly with the bleeding-related conditions proposed as new indications. Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5), with no trials or publications. The drug's anticoagulant properties and the contraindication signals for coagulation disorders make a benefit in a platelet release disorder mechanistically implausible and potentially harmful.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap for safety screening)
- Mechanism of action data (e.g., from DrugBank)
- Preclinical validation, such as platelet function and VWF/GPIb binding assays, particularly for pseudo-von Willebrand disease
- A review of whether the prediction only reflects similarities the TxGNN model (deep learning) learned between related diseases, not biological evidence, before any clinical consideration

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Elmiron (pentosan polysulfate sodium) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f0ba651e-3d8a-11df-8fbe-119855d89593) |
| 2026-11-24 | Revised: wording about the earlier partial table and hard-coded counts | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

