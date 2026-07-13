---
layout: default
title: Insulin Glulisine
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
---

# Insulin Glulisine
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

# Insulin Glulisine: From Diabetes Management to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin glulisine (Apidra®) is a rapid-acting human insulin analogue with established approval by the US FDA and EMA for glycemic control in patients with diabetes mellitus, though it is not currently registered in India.
The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus (T1DM)** — a finding aligned with its internationally approved core indication — supported by **50+ clinical trials** and **19 publications**, including multiple completed Phase 3 RCTs across adult and pediatric populations.
This report frames the prediction as a market-entry evaluation, given the complete absence of local CDSCO registration despite a robust global evidence base.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Glycemic control in diabetes mellitus (FDA/EMA approved globally; no India registration) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Insulin glulisine \[3(B)-Lys, 29(B)-Glu human insulin\] is a rapid-acting insulin analogue engineered to overcome the pharmacokinetic limitations of regular human insulin. By substituting asparagine with lysine at position B3 and lysine with glutamate at position B29, the molecule cannot form zinc-coordinated hexamers in subcutaneous tissue, enabling faster dissociation into monomers and absorption into the bloodstream. It binds the insulin receptor (INSR), activating the PI3K/Akt/mTOR signaling cascade to promote GLUT4 translocation to cell membranes, accelerate peripheral glucose uptake, stimulate glycogen synthesis, and suppress hepatic gluconeogenesis. The result is an onset of action within 10–15 minutes, peak effect at approximately 1 hour, and a duration of roughly 4 hours — closely mimicking physiological first-phase insulin secretion.

Type 1 diabetes mellitus is caused by autoimmune destruction of pancreatic β-cells (mediated primarily by autoreactive CD8+ T cells targeting antigens such as GAD65 and IA-2), leading to absolute and irreversible insulin deficiency. Without exogenous insulin replacement, patients cannot regulate blood glucose and are at immediate risk of diabetic ketoacidosis. The mechanistic link between insulin glulisine and T1DM is therefore direct and essential: the drug directly replaces the endogenous prandial insulin signal that β-cells can no longer provide. Its rapid onset is particularly well suited to prandial (mealtime) coverage in basal-bolus regimens and to continuous subcutaneous insulin infusion (CSII) pumps, where catheter compatibility and absence of zinc-induced precipitation are important practical advantages.

Globally, insulin glulisine received US FDA approval in 2004 and EMA approval under the brand Apidra® (Sanofi) for glycemic control in adults and pediatric patients ≥4 years with T1DM and T2DM. The TxGNN model's top-ranked prediction (score 99.55%) correctly identifies T1DM as the primary therapeutic target. This is not a speculative drug repurposing — rather, it represents an opportunity to bring an evidence-rich, globally established therapy into the Indian market, where it is currently unregistered.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT02688933](https://clinicaltrials.gov/study/NCT02688933) | Phase 4 | Completed | 638 | 16-week randomized active-controlled trial in adult T1DM comparing morning Toujeo (glargine U300) vs Lantus, both combined with glulisine as prandial insulin; Toujeo showed better CGM glucose control and fewer nocturnal hypoglycemic events |
| [NCT04974528](https://clinicaltrials.gov/study/NCT04974528) | Phase 3 | Completed | 319 | INHALE-1: 26-week pediatric trial comparing inhaled Afrezza vs rapid-acting insulin analogues including glulisine in combination with basal insulin in T1DM/T2DM children; provided comparative safety and efficacy data for glulisine in pediatric populations across a 52-week study window |
| [NCT00290979](https://clinicaltrials.gov/study/NCT00290979) | Phase 3 | Completed | 250 | 28-week randomized non-inferiority trial in T1DM adults comparing insulin glulisine to insulin lispro; demonstrated comparable HbA1c reduction and equivalent safety profile |
| [NCT00546702](https://clinicaltrials.gov/study/NCT00546702) | Phase 3 | Completed | 142 | 26-week open-label multicenter study evaluating glulisine efficacy (HbA1c change from baseline) and safety in T1DM patients using glargine as basal insulin |
| [NCT00271284](https://clinicaltrials.gov/study/NCT00271284) | Phase 3 | Completed | 88 | Crossover multicenter RCT comparing fasting glucose variability with glargine+glulisine vs detemir+glulisine in T1DM; demonstrated non-inferiority of both combinations |
| [NCT01202474](https://clinicaltrials.gov/study/NCT01202474) | Phase 4 | Completed | 100 | Multicenter Phase 4 study evaluating Apidra (glulisine) + Lantus in T1DM children and adolescents (ages 6–17 years) in Russia over 12 months; primary endpoint: HbA1c <8% (ages 6–12) and <7.5% (ages 13–17) |
| [NCT04124302](https://clinicaltrials.gov/study/NCT04124302) | Phase 4 | Completed | 76 | RCT in T1DM children comparing two insulin dose calculation methods for mixed meals using glulisine-based regimen; evaluated impact on postprandial glycemia |
| [NCT01848990](https://clinicaltrials.gov/study/NCT01848990) | Phase 4 | Completed | 456 | CONSISTENT 1: 6-month study evaluating hyaluronidase preadministration in T1DM patients on CSII (predominantly with glulisine); compared HbA1c improvement, local tolerability, and hypoglycemia rates vs standard CSII |
| [NCT01678235](https://clinicaltrials.gov/study/NCT01678235) | Phase 4 | Completed | 64 | Double-blind crossover RCT in T1DM children comparing postprandial glycemic control of glulisine vs insulin aspart after high-glycaemic index meals via insulin pump (CSII) |
| [NCT00964574](https://clinicaltrials.gov/study/NCT00964574) | Phase 4 | Completed | 68 | Open-label multicenter Phase 4 study evaluating efficacy, safety, insulin doses, and patient satisfaction with glulisine in T1DM patients on a glargine-based regimen over 12 months |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | Prospective Comparative Study | Acta Diabetologica | Real-world comparison of T1DM patients using glulisine vs lispro vs aspart via CSII; described HbA1c effectiveness, fasting glucose, and rates of hyperglycemia, hypoglycemia, and DKA |
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT (Pivotal) | Hormone and Metabolic Research | Multinational multicenter parallel-group RCT (n=683 T1DM adults) comparing glulisine to insulin lispro; demonstrated comparable HbA1c reduction and equivalent safety profile at 26 weeks |
| [21291333](https://pubmed.ncbi.nlm.nih.gov/21291333/) | 2011 | RCT | Diabetes Technology & Therapeutics | 26-week trial in pediatric T1DM patients comparing glulisine to lispro as part of a basal-bolus regimen; found comparable efficacy and safety across children and adolescents |
| [21457066](https://pubmed.ncbi.nlm.nih.gov/21457066/) | 2011 | RCT | Diabetes Technology & Therapeutics | Randomized crossover multicenter study in T1DM via CSII comparing glulisine vs aspart vs lispro; glulisine showed a trend toward fewer catheter occlusions than aspart |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Systematic Review | Drugs of Today | Systematic review of insulin analogues for T1DM in children and adolescents; evaluated glulisine among three approved rapid-acting analogues (lispro, aspart, glulisine) for pharmacokinetics, efficacy, and safety |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Pediatric Clinical Study | Pediatrics International | Evaluated glulisine efficacy and safety via CSII in 20 Japanese T1DM children over 1 year; postprandial glucose levels after breakfast and dinner significantly improved (P<0.05) |
| [16123473](https://pubmed.ncbi.nlm.nih.gov/16123473/) | 2005 | Pediatric PK/PD Study | Diabetes Care | PK/PD study in T1DM children and adolescents comparing glulisine vs regular human insulin (RHI) given immediately premeal; glulisine showed faster absorption, lower postprandial excursions, and improved safety |
| [19614947](https://pubmed.ncbi.nlm.nih.gov/19614947/) | 2009 | RCT | Diabetes, Obesity & Metabolism | Japanese T1DM randomized trial comparing glulisine to lispro with glargine as basal insulin; demonstrated non-inferior efficacy and similar safety in the Japanese population |
| [29159123](https://pubmed.ncbi.nlm.nih.gov/29159123/) | 2016 | Clinical PK/PD Study | Journal of Clinical & Translational Endocrinology | Compared PK/PD of glargine+glulisine basal-bolus vs twice-daily premixed insulin in T1DM during three standardized meals over 24 hours; basal-bolus showed superior physiologic glucose response |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Review | Drugs | Comprehensive review of insulin glulisine in diabetes management; summarized clinical evidence for comparable glycaemic control vs other rapid-acting analogues, PK/PD advantages, and safety data across T1DM and T2DM |

---

## India Market Information

Insulin glulisine (Apidra®) currently holds **no CDSCO registrations in India**. There are no approved products, licensed manufacturers, or authorized brands on the domestic market.

For reference, the drug holds the following major international authorizations:

| Regulatory Body | Approval Year | Brand Name | Approved Indication |
|---|---|---|---|
| US FDA | 2004 | Apidra® (Sanofi) | Glycemic control in adults and children ≥4 years with T1DM and T2DM |
| EMA | 2004 | Apidra® (Sanofi) | Glycemic control in adults and children ≥6 years with T1DM and T2DM |

A new drug application to CDSCO under the New Drugs and Clinical Trials Rules, 2019 would be required before any market entry in India.

---

## Safety Considerations

**Drug Interactions (353 interactions identified; key moderate-level interactions listed):**

| Interacting Drug | Level | Clinical Concern |
|---|---|---|
| Epinephrine | Moderate | Sympathomimetics counter insulin's glucose-lowering effect; concurrent use may cause hyperglycemia |
| Phenylephrine | Moderate | Similar to epinephrine; blood glucose monitoring required |
| Acebutolol | Moderate | Beta-blockers may mask tachycardia as a warning sign of hypoglycemia |
| Hydrochlorothiazide | Moderate | Thiazide diuretics impair insulin secretion and peripheral glucose utilization |
| Hydrocortisone | Moderate | Corticosteroids cause insulin resistance; insulin dose may need to be increased |
| Metformin | Moderate | Additive blood glucose-lowering effect; monitor for hypoglycemia, especially with dose titration |
| Pioglitazone | Moderate | Additive glucose-lowering; increased risk of hypoglycemia and fluid retention |
| Alogliptin | Moderate | Additive glucose-lowering; hypoglycemia risk when combined with insulin |
| Ethanol | Moderate | Alcohol inhibits hepatic gluconeogenesis, potentiating insulin-induced hypoglycemia |
| Formoterol / Salbutamol | Moderate | Beta-2 agonists antagonize insulin action; monitor blood glucose during bronchodilator use |

As local prescribing information (CDSCO-approved package insert) is not available, please refer to the Apidra® international prescribing information (FDA label or EMA SmPC) for full warnings and contraindications, including hypoglycemia precautions, insulin allergy, and special population dosing (renal/hepatic impairment, elderly, pediatric).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Insulin glulisine is a globally established rapid-acting insulin analogue with decades of Phase 3/4 RCT evidence firmly supporting its use in T1DM across adult and pediatric populations; the TxGNN model's top prediction correctly identifies its primary therapeutic niche. The sole barrier to use in India is the absence of CDSCO registration — not a lack of clinical evidence or mechanistic rationale.

**To proceed, the following is needed:**

- File a New Drug Application (NDA) with CDSCO under the New Drugs and Clinical Trials Rules, 2019, leveraging the existing FDA/EMA approvals as primary evidence dossier
- Compile the India-specific prescribing information (package insert) with local warnings, contraindications, and dosing guidance in alignment with CDSCO requirements
- Retrieve full MOA and pharmacology data from the DrugBank API (DB01309) and published literature to complete the regulatory dossier and drug monograph
- Assess cold-chain logistics and storage infrastructure requirements for subcutaneous insulin products across Indian distribution networks
- Evaluate competitive landscape and pricing strategy against existing rapid-acting insulin analogues registered in India (insulin lispro, insulin aspart)
- Confirm with CDSCO whether any local bridging study is required for already-globally-approved insulin analogues under the accelerated approval pathway for globally approved drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

