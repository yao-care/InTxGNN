---
layout: default
title: Carbocisteine
parent: Model Prediction Only (L5)
nav_order: 146
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Carbocisteine: predicted new indication Gout (evidence level L5). Approved use: Not stated in the licence records compiled for this report"
monitor_inn: "Carbocisteine"
predicted_indications: ["gout"]
---

# Carbocisteine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Carbocisteine: From Mucolytic Therapy to Gout
{: .text-alpha }

## One-Sentence Summary

Carbocisteine is a mucolytic agent (a cysteine derivative) marketed in India as Mucodyne capsules and syrup. The TxGNN model predicts it may be effective for **gout**, but there are currently **no registered clinical trials and no publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records compiled for this report |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indication is recorded in the data compiled for this report. Carbocisteine is generally known as a mucolytic, and it has reported antioxidant and anti-inflammatory properties.

Those properties could plausibly relate to the inflammatory side of gout, for example by reducing oxidative stress or neutrophil-driven inflammation. This is speculative. Nothing in the compiled data confirms a mechanistic link between carbocisteine and gout.

The very high TxGNN score (99.67%) is a model-derived prediction only. It is not clinical or mechanistic evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 137159 | Mucodyne 250mg Capsule | Strip of 10 capsules | Not stated |
| 146086 | Mucodyne 150mg Capsule | Strip of 10 capsules | Not stated |
| 135708 | Mucodyne 250mg Syrup | Bottle of 100 ml syrup | Not stated |

All three licences are valid single-ingredient products from Elder Pharmaceuticals Ltd.

## Safety Considerations

- **Knowledge-graph contraindication signal**: The TxGNN knowledge graph (PrimeKG) links carbocisteine to **active peptic ulcer disease** as a contraindication. This comes from graph relationships, not from package insert text.
- **Drug interactions**: No interaction records were found.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (Evidence Level L5). There are no clinical trials, no literature and no confirmed mechanism linking carbocisteine to gout. The approved indications and package insert safety information are also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulatory source (blocking gap)
- Approved indication text for the Mucodyne licences
- Mechanism of action data for carbocisteine, from DrugBank or other sources
- A literature and trial search on carbocisteine's antioxidant and anti-inflammatory effects in urate-crystal or gouty inflammation models
- Assessment of the peptic ulcer contraindication signal, since gout patients often use NSAIDs that carry gastrointestinal risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

