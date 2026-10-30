---
layout: default
title: Imiquimod
parent: Model Prediction Only (L5)
nav_order: 429
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "Imiquimod"
predicted_indications: ["pre-malignant neoplasm", "benign neoplasm of buccal mucosa", "cervical neuroblastoma", "odontogenic cyst", "benign neoplasm of tongue", "nasopharyngeal teratoma", "cystic neoplasm", "inner ear neoplasm", "neoplasm of major salivary gland", "schwannoma of jugular foramen"]
description: "Imiquimod: predicted new indication Pre-malignant neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Imiquimod
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Imiquimod: Pre-malignant neoplasm
{: .text-alpha }

## One-Sentence Summary

Imiquimod is a topical immune response modifier, originally used for actinic keratosis, superficial basal cell carcinoma and anogenital warts.
The TxGNN model predicts it may be effective for **pre-malignant neoplasm**,
with **2 clinical trials** and **9 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pre-malignant neoplasm |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 (see note below) |
| India Market Status | Listed in a compiled Indian medicine price dataset (3 of 3) – CDSCO approval status is not included in this data |
| Number of Listed Products | 3 (valid: 3) |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* Under the strict rule (≥2 completed Phase 3 RCTs), the data compiled for this report would not reach L1. Only one Phase 3 trial is completed (a small open-label, single-arm study), and the other was a terminated RCT. The L1 label reflects the strong evidence for the approved indications, and the evidence for the extension to other pre-malignant sites is closer to L3 (reviews and case reports). The decision below should be read with that in mind.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known information, imiquimod is a Toll-like receptor 7 (TLR7) agonist. It triggers local innate and adaptive immune responses (interferon-alpha, TNF-alpha, IL-12) that help clear dysplastic or HPV-infected epithelium.

Its original uses (actinic keratosis, superficial basal cell carcinoma, HPV-related warts) are all conditions of abnormal skin epithelium, and several are pre-malignant. Pre-malignant neoplasm is therefore a natural extension. The same immune mechanism could plausibly act on other intraepithelial neoplasias, such as cervical, vulvar and anal lesions.

Evidence for the approved skin indications is strong. For the other pre-malignant sites it comes mainly from reviews and case reports.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label study of imiquimod 5% cream, 3 days per week, for actinic keratoses on the head; assessed duration of effect. Small, single-arm. |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | Randomized trial of topical imiquimod for high-grade cervical intraepithelial neoplasia, as an alternative to excisional treatment. Terminated early; too small to support efficacy conclusions. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Interventions for anal canal intraepithelial neoplasia, a pre-malignant HPV-associated condition |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Medical interventions for high-grade vulval intraepithelial neoplasia |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Combined treatments with photodynamic therapy for non-melanoma skin cancer |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Current management of actinic keratoses, including topical field therapies |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Topical strategies for non-melanoma skin cancer and precursor lesions, including imiquimod |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case report | Int J STD AIDS | Successful treatment of high-grade vulval intra-epithelial neoplasia with imiquimod 5% in a renal transplant recipient |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case report | Int J STD AIDS | Clearance of bowenoid papulosis of the penis with topical imiquimod 5% |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical | Urol Oncol | Pharmacokinetics of related TLR7 agonists in a rat model, for bladder cancer |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 107760 | Imiquad Cream (0.25gm Each) | Sachet of 3 creams | Not stated in the licence record |
| Registration No. 182926 | Qmica 12.5mg Cream | Tube of 1 gm cream | Not stated in the licence record |
| Registration No. 151164 | Nilwart Cream | Tube of 3 gm cream | Not stated in the licence record |

All three products are topical single-ingredient creams and are currently valid.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (topical immune response modifier, TLR7 agonist), not a conventional cytotoxic |
| Myelosuppression Risk | Low with topical use; please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Low with topical use |
| Monitoring Items | Local skin reactions; please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Disease contraindication signals (knowledge graph, not label text):** photosensitivity disease, sunburn, photoparoxysmal response, autoimmune disease, graft versus host disease.
- **Case-report safety signals:** malignant conversion of oral papillomatosis during imiquimod therapy; erythema multiforme and lichen planopilaris after topical use in Gorlin syndrome patients; a new mucinous carcinoma arising during treatment of extramammary Paget disease.
- **Drug Interactions:** 59 potential interactions were recorded, all with an unclassified severity level. Examples include warfarin, clopidogrel, prednisone, prednisolone, budesonide, hydroxychloroquine, simvastatin, morphine and ibuprofen. Clinical significance should be checked in a drug interaction reference.

Package insert warnings and contraindications for the India products were not available. Please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Imiquimod has well-established use in actinic keratosis and other HPV-related and pre-malignant skin lesions, and a plausible immune mechanism supports extension to other intraepithelial neoplasias. However, the direct trial evidence for new sites is thin (one small completed Phase 3 study and one terminated RCT), so the extension rests mainly on reviews and case reports.

**To proceed, the following is needed:**
- The India package insert warnings and contraindications, which are a blocking gap for safety screening
- Detailed mechanism of action data (MOA)
- Adequately powered randomized trials in non-skin pre-malignant sites (cervical, vulvar, anal)
- A safety plan covering photosensitivity, autoimmune disease and transplant or immunosuppressed patients
- Confirmation of the approved indication text for the three India products

### Other Predicted Indications (for reference)

Other predictions ranked lower. Oral mucosal benign neoplasm and odontogenic cyst (via Gorlin syndrome) are research questions supported only by reviews, animal studies and case reports. Seven other predictions (including cervical neuroblastoma, nasopharyngeal teratoma, inner ear neoplasm, major salivary gland neoplasm and jugular foramen schwannoma) have little or no relevant evidence and should be held.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

