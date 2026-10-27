---
layout: default
title: Ruxolitinib
parent: Model Prediction Only (L5)
nav_order: 758
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ruxolitinib: predicted new indication Uterine corpus perivascular epithelioid cell tumor (PEComa) (evidence level L5). Approved use: Myelofibrosis…"
monitor_inn: "Ruxolitinib"
predicted_indications: ["uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "lymphangioleiomyomatosis", "liposarcoma", "familial rhabdoid tumor", "lung PEComa", "ovarian myxoid liposarcoma", "hemophagocytic syndrome associated with an infection", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease"]
---

# Ruxolitinib
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

## Ruxolitinib: From Myelofibrosis and Polycythemia Vera to Uterine Corpus Perivascular Epithelioid Cell Tumor (PEComa)
{: .text-alpha }

## One-Sentence Summary

Ruxolitinib is an oral JAK1/2 inhibitor originally used for myeloproliferative neoplasms such as myelofibrosis and polycythemia vera.
The TxGNN model predicts it may be effective for **uterine corpus perivascular epithelioid cell tumor (PEComa)**, with a very high score.
However, this is a **model prediction only**: **no clinical trials and no publications** were found for this specific indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myelofibrosis, polycythemia vera and related myeloproliferative neoplasms (from the knowledge graph; the India licence records do not state an indication) |
| Predicted New Indication | Uterine corpus perivascular epithelioid cell tumor (PEComa) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Ruxolitinib is a JAK1/2 inhibitor, and its efficacy in myeloproliferative neoplasms is established. Mechanistically, it may be applicable to tumours in which JAK-STAT signalling plays a role.

For uterine PEComa, the link is speculative. PEComas are generally driven by mTOR/PI3K pathway activation, and possible crosstalk with JAK-STAT signalling is a hypothesis rather than an established finding. The very high TxGNN score probably reflects proximity in the knowledge graph to related diseases, not direct evidence of JAK1/2 biology in this tumour.

The same pattern appears across the related PEComa-family predictions: benign PEComa, lung PEComa, lymphangiomyoma and lymphangioleiomyomatosis. These carry similarly high scores but no supporting studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| Registration No. 114043 | Jakavi 15mg Tablet (Novartis India Ltd) | Strip of 14 tablets |
| Registration No. 113919 | Jakavi 5mg Tablet (Novartis India Ltd) | Strip of 14 tablets |
| Registration No. 114073 | Jakavi 20mg Tablet (Novartis India Ltd) | Strip of 10 tablets |
| Registration No. 114253 | Jakavi 15mg Tablet (Novartis India Ltd) | Strip of 10 tablets |
| Registration No. 113944 | Jakavi 20mg Tablet (Novartis India Ltd) | Strip of 14 tablets |

All five registrations are valid single-ingredient oral products. The licence records do not include approved indication text.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Medium. Cytopenias such as thrombocytopenia, anaemia and neutropenia are recognised with JAK inhibitors; please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 338 interactions were recorded. The most clinically important are those rated **Major**:
  - Clarithromycin
  - Cobicistat
  - Deferasirox
  - Deferiprone
  - Ibritumomab tiuxetan
  - Tositumomab and Tositumomab (I-131)
  - Samarium (153Sm) lexidronam
- **Moderate** interactions include dexamethasone, rosuvastatin, fenfluramine, dexfenfluramine, sibutramine, troglitazone, palifermin and strontium chloride Sr-89.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for uterine PEComa rests on the model score alone (L5), with no trials, no literature and no established mechanistic rationale. The drug is marketed in India, but not for this indication.

Among the other predicted indications, **hemophagocytic lymphohistiocytosis (HLH)** is the best supported. It has a mechanistic rationale (JAK/STAT-driven cytokine storm), a response-stratified paediatric study, case series and retrospective cohorts, and is rated L3. It is a more promising repurposing candidate to prioritise. Myxoid liposarcoma has only preclinical JAK-STAT data.

**To proceed, the following is needed:**
- Evidence of JAK-STAT dependence in uterine PEComa (preclinical or case-level data)
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications for the India-marketed products
- A decision on whether to re-prioritise the HLH indication, which would require a prospective trial design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

