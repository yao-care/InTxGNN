---
layout: default
title: Clarithromycin
parent: Model Prediction Only (L5)
nav_order: 190
evidence_level: L5
indication_count: 5
monitor_inn: "Clarithromycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility"]
last_modified_at: 2026-11-24
description: "Clarithromycin: predicted new indication hyperamylasemia (evidence level L5). In India: at least 20 listed products"
---

# Clarithromycin
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

## Clarithromycin: Macrolide antibiotic (bacterial protein synthesis inhibitor) → hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Clarithromycin is a macrolide antibiotic marketed in India in many tablet and oral liquid products.
The TxGNN model predicts it may be effective for **hyperamylasemia**, with a score of 0.9935.
No clinical trials are registered and only **1 publication** (a 2004 case report) was found, so the prediction rests almost entirely on the model.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | hyperamylasemia |
| TxGNN Prediction Score | 0.9935 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for clarithromycin: "Clarithromycin is a macrolide antimicrobial drug. […] Clarithromycin exerts its antibacterial action by binding to the 50S ribosomal subunit of susceptible bacteria resulting in inhibition of protein synthesis." ([DailyMed: clarithromycin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ba216276-b0bd-420a-9e0d-090bdfcc2460), label version 2026-11-12; accessed 2026-11-19.) Clarithromycin belongs to the macrolide class of antibiotics, which are generally known to inhibit bacterial protein synthesis and to have some anti-inflammatory and immunomodulatory activity.

No direct mechanistic link to hyperamylasemia has been established. The only retrieved publication (PMID 15228140, 2004) is a case report of *Mycobacterium abscessus* lung infection that coincided with primary macroamylasemia. Clarithromycin was most likely used there as an antimycobacterial agent, and the raised amylase is probably incidental or related to the underlying condition, not a treatment effect. The high score is a computational prediction without clinical corroboration, so this prediction should be treated as a hypothesis only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15228140](https://pubmed.ncbi.nlm.nih.gov/15228140/) | 2004 | Case report | Nihon Kokyuki Gakkai zasshi | Lung infection with *M. abscessus* in a 76-year-old man, complicated by primary macroamylasemia; no evidence that clarithromycin treats hyperamylasemia |

---

## India Market Information

At least 20 valid single-ingredient registrations were found, and the list may be partial. Approved indication text is not recorded for these records.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 34172 | Clarigard 500 Tablet | Strip of 10 tablets | Valid |
| 34479 | Crixan 125mg Granules | Bottle of 30 ml Powder for Oral Suspension | Valid |
| 36267 | Celex OD 500mg Tablet | Strip of 4 tablets | Valid |
| 37644 | Clarie 500mg Tablet | Strip of 10 tablets | Valid |
| 37986 | Claricin Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 38981 | Clarithro 250mg Tablet | Strip of 4 tablets | Valid |
| 39505 | Clarithro 500mg Tablet XR | Strip of 5 tablet xr | Valid |
| 39648 | Clarix 250mg Tablet | Strip of 10 tablets | Valid |
| 45283 | Clarigal 500mg Tablet | Strip of 4 tablets | Valid |
| 46720 | Clariford 250mg Tablet | Strip of 4 tablets | Valid |
| 47366 | Cth More 500mg Tablet | Strip of 10 tablets | Valid |
| 48478 | Claricin 250mg Tablet | Strip of 10 tablets | Valid |
| 49074 | Clarifix 500mg Tablet | Strip of 10 tablets | Valid |
| 53414 | Claripax 250mg Tablet | Strip of 10 tablets | Valid |
| 54444 | Clarinic Kid 125mg Tablet | Strip of 10 tablets | Valid |
| 117637 | Klear Dry Syrup | Bottle of 30 ml Dry Syrup | Valid |
| 120102 | Klazin Oral Suspension | Bottle of 30 ml Oral Suspension | Valid |
| 127041 | Laritova 500 Tablet | Strip of 4 tablets | Valid |
| 138725 | Mycitec 500 Tablet | Strip of 10 tablets | Valid |
| 199458 | Rithroxor 250mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: 822 interactions are recorded. Examples include:
  - Major: abemaciclib, fentanyl, acalabrutinib
  - Moderate: paclitaxel, tramadol, nifedipine, ethinylestradiol, hydrocortisone, afatinib
  - Minor: dolutegravir, zidovudine, loratadine
- Interactions with calcineurin inhibitors would be a particular concern in any transplant-related use.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. No trials exist, and the single case report does not show a treatment effect. No cited study directly tests clarithromycin for hyperamylasemia, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism-of-action data and a plausible biological link to amylase regulation
- Controlled or observational studies directly addressing hyperamylasemia
- Package insert warnings and contraindications from the India label
- A review of the interaction burden for the intended patient population

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: clarithromycin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ba216276-b0bd-420a-9e0d-090bdfcc2460) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

