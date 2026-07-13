---
layout: default
title: Edaravone
parent: 僅模型預測 (L5)
nav_order: 259
evidence_level: L5
indication_count: 2
---

# Edaravone
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

# Edaravone: From Amyotrophic Lateral Sclerosis to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Edaravone (brand name: Radicava) is a free radical scavenger originally approved for the treatment of amyotrophic lateral sclerosis (ALS) and acute ischemic stroke, where oxidative stress drives neuronal damage.
The TxGNN model predicts it may have therapeutic potential in **Heparin Cofactor 2 Deficiency**, with a prediction score of **99.47%**.
However, with **0 clinical trials** and **0 publications** currently available to support this direction, this prediction rests entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Amyotrophic Lateral Sclerosis (ALS); Acute Ischemic Stroke |
| Predicted New Indication | Heparin Cofactor 2 Deficiency |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on known published information, Edaravone is a potent free radical scavenger that neutralizes reactive oxygen species (ROS) and hydroxyl radicals, protecting cells from oxidative damage. Its efficacy in ALS and acute ischemic stroke has been clinically established — both conditions share oxidative stress as a key driver of tissue injury.

The theoretical bridge to Heparin Cofactor II (HCII) deficiency works as follows: ROS can oxidize and inactivate circulating coagulation inhibitor proteins, including serine protease inhibitors such as HCII. If oxidative inactivation were a significant contributor to reduced HCII function, Edaravone's ROS-scavenging activity might theoretically help preserve functional HCII levels, thereby reducing thrombotic risk.

However, this mechanistic rationale is weak for the specific indication. HCII deficiency is fundamentally a genetic disorder — caused by insufficient protein synthesis or structural gene mutations resulting in reduced protein quantity or function from the outset. Edaravone cannot compensate for a protein that is not being produced or is structurally defective. The indirect pathway of "oxidative stress → coagulation inhibitor inactivation → thrombosis" may exist as a modulating factor, but its relative contribution to HCII deficiency is unknown and unlikely to be primary. The TxGNN model may be detecting a distant topological proximity in the disease knowledge graph rather than a direct therapeutic mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Edaravone is currently not approved or marketed in India. No product registrations were identified in the CDSCO database at the time of this report.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is high (99.47%), there is no clinical, preclinical, or mechanistic evidence connecting Edaravone to Heparin Cofactor 2 Deficiency. The disorder is genetic in origin, making Edaravone's antioxidant mechanism an unlikely therapeutic fit.

**To proceed, the following is needed:**
- Mechanistic studies confirming whether Edaravone can meaningfully elevate HCII protein activity or plasma levels in a relevant model
- Preclinical data (in vitro or animal model) demonstrating any effect on thrombin inhibition via the HCII pathway
- Drug labelling and full package insert data to complete the safety profile (currently a blocking data gap)
- Clarification of whether the TxGNN prediction is driven by indirect disease-ontology co-localization (e.g., shared thrombosis phenotype) rather than mechanistic relevance
- Consideration of whether orphan drug incentives may justify exploratory investment, given the rarity of HCII deficiency and the complete absence of existing treatments
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

