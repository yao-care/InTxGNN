---
layout: default
title: Apremilast
parent: 僅模型預測 (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Apremilast
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

# Apremilast: From Psoriatic Arthritis to Migraine Disorder

## One-Sentence Summary

Apremilast (Otezla®) is an oral selective phosphodiesterase-4 (PDE4) inhibitor, approved internationally for psoriatic arthritis and plaque psoriasis, but not currently registered in India.
The TxGNN model predicts it may be effective for **Migraine Disorder**, achieving the highest prediction score (98.66%) among all 10 predicted indications.
However, this prediction is supported by **0 clinical trials** and **0 relevant publications** — this remains a knowledge-graph inference with no empirical validation to date.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Psoriatic arthritis / Plaque psoriasis (per international approvals; India regulatory data unavailable) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 98.66% |
| Evidence Level | L5 (Model prediction only, no actual studies) |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current regulatory dataset. Based on published literature (PMID 24797159; PMID 20525198), Apremilast is a selective small-molecule inhibitor of phosphodiesterase 4 (PDE4), the predominant phosphodiesterase isoform in immune and inflammatory cells. By blocking PDE4, Apremilast prevents the hydrolysis of cyclic AMP (cAMP), sustaining elevated intracellular cAMP. This cascade suppresses pro-inflammatory cytokines (TNF-α, IL-6, IL-12, IL-17, IL-23) and upregulates anti-inflammatory IL-10 — an anti-inflammatory profile that underlies its efficacy in psoriatic arthritis and psoriasis.

The theoretical connection to migraine rests on neuroinflammation. Activation of meningeal mast cells, release of inflammatory peptides around the trigeminovascular system, and dural neurogenic inflammation are recognized contributors to migraine susceptibility. Since PDE4 is expressed in neural and glial tissue and PDE4 inhibition can dampen neuroinflammatory cytokine cascades, a hypothesis can be constructed that Apremilast may raise the migraine attack threshold by reducing neuroinflammatory tone.

However, the core pathophysiology of migraine — CGRP-mediated vasodilation, trigeminovascular activation, and cortical spreading depression (CSD) — is not directly governed by the PDE4–cAMP axis. No preclinical animal model data or human clinical studies have tested this hypothesis directly. The TxGNN score of 98.66% reflects connectivity in a knowledge graph, not an empirical signal from trial or laboratory data.

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
Despite receiving the highest TxGNN prediction score among all 10 candidates, there is zero preclinical or clinical evidence for Apremilast in migraine disorder. The mechanistic bridge between PDE4 inhibition and migraine pathophysiology is theoretical only and has not been investigated in any experimental model.

**To proceed, the following is needed:**
- Preclinical neuroinflammation studies in established migraine models (e.g., dural plasma extravasation model, cortical spreading depression model, trigeminal ganglion inflammatory preparation)
- Investigation of PDE4 isoform expression and cAMP signaling in trigeminal ganglia and meningeal tissue
- Mechanistic data gap resolution: MOA documentation from DrugBank (Data Gap DG002)
- Safety data gap resolution: package insert warnings and contraindications from CDSCO/international label (Data Gap DG001)
- Drug-drug interaction database verification before any study initiation

---

> **Note on Secondary Predictions — Rheumatoid Arthritis (Rank 3)**
>
> Among all 10 TxGNN predictions, **Rheumatoid Arthritis (TxGNN score: 98.09%, Evidence Level: L2)** is substantially more actionable than migraine disorder:
>
> - **1 completed Phase 2 RCT** (NCT01250548, n=34) provides direct proof-of-concept in active RA
> - **1 terminated Phase 2 RCT** (NCT01285310, n=237, double-blind placebo-controlled) represents the largest Apremilast RA dataset — its termination is a meaningful negative signal warranting investigation of the stopping reason
> - **19 publications** span Phase 2 RCT results (PMID 25779750), in vitro mechanistic studies (PMID 20525198), preclinical in vivo arthritis models (PMID 30072998), PK/PD data (PMID 26097790), and drug approval reviews (PMID 24797159)
>
> The RA indication carries a **"Research Question"** recommendation and warrants a dedicated evidence review before final go/hold determination. The terminated large trial is the key outstanding question to resolve.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

