---
layout: default
title: Sirolimus
parent: Moderate Evidence (L3-L4)
nav_order: 775
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Sirolimus: predicted new indication Liposarcoma (evidence level L3). Approved use: Renal cell carcinoma (including clear cell and non-papillary subtypes)"
---

# Sirolimus
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

# Sirolimus: From Renal Cell Carcinoma and Lymphangioleiomyomatosis to Liposarcoma

## One-Sentence Summary

Sirolimus is an mTOR inhibitor originally used for renal cell carcinoma and lymphangioleiomyomatosis (LAM).
The TxGNN model predicts it may be effective for **liposarcoma**, but this is supported by only **1 clinical trial** (a single-arm Phase 2 combination study) and mostly indirect literature.
Among the other predictions, **lymphangiomyoma (LAM)** has by far the strongest support, but it overlaps with an existing original indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma (including clear cell and non-papillary subtypes); lymphangioleiomyomatosis |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 15 |
| Recommended Decision | Hold (research question; not ready to advance) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, sirolimus inhibits mTORC1, a kinase that drives cell growth and proliferation. Its efficacy in renal cell carcinoma and LAM, both settings with mTOR pathway activation, is established.

The PI3K/AKT/mTOR pathway is reported to be activated in soft tissue sarcomas, including liposarcoma. This is the mechanistic basis for the prediction. Mouse models also suggest that mTOR inhibition can slow tumour growth in sarcoma.

The support is still thin. The only linked trial is a single-arm study of sirolimus combined with another agent, so sirolimus's own contribution cannot be separated. The rest is review-level sarcoma literature and indirect transplant data on cancer risk.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Single-arm, multicentre study of sirolimus plus cyclophosphamide in metastatic or unresectable myxoid liposarcoma and chondrosarcoma. No efficacy results were provided. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT (indirect) | J Am Soc Nephrol | In renal transplant patients, sirolimus after early cyclosporine withdrawal reduced the risk of cancer. This is not a liposarcoma study. |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of novel therapeutics and recent regulatory approvals in soft tissue sarcoma. |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Rationale and results of molecular-targeted agents in advanced sarcomas. |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Targeted treatments for rare connective tissue tumours and sarcomas. |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Review | Transplant Proc | Cancer screening in renal transplant patients on long-term immunosuppression (indirect). |

## India Market Information

Sirolimus has 15 valid single-ingredient registrations. The data compiled for this report do not include approved indication text for any of them. Representative products:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 185868 | Rapamune 1mg Tablet (Pfizer Ltd) | Strip of 10 tablets | Not stated |
| 191166 | Raparen 1mg Injection (La Renon Healthcare) | Vial of 1 injection | Not stated |
| 190480 | Rapacan 2mg Capsule (Biocon) | Strip of 10 capsules | Not stated |
| 200266 | Siromus 1mg Tablet (Zydus Cadila) | Strip of 6 tablets | Not stated |
| 222768 | Toraft 1mg Tablet (Torrent) | Strip of 10 tablets | Not stated |

Available forms are oral (tablet, capsule) and injectable.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor, immunosuppressant); not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; typically blood counts, liver and renal function, lipids, glucose and drug trough levels |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindication signals (knowledge-graph associations, not label text):** hypertension, kidney disease, liver disease, hyperglycaemia and diabetes, hyperlipidaemia and hypertriglyceridaemia, infections (including pneumocystosis and cytomegalovirus infection), interstitial lung disease, stroke and cerebrovascular disorders, hyperbilirubinaemia, pericardial effusion, progressive multifocal leukoencephalopathy, and certain cancers (including brain cancer). These should be verified against the product label.
- **Drug Interactions:** 645 interactions were identified. Major interactions include amphotericin B (including lipid complex), clarithromycin, mesalazine and balsalazide. Moderate interactions include corticosteroids (dexamethasone, hydrocortisone, betamethasone, budesonide, triamcinolone), antidiabetic agents (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, dapagliflozin, chlorpropamide, albiglutide), cimetidine and aprepitant.

Please refer to the package insert for label warnings and contraindications.

## Other Predicted Indications

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 5 | Lymphangiomyoma (LAM) | 99.79% | L1 | Proceed with Guardrails. Phase 3 MILES trial ([NCT00414648](https://clinicaltrials.gov/study/NCT00414648), n=89, completed) plus the ongoing Phase 3 early-disease trial ([NCT03150914](https://clinicaltrials.gov/study/NCT03150914)). This is an established use, not true repurposing. |
| 9 | Lung PEComa | 99.63% | L3 | Proceed with Guardrails. Evidence is transferred from LAM; confirm the diagnosis. |
| 4 | Benign PEComa | 99.80% | L4 | Research Question. Strong mechanism (TSC1/TSC2 loss), but support is mostly case reports. |
| 3 | Uterine corpus PEComa | 99.80% | L4 | Research Question. No site-specific records. |
| 2, 6, 7, 8, 10 | Ovarian myxoid liposarcoma, unclassified RCC, RCC with neuroblastoma, Xp11.2/TFE3 RCC, vulva sarcoma | 99.6–99.8% | L5 | Hold. Prediction score only, with no direct evidence. |

## Conclusion and Next Steps

**Decision: Hold (Research Question)** for the lead prediction, liposarcoma.

**Rationale:**
The evidence consists of one single-arm combination trial with no reported results, plus reviews and indirect transplant data. This is not enough to separate sirolimus's own effect in liposarcoma. The best-supported candidates are LAM-related, which is an existing indication rather than new repurposing, and these could proceed with guardrails.

**To proceed, the following is needed:**
- Results and sirolimus-specific contribution from NCT02821507, and confirmation of the liposarcoma subtypes enrolled
- Detailed mechanism of action data (MOA)
- Package insert warnings, contraindications and approved indications for the Indian products
- A plan for managing drug interactions, infection risk, metabolic effects (lipids, glucose) and trough-level monitoring
- Site-specific literature searches for PEComa subtypes before any further decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

