---
layout: default
title: Nepafenac
parent: High Evidence (L1-L2)
nav_order: 587
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-30
description: "Nepafenac: predicted new indication Eye disease (evidence level L1). Approved use: Not stated in the Indian licence records. Based on the supporting lit…"
monitor_inn: "Nepafenac"
predicted_indications: ["eye disease", "optic papillitis", "hypotrichosis simplex of the scalp", "seborrheic keratosis", "von Hippel anomaly", "congenital hypotrichosis milia", "mcpherson robertson cammarano syndrome", "lagophthalmos", "vulvar inverted follicular keratosis", "vitreous detachment"]
---

# Nepafenac
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Nepafenac: From Ocular Inflammation and Pain After Cataract Surgery to Eye Disease
{: .text-alpha }

## One-Sentence Summary

Nepafenac is a topical NSAID prodrug used as an eye drop, with marketed products across India (20 valid registrations).
The TxGNN model predicts it may be effective for **eye disease**, a broad category that overlaps heavily with its existing use, supported by **40 clinical trials** and **20 publications** currently compiled for this prediction.
This is better viewed as confirmation of an existing use than as true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Indian licence records. Based on the supporting literature, it is used for pain and inflammation after cataract surgery |
| Predicted New Indication | Eye disease |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L1 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Nepafenac is a prodrug. Enzymes in eye tissue convert it to amfenac, which inhibits COX-1 and COX-2 and reduces prostaglandin synthesis. Prostaglandins drive inflammation, pain and cystoid macular edema after eye surgery, so blocking them directly addresses these problems.

The original use (inflammation and pain after cataract surgery) sits inside the broad "eye disease" category. Studies also show that topically applied nepafenac and amfenac reach the back of the eye. Trials in diabetic macular edema, epiretinal membrane surgery and retinal detachment therefore make mechanistic sense.

Currently, detailed mechanism of action data is not available in the structured drug record. The mechanism described above is drawn from the published literature.

One caveat: the Phase 3 registration trials are not what drives the L1 grade here. The grade rests on the volume of Phase 2/4 evidence and a 2024 systematic review. The Phase 3 trials listed below do exist in the compiled data, but only a subset has been individually graded for relevance.

---

## Clinical Trial Evidence

The 10 most relevant trials are listed (graded A/B first, then larger completed Phase 3 trials).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | Completed | 1342 | Nepafenac 0.3% vs 0.1% vs vehicle for inflammation and pain after cataract surgery |
| [NCT00782717](https://clinicaltrials.gov/study/NCT00782717) | Phase 2 | Completed | 263 | Nevanac 0.1% vs vehicle to reduce macular edema after cataract surgery in diabetic retinopathy |
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | Completed | 2120 | Nepafenac 0.3% for prevention and treatment of inflammation and pain after cataract surgery |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | Completed | 881 | Nepafenac 0.3% once daily vs vehicle in diabetic patients after cataract surgery |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | Completed | 819 | Companion trial, nepafenac 0.3% vs vehicle in diabetic patients after cataract surgery |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Phase 3 | Completed | 448 | Clinical equivalence of a generic nepafenac 0.3% vs Ilevro for pain and inflammation after cataract surgery |
| [NCT00333255](https://clinicaltrials.gov/study/NCT00333255) | Phase 3 | Completed | 267 | Nevanac 0.1% vs Acular LS for inflammation around cataract surgery |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Phase 3 | Completed | 260 | Nepafenac 0.1% vs placebo after cataract surgery in Chinese adults |
| [NCT00900887](https://clinicaltrials.gov/study/NCT00900887) | Phase 2 | Completed | 84 | Topical nepafenac 0.1% or ketorolac 0.5% for central thickness after photocoagulation in diabetic macular edema |
| [NCT07736690](https://clinicaltrials.gov/study/NCT07736690) | Phase 4 | Completed | 60 | Perioperative nepafenac and early recovery after epiretinal membrane surgery |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39095467](https://pubmed.ncbi.nlm.nih.gov/39095467/) | 2024 | Systematic review / network meta-analysis | Eye (London) | Compared topical NSAIDs for macular thickening and visual outcome after phacoemulsification |
| [25686158](https://pubmed.ncbi.nlm.nih.gov/25686158/) | 2015 | Cochrane review | Cochrane Database Syst Rev | Topical NSAIDs for diabetic cystoid macular oedema |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clin Exp Optom | Nepafenac in cataract surgery: high ocular penetration, low side-effect profile |
| [26502088](https://pubmed.ncbi.nlm.nih.gov/26502088/) | 2016 | Review | Dev Ophthalmol | NSAIDs in retinal diseases |
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | Comparative trial | Korean J Ophthalmol | Nepafenac 0.1% vs prednisolone 1% after micro-incisional cataract surgery |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | Randomized trial | Ophthalmology Glaucoma | Nepafenac 0.1% vs prednisolone acetate after laser peripheral iridotomy |
| [40243047](https://pubmed.ncbi.nlm.nih.gov/40243047/) | 2025 | Comparative study | Indian J Ophthalmol | Nepafenac 0.1% vs 0.3% in pseudoexfoliation after cataract surgery |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | Preclinical PK | Exp Eye Res | Topical nepafenac and amfenac reach the posterior segment of the eye |
| [17259381](https://pubmed.ncbi.nlm.nih.gov/17259381/) | 2007 | Preclinical | Diabetes | Topical nepafenac inhibited diabetes-induced retinal microvascular disease in rats |
| [17964407](https://pubmed.ncbi.nlm.nih.gov/17964407/) | 2007 | Case report | J Cataract Refract Surg | Corneal melt associated with nepafenac in a patient with graft-versus-host disease |

---

## India Market Information

The compiled data list 20 valid single-ingredient registrations. Five are shown below. The licence records do not include approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 154180 | Nepanix Eye Drop (Phoenix Pharmaceuticals) | Ophthalmic suspension, 5 ml bottle | Not stated in the records |
| 150465 | Nepalact-Z Sterile Eye Drops (Sun Pharmaceutical Industries) | Ophthalmic suspension, 5 ml bottle | Not stated in the records |
| 503 | Amplinak Ophthalmic Suspension (Allergan India) | Ophthalmic suspension, 5 ml bottle | Not stated in the records |
| 150962 | Nepastar OD Eye Drop (Mankind Pharma) | Eye drop, 3 ml bottle | Not stated in the records |
| 2876 | Avanep Eye Drop (Alembic Pharmaceuticals) | Eye drop, 5 ml packet | Not stated in the records |

---

## Safety Considerations

- **Corneal adverse events**: A published case report describes corneal melt (perforation) with nepafenac in a patient with graft-versus-host disease. Prolonged NSAID use can delay corneal healing.
- **Conditions flagged in the drug knowledge graph** (these come from a computational database, not from label text): rheumatoid arthritis, diabetes mellitus, diabetic ketoacidosis, blood coagulation disease, keratitis, keratoconjunctivitis, dry eye syndrome, xerophthalmia and corneal ulcer. Corneal and ocular surface conditions deserve particular caution.

Please also refer to the package insert for full safety information. No drug interaction data were found.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Many completed Phase 2, 3 and 4 trials, plus systematic reviews, support nepafenac for ocular inflammation, pain and macular edema around eye surgery. "Eye disease" is too broad to be a meaningful new indication, so the evidence confirms an existing use rather than a true repurposing opportunity.

**To proceed, the following is needed:**
- Define a narrow, specific indication (for example, prevention of macular edema after cataract surgery in high-risk patients such as those with diabetes) instead of "eye disease".
- Obtain the Indian package insert, including approved indications, warnings and contraindications.
- Set up monitoring for corneal adverse events (melting, delayed healing) with prolonged use.
- Complete relevance grading of the ungraded trials and confirm the Phase 3 evidence base.

**Other predictions (not recommended at this time):**
- **Vitreous detachment** (Research Question): one Phase 4 biomarker study in retinal detachment (NCT07162818, n=61), with indirect evidence and unproven clinical benefit.
- **Optic papillitis** (Hold): only preclinical and indirect evidence. Topical nepafenac is unlikely to reach the optic nerve head at therapeutic levels.
- **Hypotrichosis simplex of the scalp, seborrheic keratosis, von Hippel anomaly, congenital hypotrichosis milia, McPherson Robertson Cammarano syndrome, lagophthalmos, vulvar inverted follicular keratosis** (Hold): no trials or literature, and no plausible mechanism. For lagophthalmos, NSAIDs could worsen corneal exposure complications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

