---
layout: default
title: Pirfenidone
parent: Model Prediction Only (L5)
nav_order: 678
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Pirfenidone"
predicted_indications: ["extracutaneous mastocytoma", "dermatofibrosarcoma protuberans", "aggressive systemic mastocytosis", "heart fibrosarcoma", "conventional fibrosarcoma", "autosomal recessive familial Mediterranean fever", "kidney fibrosarcoma", "hepatic infarction", "fibroblastic neoplasm", "low grade fibromyxoid sarcoma"]
description: "Pirfenidone: predicted new indication Extracutaneous mastocytoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Pirfenidone
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

## Pirfenidone: Extracutaneous mastocytoma
{: .text-alpha }

## One-Sentence Summary

Pirfenidone is an oral anti-fibrotic drug originally used to treat idiopathic pulmonary fibrosis and related interstitial pneumonias.
The TxGNN model predicts it may be effective for **extracutaneous mastocytoma**,
but **no clinical trials and no publications** currently support this prediction, so it remains a computational hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Extracutaneous mastocytoma |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, pirfenidone is an anti-fibrotic agent with an established role in idiopathic pulmonary fibrosis. Its anti-fibrotic and anti-inflammatory activity is generally linked to modulation of the TGF-beta pathway.

A plausible but unverified connection to extracutaneous mastocytoma is this TGF-beta and anti-inflammatory activity. However, mastocytoma is driven mainly by KIT signaling, and the data compiled for this report contain no study showing that pirfenidone acts on this pathway or on mast cell tumours. The high score is therefore best read as a network-based computational signal, not as proof of efficacy.

Other top-ranked predictions show a similar pattern. They include dermatofibrosarcoma protuberans, aggressive systemic mastocytosis, several fibrosarcomas, familial Mediterranean fever, hepatic infarction, fibroblastic neoplasm and low grade fibromyxoid sarcoma. Only fibroblastic neoplasm (rank 9) has any supporting literature, and that is indirect, preclinical, or case-level.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for extracutaneous mastocytoma.

---

## Literature Evidence

Currently no related literature available for extracutaneous mastocytoma.

For context, the only predicted indication in the data with any literature is rank 9, fibroblastic neoplasm (L4, preclinical level). This evidence is indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12907346](https://pubmed.ncbi.nlm.nih.gov/12907346/) | 2003 | Pilot clinical study | Am J Gastroenterol | Pilot project on pirfenidone for desmoid tumours in familial adenomatous polyposis; design details not confirmed from the available text |
| [27835939](https://pubmed.ncbi.nlm.nih.gov/27835939/) | 2016 | In vitro | BMC Musculoskelet Disord | Pirfenidone inhibited TGF-β1-mediated fibrotic activity in Dupuytren's disease-derived fibroblasts |
| [30927912](https://pubmed.ncbi.nlm.nih.gov/30927912/) | 2019 | In vitro | BMC Musculoskelet Disord | Studied pirfenidone effects on TGF-β1-stimulated non-SMAD signalling in Dupuytren's fibroblasts |
| [35129055](https://pubmed.ncbi.nlm.nih.gov/35129055/) | 2022 | Preclinical | Pharm Dev Technol | Explored pirfenidone as a locally injectable anti-fibrotic for Dupuytren's disease |
| [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/) | 2018 | Case report | Perm J | Undifferentiated pleomorphic sarcoma reported after pirfenidone use (possible safety signal) |
| [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/) | 2020 | Case report | Rheumatology (Oxford) | Multiple eruptive dermatofibromas aggravated by mycophenolate mofetil and pirfenidone in a patient with systemic sclerosis |

---

## India Market Information

Pirfenidone is marketed in India as single-ingredient oral tablets (20 valid registrations, none cancelled). Approved indication text is not available for these registrations. Five of the main authorizations are shown below:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 173786 | Pirfenex Tablet | Strip of 15 tablets | Cipla Ltd |
| 84944 | Fibrodone 400mg Tablet | Strip of 10 tablets | Lupin Ltd |
| 178901 | Pirfetab 267 Tablet | Strip of 10 tablets | Zydus Cadila |
| 174682 | Pirfact 801 Tablet | Strip of 10 tablets | Sun Pharmaceutical Industries Ltd |
| 175189 | Pulmofib 801mg Tablet | Strip of 10 tablets | MSN Laboratories |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database. The 20 listed in the data are all of Moderate severity. Examples include:
  - Bupropion
  - Omeprazole, esomeprazole and lansoprazole
  - Cimetidine
  - Eliglustat
  - Obeticholic acid
  - Naltrexone
  - Miconazole
  - Disulfiram
  - Ivacaftor
  - Ticlopidine

  Review concomitant medicines carefully before any use.
- **Possible tumour-related signal**: Case reports describe an undifferentiated pleomorphic sarcoma after pirfenidone use and dermatofibromas aggravated by pirfenidone together with mycophenolate. These are isolated reports and do not establish causality, but they warrant evaluation if pirfenidone is considered in neoplastic settings.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (0.9971), with no clinical trials or publications for extracutaneous mastocytoma. Mastocytoma is driven mainly by KIT signalling, and no mechanistic link to pirfenidone is supported by the available data.

**To proceed, the following is needed:**
- Mechanism of action data for pirfenidone
- Package insert warnings and contraindications from the India regulatory source, which are needed for safety screening
- Preclinical evidence (for example mast cell or tumour models) testing pirfenidone against KIT-driven or TGF-beta-related mechanisms
- Review of the sarcoma and dermatofibroma case reports for any safety signal in neoplastic settings
- Comparison against established treatments, such as KIT-targeted therapy
- Approved indication text for the Indian registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

