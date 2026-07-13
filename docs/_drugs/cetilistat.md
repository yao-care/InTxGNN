---
layout: default
title: Cetilistat
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 4
---

# Cetilistat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Cetilistat: From Obesity to Hypervitaminosis

## One-Sentence Summary

Cetilistat is a pancreatic lipase inhibitor approved in Japan in 2013 for the treatment of obesity and related metabolic disorders, including type 2 diabetes.
The TxGNN model predicts it may be effective for **Hypervitaminosis**,
however there are currently **0 clinical trials** and **0 publications** directly supporting this direction — the prediction rests entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Obesity and type 2 diabetes (approved Japan 2013, not approved in US or EU) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the primary DrugBank record. Based on pharmacological evidence gathered from the drug interaction database, Cetilistat (also known as ATL-962, marketed as Oblean® in Japan) functions as an **intestinal pancreatic lipase inhibitor** — it blocks the enzyme responsible for hydrolyzing dietary triglycerides in the gut, thereby reducing fat absorption by approximately 35%. This mechanism mirrors that of orlistat but with a structurally distinct compound, offering a potentially improved gastrointestinal tolerability profile.

The TxGNN link to hypervitaminosis is mechanistically plausible on its surface: because Cetilistat reduces intestinal fat absorption, it would theoretically also impair the co-absorption of **fat-soluble vitamins (A, D, E, and K)**, which depend on dietary lipids for micellar incorporation. The model may have interpreted this "fat-soluble vitamin absorption reduction" pathway as a positive association with hypervitaminosis (excess fat-soluble vitamins), suggesting the drug could correct an absorption-driven excess state.

However, this mechanistic connection is tenuous and potentially counterproductive in practice. Fat-soluble hypervitaminosis (e.g., vitamin A or D toxicity) is primarily managed by **discontinuing the offending supplement or food source** — not by blocking intestinal absorption broadly. More critically, indiscriminate lipase inhibition would simultaneously reduce all fat-soluble vitamins, risking deficiency states (particularly vitamins D and K) even in patients being treated for vitamin A or D excess. The prediction is best understood as a topological artifact of the knowledge graph rather than a clinically actionable association.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Cetilistat has no registered products in India. It is not approved by CDSCO and has no active marketing authorizations.

---

## Safety Considerations

**Drug Interactions (Pharmacological):**
- Cetilistat directly inhibits **pancreatic lipase (PNLIP, gene: PNLIP, Entrez: 5406)** — its primary pharmacological target. This interaction underlies all downstream metabolic effects, including impaired absorption of fat-soluble vitamins A, D, E, and K. Co-administration with fat-soluble vitamin supplements or drugs with lipophilic formulations may result in altered bioavailability.

For warnings and contraindications, please refer to the Japanese package insert (Oblean®), as no CDSCO-approved label exists and formal safety data was not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four TxGNN-predicted indications for Cetilistat carry L5 evidence — model prediction only, with zero supporting clinical trials or publications. The top prediction (hypervitaminosis) is mechanistically speculative and carries meaningful safety concerns if pursued clinically. The drug is not registered in India, providing no existing regulatory foundation to build upon.

**To proceed, the following is needed:**

- **Mechanistic validation**: Obtain full MOA data from DrugBank API (DB06586) to confirm or expand the known lipase inhibition profile and assess applicability to hypervitaminosis subtypes
- **Safety data**: Retrieve the Japanese prescribing information (Oblean® package insert) to populate key warnings, contraindications, and known adverse events — currently a blocking data gap (DG001)
- **Indication reassessment**: Consider evaluating Cetilistat against its **primary approved indication** (obesity / type 2 diabetes) rather than model-predicted indications, as clinical evidence for these is substantially more developed
- **KG artifact review**: Indications ranked 3 (obsolete hypertelorism) and 4 (frontorhiny) should be flagged as likely knowledge graph topology false positives and excluded from further review cycles
- **Vitamin monitoring protocol**: Any exploratory study design involving Cetilistat must include serial monitoring of serum fat-soluble vitamin levels (A, 25-OH-D, E, INR/PT for K) given the mechanism-driven depletion risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

