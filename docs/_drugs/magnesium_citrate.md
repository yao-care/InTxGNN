---
layout: default
title: Magnesium Citrate
parent: Model Prediction Only (L5)
nav_order: 513
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
monitor_inn: "Magnesium citrate"
predicted_indications: ["calcium-alkali syndrome", "primary bone dysplasia with defective bone mineralization"]
description: "Magnesium Citrate: predicted new indication Calcium-alkali syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Magnesium Citrate
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

## Magnesium Citrate: Calcium-alkali syndrome
{: .text-alpha }

## One-Sentence Summary

Magnesium citrate is a magnesium salt used in conditions of mineral and bone metabolism (such as osteoporosis, hypercalcaemia and phosphorus metabolism disorders) and as a laxative for constipation.
The TxGNN model predicts it may be relevant for **calcium-alkali syndrome**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Calcium-alkali syndrome |
| TxGNN Prediction Score | 0.9951 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 12 of 12) |
| Number of Registrations | 12 (valid: 12) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, magnesium citrate is an oral magnesium salt. Magnesium takes part in calcium and phosphorus homeostasis and in parathyroid hormone (PTH) regulation, and it overlaps with the drug's original indications (hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease). This overlap is the likely basis for the model's prediction.

However, the link is weak. Calcium-alkali syndrome is caused by excessive intake of calcium and absorbable alkali, and its main management is to stop the offending agents and give hydration. Whether magnesium citrate offers any benefit is unestablished. The citrate component is alkalinizing, and magnesium can accumulate in renal impairment, which is common in this syndrome, so there is a possible safety concern.

A second prediction, **primary bone dysplasia with defective bone mineralization** (score 0.9933), is similarly unsupported. Magnesium is a cofactor in bone mineral metabolism, but these are heterogeneous genetic disorders driven by specific gene defects (for example hypophosphatasia). A general magnesium supplement is not expected to correct them, and no clinical evidence exists for it.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 14554 | Alkovak Oral Solution | 200 ml bottle, oral solution | Not stated |
| 230592 | Urikem Syrup | 200 ml bottle, syrup | Not stated |
| 230736 | Utimack Syrup | 200 ml bottle, syrup | Not stated |
| 200118 | Ston 1 Oral Solution Mixed Fruit | 200 ml bottle, oral solution | Not stated |
| 200326 | Ston 1 Oral Solution Delicious Pineapple | 200 ml bottle, oral solution | Not stated |

Twelve valid single-ingredient licences are registered in total; the five above are shown. There are no combination or cancelled licences.

## Safety Considerations

- **Contraindications (from knowledge-graph drug-disease edges, not label text)**: kidney disease and impaired renal function, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, hypercalcaemia, hyperparathyroidism, hyperphosphataemia, metabolic acidosis, adrenal insufficiency (including Addison disease and congenital adrenal hyperplasia), peptic ulcer disease, appendicitis, diarrhoeal disease, sarcoidosis, rhabdomyolysis. Several of these (renal impairment, hypercalcaemia, metabolic acidosis) are directly relevant to calcium-alkali syndrome.
- **Drug Interactions**: 235 interactions are recorded. The only Major one in the listed set is **dolutegravir**. Moderate interactions include alendronic acid, doxycycline, hydrocortisone, triamcinolone, hydrochlorothiazide, amiloride, acetazolamide, amiodarone, tramadol, and salbutamol. The binding or chelation effect of magnesium on drugs such as dolutegravir, doxycycline and bisphosphonates should be considered when timing doses.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN model (deep learning) score, with no clinical trials or literature (Evidence Level L5). Calcium-alkali syndrome is managed by removing the causative agents, and magnesium citrate carries a possible safety concern in the renal impairment that often accompanies it.

**To proceed, the following is needed:**
- A literature and clinical-trial search specific to magnesium and calcium-alkali syndrome, to see whether any supporting evidence exists
- Mechanism of action data for magnesium citrate
- Package insert warnings and contraindications for the marketed Indian products, and their approved indications
- A renal safety assessment for patients with impaired kidney function and for the alkalinizing effect of citrate
- Route compatibility and similarity-to-original-indication analyses, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

