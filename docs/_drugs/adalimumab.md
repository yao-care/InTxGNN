---
layout: default
title: Adalimumab
parent: Model Prediction Only (L5)
nav_order: 25
evidence_level: L5
indication_count: 3
monitor_inn: "Adalimumab"
predicted_indications: ["hypermobility of coccyx", "Kummell disease", "vertebral disease"]
last_modified_at: 2026-11-24
description: "Adalimumab: predicted new indication hypermobility of coccyx (evidence level L5). In India: 15 listed products (15 not discontinued)"
---

# Adalimumab
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

## Adalimumab: TNF-alpha–blocking monoclonal antibody → hypermobility of coccyx
{: .text-alpha }

## One-Sentence Summary

Adalimumab is an anti-TNF-alpha monoclonal antibody used for several inflammatory and autoimmune conditions.
The TxGNN model predicts it may be effective for **hypermobility of coccyx**,
but there are **no clinical trials** and **no publications** directly studying this condition, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | hypermobility of coccyx |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (15 of 15) – CDSCO approval status is not included in this data |
| Number of Listed Products | 15 (valid: 15) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for adalimumab: "Adalimumab products bind specifically to TNF-alpha and block its interaction with the p55 and p75 cell surface TNF receptors. Adalimumab products also lyse surface TNF expressing cells in vitro in the presence of complement." ([DailyMed: Simlandi (adalimumab-ryvk) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12f609c9-2088-bb05-e063-6394a90a9ecc), label version 2026-11-11; accessed 2026-11-19.) Adalimumab is known as a TNF-alpha inhibitor, and its action in inflammatory conditions is driven by blocking this cytokine.

Coccygeal hypermobility is generally a mechanical or traumatic condition, not a TNF-driven inflammatory one. The mechanistic rationale is therefore weak. The high score may reflect the condition's proximity to spondyloarthropathy-related disease nodes in the model's training data rather than a true pharmacological link. Without direct studies, this prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for hypermobility of coccyx.

## India Market Information

Adalimumab is marketed in India under 15 valid single-ingredient licences, all injectable (vials and prefilled syringes). The licence records carry no indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 839 | Adalipca 40mg Injection | Vial of 1 Injection | Valid |
| 962 | Adfrar Injection | Prefilled syringe of 1 Injection | Valid |
| 1845 | Adlumab 40mg Injection | Vial of 0.8 ml Injection | Valid |
| 2395 | Adalirel 40mg Injection | Vial of 1 Injection | Valid |
| 4182 | Adalimac 40mg Injection | Prefilled syringe of 0.8 ml Injection | Valid |
| 5948 | Admira 40mg/0.8ml Injection | Vial of 1 Injection | Valid |
| 8950 | Adalirel 20mg Injection | Vial of 0.4 ml Injection | Valid |
| 10487 | Amab Injection | Prefilled syringe of 0.8 ml Injection | Valid |
| 36414 | Cipleumab 40mg Injection | Prefilled syringe of 0.8 ml Injection | Valid |
| 72488 | Exemptia 40mg/0.8ml Injection | Prefilled syringe of 1 Injection | Valid |
| 74060 | Exemptia 20mg/0.4ml Injection | Prefilled syringe of 1 ml Injection | Valid |
| 76391 | Envira 40mg Injection | Vial of 0.8 ml Injection | Valid |
| 134542 | Mabura 40mg Injection | Vial of 1 ml Injection | Valid |
| 136100 | Mabvinra 40mg Injection | Vial of 1 Injection | Valid |
| 174104 | Plamumab 40mg Injection | Vial of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 353 interactions were identified in the interaction screening. The main ones are:
  - **Major**: corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone, prednisolone, prednisone, triamcinolone), deferiprone, and radiopharmaceutical or radioimmunotherapy agents (ibritumomab tiuxetan, iobenguane I-131, tositumomab and tositumomab I-131).
  - **Moderate**: metronidazole, tinidazole, rosuvastatin, simvastatin.
  - **Minor**: zinc salts (acetate, gluconate, sulfate).

Please refer to the package insert for warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score (0.9977) but no clinical trials or publications, and the condition is mechanical rather than TNF-driven. The evidence level is L5, so there is no basis to proceed.

**To proceed, the following is needed:**
- Any direct clinical or preclinical evidence linking TNF blockade to coccygeal hypermobility
- Mechanism of action data for adalimumab
- Package insert warnings and contraindications from the India licence holders
- A clearer biological rationale, for example whether an inflammatory component exists in the target population

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Simlandi (adalimumab-ryvk) prescribing information, Teva Pharmaceuticals USA, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12f609c9-2088-bb05-e063-6394a90a9ecc) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

