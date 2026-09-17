---
layout: default
title: Hyaluronidase
parent: High Evidence (L1-L2)
nav_order: 407
evidence_level: L1
indication_count: 10
---

# Hyaluronidase
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Hyaluronidase: From Adjunctive Enzyme Use to Diabetic Retinopathy (Vitreous Hemorrhage Clearance)

## One-Sentence Summary

Hyaluronidase has no discrete original indication on file in this evidence pack — it is a tissue-dispersing enzyme historically used as an adjuvant to other injectable/ophthalmic procedures rather than a stand-alone therapy, and it is currently **not marketed in India**. The TxGNN model's most clinically substantiated prediction is efficacy in **Diabetic Retinopathy**, specifically for clearing associated vitreous hemorrhage, supported by **4 clinical trials (including two completed Phase 3 studies)**, though dedicated literature for this exact pairing is still sparse.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file (data gap) — known real-world use as an adjuvant enzyme to enhance dispersion/absorption of co-injected agents, not a primary disease indication |
| Predicted New Indication | Diabetic Retinopathy (vitreous hemorrhage clearance) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> Note: TxGNN's single *highest-scoring* prediction in this evidence pack is actually **esotropia** (99.89%), but the only supporting literature describes diplopia/strabismus as a *complication* of hyaluronidase-containing local anesthesia — evidence pointing against, not for, a therapeutic effect. Diabetic Retinopathy is presented as the headline candidate here because it is the only prediction with completed Phase 3 trial support (decision stage S3), while esotropia remains at Hold (S0). A related sub-indication, **severe nonproliferative diabetic retinopathy**, also reached a meaningful evidence stage (L2, S2, Proceed with Guardrails) on the strength of one completed Phase 2 trial and shares the same mechanistic basis below.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Hyaluronidase is not available in this evidence pack. Based on known pharmacology, Hyaluronidase is an enzyme (hyaluronan hydrolase) that degrades hyaluronic acid, a major glycosaminoglycan component of the vitreous gel and extracellular matrix. It has long been used clinically as a dispersing/diffusing adjuvant (e.g., with local anesthetics, subcutaneous fluids, and contrast agents).

In ophthalmology, this same enzymatic activity has been developed into an intravitreal injectable formulation (ovine hyaluronidase, marketed elsewhere as **Vitrase**) intended to liquefy the vitreous gel and induce posterior vitreous detachment, thereby accelerating clearance of blood products trapped in the vitreous following diabetic retinopathy–associated hemorrhage. This is a well-established, already partially commercialized mechanism abroad rather than a novel hypothesis — the TxGNN signal here largely recapitulates known pharmacology rather than uncovering an unexpected new mechanism.

Diabetic Retinopathy and its severe non-proliferative subtype form a natural pair: both involve retinal microvascular damage leading to vitreous hemorrhage, and hyaluronidase's role is specifically in managing the hemorrhagic/opacifying sequela rather than modifying the underlying retinal vascular disease itself. This distinction matters for scoping any future indication claim.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00198510](https://clinicaltrials.gov/study/NCT00198510) | Phase 3 | Completed | 750 | Pivotal safety/efficacy study of intravitreal Vitrase (ovine hyaluronidase) for clearance of severe vitreous hemorrhage |
| [NCT00198497](https://clinicaltrials.gov/study/NCT00198497) | Phase 3 | Completed | 510 | Second pivotal Phase 3 study, same Vitrase intravitreal injection program for severe vitreous hemorrhage |
| [NCT00198471](https://clinicaltrials.gov/study/NCT00198471) | Phase 2 | Completed | 10 | Open-label study of intravitreous Vitrase to induce posterior vitreous detachment in moderate-to-severe non-proliferative diabetic retinopathy |

*One additional trial (NCT04311606, anti-VEGF therapy for thyroid eye disease) was excluded — it tests a different drug for an unrelated indication and was graded low-relevance (likely knowledge-graph co-occurrence noise).*

---

## Literature Evidence

Currently no dedicated literature is indexed under the Diabetic Retinopathy prediction itself. For background, a related prediction in this pack (Diabetic Cataract) surfaced a directly relevant review:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12757408](https://pubmed.ncbi.nlm.nih.gov/12757408/) | 2003 | Review | Drugs in R&D | Describes development of ISTA Pharmaceuticals' ophthalmic injectable ovine hyaluronidase (Vitrase) for initial treatment of vitreous hemorrhage and diabetic retinopathy, as an alternative to invasive vitrectomy |

---

## Safety Considerations

- **Drug Interactions**: 63 documented interactions on file, all classified as **Minor** severity in the excerpt reviewed. Representative interacting agents include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, triamcinolone), antihistamines (cetirizine, loratadine, chlorpheniramine, brompheniramine, acrivastine, phenyltoloxamine), local anesthetics (lidocaine, articaine), hormonal agents (estradiol, ethinylestradiol, conjugated estrogens), acetylsalicylic acid, and promethazine. No major or contraindicated interactions were identified in the data reviewed.
- Detailed prescribing warnings and contraindications (i.e., the official product label) have not yet been retrieved — this is flagged as a **blocking data gap** for a full safety assessment (see Next Steps).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The Diabetic Retinopathy (vitreous hemorrhage) prediction is backed by two completed Phase 3 trials (750 and 510 patients) plus a supporting Phase 2 study, and reflects an already-established mechanism (intravitreal hyaluronidase/Vitrase) rather than a speculative new pathway. However, the drug is currently unregistered in India, and a blocking gap in official label/safety data prevents a complete S1-level safety review.

**To proceed, the following is needed:**
- Retrieve official product label warnings, contraindications, and precautions (currently the single blocking gap, DG001)
- Confirm detailed mechanism-of-action documentation from DrugBank (DG002)
- Assess route/formulation compatibility for intravitreal ophthalmic use in the India regulatory context, given the product is not currently registered
- Treat the remaining 8 predicted indications in this pack (including the top TxGNN-scored esotropia, 99.89%) as low-priority/Hold — they lack supporting trials or literature, and in esotropia's case the only available evidence points against a therapeutic effect
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

