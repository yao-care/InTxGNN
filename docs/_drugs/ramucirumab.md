---
layout: default
title: Ramucirumab
parent: Model Prediction Only (L5)
nav_order: 724
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "Ramucirumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "cervical adenosquamous carcinoma, glassy cell variant", "uterine ligament endometrioid adenocarcinoma", "uterine ligament clear cell adenocarcinoma", "uterine ligament mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
description: "Ramucirumab: predicted new indication Uterine ligament adenocarcinoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Ramucirumab
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

## Ramucirumab: Uterine ligament adenocarcinoma
{: .text-alpha }

## One-Sentence Summary

Ramucirumab is an injectable antibody originally used for cancers including non-small cell lung carcinoma, gastric adenocarcinoma and hepatocellular carcinoma.
The TxGNN model predicts it may be effective for **uterine ligament adenocarcinoma**,
but **no clinical trials and no publications** were found for this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Uterine ligament adenocarcinoma |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ramucirumab is known to be a VEGFR2 antagonist, and its efficacy in gastric, lung and liver cancers is established. Mechanistically, blocking VEGFR2 may be applicable to adenocarcinomas that depend on angiogenesis.

The predicted indication is an adenocarcinoma, a histology shared with gastric adenocarcinoma and lung adenocarcinoma among the original indications. The link is therefore inferred from the similarity of disease types, not from direct evidence in this tumour. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

**Other predicted indications** (all L5, all Hold, none with trials or literature):

| Rank | Predicted Indication | Score |
|---|---|---|
| 2 | Endocervical carcinoma | 0.9995 |
| 3 | Adenoid cystic carcinoma of the cervix uteri | 0.9995 |
| 4 | Uterine ligament serous adenocarcinoma | 0.9994 |
| 5 | Signet ring cell variant cervical mucinous adenocarcinoma | 0.9994 |
| 6 | Cervical adenosquamous carcinoma, glassy cell variant | 0.9994 |
| 7 | Uterine ligament endometrioid adenocarcinoma | 0.9994 |
| 8 | Uterine ligament clear cell adenocarcinoma | 0.9994 |
| 9 | Uterine ligament mucinous adenocarcinoma | 0.9994 |
| 10 | Intestinal variant cervical mucinous adenocarcinoma | 0.9994 |

Most predictions are gynaecological adenocarcinomas. Among them, endocervical carcinoma has the most biological plausibility, because VEGF-driven angiogenesis matters in cervical cancer and another anti-VEGF agent, bevacizumab, has an established role there.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 39275 | Cyramza 100mg Injection | Vial of 10 ml injection | Not stated in the records |
| 35995 | Cyramza 500mg Injection | Vial of 50 ml injection | Not stated in the records |

Both licenses are valid single-ingredient products from Eli Lilly and Company India Pvt Ltd.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-VEGFR2 monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 127 interactions were recorded. The ones listed here are Major and mostly involve agents that affect bleeding or clotting, so bleeding risk deserves attention:
  - Antiplatelet agents: acetylsalicylic acid, clopidogrel, cilostazol, abciximab, cangrelor
  - Anticoagulants and thrombolytics: apixaban, betrixaban, bivalirudin, dalteparin, alteplase, antithrombin III human, defibrotide, caplacizumab
  - Others: deferasirox, ibritumomab tiuxetan, tositumomab (including I-131)
  - Moderate-level interactions include dexfenfluramine, fenfluramine and sibutramine.

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions rest on model scores alone (L5), with no clinical trials or publications. The rationale is plausible but inferred from related diseases. The Indian package insert has also not been obtained, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Download and review the Indian package insert (warnings, contraindications and approved indications)
- Detailed mechanism of action data (for example from DrugBank)
- A literature and trial search for ramucirumab in cervical and uterine adenocarcinomas, starting with endocervical carcinoma
- Assessment of whether these rare histologies have enough patients to support a trial
- A bleeding-risk and interaction review for the intended patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

