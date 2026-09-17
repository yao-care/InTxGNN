---
layout: default
title: Parnaparin
parent: Model Prediction Only (L5)
nav_order: 641
evidence_level: L5
indication_count: 3
---

# Parnaparin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Parnaparin: From Anticoagulant Therapy to Breast Fibrocystic Disease

## One-Sentence Summary

Parnaparin is a low molecular weight heparin (LMWH) used systemically for anticoagulation and thromboprophylaxis; it is **not currently marketed in Taiwan**. The TxGNN model's top-ranked prediction is **Breast Fibrocystic Disease**, but this direction is supported by **no clinical trials and no literature**, and the model's own rationale flags the association as a likely artefact of knowledge-graph proximity rather than a genuine pharmacological link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded for Taiwan (drug unmarketed); internationally used as an LMWH for anticoagulation/thromboprophylaxis |
| Predicted New Indication | Breast Fibrocystic Disease |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, drug-record-level mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). However, contextual information captured in the candidate rationale identifies Parnaparin as a **low molecular weight heparin (LMWH, ATC B01AB07)**, which produces anticoagulant effects by activating antithrombin to inhibit Factor Xa (and, to a lesser extent, thrombin/Factor IIa).

For the top-ranked prediction — breast fibrocystic disease, a benign, hormonally-driven proliferative and cystic condition of breast tissue — there is **no known or plausible mechanistic pathway** connecting Factor Xa inhibition to hormone-sensitive breast tissue pathology. No anti-inflammatory, hormonal, or growth-modulating mechanism links the two. The model's own repurposing rationale explicitly states that this high TxGNN score likely reflects **node proximity within the knowledge graph rather than a validated biological relationship**, and notes that the absence of confirmed original-indication data further weakens any mechanistic inference.

By contrast, the second-ranked candidate — thrombophilia due to Protein C deficiency (autosomal recessive) — has a coherent, class-level mechanistic rationale: LMWH agents are an established therapeutic class for thrombosis risk arising from impaired natural anticoagulant pathways. This suggests the underlying model signal for "LMWH ↔ thrombotic disease" is more biologically grounded than the top-ranked breast pathology signal, even though it is still unsupported by drug-specific trial or literature evidence in this dataset.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

No market authorizations are recorded for Parnaparin in Taiwan — the drug has 0 registered licenses and a market status of "Not Marketed." No approved-indication text is therefore available from Taiwan regulatory sources.

---

## Other Predicted Indications Under Evaluation

This evidence pack (candidate ID `TW-DB09260-multi`) evaluates three TxGNN-predicted indications for Parnaparin in parallel. For context alongside the primary prediction above:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 1 | Breast Fibrocystic Disease | 99.21% | L5 | S0 | Hold |
| 2 | Thrombophilia due to Protein C Deficiency (AR) | 99.11% | L4 | S1 | Research Question |
| 3 | Benign Mammary Dysplasia | 99.03% | L5 | S0 | Hold |

Rank 2 carries a stronger class-level mechanistic rationale (LMWH as a recognized option for thrombophilia management) and has progressed further in the internal decision pipeline (S1 vs. S0), despite lacking direct trial or literature support in this dataset. It may be a more productive direction for a formal research question than the top-ranked candidate.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the DDI query (result: not found, 0 interactions), and no warnings or contraindications data are currently available for Parnaparin in this evidence pack (DG001, Blocking severity — TFDA label warnings/contraindications not yet retrieved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Breast Fibrocystic Disease) has evidence level L5 — a model score with no supporting clinical trials or literature — and the drug's own mechanistic profile (Factor Xa inhibition) has no established pathological link to the predicted condition. In addition, a Blocking-severity data gap (missing TFDA label warnings/contraindications) prevents even a preliminary safety assessment, and Parnaparin has no current market presence in Taiwan.

**To proceed, the following is needed:**
- TFDA label data (warnings/contraindications) to clear the Blocking gap before any S1 safety review can begin
- Confirmed mechanism-of-action data from DrugBank to validate or refute the mechanistic rationale
- Original approved-indication data for Parnaparin to establish a proper baseline for similarity assessment
- If pursuing further work, prioritize the Protein C deficiency thrombophilia candidate (rank 2) over breast fibrocystic disease, given its stronger class-level mechanistic plausibility and more advanced decision-stage status (S1, Research Question)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

