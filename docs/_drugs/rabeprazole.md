---
layout: default
title: Rabeprazole
parent: 僅模型預測 (L5)
nav_order: 711
evidence_level: L5
indication_count: 2
---

# Rabeprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Rabeprazole: From Acid-Related Disorders to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Rabeprazole is a proton pump inhibitor (PPI) whose original indication data is not available in the current India regulatory dataset (the drug is currently unmarketed there), but its known drug class is typically used for GERD/peptic ulcer disease.
The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model prediction with no direct experimental or clinical validation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no India license records; Rabeprazole's drug class — PPI — is generally indicated for GERD/peptic ulcer disease) |
| Predicted New Indication | Smouldering Systemic Mastocytosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| India Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not directly available for this drug (flagged as a data gap, DG002). Based on known information, Rabeprazole is a proton pump inhibitor (PPI) that inhibits the H⁺/K⁺-ATPase in gastric parietal cells — a well-established pharmacological mechanism used to suppress gastric acid secretion.

There is no known direct mechanistic connection between this pathway and the pathology of mastocytosis, which is typically driven by KIT-mutation-related clonal mast cell proliferation (e.g., KIT D816V). The TxGNN model's very high score (99.44%) likely reflects an indirect statistical association in the knowledge graph — for example, shared nodes around gastric acid/histamine metabolism (H2 receptors, enterochromaffin-like cells) — rather than a validated pharmacological rationale.

A second candidate indication, *lymphoadenopathic mastocytosis with eosinophilia* (score 99.35%), shows the same pattern: a rare mastocytosis subtype with no clinical trial or literature support, and no established mechanistic link to PPI activity. Both predictions should be treated as hypothesis-generating only, not as evidence of therapeutic plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Rabeprazole currently has **0 registrations** in the India regulatory dataset and is marked as **Not Marketed**. No product authorization records are available for this evidence pack.

---

## Safety Considerations

- **Drug Interactions**: 486 total interactions on record. Notable **Major**-level interactions include **Acalabrutinib** and **Atazanavir** (source: DDInter). Multiple **Moderate**-level interactions are also documented, including amphotericin B (and formulations), aminoglycosides (amikacin), thiazide diuretics (bendroflumethiazide, benzthiazide), and several kinase inhibitors (apalutamide, armodafinil, bosutinib). A full interaction screen against any co-administered therapy is recommended.

(Key warnings and contraindications are not available in this evidence pack — please refer to the package insert for that information.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level is L5 — both candidate indications are supported only by the TxGNN model score, with zero clinical trials or publications identified. Critically, TFDA-equivalent label data (warnings/contraindications) is flagged as a **Blocking** data gap (DG001), which by itself prevents this candidate from entering the S1 safety review stage.

**To proceed, the following is needed:**
- Official label data (warnings, contraindications) — currently Blocking gap (DG001)
- Confirmed mechanism of action detail from DrugBank — currently High-priority gap (DG002)
- Preclinical/mechanistic studies exploring any link between PPI pharmacology and KIT-driven mast cell proliferation
- Full DDI review given the high interaction count (486), particularly the Major-level interactions, before any further evaluation in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

