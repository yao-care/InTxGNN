---
layout: default
title: Zafirlukast
parent: Model Prediction Only (L5)
nav_order: 901
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "Zafirlukast"
predicted_indications: ["bronchitis"]
description: "Zafirlukast: predicted new indication Bronchitis (evidence level L5). In India: 1 listed product (1 not discontinued)"
---

# Zafirlukast
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

## Zafirlukast: Bronchitis
{: .text-alpha }

## One-Sentence Summary

Zafirlukast is a cysteinyl leukotriene receptor antagonist. The TxGNN model predicts it may be useful for **bronchitis**, but this rests on the model score alone: **no clinical trials** and **no publications** were found for this indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for zafirlukast: "Zafirlukast is a selective and competitive receptor antagonist of leukotriene D 4 and E 4 (LTD 4 and LTE 4 ), components of slow-reacting substance of anaphylaxis (SRSA). Cysteinyl leukotriene production and receptor occupation have been correlated with the pathophysiology of asthma, including airway edema, smooth muscle constriction, and altered cellular activity associated with the inflammatory process, which contribute to the signs and symptoms of asthma." ([DailyMed: zafirlukast prescribing information, American Health Packaging](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a60f39f6-d590-4b00-8751-7f12b7ec5385), label version 2024-10-11; accessed 2026-11-19.) Zafirlukast is known as a CysLT1 receptor antagonist. Cysteinyl leukotrienes contribute to airway inflammation, bronchoconstriction and mucus secretion, so a plausible mechanistic rationale exists for inflammatory bronchial conditions.

This reasoning remains hypothetical. Bronchitis is a heterogeneous condition (acute viral, chronic, eosinophilic), and the subtype the model refers to is not specified. The similarity to the drug's current use has not yet been assessed, and route compatibility is also pending.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 247909 | Zuvair 10mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

The product is a single-ingredient oral tablet and is currently valid.

## Safety Considerations

- **Drug Interactions**: 376 interacting drugs were identified. Moderate-level interactions include aprepitant, acetylsalicylic acid, metronidazole, budesonide (including nasal), saxagliptin, eliglustat, naltrexone, nateglinide, nitisinone, repaglinide, rosuvastatin, simvastatin and tinidazole. Sibutramine is rated minor. Pantoprazole, mesalazine, morphine, metformin and omeprazole have an unrated (unknown) level.

Package insert warnings and contraindications were not available. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for this prediction is the model score of 0.9993. There are no clinical trials or publications for bronchitis, so the evidence level is L5. The drug is marketed in India, but that does not support this new use.

**To proceed, the following is needed:**
- Clinical or observational evidence in a defined bronchitis subtype (e.g., chronic or eosinophilic)
- Mechanism of action data to support the link to bronchitis
- Package insert warnings and contraindications, to complete the safety review
- A review of the interacting drugs likely to be co-prescribed in this population

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: zafirlukast prescribing information, American Health Packaging](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=a60f39f6-d590-4b00-8751-7f12b7ec5385) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

