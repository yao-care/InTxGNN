---
layout: default
title: Amorolfine
parent: 僅模型預測 (L5)
nav_order: 56
evidence_level: L5
indication_count: 10
---

# Amorolfine
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

# Amorolfine: From Onychomycosis to Drug-Induced Osteoporosis

## One-Sentence Summary

Amorolfine is a morpholine-class topical antifungal, best known for treating onychomycosis (fungal nail infections) via nail lacquer formulation.
The TxGNN model predicts it may have potential for **Drug-Induced Osteoporosis** as the top-ranked indication,
however this is currently supported by **0 clinical trials** and **0 publications** — the evidence base is entirely model-prediction only, and all 10 predicted indications across this batch share this L5 status.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Onychomycosis (fungal nail infections) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.9978% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Amorolfine is a morpholine-class antifungal that inhibits ergosterol biosynthesis in fungal cell membranes — specifically targeting the enzymes Δ14-reductase and Δ7→Δ8-isomerase. This disrupts membrane integrity and kills the fungal cell. It is formulated exclusively as a topical nail lacquer, resulting in negligible systemic absorption. This pharmacokinetic profile is critical: systemic exposure following topical application is essentially non-existent.

The mechanistic rationale for drug-induced osteoporosis is extremely weak. While certain **azole** antifungals (particularly itraconazole) have shown indirect interference with sterol-dependent bone metabolism pathways, amorolfine belongs to the **morpholine** class — a fundamentally different chemical scaffold with no established Hedgehog pathway, CYP enzyme, or osteoclast/osteoblast interaction. Cross-class extrapolation from azoles to morpholines is not scientifically justified.

Even if a sterol-bone metabolism link were biologically plausible, amorolfine's near-zero systemic bioavailability from topical use makes any systemic pharmacological effect clinically irrelevant. The TxGNN prediction most likely reflects a topological artifact within the knowledge graph — ergosterol/sterol metabolism nodes are structurally adjacent to bone-related pathways — rather than a genuine drug-disease pharmacological signal. Of the 10 predictions in this batch, only **urethral disease** (rank 10) carries even a minimal mechanistic connection (fungal urethritis), and the topical delivery barrier applies there as well.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Amorolfine are rated L5 (model prediction only, zero supporting clinical or preclinical evidence), and Amorolfine's exclusive topical formulation with negligible systemic exposure represents a fundamental pharmacokinetic barrier to any systemic repurposing hypothesis. The drug is also not currently registered or marketed in India, meaning there is no existing regulatory pathway to leverage.

**To proceed, the following is needed:**
- Retrieve the original approved indication(s) from the drug's package insert or regulatory filings (CDSCO / EMA / originator label) to complete the baseline drug profile
- Obtain detailed mechanism of action data (MOA) from DrugBank API to enable mechanistic plausibility analysis
- Determine whether a systemic oral or IV formulation of amorolfine exists in any jurisdiction — without a systemic delivery route, all current predictions remain clinically inaccessible
- Consider whether any predicted indication could theoretically be addressed via **local/topical delivery** (e.g., fungal urethritis as a topical application), which is the only scenario with minimal biological plausibility in this batch
- Collect TFDA/CDSCO package insert warnings and contraindications to complete the S1-level safety assessment before any further development discussion
- If the program continues, prioritise the mechanistic re-evaluation of **urethral disease** (rank 10) as the sole candidate with a tenuous but existing biological rationale, contingent on resolving the delivery route question

> ⚠️ **Research Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

