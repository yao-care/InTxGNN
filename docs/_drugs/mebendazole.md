---
layout: default
title: Mebendazole
parent: Model Prediction Only (L5)
nav_order: 516
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Mebendazole"
predicted_indications: ["acne (disease)"]
description: "Mebendazole: predicted new indication Acne (disease) (evidence level L5). In India: at least 20 listed products"
---

# Mebendazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Mebendazole: Acne (disease)
{: .text-alpha }

## One-Sentence Summary

Mebendazole is an anthelmintic (anti-worm) drug, originally used for intestinal worm infections such as pinworm (enterobiasis), roundworm (ascariasis) and whipworm (trichuriasis).
The TxGNN model predicts it may be effective for **acne**, but the data compiled for this report contain **no clinical trials** and **only 1 publication**, an unrelated case report, so the prediction is essentially unsupported.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 0.9920 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for mebendazole: "Mebendazole, a benzimidazole, is an anthelmintic. […] Mebendazole interferes with cellular tubulin formation in the helminth and causes ultrastructural degenerative changes in its intestine. As a result, its glucose uptake and the digestive and reproductive functions are disrupted, leading to immobilization, inhibition of egg production and death of the helminth." ([DailyMed: Vermox (mebendazole) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a720c424-517a-461b-8e13-6c37caf8aa3f), label version 2021-10-05; accessed 2026-11-19.) Based on general knowledge, mebendazole is a benzimidazole anthelmintic that is understood to bind parasite tubulin, disrupting microtubule-dependent processes such as glucose uptake. This is well established for intestinal worm infections.

That mechanism does not map onto acne. Acne is driven by excess sebum, follicular blockage, *Cutibacterium acnes* and inflammation, and none of these is a recognised target of tubulin-binding anthelmintics. The high TxGNN score (0.9920) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The only retrieved publication is an unrelated parasitic case report that mentions acne-like skin lesions, which looks like a spurious match.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7072899](https://pubmed.ncbi.nlm.nih.gov/7072899/) | 1982 | Case report (unrelated condition) | The American Journal of Tropical Medicine and Hygiene | Report of human proliferative sparganosis in Venezuela. The patient had acne-like skin lesions as a symptom of the parasitic infection, which does not support mebendazole as an acne treatment. |

---

## India Market Information

There are 20 valid single-ingredient registrations. The registration data supplied no approved-indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 18317 | Acavom 100mg Tablet | Strip of 6 tablets | Valid |
| 60290 | D Worm Tablet | Strip of 1 Tablet | Valid |
| 78136 | Emzol 100mg Suspension | Bottle of 30 ml Suspension | Valid |
| 105930 | H R T 100mg Tablet | Strip of 10 tablets | Valid |
| 123391 | Levasol M 100 mg/150 mg Tablet | Strip of 1 Tablet | Valid |
| 124960 | Levasol M Syrup | Bottle of 10 ml Syrup | Valid |
| 134860 | Mebex 500mg Tablet | Strip of 1 Tablet | Valid |
| 136436 | Min Min 100mg Tablet | Strip of 10 tablets | Valid |
| 136932 | Mebenth 100mg Tablet | Strip of 6 tablets | Valid |
| 137205 | Mabel 100mg Tablet | Strip of 6 tablets | Valid |
| 138278 | Mebidex 100mg Tablet | Strip of 6 tablets | Valid |
| 140115 | Mex 100mg Tablet | Strip of 10 tablets | Valid |
| 153261 | Nuzole 100mg Tablet | Strip of 6 tablets | Valid |
| 185356 | Raid 100mg/150mg Tablet | Strip of 1 Tablet | Valid |
| 193683 | Raid Suspension | Bottle of 10 ml Suspension | Valid |
| 202221 | StayHappi Mebendazole 100mg Tablet | Strip of 6 tablets | Valid |
| 202362 | Sta 500mg Tablet | Strip of 1 Tablet | Valid |
| 206648 | Sandin 100mg Tablet | Strip of 6 tablets | Valid |
| 241478 | Wormin 100mg Tablet | Strip of 6 tablets | Valid |
| 242781 | W Ban Suspension | Bottle of 30 ml Suspension | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: liver disease and gallbladder disease.
- **Drug Interactions (10 recorded)**:
  - Moderate: metronidazole, iodide I-131, iodide I-123, phenobarbital, carbamazepine, ritonavir, fosphenytoin, phenytoin, primidone.
  - Minor: cimetidine.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials, the single retrieved publication is irrelevant to acne, and there is no plausible mechanistic link between mebendazole and acne pathophysiology.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence that mebendazole affects acne-relevant pathways (sebum production, *C. acnes*, inflammation)
- Detailed mechanism of action data
- Package insert warnings and contraindications from the India registrations
- Route and formulation assessment (the current products are oral or suspension forms)

**Other predictions in the same data set (for reference):**
- Support comes from observational studies, reviews and the WHO guideline. Benzimidazoles, mainly albendazole with mebendazole as an alternative, are already standard antiparasitic therapy, so these are existing-use confirmations rather than new repurposing. Long-term use requires liver function and blood count monitoring.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data are not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Vermox (mebendazole) prescribing information, Janssen Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a720c424-517a-461b-8e13-6c37caf8aa3f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

