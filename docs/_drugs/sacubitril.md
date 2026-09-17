---
layout: default
title: Sacubitril
parent: Model Prediction Only (L5)
nav_order: 752
evidence_level: L5
indication_count: 5
---

# Sacubitril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Sacubitril: From Heart Failure to Diabetic Nephropathy

## One-Sentence Summary

> Sacubitril is the neprilysin-inhibitor component of the ARNI combination (sacubitril/valsartan), whose proven use is in heart failure with reduced ejection fraction (HFrEF).
> The TxGNN model's five candidate indications include several that lack any biological plausibility, but **diabetic nephropathy** stands out as the only candidate supported by real evidence —
> **2 clinical trials** (including a completed real-world study and a Phase 4 RCT in setup) and **20 publications**, including a post-hoc analysis of the pivotal PARADIGM-HF trial.

**Note on candidate selection**: TxGNN's raw top-ranked prediction (rank 1, "brain small vessel disease 1 with or without ocular anomalies," score 99.58%) and three other candidates (ranks 2, 4, 5) have **no clinical trials, no relevant literature, and no mechanistic link** to neprilysin inhibition — the evidence pack itself flags these as likely embedding noise rather than genuine signal. This report therefore focuses on **diabetic nephropathy (rank 3)**, the only candidate with a coherent mechanism and supporting data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Heart failure with reduced ejection fraction (HFrEF) — inferred from trial/literature context (e.g., NCT04735354, PARADIGM-HF); not formally recorded in this evidence pack |
| Predicted New Indication | Diabetic Nephropathy |
| TxGNN Prediction Score | 99.50% (rank 8,395 among all candidates) |
| Evidence Level | L3 (observational studies / post-hoc RCT analysis; no completed prospective RCT with renal endpoints) |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in this evidence pack (marked as a data gap). Based on known pharmacology, sacubitril is the prodrug component of the angiotensin receptor–neprilysin inhibitor (ARNI) combination sacubitril/valsartan, whose efficacy in HFrEF is well established (referenced within this pack via the PARADIGM-HF post-hoc analysis, PMID 29661699, and the India real-world HFrEF study NCT04735354).

Mechanistically, neprilysin inhibition raises circulating natriuretic peptides (ANP/BNP/CNP), which improve glomerular hemodynamics, reduce proteinuria, and exert anti-inflammatory and anti-fibrotic effects on the kidney. Combined with valsartan's RAAS blockade, this dual action plausibly extends beyond cardiac benefit into renal protection — a rationale reinforced by multiple animal models of diabetic kidney disease (db/db mice, streptozotocin-induced diabetic rats) showing reduced glomerulosclerosis and oxidative stress with sacubitril/valsartan treatment.

Clinically, this is supported by a completed BOLD-MRI cohort study in type 2 diabetics (PMID 40416927) and a randomized human study in diabetic nephropathy patients with hypertension (PMID 37549515), plus an ongoing Phase 4 RCT (NCT06501651) specifically designed to compare sacubitril/valsartan against valsartan alone in type 2 diabetic nephropathy. However, no completed RCT with hard renal endpoints (eGFR decline, ESRD) yet exists — evidence remains at the observational/mechanistic tier.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06501651](https://clinicaltrials.gov/study/NCT06501651) | Phase 4 | Not yet recruiting | 297 | RCT comparing sacubitril/valsartan vs. valsartan in essential hypertension with type 2 diabetic nephropathy; 12-week treatment period, 2:1 randomization |
| [NCT04735354](https://clinicaltrials.gov/study/NCT04735354) | N/A (observational) | Completed | 268 | Retrospective real-world EMR study of sacubitril/valsartan in HFrEF patients in India; supports safety/utilization pattern but not renal-specific |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37549515](https://pubmed.ncbi.nlm.nih.gov/37549515/) | 2023 | RCT (human) | Int Immunopharmacol | 112 diabetic nephropathy + hypertension patients randomized to nifedipine + valsartan vs. nifedipine + sacubitril/valsartan; evaluated renal function outcomes |
| [29661699](https://pubmed.ncbi.nlm.nih.gov/29661699/) | 2018 | Secondary analysis of RCT | Lancet Diabetes Endocrinol | Post-hoc analysis of PARADIGM-HF: neprilysin inhibition effect on renal function in T2DM patients with chronic heart failure on target RAAS-inhibitor doses |
| [40416927](https://pubmed.ncbi.nlm.nih.gov/40416927/) | 2025 | Cohort (imaging) | Diabetes Metab Syndr Obes | BOLD-MRI study evaluating renal protective effects of sacubitril/valsartan in type 2 diabetics |
| [37625003](https://pubmed.ncbi.nlm.nih.gov/37625003/) | 2023 | Review | Diabetes Care | Update on pillars of diabetic kidney disease therapy, including RAAS blockade and emerging agents |
| [34431635](https://pubmed.ncbi.nlm.nih.gov/34431635/) | 2021 | Review | Rev Med Suisse | Potential role of sacubitril/valsartan in type 2 diabetes management, including glycemic and renal effects |
| [35165832](https://pubmed.ncbi.nlm.nih.gov/35165832/) | 2022 | Review | Curr Hypertens Rep | Review of newer BP-lowering drugs targeting hypertensive target organ (including renal) damage |
| [35975848](https://pubmed.ncbi.nlm.nih.gov/35975848/) | 2023 | Review | Curr Diabetes Rev | Cardiorenal complications of diabetes and novel combination therapies |
| [33870733](https://pubmed.ncbi.nlm.nih.gov/33870733/) | 2021 | Animal study | Am J Physiol Renal Physiol | Differential effects of sacubitril/valsartan vs. valsartan on diabetic kidney disease in db/db and KKAy mice |
| [35992034](https://pubmed.ncbi.nlm.nih.gov/35992034/) | 2022 | Animal study | Diabetes Metab Syndr Obes | Sacubitril/valsartan improves early diabetic nephropathy in rats via NLRP3 inflammasome inhibition |
| [37202215](https://pubmed.ncbi.nlm.nih.gov/37202215/) | 2023 | Animal study | Nephrol Dial Transplant | Sacubitril/valsartan ameliorates renal tubulointerstitial injury via increased renal plasma flow in diabetic mice with aldosterone excess |

---

## India Market Information

Sacubitril currently has **no marketing authorization registered in India** (0 licenses on file; market status: not marketed). No product-level dosage form or indication data is available.

---

## Safety Considerations

**Drug Interactions** (from DDInter, 6 total, all Moderate severity):

| Interacting Drug | Interaction Level |
|---|---|
| Nitisinone | Moderate |
| Rosuvastatin | Moderate |
| Simvastatin | Moderate |
| Cobicistat | Moderate |
| Revefenacin | Moderate |
| Alpelisib | Moderate |

No package-insert-level warnings or contraindications were available in this evidence pack; please refer to the official product label for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for renal protection is biologically sound and supported by consistent animal and early human data, but no completed prospective RCT with hard renal endpoints exists yet — the only purpose-built Phase 4 trial (NCT06501651) has not started recruiting. Evidence level L3 does not meet the bar for a Go or even a guarded proceed at this stage.

**To proceed, the following is needed:**
- Completion and results of NCT06501651 (Phase 4 RCT, sacubitril/valsartan vs. valsartan in T2DM nephropathy)
- Full mechanism-of-action documentation (currently a data gap, DG002)
- India-specific regulatory/label review, since the drug is not currently marketed there (DG001 — TFDA label warnings/contraindications required before any S1 safety screening)
- Renal-specific hard-endpoint data (eGFR slope, progression to ESRD) beyond the current surrogate/imaging and animal-model evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

