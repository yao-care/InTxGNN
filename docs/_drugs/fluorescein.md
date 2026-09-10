---
layout: default
title: Fluorescein
parent: 僅模型預測 (L5)
nav_order: 361
evidence_level: L5
indication_count: 10
---

# Fluorescein
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

# Fluorescein: From Diagnostic Ophthalmic Dye to Prinzmetal Angina

## One-Sentence Summary

Fluorescein (DB00693) has no confirmed therapeutic indication on file in this evidence pack — it is best known as a diagnostic fluorescent dye (e.g., ophthalmic/retinal angiography, wound and burn assessment), not a treatment drug.
The TxGNN model predicts it may be effective for **Prinzmetal Angina**, but this pairing is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-based signal with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this pack — Fluorescein is not registered in the local market covered here; its established use is as a diagnostic dye rather than a therapeutic agent |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for Fluorescein in this pack. Based on known pharmacological information, Fluorescein is a fluorescent diagnostic dye used almost exclusively for imaging procedures (fluorescein angiography of the retina/choroid, corneal staining, wound assessment) — it has no established cardiovascular pharmacology and no known mechanism relevant to coronary vasospasm, which is the pathophysiology underlying Prinzmetal angina. No clinical trial or literature evidence links Fluorescein to this disease.

It is also worth noting a pattern across this entire candidate: for the other predicted indications in this pack that *do* have associated clinical trials or literature (rheumatoid arthritis, hemoglobinopathy, thrombophilia, hyperthyroidism, beta-thalassemia), the retrieved evidence consistently shows Fluorescein being used as a **diagnostic/imaging tool** (fluorescein angiography, OCT-angiography assessment) within studies of those diseases — not as an investigational treatment. In each case the reviewer notes explicitly flag this as a disease-term/keyword mismatch rather than a genuine treatment hypothesis. This reinforces that the TxGNN score for Prinzmetal angina (like the other top-ranked, evidence-free predictions) should be treated as a graph-based statistical association only, without mechanistic or clinical support.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Market Information

Fluorescein is currently **not marketed** under this registry (0 registrations), so no license/product information is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Prinzmetal angina) is an L5, model-only signal with zero clinical trials or literature support, no plausible mechanistic link, and no MOA data available. Broader review of this candidate's other predicted indications shows Fluorescein's real-world evidence footprint is entirely diagnostic (angiography/imaging), not therapeutic — undermining confidence in any of the top-10 TxGNN predictions for this drug.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- TFDA/regulatory label warnings, contraindications, and DDI data (currently all data gaps)
- A mechanistic rationale connecting Fluorescein to coronary vasospasm before any further evaluation of the Prinzmetal angina hypothesis
- Re-screening of all 10 predicted indications to explicitly separate "diagnostic use in disease X" evidence from genuine "treatment for disease X" evidence, since the current evidence set conflates the two
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

