---
layout: default
title: Norfloxacin
parent: 僅模型預測 (L5)
nav_order: 603
evidence_level: L5
indication_count: 10
---

# Norfloxacin
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

# Norfloxacin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Norfloxacin is a fluoroquinolone-class antibacterial; Taiwan-specific approved indication text is not available in this evidence pack because the drug is currently **not marketed in Taiwan**. The TxGNN model's top prediction is **Polyclonal Hyperviscosity Syndrome**, but this pairing is currently supported by **0 clinical trials** and **0 publications** — the model's own rationale explicitly states there is no known mechanistic or biological link between an antibacterial agent and a plasma-protein hyperviscosity disorder.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (Taiwan: unmarketed, 0 licenses); commonly known class use is bacterial infection (fluoroquinolone antibiotic) |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on known information, Norfloxacin is a fluoroquinolone antibiotic that acts by inhibiting bacterial DNA gyrase and topoisomerase IV; its established use is for bacterial infections such as urinary tract and gastrointestinal infections.

For the top-ranked prediction, Polyclonal Hyperviscosity Syndrome — a disorder driven by excess circulating immunoglobulins/plasma proteins — there is no known pharmacological or mechanistic pathway connecting an antibacterial agent's mode of action to plasma viscosity regulation. The model's own generated rationale is explicit on this point: *"無任何臨床試驗或文獻支持...與血漿蛋白過高導致的高黏滯症候群無已知作用機轉關聯，純為 TxGNN 圖譜預測，無生物學合理性佐證"* (no supporting trials or literature; no known mechanistic link; pure graph-based prediction with no biological plausibility support).

This prediction should therefore be treated as a knowledge-graph statistical association only, not as a mechanistically grounded repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Currently no market authorization records in Taiwan — Norfloxacin is not marketed (0 licenses on file).

## Safety Considerations

Key warnings and contraindications are not available in this evidence pack (data gap DG001, flagged as Blocking — TFDA label/warning data has not yet been retrieved).

**Drug Interactions**: A DDI query returned 299 total interactions on file. Notable **Major**-level interactions include:
- Hydrocortisone
- Bupropion
- Triamcinolone
- Dexamethasone
- Betamethasone
- Chlorpropamide

Numerous **Moderate**-level interactions were also identified (e.g., Metformin, Acetylsalicylic acid, Pioglitazone, Canagliflozin, Alogliptin, Albiglutide), largely involving glucose-lowering agents and corticosteroids. Full interaction profile (299 entries) should be reviewed against the eventual TFDA label once available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Polyclonal Hyperviscosity Syndrome) has zero supporting clinical or literature evidence and is explicitly flagged by the model's own rationale as lacking biological plausibility. Combined with the absence of Taiwan market authorization and missing MOA/label data, this candidate does not meet the threshold to advance past initial screening.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking — required before any S1 safety screening)
- Confirmed DrugBank mechanism of action (DG002)
- If pursuing repurposing for this drug at all, redirect attention to **rank 10 (Septicemic Plague)** instead: it carries stronger class-effect rationale (fluoroquinolones ciprofloxacin/levofloxacin are CDC/FDA-recognized plague treatments) and reached evidence level L3 / Research Question stage — a more biologically defensible candidate than the current top-ranked hit
- Independent literature/mechanism review before considering any indication in this candidate set for further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

