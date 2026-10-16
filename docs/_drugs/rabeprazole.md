---
layout: default
title: Rabeprazole
parent: Model Prediction Only (L5)
nav_order: 718
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Rabeprazole: predicted new indication Smouldering systemic mastocytosis (evidence level L5). Approved use: Peptic ulcer disease, gastroesophageal reflux disease, duodenal ulcer…"
monitor_inn: "Rabeprazole"
predicted_indications: ["Smouldering systemic mastocytosis", "lymphoadenopathic mastocytosis with eosinophilia"]
---

# Rabeprazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Rabeprazole: From Peptic Ulcer and Acid-Related Disease to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Rabeprazole is a proton pump inhibitor originally used for acid-related conditions such as peptic ulcer disease, gastroesophageal reflux disease and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be useful for **Smouldering systemic mastocytosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastroesophageal reflux disease, duodenal ulcer, Zollinger-Ellison syndrome (the India licence records contain no approved indication text) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rabeprazole is a proton pump inhibitor (a class that suppresses gastric acid secretion). Its efficacy in acid-related disease is established, and the knowledge graph already links it to systemic mastocytosis and mastocytosis.

The link to the predicted indication is indirect. In mastocytosis, mast cells release excess histamine, which can drive gastric acid hypersecretion. Acid suppression can control these complications, but this is symptom control, not treatment of the underlying disease. The high score most likely reflects the close network proximity between smouldering systemic mastocytosis and the mastocytosis indications already listed for the drug.

There is no evidence that rabeprazole reduces mast cell burden, affects KIT-driven proliferation, or slows progression in smouldering disease.

The second-ranked prediction, **lymphoadenopathic mastocytosis with eosinophilia** (score 99.35%), follows the same reasoning. It is a subtype extension of the existing mastocytosis indications, not a new mechanism. There is no evidence that rabeprazole affects eosinophilia, lymphadenopathy or the underlying neoplastic process. It also has no trials or literature (evidence level L5, Hold).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

There are 20 valid single-ingredient registrations and no cancelled ones. The compiled records contain no approved indication text. The main authorizations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 191472 | Rowet 20mg Tablet | Strip of 10 tablets | Not available |
| 198837 | Rastik-IT Capsule SR | Strip of 10 sustained-release capsules | Not available |
| 199186 | Rabicred IV 20mg Injection | Vial of 1 injection | Not available |
| 184495 | Rabeloc 20 Tablet | Strip of 10 tablets | Not available |
| 184873 | Rablet 10 Tablet | Strip of 15 tablets | Not available |

Available forms include oral tablets, sustained-release capsules and tablets, and injectables.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease relationships, not label text): liver disease, gallbladder disease, osteoporosis, postmenopausal osteoporosis, bone fracture.
- **Drug Interactions**: 486 interactions were identified. Examples of **Major** interactions include **acalabrutinib** and **atazanavir**. Examples of **Moderate** interactions include amikacin, amphotericin B formulations, amphetamine, aprepitant, armodafinil, apalutamide and bosutinib. Minor interactions include acetylsalicylic acid and axitinib.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score, with no clinical trials or literature (L5). Any plausible benefit is symptomatic control of acid hypersecretion, which the existing mastocytosis indications already cover. It is not a new disease-modifying effect.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from India Pharma, a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Clinical or observational evidence on rabeprazole use in smouldering systemic mastocytosis, including any effect on mast cell burden or disease progression
- Clarification of whether the prediction adds value beyond the existing mastocytosis indications
- Route compatibility and similarity-to-original assessments, both still pending
- A review of the long-term bone and liver safety signals, given the knowledge-graph contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

