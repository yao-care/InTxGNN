---
layout: default
title: Pegaptanib
parent: Model Prediction Only (L5)
nav_order: 645
evidence_level: L5
indication_count: 2
---

# Pegaptanib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Pegaptanib: From Neovascular Age-Related Macular Degeneration to Esophageal Varices with Bleeding

## One-Sentence Summary

Pegaptanib is an anti-VEGF165 aptamer originally developed for neovascular (wet) age-related macular degeneration. The TxGNN model predicts potential efficacy for **esophageal varices with bleeding**, but this direction is currently supported by **zero clinical trials** and **zero publications** — it rests entirely on a theoretical mechanistic hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neovascular (wet) age-related macular degeneration |
| Predicted New Indication | Esophageal varices with bleeding |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is not yet available for pegaptanib in this evidence pack (flagged as a High-severity data gap). Based on known pharmacology, pegaptanib is an anti-VEGF165 aptamer that inhibits angiogenesis, and this mechanism is what underlies its proven efficacy in neovascular AMD.

The proposed link to esophageal varices rests on the observation that portosystemic collateral vessel formation in portal hypertension has, in animal models, been associated with VEGF signaling — so an anti-VEGF agent could theoretically reduce collateral vessel growth. However, this connection is a mechanistic hypothesis only; no human data (for pegaptanib or any anti-VEGF agent) support use in esophageal variceal bleeding.

Importantly, this hypothesis contains an internal tension worth flagging explicitly: anti-VEGF agents are systemically associated with a known bleeding tendency, which is directly at odds with using the drug to manage or prevent variceal **bleeding** in cirrhotic/portal-hypertensive patients. A closely related candidate — esophageal varices *without* bleeding (rank 2, same TxGNN score) — was also predicted, but carries the same lack of evidentiary support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Pegaptanib is not currently marketed (0 registrations on file); no authorization records are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: the mechanistic rationale above independently flags a plausible bleeding-risk concern specific to this indication — anti-VEGF agents carry a known bleeding-tendency side effect, which is mechanistically discordant with treating variceal bleeding. This should be treated as a safety signal pending confirmed labeling data.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is evidence level L5 — a model prediction with no supporting clinical trials or literature, and the underlying mechanistic story is mechanistically self-contradictory (an agent with a known bleeding-tendency side effect proposed for a bleeding indication). TFDA/label safety data needed for even a preliminary safety screen (S1) is currently blocked (Data Gap DG001, Blocking severity).

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently blocking S1 safety screening
- Confirmed DrugBank mechanism-of-action data for pegaptanib
- Preclinical/mechanistic evidence specifically linking VEGF inhibition to portal hypertension collateral formation (not just general angiogenesis literature)
- Safety data on systemic anti-VEGF use in cirrhotic/portal-hypertensive patients, given the bleeding-risk contradiction noted above
- Any real-world or case-level evidence before advancing past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

