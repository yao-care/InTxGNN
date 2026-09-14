---
layout: default
title: Teneligliptin
parent: 僅模型預測 (L5)
nav_order: 809
evidence_level: L5
indication_count: 8
---

# Teneligliptin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Teneligliptin: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

> Teneligliptin is a DPP-4 inhibitor approved in Japan and South Korea for type 2 diabetes mellitus (it holds no license in Taiwan).
> The TxGNN model predicts potential effectiveness for **Opsismodysplasia**, a rare genetic skeletal dysplasia,
> but this is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale explicitly flags no known biological link between the two conditions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (approved in Japan/South Korea; not TFDA-licensed — sourced from pharmacology `clinical_use` field, not from a formal Taiwan license record) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.45% (raw score), but ranked **9038th** overall — many disease pairs score near this ceiling, so the raw score alone is not strongly discriminating |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not officially available (the `original_moa` field is marked as a data gap). However, pharmacological target-binding data confirms teneligliptin's primary target is DPP4 (dipeptidyl peptidase-4), with additional off-target binding to DPP8 and DPP9 — consistent with its known classification as a DPP-4 inhibitor ("gliptin" class) that improves glycemic control by enhancing incretin (GLP-1/GIP) signaling.

Opsismodysplasia is a rare autosomal-recessive skeletal dysplasia associated with defective endochondral ossification, with no established biological pathway connecting it to incretin-based glucose metabolism. The model's own repurposing rationale states there is **no known biological association** between DPP-4 inhibition and this disease, and attributes the high score to a likely knowledge-graph artifact (e.g., shared upstream metabolic nodes) rather than a genuine pharmacological signal.

Given the missing original indication record in the Taiwan regulatory data, the missing MOA documentation, and the model's own caveat about mechanistic implausibility, this prediction should be treated as a low-confidence signal requiring independent validation rather than a candidate ready for evidence review. For context, all 7 other top-ranked predictions for this drug (thiamine-responsive dysfunction syndrome, stiff person syndrome variants, and several lipodystrophy subtypes) show the same pattern — L5 evidence, no trials or literature, and self-reported weak-to-absent mechanistic links.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Teneligliptin currently holds **no drug license registration in Taiwan** (market status: 未上市 / Not Marketed; total licenses: 0). No product, dosage form, or approved indication data is available from the Taiwan regulatory record.

## Safety Considerations

- **Drug Interactions (Pharmacological Target Profile)**: The available data (3 entries) reflects target-binding pharmacology rather than a classic clinical drug-drug interaction list:

| Target | Gene | Species | Note |
|--------|------|---------|------|
| Dipeptidyl peptidase 4 (DPP4) | DPP4 | Human | Primary pharmacological target — enzyme inhibited for incretin-based glucose control |
| Dipeptidyl peptidase 8 (DPP8) | DPP8 | Human | Off-target binding; DPP8/9 inhibition has been associated with toxicity signals for the gliptin class in preclinical literature |
| Dipeptidyl peptidase 9 (DPP9) | DPP9 | Human | Off-target binding; same class-related caution as DPP8 |

No TFDA package insert warnings or contraindications are currently available (this is a Blocking data gap, DG001). Official prescribing information from the drug's country of approval (Japan/South Korea) should be consulted before any clinical use decision.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 (model prediction only, with zero clinical trials or literature), and the model's own mechanistic rationale identifies no plausible biological link between DPP-4 inhibition and this rare genetic skeletal disorder — the high raw score most likely reflects a knowledge-graph artifact rather than a genuine pharmacological signal.

**To proceed, the following is needed:**
- TFDA package insert data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Verified original mechanism of action documentation (High-priority gap, DG002)
- Confirmed original indication and regulatory status, since the Taiwan license record is currently empty
- Independent mechanistic or preclinical evidence linking the DPP-4/incretin pathway to skeletal dysplasia pathophysiology, before this candidate can move beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

