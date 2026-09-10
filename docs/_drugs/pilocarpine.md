---
layout: default
title: Pilocarpine
parent: 僅模型預測 (L5)
nav_order: 663
evidence_level: L5
indication_count: 1
---

# Pilocarpine
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

# Pilocarpine: From Unrecorded Original Indication to Primary Hereditary Glaucoma

## One-Sentence Summary

Pilocarpine (DrugBank DB01085) has no recorded original indication or mechanism-of-action data in this evidence pack — both are flagged as gaps. The TxGNN model predicts a link to **Primary Hereditary Glaucoma** with a **99.83% prediction score**, but this is supported by **0 clinical trials** and **0 publications**, and the model's own rationale text notes that pilocarpine's muscarinic-agonist mechanism is already a well-established glaucoma treatment mechanism — meaning this may reflect a data-completeness gap rather than a genuinely novel repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (see data gap note below) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L4 (mechanism/preclinical only, no trials or literature) |
| Taiwan Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a Blocking/High-severity data gap in this pack). Based on general pharmacological knowledge captured in the model's own rationale, pilocarpine is a muscarinic (M3) receptor agonist acting on the ciliary muscle and iris sphincter, producing miosis and increased trabecular outflow of aqueous humor — a mechanism that lowers intraocular pressure (IOP).

This mechanism is directly relevant to glaucoma pathophysiology (impaired aqueous outflow → elevated IOP → optic nerve damage), including primary hereditary forms. However, the model's own repurposing rationale explicitly cautions that this is a **well-established, not novel**, pharmacological link — pilocarpine's IOP-lowering effect on glaucoma is already textbook knowledge, not a newly discovered association. Combined with the fact that this evidence pack has no recorded original indication for the drug at all, the prediction may largely be reproducing an already-known drug–disease relationship rather than surfacing a new repurposing opportunity.

**Recommended priority**: verify whether the "no original indication" and "no MOA" data gaps are a database omission (i.e., pilocarpine's glaucoma indication was simply not captured) before treating this as a novel hypothesis worth independent investment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions**: 102 interactions identified via DDInter. Notable Moderate-level interactions are with other anticholinergic/antimuscarinic agents, where pilocarpine's cholinergic agonism would pharmacodynamically oppose their effect:

| Interacting Drug | Level | Source |
|---|---|---|
| Hyoscyamine | Moderate | ddinter |
| Atropine | Moderate | ddinter |
| Atropine (ophthalmic) | Moderate | ddinter |
| Glycopyrronium | Moderate | ddinter |
| Glycopyrronium (topical) | Moderate | ddinter |
| Clidinium | Moderate | ddinter |
| Dicyclomine | Moderate | ddinter |
| Mepenzolate | Moderate | ddinter |
| Methscopolamine | Moderate | ddinter |
| Propantheline | Moderate | ddinter |
| Scopolamine | Moderate | ddinter |
| Scopolamine (ophthalmic) | Moderate | ddinter |
| Trospium | Moderate | ddinter |

An additional ~89 interactions (including Pantoprazole, Omeprazole, Lansoprazole, Metformin, Morphine, Epinephrine, Clotrimazole) are logged at "Unknown" severity level and require individual review before clinical use.

No TFDA package-insert warnings or contraindications are available in this pack — this is logged as a **Blocking** data gap (DG001) and must be resolved before any safety pre-assessment (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is backed by mechanism plausibility only (L4), with no clinical trials or literature, no Taiwan market presence, and a Blocking data gap on TFDA label warnings/contraindications that prevents even a baseline safety assessment. Additionally, the model's own rationale suggests this may reflect an already-known drug–disease relationship rather than a genuine new signal.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) to resolve DG001 (Blocking)
- Confirmed mechanism of action from DrugBank to resolve DG002 (High)
- Confirmation of pilocarpine's actual original/approved indications (currently blank in this pack) to determine whether "Primary Hereditary Glaucoma" is truly a new indication or an existing one
- Targeted clinical trial and literature search once the above is resolved, to establish a higher evidence level before advancing past S1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

