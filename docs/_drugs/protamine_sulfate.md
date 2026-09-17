---
layout: default
title: Protamine Sulfate
parent: Model Prediction Only (L5)
nav_order: 702
evidence_level: L5
indication_count: 10
---

# Protamine Sulfate
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

# Protamine Sulfate: From Heparin Antagonism to Helminthiasis, Animal

## One-Sentence Summary

Protamine sulfate is a strongly cationic polypeptide best known pharmacologically as a heparin antagonist (and as the carrier protein in NPH/protamine insulin formulations); no formal original-indication or MOA record is present in this evidence pack. The TxGNN model's top-ranked signal for this drug is **Helminthiasis, Animal**, but the score is exactly at the model's baseline (50%) with an internal rank of ~1.75 million, and **no clinical trials or literature** support it. Across all 10 candidates returned, evidence is essentially absent — only one candidate (Gingivitis) has any supporting trial/literature, and even that evidence does not actually involve protamine sulfate as the tested intervention.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is not marketed in Taiwan and no formal indication text was returned (known general pharmacology: heparin reversal/anticoagulant antagonist) |
| Predicted New Indication | Helminthiasis, Animal |
| TxGNN Prediction Score | 50.00% (baseline level, not a distinguishing signal) |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (original_moa is a data gap, and no original indication is recorded). Based on generally known pharmacology, protamine sulfate is a cationic peptide that neutralizes heparin's anticoagulant activity and is also used as a slow-release carrier for insulin — neither function has an established pharmacological basis for antiparasitic activity.

The evidence pack's own analysis for this candidate is explicit on this point: there is "no known mechanistic link" between protamine sulfate and helminth infection, and the score of 0.5 sits at what appears to be the model's uninformative baseline rather than a genuine signal — an internal rank of ~1,749,451 places it deep in the tail of TxGNN's overall candidate space, not near the top. The same pattern holds for the other 9 candidates in this set (classical swine fever, hip dysplasia, viral hepatitis in animals, gingival overgrowth, and several swine/bovine veterinary diseases): all score exactly 0.5 with no mechanistic rationale offered.

The one partial exception is **Gingivitis** (rank 5 of this set), which has L4 evidence (one clinical trial, four PubMed records). However, on inspection none of that evidence actually tests protamine sulfate: the trial (NCT03792113) compares fibrin glue to sutures in periodontal surgery, and the literature covers unrelated topics (in vitro mitogenesis inhibition, nanovesicle engineering, canine gingival heparin content, and lysozyme paste in guinea pigs). The link appears to be disease-category co-occurrence rather than a tested drug effect. Overall, this evidence pack does not support a credible repurposing hypothesis for protamine sulfate at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

---

## Taiwan Market Information

Protamine sulfate is currently **not marketed in Taiwan** (0 licenses on record), so no product registration table is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Helminthiasis, Animal) carries no clinical trial or literature support and a baseline-level TxGNN score, and the evidence pack's own rationale confirms there is no plausible mechanistic link. None of the 10 returned candidates — including the sole candidate with any supporting evidence (Gingivitis, whose evidence does not actually involve protamine sulfate) — reach a level justifying further evaluation.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — currently a blocking data gap (DG001) preventing any S1 safety assessment
- Confirmed mechanism-of-action data from DrugBank (DG002)
- A re-run of TxGNN scoring or an alternate indication list, since all current candidates cluster at an uninformative baseline score with no differentiating signal
- If pursued further, independent verification of a genuine drug-level (not disease-category) association before considering the Gingivitis lead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

