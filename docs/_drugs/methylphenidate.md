---
layout: default
title: Methylphenidate
parent: 僅模型預測 (L5)
nav_order: 337
evidence_level: L5
indication_count: 4
---

# Methylphenidate
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

# Methylphenidate: From ADHD to Faciodigitogenital Syndrome

## One-Sentence Summary

Methylphenidate is a central nervous system stimulant with long-established use in treating Attention Deficit Hyperactivity Disorder (ADHD) and narcolepsy, acting primarily through dopamine and norepinephrine reuptake inhibition.
The TxGNN model predicts it may be effective for **Faciodigitogenital Syndrome** (Aarskog-Scott syndrome),
however, **no clinical trials and no publications** currently support this specific direction — placing this at evidence level **L5 (model prediction only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ADHD (Attention Deficit Hyperactivity Disorder) |
| Predicted New Indication | Faciodigitogenital Syndrome |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Methylphenidate functions as a dopamine transporter (DAT) and norepinephrine transporter (NET) blocker, elevating synaptic catecholamine concentrations in the prefrontal cortex and striatum. This mechanism underpins its clinical efficacy in ADHD and attention-related disorders.

Faciodigitogenital syndrome (Aarskog-Scott syndrome) is a rare X-linked condition caused by mutations in the *FGD1* gene, resulting in defective Rho GTPase / cytoskeletal signalling. The disease core involves impaired cell scaffolding and developmental morphogenesis — a pathway mechanistically unrelated to catecholamine reuptake inhibition. No known pharmacological bridge connects DAT/NET blockade to FGD1 protein function.

The high TxGNN score most likely reflects knowledge-graph topology: co-occurring phenotypic features such as cognitive developmental delay and behavioural difficulties create statistical proximity between Methylphenidate's indication neighbourhood and this rare syndrome. This is considered a high-risk false-positive signal rather than a genuine mechanistic prediction, and independent preclinical validation would be required before any further clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Methylphenidate has no products registered with CDSCO in India based on currently available regulatory data (0 licences on file).

---

## Safety Considerations

**Drug Interactions**: Methylphenidate has **137 documented interactions** in the DDInter database. Highest-priority interactions are summarised below:

| Severity | Interacting Drug | Clinical Note |
|----------|-----------------|---------------|
| **Major** | Bupropion | Increased seizure risk; potential cardiovascular effects |
| Moderate | Isometheptene | Additive sympathomimetic vasoconstriction |
| Moderate | Ephedrine | Additive sympathomimetic effects, blood pressure elevation |
| Moderate | Epinephrine | Additive cardiovascular stimulation |
| Moderate | Polyethylene glycol (3350 with electrolytes) | Potential interaction |
| Moderate | Picosulfuric acid | Potential interaction |
| Moderate | Sodium sulfate | Potential interaction |
| Unknown | Metformin, Morphine, Omeprazole, Pantoprazole, Simvastatin, Prednisone, Vancomycin, and others | Clinical significance not fully characterised |

Please refer to the package insert for complete warnings and contraindications, which were not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a near-maximum TxGNN prediction score, there is no clinical trial evidence, no supporting literature, and no established mechanistic link between Methylphenidate's catecholamine reuptake inhibition and the FGD1/Rho GTPase pathway defect that drives faciodigitogenital syndrome. The high score is best explained by phenotypic co-occurrence patterns in the knowledge graph, not pharmacological plausibility.

**To proceed, the following would be needed:**
- Preclinical studies (cell model or animal model) demonstrating a functional interaction between catecholamine signalling and FGD1/Rho GTPase pathway activity
- Systematic review of cognitive and behavioural phenotypes in faciodigitogenital syndrome to assess whether dopaminergic dysregulation is a documented feature
- India CDSCO regulatory filing and package insert data (warnings, contraindications) to complete the safety profile
- DrugBank MOA data retrieval (DG002) to enable formal mechanistic-link analysis
- Clinical case series or registry data documenting stimulant medication use in Aarskog-Scott syndrome patients, if any exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

