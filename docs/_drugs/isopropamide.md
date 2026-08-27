---
layout: default
title: Isopropamide
parent: 僅模型預測 (L5)
nav_order: 349
evidence_level: L5
indication_count: 2
---

# Isopropamide
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

# Isopropamide: From Anticholinergic Agent to Gastroduodenitis

## One-Sentence Summary

Isopropamide is an anticholinergic (antimuscarinic) agent with no currently recorded approved indications in the dataset; its pharmacological class suggests historical use in gastrointestinal spasm and acid-related conditions.
The TxGNN model predicts it may be relevant for **Gastroduodenitis** (rank 1) and **Overactive Bladder** (rank 2).
However, **zero clinical trials and zero publications** were identified for either indication, placing the overall evidence at the lowest tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record |
| Predicted New Indication | Gastroduodenitis (rank 1); Overactive Bladder (rank 2) |
| TxGNN Prediction Score | 99.99% (Gastroduodenitis); 99.88% (Overactive Bladder) |
| Evidence Level | L5 — Model prediction only, no actual studies |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Isopropamide belongs to the anticholinergic (antimuscarinic) drug class. Agents of this class act by blocking muscarinic acetylcholine receptors — in particular the M3 subtype — thereby reducing smooth muscle contraction and secretory activity in the gastrointestinal and urogenital tracts. This mechanism is consistent with the TxGNN model's two top predictions.

For **Gastroduodenitis** (rank 1): Antimuscarinic agents theoretically reduce gastric acid output by inhibiting M3 receptors on gastric parietal cells and relieve associated cramping by reducing smooth muscle tone in the duodenal wall. This creates an indirect pharmacological link to the inflammatory symptom complex seen in gastroduodenitis. However, modern gastroduodenitis management has largely shifted to proton pump inhibitors (PPIs) and *H. pylori* eradication regimens, rendering anticholinergic therapy a marginal and outdated approach. The TxGNN high score (0.9999) most likely reflects knowledge-graph node proximity — i.e., shared pathway nodes — rather than direct clinical utility.

For **Overactive Bladder (OAB)** (rank 2): This is the pharmacologically more compelling repurposing direction. Isopropamide's antimuscarinic mechanism is identical to that of established OAB therapies such as oxybutynin, tolterodine, solifenacin, and darifenacin — all of which block bladder detrusor M3 receptors to suppress involuntary contractions. Class-level evidence for M3 antagonism in OAB is rated L1. Nevertheless, isopropamide itself has no OAB-specific clinical data, and the drug is currently off-market with an incomplete safety database.

Currently, detailed mechanism of action data (MOA) for isopropamide is not available in the provided dataset. The mechanistic reasoning above is inferred from known anticholinergic pharmacology and the explanatory notes embedded in the Evidence Pack's repurposing rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for either predicted indication.

---

## Literature Evidence

Currently no related literature available for either predicted indication.

---

## India Market Information

Isopropamide has **no registered products** in India. No authorization records are available.

---

## Safety Considerations

Please refer to the package insert (or historical drug monographs) for safety information. No warnings, contraindications, or drug interaction data were available in the current dataset. As the drug is not currently marketed in India, independent safety review is essential before any clinical development pathway is initiated.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence base for Isopropamide in both predicted indications is at the L5 level (model prediction only, no supporting studies). The drug is not marketed in India and has zero safety data on file — formal development cannot proceed responsibly without first resolving fundamental data gaps.

**To proceed, the following is needed:**

- **MOA data**: Confirm receptor-binding profile and selectivity from DrugBank or published pharmacology literature
- **Safety package**: Retrieve historical prescribing information (package insert, WHO monograph, or archived regulatory filings) to characterise warnings, contraindications, and known adverse effects
- **Drug interaction profile**: Assess anticholinergic drug-drug interactions, especially with other CNS-active or narrow-therapeutic-index agents
- **Indication prioritisation**: If development is pursued, the **Overactive Bladder** direction (rank 2, L4 by class-effect inference) offers a stronger mechanistic justification than Gastroduodenitis (rank 1, L5); recommend redirecting primary analysis to OAB
- **Regulatory feasibility assessment**: Determine whether isopropamide was voluntarily withdrawn or formally recalled, as this has direct implications for regulatory re-entry strategy
- **Preclinical data review**: Search for any archived in vitro/in vivo studies to establish a minimum evidence floor before considering Phase 1 planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

