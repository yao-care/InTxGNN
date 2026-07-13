---
layout: default
title: Dactinomycin
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 9
---

# Dactinomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Dactinomycin: From Pediatric Solid Tumors to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Dactinomycin (Actinomycin D) is a cytotoxic intercalating antibiotic established in pediatric oncology, used as a cornerstone agent in standard regimens for rhabdomyosarcoma, Wilms' tumor, and gestational trophoblastic neoplasia.
The TxGNN model predicts it may be effective for **Relapsing-Remitting Multiple Sclerosis (RRMS)**,
with **0 clinical trials** and **0 publications** currently supporting this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pediatric solid tumors (rhabdomyosarcoma, Wilms' tumor, gestational trophoblastic neoplasia) |
| Predicted New Indication | Relapsing-Remitting Multiple Sclerosis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on established pharmacological knowledge, Dactinomycin (Actinomycin D) is a DNA-intercalating antibiotic that inserts between guanine-cytosine base pairs and physically blocks RNA polymerase, halting RNA transcription. This mechanism confers potent, non-selective cytotoxic activity against all rapidly proliferating cells, forming the pharmacological basis for its long-standing use in pediatric oncology — particularly in the VAC combination regimen (vincristine + actinomycin D + cyclophosphamide).

Relapsing-Remitting Multiple Sclerosis is an autoimmune demyelinating disease driven by autoreactive T- and B-lymphocytes that attack the myelin sheath of the central nervous system. Theoretically, a cytotoxic agent like Dactinomycin could suppress this autoimmune cascade through non-selective lymphocyte depletion. This indirect mechanistic pathway likely explains the TxGNN model's prediction — shared immune-related nodes in the knowledge graph may create an apparent connection between Dactinomycin and RRMS.

However, the clinical rationale is weak. Established RRMS disease-modifying therapies (natalizumab, fingolimod, ocrelizumab, cladribine) achieve targeted immunomodulation with substantially more favorable and predictable safety profiles. Dactinomycin's severe toxicity burden — dose-limiting myelosuppression, hepatotoxicity, mucositis, and known carcinogenicity — would be clinically disproportionate for a chronic, non-malignant condition. The high TxGNN score most likely reflects indirect knowledge graph connectivity rather than true biological plausibility for RRMS.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Dactinomycin is currently **not registered in India**. No marketing authorizations are on record (0 licenses).

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Intercalating antibiotic — Actinomycin class) |
| Myelosuppression Risk | High — bone marrow suppression is a dose-limiting toxicity; neutropenia, thrombocytopenia, and anemia are expected and common adverse effects |
| Emetogenicity Classification | Moderate to high |
| Monitoring Items | Complete blood count with differential (CBC/diff), liver function tests (AST, ALT, bilirubin), renal function, signs of oral mucositis and veno-occlusive disease (particularly in young children) |
| Handling Protection | Must follow cytotoxic / hazardous drug handling regulations: dedicated preparation area, appropriate PPE (gloves, gown, eye protection) during compounding and administration |

---

## Safety Considerations

**Drug Interactions** (164 total interactions identified; key interactions below):

| Severity | Interacting Drug | Notes |
|----------|-----------------|-------|
| Major | Deferiprone | Additive risk of agranulocytosis and severe neutropenia; concurrent use should be avoided |
| Major | Samarium (153Sm) lexidronam | Additive myelosuppression; bone marrow recovery must be confirmed before combining |
| Moderate | Mercaptopurine | Additive hematologic toxicity; dose adjustment and close CBC monitoring required |
| Moderate | Palifermin | Palifermin should not be administered within 24 hours before or after cytotoxic chemotherapy (increased mucosal toxicity risk) |
| Moderate | Strontium chloride Sr-89 | Additive bone marrow suppression; hematologic parameters must be adequate before use |
| Moderate | Fostamatinib | Increased risk of hematologic adverse events |
| Moderate | Roflumilast | Potential additive immunosuppressive effect |
| Moderate | Chloramphenicol | Additive myelosuppressive potential |
| Minor | Levofloxacin | Minor interaction; monitor for overlapping adverse effects |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or published literature evidence supporting Dactinomycin in relapsing-remitting multiple sclerosis. The mechanistic link is speculative and relies on indirect knowledge graph connectivity; furthermore, the drug's severe cytotoxicity profile creates a clearly unfavorable risk-benefit ratio compared to all currently approved RRMS disease-modifying therapies.

**To proceed, the following is needed:**
- Preclinical studies (in vitro autoimmune models or EAE mouse model) specifically evaluating Dactinomycin's immunomodulatory effects in a demyelinating disease context
- Verified mechanism of action data (DrugBank API or primary pharmacology literature) to confirm whether low-dose immunosuppression is mechanistically plausible without unacceptable toxicity
- A comparative risk-benefit analysis against current standard-of-care RRMS therapies to establish whether any therapeutic window exists
- Toxicogenomic or dose-finding data exploring sub-cytotoxic immunosuppressive dosing regimens

> **Multi-indication note:** This report covers the top-ranked TxGNN prediction (Rank 1: RRMS, L5, Hold). This evidence pack contains 9 predicted indications in total. Significantly stronger clinical evidence exists for Dactinomycin in **rhabdomyosarcoma subtypes** (Rank 5: parameningeal embryonal RMS — L2, *Proceed with Guardrails*, supported by Phase 3 RCT data) and **liver sarcoma** (Rank 7 — L3, *Proceed with Guardrails*, with 1 Phase 3 trial and 20 publications). Separate focused reports for these higher-evidence indications are recommended.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

