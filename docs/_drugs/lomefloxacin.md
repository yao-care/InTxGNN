---
layout: default
title: Lomefloxacin
parent: Model Prediction Only (L5)
nav_order: 497
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lomefloxacin: predicted new indication Laryngotracheitis (evidence level L5). Approved use: Urinary tract infection, bronchitis"
monitor_inn: "Lomefloxacin"
predicted_indications: ["laryngotracheitis", "heart valve disease", "heart conduction disease", "congenital anomaly of ventricular septum", "heart neoplasm", "pericardium disease", "carcinoid heart disease", "myocardial rupture", "heart aneurysm", "cardiac anomalies-heterotaxy syndrome"]
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

## Lomefloxacin: From Urinary Tract Infection and Bronchitis to Laryngotracheitis
{: .text-alpha }

## One-Sentence Summary

Lomefloxacin is a fluoroquinolone antibacterial, originally used to treat urinary tract infection and bronchitis.
The TxGNN model predicts it may be effective for **laryngotracheitis**,
but there are currently **no clinical trials** and **no publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, bronchitis (from the TxGNN knowledge graph; no approved indication text is available in the India licence records) |
| Predicted New Indication | Laryngotracheitis |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 15 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lomefloxacin is a fluoroquinolone, a class that inhibits bacterial DNA gyrase and topoisomerase IV. Its use in bronchitis is established, and a respiratory-tract infection indication may be mechanistically applicable to laryngotracheitis.

The link is limited, however. Laryngotracheitis (croup) is mostly viral, so an antibacterial agent has little relevance except in bacterial tracheitis. The high TxGNN score is most likely driven by network proximity to respiratory infection indications rather than by direct biological evidence.

Other predictions in the top 10 are mostly cardiac conditions (heart valve disease, heart conduction disease, heart aneurysm, myocardial rupture and others). These have no plausible mechanistic basis, and some conflict with known fluoroquinolone safety signals. They are likely artifacts of the knowledge graph and are not recommended for further evaluation:
- Fluoroquinolones are associated with QT prolongation and arrhythmia risk.
- They are associated with aortic aneurysm/dissection and valve regurgitation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 87421 | Floxaday 400mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 6 tablets | Not specified in the records |
| Registration No. 124626 | Lomef 400mg Tablet (Torrent Pharmaceuticals Ltd) | Strip of 10 tablets | Not specified in the records |
| Registration No. 130215 | Lomibact 3mg Drop (Sun Pharmaceutical Industries Ltd) | Packet of 5 ml drop | Not specified in the records |
| Registration No. 130619 | Lom 0.3% Eye Drop (Oscar Remedies Pvt Ltd) | Packet of 5 ml eye drop | Not specified in the records |
| Registration No. 100528 | Gynalom 400mg Tablet (Wockhardt Ltd) | Strip of 5 tablets | Not specified in the records |

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

