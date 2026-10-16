---
layout: default
title: Hyaluronidase
parent: Model Prediction Only (L5)
nav_order: 411
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Hyaluronidase: predicted new indication Top TxGNN rank: esotropia . Best-supported candidate: diabetic retino… (evidence level L5). Approved use: Not stated in the compiled licence data"
monitor_inn: "Hyaluronidase"
predicted_indications: ["esotropia", "amenorrhea (disease)", "severe nonproliferative diabetic retinopathy", "renal tubular acidosis", "dermatitis", "diabetic retinopathy", "acrodermatitis chronica atrophicans", "diabetic cataract", "neonatal dermatomyositis", "non-syndromic esophageal malformation"]
---

# Hyaluronidase
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

# Hyaluronidase: From an Adjuvant Enzyme (No Approved Indication on Record) to Diabetic Retinopathy

## One-Sentence Summary

Hyaluronidase is an enzyme that breaks down hyaluronan in tissue. It is marketed in India as an injectable, but the approved indication text was not available in the data compiled for this report.
The TxGNN model's top-ranked prediction is **esotropia**, but the evidence supports it only as a complication of anesthetic blocks, not as a therapy. The best-supported candidate is **diabetic retinopathy**, which has **3 clinical trials** (2 completed Phase 3 trials, both in vitreous hemorrhage) and **19 publications**.
This report therefore evaluates diabetic retinopathy as the lead candidate and also summarises the other predictions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the compiled licence data |
| Predicted New Indication | Top TxGNN rank: esotropia (evidence supports an adverse-event link only). Best-supported candidate: diabetic retinopathy |
| TxGNN Prediction Score | Esotropia 99.89%; diabetic retinopathy 99.71% |
| Evidence Level | Diabetic retinopathy: L1 (as scored, based on two completed Phase 3 trials in vitreous hemorrhage; efficacy results not reviewed). Esotropia: L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Proceed with Guardrails (diabetic retinopathy, as a research question only); Hold for all other predictions |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, hyaluronidase is an enzyme that degrades hyaluronan, a component of the extracellular matrix. It is widely used to help other injected drugs spread through tissue. In the eye, it acts as a "pharmacologic vitreolysis" agent: it liquefies the vitreous gel and can promote posterior vitreous detachment.

**Diabetic retinopathy (the best-supported prediction).** Hyaluronan metabolism is dysregulated in proliferative diabetic retinopathy and appears to drive inflammation and new blood vessel growth. Preclinical studies (diabetic rats, the HIF-1α pathway, the retinal endothelial glycocalyx in mice) support a biological rationale. Intravitreal ovine hyaluronidase (Vitrase) was tested in large Phase 3 trials for clearing severe vitreous hemorrhage, a common complication of diabetic eye disease. However, hyaluronidase is not an established treatment for diabetic retinopathy, and anti-VEGF therapy remains the standard of care.

**Other predictions.** The link to esotropia reflects a case report in which strabismus appeared as a complication after anesthetic blocks that included hyaluronidase. It does not reflect therapeutic benefit. For dermatitis, the literature points in the opposite direction: inhibiting hyaluronidase improved experimental dermatitis in mice, and hyaluronidase injection carries allergic risks. Amenorrhea, renal tubular acidosis, acrodermatitis chronica atrophicans, neonatal dermatomyositis and non-syndromic esophageal malformation have no meaningful supporting data. Diabetic cataract is supported only by indirect surgical-adjuvant papers.

---

## Clinical Trial Evidence

Trials for the lead candidate, diabetic retinopathy:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00198497](https://clinicaltrials.gov/study/NCT00198497) | Phase 3 | Completed | 510 | Safety and efficacy of intravitreal ovine hyaluronidase (Vitrase) for clearing severe vitreous hemorrhage; efficacy results were not available for this review |
| [NCT00198510](https://clinicaltrials.gov/study/NCT00198510) | Phase 3 | Completed | 750 | Companion trial to NCT00198497 with the same drug and route; results were not available for this review |
| [NCT00198471](https://clinicaltrials.gov/study/NCT00198471) | Phase 2 | Completed | 10 | Open-label, single-arm study of intravitreal Vitrase to induce posterior vitreous detachment in moderate to severe non-proliferative diabetic retinopathy; supports feasibility only |

No clinical trials are registered for the other nine predicted indications.

---

## Literature Evidence

Papers for diabetic retinopathy (priority given to reviews and mechanistic work; the 1960s Argentine case reports and unrelated items are omitted):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17713597](https://pubmed.ncbi.nlm.nih.gov/17713597/) | 2007 | Review | Experimental Diabetes Research | Overview of present and future pharmacotherapies for diabetic retinopathy |
| [20939804](https://pubmed.ncbi.nlm.nih.gov/20939804/) | 2011 | Review | Current Pharmaceutical Biotechnology | Pharmacologic vitreolysis; intravitreal ovine hyaluronidase was effective in clearing vitreous hemorrhage |
| [41789111](https://pubmed.ncbi.nlm.nih.gov/41789111/) | 2026 | Mechanistic study | Frontiers in Immunology | Dysregulated hyaluronan metabolism drives inflammation and angiogenesis in proliferative diabetic retinopathy |
| [23847321](https://pubmed.ncbi.nlm.nih.gov/23847321/) | 2013 | Preclinical | Invest Ophthalmol Vis Sci | Enzyme-induced vitreolysis may slow diabetic retinopathy progression through the HIF-1α pathway |
| [19050667](https://pubmed.ncbi.nlm.nih.gov/19050667/) | 2009 | Preclinical (rat) | Retina | Feasibility of inducing posterior vitreous detachment with plasmin and hyaluronidase in diabetic rats |
| [30445048](https://pubmed.ncbi.nlm.nih.gov/30445048/) | 2019 | Preclinical (mouse) | Experimental Eye Research | Effect of diabetes and hyaluronidase on the retinal endothelial glycocalyx |
| [12757408](https://pubmed.ncbi.nlm.nih.gov/12757408/) | 2003 | Drug profile | Drugs in R&D | Vitrase developed for vitreous hemorrhage and diabetic retinopathy |
| [34293791](https://pubmed.ncbi.nlm.nih.gov/34293791/) | 2022 | Pharmacokinetic study | Ophthalmic Plast Reconstr Surg | Examines whether retrobulbar hyaluronidase reaches the vitreous cavity |
| [19644368](https://pubmed.ncbi.nlm.nih.gov/19644368/) | 2009 | Review | Current Opinion in Ophthalmology | Changing treatment paradigms in diabetic retinopathy |
| [19668479](https://pubmed.ncbi.nlm.nih.gov/19668479/) | 2007 | Review | Clinical Ophthalmology | Clinical and economic review of diabetic retinopathy management |

For other predictions, the literature is limited to a case report of strabismus after cataract surgery under local anesthesia (esotropia, [16934027](https://pubmed.ncbi.nlm.nih.gov/16934027/)), a 1975 basic study of endogenous enzyme activity in endometrial tissue (amenorrhea, [1218911](https://pubmed.ncbi.nlm.nih.gov/1218911/)), and a review of allergic complications of hyaluronidase injection (dermatitis, [37145319](https://pubmed.ncbi.nlm.nih.gov/37145319/)). None of these shows therapeutic benefit.

---

## India Market Information

Seven valid single-ingredient registrations are on record. Approved indication text was not available for any of them. The five main ones are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 75207 | Entodase Injection (Entod Pharmaceuticals Ltd) | Vial of 1 ml injection | Not available |
| 103731 | Hynidase Injection (Shreya Life Sciences Pvt Ltd) | Vial of 1 injection | Not available |
| 236101 | Visial 1% Injection (Cadila Pharmaceuticals Ltd) | Prefilled syringe of 1 ml injection | Not available |
| 8884 | Anvase 1500IU Injection (Ajanta Pharma Ltd) | Vial of 5 ml injection | Not available |
| 163261 | Omnidase 1500IU Injection (Sunways India Pvt Ltd) | Vial of 1 ml injection | Not available |

Two further registrations are Hylorase 1500IU (Biosena Lifescience) and Alldase 1500IU (Uniword Pharma). All registered products are injectables.

---

## Safety Considerations

- **Drug Interactions:** 63 interactions were identified, and the 20 reviewed are all classified as Minor. They include corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone), antihistamines (promethazine, chlorpheniramine, loratadine, cetirizine), oestrogens (ethinylestradiol, estradiol, conjugated estrogens), aspirin and local anaesthetics (lidocaine, articaine).
- **Hypersensitivity:** The literature describes allergic complications of hyaluronidase injection, which are frequently misdiagnosed. A 1978 prospective study also reported a higher incidence of cystoid macular edema after cataract surgery when hyaluronidase was mixed with the local anesthetic. These are relevant to any ocular use.

Please refer to the package insert for warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (diabetic retinopathy, as a research question only). Hold for all other predicted indications.**

**Rationale:**
- Diabetic retinopathy has two completed large Phase 3 trials (510 and 750 patients) plus a small Phase 2 study with intravitreal hyaluronidase, and a coherent biological rationale. However, the Phase 3 trials targeted vitreous hemorrhage, their results were not reviewed here, and the programme did not lead to an approval for this use. Anti-VEGF therapy remains standard of care.
- The top-scoring prediction, esotropia, reflects an adverse-event association and not benefit. The other predictions have no or only indirect support, so they should be held.

**To proceed, the following is needed:**
- Full results of NCT00198497 and NCT00198510, including efficacy and safety outcomes, to decide whether the evidence moves beyond the current research-question stage
- Package insert warnings and contraindications, plus approved indication text for the Indian licences
- Detailed mechanism of action data
- An assessment of intravitreal formulation and route availability in India, since all current products are general-purpose injectables
- A safety plan covering hypersensitivity and ocular adverse events
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

