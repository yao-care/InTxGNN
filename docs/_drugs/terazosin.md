---
layout: default
title: Terazosin
parent: Model Prediction Only (L5)
nav_order: 813
evidence_level: L5
indication_count: 10
---

# Terazosin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Terazosin: From Unspecified Original Indication to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Terazosin's original approved indication is not recorded in the current evidence pack (data gap). The TxGNN model predicts potential efficacy for **Hypotrichosis Simplex of the Scalp**, with a very high prediction score (99.97%), but this direction is currently supported by **no clinical trials and no literature** — the score appears to reflect graph-level co-occurrence with other hair-loss-related disease nodes ("guilt-by-association") rather than direct biological evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current evidence pack (no license/indication records) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for terazosin is not available in the current evidence pack (blocking data gap DG002). However, literature retrieved for other predicted indications in this pack (e.g., migraine, Raynaud's phenomenon) independently confirms terazosin's identity as an **alpha-1 adrenergic receptor antagonist**, historically used in cardiovascular contexts — consistent with its classification as a "cardiovascular medication" in the retrieved review literature (PMID 34779371).

For the top-ranked prediction — hypotrichosis simplex of the scalp — no clinical trial or peer-reviewed literature evidence exists in this evidence pack. The model's own rationale explicitly flags this as a low-confidence association: the high TxGNN score likely reflects proximity in the knowledge graph to other hair-related disease nodes (e.g., alopecia, congenital hypotrichosis, hypertrichosis) rather than a validated pharmacological mechanism. Notably, the evidence pack itself highlights an internal inconsistency: rank 8 ("Ambras type hypertrichosis universalis congenita" — excessive hair growth) also scores highly despite being the pharmacologically opposite phenotype to hair loss, reinforcing that this cluster of predictions may reflect semantic/topical clustering ("hair-related diseases") in the graph rather than a coherent, direction-specific pharmacological signal.

By contrast, other lower-ranked predictions in this same evidence pack — **migraine disorder** (rank 5, L3) and **Raynaud disease** (rank 7, L3) — are supported by actual human studies referencing terazosin directly, with plausible mechanistic links to alpha-1 blockade (reduced sympathetically-mediated vasospasm). These may warrant separate evaluation as stronger repurposing candidates, even though they are not the top-ranked TxGNN score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Terazosin currently has **no marketing authorization on record** in India (market status: Not Marketed; total registrations: 0). No license or product data is available in the current evidence pack.

---

## Safety Considerations

**Drug Interactions**: A DDI query returned **137 total interactions**. Representative interactions identified include (all "Moderate" severity unless noted):

| Interacting Drug | Level | Source |
|---|---|---|
| Hydrocortisone | Moderate | ddinter |
| Bupropion | Moderate | ddinter |
| Triamcinolone | Moderate | ddinter |
| Morphine | Moderate | ddinter |
| Dexamethasone | Moderate | ddinter |
| Betamethasone | Moderate | ddinter |
| Budesonide | Moderate | ddinter |
| Canagliflozin | Moderate | ddinter |
| Dapagliflozin | Moderate | ddinter |
| Prednisone | Moderate | ddinter |

Additional interactions of "Unknown" severity were also identified (e.g., Calcitriol, Pantoprazole, Glimepiride) and require further characterization. Key warnings and contraindications are not available in the current evidence pack (blocking data gap DG001 — TFDA/local label warnings and contraindications have not yet been retrieved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (hypotrichosis simplex of the scalp) has no clinical trial or literature support and is explicitly flagged by the model's own rationale as likely reflecting graph co-occurrence rather than genuine biological evidence (Evidence Level L5). Combined with two blocking/high-severity data gaps — missing label warnings/contraindications (DG001, Blocking) and missing MOA data (DG002, High) — this candidate cannot proceed to safety pre-screening (S1) at this time.

**To proceed, the following is needed:**
- Retrieve TFDA/local label warnings and contraindications (DG001) — required before any S1 safety pre-screening
- Confirm terazosin's mechanism of action via DrugBank API (DG002)
- Obtain original approved indication and license data (currently entirely absent from this evidence pack)
- If pursuing the hair-loss direction, generate or locate preclinical/mechanistic studies linking alpha-1 adrenergic blockade to hair follicle biology
- Consider parallel evaluation of the migraine (rank 5) and Raynaud disease (rank 7) candidates, which have direct human-study literature support (L3, "Research Question" status) and stronger mechanistic plausibility than the top-ranked prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

