---
layout: default
title: Pembrolizumab
parent: Model Prediction Only (L5)
nav_order: 654
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pembrolizumab: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung carcinoma, lung cancer, metastatic melanoma"
monitor_inn: "Pembrolizumab"
predicted_indications: ["fibromatosis, gingival", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "fibroma of lung", "lung benign neoplasm", "ovarioleukodystrophy", "pulmonary sulcus neoplasm", "lung germ cell tumor", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Pembrolizumab
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

## Pembrolizumab: From Non-Small Cell Lung Cancer and Metastatic Melanoma to Fibromatosis, Gingival
{: .text-alpha }

## One-Sentence Summary

Pembrolizumab is a PD-1 immune checkpoint inhibitor, originally used to treat non-small cell lung carcinoma, lung cancer and metastatic melanoma.
The TxGNN model predicts it may be effective for **gingival fibromatosis**, but **no clinical trials and no publications** were found for this indication, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung carcinoma, lung cancer, metastatic melanoma (the India licence record has no approved-indication text) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Pembrolizumab is a monoclonal antibody that targets programmed cell death protein 1 (PD-1, encoded by PDCD1). Its efficacy in lung cancer and melanoma is well established, and it has been approved for many other cancers.

Gingival fibromatosis is a benign overgrowth of gum tissue. PD-1 blockade works by reactivating T-cell responses against tumours, and there is no established mechanistic rationale for applying it to a benign fibrous overgrowth. The high TxGNN score (0.994) is a model prediction only. It is not supported by any trial or publication.

The other top-ranked predictions show the same pattern. Most have no evidence, and those with literature (such as lung benign neoplasm) are matched on malignant lung cancer studies that do not apply to the predicted disease. The predictions appear to be driven largely by the original lung cancer indications.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 115727 | Keytruda Injection (MSD Pharmaceuticals Pvt Ltd) | Vial of 4 ml injection | Not specified in the available record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. Literature on pembrolizumab reports immune-related adverse events, including endocrine, thyroid, neurological and myocarditis events, so routine monitoring of endocrine, liver and thyroid function is generally advisable |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

**Drug Interactions** (13 interactions recorded in the interaction databases):
- **Major**: lenalidomide, pomalidomide, thalidomide
- **Moderate**: corticosteroids, namely hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone, methylprednisolone and deflazacort
- Pharmacology data also confirm that the drug's target is PD-1 (CD279).

Package insert warnings and contraindications for the India product were not available. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for gingival fibromatosis is supported only by a model score. There are no trials or publications, and there is no plausible mechanism linking PD-1 blockade to a benign gingival overgrowth. Evidence is graded L5.

**To proceed, the following is needed:**
- Mechanistic or preclinical evidence linking PD-1 signalling to gingival fibromatosis
- Mechanism of action (MOA) data from DrugBank
- Package insert warnings and contraindications for the India product, which are currently missing
- A safety assessment of immune-related adverse events in a benign, non-oncology population
- Reconsideration of other candidates in the ranking (for example, lung hilum carcinoma or pulmonary sulcus neoplasm), which are anatomical or histological subsets of already-approved lung cancer indications and may be better-founded than this prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

