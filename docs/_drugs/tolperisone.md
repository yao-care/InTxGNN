---
layout: default
title: Tolperisone
parent: 僅模型預測 (L5)
nav_order: 839
evidence_level: L5
indication_count: 10
---

# Tolperisone
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

# Tolperisone: From Muscle Spasm to Laubry-Pezzi Syndrome

## One-Sentence Summary

> Tolperisone is a centrally-acting, voltage-gated sodium channel blocker used clinically as a muscle relaxant (specific formally-approved indication text is not available in this evidence pack).
> The TxGNN model predicts it may be effective for **Laubry-Pezzi Syndrome** (a congenital cardiac malformation involving ventricular septal defect with overriding aorta),
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure topological/embedding-similarity output from the model, and the evidence pack's own mechanistic review found **no known pathophysiological link** between the drug and this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Muscle spasm/spasticity (per drug class description in evidence pack; formal approved indication text not available) |
| Predicted New Indication | Laubry-Pezzi Syndrome |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is flagged as a Blocking/High-severity data gap in this evidence pack (DG001, DG002). Based on the mechanistic notes embedded in the repurposing rationale, tolperisone is described as a centrally-acting, voltage-dependent sodium channel blocker functioning as a muscle relaxant — this is the only characterization available, as no formal MOA record or approved-indication text could be extracted.

Laubry-Pezzi syndrome is a congenital structural cardiac defect (ventricular septal defect with aortic override), unrelated in etiology or pathophysiology to skeletal muscle tone regulation. The evidence pack's own mechanistic review explicitly states there is **no known pathophysiological relationship** between tolperisone's sodium-channel-blocking action and this congenital cardiac malformation — the prediction is described as "purely a TxGNN topological prediction, with no supporting literature or trials."

Given the absence of a plausible biological rationale, absence of any clinical or preclinical evidence, and the very high TxGNN score being unaccompanied by corroborating data, this candidate should be treated as a low-confidence model artifact rather than a scientifically grounded repurposing hypothesis at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Tolperisone currently has **no registration records** in the India regulatory dataset (0 licenses, market status: Not Marketed). No product/dosage-form/indication information is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are all currently unavailable — flagged as Blocking data gap DG001.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Laubry-Pezzi syndrome, TxGNN score 99.92%) has evidence level L5 — no clinical trials, no supporting literature, and no plausible mechanistic link, as confirmed by the evidence pack's own rationale review. This pattern holds across all 10 top-ranked candidates for this drug: none advance past Evidence Level L4/L5, and where literature was retrieved (e.g., "heart disease," "disorder of fucoglycosan synthesis"), it was assessed as irrelevant co-occurrence noise or indexing mismatches rather than supportive evidence. Combined with the drug's non-marketed status in India (0 registrations) and missing MOA/safety data, there is currently no basis to proceed beyond Hold.

**To proceed, the following is needed:**
- TFDA/CDSCO package insert with formal warnings and contraindications (DG001 — Blocking, required before any S1 safety screening)
- Confirmed mechanism of action from DrugBank API query (DG002)
- Original approved-indication text for the drug (currently unavailable)
- Re-indexed literature review to correctly attribute the tolperisone/Parkinson's-disease MMP-9 signal (PMID 38513594) to its actual disease category, since it was misfiled under an unrelated candidate and may warrant separate evaluation
- Any preclinical or mechanistic data specifically connecting sodium-channel blockade to congenital cardiac or craniofacial syndromes before this candidate can be reconsidered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

