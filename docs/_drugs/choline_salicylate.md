---
layout: default
title: Choline Salicylate
parent: Model Prediction Only (L5)
nav_order: 180
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-03
monitor_inn: "Choline salicylate"
predicted_indications: ["Prinzmetal angina", "hypertensive disorder", "migraine disorder", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "malignant renovascular hypertension", "Raynaud disease", "pulmonary hypertension"]
description: "Choline Salicylate: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not recorded in the local data"
---

# Choline Salicylate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Choline Salicylate: Prinzmetal angina
{: .text-alpha }

## One-Sentence Summary

Choline salicylate is a salicylate-class anti-inflammatory compound, marketed in India mainly as topical oral and dental gels and related oral products.
The TxGNN model predicts it for **Prinzmetal angina**, but there are **no clinical trials and no publications** supporting this direction, so the prediction remains a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. As a salicylate, it is generally expected to inhibit prostaglandin synthesis, which explains its anti-inflammatory and analgesic use.

No clear mechanistic link to Prinzmetal angina was identified. This condition is driven by coronary vasospasm, and its standard therapies are calcium channel blockers and nitrates. Salicylates are not established vasodilators, and high-dose NSAID-type drugs can have adverse cardiovascular or renal effects.

The high prediction score is therefore not backed by clinical or mechanistic evidence, and it should be read as a statistical association from the model rather than a reasoned therapeutic hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

The data compiled for this report list 20 valid single-ingredient licences, and none are cancelled. The records may be partial. The approved indication text is not recorded for any of them. The first 5 are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 26324 | B-Folcin Gel | Tube of 10 gm dental gel | Not specified |
| 230723 | Ulciwok Gel | Tube of 10 gm dental gel | Not specified |
| 63218 | Dentocare Liquid | Bottle of 15 ml liquid | Not specified |
| 200486 | Seleno Tablet | Strip of 10 tablets | Not specified |
| 236766 | Viloral Mouth Paint | Bottle of 20 ml paint | Not specified |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the interaction databases. Examples include:
  - Moderate: corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide), sulfonylurea antidiabetics (chlorpropamide, acetohexamide, glimepiride, glipizide, glyburide), insulins, antacids (aluminum hydroxide, calcium carbonate), activated charcoal, and fenfluramine/dexfenfluramine.
  - Minor: proton pump inhibitors (rabeprazole, dexlansoprazole).
- **Predicted-indication concern**: NSAID-class drugs can interfere with blood pressure control and renal perfusion, which matters for patients with cardiovascular disease.

Please refer to the package insert for warnings and contraindications, as none were available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score (0.9984) but no clinical trials, no publications and no plausible mechanistic link to coronary vasospasm. Evidence stays at L5.

**To proceed, the following is needed:**
- Mechanism of action data for choline salicylate
- Package insert warnings and contraindications from the India licences
- Any preclinical or clinical study directly addressing Prinzmetal angina
- A cardiovascular safety assessment, given the known effects of NSAID-class drugs on blood pressure and renal function

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

