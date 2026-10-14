---
layout: default
title: Tamoxifen
parent: Moderate Evidence (L3-L4)
nav_order: 805
evidence_level: L4
indication_count: 10
---

# Tamoxifen
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Tamoxifen: From Female Breast Carcinoma to Mammary Paget Disease

## One-Sentence Summary

Tamoxifen is an estrogen receptor-blocking hormone therapy originally used to treat breast cancer (female breast carcinoma and ductal carcinoma).
The TxGNN model predicts it may be effective for **Mammary Paget Disease**,
but the direct support is thin: **1 related clinical trial** (which does not test tamoxifen as a treatment for this disease) and **10 publications**, mostly case reports and reviews.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Female breast carcinoma (invasive ductal breast carcinoma, breast ductal adenocarcinoma) |
| Predicted New Indication | Mammary Paget disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tamoxifen is a hormone-blocking (anti-estrogen) therapy whose efficacy in hormone receptor-positive breast cancer is well established, and mechanistically it may be applicable to mammary Paget disease.

Mammary Paget disease is usually associated with underlying ductal carcinoma in situ or invasive breast cancer, which is often hormone receptor-positive. Tamoxifen's estrogen receptor antagonism therefore offers a plausible, indirect link. However, no direct evidence exists for Paget disease as a distinct entity. One case report describes a response in hormone receptor-positive *extramammary* Paget disease, which is a different disease.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002920](https://clinicaltrials.gov/study/NCT00002920) | Phase 3 | Completed | 313 | Medroxyprogesterone vs observation to prevent endometrial disorder in postmenopausal women taking tamoxifen (population includes Paget's disease of the nipple). It does not test tamoxifen as a treatment for Paget disease. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25759627](https://pubmed.ncbi.nlm.nih.gov/25759627/) | 2014 | Meta-analysis | Breast Care | Local recurrence after mastectomy vs breast-conserving surgery for Paget's disease; total recurrence rate reported as 20–40% |
| [34463889](https://pubmed.ncbi.nlm.nih.gov/34463889/) | 2022 | Case report | Investigational New Drugs | Successful tamoxifen treatment of hormone receptor-positive metastatic extramammary Paget disease (a different disease) |
| [14965622](https://pubmed.ncbi.nlm.nih.gov/14965622/) | 2001 | Case report | Breast | Extensive Paget's disease of the nipple; a response was achieved with tamoxifen, with radiotherapy giving a complete response |
| [1648987](https://pubmed.ncbi.nlm.nih.gov/1648987/) | 1991 | Review | Br J Surg | 48 women with Paget's disease of the nipple; mostly treated surgically, tamoxifen used in one case |
| [17319355](https://pubmed.ncbi.nlm.nih.gov/17319355/) | 2006 | Case series | Niger J Clin Pract | Paget's disease of the nipple-areola complex in 8 of 240 breast cancer patients in Benin City |
| [16277886](https://pubmed.ncbi.nlm.nih.gov/16277886/) | 2005 | Case report | Clin Breast Cancer | Paget's disease of the nipple as local recurrence after breast-conservation treatment |
| [8955252](https://pubmed.ncbi.nlm.nih.gov/8955252/) | 1996 | Case report | Am Surg | Paget's disease of the male breast; review of 32 reported cases |

## India Market Information

The data compiled for this report list 20 valid single-ingredient oral tablet registrations (strips of 10 tablets, 10 mg and 20 mg strengths). Approved indication text is not available for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 46661 | Canogen 20mg Tablet | Strip of 10 tablets | Not stated |
| 214870 | Tamodex 20mg Tablet | Strip of 10 tablets | Not stated |
| 166053 | Oncotam 20mg Tablet | Strip of 10 tablets | Not stated |
| 42515 | Camofen 20mg Tablet | Strip of 10 tablets | Not stated |
| 163786 | Oncomox 10mg Tablet | Strip of 10 tablets | Not stated |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal (endocrine) therapy, a selective estrogen receptor modulator; not a conventional cytotoxic agent |
| Myelosuppression Risk | Low; the knowledge graph lists thrombocytopenia and leukopenia as contraindication-related conditions, so blood counts should be monitored |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC, liver function, calcium, and endometrial and thromboembolic risk assessment |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: thrombocytopenia, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, stroke and cerebrovascular disorder, cerebral infarction, pulmonary embolism, leukopenia, vision disorder, blindness.
- **Drug Interactions**: 546 interactions are recorded. Major-level examples include bupropion, lorcaserin, cimetidine, dolasetron, eliglustat, cisapride, dexfenfluramine and fenfluramine. Moderate-level examples include famotidine, loperamide, aprepitant, dexamethasone, clarithromycin, granisetron and levofloxacin.

Package insert warnings and contraindications were not available for this report; please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no study tests tamoxifen directly in mammary Paget disease. Support is limited to an indirect hormone receptor link, case reports and a trial that does not test tamoxifen as treatment, so the evidence level is L4.

**To proceed, the following is needed:**
- Hormone receptor status data in mammary Paget disease and its underlying breast cancer
- Prospective or retrospective clinical data on tamoxifen use in this disease
- Package insert warnings and contraindications for the India-registered products
- Detailed mechanism of action data

**Other predictions in this analysis (for context):**
- **Breast carcinoma in situ** (L1, Proceed with Guardrails): supported by Phase 3 randomized evidence, including low-dose tamoxifen in the TAM-01 trial (NCT01357772; PMIDs 36917758, 30973790). It is close to the original breast cancer use and is not a novel repurposing finding. Guardrails: restrict to hormone receptor-positive disease, weigh thromboembolic and endometrial risks, and consider low-dose regimens.
- **Estrogen-receptor positive breast cancer** (L1, Proceed with Guardrails): this is the established approved use, not a repurposing opportunity.
- **Hormone-resistant breast carcinoma** (L2, Research Question): only small, partly terminated Phase 2 combination studies; monotherapy efficacy is unsupported.
- **Invasive tubular breast carcinoma** (L4, Research Question): plausible mechanism but no direct tamoxifen evidence.
- **Basal-like breast carcinoma, Ehrlich tumor carcinoma, intraductal cribriform breast adenocarcinoma, sebaceous breast carcinoma, botryoid-type embryonal rhabdomyosarcoma of the vagina**: Hold. Evidence is preclinical or absent, and the rhabdomyosarcoma prediction is likely a false positive.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

