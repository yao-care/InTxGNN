---
layout: default
title: Inositol Nicotinate
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 10
---

# Inositol Nicotinate
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

以下是根據 Evidence Pack 產生的評估報告：

---

# Inositol Nicotinate: From Niacin Supplement to Vitamin Deficiency Disorder

## One-Sentence Summary

Inositol nicotinate is a niacinamide ester of inositol that functions as a slow-release form of niacin (Vitamin B3); it carries no registered indications in the Indian regulatory database and has not been marketed there.
The TxGNN model predicts it may be effective for **Vitamin Deficiency Disorder**, with a prediction score of **99.96%**, yet **0 clinical trials** and **0 publications** currently support this specific repurposing direction.
All top-10 predicted indications share the same L5 evidence level, meaning this candidate rests entirely on model inference with no corroborating empirical data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indications (not marketed in India) |
| Predicted New Indication | Vitamin Deficiency Disorder |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Inositol nicotinate is a compound in which six nicotinic acid (niacin / Vitamin B3) molecules are esterified to one inositol ring. Upon hydrolysis in the body, it releases both free nicotinic acid and inositol (sometimes informally classified as Vitamin B8). Because niacin deficiency is the direct cause of pellagra — a classical vitamin deficiency syndrome — the chemical composition of inositol nicotinate provides the most straightforward mechanistic rationale for a link to vitamin deficiency disorders. The TxGNN model's high confidence score (0.9996) very likely reflects this structural feature rather than any disease-specific biological interaction.

Inositol plays a distinct role as a precursor to phosphatidylinositol and the IP₃/DAG second messenger pathway, meaning the compound simultaneously participates in both vitamin metabolism (via niacin) and membrane signalling (via inositol). This dual biochemical identity may cause the knowledge graph to connect the drug to a broad cluster of metabolic and nutritional disease nodes, partly explaining the high scores across multiple dissimilar indications in the top-10 list.

Currently, detailed mechanism of action data is not available from the DrugBank query included in this Evidence Pack. Based on known pharmacology, inositol nicotinate is recognised as a "flush-free" niacin formulation; its efficacy in managing dyslipidaemia has been investigated in other markets, and its relationship to vitamin B3 replenishment provides the primary biological basis for the top TxGNN prediction. Until MOA data are formally retrieved and the drug's full pharmacological profile is confirmed, mechanistic conclusions should be treated as provisional.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the 10 predicted indications.

---

## Literature Evidence

Currently no related literature available for any of the 10 predicted indications.

---

## India Market Information

This drug is not currently marketed in India. No regulatory licences or approved product records are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note — Potential Negative Mechanism (Rank 5 Indication):** Although full safety data are unavailable, it is pharmacologically established that high-dose niacin can competitively inhibit renal tubular secretion of organic acids, reducing uric acid clearance and raising serum urate. The TxGNN prediction of *acute urate nephropathy* (rank 5, score 99.70%) therefore conflicts with the known pharmacology of the niacin component; this indication should be deprioritised and treated as a potential safety concern rather than a repurposing opportunity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications sit at Evidence Level L5 — model prediction only, with zero supporting clinical trials or peer-reviewed publications — making it premature to advance any candidate to a feasibility or investment decision stage.

**To proceed, the following is needed:**

- **MOA data retrieval**: Query DrugBank API for DB08949 to obtain full mechanism of action, categories, and toxicity profile before any mechanistic analysis can be completed.
- **Safety data retrieval**: Download and parse the relevant package inserts (or equivalent regulatory labelling) to populate warnings, contraindications, and drug interaction data — currently all flagged as blocking data gaps.
- **Literature scoping review**: Commission a broader PubMed/Embase search using niacin and inositol as alternative search terms (rather than only "inositol nicotinate") to determine whether closely related compounds have supporting evidence for the top predicted indications.
- **Cluster effect validation**: The four hepatoportal indications (ranks 7–10) share an identical TxGNN score (0.9962), strongly suggesting a KG cluster effect rather than genuine disease-specific predictions. A graph analysis of the TxGNN disease node neighbourhood for these indications is recommended before interpreting them as distinct repurposing signals.
- **India regulatory pathway assessment**: Since the drug is not marketed in India, a regulatory entry-point assessment (import licence, new drug application, or investigational use pathway) would be required before any clinical development can be initiated in-country.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

