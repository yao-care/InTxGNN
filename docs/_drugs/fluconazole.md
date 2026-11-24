---
layout: default
title: Fluconazole
parent: Model Prediction Only (L5)
nav_order: 358
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Fluconazole: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Oral candidiasis, candidiasis, vulvovaginal candidiasis…"
monitor_inn: "Fluconazole"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
---

# Fluconazole
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

## Fluconazole: From Candidiasis to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Fluconazole is an azole antifungal originally used to treat candidiasis (oral, oesophageal, vulvovaginal, and invasive forms) and cryptococcal meningitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Oral candidiasis, candidiasis, vulvovaginal candidiasis, oesophageal candidiasis, cryptococcal meningitis, candidaemia, disseminated candidiasis |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9924 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for fluconazole: "Fluconazole is a highly selective inhibitor of fungal cytochrome P450 dependent enzyme lanosterol 14-α-demethylase. This enzyme functions to convert lanosterol to ergosterol. The subsequent loss of normal sterols correlates with the accumulation of 14-α-methyl sterols in fungi and may be responsible for the fungistatic activity of fluconazole." ([DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204), label version 2026-04-02; accessed 2026-11-19.) Based on known information, fluconazole is an azole antifungal that inhibits fungal CYP51 (lanosterol 14-alpha-demethylase) and blocks ergosterol synthesis. Its efficacy in superficial and invasive fungal infections is established.

The link to the new indication is weak. Punctate epithelial keratoconjunctivitis is most often viral (for example adenovirus) or related to dry eye, drug toxicity, or other non-fungal causes. An antifungal mechanism therefore has no clear connection to the typical cause. A plausible link would exist only for a fungal subset of keratoconjunctivitis, and the supplied data do not support that.

The high score (0.9924) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction should be regarded as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Fluconazole is marketed in India with 20 valid registrations and no cancelled ones. The approved indication text is not available for these registrations.

<!-- review:begin in-lic-20261124c-fluconazole-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Fluconazole is marketed in India with 20 valid single-ingredient registrations and no cancelled ones." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-fluconazole-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 9497 | Antol 150mg Tablet | Strip of 10 tablets | Valid |
| 19436 | Abiflu 200 Tablet | Strip of 2 tablets | Valid |
| 39101 | Cozen 150mg Tablet | Strip of 1 Tablet | Valid |
| 40824 | Canfree 150mg Tablet | Strip of 1 Tablet | Valid |
| 84553 | Flumet 400mg Tablet | Strip of 1 Tablet | Valid |
| 85136 | Fungiset 200 Tablet | Strip of 1 Tablet | Valid |
| 85629 | Flufung 150 Tablet | Strip of 4 tablets | Valid |
| 86781 | Fredluco 150 Tablet | Strip of 1 Tablet | Valid |
| 87089 | FZN 150mg Tablet | Strip of 1 Tablet | Valid |
| 87432 | Flow 150mg Capsule | Strip of 1 Capsule | Valid |
| 87481 | Flucowin Tablet | Strip of 1 Tablet | Valid |
| 89362 | Flucar 200 Capsule | Strip of 4 capsules | Valid |
| 90568 | Fiscon Kit | Box of 1 Kit | Valid |
| 91124 | Fungisanf 150mg Tablet | Strip of 10 tablets | Valid |
| 91225 | Flubri 150mg Tablet | Strip of 5 tablets | Valid |
| 91489 | Flucotrap 150mg Tablet | Strip of 2 tablets | Valid |
| 91989 | Flunem 150mg Tablet | Strip of 1 Tablet | Valid |
| 94167 | Flucojon 200mg Tablet | Strip of 2 tablets | Valid |
| 146110 | M Fluk 150mg Tablet | Strip of 10 tablets | Valid |
| 234535 | V Can 150mg Capsule | Strip of 1 Capsule | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All listed forms are oral (capsules and tablets). No topical or ophthalmic fluconazole product appears among the registrations, so route compatibility with an eye indication would need to be assessed separately.

## Safety Considerations

- **Contraindications (from knowledge graph, not label text)**: Long QT syndrome, familial long QT syndrome, kidney disease, pyoureter, liver disease, gallbladder disease.
- **Drug Interactions**: 783 interactions were recorded. Examples:
  - **Major**: Chlorpropamide.
  - **Moderate**: Famotidine, rabeprazole, omeprazole, dexlansoprazole, hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, loperamide, aprepitant, saxagliptin, bisacodyl.
  - **Minor**: Amphotericin B, clarithromycin.

Please refer to the package insert for warnings and label contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no clinical trials or literature. The antifungal mechanism does not fit the usual non-fungal causes of this condition, and no ophthalmic fluconazole product is registered in India.

**To proceed, the following is needed:**
- Mechanism of action data and a clearer mechanistic rationale for the proposed indication
- Literature and trial searches for fluconazole in fungal keratitis or keratoconjunctivitis, to find any supporting subset
- Package insert warnings and contraindications from the India regulatory source, since the safety screen cannot proceed without them
- Assessment of route and formulation (oral versus ophthalmic) for an ocular use
- Review of the knowledge-graph contraindications (QT prolongation, renal and hepatic disease) against a possible ocular use

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Diflucan (fluconazole) prescribing information, Roerig](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f694c617-3383-416c-91b6-b94fda371204) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

