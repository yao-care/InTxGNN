---
layout: default
title: Ranibizumab
parent: Model Prediction Only (L5)
nav_order: 725
evidence_level: L5
indication_count: 10
---

# Ranibizumab
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

# Ranibizumab: From Diabetic Retinopathy and Macular Degeneration to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Ranibizumab is an anti-VEGF antibody fragment injected into the eye, originally used for retinal diseases such as diabetic retinopathy, diabetic macular edema and macular degeneration.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, supported by **18 publications** (including Phase 3 RIDE/RISE analyses and a recent randomized trial), but **no registered clinical trials** in the data compiled for this report.
Most other top predictions (mainly cataract types) have no meaningful supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetic retinopathy, diabetic macular edema, macular degeneration, retinal artery occlusion, retinopathy of prematurity (the approved indication text in the India licenses is blank) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (provisional, see note below) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, ranibizumab is an anti-VEGF-A agent. VEGF-A drives retinal vascular leakage and abnormal new vessel growth. Elevated vitreous and serum VEGF levels are documented in diabetic retinopathy (PMID 36580154).

The predicted indication is closely related to what ranibizumab already treats. Severe nonproliferative diabetic retinopathy is an earlier stage of the same disease as diabetic retinopathy and diabetic macular edema. This is closer to an on-label extension than true repurposing. Post hoc analyses of the Phase 3 RIDE/RISE trials show regression of diabetic retinopathy severity with ranibizumab (PMID 32606578). The recent Pavilion randomized trial tested a ranibizumab port delivery system in nonproliferative diabetic retinopathy without macular edema (PMID 40048178).

**Caveat:** The L1 grade rests on literature identified from titles and abstracts only. No trial records were supplied. The primary RCT reports should be checked before final sign-off.

### Other Predictions Reviewed

Nine other predictions were also reviewed. They do not support a go decision.

| Predicted Indication | Evidence Level | Assessment |
|------|------|------|
| Diabetes mellitus type 2 associated cataract | L4 | Retrieved papers address diabetic macular edema, not cataract. No mechanism for ranibizumab to treat cataract. |
| Tetanic cataract | L5 | No data. Cataract from calcium disturbance, with no VEGF link. |
| Craniostenosis cataract | L5 | No data. Rare syndromic cataract, with no VEGF link. |
| Mature cataract | L4 | Ranibizumab was only an adjunct for retinal disease during cataract surgery. It does not treat the lens opacity. |
| Immature cataract | L5 | No data and no mechanistic rationale. |
| Cortical cataract | L4 | Papers concern macular edema. One case report describes capsular block syndrome as an adverse event after injection. |
| Nuclear senile cataract | L5 | No data. Age-related lens changes are not VEGF-mediated. |
| Senile cataract | L4 | Papers concern cytokines and anti-VEGF response in retinal disease, not cataract. |
| Hemorrhagic disease of newborn | L5 | Caused by vitamin K deficiency. The two linked trials study other diseases, and the match appears to be a name-similarity artifact. |

All nine are recommended as **Hold**.

## Literature Evidence

No clinical trials are registered for the lead prediction. Evidence comes from literature. Ten of the most relevant publications are listed.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmology | Pavilion trial: ranibizumab port delivery system vs monitoring in nonproliferative diabetic retinopathy without macular edema |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Post hoc analysis of RCT (RIDE/RISE) | Ophthalmology Retina | Meta-analysis of baseline retinopathy severity and time to macular edema resolution with ranibizumab |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | Post hoc analysis of RCT (RIDE/RISE) | Clinical Ophthalmology | Predictors of early diabetic retinopathy regression with ranibizumab |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | Post hoc analysis (RIDE/RISE extension) | BMJ Open Ophthalmology | Retinopathy severity scale changes with less frequent ranibizumab after induction |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | Secondary analysis of RCT | JAMA Ophthalmology | Retinopathy change over 2 years comparing aflibercept, bevacizumab and ranibizumab |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | Secondary analysis of RCT | Retina | DRCR.net Protocol I 5-year changes in retinopathy severity with ranibizumab |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2025 | Systematic review / meta-analysis | Health Technology Assessment | Anti-VEGF drugs compared with laser photocoagulation for diabetic retinopathy |
| [42219053](https://pubmed.ncbi.nlm.nih.gov/42219053/) | 2026 | Systematic review / meta-analysis | European Journal of Pharmacology | Sustained ranibizumab port delivery for disease modification in diabetic retinopathy and macular edema |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opinion on Biological Therapy | Ranibizumab has proven effective in diabetic retinopathy, including macular edema |
| [40969370](https://pubmed.ncbi.nlm.nih.gov/40969370/) | 2025 | Retrospective cohort | Frontiers in Endocrinology | Nomogram of predictors of response to anti-VEGF plus laser in severe nonproliferative diabetic retinopathy |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 121668 | Lucentis Injection (Novartis India Ltd) | Vial of 1 ml injection | Not available in the data compiled for this report |
| 184362 | Razumab 2.3mg Injection (Intas Pharmaceuticals Ltd) | Vial of 1 injection | Not available in the data compiled for this report |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** eye infectious disease and conjunctivitis. Ranibizumab should not be used in the presence of ocular or periocular infection.
- **Case report:** capsular block syndrome has been reported after intravitreal ranibizumab in a patient with macular degeneration (PMID 38476863).
- **Drug interactions:** no interactions were found in the database query.

For full warnings and precautions, please refer to the package insert, which was not available for this report.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for severe nonproliferative diabetic retinopathy only; **Hold** for all cataract and newborn hemorrhage predictions)

**Rationale:**
Ranibizumab is already marketed in India for related retinal diseases. Its mechanism is directly relevant to diabetic retinopathy, and Phase 3 trial analyses and a recent randomized trial support retinopathy improvement. However, the evidence grade is provisional because it rests on literature without registered trial records.

**To proceed, the following is needed:**
- Review of the primary RCT reports (RIDE/RISE, Protocol I, Pavilion) to confirm the L1 grade
- The package insert from the Indian regulator or manufacturer (approved indications, warnings and contraindications are missing for both licenses)
- Detailed mechanism of action data
- Confirmation of whether severe nonproliferative diabetic retinopathy is already covered by the current Indian label, which would make this a label clarification rather than new development
- A safety monitoring plan for intravitreal injection, including infection and intraocular adverse events
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

