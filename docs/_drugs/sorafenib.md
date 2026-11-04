---
layout: default
title: Sorafenib
parent: Model Prediction Only (L5)
nav_order: 783
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-04
monitor_inn: "Sorafenib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "female breast carcinoma", "renal pelvis carcinoma", "vulva sarcoma", "dermatofibrosarcoma protuberans"]
description: "Sorafenib: predicted new indication Liposarcoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Sorafenib
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

## Sorafenib: Liposarcoma
{: .text-alpha }

## One-Sentence Summary

Sorafenib is an oral multikinase inhibitor that blocks RAF signaling and the VEGFR and PDGFR receptors involved in tumor growth and blood-vessel formation.
The TxGNN model predicts it may be useful for **liposarcoma**, but no study has tested sorafenib in liposarcoma itself, so the evidence level is **L5**.
The only trial of any relevance is **1 Phase 2 trial** in advanced soft tissue sarcoma in general, and the **literature** consists mainly of reviews and preclinical work.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (7 of 7) – CDSCO approval status is not included in this data |
| Number of Listed Products | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. From what is known about the drug class, sorafenib inhibits the RAF/MEK/ERK pathway and the VEGFR and PDGFR receptors. Angiogenesis and MAPK signaling matter in several soft tissue sarcomas, and laboratory work shows sorafenib can slow growth and MAPK signaling in sarcoma-related cell models, including a dedifferentiated liposarcoma cell line studied alongside nerve sheath tumor cells.

The fit is only partial. Liposarcoma is typically driven by MDM2/CDK4 amplification rather than by the targets of sorafenib, and activity in soft tissue sarcoma appears to depend on tumor histology. The prediction is therefore a hypothesis rather than a supported use.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Single-arm study of sorafenib in advanced soft tissue sarcomas of mixed histology; not specific to liposarcoma and not randomized |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | Phase 2 trial | Cancer | Phase 2 intergroup trial (S0505) of sorafenib in advanced soft tissue sarcomas; mixed histologies, not liposarcoma-specific |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 trial | Ann Surg Oncol | Neoadjuvant radiotherapy plus sorafenib in locally advanced extremity soft tissue sarcoma |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | Treatment of soft tissue sarcomas is increasingly guided by histology; other agents are discussed for liposarcoma |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magy Onkol | Histology-based medical treatment of soft tissue sarcomas |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Mol Cancer Ther | Sorafenib inhibited growth and MAPK signaling in nerve sheath tumor cells and dedifferentiated liposarcoma cell lines |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical | Am J Pathol | Dedifferentiated liposarcoma xenograft models; response to PI3K pathway inhibition (not sorafenib) |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 206423 | Shilfenib 200mg Tablet (Shilpa Medicare) | Bottle of 120 tablets | Not available |
| 203494 | Sorepto 200mg Tablet (Lupin) | Bottle of 30 tablets | Not available |
| 145374 | Mapsonib 200mg Tablet (AMPS Biotech) | Bottle of 30 tablets | Not available |
| 200900 | Sorafenat 200mg Tablet (Natco Pharma) | Bottle of 120 tablets | Not available |
| 152105 | Nexavar 200mg Tablet (Bayer Zydus Pharma) | Bottle of 60 tablets | Not available |

Seven single-ingredient licences are recorded, all valid; the five above are the main ones.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multikinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 509 interactions are recorded. Examples include a major interaction with dolasetron, and moderate interactions with clarithromycin, dexamethasone, levofloxacin, famotidine, loperamide and palonosetron.

Please also refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study has tested sorafenib in liposarcoma. The available trials enroll soft tissue sarcoma in general and the laboratory work involves other tumor cells, so the evidence level is L5. The high model score and partial mechanistic fit are not enough to justify moving forward.

**To proceed, the following is needed:**
- Liposarcoma-specific clinical data, for example subgroup results from the soft tissue sarcoma trials
- Preclinical testing of sorafenib in liposarcoma models, given that its main drivers (MDM2/CDK4) are not sorafenib targets
- Detailed mechanism-of-action data
- Package insert warnings and contraindications from the Indian regulatory sources
- A safety and interaction review for the intended patient population

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

