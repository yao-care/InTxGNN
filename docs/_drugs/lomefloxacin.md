---
layout: default
title: Lomefloxacin
parent: Model Prediction Only (L5)
nav_order: 497
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Lomefloxacin"
predicted_indications: ["laryngotracheitis", "heart valve disease", "heart conduction disease", "congenital anomaly of ventricular septum", "heart neoplasm", "pericardium disease", "myocardial rupture", "cardiac anomalies-heterotaxy syndrome", "carcinoid heart disease", "heart aneurysm"]
description: "Lomefloxacin: predicted new indication Laryngotracheitis (evidence level L5). In India: 15 listed products (15 not discontinued)"
---

# Lomefloxacin
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

## Lomefloxacin: Laryngotracheitis
{: .text-alpha }

## One-Sentence Summary

Lomefloxacin is a fluoroquinolone antibacterial, originally used to treat urinary tract infection and bronchitis.
The TxGNN model predicts it may be effective for **laryngotracheitis**,
but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Laryngotracheitis |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (15 of 15) – CDSCO approval status is not included in this data |
| Number of Listed Products | 15 (valid: 15) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lomefloxacin is a fluoroquinolone, a class that inhibits bacterial DNA gyrase and topoisomerase IV. Its use in bronchitis is established, and a respiratory-tract infection indication may be mechanistically applicable to laryngotracheitis.

The link is limited, however. Laryngotracheitis (croup) is mostly viral, so an antibacterial agent has little relevance except in bacterial tracheitis. The high TxGNN score is most likely driven by network proximity to respiratory infection indications rather than by direct biological evidence.

Other predictions in the top 10 are mostly cardiac conditions (heart valve disease, heart conduction disease, heart aneurysm, myocardial rupture and others). These have no plausible mechanistic basis, and some conflict with known fluoroquinolone safety signals. The scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. They are not recommended for further evaluation:
- Fluoroquinolones are associated with QT prolongation and arrhythmia risk.
- They are associated with aortic aneurysm/dissection and valve regurgitation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 87421 | Floxaday 400mg Tablet | Strip of 6 tablets | Valid |
| 92188 | Floxaquin LA 400mg Tablet | Strip of 4 tablets | Valid |
| 100528 | Gynalom 400mg Tablet | Strip of 5 tablets | Valid |
| 124626 | Lomef 400mg Tablet | Strip of 10 tablets | Valid |
| 125913 | Lomin 400mg Tablet | Strip of 10 tablets | Valid |
| 126983 | Loflox Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 127266 | Lomedon 400mg Tablet | Strip of 5 tablets | Valid |
| 130215 | Lomibact 3mg Drop | Packet of 5 ml Drop | Valid |
| 130531 | Lomexel 400mg Tablet | Strip of 10 tablets | Valid |
| 130619 | Lom 0.3% Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 130631 | Lomegen 400mg Tablet | Strip of 10 tablets | Valid |
| 211833 | Soloflox 400mg Tablet | Strip of 4 tablets | Valid |
| 228185 | Taurlom 400mg Tablet | Strip of 10 tablets | Valid |
| 234724 | Vivo 400mg Tablet | Strip of 10 tablets | Valid |
| 236811 | Vivo 400mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

All 15 registrations are valid single-ingredient products. Most are 400 mg oral tablets, with additional drop and eye drop formulations.

## Safety Considerations

- **Drug Interactions**: 238 interacting drugs were identified. Examples of **Major** interactions include:
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone
  - Bupropion
  - Chlorpropamide

  Examples of **Moderate** interactions include:
  - Antidiabetic agents: metformin, pioglitazone, acarbose, alogliptin, albiglutide, canagliflozin
  - Famotidine
  - Loperamide
  - Acetylsalicylic acid
  - Calcium-containing products

- **Class-level cardiovascular signals**: Fluoroquinolones are associated with QT prolongation, aortic aneurysm/dissection and valve regurgitation. These are relevant for any cardiac-related repurposing and argue against it.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no clinical trials or literature (Evidence Level L5). Laryngotracheitis is mostly viral, which limits the relevance of an antibacterial. Fluoroquinolone safety concerns also argue for caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Literature and trial searches on fluoroquinolone use in bacterial tracheitis or laryngotracheobronchitis
- A comparison against current standard-of-care antibacterials for respiratory infections, plus a benefit-risk review given the class safety signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

