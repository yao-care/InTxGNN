---
layout: default
title: Salbutamol
parent: Model Prediction Only (L5)
nav_order: 754
evidence_level: L5
indication_count: 10
---

# Salbutamol
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

# Salbutamol: From Bronchodilation (Asthma/COPD) to Papillary Conjunctivitis

## One-Sentence Summary

Salbutamol is a β2-adrenergic receptor agonist bronchodilator whose established use in asthma and COPD is reflected throughout this evidence pack's own mechanistic notes. The TxGNN model's single highest-scoring prediction points to **Papillary Conjunctivitis**, but this candidate currently has **no clinical trials and no published literature** supporting it — it is a pure embedding-score signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in India regulatory filings (drug is unmarketed there); per this pack's own mechanistic notes, Salbutamol is a β2-agonist bronchodilator for asthma/COPD |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.9964% (rank 143 of all candidates) |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation for Salbutamol is not available in this evidence pack (data gap DG002). Based on what is captured in the pack's own rationale fields, Salbutamol is a short-acting β2-adrenoceptor agonist whose bronchodilator effect in asthma/COPD is well established — this is corroborated by the strong, high-evidence-level entries for bronchitis (L1) and obstructive lung disease (L1) elsewhere in this same candidate set.

For the top-ranked prediction itself, however, the model's own rationale is explicit that there is **no direct mechanistic link** between bronchial smooth-muscle β2-agonism and the allergic/contact inflammatory pathology of papillary conjunctivitis — the high score reflects embedding similarity only, not biological plausibility for this specific indication.

That said, a *related* candidate in this same evidence pack (rank 8, atopic conjunctivitis, L4) is supported by animal-model literature showing that topically applied β2-agonists — including salbutamol — can suppress immediate allergic conjunctivitis and exert local anti-inflammatory activity on conjunctival tissue (PMID 3666475; PMID 2906082). This suggests a plausible *class-level* mechanism for ocular surface inflammation that could indirectly lend biological hypothesis-generating support to papillary conjunctivitis, even though no study has tested this specific diagnosis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Salbutamol currently has **no registered licenses in India** (market status: Not marketed; total registrations on file: 0).

---

## Safety Considerations

Structured warnings and contraindications data is not available for Salbutamol in this evidence pack; please refer to the package insert for that information.

Drug-drug interaction (DDI) data, however, is available — 754 total interactions on file. Representative entries:

| Interacting Drug | Interaction Level | Source |
|---|---|---|
| Acarbose | Moderate | DDInter |
| Isometheptene | Moderate | DDInter |
| Famotidine | Moderate | DDInter |
| Epinephrine | Moderate | DDInter |
| Albiglutide | Moderate | DDInter |
| Acetohexamide | Moderate | DDInter |
| Alogliptin | Moderate | DDInter |
| Bisacodyl | Moderate | DDInter |
| Canagliflozin | Moderate | DDInter |
| Castor oil | Moderate | DDInter |
| Chlorpropamide | Moderate | DDInter |
| Cisapride | Moderate | DDInter |
| Clarithromycin | Moderate | DDInter |
| Dapagliflozin | Moderate | DDInter |
| Diethylpropion | Moderate | DDInter |
| Hydrocortisone | Minor | DDInter |
| Beclomethasone dipropionate | Minor | DDInter |
| Betamethasone | Minor | DDInter |
| Budesonide | Minor | DDInter |
| Dexamethasone | Minor | DDInter |

Notably, several antidiabetic agents (SGLT2 inhibitors, sulfonylureas, DPP-4 inhibitors) show Moderate-level interactions, consistent with salbutamol's known hyperglycemic effect — this warrants attention if this candidate advances toward any patient-facing use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (papillary conjunctivitis, score 99.9964%) has zero supporting clinical trials or literature, and the model's own rationale states there is no direct mechanistic link — this is an L5, model-only signal. Note that within this same evidence pack, two other candidates (bronchitis, obstructive lung disease) are rated L1/Proceed with Guardrails, but these represent Salbutamol's *already-known* bronchodilator indication rather than a novel repurposing opportunity.

**To proceed, the following is needed:**
- TFDA/India-equivalent product label with warnings and contraindications (currently Blocking data gap DG001)
- Confirmed mechanism-of-action documentation from DrugBank (data gap DG002)
- If pursuing the ocular-inflammation hypothesis: preclinical/mechanistic studies specific to papillary conjunctivitis (the related atopic conjunctivitis animal data, PMID 3666475/2906082, could inform study design)
- Given zero India market presence, a regulatory pathway assessment would be required before any clinical development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

