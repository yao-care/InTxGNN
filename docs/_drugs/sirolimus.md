---
layout: default
title: Sirolimus
parent: Model Prediction Only (L5)
nav_order: 775
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-24
monitor_inn: "Sirolimus"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lung PEComa", "vulva sarcoma"]
description: "Sirolimus: predicted new indication Liposarcoma (evidence level L5). In India: 15 listed products (15 not discontinued)"
---

# Sirolimus
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Sirolimus: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Sirolimus is an mTOR inhibitor that is currently marketed in India under 15 valid licences. The TxGNN model predicts it may be useful for **liposarcoma**. Only **1 completed single-arm Phase 2 trial** (a sirolimus combination) is linked, and it has no posted results. No published study directly tests sirolimus in liposarcoma, so the evidence is classed as model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (15 of 15) – CDSCO approval status is not included in this data |
| Number of Listed Products | 15 (valid: 15) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for sirolimus: "Sirolimus in FYARRO is an inhibitor of mechanistic target of rapamycin kinase (mTOR, previously known as mammalian target of rapamycin). mTOR, a serine threonine kinase, is downstream of the PI3K/AKT pathway, controls key cellular processes such as cell survival, growth, and proliferation, and is commonly dysregulated in several human cancers. In cells, sirolimus binds to the immunophilin, FK Binding Protein-12 (FKBP-12), to generate an immunosuppressive complex." ([DailyMed: Fyarro (sirolimus) prescribing information, Aadi Bioscience, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0f9bb784-53e2-46f9-a65d-1c6c2a230eaf), label version 2026-09-09; accessed 2026-11-19.) Sirolimus is known to inhibit mTORC1. Activation of the PI3K/AKT/mTOR pathway has been reported in soft tissue sarcomas, including liposarcoma. Blocking mTORC1 could therefore slow tumour growth.

This is a mechanistic hypothesis only. The linked trial tests sirolimus in combination with another drug, so sirolimus's own contribution cannot be separated. The sarcoma literature is limited to reviews. Transplant data showing lower cancer risk under sirolimus are indirect and do not show activity against liposarcoma.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm, multicentre trial of sirolimus plus cyclophosphamide in metastatic or unresectable myxoid liposarcoma and chondrosarcoma. It was motivated by preclinical data suggesting mTOR inhibition can prevent tumour growth. No results are published or posted, and the combination design cannot isolate sirolimus's effect. |

## Literature Evidence

None of these publications reports a test of sirolimus in liposarcoma. They are background or indirect evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT (indirect) | J Am Soc Nephrol | In renal transplant recipients, switching to sirolimus after early cyclosporine withdrawal reduced the risk of cancer. This is a transplant outcome, not liposarcoma treatment. |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of novel therapeutics in soft tissue sarcoma. |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Rationale and results of recent trials of molecular-targeted agents in advanced sarcomas. |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Targeted treatments for molecular subgroups of rare connective tissue tumours and sarcomas. |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Review | Transplant Proc | Cancer screening in renal transplant patients on long-term immunosuppression (indirect). |

## India Market Information

Sirolimus has 15 valid licences, all for single-ingredient products. The approved-indication text is not recorded in the local data.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 77810 | Emtor 1mg Tablet | Strip of 10 tablets | Valid |
| 126694 | Limus 1mg Tablet | Strip of 10 tablets | Valid |
| 185292 | Rapacan 1mg Tablet | Strip of 10 tablets | Valid |
| 185868 | Rapamune 1mg Tablet | Strip of 10 tablets | Valid |
| 188877 | Rocas 1mg Tablet | Strip of 6 tablets | Valid |
| 189703 | Raparen 1mg Tablet | Strip of 10 tablets | Valid |
| 190334 | Rapasim 1 Tablet | Strip of 10 tablets | Valid |
| 190480 | Rapacan 2mg Capsule | Strip of 10 capsules | Valid |
| 191166 | Raparen 1mg Injection | Vial of 1 Injection | Valid |
| 194644 | Rapolax 1mg Tablet | Strip of 10 tablets | Valid |
| 200266 | Siromus 1mg Tablet | Strip of 6 tablets | Valid |
| 202617 | Sirova 1mg Tablet | Strip of 10 tablets | Valid |
| 203491 | Siropan 1mg Tablet | Strip of 10 tablets | Valid |
| 208617 | Sirotrend 1mg Tablet | Strip of 10 tablets | Valid |
| 222768 | Toraft 1mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 645 interactions are recorded. Examples classed as Major include amphotericin B (including the lipid complex), mesalazine, balsalazide and clarithromycin. Moderate examples include several corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, dapagliflozin), cimetidine and aprepitant.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting study is an unpublished single-arm Phase 2 combination trial. No published study tests sirolimus in liposarcoma, and the remaining literature is indirect. The high model score and the plausible mTOR rationale justify further research, not a decision to advance.

**To proceed, the following is needed:**
- Results of NCT02821507, with the liposarcoma subgroup and the contribution of sirolimus separated from cyclophosphamide
- Published clinical studies of sirolimus in liposarcoma
- Detailed mechanism-of-action data
- Package insert warnings and contraindications for the marketed products
- A plan to manage the large number of drug interactions

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data for sirolimus are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Fyarro (sirolimus) prescribing information, Aadi Bioscience, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0f9bb784-53e2-46f9-a65d-1c6c2a230eaf) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

