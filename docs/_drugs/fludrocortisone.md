---
layout: default
title: Fludrocortisone
parent: Model Prediction Only (L5)
nav_order: 361
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
description: "Fludrocortisone: predicted new indication Primary cutaneous T-cell lymphoma (evidence level L5). Approved use: Not stated in the licence data compiled for this report"
monitor_inn: "Fludrocortisone"
predicted_indications: ["primary cutaneous T-cell lymphoma", "cystic teratoma", "spinal cord dermoid cyst", "dermoid cyst of ovary", "disease of orbital part of eye adnexa", "eye disease", "disease of orbital region", "exostosis"]
---

# Fludrocortisone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Fludrocortisone: From Mineralocorticoid Replacement to Primary Cutaneous T-Cell Lymphoma
{: .text-alpha }

## One-Sentence Summary

Fludrocortisone is an oral corticosteroid with mainly mineralocorticoid activity, marketed in India as single-ingredient tablets.
The TxGNN model's top prediction is **primary cutaneous T-cell lymphoma**, but it is supported by **no clinical trials and no publications**, so it is a model prediction only.
The best-supported direction among the other predictions is **eye disease**, with **0 clinical trials** and **22 publications**, most of them indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data compiled for this report |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (3 of 3) – CDSCO approval status is not included in this data |
| Number of Listed Products | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fludrocortisone is a mineralocorticoid with some glucocorticoid activity. It is used clinically for conditions such as adrenal insufficiency and orthostatic hypotension, as seen in the literature compiled for this report.

For primary cutaneous T-cell lymphoma, the link is speculative. Glucocorticoid-mediated lymphocyte apoptosis could plausibly matter in T-cell malignancies. However, fludrocortisone's glucocorticoid potency is low, and corticosteroids used for this lymphoma are other agents. The high score (0.9958) reflects model similarity only, and no trial or publication supports it.

The other predictions are weaker still:
- **Cystic teratoma, spinal cord dermoid cyst, dermoid cyst of ovary, exostosis:** No plausible mechanistic link was found. These are structural or developmental lesions, typically managed surgically. The predictions probably reflect TxGNN model (deep learning) artifacts.
- **Disease of orbital part of eye adnexa, disease of orbital region:** Only a generic corticosteroid anti-inflammatory rationale exists, not specific to fludrocortisone.
- **Eye disease:** This has indirect and preclinical support (see Literature Evidence) and is the most credible of the predicted directions.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top predicted indication, primary cutaneous T-cell lymphoma, or for any other predicted indication in the data compiled for this report.

---

## Literature Evidence

No literature was found for primary cutaneous T-cell lymphoma. The table below covers the most relevant publications for the best-supported alternative, **eye disease** (rank 6). Most other retrieved papers are reviews or case reports on autonomic, endocrine or renal conditions that mention fludrocortisone for its established uses, not for eye disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36161841](https://pubmed.ncbi.nlm.nih.gov/36161841/) | 2022 | Phase 1B study | BMJ Open Ophthalmol | Safety and tolerability of single intravitreal fludrocortisone acetate (1 mg and 2 mg) in geographic atrophy secondary to age-related macular degeneration |
| [34509498](https://pubmed.ncbi.nlm.nih.gov/34509498/) | 2021 | Preclinical | Exp Eye Res | Fludrocortisone showed anti-inflammatory and neuroprotective effects on Müller cell cytokine responses in retinal degeneration models |
| [11008895](https://pubmed.ncbi.nlm.nih.gov/11008895/) | 1999 | Clinical study (small) | Int Ophthalmol | Evaluated fludrocortisone for systemic hypotension in primary open-angle glaucoma patients, targeting a vascular risk factor rather than the eye disease directly |
| [17998043](https://pubmed.ncbi.nlm.nih.gov/17998043/) | 2007 | Review | Surv Ophthalmol | Non-IOP-lowering glaucoma approaches; notes fludrocortisone is used by some physicians to avoid blood pressure dips |
| [23430676](https://pubmed.ncbi.nlm.nih.gov/23430676/) | 2013 | Review | Klin Monbl Augenheilkd | Similar review of non-IOP-lowering glaucoma therapy, including salt and fludrocortisone |
| [31994621](https://pubmed.ncbi.nlm.nih.gov/31994621/) | 2019 | Review/case | Rev Assoc Med Bras | Autoimmune polyglandular syndrome type 2 (Addison's disease with thyroid disease and/or type 1 diabetes) |
| [15934882](https://pubmed.ncbi.nlm.nih.gov/15934882/) | 2005 | Review | Expert Opin Pharmacother | Pharmacological treatments for familial dysautonomia, a disorder with ophthalmological involvement |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 136024 | Minocort Tablet | Strip of 10 tablets | Not stated |
| 85156 | Fludrol Tablet | Strip of 10 tablets | Not stated |
| 84139 | Floricot Tablet | Strip of 10 tablets | Not stated |

All three registrations are valid single-ingredient oral products.

---

## Safety Considerations

- **Drug Interactions:** 446 interactions were identified. Notable examples:
  - **Major:** Bupropion.
  - **Moderate:** Antidiabetic agents (acarbose, pioglitazone, alogliptin, linagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, albiglutide, dulaglutide), amphotericin B, aprepitant, acetylsalicylic acid, clarithromycin, bisacodyl, picosulfuric acid, and the anabolic steroids oxandrolone and oxymetholone.
- **Ocular considerations:** For any eye-related hypothesis, known corticosteroid ocular risks (raised intraocular pressure, cataract) must be weighed.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, primary cutaneous T-cell lymphoma, has no trials or literature and only a speculative mechanism, and the other model-only predictions lack plausible mechanisms. Eye disease is the only direction with indirect or preclinical support (a Phase 1B safety study and preclinical retinal work), and it has no efficacy evidence, so it is best treated as a research question rather than a candidate to advance.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications for the Indian products (a blocking gap for safety screening)
- Detailed mechanism of action data
- A focused hypothesis for the eye direction (for example, retinal degeneration neuroprotection or glaucoma with systemic hypotension), with efficacy data beyond the Phase 1B safety study
- Any preclinical or clinical evidence for primary cutaneous T-cell lymphoma, if that direction is to be pursued
- An assessment of route compatibility, since the marketed forms are oral tablets while the ocular studies used intravitreal administration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

