---
layout: default
title: D-Glucose
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
---

# D-Glucose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# D-Glucose: From Hypoglycemia Support to Open-Angle Glaucoma

## One-Sentence Summary

D-glucose is the body's fundamental monosaccharide energy substrate, classically used in clinical settings for hypoglycemia management and nutritional support, but currently not registered as a pharmaceutical product in India.
The TxGNN model predicted 10 new potential indications; **Open-Angle Glaucoma** (TxGNN score: 83.03%, prediction rank 3) carries the strongest evidence base — **5 clinical trials** and **20 publications** — including a **double-blind RCT** that directly demonstrated topical glucose can temporarily restore visual function in POAG patients.
Current evidence is classified at **L3**, supporting a **Research Question** designation for structured follow-up investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypoglycemia / nutritional support (no India registrations) |
| Predicted New Indication | Open-Angle Glaucoma |
| TxGNN Prediction Score | 83.03% |
| Evidence Level | L3 (Observational studies, meta-analyses, and one direct RCT) |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Retinal ganglion cells (RGCs) — the neurons that transmit visual signals from the retina to the brain — have among the highest energy demands of any cell in the body and depend almost exclusively on glucose as their primary fuel. The **bioenergetic hypothesis** of glaucoma, reviewed systematically in a 2008 publication (PMID 18700928), proposes that RGC death in primary open-angle glaucoma (POAG) is driven in part by energy failure at the optic nerve head: insufficient ATP generation due to mitochondrial dysfunction. This means that even when intraocular pressure (IOP) is well-controlled, RGCs may continue to degenerate due to energy substrate insufficiency — creating a rationale for glucose supplementation as a neuroprotective strategy independent of IOP management.

The epidemiological link between glucose metabolism and glaucoma is well established. Large population-based studies — including the Korean nationwide cohort (PMID 32966328) and the Australian Blue Mountains Eye Study (PMID 9111268) — show that elevated fasting plasma glucose is independently associated with OAG incidence and elevated IOP. Multiple meta-analyses (PMID 25283061) and Mendelian randomization studies in European, Japanese, and multi-ethnic populations (PMID 35622353, 36162535, 38672220) have further probed the causal relationship between glycemic traits and POAG risk. Recent investigation of SGLT2 inhibitors (PMID 40263428) — drugs that lower glucose by blocking its renal reabsorption — further implicates glucose transport as a modifiable factor in POAG.

The most compelling and direct evidence comes from a **double-blind, randomized controlled trial** published in *Ophthalmology* (PMID 24491639), which found that topically applied glucose induced **temporary visual recovery** in POAG patients. This proof-of-concept result supports the model in which locally delivering glucose energy to oxygen- and substrate-deprived RGCs can transiently rescue function, providing a direct pharmacological bridge between D-glucose and glaucoma neuroprotection.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT07290244](https://clinicaltrials.gov/study/NCT07290244) | Phase 1 | Recruiting | 18 | Single-dose safety and tolerability of ER-100 in adults with Open-Angle Glaucoma (OAG) and Non-Arteritic Anterior Ischemic Optic Neuropathy (NAION); relevant if intervention is energy-metabolism related |
| [NCT04118920](https://clinicaltrials.gov/study/NCT04118920) | Phase 1 | Active, Not Recruiting | 18 | Topical insulin eye drops for OAG — insulin stimulates RGC glucose uptake, mechanistically parallel to the case for direct glucose supplementation; 18-patient safety study |
| [NCT05405868](https://clinicaltrials.gov/study/NCT05405868) | Phase 3 | Recruiting | 496 | Double-blind, placebo-controlled trial of nicotinamide (NAM) to slow visual field loss in OAG; the largest ongoing metabolic neuroprotection trial for glaucoma, with similar bioenergetic rationale |
| [NCT04645992](https://clinicaltrials.gov/study/NCT04645992) | N/A | Unknown | 80 | Yoga + TENS in diabetic glaucoma; examines combined effects on IOP, autonomic control, and fasting blood glucose — background context only |
| [NCT03870230](https://clinicaltrials.gov/study/NCT03870230) | N/A | Recruiting | 120 | Observational study of neurovascular coupling in glaucoma; investigates RGC energy supply mechanisms independent of IOP, supporting the bioenergetic framework |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [24491639](https://pubmed.ncbi.nlm.nih.gov/24491639/) | 2014 | Double-blind RCT | *Ophthalmology* | **Central evidence**: Topical glucose induced temporary visual recovery in POAG patients; direct proof-of-concept that RGC function can be rescued by local glucose substrate delivery |
| [25283061](https://pubmed.ncbi.nlm.nih.gov/25283061/) | 2015 | Meta-analysis | *Ophthalmology* | Systematic review and meta-analysis: diabetes and elevated blood glucose levels associated with glaucoma, elevated IOP, and ocular hypertension in the general population |
| [35622353](https://pubmed.ncbi.nlm.nih.gov/35622353/) | 2022 | Mendelian Randomization | *Invest. Ophthalmol. Vis. Sci.* | MR study assessing causal associations between T2D, fasting glucose, HbA1c and POAG risk in European and East Asian populations |
| [18700928](https://pubmed.ncbi.nlm.nih.gov/18700928/) | 2008 | Review | *Clin. Exp. Ophthalmol.* | Comprehensive review of bioenergetic-based neuroprotection in POAG: energy failure at the optic nerve head as a core driver of RGC death |
| [32966328](https://pubmed.ncbi.nlm.nih.gov/32966328/) | 2020 | Population-based cohort | *PLoS One* | Nationwide Korean cohort study: fasting plasma glucose independently associated with incident OAG after adjusting for IOP |
| [36162535](https://pubmed.ncbi.nlm.nih.gov/36162535/) | 2023 | Mendelian Randomization | *Am. J. Ophthalmol.* | MR analysis of genetically predicted glycemic traits and POAG risk in a Japanese population; addresses causality amid observational controversy |
| [36237805](https://pubmed.ncbi.nlm.nih.gov/36237805/) | 2022 | Cross-sectional | *Cureus* | POAG prevalence and risk factors in T2DM patients in North India; IOP elevated in diabetics and correlated with fasting blood glucose levels |
| [9111268](https://pubmed.ncbi.nlm.nih.gov/9111268/) | 1997 | Cohort | *Ophthalmology* | Blue Mountains Eye Study (Australia): foundational investigation of the relationship between diabetes and OAG in an older community population |
| [34303323](https://pubmed.ncbi.nlm.nih.gov/34303323/) | 2022 | Interventional (non-drug) | *J. Complement. Integr. Med.* | Yoga practice reduced IOP and fasting blood glucose simultaneously in T2DM patients with high-tension POAG; confirms bidirectional glucose-IOP coupling |
| [38672220](https://pubmed.ncbi.nlm.nih.gov/38672220/) | 2024 | Mendelian Randomization | *Biomedicines* | Two-sample MR: evaluates causal roles of T2D and glycemic traits (fasting glucose, HbA1c) as exposures for POAG across multiple ancestries |

---

## Safety Considerations

Please refer to the package insert for safety information.

No key warnings, contraindications, or drug interaction data were identified in the evidence sources at the time of this evaluation. D-glucose as a physiological substrate has an extensive clinical safety record in general use; however, formal pharmacovigilance data specific to the ophthalmic repurposing context (e.g., chronic topical ocular application) is not currently available.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The bioenergetic hypothesis for RGC neuroprotection is mechanistically coherent and supported by a direct double-blind RCT demonstrating temporary visual recovery with topical glucose in POAG patients. However, this remains proof-of-concept evidence only (small sample, transient effects), and the complex epidemiological relationship between systemic glycemia and glaucoma risk introduces uncertainty about the net therapeutic direction. Evidence is currently at L3 — sufficient to justify a focused research programme, but not to support clinical application.

**To proceed, the following is needed:**
- Replicate and scale the topical glucose RCT (PMID 24491639) in an adequately powered trial with long-term visual field endpoints
- Define the optimal ophthalmic formulation: glucose concentration, vehicle (eye drops vs. gel), and dosing frequency
- Mechanistically confirm that topical glucose restores RGC ATP levels and reduces apoptotic signalling in the optic nerve
- Assess additive neuroprotective benefit when combined with first-line IOP-lowering therapy (prostaglandin analogues, beta-blockers)
- Evaluate chronic safety of topical glucose use: infection risk, corneal epithelial effects, and impact on anterior chamber glucose concentration
- Clarify whether the systemic glycemia–glaucoma epidemiological signal reflects causality or confounding, to determine whether systemic glucose modulation also carries therapeutic potential
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

