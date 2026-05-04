---
layout: default
title: Levodopa
parent: 僅模型預測 (L5)
nav_order: 288
evidence_level: L5
indication_count: 1
---

# Levodopa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Levodopa: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Levodopa is a dopamine precursor and the cornerstone pharmacological treatment for Parkinson's disease, typically administered in combination with a decarboxylase inhibitor (e.g., carbidopa or benserazide).
The TxGNN model predicts it may be effective for **Rasmussen Subacute Encephalitis**, a rare, progressive inflammatory brain disorder.
Currently, **no clinical trials** and **no publications** directly support this specific repurposing direction, making this a purely model-driven hypothesis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease (dopamine replacement therapy) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Levodopa is the metabolic precursor to dopamine. It crosses the blood-brain barrier and is converted to dopamine in the brain by aromatic L-amino acid decarboxylase, compensating for the dopaminergic deficit in basal ganglia circuits.

Rasmussen Subacute Encephalitis (RE) is a rare, severe, progressive neuroinflammatory disease primarily affecting children, characterized by focal cortical inflammation, intractable epilepsy, and progressive hemiplegia. The pathophysiology involves T-cell–mediated cytotoxicity against neurons and astrocytes. While the mechanistic link between dopaminergic augmentation and RE is not immediately obvious, TxGNN's knowledge graph may be capturing indirect pathways — such as shared neurological network disruption, seizure-related dopaminergic dysregulation, or co-occurrence patterns in the training data.

It is important to note that the high TxGNN score (99.06%) reflects the model's confidence based on graph topology and learned relationships, **not** the strength of clinical evidence. Without any supporting trials or literature, this prediction should be regarded as a hypothesis-generating signal requiring independent mechanistic validation before further development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Levodopa has **no registered products** in India at this time (0 licenses, not marketed).

---

## Safety Considerations

**Drug Interactions** (104 total interactions identified; representative selection below):

| Interacting Drug | Severity | Notes |
|-----------------|----------|-------|
| Epinephrine | Moderate | Potential for cardiovascular effects |
| Bupropion | Moderate | Risk of increased dopaminergic adverse effects |
| Metoclopramide | Moderate | Dopamine antagonism may reduce levodopa efficacy |
| Metronidazole | Moderate | Potential pharmacokinetic interaction |
| Pyridoxine (Vitamin B6) | Moderate | May accelerate peripheral levodopa metabolism, reducing CNS availability (clinically significant without decarboxylase inhibitor) |
| Iron | Moderate | Chelation may reduce levodopa absorption |
| Atropine | Moderate | Anticholinergic interaction |
| Hyoscyamine | Moderate | Anticholinergic interaction |
| Glycopyrronium | Moderate | Anticholinergic interaction |
| Ephedrine | Moderate | Sympathomimetic interaction risk |
| Aluminum hydroxide | Minor | May reduce absorption |
| Calcium carbonate | Minor | May reduce absorption |
| Magnesium hydroxide | Minor | May reduce absorption |

For complete warnings and contraindications, please refer to the package insert, as this data was not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This repurposing candidate is supported only by TxGNN model prediction (Evidence Level L5) with zero clinical trials and zero publications linking Levodopa to Rasmussen Subacute Encephalitis. The absence of any documented human or preclinical evidence means the risk-benefit profile cannot be assessed at this stage.

**To proceed, the following is needed:**

- **Mechanistic validation**: Identify a plausible biological pathway connecting dopaminergic signaling to RE pathophysiology (e.g., dopamine's role in neuroinflammation, GABAergic/glutamatergic modulation, or seizure threshold regulation)
- **Preclinical evidence**: Animal model studies or in vitro data demonstrating Levodopa's effect on encephalitic or seizure-related neuroinflammation
- **Literature review**: Broader search for any case reports, compassionate use records, or mechanistic studies in related inflammatory encephalopathies
- **Safety data gap closure**: Obtain and review full TFDA/CDSCO package insert for formal warnings and contraindications
- **MOA data retrieval**: Query DrugBank API (DB01235) for complete mechanism, targets, and pathways to support mechanistic linkage analysis
- **Regulatory pathway assessment**: Given Levodopa is not currently marketed in India, a de novo regulatory strategy would be required if the hypothesis is validated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

