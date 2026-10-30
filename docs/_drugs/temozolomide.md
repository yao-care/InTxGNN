---
layout: default
title: Temozolomide
parent: Model Prediction Only (L5)
nav_order: 813
evidence_level: L5
indication_count: 1
monitor_inn: "Temozolomide"
predicted_indications: ["cauda equina neoplasm"]
last_modified_at: 2026-10-30
description: "Temozolomide: predicted new indication Cauda equina neoplasm (evidence level L5). Approved use: Anaplastic astrocytoma, astrocytoma (excluding glioblastoma)…"
---

# Temozolomide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Temozolomide: From Glioma to Cauda Equina Neoplasm
{: .text-alpha }

## One-Sentence Summary

Temozolomide is an oral alkylating chemotherapy drug. The knowledge graph records it for anaplastic astrocytoma, astrocytoma (excluding glioblastoma) and brain glioblastoma.
The TxGNN model predicts it may be effective for **cauda equina neoplasm**, but the evidence is thin: **no registered clinical trials** and only **3 case reports**, of which just one concerns a tumour of this type (a spinal myxopapillary ependymoma).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaplastic astrocytoma, astrocytoma (excluding glioblastoma), brain glioblastoma (relations recorded in the knowledge graph; the licence records compiled for this report contain no indication text) |
| Predicted New Indication | Cauda equina neoplasm |
| TxGNN Prediction Score | 0.9930 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | At least 20 (single-ingredient licences; the list may be partial) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Temozolomide is an oral DNA alkylating agent. It methylates guanine (O6 and N7 positions) and adenine (N3 position), and it crosses the blood-brain barrier, so it is active in tumours of the central nervous system. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description comes from general knowledge of temozolomide pharmacology.

Cauda equina neoplasms are mostly myxopapillary ependymomas, which are glial-derived tumours of the filum terminale and conus region. Because gliomas and these tumours share a glial origin, a plausible biological link exists. Activity is likely to depend on MGMT promoter methylation status, which is not reported in the available evidence.

The high TxGNN score (0.993) is a computational prediction only and is not clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29270703](https://pubmed.ncbi.nlm.nih.gov/29270703/) | 2018 | Case report | Eur Spine J | Remarkable response to temozolomide in a recurrent spinal myxopapillary ependymoma with cerebrospinal dissemination |
| [42760727](https://pubmed.ncbi.nlm.nih.gov/42760727/) | 2026 | Case report | Medicine | Nasal NUT carcinoma managed with multimodal treatment including radiotherapy; not a cauda equina tumour |
| [18706663](https://pubmed.ncbi.nlm.nih.gov/18706663/) | 2009 | Case report | Neuro-Chirurgie | Cryptococcal infection in a child treated for pontine glioma; not a study of cauda equina neoplasm |

Only the first report relates to a tumour of this type, and it is a single case. It is a related condition (spinal myxopapillary ependymoma) rather than a study of cauda equina neoplasm as a defined disease. No cited study directly addresses the predicted disease, so the evidence level is capped at L5.

---

## India Market Information

At least 20 single-ingredient licences are recorded (the list may be partial). The licence records compiled for this report contain no approved-indication text. Five main authorisations are listed:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 228645 | Temoblast 250mg Capsule | Strip of 5 capsules | Not stated in records |
| 220212 | Temotide 100mg Tablet | Strip of 5 tablets | Not stated in records |
| 223951 | Temo GBM 250mg Capsule | Bottle of 5 capsules | Not stated in records |
| 225370 | Temokem 100mg Injection | Packet of 5 injections | Not stated in records |
| 96306 | Gliotem 250mg Capsule | Strip of 1 capsule | Not stated in records |

Products are available as oral capsules and tablets, and as an injection.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | High. The knowledge graph records contraindication relations with neutropenia, thrombocytopenia, pancytopenia, lymphopenia, anaemia and aplastic anaemia |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindication relations recorded in the knowledge graph** (not label text): liver failure, thrombocytopenia, neutropenia, agranulocytosis, anaemia, macrocytic anaemia, pneumocystosis, pancytopenia, lymphopenia, myelodysplastic syndrome, idiopathic aplastic anaemia, aplastic anaemia.
- **Drug Interactions**: 320 interactions are recorded in total. The only graded ones in the list reviewed are Naltrexone (Moderate) and Levofloxacin (Minor). Others, such as Metformin, Omeprazole, Prednisone and Morphine, have no graded severity.

Please refer to the package insert for warnings and labelled contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible, since the tumour is glial-derived and temozolomide penetrates the CNS. However, the only supporting clinical evidence is a single case report in a related condition, with no registered trials. The label-based safety information is also missing.

**To proceed, the following is needed:**
- Clinical studies directly addressing cauda equina neoplasm, such as case series or prospective trials in myxopapillary ependymoma
- MGMT promoter methylation data for these tumours
- Package insert warnings, contraindications and approved indication text for the Indian licences
- Detailed mechanism-of-action data
- A myelosuppression monitoring plan for this patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

