---
layout: default
title: Mitomycin
parent: 僅模型預測 (L5)
nav_order: 453
evidence_level: L5
indication_count: 10
---

# Mitomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Mitomycin: From Solid Tumor Chemotherapy to Solid Pseudopapillary Carcinoma of Pancreas

## One-Sentence Summary

Mitomycin is a classic cytotoxic antibiotic historically used as a core component in combination chemotherapy regimens for solid tumors, including gastric and exocrine pancreatic cancers (e.g., SMF, FAM protocols).
The TxGNN model predicts it may be effective for **Solid Pseudopapillary Carcinoma of Pancreas**,
with **0 clinical trials** and **0 publications** currently supporting this specific direction.
The overall evidence base is minimal, and caution is warranted before further investment in this indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in regulatory data; Mitomycin is historically used in combination chemotherapy for gastric cancer, exocrine pancreatic cancer, and other solid tumors |
| Predicted New Indication | Solid Pseudopapillary Carcinoma of Pancreas |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Mitomycin (Mitomycin C) is a cytotoxic antibiotic that acts as a bifunctional alkylating agent, forming DNA interstrand and intrastrand cross-links. This covalent DNA modification inhibits DNA replication and transcription, selectively targeting rapidly proliferating cells — a property that forms the theoretical basis for its use in oncology.

Solid Pseudopapillary Carcinoma of the Pancreas (SPC) is a rare low-grade malignant tumor, predominantly affecting young women. Because it is low-grade with a relatively favorable prognosis, the primary treatment is surgical resection rather than systemic chemotherapy. SPC's biological behavior — slow growth and low mitotic activity — is mechanistically misaligned with agents like Mitomycin, which exert greatest effect against high-proliferation tumors. There is no published evidence specific to Mitomycin in SPC.

The TxGNN graph model prediction may reflect Mitomycin's historical association with pancreatic tumor subtypes broadly, rather than any specific mechanistic rationale for SPC. The prediction score of 99.86% reflects the model's confidence in a biological relationship at the knowledge-graph level, not the strength of clinical evidence. In the absence of supporting clinical data, and given that SPC is managed primarily by surgery, this prediction is considered hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Mitomycin in solid pseudopapillary carcinoma of pancreas.

---

## Literature Evidence

Currently no related literature available for Mitomycin in solid pseudopapillary carcinoma of pancreas.

---

## India Market Information

Mitomycin is currently **not marketed in India** and has **0 registered product authorizations** on record. No license data is available to display.

---

## Cytotoxicity

Mitomycin is a conventional cytotoxic antineoplastic antibiotic. The following safety profile applies based on established pharmacological class knowledge:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Antineoplastic antibiotic (alkylating-type mechanism via DNA cross-linking) |
| Myelosuppression Risk | High — Cumulative, delayed myelosuppression is a hallmark toxicity; thrombocytopenia and neutropenia typically nadir at 4–6 weeks; Hemolytic Uremic Syndrome (HUS) is a rare but serious complication with cumulative dosing |
| Emetogenicity Classification | Low to Moderate (IV bolus); prophylactic antiemetics are generally recommended |
| Monitoring Items | Complete Blood Count (CBC) with differential and platelets (monitor for delayed nadir), serum creatinine and urinalysis (HUS surveillance), pulmonary function tests (interstitial pneumonitis risk with prolonged use) |
| Handling Protection | Must follow cytotoxic drug handling regulations — preparation in a biological safety cabinet, PPE (gloves, gown, mask), and compliance with cytotoxic waste disposal protocols required |

---

## Safety Considerations

**Drug Interactions (193 interactions on record; key interactions listed below):**

| Interacting Drug | Severity | Notes |
|-----------------|----------|-------|
| Deferiprone | Major | Concurrent use with myelosuppressive agents significantly increases risk of agranulocytosis |
| Samarium (153Sm) lexidronam | Major | Additive myelosuppression risk with radiopharmaceuticals |
| Palifermin | Moderate | Palifermin should not be administered within 24 hours of cytotoxic chemotherapy |
| Strontium chloride Sr-89 | Moderate | Additive bone marrow suppression risk |
| Fostamatinib | Moderate | Potential pharmacodynamic interaction; monitor blood counts |
| Levofloxacin | Minor | Monitor for QT prolongation and other additive effects |

> Note: The full interaction list contains 193 entries. Package insert and clinical pharmacist review are essential before co-administration with any agent.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score for Mitomycin in solid pseudopapillary carcinoma of the pancreas, but this indication has zero supporting clinical trials and zero published literature. SPC is a low-grade tumor managed primarily by surgery, making systemic cytotoxic chemotherapy of limited relevance, and Mitomycin's mechanism is better suited to high-proliferation malignancies.

**To proceed, the following is needed:**

- **MOA data**: Retrieve complete mechanism of action from DrugBank (DB00305) to enable formal mechanistic linkage analysis
- **Safety data gap**: Obtain the full prescribing information / package insert (TFDA or FDA/EMA) to populate key warnings and contraindications — currently blocking safety review (DG001, Severity: Blocking)
- **Indication re-evaluation**: Consider pivoting analysis to Rank 8 indication (*malignant exocrine pancreas neoplasm*, Evidence Level L4) where Mitomycin has historical use in SMF/FAM regimens and limited literature support — this represents a more scientifically grounded repurposing hypothesis
- **India registration pathway**: If pursuing any pancreatic indication, regulatory pathway for new drug application in India (CDSCO) must be established; Mitomycin currently has no registered products in India
- **Preclinical data review**: Systematic review of SPC molecular biology (CTNNB1 mutations, Wnt pathway) to assess whether DNA cross-linking agents have any rational mechanistic basis in this specific tumor type

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

