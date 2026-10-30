---
layout: default
title: Doripenem
parent: Model Prediction Only (L5)
nav_order: 284
evidence_level: L5
indication_count: 5
monitor_inn: "Doripenem"
predicted_indications: ["hepatoportal sclerosis", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis"]
last_modified_at: 2026-10-30
description: "Doripenem: predicted new indication Hepatoportal sclerosis (evidence level L5). Approved use: Cholecystitis, low phospholipid associated cholelithiasis…"
---

# Doripenem
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Doripenem: From Cholecystitis to Hepatoportal Sclerosis
{: .text-alpha }

## One-Sentence Summary

Doripenem is a carbapenem antibiotic. The TxGNN model (deep learning) predicts it may be effective for **hepatoportal sclerosis**, but **no clinical trials and no publications** support this prediction, so it rests on the model score alone, which may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cholecystitis, low phospholipid associated cholelithiasis, pyelonephritis (relations recorded in the knowledge graph; the licence records contain no approved indication text) |
| Predicted New Indication | Hepatoportal sclerosis |
| TxGNN Prediction Score | 0.9900 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | at least 20 |
| Number of Approvals | At least 20 registrations (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Doripenem is a carbapenem antibiotic, a class that works by inhibiting bacterial cell wall synthesis. Its use in the biliary and urinary tract infections recorded in the knowledge graph fits that antibacterial action.

Hepatoportal sclerosis is a non-infectious vascular disorder of the liver that causes noncirrhotic portal hypertension. Nothing in the data compiled for this report supports a mechanistic link between an antibacterial agent and this disease. The high score (0.9900) comes from the TxGNN model (deep learning). It may reflect similarities the model learned between related diseases, such as the hepatobiliary original indications (cholecystitis, cholelithiasis), not biological evidence, and it has not been biologically validated.

The same score of 0.9900 was also given by the TxGNN model to four other liver-related conditions: hepatopulmonary syndrome, idiopathic copper-associated cirrhosis, early-onset familial noncirrhotic portal hypertension and primitive portal vein thrombosis. Each of them has no trials, no literature and no supported mechanistic link. The identical scores may reflect similarities the model learned between related diseases rather than disease-specific signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

At least 20 single-ingredient injectable registrations are listed, all valid. The list may be partial. No approved indication text is recorded in the licence data. Five main registrations are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 65614 | Dori 500mg Injection | Vial of 1 injection | Not recorded |
| 69040 | Doriray 500mg Injection | Vial of 1 injection | Not recorded |
| 112816 | Inarem 250mg Injection | Vial of 1 injection | Not recorded |
| 62869 | Dorilon 500mg Injection | Vial of 1 injection | Not recorded |
| 158086 | Nozodor 500mg Injection | Vial of 1 ml injection | Not recorded |

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: Doripenem is linked to *Clostridium difficile* colitis, perinatal necrotizing enterocolitis and impaired renal function disease as contraindication relations.
- **Drug Interactions**: Four moderate-level interactions are listed: picosulfuric acid, ethinylestradiol, mycophenolic acid and pemetrexed.

For full warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications, and no plausible mechanism links a carbapenem antibiotic to hepatoportal sclerosis. The evidence level is L5, so it is a model prediction only.

**To proceed, the following is needed:**
- Mechanism of action data and a testable biological hypothesis connecting doripenem to hepatoportal sclerosis
- A systematic literature search for any direct clinical or preclinical studies in this disease
- Package insert warnings and contraindications from Indian regulatory sources
- Evidence that the score reflects more than the similarities the TxGNN model (deep learning) learned between related hepatobiliary diseases
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

