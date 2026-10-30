---
layout: default
title: Fluconazole
parent: Model Prediction Only (L5)
nav_order: 358
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
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
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, fluconazole is an azole antifungal that inhibits fungal CYP51 (lanosterol 14-alpha-demethylase) and blocks ergosterol synthesis. Its efficacy in superficial and invasive fungal infections is established.

The link to the new indication is weak. Punctate epithelial keratoconjunctivitis is most often viral (for example adenovirus) or related to dry eye, drug toxicity, or other non-fungal causes. An antifungal mechanism therefore has no clear connection to the typical cause. A plausible link would exist only for a fungal subset of keratoconjunctivitis, and the supplied data do not support that.

The high score (0.9924) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction should be regarded as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Fluconazole is marketed in India with 20 valid single-ingredient registrations and no cancelled ones. The approved indication text is not available for these registrations. The main authorizations are:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 234535 | V Can 150mg Capsule | Strip of 1 capsule | Pegasus Farmaco India Pvt Ltd |
| 87481 | Flucowin Tablet | Strip of 1 tablet | Makers Laboratories Ltd |
| 146110 | M Fluk 150mg Tablet | Strip of 10 tablets | Madhav Biotech Pvt. Ltd |
| 89362 | Flucar 200 Capsule | Strip of 4 capsules | Cartel Laboratories |
| 39101 | Cozen 150mg Tablet | Strip of 1 tablet | Zenith Healthcare Ltd |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

