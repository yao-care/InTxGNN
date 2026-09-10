---
layout: default
title: Sorbitol
parent: 僅模型預測 (L5)
nav_order: 777
evidence_level: L5
indication_count: 1
---

# Sorbitol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Sorbitol: From Osmotic Laxative/Excipient Use to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Sorbitol is a sugar alcohol traditionally used as an osmotic laxative, diuretic, and pharmaceutical excipient; detailed original indication and mechanism-of-action data are not yet available in this evidence pack. The TxGNN model predicts a possible association with **Exercise-Induced Malignant Hyperthermia**, but this prediction is currently supported by **zero clinical trials** and **zero publications**, and the model's own rationale flags the link as lacking biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (per evidence pack: osmotic laxative / diuretic / pharmaceutical excipient use) |
| Predicted New Indication | Exercise-Induced Malignant Hyperthermia |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Sorbitol is a sugar alcohol used clinically as an osmotic laxative, diuretic, and pharmaceutical excipient; its original indication and pharmacological classification are not fully captured in this evidence pack.

Exercise-induced malignant hyperthermia is a disorder of skeletal muscle calcium regulation, typically linked to RYR1/CACNA1S gene variants, triggered by anesthetic exposure or strenuous exercise. There is no known pharmacological pathway by which Sorbitol would affect ryanodine receptor function, sarcoplasmic reticulum calcium release, or thermoregulation.

The evidence pack's own rationale is explicit on this point: the very high TxGNN score (0.994) most likely reflects **topological proximity within the knowledge graph** rather than a genuine, explainable biological mechanism. In the absence of any mechanistic pathway, clinical trial, or literature support, this association should be treated as a candidate for further screening only — not as a credible repurposing signal at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

No market authorization records are currently available — Sorbitol is not marketed in Taiwan under this evidence pack's regulatory dataset (0 registrations).

---

## Safety Considerations

**Drug Interactions** (from DDInter):

| Interacting Drug | Severity Level | Source |
|---|---|---|
| Lamivudine | Moderate | DDInter |
| Tolevamer | Major | DDInter |

Key warnings and contraindications are not yet available in this evidence pack; please refer to the official product label once TFDA labeling data is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but there is no clinical trial or literature evidence (Evidence Level L5), the drug is not currently marketed in Taiwan, and the model's own mechanistic rationale suggests the association is likely a knowledge-graph artifact rather than a biologically plausible link.

**To proceed, the following is needed:**
- TFDA product label (warnings/contraindications) — currently blocking (DG001)
- Confirmed mechanism of action data from DrugBank (DG002)
- Independent mechanistic or preclinical evidence connecting Sorbitol to malignant hyperthermia pathways before any further clinical evaluation is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

