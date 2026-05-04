---
layout: default
title: Alfuzosin
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Alfuzosin
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

# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is a selective alpha-1 adrenergic receptor antagonist primarily approved for the treatment of benign prostatic hyperplasia (BPH), where it relaxes smooth muscle in the prostate and bladder neck to improve urinary flow.
The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita**, an extremely rare congenital disorder characterised by excessive hair growth over the entire body.
Currently, **0 clinical trials** and **0 publications** directly support this repurposing direction, representing the weakest possible evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign Prostatic Hyperplasia (BPH) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.9999% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Alfuzosin is a selective alpha-1 adrenergic receptor (α₁-AR) antagonist. It blocks post-synaptic α₁ receptors in the smooth muscle of the prostate capsule, prostatic urethra, and bladder neck, thereby reducing urethral resistance and improving urinary outflow in men with BPH. Its selectivity for α₁ receptors in the lower urinary tract underpins its established clinical role.

Ambras type hypertrichosis universalis congenita is a profoundly rare genetic disorder caused by a chromosomal rearrangement near the TRPS1 gene on chromosome 8q24, which disrupts transcriptional regulation of hair follicle development. The condition manifests as excessive, generalized hair growth present from birth. Although α₁ adrenergic receptors are expressed in dermal papilla cells and pilosebaceous units, there is no known pathway by which α₁ receptor blockade could reverse or modulate a constitutional TRPS1-driven developmental programme.

The high TxGNN score most likely reflects graph-topological proximity within the knowledge graph — a path connecting adrenergic signalling → hair follicle biology → hair overgrowth disorders — rather than a mechanistically specific drug–disease interaction. This interpretation is reinforced by the observation that the same model simultaneously predicts Alfuzosin for both hypertrichosis (hair excess) and hypotrichosis (hair loss) conditions in this batch, a biologically contradictory pairing that strongly suggests non-specific clustering rather than genuine therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for Alfuzosin in Ambras type hypertrichosis universalis congenita.

---

## India Market Information

Alfuzosin is currently **not marketed in India** and holds **no product licences**. No regulatory authorisation records are available.

---

## Safety Considerations

Please refer to the package insert for key warnings and contraindications, as this data was not available in the current Evidence Pack.

**Drug Interactions:** Alfuzosin has a total of **198 documented interactions**. The following represent the highest-risk combinations:

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Cisapride | **Major** | Risk of additive QT prolongation and serious cardiac arrhythmia |
| Clarithromycin | **Major** | CYP3A4 inhibition markedly increases Alfuzosin plasma levels, raising hypotension and QT risk |
| Dolasetron | **Major** | Additive QT-prolonging effect; arrhythmia risk |
| Famotidine | Moderate | Potential pharmacodynamic interaction |
| Aprepitant | Moderate | CYP3A4 modulation may alter Alfuzosin exposure |
| Bupropion | Moderate | CNS/cardiovascular additive effects |
| Canagliflozin | Moderate | Additive hypotensive risk |
| Dapagliflozin | Moderate | Additive hypotensive risk |
| Empagliflozin | Moderate | Additive hypotensive risk |
| Levofloxacin | Moderate | Potential QT-prolonging interaction |

> ⚠️ The three **Major** interactions (Cisapride, Clarithromycin, Dolasetron) should be treated as contraindicated combinations in clinical practice due to cardiac arrhythmia risk.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications for Alfuzosin in this batch are classified at Evidence Level L5, meaning they rest solely on model prediction with zero supporting clinical trials or directly relevant publications. The top-ranked indication — Ambras type hypertrichosis universalis congenita — is a monogenic developmental disorder for which alpha-1 receptor blockade has no plausible therapeutic mechanism. The simultaneous prediction of both hypertrichosis and hypotrichosis (opposing phenotypes) within the same batch further indicates that the model is capturing topological noise in the hair follicle disease cluster rather than a genuine pharmacological signal. Additionally, Alfuzosin has no established market presence in India, making regulatory and commercial pathways for any new indication significantly more complex.

**To proceed, the following would be needed:**

- Retrieve and review the full Alfuzosin prescribing information to document approved indications, contraindications, and boxed warnings (DG001 — currently Blocking)
- Obtain complete MOA data from DrugBank to enable rigorous mechanistic linkage analysis (DG002 — currently High severity gap)
- Conduct hypothesis-driven preclinical research establishing whether α₁ receptor signalling has any measurable effect on TRPS1 pathway activity or hair follicle phenotype before any clinical consideration is warranted
- If a more mechanistically credible indication is identified in future TxGNN runs (e.g., a vascular or smooth-muscle condition), a fresh Evidence Pack targeting that indication should be generated

> *This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

