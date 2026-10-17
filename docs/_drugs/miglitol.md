---
layout: default
title: Miglitol
parent: Model Prediction Only (L5)
nav_order: 552
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Miglitol: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Miglitol"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pancreatic agenesis", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
---

# Miglitol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Miglitol: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Miglitol is an oral intestinal alpha-glucosidase inhibitor, originally used to control blood sugar in type 2 diabetes mellitus.
The TxGNN model ranks **classic stiff person syndrome** as its top prediction, but **no clinical trials and no publications** support it, so it is a model-only signal.
Among Miglitol's 10 predicted indications, the only one with real clinical evidence is **type 1 diabetes mellitus** (1 Phase 3 trial and 9 publications), covered below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (the Indian licence records contain no indication text, so this comes from the knowledge-graph indication data) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L5 (model prediction only) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 18 (all valid, single-ingredient) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally recorded in the data compiled for this report. Miglitol is known to be an intestinal alpha-glucosidase inhibitor. It delays carbohydrate digestion and lowers the rise in blood glucose after meals. It acts mainly in the gut, and its systemic effects are minimal.

The review of this prediction found **no plausible mechanistic link** between Miglitol and classic stiff person syndrome. Stiff person syndrome is an autoimmune neurological disorder, usually associated with GAD65 antibodies. Miglitol has no known effect on the nervous system or the immune system.

The high score most likely reflects network proximity in the knowledge graph. GAD65 autoimmunity is shared with type 1 diabetes, so stiff person syndrome sits close to diabetes in the graph. It does not reflect a direct drug-target relationship. The second-ranked prediction, focal stiff limb syndrome (score 99.87%), is a related disorder and is likely driven by the same association.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for classic stiff person syndrome.

---

## Literature Evidence

Currently no related literature available for classic stiff person syndrome.

---

## Other Predicted Indications

The model returned 10 predictions with scores between 99.60% and 99.87%. Only one has clinical evidence.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 1 | Classic stiff person syndrome | 99.87% | L5 | Hold. Graph proximity to diabetes/autoimmunity only. |
| 2 | Focal stiff limb syndrome | 99.87% | L5 | Hold. Same reasoning as rank 1. |
| 3 | Thiamine-responsive dysfunction syndrome | 99.87% | L5 | Hold. The disease features diabetes, but Miglitol would at best treat hyperglycaemia symptomatically. |
| 4 | Opsismodysplasia | 99.87% | L5 | Hold. Only a tenuous insulin/PI3K pathway link. |
| 5 | Drug-induced localized lipodystrophy | 99.73% | L5 | Hold. No mechanism for reversing fat loss. |
| 6 | Centrifugal lipodystrophy | 99.72% | L5 | Hold. No direct rationale. |
| 7 | Pancreatic agenesis | 99.71% | L5 | Hold. Could only blunt post-meal glucose as an adjunct and cannot replace insulin. |
| 8 | Pressure-induced localized lipoatrophy | 99.71% | L5 | Hold. No mechanistic link. |
| 9 | Idiopathic localized lipodystrophy | 99.70% | L5 | Hold. No mechanistic link. |
| 10 | **Type 1 diabetes mellitus** | 99.60% | L1 (provisional) | Research question. Biologically plausible adjunct to insulin. |

### Best-Supported Prediction: Type 1 Diabetes Mellitus

Miglitol delays carbohydrate absorption, and this does not depend on the body's own insulin secretion. It is therefore biologically plausible as an add-on to insulin for after-meal blood sugar spikes in type 1 diabetes. This is an adjunctive, symptomatic use within the diabetes class. It does not modify the disease, and the benefit is modest.

**Clinical trial**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00213109](https://clinicaltrials.gov/study/NCT00213109) | Phase 3 | Completed | Not reported | Open trial of Miglitol's efficacy and safety in type 1 diabetes patients treated with insulin. |

This is an open trial, likely single-arm, and enrollment is not reported. It does not clearly qualify as a randomized controlled Phase 3 trial. The L1 grade is therefore provisional, and the design and results should be verified. Under the stated level definitions (at least 2 completed Phase 3 RCTs), a single open-label trial would not reach L1.

**Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24843410](https://pubmed.ncbi.nlm.nih.gov/24843410/) | 2010 | Clinical study | J Diabetes Investig | Miglitol plus insulin for type 1 diabetes patients who have sharp post-meal glucose rises despite intensive insulin therapy. |
| [21869539](https://pubmed.ncbi.nlm.nih.gov/21869539/) | 2011 | Clinical study | Endocr J | 11 patients on intensive insulin therapy took Miglitol 25-50 mg three times daily. Insulin doses, body weight, hypoglycaemia and incretin responses were assessed. |
| [2060451](https://pubmed.ncbi.nlm.nih.gov/2060451/) | 1991 | Clinical study | Diabetes Care | Effects on meal glucose tolerance and insulin timing in type 1 diabetes. |
| [2180090](https://pubmed.ncbi.nlm.nih.gov/2180090/) | 1990 | Clinical study | S Afr Med J | In 11 patients, 50 mg Miglitol significantly lowered post-meal glucose rises versus placebo at 30 and 60 minutes. |
| [2663321](https://pubmed.ncbi.nlm.nih.gov/2663321/) | 1989 | Clinical study (single-blind) | Diabetes Res | In 13 patients, Miglitol significantly reduced the area under the glucose curve versus placebo, with no reduction in fasting glucose. |
| [3653827](https://pubmed.ncbi.nlm.nih.gov/3653827/) | 1987 | Clinical study | Fortschr Med | Improved metabolic control and good tolerance in insulin-dependent diabetes. |
| [12073790](https://pubmed.ncbi.nlm.nih.gov/12073790/) | 2002 | Review | Rev Med Liege | Pharmacological approaches to post-meal hyperglycaemia, including alpha-glucosidase inhibitors. |
| [11460577](https://pubmed.ncbi.nlm.nih.gov/11460577/) | 2001 | Review | Exp Clin Endocrinol Diabetes | Overview of oral hypoglycaemic agents, including alpha-glucosidase inhibitors. |
| [33268615](https://pubmed.ncbi.nlm.nih.gov/33268615/) | 2020 | Case report | J UOEH | SGLT2 inhibitor effects in two type 1 diabetes patients, one already taking Miglitol. Only indirectly relevant to Miglitol. |

---

## India Market Information

Eighteen valid single-ingredient registrations are on file. The records contain no approved-indication text. The five below are examples.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 142594 | Migset 25mg Tablet (Cipla) | Strip of 10 tablets | Not specified in the data |
| 136339 | Mignar 50 Tablet (Glenmark) | Strip of 15 tablets | Not specified in the data |
| 101510 | Glybloc 50mg Tablet (Torrent) | Strip of 10 tablets | Not specified in the data |
| 76480 | Etilox 25mg Tablet (Sun Pharma) | Strip of 10 tablets | Not specified in the data |
| 143524 | Miglit 50mg Tablet (Biocon) | Strip of 10 tablets | Not specified in the data |

All products are oral tablets in 25 mg and 50 mg strengths.

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the Indian package insert.

- **Knowledge-graph contraindication signals** (derived from the graph, not from label text): kidney disease, pyoureter, inflammatory bowel disease, ulcerative colitis, infectious disease, hypoglycaemia, injury.
- **Drug interactions**: 241 interactions are recorded. Examples at **Moderate** level include phenylephrine, pseudoephedrine, epinephrine, formoterol, salbutamol, acetazolamide, hydrochlorothiazide, ethinylestradiol, estradiol, hydrocortisone, triamcinolone, ethanol, alpelisib, aripiprazole, asenapine and asparaginase. Examples at **Minor** level include ranitidine and topical hydrocortisone or alclometasone.
- **Practical concerns in type 1 diabetes use**: gastrointestinal side effects are common. Because Miglitol delays carbohydrate absorption, hypoglycaemia must be treated with glucose rather than sucrose.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, classic stiff person syndrome, rests only on a graph-based association with no mechanistic link, no trials and no publications. The nine other predictions are also model-only, except type 1 diabetes. That one has a plausible adjunctive role and several small clinical studies, but it is a modest, symptomatic benefit and is not a new disease target.

**To proceed, the following is needed:**
- For stiff person syndrome, a credible mechanistic hypothesis and preclinical or clinical evidence. Without these, it should not be pursued.
- For type 1 diabetes, verification of the design, size and results of NCT00213109, and a decision on whether the evidence level can be confirmed.
- The Indian package insert, to obtain approved indications, warnings and contraindications.
- Formal mechanism of action data in the drug record.
- A safety monitoring plan covering hypoglycaemia management, gastrointestinal tolerability and kidney disease.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

