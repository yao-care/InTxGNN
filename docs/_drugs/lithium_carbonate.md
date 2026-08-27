---
layout: default
title: Lithium Carbonate
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
---

# Lithium Carbonate
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

# Lithium Carbonate: From Bipolar Disorder to Pseudoachondroplasia

## One-Sentence Summary

Lithium carbonate is a classic mood-stabilizing agent, widely used for the management of bipolar disorder and related mood conditions.
The TxGNN model predicts it may have therapeutic potential for **Pseudoachondroplasia**,
however, **no supporting clinical trials or published literature** have been identified for this specific indication, placing this prediction at the lowest evidence level (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bipolar disorder / Mood stabilization (universally established; no India regulatory record on file) |
| Predicted New Indication | Pseudoachondroplasia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for lithium carbonate is not available in this evidence pack. Based on established pharmacology, lithium carbonate's best-characterized molecular target is GSK-3β (glycogen synthase kinase-3β). By inhibiting GSK-3β, lithium activates downstream Wnt/β-catenin signaling, a pathway known to participate in bone and cartilage morphogenesis. In theory, potentiating this pathway could influence chondrogenesis and skeletal development, which is the basis for the model's prediction.

However, pseudoachondroplasia is primarily caused by mutations in the **COMP gene** (cartilage oligomeric matrix protein), which lead to abnormal protein folding and retention of COMP in the endoplasmic reticulum of chondrocytes. The disease pathology centers on ER stress and protein trafficking failure — not on Wnt pathway dysregulation. The mechanistic bridge between lithium's GSK-3β inhibition and the COMP-mutation-driven chondrocyte dysfunction is therefore highly indirect and lacks any direct experimental grounding.

In summary, while lithium's effects on cellular signaling are real and well-characterized in neuropsychiatric contexts, their applicability to a rare structural skeletal dysplasia of this etiology remains entirely theoretical. The high TxGNN score reflects graph-topological proximity in the knowledge graph, not mechanistic or clinical plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Lithium carbonate has no regulatory registrations on record in the India market dataset included in this evidence pack.

---

## Safety Considerations

**Drug Interactions**: Lithium carbonate has **252 documented drug interactions** in the DDI database. Selected interactions by severity are listed below:

| Severity | Representative Interacting Drugs |
|----------|----------------------------------|
| **Major** | Bupropion, Lorcaserin |
| **Moderate** | Metformin, Metronidazole, Clarithromycin, Morphine, Pioglitazone, Canagliflozin, Chlorpropamide, Alogliptin, Albiglutide, Acarbose, Mesalazine, Balsalazide, Loperamide, Famotidine, Potassium citrate |
| **Minor** | Doxycycline, Epinephrine, Acetylsalicylic acid |

> Note: The complete list comprises 252 interactions. Major interactions (e.g., Bupropion) may increase seizure risk or serotonergic toxicity. Please consult the full package insert for comprehensive safety information including warnings and contraindications, which were not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial, observational study, or directly relevant literature linking lithium carbonate to pseudoachondroplasia. The TxGNN prediction is driven entirely by knowledge graph topology (L5), and the proposed mechanistic link — GSK-3β inhibition in a disease whose root cause is COMP protein misfolding — is too indirect to justify further development without substantial preclinical validation.

**To proceed, the following is needed:**
- Formal mechanism of action (MOA) documentation from DrugBank or peer-reviewed sources
- Preclinical cell-line or animal model studies demonstrating GSK-3β / Wnt pathway modulation specifically in COMP-mutant chondrocytes
- Evidence that Wnt pathway dysregulation contributes to pseudoachondroplasia phenotype (biomarker or genetic studies)
- India regulatory package insert data for full safety warnings, contraindications, and dosing guidance
- Evaluation of whether lithium's narrow therapeutic index is compatible with pediatric skeletal dysplasia populations (this condition typically presents in childhood)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

