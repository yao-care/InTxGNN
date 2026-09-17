---
layout: default
title: Idebenone
parent: Model Prediction Only (L5)
nav_order: 416
evidence_level: L5
indication_count: 10
---

# Idebenone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Idebenone: From an Unrecorded Original Indication to Hepatic Porphyria

## One-Sentence Summary

The original approved indication for Idebenone is not recorded in the current data set, and it is currently **not marketed in Taiwan**. The TxGNN model's top prediction is that Idebenone may be effective for **Hepatic Porphyria**, but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a pure model prediction with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current data |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| Taiwan Market Status | ✗ Not marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Idebenone is not available in this evidence pack (flagged as a High-severity data gap). Based on the mechanistic rationale accompanying the prediction, Idebenone is described as a CoQ10 analogue that acts on the mitochondrial electron transport chain (bypassing Complex I) and has antioxidant properties.

Hepatic porphyria's core pathology involves defects in the heme biosynthesis pathway (e.g., ALA synthase dysregulation), which has no established mechanistic link to mitochondrial oxidative phosphorylation or antioxidant activity. The evidence pack itself notes that TxGNN's high score for this pair may reflect proximity between "liver metabolism" nodes in the knowledge graph rather than a validated pharmacological mechanism.

Because Idebenone's original indication is not recorded here, no direct comparison between the original and predicted indication can be made. The mechanistic rationale should be treated as a hypothesis-generating signal only, not as pharmacological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Idebenone currently holds **no marketing authorization in Taiwan** (market status: Not marketed, 0 registered licenses). No product-level registration data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-drug interaction data are all currently unrecorded — TFDA label warnings/contraindications are flagged as a Blocking-severity data gap (DG001) that must be resolved before any safety assessment can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has zero clinical trial or literature evidence (Evidence Level L5 — model prediction only), and the proposed mechanistic link between Idebenone's mitochondrial/antioxidant activity and hepatic porphyria's heme-synthesis pathology is speculative. Combined with a Blocking-severity gap on TFDA label safety data, this candidate does not meet the threshold for further evaluation at this time.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any S1 safety screening
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Preclinical or case-level evidence connecting mitochondrial/antioxidant mechanisms to heme biosynthesis regulation
- **Porphyrinogenicity assessment**: since the predicted indication is itself a porphyria, it is essential to confirm Idebenone does not induce hepatic CYP450/ALA synthase activity, as porphyrinogenic drugs can precipitate acute porphyric attacks in this patient population
- Note: 9 additional lower-ranked candidates (hepatopulmonary syndrome, portal vein thrombosis, various myopathies, etc.) were also predicted, all at the same L5 evidence level with no supporting trials or literature — none currently warrant prioritization over this top candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

