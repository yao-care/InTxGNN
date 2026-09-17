---
layout: default
title: Voglibose
parent: Moderate Evidence (L3-L4)
nav_order: 887
evidence_level: L3
indication_count: 10
---

# Voglibose
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

Using domain judgment as a drug-repurposing expert to select the report's focal indication: `predicted_indications[0]` (hypotrichosis simplex of the scalp) is explicitly flagged in its own rationale as "純為 TxGNN 高分預測，無任何生物學支持" (no biological plausibility, zero evidence) — reporting it as the headline finding would be misleading. **Type 1 Diabetes Mellitus** (rank 2, duplicated at rank 6 as "IDDM 1") is the only candidate with real mechanistic rationale, trial evidence, and literature (L3), so it is used as the report subject below.

---

# Voglibose: From Type 2 Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

> Voglibose is an α-glucosidase inhibitor internationally used to control postprandial hyperglycemia in Type 2 Diabetes Mellitus.
> The TxGNN model predicts it may be useful as an **adjunct to insulin therapy in Type 1 Diabetes Mellitus** (flattening post-meal glucose spikes and reducing nocturnal hypoglycemia),
> with **15 clinical trials** (mostly indirect, in T2DM populations) and **5 publications** — including one small cohort study directly in insulin-dependent (Type 1) diabetic patients — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in local regulatory data (drug not marketed in India); internationally an α-glucosidase inhibitor indicated for glycemic control in Type 2 Diabetes Mellitus |
| Predicted New Indication | Type 1 Diabetes Mellitus (insulin-adjunct use) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (marked as a High-severity data gap). Based on the trial and literature evidence collected, voglibose is known to act as an **α-glucosidase inhibitor**, delaying intestinal carbohydrate absorption and blunting postprandial blood glucose rises. This mechanism has been extensively validated in Type 2 Diabetes Mellitus, including head-to-head Phase 3/4 trials against acarbose, vildagliptin, sitagliptin, and dapagliflozin.

The predicted new indication, Type 1 Diabetes Mellitus, shares an obvious pathophysiological link: both conditions involve poor glycemic control requiring exogenous insulin at some stage of disease. In T1DM patients on intensive insulin therapy, the main clinical challenge shifts from insulin *deficiency* to managing glucose *variability* — sharp postprandial peaks followed by nocturnal hypoglycemia. Because voglibose slows carbohydrate absorption without directly increasing insulin secretion, it is mechanistically well suited to smoothing this glycemic curve rather than replacing insulin.

Notably, the knowledge graph independently surfaced this same biological signal twice — once under "type 1 diabetes mellitus" and once under its older clinical synonym "IDDM 1" — both scoring similarly (~99.4–99.8%) and both supported by the same literature, which reinforces the internal consistency of the prediction rather than being a random high score.

---

## Clinical Trial Evidence

**Note:** all trials below were conducted in **Type 2 Diabetes Mellitus** populations (grade C relevance) or T1DM-adjacent monitoring studies; none is a dedicated T1DM interventional trial. They are listed because voglibose's pharmacodynamic profile (established here) underpins the T1DM adjunct rationale.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00970528](https://clinicaltrials.gov/study/NCT00970528) | Phase 4 | Completed | 124 | Voglibose vs acarbose in patients inadequately controlled on **insulin glargine** ± metformin (T2DM) |
| [NCT02049814](https://clinicaltrials.gov/study/NCT02049814) | Phase 4 | Completed | 494 | Non-inferiority: voglibose vs acarbose + metformin, HbA1c endpoint (T2DM) |
| [NCT00368134](https://clinicaltrials.gov/study/NCT00368134) | Phase 3 | Completed | 370 | Vildagliptin vs voglibose, 12-week efficacy/safety/tolerability comparison (T2DM) |
| [NCT01993927](https://clinicaltrials.gov/study/NCT01993927) | N/A | Completed | 742 | Long-term postmarketing surveillance of voglibose tablets/OD tablets in impaired glucose tolerance |
| [NCT01309698](https://clinicaltrials.gov/study/NCT01309698) | Phase 4 | Completed | 24 | PK/PD of vildagliptin + voglibose co-administration in Japanese T2DM patients |
| [NCT02287402](https://clinicaltrials.gov/study/NCT02287402) | Phase 4 | Completed | 197 | AO-128 (voglibose) 0.6 mg/day postmarketing study in impaired glucose tolerance |
| [NCT00837577](https://clinicaltrials.gov/study/NCT00837577) | Phase 3 | Completed | 133 | Sitagliptin add-on to **voglibose monotherapy** in T2DM with inadequate control |
| [NCT01055652](https://clinicaltrials.gov/study/NCT01055652) | Phase 1 | Completed | 28 | Drug–drug interaction: voglibose 0.2mg TID effect on dapagliflozin PK (T2DM) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10778865](https://pubmed.ncbi.nlm.nih.gov/10778865/) | 2000 | Cohort | Metabolism: Clinical and Experimental | **Directly relevant**: pre-evening-meal voglibose reduced nocturnal hypoglycemia in 10 insulin-dependent (Type 1) diabetic patients on intensive insulin therapy |
| [12387032](https://pubmed.ncbi.nlm.nih.gov/12387032/) | 2002 | Review | Nihon Rinsho (Japanese J Clinical Medicine) | Review of combination therapy with insulin and α-glucosidase inhibitors |
| [39723258](https://pubmed.ncbi.nlm.nih.gov/39723258/) | 2024 | Review | Frontiers in Pharmacology | General review of anti-diabetic therapy effects (T1DM & T2DM) on dental implant outcomes; background context only |
| [9778959](https://pubmed.ncbi.nlm.nih.gov/9778959/) | 1998 | Case Report | Nihon Ronen Igakkai Zasshi | Slowly progressive IDDM (LADA-type T1DM) case with comorbid autoimmune disease |
| [18502532](https://pubmed.ncbi.nlm.nih.gov/18502532/) | 2008 | Case Report | Diabetes Research and Clinical Practice | Insulin edema case in a T2DM patient; tangential relevance |

---

## India Market Information

Voglibose is **not currently marketed in India** — the regulatory data pack contains **0 registered licenses/products**. No dosage forms or approved indication text are available locally.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are all currently unavailable in this evidence pack — this is flagged as a **Blocking** data gap that must be resolved before any safety evaluation can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale is plausible and reinforced by a consistent knowledge-graph signal (T1DM and its synonym IDDM both scored highly), but direct clinical evidence is limited to one small, 25-year-old cohort study (n=10) — all other trials are in T2DM populations. Combined with a **Blocking** data gap on local label warnings/contraindications and the fact that the drug is not currently marketed in India, the evidence base does not yet support proceeding.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain official package insert / label warnings and contraindications before any safety review
- Resolve DG002 (High): confirm mechanism of action via DrugBank API for a rigorous mechanistic-link assessment
- A dedicated, adequately powered study of voglibose as insulin adjunct specifically in T1DM (the current cohort evidence is too small and dated to support a decision)
- Clarify local regulatory pathway, since voglibose has zero registrations in India today
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

