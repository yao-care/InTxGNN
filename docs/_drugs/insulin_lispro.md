---
layout: default
title: Insulin Lispro
parent: Model Prediction Only (L5)
nav_order: 439
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Insulin Lispro: predicted new indication Autoimmune oophoritis (evidence level L5). Approved use: Type 2 diabetes mellitus (also type 1 diabetes mellitus and diabetic…"
monitor_inn: "Insulin lispro"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
---

# Insulin Lispro
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Insulin Lispro: From Type 2 Diabetes Mellitus to Autoimmune Oophoritis
{: .text-alpha }

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analogue originally used to treat type 1 and type 2 diabetes mellitus, including diabetic ketoacidosis.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (also type 1 diabetes mellitus and diabetic ketoacidosis) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 14 of 14) |
| Number of Registrations | 14 (valid: 14) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin lispro is a rapid-acting insulin analogue, its efficacy in diabetes mellitus is well established, and mechanistically it acts through insulin signaling.

For autoimmune oophoritis, the only link is speculative. Insulin signaling operates in ovarian granulosa cells, and autoimmune endocrine conditions can overlap with type 1 diabetes. This is not a therapeutic rationale for insulin lispro. The high TxGNN score is a model prediction and should not be read as evidence of benefit.

Other high-ranking predictions show the same pattern. Several (thiamine-responsive dysfunction syndrome, pancreatic agenesis) mainly reflect diabetes management, which is an extension of the existing indication. Several others (stiff person syndrome spectrum) reflect shared anti-GAD autoimmunity with type 1 diabetes. Two (drug-induced localized lipodystrophy, pressure-induced localized lipoatrophy) likely reflect injection-site adverse effects of insulin and are not therapeutic signals. Opsismodysplasia has a pathway-level link through INPPL1 (SHIP2), a negative regulator of insulin signaling, but no evidence that insulin alters the skeletal phenotype.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for autoimmune oophoritis.

For the rank 7 prediction, pancreatic agenesis, one general review is available. It is indirect evidence only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | Journal of the American Pharmaceutical Association | Overview of insulin therapy in type 2 diabetes and practical aspects of starting it; does not address pancreatic agenesis directly |

## India Market Information

The approved indication text is not recorded for these registrations. Five of the 14 valid registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 103754 | Humalog 100IU/ml Kwikpen (Eli Lilly and Company India) | Disposable pen of 3 ml solution for injection | Not specified |
| 103700 | Humalog 100IU/ml Solution for Injection (Eli Lilly and Company India) | Cartridge of 3 ml solution for injection | Not specified |
| 104016 | Humalog 200IU/ml Kwikpen (Eli Lilly and Company India) | Pre-filled pen of 3 ml solution for injection | Not specified |
| 73299 | Eglucent Rapid 100IU/ml Kwikpen (Lupin) | Pre-filled pen of 3 ml solution for injection | Not specified |
| 103706 | Humalog Mix 25 100IU/ml Cartridge (Eli Lilly and Company India) | Cartridge of 3 ml injection | Not specified |

All 14 registrations are single-ingredient products and currently valid. They are injectable only (cartridges and pens), in solution and premixed suspension forms.

## Safety Considerations

- **Drug Interactions**: The data compiled for this report list 352 known interactions. Most of those shown are moderate, with a few minor. Examples:
  - Moderate: metformin, alogliptin, albiglutide (additive glucose-lowering effects), epinephrine, salbutamol, formoterol, phenylephrine, pseudoephedrine, hydrocortisone, estradiol, ethinylestradiol, levonorgestrel, hydrochlorothiazide, acetazolamide, doxycycline, acebutolol, alpelisib, ethanol
  - Minor: topical hydrocortisone, topical alclometasone

Please refer to the package insert for warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for autoimmune oophoritis is supported only by a model score, with no clinical trials or literature, and the mechanistic link is speculative. Many of the other top predictions reflect existing diabetes care or injection-site adverse effects rather than new therapeutic opportunities.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Detailed mechanism of action data
- Preclinical or clinical evidence linking insulin lispro to autoimmune oophoritis
- Assessment of route compatibility and similarity to the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

