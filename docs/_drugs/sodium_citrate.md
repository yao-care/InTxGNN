---
layout: default
title: Sodium Citrate
parent: 僅模型預測 (L5)
nav_order: 771
evidence_level: L5
indication_count: 9
---

# Sodium Citrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Sodium Citrate: From Undocumented Original Indication to Papillary Conjunctivitis

## One-Sentence Summary

Sodium citrate (DrugBank DB09154) has no recorded original indication or mechanism-of-action data in this evidence pack, and it is not currently marketed in this jurisdiction. The TxGNN model's top-ranked prediction is **Papillary Conjunctivitis**, but this prediction is supported by **0 clinical trials** and **0 publications** — it is a pure model score with no mechanistic hypothesis behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No original indication data available (drug not marketed; regulatory records absent) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for sodium citrate, and no original approved indication is recorded in this evidence pack. Based on other entries in this evidence pack, sodium citrate is known clinically as an oral alkalinizing agent — it is used to raise intragastric pH (e.g., pre-anesthesia prophylaxis against aspiration pneumonitis) — which gives some general pharmacological context, though this is not tied to any regulatory-approved indication captured here.

For the top-ranked prediction, **papillary conjunctivitis**, the evidence pack explicitly states there is no mechanistic hypothesis, no clinical trial, and no literature connecting sodium citrate to this condition — it is a model score alone (TxGNN rank 1381, score 99.95%). This should be treated as a purely exploratory signal, not a grounded repurposing hypothesis.

By contrast, a lower-ranked prediction in the same pack — "stomach disease" (rank 4, TxGNN score 99.89%) — has somewhat more supporting context: in vitro studies show sodium citrate combined with 3-bromopyruvate induces apoptosis in gastric cancer cell lines via glycolysis inhibition, and one case report describes sodium citrate–associated gastric/esophageal mucosal injury. Neither constitutes direct clinical evidence of therapeutic benefit, but it illustrates that not all predictions in this pack carry equal evidentiary weight — the top-ranked candidate (papillary conjunctivitis) is the weakest of them.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

No registration records available — sodium citrate is not currently marketed in this jurisdiction (0 licenses on file).

---

## Safety Considerations

**Drug Interactions**: A total of **114 known interactions** are on record (sample of 20 provided). Notable entries include:

- **Major**: Aluminum hydroxide
- **Moderate**: Doxycycline, Acetylsalicylic acid, Iron, Ephedrine (oral/nasal), Levofloxacin, Minocycline, Rosuvastatin, Tetracycline, Acalabrutinib, Pseudoephedrine
- **Minor**: Acetohexamide, Chlorpropamide, Glipizide, Glyburide, Lactulose, Misoprostol, Tolazamide, Tolbutamide

Key warnings and contraindication data are not available in this evidence pack — please refer to the package insert for that information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (papillary conjunctivitis) has zero supporting clinical trials or literature — it is a TxGNN model score with no mechanistic hypothesis (L5, S0). Even the pack's better-supported candidate (stomach disease) only reaches preclinical/case-report-level evidence (L4), insufficient to justify moving past a research question stage.

**To proceed, the following is needed:**
- Original approved indication and regulatory history for sodium citrate
- Mechanism of action (MOA) data (currently flagged as a Blocking data gap)
- TFDA-equivalent package insert warnings/contraindications (currently a Blocking data gap)
- If pursuing papillary conjunctivitis: a documented mechanistic rationale before any trial design is considered
- If pursuing stomach disease instead: prospective clinical evidence beyond the existing in vitro/case-report literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

