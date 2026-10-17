---
layout: default
title: Racecadotril
parent: Model Prediction Only (L5)
nav_order: 719
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Racecadotril: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Acute diarrhea"
monitor_inn: "Racecadotril"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder", "septicemic plague", "acute cystitis (disease)"]
---

# Racecadotril
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Racecadotril: From Acute Diarrhea to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Racecadotril is an intestinal antisecretory drug originally used to treat acute diarrhea.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute diarrhea |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 97.72% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, racecadotril is a prodrug that inhibits enkephalinase (neprilysin). This reduces breakdown of enkephalins in the gut and lowers intestinal hypersecretion, which is the basis for its use in acute diarrhea.

No plausible link was identified between this mechanism and polyclonal hyperviscosity syndrome, a condition of raised serum viscosity from elevated polyclonal immunoglobulins. The high score therefore appears to be a computational artefact of the knowledge graph rather than a pharmacological signal.

The same pattern holds for the other top predictions, which are mostly haematological or immune conditions: hyperamylasemia, congenital analbuminemia, blood group incompatibility, monoclonal gammopathy and others. None has a recognised mechanistic connection to enkephalinase inhibition. Several scored identically or almost identically (hyperamylasemia 97.72%, congenital analbuminemia 97.53%), which suggests the scores reflect network proximity among related disease terms.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Racecadotril is marketed in India with 20 valid single-ingredient registrations and no cancelled ones. The compiled data contains no approved-indication text for these products. Five of them:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 199136 | Radovib 100mg Capsule | Strip of 10 capsules | Vibcare Pharma Pvt Ltd |
| 36480 | Cadotril 100mg Capsule | Strip of 10 capsules | Ordain Health Care Global Pvt Ltd |
| 192558 | Rotril 10mg Sachet | Packet of 1 gm sachet | Delwis Healthcare Pvt Ltd |
| 249060 | Zomatril 100mg Tablet DT | Strip of 10 dispersible tablets | FDC Ltd |
| 74114 | Enuff O Dry Syrup | Bottle of 30 ml oral suspension | Hetero Drugs Ltd |

Available forms include capsules, dispersible tablets, sachets, powder, granules and oral suspensions.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature and no plausible mechanistic link to the predicted condition. All ten top-ranked predictions are likewise at evidence level L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator, since safety screening cannot proceed without them
- Detailed mechanism of action data (MOA) from DrugBank
- A credible biological hypothesis linking enkephalinase inhibition to polyclonal hyperviscosity syndrome
- Preclinical or mechanistic studies, if such a hypothesis emerges
- A review of lower-ranked predictions, especially those closer to gastrointestinal indications, which may be more pharmacologically plausible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

