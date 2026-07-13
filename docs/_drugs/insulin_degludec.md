---
layout: default
title: Insulin Degludec
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 6
---

# Insulin Degludec
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Insulin Degludec: From Globally Approved Basal Insulin to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin degludec (Tresiba®) is an ultra-long-acting basal insulin analogue, already approved by the FDA (2015) and EMA (2013) for type 1 and type 2 diabetes, yet currently without local market registration in India.
The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus** — which aligns precisely with its established global therapeutic role —
with **50 clinical trials** and **20 publications** providing exceptionally robust support for this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not locally registered; globally approved for type 1 and type 2 diabetes mellitus (FDA 2015, EMA 2013) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Insulin degludec is engineered to form soluble multi-hexamer chains upon subcutaneous injection. These multi-hexamers slowly dissociate at the injection site into dimers and monomers, which are then continuously absorbed into the bloodstream. This unique depot mechanism confers an ultra-flat, stable glucose-lowering profile with a duration of action exceeding 42 hours and virtually no pharmacodynamic peak. Day-to-day within-patient variability is approximately 20% (coefficient of variation), strikingly lower than NPH insulin at approximately 68% — a clinically decisive advantage for patients requiring predictable, round-the-clock basal insulin coverage.

In type 1 diabetes mellitus, autoimmune destruction of pancreatic β-cells eliminates endogenous insulin secretion entirely. Insulin degludec directly replaces this lost basal insulin by binding the insulin receptor and activating the IRS-1/PI3K/Akt signalling cascade. This promotes glucose uptake into skeletal muscle and adipose tissue, stimulates hepatic glycogen synthesis, and suppresses hepatic gluconeogenesis. The ultra-long, peakless action profile is particularly valuable in T1DM: any gap in basal coverage leads rapidly to hyperglycaemia and ketogenesis, and unpredictable peaks increase nocturnal hypoglycaemia risk — precisely the limitation that insulin degludec was designed to eliminate.

The TxGNN model's high-confidence prediction (99.44%) for T1DM reflects a knowledge-graph pathway grounded in well-established pharmacology rather than speculative repurposing. Multiple Phase 3 pivotal trials in the BEGIN programme, alongside more recent head-to-head comparator trials (ONWARDS 6, QWINT-5, EXPECT), have confirmed equivalent or superior HbA1c reduction with a clinically meaningful reduction in nocturnal hypoglycaemia compared to insulin glargine and insulin detemir. The local "not marketed" status most plausibly reflects an absence of a local regulatory filing rather than any deficiency in clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | Completed | 350 | BEGIN Young 1: IDeg vs insulin detemir in children and adolescents aged 1 to <18 years with T1DM on a basal-bolus regimen with insulin aspart; 26-week efficacy and safety comparison with 26-week extension, conducted across Africa, Asia, Europe and USA |
| [NCT00982228](https://clinicaltrials.gov/study/NCT00982228) | Phase 3 | Completed | 629 | BEGIN BB T1 LONG: 52-week multinational treat-to-target trial comparing IDeg + insulin aspart versus insulin glargine + insulin aspart in T1DM adults, with an extension period (BEGIN T1) |
| [NCT02670915](https://clinicaltrials.gov/study/NCT02670915) | Phase 3 | Completed | 834 | Faster-acting insulin aspart (Fiasp) vs NovoRapid, both in combination with IDeg as background basal insulin, in children and adolescents with T1DM; global multi-centre trial |
| [NCT02030600](https://clinicaltrials.gov/study/NCT02030600) | Phase 3 | Completed | 721 | SWITCH 2: Double-blind, two-period cross-over trial comparing IDeg vs insulin glargine with or without OADs in T2DM; largest sample size in this dataset, with high internal validity |
| [NCT02392117](https://clinicaltrials.gov/study/NCT02392117) | N/A | Completed | 1,262 | Large-scale prospective non-interventional observational study of Tresiba® safety and effectiveness in real-world T1DM and T2DM populations across Europe; supplements RCT external validity |
| [NCT04196231](https://clinicaltrials.gov/study/NCT04196231) | Phase 4 | Completed | 258 | BEYOND: Open-label 3-arm RCT evaluating the durability of IDeg/GLP-1RA and IDeg/SGLT-2i combination regimens versus basal-bolus therapy in poorly controlled T2DM; real-world usage context |
| [NCT03938740](https://clinicaltrials.gov/study/NCT03938740) | Phase 2 | Completed | 61 | Exploratory randomised open-label 2-arm trial comparing hepatic-directed vesicle–insulin lispro versus IDeg to determine optimum basal insulin dosing algorithms in T1DM |
| [NCT01773798](https://clinicaltrials.gov/study/NCT01773798) | Phase 1 | Completed | 33 | PK/PD properties of insulin degludec/insulin aspart 15 (IDegAsp) in T1DM subjects; supports dose-response characterisation and formulation understanding |
| [NCT01076634](https://clinicaltrials.gov/study/NCT01076634) | Phase 1 | Completed | 33 | Comparison of two IDeg formulations on pharmacodynamic properties in T1DM subjects; conducted in Europe |
| [NCT01704417](https://clinicaltrials.gov/study/NCT01704417) | Phase 1 | Completed | 40 | Head-to-head comparison of the effect of exercise on blood glucose between IDeg and insulin glargine in T1DM subjects; conducted in Europe |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT (Phase 3) | Lancet | QWINT-5: Once-weekly insulin efsitora alfa vs once-daily IDeg in T1DM adults; Phase 3 non-inferiority trial — IDeg served as the gold-standard active comparator, affirming its benchmark status in T1DM |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6: Once-weekly insulin icodec vs once-daily IDeg in T1DM adults; Phase 3a head-to-head efficacy and safety trial |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT (Phase 3) | Lancet Diabetes & Endocrinology | EXPECT trial: IDeg vs insulin detemir, both in combination with insulin aspart, in pregnant women with T1DM; multinational open-label non-inferiority trial |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematic review / Meta-analysis | Clinical Therapeutics | IDeg vs insulin glargine and insulin detemir in T1DM and T2DM: comparable HbA1c reduction with a consistent, clinically relevant reduction in hypoglycaemic episodes |
| [34643020](https://pubmed.ncbi.nlm.nih.gov/34643020/) | 2022 | RCT | Diabetes, Obesity & Metabolism | HypoDeg trial: Randomised controlled cross-over trial comparing IDeg vs insulin glargine U100 in T1DM patients prone to nocturnal severe hypoglycaemia |
| [36800034](https://pubmed.ncbi.nlm.nih.gov/36800034/) | 2023 | RCT | European Journal of Pediatrics | Three-arm RCT comparing IDeg vs insulin glargine vs NPH insulin in toddlers and preschoolers (ages 2–6 yr) with T1DM; glycaemic variability and time-in-range outcomes |
| [31055056](https://pubmed.ncbi.nlm.nih.gov/31055056/) | 2020 | Systematic review | Diabetes & Metabolism | Comprehensive synthesis of randomised and observational trials of IDeg in T1DM and T2DM; highlights better fasting glucose control and consistently lower nocturnal hypoglycaemia vs comparators |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes & Endocrinology | Management of T1DM in pregnancy: lifestyle, pharmacological treatment including IDeg, and novel technologies (CGM, insulin pumps) for achieving glycaemic targets |
| [23890782](https://pubmed.ncbi.nlm.nih.gov/23890782/) | 2014 | Review | Endocrinologia y Nutricion | Early clinical overview of IDeg's ultra-long-acting mechanism (multi-hexamer depot formation) and Phase 2/3 data in T1DM and T2DM |
| [25143741](https://pubmed.ncbi.nlm.nih.gov/25143741/) | 2014 | Review | Vascular Health and Risk Management | Insulin degludec/insulin aspart combination for T1DM and T2DM: pharmacological rationale and pivotal clinical trial evidence |

---

## India Market Information

Insulin degludec (Tresiba®) currently has **no registered authorizations** in the India market. No marketing approval records or license registrations were identified through the regulatory data query.

For reference, insulin degludec is approved under the following major regulatory jurisdictions:

| Jurisdiction | Approval Year | Approved Indication |
|-------------|--------------|---------------------|
| EMA (Europe) | 2013 | Type 1 and type 2 diabetes mellitus in adults |
| FDA (USA) | 2015 | Type 1 and type 2 diabetes mellitus in adults and paediatric patients (≥1 year) |
| Global (multiple markets) | 2013–present | Available as Tresiba® (100 U/mL and 200 U/mL) and Ryzodeg® (IDeg/IAsp combination) |

The absence of India registration reflects a regulatory filing gap rather than a safety or efficacy concern.

---

## Safety Considerations

**Drug Interactions (351 total interactions identified; key examples listed below):**

| Interacting Drug | Interaction Level | Clinical Note |
|-----------------|------------------|---------------|
| Epinephrine | Moderate | Catecholamines antagonise insulin's glucose-lowering effect; monitor blood glucose closely |
| Hydrocortisone | Moderate | Systemic corticosteroids elevate blood glucose and reduce insulin efficacy; dose adjustment may be required |
| Acebutolol | Moderate | Beta-blockers can mask hypoglycaemia symptoms (except sweating); use with caution |
| Hydrochlorothiazide | Moderate | Thiazide diuretics may impair glucose tolerance; insulin dose titration may be needed |
| Metformin | Moderate | Additive glucose-lowering effect; combined use is common and generally beneficial but requires monitoring |
| Pioglitazone | Moderate | Additive glucose-lowering; increased risk of fluid retention and heart failure; caution in at-risk patients |
| Alogliptin | Moderate | Additive glucose-lowering with DPP-4 inhibitor; heightened hypoglycaemia risk |
| Ethanol | Moderate | Alcohol inhibits hepatic gluconeogenesis and can substantially potentiate hypoglycaemia |
| Formoterol / Salbutamol | Moderate | Beta-2 agonists elevate blood glucose and may counteract insulin action |
| Estradiol / Levonorgestrel / Norethisterone | Moderate | Hormonal preparations may alter insulin requirements; regular blood glucose monitoring advised |

Please refer to the package insert for the full list of 351 interactions, complete warnings, contraindications, and special population guidance (pregnancy, renal/hepatic impairment, elderly).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Insulin degludec carries one of the strongest evidence bases of any basal insulin in modern diabetes therapeutics — with multiple completed Phase 3 multinational RCTs (BEGIN programme), post-marketing surveillance studies across tens of thousands of patients, and active benchmark-comparator status in Phase 3 trials of next-generation once-weekly basal insulins (ONWARDS 6, QWINT-5). The L1 evidence classification is unambiguous. The India "not marketed" status represents a regulatory filing gap that does not reflect any therapeutic uncertainty.

**To proceed, the following is needed:**
- Submit a local CDSCO marketing authorisation application, citing FDA and EMA approval dossiers as primary supporting documentation
- Obtain and thoroughly review the full prescribing information / SmPC to document India-specific safety labelling, warnings, and contraindications (currently a data gap flagged as blocking)
- Establish cold-chain logistics and storage infrastructure adequate for insulin products (2–8°C; do not freeze)
- Confirm paediatric dosing guidance and registration scope (T1DM in patients ≥1 year as per FDA label)
- Set up post-marketing pharmacovigilance and adverse event reporting mechanisms compliant with CDSCO requirements
- Develop healthcare provider education materials highlighting the clinical advantages of IDeg over currently available basal insulin options (lower nocturnal hypoglycaemia, flexible once-daily dosing window, lower day-to-day variability)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

