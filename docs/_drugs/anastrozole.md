---
layout: default
title: Anastrozole
parent: Model Prediction Only (L5)
nav_order: 60
evidence_level: L5
indication_count: 5
monitor_inn: "Anastrozole"
predicted_indications: ["neuroblastoma", "vertebral anomalies and variable endocrine and T-cell dysfunction", "ganglioneuroblastoma (disease)", "retroperitoneal neoplasm", "monocytic leukemia"]
last_modified_at: 2026-11-24
description: "Anastrozole: predicted new indication neuroblastoma (evidence level L5). In India: at least 20 listed products"
---

# Anastrozole
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

## Anastrozole: aromatase inhibitor → neuroblastoma
{: .text-alpha }

## One-Sentence Summary

Anastrozole is an aromatase inhibitor that lowers oestrogen production. The TxGNN model predicts it may be relevant to **neuroblastoma**, with a score of 0.9953. No clinical trials or publications currently study this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | neuroblastoma |
| TxGNN Prediction Score | 0.9953 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for anastrozole: "The growth of many cancers of the breast is stimulated or maintained by estrogens. In postmenopausal women, estrogens are mainly derived from the action of the aromatase enzyme, which converts adrenal androgens (primarily androstenedione and testosterone) to estrone and estradiol. […] Anastrozole is a selective non-steroidal aromatase inhibitor." ([DailyMed: Arimidex (anastrozole) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=acbfaaa9-503c-4691-9828-76a7146ed6de), label version 2026-03-02; accessed 2026-11-19.) Anastrozole is known as an aromatase inhibitor, a class that blocks the conversion of androgens to oestrogens. Whether this action has any bearing on neuroblastoma is not established.

The data compiled for this report found no established rationale linking aromatase inhibition to neuroblastoma biology. The high score is a model output and has not been checked against clinical or laboratory findings. It should be treated as a hypothesis to test, not as a supported repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 1309 | Arimidex 1mg Tablet | Box of 28 tablets | Valid |
| 2085 | ANAZOL 1 MG TABLET | Strip of 10 tablets | Valid |
| 5298 | Anaday Tablet | Strip of 10 tablets | Valid |
| 6826 | Atraz 1mg Tablet | Strip of 10 tablets | Valid |
| 7698 | Anastronat 1mg Tablet | Strip of 30 tablets | Valid |
| 8228 | Aritoz Tablet | Strip of 14 tablets | Valid |
| 8823 | Astronex 1mg Tablet | Strip of 5 tablets | Valid |
| 9858 | Avantaz Tablet | Strip of 14 tablets | Valid |
| 10268 | Anastar 1mg Tablet | Strip of 1 Tablet | Valid |
| 11427 | Alstar 1mg Tablet | Strip of 10 tablets | Valid |
| 14122 | Altrol 1mg Tablet | Strip of 14 tablets | Valid |
| 17086 | Anaglob 1mg Tablet | Strip of 14 tablets | Valid |
| 17094 | Anastrocare 1mg Tablet | Strip of 10 tablets | Valid |
| 28349 | Brestozol Tablet | Strip of 10 tablets | Valid |
| 73489 | Elinal Tablet | Strip of 10 tablets | Valid |
| 78860 | Egsure 1mg Tablet | Strip of 5 tablets | Valid |
| 85047 | Femitraz Tablet | Strip of 10 tablets | Valid |
| 129672 | Lilmantro 1mg Tablet | Strip of 10 tablets | Valid |
| 201544 | Stazonex Tablet | Strip of 10 tablets | Valid |
| 224544 | Trazocad 1mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

The list shows 5 of the licences compiled for this report and may be partial. All the licences listed are valid single-ingredient products.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal therapy (aromatase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Disease-related cautions**: The data compiled for this report flag myocardial ischemia and coronary artery disease as conditions of concern. These come from relation data, not from label text.
- **Drug Interactions**: 147 potential interactions were recorded, none with a graded severity level (all "Unknown"). Examples include bupropion, pantoprazole, glimepiride, morphine, metformin, omeprazole, simvastatin, prednisone and acetylsalicylic acid.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. No trials or publications address neuroblastoma, and no mechanistic link to aromatase inhibition has been identified. The evidence level is L5.

**To proceed, the following is needed:**
- A mechanistic rationale connecting aromatase inhibition (or anastrozole specifically) to neuroblastoma biology
- Preclinical studies in neuroblastoma models
- Mechanism of action data for anastrozole
- Package insert warnings and contraindications, and graded severity for the recorded interactions
- A safety review for the paediatric population, since neuroblastoma mainly affects children

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Arimidex (anastrozole) prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=acbfaaa9-503c-4691-9828-76a7146ed6de) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

