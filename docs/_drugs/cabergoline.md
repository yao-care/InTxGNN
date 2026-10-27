---
layout: default
title: Cabergoline
parent: Model Prediction Only (L5)
nav_order: 128
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Cabergoline: predicted new indication Pituitary cancer (evidence level L5). Approved use: Hyperprolactinemia and prolactin-producing pituitary tumour"
monitor_inn: "Cabergoline"
predicted_indications: ["progeria-short stature-pigmented nevi syndrome", "pituitary cancer", "cerebral palsy, spastic quadriplegic", "glaucoma"]
---

# Cabergoline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Cabergoline: From Hyperprolactinemia to Pituitary Cancer
{: .text-alpha }

## One-Sentence Summary

Cabergoline is a dopamine D2 receptor agonist originally used to treat hyperprolactinemia and prolactin-producing pituitary tumours.
The TxGNN model predicts it may be effective for **Pituitary Cancer**, with **14 clinical trials** and **20 publications** on pituitary tumours currently supporting this direction.
Almost all of this evidence concerns pituitary adenomas (mostly prolactinomas), not true pituitary carcinoma, so the extrapolation is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperprolactinemia and prolactin-producing pituitary tumour (the India licence records contain no approved indication text) |
| Predicted New Indication | Pituitary cancer |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L1 (adenoma-spectrum evidence; indirect for carcinoma) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

Note: The highest-scoring prediction (rank 1) was pituitary adenocarcinoma, but the best-supported prediction is pituitary cancer (rank 3), so this report focuses on the latter. The other predictions (progeria-short stature-pigmented nevi syndrome, spastic quadriplegic cerebral palsy, glaucoma) have little or no support and are not recommended (see the end of the report).

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the data compiled for this report. Based on known pharmacology, cabergoline is a D2 dopamine receptor agonist. Pituitary tumour cells, particularly lactotroph adenomas and some nonfunctioning and corticotroph adenomas, express D2 receptors. Activating these receptors lowers hormone secretion and can shrink the tumour.

The original indication (prolactin-secreting pituitary tumours) and the predicted indication (pituitary cancer) both involve neoplasms of the pituitary. Cabergoline's efficacy in prolactinomas is well established. Trials and studies in nonfunctioning and corticotroph adenomas are growing, and a 2020 review (PMID 31597135) discusses its anti-tumour mechanisms and potential broader applications.

The main caveat is that true pituitary carcinoma is very rare. The supplied evidence concerns adenomas, so any benefit in carcinoma is extrapolated. The high TxGNN score is a model prediction, not clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00889525](https://clinicaltrials.gov/study/NCT00889525) | Phase 3 | Completed | Not reported | Cabergoline for Cushing disease due to corticotroph pituitary adenoma (D2 receptor expressed in vitro) |
| [NCT03271918](https://clinicaltrials.gov/study/NCT03271918) | Phase 3 | Completed | 140 | Randomized trial of cabergoline in residual nonfunctioning pituitary adenoma after surgery |
| [NCT02288962](https://clinicaltrials.gov/study/NCT02288962) | Phase 3 | Active, not recruiting | 60 | Randomized trial of dopamine agonist treatment in nonfunctioning pituitary adenomas |
| [NCT07463235](https://clinicaltrials.gov/study/NCT07463235) | Phase 3 | Recruiting | 70 | High vs standard cabergoline dose in microprolactinomas (safety and remission) |
| [NCT01620138](https://clinicaltrials.gov/study/NCT01620138) | Phase 2/3 | Completed | 21 | Somatostatin and dopamine receptor expression in nonfunctioning adenomas and resistant prolactinomas, with in vitro and in vivo responses |
| [NCT07034859](https://clinicaltrials.gov/study/NCT07034859) | Phase 4 | Enrolling by invitation | 30 | Cabergoline as primary therapy for nonfunctioning pituitary adenoma, 48 weeks |
| [NCT00376064](https://clinicaltrials.gov/study/NCT00376064) | Phase 4 | Completed | 20 | Octreotide plus cabergoline in partially responsive acromegaly |
| [NCT01915303](https://clinicaltrials.gov/study/NCT01915303) | Phase 2 | Terminated | 68 | Pasireotide alone or with cabergoline in Cushing's disease |
| [NCT07045935](https://clinicaltrials.gov/study/NCT07045935) | Phase 4 | Recruiting | 60 | Metabolic outcomes of dopamine agonist treatment in prolactinomas |
| [NCT00460616](https://clinicaltrials.gov/study/NCT00460616) | N/A | Completed | 50 | Observational study of cardiac abnormalities and valvular regurgitation in long-term cabergoline-treated prolactinoma patients |

None of these trials studies pituitary carcinoma specifically.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30540568](https://pubmed.ncbi.nlm.nih.gov/30540568/) | 2019 | Randomized trial | Am J Clin Oncol | 2-year open-label trial of cabergoline in residual nonfunctioning pituitary adenoma |
| [37097352](https://pubmed.ncbi.nlm.nih.gov/37097352/) | 2023 | Review | JAMA | Diagnosis and management of pituitary adenomas |
| [40876473](https://pubmed.ncbi.nlm.nih.gov/40876473/) | 2025 | Review | Lancet Diabetes Endocrinol | Pathogenesis, diagnosis and management of prolactin-secreting adenomas |
| [36974474](https://pubmed.ncbi.nlm.nih.gov/36974474/) | 2023 | Review | J Clin Endocrinol Metab | Approach to the patient with prolactinoma |
| [36013562](https://pubmed.ncbi.nlm.nih.gov/36013562/) | 2022 | Review | Medicina (Kaunas) | Treatment of prolactinoma, including multimodality therapy for aggressive prolactinomas |
| [31597135](https://pubmed.ncbi.nlm.nih.gov/31597135/) | 2020 | Review | Neuroendocrinology | New anti-tumour mechanisms of cabergoline and potential broader applications |
| [38989697](https://pubmed.ncbi.nlm.nih.gov/38989697/) | 2024 | Preclinical | Neuro-oncology | Targeting HTR2B suppresses nonfunctioning adenoma growth and sensitizes cells to cabergoline |
| [28025719](https://pubmed.ncbi.nlm.nih.gov/28025719/) | 2017 | Review | Pituitary | Cabergoline use in acromegaly |
| [25732645](https://pubmed.ncbi.nlm.nih.gov/25732645/) | 2015 | Review | Endocrinol Metab Clin North Am | Cabergoline in pituitary tumours and valvular disorders; most studies find no significant valvulopathy risk |
| [36511080](https://pubmed.ncbi.nlm.nih.gov/36511080/) | 2023 | Case report | Echocardiography | Cardiac valvulopathy after 15 years of low-dose cabergoline (cumulative dose 572 mg) |

---

## India Market Information

Cabergoline is marketed in India with 20 valid single-ingredient registrations. The licence records contain no approved indication text. Main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 36862 | Caberlact 0.25mg Tablet (Neon Laboratories) | Strip of 2 tablets | Not stated in records |
| 182542 | Parcar 1mg Tablet (Zydus Cadila) | Strip of 4 tablets | Not stated in records |
| 34407 | Caberlin 0.25 Tablet (Sun Pharmaceutical) | Strip of 4 tablets | Not stated in records |
| 37029 | Colette 0.25mg Tablet (Cipla) | Strip of 4 tablets | Not stated in records |
| 33955 | Cabgolin 0.5 Tablet (Sun Pharmaceutical) | Strip of 4 tablets | Not stated in records |

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver disease, gallbladder disease, heart valve disease, pulmonary fibrosis (including postinflammatory), IgG4-related retroperitoneal fibrosis, severe pre-eclampsia and pre-eclampsia.
- **Cardiac valvulopathy**: Long-term, high-dose use carries a valvulopathy signal (PMID 36511080), although most studies show no significant association at typical doses (PMID 25732645). Echocardiographic monitoring is advised.
- **Drug interactions**: 60 interactions were identified. Major: lorcaserin and clarithromycin. Moderate: metoclopramide. Others (e.g. omeprazole, metformin, prednisone, simvastatin) have unclassified severity.
- **Angle-closure glaucoma**: A case report describes bilateral angle-closure glaucoma with cabergoline (PMID 21347189).

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed and ongoing Phase 3 trials, plus a randomized trial, support cabergoline in the pituitary tumour spectrum (nonfunctioning and corticotroph adenomas), with a plausible D2 receptor mechanism. However, none addresses true pituitary carcinoma, so this is an indirect extrapolation and not direct proof.

**To proceed, the following is needed:**
- Evidence specific to aggressive pituitary tumours or carcinoma (case series, registry data)
- Package insert warnings and contraindications for India-marketed products
- Detailed mechanism of action data
- A dosing and monitoring plan (echocardiography, dose individualization)

**Other predictions (Hold):** Pituitary adenocarcinoma has only case-report-level support. Progeria-short stature-pigmented nevi syndrome and spastic quadriplegic cerebral palsy have no evidence beyond the model score. Glaucoma is not supported, since the available reports suggest cabergoline may cause angle-closure glaucoma rather than treat it.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

