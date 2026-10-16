---
layout: default
title: Adapalene
parent: Model Prediction Only (L5)
nav_order: 26
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Adapalene: predicted new indication Zinc, elevated plasma (evidence level L5). Approved use: Acne"
---

# Adapalene
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Adapalene: From Acne to Elevated Plasma Zinc

## One-Sentence Summary

Adapalene is a topical retinoid originally used to treat acne.
The TxGNN model predicts it may be effective for **elevated plasma zinc**, but **no clinical trials and no publications** currently support this direction. The prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, adapalene is a topical retinoid that acts as a selective retinoic acid receptor (RAR-beta/gamma) agonist. Its efficacy in acne is established, but a mechanistic link to elevated plasma zinc has not been found.

Elevated plasma zinc is a laboratory finding or biochemical state rather than a conventional treatable disease. No known pathway connects retinoid receptor signalling to zinc homeostasis in a way that would lower plasma zinc. Topical adapalene also has low systemic exposure, which makes a systemic effect on plasma zinc even less likely.

The very high TxGNN score (0.995) is a model output only. It may reflect a knowledge-graph artifact, such as general retinoid–zinc associations in skin biology or shared gene-network neighbours. It should not be read as evidence of efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Twenty valid single-ingredient registrations are listed. The main five are shown below. All are topical gels, and no approved indication text is available in the data compiled for this report.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 217787 | Ticin Plus Gel | Tube of 20 gm gel | Torque Pharmaceuticals Pvt Ltd |
| 17264 | Adhibit Gel | Tube of 15 gm gel | Dupen Laboratories Pvt Ltd |
| 5953 | Aclene 0.10% Gel | Tube of 15 gm gel | Cipla Ltd |
| 12911 | Achilles 0.10% Gel | Tube of 15 gm gel | Novartis India Ltd |
| 14480 | Adene 0.1% Gel | Tube of 15 gm gel | Gary Pharmaceuticals Pvt Ltd |

---

## Safety Considerations

- **Disease associations flagged as contraindications in the knowledge graph** (not taken from label text): photoparoxysmal response, photosensitivity disease, exfoliative dermatitis, and dermatitis.
- **Drug Interactions:** 58 potential interactions were identified, but none has a severity level assigned. Examples include doxycycline, minocycline, tetracycline, metronidazole, prednisone, triamcinolone, budesonide, omeprazole, pantoprazole, ibuprofen, fluconazole, clopidogrel, and bupropion.

For full warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5). No trials or publications exist, and no plausible mechanism links a topical retinoid to lowering plasma zinc. The target is also a laboratory finding rather than a disease, and topical dosing gives low systemic exposure.

**To proceed, the following is needed:**
- Confirmation that elevated plasma zinc is a clinically meaningful therapeutic target
- Detailed mechanism of action data and any evidence linking retinoid signalling to zinc homeostasis
- Preclinical or exploratory studies showing an effect on plasma zinc
- Package insert warnings and contraindications from the India Pharma source, which are currently missing and block safety screening
- An assessment of route compatibility, since the topical gel formulations may not achieve relevant systemic exposure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

