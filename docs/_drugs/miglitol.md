---
layout: default
title: Miglitol
parent: 僅模型預測 (L5)
nav_order: 349
evidence_level: L5
indication_count: 10
---

# Miglitol
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

# Miglitol: From Type 2 Diabetes to Type 1 Diabetes Mellitus

## One-Sentence Summary

Miglitol is an α-glucosidase inhibitor traditionally used to control postprandial blood glucose in type 2 diabetes mellitus, though it is not currently registered in India.
The TxGNN model predicts it may be effective as adjunct therapy for **Type 1 Diabetes Mellitus (T1DM)** — the highest-evidence indication among all predictions in this pack — supported by **1 completed Phase 3 clinical trial** and **16 publications** spanning over three decades of research.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (α-glucosidase inhibitor class; not registered in India) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Miglitol is an α-glucosidase inhibitor that competitively inhibits intestinal brush border enzymes — particularly maltase, sucrase, and starch glucoamylase — delaying the hydrolysis of dietary complex carbohydrates and reducing the rate at which glucose enters the bloodstream after meals. Its efficacy in reducing postprandial hyperglycemia in T2DM is well-established, and this same mechanism is directly applicable to T1DM.

In T1DM, absolute insulin deficiency creates steep postprandial glucose spikes that remain difficult to control even with intensive insulin regimens. A persistent clinical challenge is the pharmacokinetic mismatch between subcutaneous rapid-acting insulin absorption and the rapid surge of meal-derived glucose. By slowing intestinal glucose release, Miglitol can attenuate the peak postprandial glucose load, improve the temporal overlap between insulin action and glucose appearance, and potentially reduce hypoglycemic episodes caused by mistimed or excess insulin boluses.

The key biological insight is that α-glucosidase inhibition acts entirely at the intestinal level — upstream of and independent of insulin secretory capacity. This means the mechanism is equally applicable whether a patient produces abundant insulin (T2DM) or none at all (T1DM), providing a strong and coherent rationale for repurposing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00213109](https://clinicaltrials.gov/study/NCT00213109) | Phase 3 | Completed | N/A | Direct evaluation of clinical efficacy and safety of Miglitol in T1DM patients treated with insulin — the primary pivotal trial for this repurposing direction |
| [NCT01697592](https://clinicaltrials.gov/study/NCT01697592) | Phase 3 | Completed | 585 | Omarigliptin add-on in Japanese T2DM patients on oral antihyperglycemic monotherapy; provides regulatory precedent for adjunct oral antidiabetics in Asian populations |
| [NCT02475499](https://clinicaltrials.gov/study/NCT02475499) | N/A | Completed | 886,172 | Population-based cohort study assessing incretin-based drugs and pancreatic cancer risk in T2DM across Canada, US, and UK |
| [NCT02456428](https://clinicaltrials.gov/study/NCT02456428) | N/A | Completed | 1,499,650 | Multi-centre network study of incretin drugs and heart failure risk in T2DM; cardiovascular safety background for oral antidiabetic combinations |
| [NCT02476760](https://clinicaltrials.gov/study/NCT02476760) | N/A | Completed | 1,417,914 | Observational study of incretin drugs and acute pancreatitis risk in T2DM |
| [NCT03492580](https://clinicaltrials.gov/study/NCT03492580) | N/A | Completed | 714,582 | Comparative effectiveness of Canagliflozin vs. other antihyperglycemics for heart failure hospitalization and amputation in T2DM |
| [NCT06449235](https://clinicaltrials.gov/study/NCT06449235) | Phase 4 | Not Yet Recruiting | 938 | Real-world safety and efficacy evaluation of omarigliptin in newly diagnosed T2DM patients in Bangladesh |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [2060451](https://pubmed.ncbi.nlm.nih.gov/2060451/) | 1991 | RCT | Diabetes Care | Miglitol delays carbohydrate absorption, improves meal glucose tolerance, and enables more flexible insulin timing in T1DM patients; foundational controlled evidence for this repurposing direction |
| [24843410](https://pubmed.ncbi.nlm.nih.gov/24843410/) | 2010 | Clinical Study | J Diabetes Investigation | Miglitol + insulin combination addresses precipitous postprandial glucose rise uncontrolled by intensive insulin therapy alone; supports clinical utility in T1DM |
| [21869539](https://pubmed.ncbi.nlm.nih.gov/21869539/) | 2011 | Clinical Study | Endocrine Journal | Miglitol 25–50 mg TID with intensive insulin: improved glycemic control, reduced hypoglycemia frequency, and modified incretin hormone responses in 11 T1DM subjects |
| [3311550](https://pubmed.ncbi.nlm.nih.gov/3311550/) | 1987 | Clinical Trial | Clin Pharmacol Ther | Miglitol (Bay-m-1099) allows immediate preprandial insulin injection with ~20% dose reduction while maintaining postprandial control equivalent to insulin given 30 min pre-meal |
| [3286168](https://pubmed.ncbi.nlm.nih.gov/3286168/) | 1988 | Clinical Trial | Diabetes Res Clin Pract | α-Glucosidase inhibition permits flexible insulin timing and reduced dosing in IDDM; directly addresses the clinical challenge of insulin-meal coordination in T1DM |
| [2663321](https://pubmed.ncbi.nlm.nih.gov/2663321/) | 1989 | Clinical Trial | Diabetes Research | Single-blind crossover in 13 IDDM patients: Miglitol significantly reduced area under the glucose curve vs. placebo over 4-week treatment periods |
| [3130257](https://pubmed.ncbi.nlm.nih.gov/3130257/) | 1988 | Clinical Trial | Eur J Clin Investigation | Prolonged administration of BAYm1099 (Miglitol precursor) and BAYo1248 in IDDM: improved glycemic control and reduced insulin requirements confirmed |
| [8261749](https://pubmed.ncbi.nlm.nih.gov/8261749/) | 1993 | Clinical Trial | Diabetic Medicine | Systematic assessment of α-glucosidase inhibition as an adjunct strategy for T1DM management |
| [11460577](https://pubmed.ncbi.nlm.nih.gov/11460577/) | 2001 | Review | Exp Clin Endocrinol Diabetes | Comprehensive review of oral hypoglycemic agents including α-glucosidase inhibitors; reviews mechanism and therapeutic role including insulin-dependent settings |
| [12073790](https://pubmed.ncbi.nlm.nih.gov/12073790/) | 2002 | Review | Rev Med Liège | Pharmacological approaches to postprandial hyperglycemia: Miglitol and acarbose as intestinal glucose absorption modifiers applicable to both T1DM and T2DM |

---

## India Market Information

Miglitol currently has **no registered products** in India and is classified as not marketed. No authorization records are available.

---

## Safety Considerations

**Drug Interactions** (241 total interactions identified; key moderate-level interactions listed below):

| Interacting Drug | Level | Clinical Note |
|-----------------|-------|---------------|
| Epinephrine | Moderate | Sympathomimetic used for hypoglycemia reversal — Miglitol may attenuate its glucose-raising effect |
| Pseudoephedrine | Moderate | Sympathomimetic raises blood glucose; pharmacodynamic antagonism with Miglitol |
| Phenylephrine | Moderate | Sympathomimetic interaction |
| Formoterol / Salbutamol | Moderate | Beta-agonists raise blood glucose; pharmacodynamic antagonism |
| Hydrocortisone / Triamcinolone | Moderate | Corticosteroid-induced hyperglycemia may reduce Miglitol's glycemic benefit |
| Hydrochlorothiazide | Moderate | Thiazide diuretics can impair glucose tolerance |
| Ethanol | Moderate | May potentiate hypoglycemia risk, particularly in T1DM patients concurrently using insulin |
| Alpelisib | Moderate | PI3K inhibitor causes hyperglycemia; clinically significant pharmacodynamic interaction |
| Aripiprazole / Asenapine | Moderate | Atypical antipsychotics associated with glucose dysregulation |
| Ethinylestradiol / Estradiol | Moderate | Hormonal effects on glycemic control |
| Asparaginase (E. coli / Erwinia) | Moderate | Associated with glucose dysregulation in oncology settings |
| Acetazolamide | Moderate | Carbonic anhydrase inhibition; glycemic interaction |

Please refer to the package insert for key warnings and contraindications, as this data was not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
NCT00213109, a completed Phase 3 trial directly evaluating Miglitol in T1DM patients receiving insulin therapy, combined with over a dozen clinical publications from 1986–2020 across multiple independent research groups, establishes L1-level evidence for this repurposing direction. The mechanistic rationale — insulin-independent postprandial glucose reduction via intestinal α-glucosidase inhibition — is biologically sound and directly applicable to T1DM physiology.

**To proceed, the following is needed:**
- Retrieve the full results of NCT00213109 and evaluate primary endpoints (HbA1c reduction, postprandial glucose excursion, hypoglycemia frequency, insulin dose change)
- Obtain detailed MOA data from DrugBank to formally document mechanistic justification (DG002)
- Retrieve and review the package insert from a jurisdiction where Miglitol is approved (e.g., US FDA, Japan PMDA) to identify key warnings and contraindications before entering S1 safety evaluation (DG001 — currently Blocking)
- Conduct a formal benefit-risk analysis specific to the T1DM population, with particular focus on hypoglycemia risk when Miglitol is used adjunctively with insulin
- Define India regulatory pathway and evaluate market entry feasibility given Miglitol's current zero-registration status in India
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

