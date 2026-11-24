---
layout: default
title: Etodolac
parent: Model Prediction Only (L5)
nav_order: 330
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "Etodolac"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "hypermobility of coccyx"]
description: "Etodolac: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). In India: at least 20 listed products"
---

# Etodolac
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

## Etodolac: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Etodolac is a nonsteroidal anti-inflammatory drug (NSAID), originally used for rheumatoid arthritis, osteoarthritis and related joint disorders.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare inherited skeletal disorder.
This prediction has **0 clinical trials** and **0 publications** behind it, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for etodolac: "The mechanism of action of etodolac extended-release tablets, like that of other NSAIDs, is not completely understood, but may be related to prostaglandin synthetase inhibition." ([DailyMed: Etodolac Er (etodolac) prescribing information, Advanced Rx Pharmacy of Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=baebdfb2-17f6-9081-e053-2a95a90ab331), label version 2024-12-31; accessed 2026-11-19.) It is known to be an NSAID that inhibits cyclooxygenase (COX), with a preferential effect on COX-2. This reduces prostaglandin-driven inflammation and pain in joint disease.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare skeletal dysplasia caused by mutations in the CDMP1/GDF5 gene. The defect lies in growth-factor signalling during bone and cartilage development. Etodolac's COX inhibition does not act on this pathway, and no plausible mechanistic link is evident.

The high score (0.9997) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At best, an NSAID might relieve joint pain symptomatically. It would not be expected to change the underlying developmental defect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Etodolac has 20 valid registrations in India. Several products combine etodolac with other actives such as thiocolchicoside, paracetamol or tramadol. The licence records contain no approved-indication text. Five main plain-etodolac products are shown below.

<!-- review:begin in-lic-20261124-etodolac-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Etodolac has 20 valid registrations in India, all single-entity listings." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-etodolac-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 72040 | Dolanox P 400mg/325mg Tablet | Strip of 10 tablets | Valid |
| 72346 | Etova 400 Tablet | Strip of 10 tablets | Valid |
| 72861 | Etornext-ER Tablet | Strip of 10 tablet er | Valid |
| 73022 | Etova 200 Tablet | Strip of 10 tablets | Valid |
| 73477 | Etosafe ER Tablet | Strip of 10 tablet er | Valid |
| 75403 | Etogesic MR 400mg/8mg Tablet | Strip of 10 tablets | Valid |
| 75459 | Edonix 600mg Tablet ER | Strip of 10 tablet er | Valid |
| 77181 | Etomight 400mg Tablet ER | Strip of 10 tablet er | Valid |
| 77392 | Edothi-ER 400 Tablet | Strip of 10 tablet er | Valid |
| 78268 | Etoteem TH 400mg/4mg Tablet | Strip of 10 tablets | Valid |
| 79035 | Etodenz-XT Tablet | Strip of 10 tablets | Valid |
| 80095 | Etulac 400mg Tablet ER | Strip of 10 tablet er | Valid |
| 80925 | Etoteem 400mg Tablet | Strip of 10 tablets | Valid |
| 81108 | Epolis P 400mg/325mg Tablet | Strip of 10 tablets | Valid |
| 81431 | Etoswift 400mg Tablet ER | Strip of 10 tablet er | Valid |
| 91885 | Fiendoc TH 400mg/4mg Tablet | Strip of 10 tablets | Valid |
| 119214 | Kandolac 400mg/4mg Tablet MR | Strip of 10 tablet mr | Valid |
| 139968 | Megtios TH 400mg/4mg Tablet | Strip of 10 tablets | Valid |
| 227289 | Tomoltif 300mg/325mg Tablet | Strip of 10 tablets | Valid |
| 227628 | Telor ED 400mg/325mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All products are oral formulations.

---

## Safety Considerations

- **Disease-level contraindication signals** (from the knowledge graph, not package insert text): hypertension and hypertensive disorders, kidney disease, liver disease, gallbladder disease, peptic ulcer disease (including active ulcer), blood coagulation disease, myocardial infarction and coronary thrombosis, hemoglobinopathy, and cardiovascular and heart disease.
- **Drug Interactions**: 221 interactions were identified in total. Those listed below are a sample of 20, and most carry a Moderate rating.
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide (Moderate)
  - Acetylsalicylic acid (Moderate)
  - Mesalazine and balsalazide (Moderate)
  - Metformin, glimepiride, chlorpropamide, repaglinide (Moderate)
  - Potassium citrate and potassium bicarbonate (Moderate)
  - Picosulfuric acid and polyethylene glycol with electrolytes (Moderate)
  - Famotidine, ranitidine, cimetidine, linaclotide (Minor)

Please refer to the package insert for the full set of warnings.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or publications behind it. The target is a genetic developmental disorder, and etodolac's COX-inhibiting mechanism has no apparent link to the GDF5 signalling defect. The score is likely a network-proximity artefact.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence linking etodolac to GDF5-related skeletal dysplasia
- Detailed mechanism-of-action data for etodolac
- Package insert warnings and contraindications from the India regulatory source
- A clear case that symptomatic NSAID use would help this rare population, with cardiovascular, gastrointestinal and renal risks assessed

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Indian medicine data (the Indian Medicine Dataset used by this site). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for etodolac is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Etodolac Er (etodolac) prescribing information, Advanced Rx Pharmacy of Tennessee, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=baebdfb2-17f6-9081-e053-2a95a90ab331) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

