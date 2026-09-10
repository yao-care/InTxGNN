---
layout: default
title: Ripasudil
parent: 僅模型預測 (L5)
nav_order: 737
evidence_level: L5
indication_count: 10
---

# Ripasudil
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

# Ripasudil: From ROCK-Inhibitor Glaucoma Therapy (Unconfirmed in Taiwan) to Hyperprolactinemia

## One-Sentence Summary

> Ripasudil (DB13165) is a Rho-kinase (ROCK) inhibitor, pharmacologically known for lowering intraocular pressure by relaxing the trabecular meshwork — though no confirmed original indication or MOA data is on file for this dataset, and the drug is **not currently marketed in Taiwan**.
> The TxGNN model's top-ranked prediction is **Hyperprolactinemia**, but this prediction is supported by **no clinical trials and no literature**, and the mechanistic rationale itself is flagged as weak.
> Several other candidates in the same prediction batch (glaucoma-spectrum diseases) show far stronger mechanistic plausibility, but likewise lack any supporting studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established in local regulatory filings (drug not marketed in Taiwan); known globally as a ROCK inhibitor used for glaucoma/ocular hypertension (per literature references cited in this evidence pack, unconfirmed here) |
| Predicted New Indication | Hyperprolactinemia (disease) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Ripasudil is not available in this evidence pack (flagged as a High-severity data gap). Based on the mechanistic notes embedded in the prediction rationale, Ripasudil is understood to be a **Rho-kinase (ROCK) inhibitor**, a drug class that acts primarily on smooth muscle relaxation and cytoskeletal regulation — most notably relaxing the trabecular meshwork to increase aqueous humor outflow, the basis for its known use in glaucoma/ocular hypertension in other markets.

For the top-ranked prediction, **Hyperprolactinemia**, the model's own rationale acknowledges the mechanistic link is weak: prolactin secretion is regulated primarily via the dopamine D2 receptor pathway, and there is no established evidence that Rho/ROCK signaling plays a key role in pituitary lactotroph function. The high TxGNN score likely reflects indirect or noisy connections in the knowledge graph rather than a genuine pharmacological relationship.

Notably, this candidate batch contains several **other predictions with substantially stronger mechanistic coherence** — see the table below. Diseases involving impaired aqueous humor outflow (Axenfeld anomaly, hydrophthalmos, primary infantile glaucoma) align directly with Ripasudil's known ROCK-inhibition/IOP-lowering mechanism, even though none currently have supporting clinical or literature evidence.

---

## Other Candidate Indications (Same Prediction Batch)

| Disease | TxGNN Score | Evidence Level | Recommendation | Mechanistic Note |
|---------|------|------|------|------|
| Hyperprolactinemia (disease) | 99.87% | L5 | Hold | Weak — no known ROCK/prolactin pathway link |
| Axenfeld anomaly | 99.86% | L5 | Research Question | Plausible — anterior chamber angle disorder overlaps with aqueous outflow mechanism |
| Hydrophthalmos | 99.85% | L5 | Research Question | Plausible — congenital glaucoma directly matches IOP-lowering mechanism |
| Glaucoma 3, primary infantile, B | 99.81% | L5 | Research Question | Plausible — shares core outflow-resistance pathology with adult glaucoma |
| Familial hyperprolactinemia | 99.79% | L5 | Hold | Weak, same rationale as rank 1 |
| Dense granule disease | 99.79% | L5 | Hold | Directionally uncertain — ROCK inhibition may impair rather than restore platelet function |
| Macrothrombocytopenia with mitral valve insufficiency | 99.77% | L5 | Hold | Directionally uncertain, no supporting data |
| Hereditary thrombocytopenia with normal platelets | 99.77% | L5 | Hold | Directionally uncertain, no supporting data |
| Transient neonatal thrombocytopenia | 99.77% | Pending | Pending | Not yet scored |
| Thrombocytopenia | 99.73% | L5 | Hold | One indirect paper (dengue-induced permeability, not Ripasudil-specific) |

---

## Clinical Trial Evidence

*(For top-ranked prediction: Hyperprolactinemia)*

Currently no related clinical trials registered

---

## Literature Evidence

*(For top-ranked prediction: Hyperprolactinemia)*

Currently no related literature available

For reference, the only literature found anywhere in this batch relates to rank 10 (Thrombocytopenia):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40189910](https://pubmed.ncbi.nlm.nih.gov/40189910/) | 2025 | Mechanistic (in vitro) | Virulence | Shows Ripasudil and other ROCK/Src inhibitors reduce dengue virus (DENV2)-induced endothelial permeability in vitro; not a direct study of Ripasudil for thrombocytopenia and not generalizable as a therapeutic indication |

---

## Taiwan Market Information

This drug is **not currently marketed in Taiwan** (未上市). No registration or license records are available in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA label warnings/contraindications are flagged as a Blocking data gap in this evidence pack — they must be obtained before any S1 safety screening can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Hyperprolactinemia) has no supporting clinical trials or literature, and the mechanistic link itself is assessed as weak by the model's own rationale. Combined with two Blocking/High-severity data gaps (missing TFDA safety label, missing MOA), there is insufficient basis to advance this candidate past S0.

**To proceed, the following is needed:**
- TFDA label data (warnings, contraindications) — currently Blocking (DG001)
- Confirmed mechanism of action from DrugBank — currently High severity (DG002)
- If pursuing repurposing further, consider redirecting research focus toward the glaucoma-spectrum candidates in this batch (Axenfeld anomaly, hydrophthalmos, primary infantile glaucoma), which have materially stronger mechanistic rationale despite currently lacking any clinical or literature support
- Original indication and regulatory status confirmation, since this drug is not currently marketed in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

