---
layout: default
title: Cetilistat
parent: Model Prediction Only (L5)
nav_order: 165
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Cetilistat: predicted new indication Hypervitaminosis (evidence level L5). Approved use: Obesity disorder"
monitor_inn: "Cetilistat"
predicted_indications: ["hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "obsolete hypertelorism (disease)", "frontorhiny"]
---

# Cetilistat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Cetilistat: From Obesity to Hypervitaminosis

## One-Sentence Summary

Cetilistat is a gastrointestinal lipase inhibitor originally used to treat obesity, including monogenic obesity.
The TxGNN model predicts it may be effective for **Hypervitaminosis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity disorder; monogenic obesity (the India licence records contain no approved indication text) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, cetilistat is a gastrointestinal (pancreatic) lipase inhibitor that reduces the absorption of dietary fat. Its efficacy in obesity is the basis of its original use, and it is approved in Japan for obesity and related disorders, including type 2 diabetes.

The link to hypervitaminosis is theoretical. Fat-soluble vitamins (A, D, E, K) are absorbed together with dietary fat, so blocking fat absorption could lower their uptake. However, reduced vitamin absorption is a recognised adverse effect of this drug class, not an established therapeutic strategy. The high TxGNN score (99.98%) is a computational prediction only and is not backed by any trial or publication.

Other predictions from the model are weaker still:
- **Proximal 16p11.2 microdeletion syndrome** (99.97%): this is a genetic cause of severe early-onset obesity, so there is an indirect link to the original indication. Any benefit would be limited to weight effects and would not address the neurodevelopmental features.
- **Hypertelorism (obsolete term)** and **frontorhiny**: these are craniofacial malformations with no plausible pharmacological link to lipase inhibition. They are likely knowledge-graph artifacts.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 39467 | Cetislim Tablet | Strip of 10 tablets | Not stated in the licence record |
| 26877 | Belishape 120mg Tablet | Strip of 10 tablets | Not stated in the licence record |
| 115837 | Kilfat Tablet | Strip of 10 tablets | Not stated in the licence record |

All three registrations are valid single-ingredient oral products (Akumentis Healthcare Ltd for Cetislim and Kilfat; Oldmed Healthcare Pvt Ltd for Belishape).

## Safety Considerations

- **Drug Interactions**: The only interaction recorded is pharmacological. Cetilistat targets human pancreatic lipase (gene *PNLIP*), which is its intended mechanism rather than a drug-drug interaction. No interaction severity level is available.

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score, with no clinical trials or literature (Evidence Level L5). The proposed mechanism is also an adverse effect of lipase inhibitors rather than a recognised treatment approach for hypervitaminosis.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-marketed products, which are required before any safety screening
- Detailed mechanism of action data
- Preclinical or observational data on whether lipase inhibition meaningfully lowers fat-soluble vitamin levels in hypervitaminosis
- Evidence of a clinical benefit that would outweigh the risk of vitamin deficiency from reduced absorption
- A reassessment of whether the 16p11.2 microdeletion prediction merits follow-up as an obesity-related indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

