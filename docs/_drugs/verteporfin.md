---
layout: default
title: Verteporfin
parent: Model Prediction Only (L5)
nav_order: 887
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Verteporfin: predicted new indication Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies (evidence level L5). Approved use: Macular degeneration"
monitor_inn: "Verteporfin"
predicted_indications: ["mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies"]
---

# Verteporfin
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

## Verteporfin: From Macular Degeneration to Mitochondrial Oxidative Phosphorylation Disorder Due to Nuclear DNA Anomalies
{: .text-alpha }

## One-Sentence Summary

Verteporfin is a photosensitizer originally used in photodynamic therapy for macular degeneration.
The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**,
but currently **no clinical trials and no publications** support this direction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Macular degeneration |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 0.9949 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, verteporfin is a benzoporphyrin-derivative photosensitizer used in photodynamic therapy for neovascular macular degeneration. Its efficacy in that eye disease is established, but a mechanistic link to the new indication has not been shown.

Preclinical reports suggest verteporfin can inhibit YAP-TEAD signaling. However, the data compiled for this report contain nothing connecting this activity to mitochondrial disorders caused by nuclear DNA abnormalities. Any connection, for example through mitochondrial stress, reactive oxygen species (ROS) or autophagy modulation, is speculative and unverified.

There is also a safety concern. When activated by light, verteporfin generates ROS, which could plausibly worsen rather than improve mitochondrial dysfunction. This must be resolved before any repurposing hypothesis is pursued. The high model score (0.9949) should therefore be treated as a hypothesis-generating signal only.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 234341 | Visudyne Injection (Novartis India Ltd) | Vial of 1, powder for injection | Not specified in the available data |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (derived from the TxGNN knowledge graph, not from package insert text): inherited porphyria, porphyrin metabolism disease, porphyria, liver disease, gallbladder disease.
- **Drug Interactions**: 117 interactions were recorded, mostly of Moderate severity. Examples include:
  - Tetracycline-class antibiotics (doxycycline, tetracycline, minocycline), including topical forms
  - Sulfonylurea antidiabetics (glimepiride, glipizide, glyburide, tolbutamide, chlorpropamide, tolazamide, acetohexamide)
  - Acetylsalicylic acid
  - Levofloxacin
  - Sulfasalazine
  - Mannitol
  - Beta carotene
  - Papaverine

  Many of these are likely photosensitivity-related. Polymyxin B is listed as Minor.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it (Evidence Level L5). No mechanistic link to the proposed indication is established, and verteporfin's ROS-generating photosensitizing action could be harmful in mitochondrial disease. Investment in this direction is not justified at present.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) to support a mechanistic-link analysis
- Package insert warnings and contraindications from the India Pharma source, which currently block safety screening
- Preclinical studies testing verteporfin in models of nuclear-DNA-driven OXPHOS deficiency, with attention to ROS-related toxicity
- A literature and trial search to confirm whether any supporting evidence exists
- Assessment of route compatibility, since the current product is an injectable used with light activation in the eye
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

