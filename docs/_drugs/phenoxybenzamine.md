---
layout: default
title: Phenoxybenzamine
parent: 僅模型預測 (L5)
nav_order: 656
evidence_level: L5
indication_count: 2
---

# Phenoxybenzamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Phenoxybenzamine: From Pheochromocytoma-Related Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Phenoxybenzamine is a non-selective, irreversible alpha-adrenergic receptor antagonist, historically used to manage pheochromocytoma-related hypertension and peripheral vasospasm (this original indication is inferred from its DrugBank pharmacological classification, as confirmed original-indication data is currently a gap). The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-based prediction with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pheochromocytoma-related hypertension / peripheral vasospasm (inferred from drug class; confirmed indication text unavailable) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on its DrugBank (DB00925) pharmacological classification, phenoxybenzamine is known to act as a non-selective, irreversible α-adrenergic receptor antagonist, traditionally used to control hypertension and peripheral vascular spasm associated with pheochromocytoma.

The proposed link to glaucoma is theoretical: α1-receptor antagonism could, in principle, relax vascular smooth muscle in the trabecular meshwork or ciliary body and thereby influence aqueous humor outflow. However, this is a speculative pathway rather than a validated mechanism for intraocular pressure (IOP) reduction — clinically established IOP-lowering agents in this receptor family are α2-**agonists** (e.g., brimonidine), which act in the opposite pharmacological direction. Primary hereditary glaucoma is also driven by specific genetic mechanisms (e.g., MYOC, CYP1B1 mutations), which have no established direct connection to adrenergic signaling.

A second, related candidate — **open-angle glaucoma** (TxGNN score 99.48%, rank 8696) — was also flagged by the model, but likewise has zero clinical trials or literature support. Both predictions currently rest solely on knowledge-graph link scores rather than experimental or clinical validation, and the drug's known systemic effects (postural hypotension, tachycardia) raise additional feasibility questions for any ophthalmic application, for which no topical/ocular formulation data exist.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

- **Drug Interactions**: 32 interactions identified in total (DDInter), all classified as Moderate severity. Notable interacting agents include: Bupropion, Morphine, Canagliflozin, Dapagliflozin, Dronabinol, Empagliflozin, Nabilone, Ertugliflozin, Opium, Amifostine, Promethazine, Nitrous acid, Iobenguane (I-123), Epoprostenol, Iloprost, Selexipag, Treprostinil, Codeine, Hydrocodone, and Mepyramine.

(Key warnings and contraindications are not yet available — see Data Gap DG001 below.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN knowledge-graph score (Evidence Level L5) with zero clinical trials and zero literature, and the drug is not currently marketed in India (0 registrations). Combined with a Blocking-severity data gap on TFDA/local label safety information (DG001), there is insufficient evidence to advance this candidate past initial screening.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001 — Blocking; required before any S1 safety screening can occur)
- Confirmed mechanism of action and original approved indication documentation (DG002)
- Preclinical or early clinical data testing IOP-lowering effect specifically (topical or systemic)
- Ophthalmic formulation and local safety/tolerability assessment, given known systemic hypotensive effects
- At minimum, one observational study or mechanistic study to move evidence level beyond L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

