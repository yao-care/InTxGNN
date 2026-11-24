---
layout: default
title: Ebastine
parent: Model Prediction Only (L5)
nav_order: 296
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Ebastine: predicted new indication Coronary artery disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, idiopathic urticaria"
monitor_inn: "Ebastine"
predicted_indications: ["coronary artery disease", "myocardial ischemia"]
---

# Ebastine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Ebastine: From Allergic Rhinitis to Coronary Artery Disease
{: .text-alpha }

## One-Sentence Summary

Ebastine is a second-generation H1-antihistamine, originally used for allergic rhinitis, vasomotor rhinitis and idiopathic urticaria.
The TxGNN model predicts it may be effective for **coronary artery disease**,
but there are currently **no clinical trials** and **no publications** supporting this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, idiopathic urticaria |
| Predicted New Indication | Coronary artery disease |
| TxGNN Prediction Score | 0.9918 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of ebastine as: Histamine H1 receptor inverse agonist ([ChEMBL CHEMBL305660 (ebastine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL305660), CC BY-SA 3.0; accessed 2026-11-19.) Based on known information, ebastine belongs to the class of second-generation H1-antihistamines. Its efficacy in allergic rhinitis and urticaria is established, and a speculative mechanistic link to coronary artery disease may exist through histamine and mast cell signalling in atherosclerosis and coronary vasospasm.

This link is not supported by any trial or publication in the data compiled for this report. The high TxGNN score (0.9918) is a computational prediction only and should not be read as evidence of efficacy.

Other predictions for ebastine, such as myocardial ischemia, also have no clinical support. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction (coronary artery disease).

## India Market Information

Ebastine is marketed in India with 20 valid single-ingredient registrations and no cancelled ones. The compiled data do not include approved indication text for these products.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 31358 | Belay Tablet | Strip of 10 tablets | Valid |
| 72774 | Ebast Suspension | Bottle of 60 ml Suspension | Valid |
| 74955 | Ebast 5mg Tablet DT | Strip of 10 tablet dt | Valid |
| 75380 | Eba P 10mg/10mg Tablet | Strip of 10 tablets | Valid |
| 76423 | Ebaler 10mg Tablet | Strip of 10 tablets | Valid |
| 76439 | Ebstic 10 Tablet | Strip of 10 tablets | Valid |
| 77362 | Eebia P 10mg/10mg Tablet | Strip of 10 tablets | Valid |
| 77831 | Ebaway-P Tablet | Strip of 10 tablets | Valid |
| 78667 | Ebazide 10mg Tablet | Strip of 10 tablets | Valid |
| 78669 | Ebanit 20mg Tablet | Strip of 10 tablets | Valid |
| 79673 | Elestin 20mg Tablet | Strip of 10 tablets | Valid |
| 79818 | Ebagud 10 Tablet | Strip of 10 tablets | Valid |
| 80214 | Estifen 20mg Tablet | Strip of 10 tablets | Valid |
| 80516 | Ebahist 10mg Tablet | Strip of 10 tablets | Valid |
| 80540 | Estifen 10mg Tablet | Strip of 10 tablets | Valid |
| 81024 | Elbast 20mg Tablet | Strip of 10 tablets | Valid |
| 81837 | Ebram M 10mg/10mg Tablet | Strip of 10 tablets | Valid |
| 82445 | Ebagail 20mg Tablet | Strip of 10 tablets | Valid |
| 117714 | Kestil 10mg Tablet | Strip of 10 tablets | Valid |
| 232970 | Ufibast 20mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

Please refer to the package insert for safety information.

Note: ebastine's drug class has a history of QT-related concerns (for example terfenadine), although ebastine's own risk is considered low at standard doses. This matters if the drug is considered for patients with cardiac disease.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for coronary artery disease is supported only by the TxGNN model score, with no clinical trials or publications. Safety data from the package insert are also missing, and cardiac safety in a coronary population would need specific attention.

**To proceed, the following is needed:**
- Mechanism of action data for ebastine
- Preclinical or mechanistic studies linking histamine/H1 signalling to coronary disease
- Package insert warnings and contraindications from India
- Cardiac safety assessment, including QT effects
- Any observational or clinical data on ebastine in cardiovascular outcomes

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL305660 (ebastine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL305660) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

