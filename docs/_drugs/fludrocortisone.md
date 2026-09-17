---
layout: default
title: Fludrocortisone
parent: Model Prediction Only (L5)
nav_order: 358
evidence_level: L5
indication_count: 8
---

# Fludrocortisone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

# Fludrocortisone: From Adrenocortical Insufficiency to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Fludrocortisone is a synthetic mineralocorticoid internationally used for adrenocortical insufficiency (Addison's disease) and orthostatic hypotension; it is not currently marketed in Taiwan. The TxGNN model's top-ranked prediction is **Primary Cutaneous T-Cell Lymphoma**, but this candidate is supported by **0 clinical trials** and only **1 unrelated case report**, and the evidence pack's own mechanistic review flags it as a likely knowledge-graph embedding false positive.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Taiwan registry (drug not marketed); internationally documented for adrenocortical insufficiency and orthostatic hypotension — general pharmacological knowledge, not TW label data |
| Predicted New Indication | Primary Cutaneous T-Cell Lymphoma |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Fludrocortisone's known pharmacology is mineralocorticoid receptor agonism with weak glucocorticoid activity; the weak glucocorticoid component is the only plausible bridge to an anti-inflammatory/immunomodulatory effect relevant to a lymphoproliferative skin disease.

However, this bridge is theoretical only. Cutaneous T-cell lymphoma (CTCL) is conventionally managed with potent topical or systemic **glucocorticoids** and other lymphoma-directed therapies, not mineralocorticoid-predominant agents like fludrocortisone — there is no established pharmacological precedent for this use. The single literature hit returned by the evidence collection (a 1967 case report on "Pathergic granulomatosis") is not about CTCL and provides no mechanistic or clinical support.

Given the absence of any clinical trials, ICTRP records, or relevant literature, the evidence pack's own analysis concludes this is most likely a knowledge-graph embedding artifact rather than a biologically grounded signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6028675](https://pubmed.ncbi.nlm.nih.gov/6028675/) | 1967 | Case Report | Archives of Dermatology | Case report on "Pathergic granulomatosis"; no abstract available and no direct relevance to CTCL treatment |

## Taiwan Market Information

No Taiwan drug licenses are currently on record for fludrocortisone (market status: Not marketed, total registrations: 0).

## Safety Considerations

- **Drug Interactions**: 446 documented interactions on record (source: DDInter). Notable entries include: **Bupropion (Major)**; Moderate-level interactions with antidiabetic agents (Acarbose, Alogliptin, Pioglitazone, Canagliflozin, Dapagliflozin, Empagliflozin, Linagliptin, Chlorpropamide, Albiglutide, Dulaglutide), antifungals (Amphotericin B and its lipid complex form), Clarithromycin, Aprepitant, Acetylsalicylic acid, laxatives (Bisacodyl, Picosulfuric acid), and anabolic steroids (Oxandrolone, Oxymetholone).

TFDA-specific warnings and contraindications are not currently available (Blocking data gap, DG001) — please refer to the official package insert once obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (CTCL) has an L5 evidence level — no clinical trials, no relevant literature, and a mechanistic rationale that the evidence pack itself assesses as an unsupported knowledge-graph artifact. There is no basis to advance this candidate further at this time.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a Blocking gap (DG001)
- Confirmed mechanism of action data via DrugBank — currently a High-severity gap (DG002)
- Any preclinical or mechanistic study specifically linking mineralocorticoid/glucocorticoid signaling to CTCL pathophysiology
- Consider separately evaluating the rank-6 candidate ("eye disease," broadly capturing **geographic atrophy / dry age-related macular degeneration**), which is supported by a completed Phase 1b intravitreal safety trial (PMID 36161841) and a mechanistic retinal anti-inflammatory study (PMID 34509498) — substantially stronger evidence than the top-ranked CTCL candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

