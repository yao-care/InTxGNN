---
layout: default
title: Bevacizumab
parent: Model Prediction Only (L5)
nav_order: 108
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bevacizumab: predicted new indication Epiglottis neoplasm (evidence level L5). Approved use: Peritoneal cancer, ovarian cancer, breast cancer…"
monitor_inn: "Bevacizumab"
predicted_indications: ["epiglottis neoplasm", "benign neoplasm of tongue", "tumor of testis and paratestis", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "cystic neoplasm", "nasal cavity inverting papilloma", "mesenchymoma", "schwannoma of jugular foramen"]
---

# Bevacizumab
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

# Bevacizumab: From Ovarian and Peritoneal Cancer to Epiglottis Neoplasm

## One-Sentence Summary

Bevacizumab is an anti-VEGF antibody originally used to treat cancers such as ovarian, peritoneal, breast, colorectal and brain tumours.
The TxGNN model predicts it may be effective for **epiglottis neoplasm**, but this top-ranked prediction currently has **no clinical trials** and **no publications** behind it.
It is supported by the model score alone (evidence level L5).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peritoneal cancer, ovarian cancer, breast cancer, metastatic colon cancer, glioblastoma (approved indication text is not available in the India registration records; these are from the knowledge-graph indication list) |
| Predicted New Indication | Epiglottis neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, bevacizumab is a monoclonal antibody that binds VEGF-A and blocks tumour angiogenesis. Its efficacy in ovarian, peritoneal, breast, colorectal and brain tumours is established, and mechanistically it may be applicable to other angiogenesis-dependent tumours, including head and neck tumours.

The epiglottis is part of the head and neck region, where VEGF-driven blood vessel growth is common in tumours. This is the only rationale available for this prediction. No trial or publication specific to epiglottis neoplasm was found, so the link remains speculative.

Other predictions in the top 10 list show a similar pattern. Several are head and neck or rare tumours (tongue, floor of mouth, hypopharynx, nasal cavity, neuroblastoma, schwannoma) supported only by indirect or preclinical evidence. The one exception is "cystic neoplasm" (rank 7), which has Phase 3 ovarian cancer data. That evidence mostly reflects an existing indication rather than true repurposing, and the mapping from "cystic neoplasm" to ovarian cancer is loose.

## Clinical Trial Evidence

Currently no related clinical trials registered for epiglottis neoplasm.

## Literature Evidence

Currently no related literature available for epiglottis neoplasm.

## India Market Information

Showing 5 of 20 valid registrations (all single-ingredient products, none cancelled). Approved indication text is not recorded for these registrations.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 13400 | Avastimab 400mg Injection | Vial of 16 ml injection | RPG Life Sciences Ltd |
| 13987 | Avastimab 100mg Injection | Vial of 4 ml injection | RPG Life Sciences Ltd |
| 110852 | Ivzumab 400 Solution for Injection | Vial of 16 ml solution for injection | RPG Life Sciences Ltd |
| 116540 | Krabeva 100mg Injection | Vial of 4 ml injection | Biocon |
| 233880 | Versavo 400 Solution for Infusion | Vial of 16 ml solution for infusion | Dr Reddy's Laboratories Ltd |

All products are injectable or infusion formulations.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-VEGF monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 22 interactions were recorded in the interaction database. The Major-level interactions are with:
  - Deferiprone
  - Samarium (153Sm) lexidronam
  - Panitumumab
  - Sunitinib
  - Thalidomide
- Moderate-level interactions include:
  - Bisphosphonates (alendronic acid, risedronic acid, etidronic acid, ibandronate, pamidronic acid, tiludronic acid)
  - Growth factors (filgrastim, pegfilgrastim, sargramostim, palifermin)
  - Radiopharmaceuticals (strontium-89, radium-223, sodium phosphate P-32)
  - Idelalisib
  - Romosozumab

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The epiglottis neoplasm prediction rests only on a high model score (99.90%) with no trials or literature. The mechanism is plausible but unsupported by disease-specific evidence.

**To proceed, the following is needed:**
- Disease-specific clinical or preclinical evidence in epiglottis or laryngeal tumours
- Mechanism of action data and a clearer link between the original and new indications
- Package insert warnings and contraindications for the India-marketed products, plus approved indication text
- Route compatibility assessment and a safety review, including the Major interactions listed above
- Consideration of "cystic neoplasm" (rank 7, L1 evidence in ovarian cancer) as a separate question, noting that it largely overlaps with an existing indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

