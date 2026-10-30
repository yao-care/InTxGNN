---
layout: default
title: Eflornithine
parent: Model Prediction Only (L5)
nav_order: 299
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
monitor_inn: "Eflornithine"
predicted_indications: ["esotropia", "neurotrophic keratopathy"]
description: "Eflornithine: predicted new indication Esotropia (evidence level L5). Approved use: Not recorded in the local data"
---

# Eflornithine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Eflornithine: Esotropia
{: .text-alpha }

## One-Sentence Summary

Eflornithine was originally used to treat human African trypanosomiasis (sleeping sickness), and in India it is marketed as a topical cream.
The TxGNN model predicts it may be effective for **esotropia**, but **no clinical trials and no publications** currently support this prediction, so it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Esotropia |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (5 of 5) – CDSCO approval status is not included in this data |
| Number of Listed Products | 5 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, eflornithine irreversibly inhibits ornithine decarboxylase (ODC), the first step of polyamine biosynthesis. This is how it acts against African trypanosomes, and it is the target the pharmacology data lists for the drug.

The link to esotropia is weak. Esotropia is an ocular alignment disorder tied to neuromuscular and visual-development factors. No established connection exists between polyamine depletion and its pathophysiology. The high score (0.9985) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It has no clinical or literature support, so the prediction should be treated as a hypothesis, not a finding.

Other predicted indications in the same list have better biological grounding. Bovine trypanosomiasis, for example, uses the same ODC-inhibition mechanism as the original indication. It is covered under "Other Predictions Worth Noting" below.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for esotropia.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 73041 | Efnithin 13.9% Cream (Zydus Cadila) | Cream, 10 g tube | Not listed |
| 72374 | Eflora Cream (Sun Pharmaceutical Industries Ltd) | Cream, 15 g tube | Not listed |
| 74214 | Eflite 13.9% Cream (Canbro Healthcare) | Cream, 15 g tube | Not listed |
| 74174 | Eflocare Cream (Shalaks Healthcare) | Cream, 10 g tube | Not listed |
| 72444 | Elyn Cream (Ajanta Pharma Ltd) | Cream, 15 g tube | Not listed |

All five registrations are valid single-ingredient topical creams. The available injectable and oral uses of eflornithine are not represented among the Indian registrations in the data. Reference sources describe the topical use as treatment of facial hirsutism.

## Safety Considerations

- **Knowledge-graph contraindication signals**: The knowledge graph links eflornithine to exanthem (rash) and dermatitis as contraindication-type associations. These come from graph relationships, not from label text, and should be verified against the package insert.
- **Drug Interactions**: One pharmacology entry was found: the drug's target, ornithine decarboxylase (ODC1, human). This is a target relationship, not a drug-drug interaction with a graded severity.

Please refer to the package insert for further safety information, including warnings and contraindications.

## Other Predictions Worth Noting

| Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Neurotrophic keratopathy | 0.9938 | L5 | Speculative. ODC inhibition might impair corneal epithelial repair. |

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The esotropia prediction rests only on a model score, with no trials, no literature, and no plausible mechanistic link to polyamine depletion. The Indian marketed products are topical creams, and route compatibility with an ocular alignment disorder has not been established.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products, which are currently missing and block safety screening
- Detailed mechanism of action data for eflornithine
- A literature and trial search that targets esotropia specifically, and a mechanistic hypothesis if any signal is found
- A route and formulation assessment against the topical products actually marketed
- If a lead is wanted from this candidate list, evaluate bovine trypanosomiasis (the only candidate with a mechanistic rationale and related literature) as a veterinary research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

