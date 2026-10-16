---
layout: default
title: Crizotinib
parent: Model Prediction Only (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Crizotinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung carcinoma / lung cancer"
monitor_inn: "Crizotinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung hilum carcinoma", "lung benign neoplasm", "lung germ cell tumor", "pulmonary sulcus neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Crizotinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Crizotinib: From Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Crizotinib is a targeted kinase inhibitor (ALK, ROS1 and MET) originally used to treat non-small cell lung cancer.
The TxGNN model predicts it may be effective for **gingival fibromatosis** (top-ranked prediction), but **no clinical trials and no publications** support this prediction.
It is a computational signal only and should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung carcinoma / lung cancer (from the knowledge graph; approved indication text is not available in the India licence records) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From the literature, crizotinib is known to be an ATP-competitive inhibitor of the receptor tyrosine kinases ALK, ROS1 and MET. Its efficacy in ALK- or ROS1-positive non-small cell lung cancer is well established.

For gingival fibromatosis, no pathway connecting these targets to the disease has been shown. The high TxGNN score (99.81%) reflects a pattern in the knowledge graph rather than demonstrated biology, and it should not be read as evidence of efficacy.

Other high-ranking predictions give context:
- **Closest to the original indication:** lung hilum carcinoma (score 99.73%) is largely a subset of already-approved NSCLC use, supported by two case reports (ROS1-positive neoadjuvant therapy; 68-month PFS in ALK-positive disease). It is not a true repurposing.
- **Lung germ cell tumor (99.73%)**: two basket or tumor-agnostic trials exist, but nothing shows that a germ cell tumor patient was treated.
- **Lung benign neoplasm (99.73%)**: the many Phase 3 NSCLC trials concern a malignant, already-approved indication and do not transfer to benign tumors.

## Clinical Trial Evidence

Currently no related clinical trials registered for gingival fibromatosis.

## Literature Evidence

Currently no related literature available for gingival fibromatosis.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 48989 | Crizalk 250mg Capsule (Pfizer Ltd) | Capsule (box of 60) | Not listed in licence record |
| 48988 | Crizalk 200mg Capsule (Pfizer Ltd) | Capsule (box of 60) | Not listed in licence record |

Both registrations are valid single-agent oral products.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK/ROS1/MET tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function (case reports describe fatal fulminant liver failure), ECG and heart rate (case reports describe bradycardia, QT prolongation and other cardiac toxicity), CBC |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 566 interactions were recorded. Major-level interactions include clarithromycin, cisapride, dolasetron, eliglustat and granisetron. Moderate-level examples include famotidine, metformin, loperamide, bupropion, aprepitant, dexamethasone and budesonide.
- **Case-report safety signals** (not label text): fatal fulminant liver failure, multiple cardiac toxicities (bradycardia, QT prolongation, ventricular arrhythmia, pericarditis), sick sinus syndrome, erythema multiforme and erosive esophagitis.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials, no literature and no plausible mechanistic link to gingival fibromatosis. Known hepatic and cardiac risks make it hard to justify further work without a stronger biological rationale.

**To proceed, the following is needed:**
- Mechanism-of-action data and a biological rationale linking ALK, ROS1 or MET signaling to gingival fibromatosis
- Preclinical data (for example, fibroblast models from affected tissue)
- Package insert warnings and contraindications from the India licence holder, which are currently missing
- A risk-benefit assessment for a non-malignant, non-life-threatening condition, given the hepatotoxicity and cardiotoxicity reports
- If lung-related indications are of interest, prioritize lung hilum carcinoma (ALK/ROS1-positive), which falls under the existing NSCLC indication, over the other predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

