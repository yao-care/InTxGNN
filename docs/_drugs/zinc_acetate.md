---
layout: default
title: Zinc Acetate
parent: Model Prediction Only (L5)
nav_order: 904
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Zinc acetate"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "bronchitis", "diabetic retinopathy", "acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "acne keloid", "hydroa vacciniforme, familial", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis", "urinary tract infection (disease)"]
description: "Zinc Acetate: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). In India: 8 listed products (8 not discontinued)"
---

# Zinc Acetate
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

## Zinc Acetate: Severe nonproliferative diabetic retinopathy
{: .text-alpha }

## One-Sentence Summary

Zinc acetate is a zinc salt originally used for conditions such as Wilson disease, dermatitis, burns and iron metabolism disorders.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**,
but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (8 of 8) – CDSCO approval status is not included in this data |
| Number of Listed Products | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for zinc acetate: "Zinc is an essential trace element. Zinc functions as a cofactor of various enzymes including DNA polymerases, RNA polymerases, alcohol dehydrogenase, and alkaline phosphatases. Zinc is a coordinator of protein structural folding, such as folding of “Zinc finger” motif that interacts with a variety of proteins, lipids, and nucleic acids." ([DailyMed: zinc sulfate prescribing information, Camber Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49698d00-f44b-4b1f-ae34-6b9067911757), label version 2026-03-04; accessed 2026-11-19.) Based on known information, zinc acetate is a zinc salt used in Wilson disease and in several skin and wound conditions, and mechanistically it may be applicable to diabetic retinopathy.

A plausible but unproven link is zinc's role as a cofactor for antioxidant enzymes such as Cu/Zn-superoxide dismutase. Through this role it may influence oxidative stress and inflammation in the retina. Zinc is also involved in glucose metabolism and microvascular health, which is relevant to diabetic eye disease.

These links are hypotheses only. Nothing in the data compiled for this report confirms them. The same model also ranks the broader term "diabetic retinopathy" highly (score 0.9992), which is consistent with the first prediction but is not independent evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 6636 | Actozinc Syrup | Bottle of 100 ml Oral Solution | Valid |
| 47176 | Coverdoz 50mg/100mg/12mg Kit | Box of 1 Kit | Valid |
| 105716 | HI ZN Syrup | Bottle of 60 ml Syrup | Valid |
| 109846 | Imuzinc Syrup | Bottle of 100 ml Syrup | Valid |
| 246747 | Ziverdo Kit | Box of 1 Kit | Valid |
| 247671 | Zincovec 50 Tablet | Strip of 10 tablets | Valid |
| 248054 | Zia Syrup | Bottle of 100 ml Syrup | Valid |
| 250704 | Zia Syrup | Bottle of 50 ml Syrup | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

All registrations are valid products, and none is cancelled.

<!-- review:begin in-lic-20261106-zinc_acetate-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All 8 registrations are valid single-ingredient products, and none is cancelled." Removed: it described the products as single-ingredient or combination products in a way that did not match the Indian medicine data (the Indian Medicine Dataset as of 2026-11-06). Revised 2026-11-24: the hard-coded number of records and the wording about the old table were dropped; the Quick Overview and the product table under India Market Information show the current figures. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261106-zinc_acetate-1 -->

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: The knowledge graph links zinc acetate to inherited porphyria, porphyrin metabolism disease and porphyria as contraindicated conditions.
- **Drug Interactions**: The interaction screen returned 100 records, and the 20 reviewed show mostly minor interactions. Moderate-level interactions were noted with:
  - Alendronic acid
  - Risedronic acid
  - Ibandronate
  - Tetracycline
  - Baloxavir marboxil

  Minor interactions include several corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone) and immunosuppressive or biologic agents (abatacept, adalimumab, azathioprine, among others).

Please refer to the package insert for further safety information, including warnings.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials or publications for diabetic retinopathy, so the evidence level is L5 (model prediction only). The mechanism of action is also not available, and the package insert safety data has not been obtained.

**To proceed, the following is needed:**
- Mechanism of action data for zinc acetate (e.g., from DrugBank)
- Package insert warnings and contraindications from the India regulatory records, which are required before any safety screening
- A systematic literature search on zinc and diabetic retinopathy, including preclinical and observational studies
- A check of clinical trial registries for zinc in diabetic retinopathy
- Assessment of route and formulation suitability for retinal disease, since the marketed forms are oral tablets, syrups and kits
- Review of the porphyria contraindication signal and of interactions with chelation-sensitive drugs (bisphosphonates, tetracycline)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient" | Corrected (revised 2026-11-24; earlier version kept in the record) | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: zinc sulfate prescribing information, Camber Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49698d00-f44b-4b1f-ae34-6b9067911757) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

