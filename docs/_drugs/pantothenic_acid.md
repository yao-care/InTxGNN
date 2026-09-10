---
layout: default
title: Pantothenic Acid
parent: 僅模型預測 (L5)
nav_order: 637
evidence_level: L5
indication_count: 9
---

# Pantothenic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Pantothenic Acid: From Vitamin B5 Supplementation to Congenital Prothrombin Deficiency

## One-Sentence Summary

Pantothenic acid (Vitamin B5, DrugBank DB01783) is an essential precursor of Coenzyme A (CoA) and is conventionally used as a nutritional supplement; it is not currently marketed in Taiwan and has no formal regulatory indication on file. The TxGNN model predicts it may be effective for **Congenital Prothrombin Deficiency**, but this prediction is currently supported only by **1 clinical trial of low relevance (Grade C)** and **no directly related literature**, placing it at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin B5 nutritional supplementation (no formal disease indication on file; not marketed in Taiwan) |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for pantothenic acid is not available in this evidence pack. Based on known pharmacology, pantothenic acid is the metabolic precursor of Coenzyme A (CoA), a cofactor central to fatty-acid metabolism, the tricarboxylic acid cycle, and broader energy/lipid biosynthesis. Its established clinical role is as a Vitamin B5 nutritional supplement, generally as part of B-complex formulations, rather than as a targeted therapeutic for a specific disease.

Congenital prothrombin deficiency is a hereditary coagulation disorder caused by mutations in the prothrombin (Factor II) gene. There is no known biochemical pathway connecting CoA/pantothenate metabolism to prothrombin synthesis or coagulation factor function. The evidence pack's own mechanistic assessment states this directly: the TxGNN model's high score most likely reflects **graph-topological proximity** within the knowledge graph rather than a genuine biochemical or pharmacological pathway linking the two entities.

Given this, the top-ranked prediction should be treated as a hypothesis-generation signal only, not as evidence of biological plausibility. Notably, other lower-ranked candidates in this same evidence pack — such as uterine inflammatory disease (rank 5) and urinary tract infection (rank 7) — carry direct preclinical or in-vitro mechanistic support and have already advanced to decision stage S1 ("Research Question"), making them more promising near-term leads than this top-scored candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | NA | Completed | 25 | Randomized, double-blind, placebo-controlled cross-over study of a multi-ingredient dietary supplement (L-arginine, Pycnogenol, vitamin K2, alpha-lipoic acid, vitamins B6/B12/folic acid) on endothelial function in volunteers with mild-to-moderate hypertension. **Relevance graded C** — population and endpoints are unrelated to congenital prothrombin deficiency; captured only via the general "dietary supplement" keyword match. |

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Not marketed in Taiwan — no drug license records are available for pantothenic acid in the source data.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (congenital prothrombin deficiency) has no known mechanistic link, only one weakly relevant (Grade C) clinical trial, and no supporting literature — evidence level L5, decision stage S0. Combined with the drug's non-marketed status in Taiwan and missing MOA/label data, there is insufficient evidence to proceed on this candidate at present.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (currently blocking safety pre-assessment, per DG001)
- Confirmed mechanism of action data from DrugBank or primary literature (DG002)
- Disease-specific clinical or preclinical studies directly evaluating pantothenic acid (not multi-ingredient supplements) in congenital prothrombin deficiency
- Consider redirecting evaluation priority toward the pack's stage-S1 candidates (uterine inflammatory disease, urinary tract infection), which already have direct preclinical/in-vitro mechanistic evidence and a "Research Question" recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

