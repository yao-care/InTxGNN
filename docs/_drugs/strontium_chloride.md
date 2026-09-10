---
layout: default
title: Strontium Chloride
parent: 僅模型預測 (L5)
nav_order: 786
evidence_level: L5
indication_count: 10
---

# Strontium Chloride
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

# Strontium Chloride: From Unspecified Original Indication to Osteoarthritis

## One-Sentence Summary

> No original indication or licensed product record is currently available for Strontium chloride (DB13987) in this dataset.
> The TxGNN model predicts it may be effective for **Osteoarthritis**,
> with **1 clinical trial** currently supporting this direction and **no directly matched publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (no original indications on file, no licensed products) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.28% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this compound (MOA: Data Gap). Based on the mechanistic rationale extracted from the evidence pack, Sr²⁺ can substitute for Ca²⁺ in bone matrix, stimulating osteoblast proliferation/differentiation while inhibiting osteoclast activity — a mechanism well established for strontium-based compounds (e.g., strontium ranelate) in bone and joint disease.

The single supporting trial (NCT00954629) tested a **topical strontium chloride hexahydrate** formulation for knee osteoarthritis pain, which is mechanistically consistent with this pathway. However, this evidence pack's drug entity is **strontium chloride (DB13987)**, a different salt form from strontium ranelate, and it has not been confirmed whether the trial's active ingredient is pharmacologically and formulation-wise identical to DB13987. This salt/formulation discrepancy must be resolved before the trial can be treated as direct supporting evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00954629](https://clinicaltrials.gov/study/NCT00954629) | Phase 3 | Unknown | 300 | 26-week, randomized, double-blind, placebo-controlled study of topical strontium chloride hexahydrate (2PX) vs. vehicle for knee osteoarthritis pain and physical function; result status not verified (trial marked "Unknown"). |

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Strontium chloride (DB13987) is currently **not marketed** in India, and no license registrations are on record in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Regulatory safety documentation (warnings, contraindications) for this compound has not yet been retrieved and is flagged as a blocking data gap for safety review.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting trial has an unresolved ("Unknown") completion status, and it is unconfirmed whether its active ingredient matches the exact salt form/formulation of DB13987. Combined with the absence of any safety documentation (warnings/contraindications), the candidate cannot yet clear even an initial safety screen (S1).

**To proceed, the following is needed:**
- Confirm whether the agent studied in NCT00954629 (topical strontium chloride hexahydrate) is pharmaceutically equivalent to DB13987
- Retrieve regulatory package insert / safety documentation (warnings, contraindications) — currently a blocking gap for S1 review
- Obtain a verified MOA reference from DrugBank to substantiate the mechanistic rationale
- Follow up on NCT00954629 for updated/completed results given its current "Unknown" status
- Deprioritize rank-2 prediction ("osteoarthritis susceptibility") as it represents a genetic susceptibility marker, not a treatable disease phenotype
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

