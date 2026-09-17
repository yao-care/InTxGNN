---
layout: default
title: Olopatadine
parent: Model Prediction Only (L5)
nav_order: 612
evidence_level: L5
indication_count: 1
---

# Olopatadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Olopatadine: From Allergic Conjunctivitis to Rosacea Conjunctivitis

## One-Sentence Summary

Olopatadine is an H1-antihistamine / mast cell stabilizer approved for allergic conjunctivitis.
The TxGNN model predicts it may be effective for **Rosacea Conjunctivitis**, with a prediction score of **99.41%**,
but **no clinical trials or published literature** currently support this direction — the signal is model-only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic conjunctivitis (based on known pharmacology cited in the evidence pack; not derived from Taiwan license data, as the drug is unmarketed) |
| Predicted New Indication | Rosacea Conjunctivitis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in DrugBank for this record (`original_moa` is a data gap). Based on known pharmacology, Olopatadine acts as an H1-receptor antihistamine with mast cell-stabilizing activity, and it is approved for allergic conjunctivitis — an IgE/mast cell-mediated ocular surface condition.

Rosacea conjunctivitis (ocular rosacea), however, arises from a largely different pathophysiology: meibomian gland dysfunction, *Demodex* mite overgrowth, neurovascular dysregulation, and chronic non-IgE inflammation. The mechanistic overlap with Olopatadine's known action is therefore indirect — it may address shared surface symptoms such as conjunctival redness and irritation, but it does not target the underlying causes of rosacea conjunctivitis.

The TxGNN score of 99.41% reflects knowledge-graph topological similarity between the drug and disease nodes, not a validated mechanistic or clinical relationship. Given the absence of any clinical trial or literature evidence, this prediction should be treated as an early-stage hypothesis rather than an actionable signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

**Drug Interactions**: A total of 112 potential interactions were identified via DDInter. All returned records report an "Unknown" severity level (clinical significance not graded in source data). Selected interacting drugs include: Pantoprazole, Doxycycline, Clotrimazole, Metformin, Omeprazole, Lansoprazole, Cimetidine, Triamcinolone, Prednisone, Simvastatin, Epinephrine, Hydrocortisone, Tetracycline, Potassium chloride, Sucralfate, Rosiglitazone, Nystatin, Tegaserod, Rosuvastatin, and Prednisolone. Because severity levels are unclassified, this list should be treated as a screening reference only, not a clinical risk assessment.

TFDA label warnings and contraindications are not yet available for this record (flagged as a Blocking data gap — DG001).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 — the prediction rests solely on TxGNN knowledge-graph scoring, with zero clinical trials or literature, and the proposed mechanism only partially overlaps with rosacea conjunctivitis pathophysiology. Additionally, a Blocking data gap (TFDA label warnings/contraindications) prevents even a baseline safety assessment (S1).

**To proceed, the following is needed:**
- TFDA label (warnings/contraindications) — Blocking gap, required before any safety screening (DG001)
- Confirmed mechanism of action from DrugBank/primary literature (DG002)
- Preclinical or observational evidence specifically linking Olopatadine (or its drug class) to rosacea/ocular rosacea outcomes
- Route/formulation compatibility assessment — Olopatadine is formulated as an ophthalmic solution for allergic conjunctivitis; whether this formulation is appropriate for rosacea conjunctivitis (which often involves periocular skin/lid margin disease) is currently unassessed
- Since the product holds no Taiwan license, a regulatory pathway assessment would be needed before any local development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

