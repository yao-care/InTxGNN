---
layout: default
title: Insulin Glulisine
parent: Model Prediction Only (L5)
nav_order: 438
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Insulin Glulisine: predicted new indication Type 1 diabetes mellitus (evidence level L5). Approved use: Diabetes mellitus"
monitor_inn: "Insulin glulisine"
predicted_indications: ["thiamine-responsive dysfunction syndrome", "opsismodysplasia", "classic stiff person syndrome", "focal stiff limb syndrome", "autoimmune oophoritis", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
---

# Insulin Glulisine
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

# Insulin Glulisine: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin glulisine is a rapid-acting human insulin analogue, originally used to treat diabetes mellitus and diabetic ketoacidosis.
The TxGNN model predicts it may be effective for **type 1 diabetes mellitus**, which in practice already falls within its diabetes indication, so this is an on-label use rather than true repurposing. It is supported by **27 registered clinical trials** and **20 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus; diabetic ketoacidosis (from the knowledge graph; the Indian licence records contain no approved indication text) |
| Predicted New Indication | Type 1 diabetes mellitus |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 (assigned from published comparative trials; the Phase 3 trials listed below also support this level) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, insulin glulisine is a rapid-acting insulin analogue that binds the insulin receptor and lowers blood glucose. It has a faster onset and shorter duration of action than regular human insulin.

Type 1 diabetes is a form of diabetes mellitus, the drug's original indication, so the prediction is consistent with existing use. Insulin replacement is the cornerstone of type 1 diabetes therapy. The drug has been studied extensively in mealtime (prandial) use, basal-bolus regimens with insulin glargine, and pump (CSII) therapy.

Other top-ranked predictions (e.g., stiff person syndrome, autoimmune oophoritis, lipodystrophies) mostly reflect comorbidity or side-effect associations in the knowledge graph rather than therapeutic rationale, and are not pursued here.

---

## Clinical Trial Evidence

The compiled data include 27 trials. The 10 most relevant are listed below, prioritising completed Phase 3 trials and direct glulisine studies.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00115570](https://clinicaltrials.gov/study/NCT00115570) | Phase 3 | Completed | 572 | Glulisine vs lispro in children and adolescents with type 1 diabetes, 26 weeks |
| [NCT00467376](https://clinicaltrials.gov/study/NCT00467376) | Phase 3 | Completed | 485 | Glulisine vs lispro with glargine in type 1 or 2 diabetes; efficacy and hypoglycaemia frequency |
| [NCT00290979](https://clinicaltrials.gov/study/NCT00290979) | Phase 3 | Completed | 250 | Non-inferiority of glulisine vs lispro on HbA1c change in type 1 diabetes, 28 weeks |
| [NCT00397553](https://clinicaltrials.gov/study/NCT00397553) | Phase 3 | Completed | 104 | Local efficacy and safety data for glulisine with glargine in type 1 diabetes |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Phase 3 | Completed | 59 | Safety of glulisine vs aspart in insulin pumps (catheter occlusion, hypoglycaemia) |
| [NCT07070752](https://clinicaltrials.gov/study/NCT07070752) | Phase 3 | Completed | 224 | Immunogenicity non-inferiority of GP40321 vs Apidra SoloStar in type 1 diabetes |
| [NCT00607087](https://clinicaltrials.gov/study/NCT00607087) | Phase 4 | Completed | 289 | Glulisine vs aspart and lispro in pumps; unexplained hyperglycaemia and infusion set occlusion |
| [NCT00964574](https://clinicaltrials.gov/study/NCT00964574) | Phase 4 | Completed | 68 | Efficacy and safety of glulisine with glargine in type 1 diabetes |
| [NCT01204593](https://clinicaltrials.gov/study/NCT01204593) | Phase 4 | Completed | 206 | Glargine plus glulisine basal-bolus therapy in uncontrolled type 1 diabetes; HbA1c change at 24 weeks |
| [NCT01194245](https://clinicaltrials.gov/study/NCT01194245) | Phase 2 | Completed | 135 | Randomised double-blind crossover of insulin lispro-PH20 or aspart-PH20 vs lispro in type 1 diabetes (glulisine not tested) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT | Horm Metab Res | Multinational open-label RCT in adults with type 1 diabetes (672 treated); glulisine compared with lispro |
| [19614947](https://pubmed.ncbi.nlm.nih.gov/19614947/) | 2009 | Clinical trial | Diabetes Obes Metab | Glulisine vs lispro with glargine in Japanese patients with type 1 diabetes |
| [20150026](https://pubmed.ncbi.nlm.nih.gov/20150026/) | 2010 | Review/Meta-analysis | Endocr Pract | Rapid-acting analogues vs regular human insulin in basal-bolus type 1 diabetes: HbA1c, hypoglycaemia, dose |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Systematic review | Drugs Today | Insulin analogues, including glulisine, for children and adolescents with type 1 diabetes |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Review | Drugs | Glulisine has similar glucose effects to lispro and is effective against other short- and rapid-acting insulins |
| [16706558](https://pubmed.ncbi.nlm.nih.gov/16706558/) | 2006 | Review | Drugs | Faster onset and shorter duration than regular human insulin; similar HbA1c control in type 1 diabetes |
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | Comparative study | Acta Diabetol | Glulisine vs lispro and aspart in pump-treated type 1 diabetes: HbA1c, hypo- and hyperglycaemia, DKA rates |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Clinical study | Pediatr Int | Glulisine in CSII for 20 children for one year; post-meal glucose improved |
| [25865292](https://pubmed.ncbi.nlm.nih.gov/25865292/) | 2016 | Review | Diabetes Metab Res Rev | CSII in diabetes: populations, safety, efficacy and pharmacoeconomics |
| [18076215](https://pubmed.ncbi.nlm.nih.gov/18076215/) | 2008 | Pharmacology review | Clin Pharmacokinet | Pharmacokinetics and pharmacodynamics of glulisine: faster absorption and shorter action than regular insulin |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 666 | Apidra 100IU/ml Solution for Injection | Vial of 10 ml solution for injection | Not stated in the licence record |
| 197 | Apidra 100IU Cartridge | Cartridge of 3 ml solution for injection | Not stated in the licence record |
| 444 | Apidra Solostar 100IU/ml Injection | Pre-filled pen of 3 ml solution for injection | Not stated in the licence record |

All three licences are held by Sanofi India Ltd and are currently valid.

---

## Safety Considerations

- **Drug Interactions**: 353 known interactions were recorded. Examples include:
  - Moderate: metformin, pioglitazone, alogliptin, albiglutide, alpelisib, epinephrine, salbutamol, formoterol, phenylephrine, pseudoephedrine, acebutolol, hydrochlorothiazide, acetazolamide, doxycycline, estradiol, ethinylestradiol, hydrocortisone, ethanol
  - Minor: topical hydrocortisone, topical alclometasone
- **Class-related concerns**: Monitor for hypoglycaemia and for injection-site lipodystrophy.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Type 1 diabetes is an on-label use of insulin glulisine. Several completed Phase 3 trials and published randomised comparisons with lispro and aspart support its efficacy and safety. Guardrails are needed because the package insert safety data are missing and the interaction burden is high.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian licence holder (a blocking gap for safety screening)
- Detailed mechanism of action data
- Approved indication text for the three Indian licences
- A hypoglycaemia and injection-site monitoring plan, with interaction screening for concomitant drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

