---
layout: default
title: Pegaptanib
parent: Model Prediction Only (L5)
nav_order: 651
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Pegaptanib: predicted new indication Esophageal varices with bleeding (a second prediction… (evidence level L5). Approved use: Macular degeneration"
monitor_inn: "Pegaptanib"
predicted_indications: ["esophageal varices with bleeding", "esophageal varices without bleeding"]
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

# Pegaptanib: From Macular Degeneration to Esophageal Varices with Bleeding

## One-Sentence Summary

Pegaptanib was originally used to treat macular degeneration.
The TxGNN model predicts it may be effective for **esophageal varices with bleeding** (and also esophageal varices without bleeding),
but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Macular degeneration |
| Predicted New Indication | Esophageal varices with bleeding (a second prediction, esophageal varices without bleeding, has the same score) |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general knowledge, pegaptanib is a pegylated RNA aptamer that selectively binds VEGF-165, and it is used for macular degeneration, where VEGF-driven angiogenesis plays a central role.

A theoretical link to esophageal varices exists. VEGF-driven angiogenesis and the hyperdynamic splanchnic circulation contribute to portal hypertension and the formation of portosystemic collaterals, including varices. Blocking VEGF could in principle reduce this process.

However, the link is speculative. Pegaptanib is given by intravitreal injection with minimal systemic exposure, so it is unlikely to reach the portal or splanchnic circulation at relevant levels. The score for the bleeding and non-bleeding forms is identical (0.992), which suggests it reflects a shared disease-node feature rather than evidence specific to each indication. Systemic anti-VEGF agents can also impair hemostasis and wound healing and carry bleeding risk, which is a particular concern in active variceal hemorrhage. Standard care (non-selective beta-blockers, endoscopic band ligation) is well established, so any repurposing would need preclinical support first.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 142632 | Macugen 0.3mg Infusion (Pfizer Ltd) | Bottle of 90 ml infusion (injectable) | Not stated in the available data |

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found for this drug. Note that systemic anti-VEGF agents carry bleeding and impaired wound-healing risks, which would be a particular concern in active variceal hemorrhage.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (evidence level L5), with no clinical trials or literature. The intravitreal route gives minimal systemic exposure, and there is a bleeding-risk concern in variceal bleeding.

**To proceed, the following is needed:**
- Preclinical evidence that VEGF inhibition affects portal hypertension or varices
- A feasibility assessment of route and exposure, since the current product is intravitreal only
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the India label
- A bleeding-risk assessment specific to variceal hemorrhage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

