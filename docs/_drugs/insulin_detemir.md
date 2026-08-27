---
layout: default
title: Insulin Detemir
parent: 僅模型預測 (L5)
nav_order: 335
evidence_level: L5
indication_count: 10
---

# Insulin Detemir
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

# Insulin Detemir: From Basal Insulin Therapy to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin detemir (Levemir®) is a long-acting basal insulin analogue developed to provide physiological insulin replacement in patients with diabetes mellitus.
The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus** — a reflection of its globally established primary indication rather than a novel repurposing discovery —
with **50 clinical trials** and **19 publications** currently supporting this direction, achieving an **L1 evidence level**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No India regulatory data available (not marketed in India) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacological knowledge, insulin detemir is a long-acting basal insulin analogue with a unique dual-action protraction mechanism: (1) strong self-association into dihexamers at the subcutaneous injection site slows local absorption; and (2) reversible binding to serum albumin via its 14-carbon fatty acid (myristic acid) side chain further delays systemic distribution. The result is a flat, predictable pharmacodynamic profile lasting approximately 24 hours — which is the pharmacokinetic property that distinguishes it from NPH insulin and makes it clinically suitable for once- or twice-daily basal dosing.

Type 1 Diabetes Mellitus arises from autoimmune destruction of pancreatic beta cells, causing absolute insulin deficiency. Patients require lifelong exogenous insulin replacement. Basal insulin analogues like insulin detemir provide the steady-state background insulin coverage needed to suppress hepatic glucose production and regulate fasting and between-meal glucose concentrations. The biological link between insulin detemir and T1DM is therefore mechanistically direct and therapeutically self-evident — rather than an inferred cross-indication.

It is important to note that this TxGNN prediction does **not** represent a novel repurposing opportunity. Insulin detemir is approved for T1DM by major regulatory agencies globally (FDA, EMA, and numerous others), and the high prediction score (99.77%) confirms that the knowledge graph correctly identified the established drug–disease pair. For India, this case should be framed as a **market entry assessment** — the drug is not currently registered with CDSCO, representing a regulatory gap rather than a scientific one.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01709929](https://clinicaltrials.gov/study/NCT01709929) | Phase 3 | Completed | 2,287 | Multicentre open-label safety study evaluating insulin detemir for insulin-dependent T1DM and T2DM across North American sites |
| [NCT01831765](https://clinicaltrials.gov/study/NCT01831765) | Phase 3 | Completed | 1,290 | 52-week efficacy and safety comparison of FIAsp (faster-acting insulin aspart) vs insulin aspart, both combined with insulin detemir as basal insulin, in adults with T1DM |
| [NCT03220425](https://clinicaltrials.gov/study/NCT03220425) | Phase 3 | Completed | 752 | Six-month open-label parallel-group comparison of insulin detemir vs NPH insulin in T1DM on a basal-bolus regimen; primary outcomes were HbA1c and hypoglycaemia rates |
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Phase 3 | Completed | 598 | Multinational, multicentre parallel RCT of insulin detemir + insulin aspart vs NPH + soluble insulin in T1DM on a basal-bolus regimen |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | Completed | 470 | Multinational RCT comparing insulin detemir vs NPH insulin (both with insulin aspart bolus) in pregnant women with T1DM; safety and glycaemic control outcomes |
| [NCT00095082](https://clinicaltrials.gov/study/NCT00095082) | Phase 3 | Completed | 447 | European/US trial comparing insulin detemir vs insulin glargine (both combined with insulin aspart) in T1DM basal-bolus therapy; non-inferiority design |
| [NCT00487240](https://clinicaltrials.gov/study/NCT00487240) | Phase 3 | Completed | 387 | Treat-to-target comparison of insulin lispro protamine suspension vs insulin detemir as basal insulin combined with mealtime therapy in T1DM |
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | Completed | 350 | BEGIN Young 1: 26-week multinational efficacy and safety comparison of insulin degludec vs insulin detemir in children and adolescents (ages 1–18) with T1DM on basal-bolus regimen, with 26-week extension |
| [NCT00447382](https://clinicaltrials.gov/study/NCT00447382) | Phase 3 | Completed | 330 | 12-month double-blind multinational RCT comparing insulin detemir produced by two manufacturing processes (NN729 vs NN304) in T1DM; confirmed bioequivalence and long-term safety |
| [NCT01461616](https://clinicaltrials.gov/study/NCT01461616) | Phase 3 | Completed | 19 | Open-label triple crossover trial comparing equal doses of NPH insulin, insulin detemir, and insulin glargine on IGFBP-1 production and IGF-I levels in T1DM; mechanistic Phase 3 data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | The Lancet Diabetes & Endocrinology | EXPECT trial: insulin degludec was non-inferior to insulin detemir (both with insulin aspart) in pregnant women with T1DM; comparable glycaemic control and neonatal outcomes |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematic Review & Meta-analysis | Clinical Therapeutics | Head-to-head comparison of insulin degludec vs glargine and detemir in T1DM/T2DM; degludec showed significantly lower nocturnal hypoglycaemia risk vs detemir |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematic Review + Network Meta-analysis | Value in Health | Comprehensive network meta-analysis of basal insulin regimens in adults with T1DM; characterised relative efficacy and safety of detemir vs glargine, degludec, and NPH |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Systematic Review & Meta-analysis | Pol Arch Med Wewn | Insulin detemir vs NPH in T1DM: detemir associated with reduced nocturnal hypoglycaemia, lower intrapatient glucose variability, and modest weight benefit |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Clinical Practice Guideline | The Lancet Diabetes & Endocrinology | Updated management guidelines for T1DM in pregnancy; endorses insulin detemir as the reference basal insulin and covers emerging diabetes technologies |
| [23110609](https://pubmed.ncbi.nlm.nih.gov/23110609/) | 2012 | Review | Drugs | Comprehensive updated review of insulin detemir pharmacology, pharmacokinetics, and clinical trial evidence in T1DM and T2DM; favourable tolerability and weight profile highlighted |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vascular Health and Risk Management | Insulin detemir update for T1DM and T2DM: reduced intrapatient pharmacodynamic variability and lower hypoglycaemia rates vs NPH insulin; suitable for patient self-titration |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vascular Health and Risk Management | Mechanism review of insulin detemir: albumin-binding and self-association explain prolonged action; clinical evidence of reduced nocturnal hypoglycaemia and weight neutrality in T1DM |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | First comprehensive drug review of insulin detemir; characterised fatty acid side-chain mechanism, 24-hour action profile, and initial Phase 3 efficacy data in T1DM and T2DM |
| [18454569](https://pubmed.ncbi.nlm.nih.gov/18454569/) | 2008 | Review | Paediatric Drugs | Insulin analogue preparations in children and adolescents with T1DM; insulin detemir pharmacology and clinical outcomes compared with NPH and glargine in the paediatric population |

---

## India Market Information

Insulin detemir is currently not registered with the CDSCO and has no approved product licences in India. No authorisation numbers, brand names, or approved indications are available through the India regulatory database.

---

## Safety Considerations

**Drug Interactions:** Insulin detemir has **353 known drug interactions** documented in DDInter. Representative interactions include:

- **Moderate interactions:** Metformin, Pioglitazone, Alogliptin, Albiglutide, Hydrochlorothiazide, Hydrocortisone (systemic), Estradiol, Ethinylestradiol, Epinephrine, Pseudoephedrine, Phenylephrine, Salbutamol, Formoterol, Acebutolol, Acetazolamide, Doxycycline, Ethanol, Alpelisib
- **Minor interactions:** Hydrocortisone (topical), Alclometasone (topical)

Please refer to the package insert for complete warnings and contraindications, as these data were not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Insulin detemir has robust L1 evidence supporting its use in Type 1 Diabetes Mellitus, with multiple completed multinational Phase 3 RCTs and systematic reviews establishing its efficacy and safety. However, this TxGNN prediction reflects an established primary indication globally, not a novel repurposing discovery — the key action item is CDSCO registration for India market entry, not further scientific validation.

**To proceed, the following is needed:**

- Prepare and submit a CDSCO new drug registration dossier, leveraging existing FDA/EMA approvals and clinical data package
- Obtain and review the full prescribing information (package insert) to complete the safety assessment — key warnings and contraindications were not extractable in the current Evidence Pack (Data Gap)
- Retrieve mechanism of action (MOA) details from DrugBank API to complete the pharmacological profile
- Confirm cold-chain storage requirements and local supply chain readiness for insulin distribution in India
- Assess pricing strategy given established generic and biosimilar competition in the Indian insulin market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

