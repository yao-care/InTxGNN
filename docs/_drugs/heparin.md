---
layout: default
title: Heparin
parent: 僅模型預測 (L5)
nav_order: 404
evidence_level: L5
indication_count: 2
---

# Heparin
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

# Heparin: From Anticoagulant Therapy to Thrombophilia due to Protein C Deficiency, Autosomal Recessive

## One-Sentence Summary

Heparin is a well-established anticoagulant used for the prevention and treatment of thromboembolic disease. The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency, autosomal recessive**, with a very high prediction score (**99.29%**), but this candidate currently has **0 clinical trials** and **0 publications** as direct supporting evidence — the signal rests on mechanistic plausibility alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anticoagulation (prevention and treatment of thromboembolic disease) — well-established use; no India licensing record available in this dataset |
| Predicted New Indication | Thrombophilia due to Protein C Deficiency, Autosomal Recessive |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation is not available for this drug entry (data gap). However, based on well-established pharmacological knowledge, heparin acts by activating antithrombin III, which in turn inhibits thrombin and factor Xa — the core mechanism underlying its anticoagulant effect.

Congenital protein C deficiency causes thrombophilia because protein C normally works with protein S to inactivate factors Va and VIIIa; when deficient, patients are prone to venous thromboembolism and, when started on warfarin without bridging, to warfarin-induced skin necrosis. Heparin's antithrombin III–mediated mechanism is pharmacologically independent of the protein C pathway, making it the textbook standard of care for treating acute thrombotic events in protein C–deficient patients and for bridging anticoagulation during warfarin initiation.

This gives the prediction strong mechanistic plausibility despite the complete absence of disease-specific trials or literature in this dataset. That absence should be read as an **evidence gap** (the condition is rare, so dedicated trials are unlikely to exist) rather than a negative signal — it warrants manual literature/guideline verification rather than outright rejection.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

- **Drug Interactions**: DrugBank/DDInter records 614 total interactions for Heparin. Notable **Moderate**-level interactions (increased bleeding or hypoglycemia risk with concurrent use) include: Acetylsalicylic acid, Chlorpropamide, Glimepiride, Repaglinide, Nateglinide, Tolazamide, Fenfluramine, Glipizide, Glyburide, Acetohexamide, Dexfenfluramine, Sibutramine, and Tolbutamide. Additional interactions with an unclassified ("Unknown") severity level include Levocarnitine, Mannitol, Calcitriol, Vitamin A, Pantoprazole, Mesalazine, and Doxycycline. These are a partial sample from a much larger interaction list and should not be treated as exhaustive.

Formal key warnings and contraindications (e.g., TFDA/label-equivalent text) are not yet available for this drug and must be obtained before clinical use is considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is very high and mechanistically well-supported by heparin's known antithrombin III/factor Xa pharmacology, but this candidate has zero direct clinical trial or literature evidence in the current dataset (Evidence Level L5), and critical safety documentation (warnings/contraindications) is missing entirely. The evidence base is not yet sufficient to progress beyond initial screening.

**To proceed, the following is needed:**
- Manual literature/guideline search specifically for heparin use in protein C deficiency–related thrombophilia (the absence of hits here reflects a data-collection gap for a rare disease, not necessarily a lack of clinical basis)
- TFDA/equivalent official label warnings and contraindications (Blocking data gap — required before any S1 safety screening can proceed)
- Formal DrugBank/MOA documentation to support mechanism-of-action review
- Confirmation of India market/licensing status, since none is currently on record
- Note: a second TxGNN signal for this drug (primary release disorder of platelets, score 99.06%, with 30 trials/20 publications) was also reviewed but excluded — the underlying evidence overwhelmingly concerns heparin-induced thrombocytopenia (a drug-caused adverse reaction) rather than treatment of a primary platelet release defect, representing a mechanistically mismatched false-positive signal that should not be advanced.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

