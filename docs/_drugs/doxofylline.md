---
layout: default
title: Doxofylline
parent: 僅模型預測 (L5)
nav_order: 250
evidence_level: L5
indication_count: 10
---

# Doxofylline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Doxofylline: From Asthma/COPD to Pierre Robin Syndrome Associated with a Chromosomal Anomaly

---

## One-Sentence Summary

Doxofylline is a second-generation methylxanthine bronchodilator with a well-established role in treating asthma and chronic obstructive pulmonary disease (COPD), distinguished from theophylline by its minimal adenosine receptor antagonism and superior safety profile.
The TxGNN model predicts potential utility in **Pierre Robin Syndrome Associated with a Chromosomal Anomaly**, but **zero clinical trials** and **zero supporting publications** exist for this combination, and mechanistic analysis strongly identifies this as a **knowledge graph false positive** rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Asthma and COPD (based on published literature; no India regulatory data on record) |
| Predicted New Indication | Pierre Robin Syndrome Associated with a Chromosomal Anomaly |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is currently unavailable from DrugBank. Based on the published literature retrieved during evidence collection, Doxofylline is a methylxanthine derivative structurally related to theophylline — distinguished by a dioxolane ring substituent at position 7 of the xanthine core. Its primary bronchodilatory mechanism involves inhibition of cyclic nucleotide phosphodiesterases (PDEs), elevating intracellular cAMP levels and thereby relaxing airway smooth muscle. Critically, unlike theophylline, Doxofylline shows markedly reduced affinity for adenosine A₁ and A₂ receptors, which is the pharmacological basis for its better cardiovascular and CNS tolerability (PMID 11268710, PMID 3240706).

Pierre Robin Syndrome associated with a chromosomal anomaly is a congenital craniofacial disorder defined by the classic triad of micrognathia (underdeveloped mandible), glossoptosis (posterior tongue displacement), and frequently cleft palate, arising from disruption of mandibular development during embryogenesis. The chromosomal anomaly subtype implies an underlying genomic structural defect as the causative mechanism. Clinical management is primarily positional, surgical, or involves mandibular distraction osteogenesis — pharmacological intervention plays no established role.

**There is no plausible mechanistic connection between Doxofylline's PDE inhibition/bronchodilation mechanism and the embryological or chromosomal basis of Pierre Robin Syndrome.** The high TxGNN score (99.54%) almost certainly results from indirect knowledge graph linkages through shared "respiratory distress," "airway obstruction," or "upper airway" symptom nodes — a well-recognized source of false positives when respiratory drugs are co-evaluated with conditions that incidentally cause breathing difficulty. The co-occurrence of two Pierre Robin syndrome subtypes at Ranks 1 and 4 with nearly identical scores (0.9954 vs. 0.9953), alongside a cluster of other congenital craniofacial conditions (orofacial clefting at Rank 5), strongly suggests a systematic ontology-level graph artifact rather than any true biological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Formal warnings and contraindications data from the India regulatory package insert are not yet available (pending data gap). Full safety assessment cannot be completed until this information is retrieved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No mechanistic link exists between Doxofylline's bronchodilator action and Pierre Robin Syndrome associated with a chromosomal anomaly; the TxGNN high score is a knowledge graph artifact driven by respiratory symptom node co-occurrence, and this prediction does not meet the threshold for further clinical or scientific investigation.

**To proceed, the following is needed:**

This specific prediction is **not recommended for advancement**. For a productive Doxofylline repurposing program, the following priority actions are recommended:

- **Resolve data gaps first:**
  - Retrieve full MOA data from DrugBank (currently missing)
  - Obtain India regulatory package insert to extract warnings and contraindications
- **Redirect focus to Rank 9 (Heart Disease, L4 evidence level):** This prediction carries a plausible pharmacological rationale — PDE inhibition raises myocardial cAMP (modest positive inotropy), while the absence of adenosine receptor blockade is specifically advantageous in cardiac patients where adenosine exerts cardioprotective effects. Supporting literature includes an RCT in chronic heart failure with hypoxaemia (PMID 8088931), a double-blind asthma RCT confirming cardiovascular safety (PMID 11951074), and a network meta-analysis in COPD (PMID 29720510). The core research question — *whether Doxofylline is a safer bronchodilator than theophylline in patients with comorbid airway obstruction and heart disease* — is clinically meaningful and actionable
- **Apply false positive filters:** The clustering of congenital craniofacial, chromosomal deletion, and rare developmental syndromes (Ranks 1–6, 8, 10) as top TxGNN hits suggests a systematic graph bias in this drug's embedding. A knowledge graph audit filtering symptom-mediated indirect edges is recommended before any further candidate screening

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

