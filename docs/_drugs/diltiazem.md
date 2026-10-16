---
layout: default
title: Diltiazem
parent: Model Prediction Only (L5)
nav_order: 270
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Diltiazem: predicted new indication Obsolete susceptibility to ischemic stroke (evidence level L5). Approved use: Hypertension, atrial fibrillation, Prinzmetal angina…"
monitor_inn: "Diltiazem"
predicted_indications: ["obsolete susceptibility to ischemic stroke"]
---

# Diltiazem
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

# Diltiazem: From Hypertension and Cardiac Arrhythmias to Susceptibility to Ischemic Stroke

## One-Sentence Summary

Diltiazem is a calcium channel blocker originally used for hypertension, atrial fibrillation, Prinzmetal angina and ventricular tachycardia.
The TxGNN model predicts it may be relevant to **susceptibility to ischemic stroke** (an obsolete ontology term),
but **no clinical trials or publications** currently support this direction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, atrial fibrillation, Prinzmetal angina, ventricular tachycardia (from the knowledge graph; no approved indication text is available from Indian licences) |
| Predicted New Indication | Obsolete susceptibility to ischemic stroke |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, diltiazem is a non-dihydropyridine calcium channel blocker, its efficacy in hypertension and cardiac rhythm disorders is established, and mechanistically it may be applicable to stroke risk reduction.

A plausible link runs through blood pressure lowering and vasodilation, since hypertension is a major risk factor for ischemic stroke. Effects on vascular smooth muscle, including a possible role in cerebral vasospasm, are also conceivable.

However, the prediction cannot be tied to a specific, verifiable mechanism. The predicted disease term is flagged as "obsolete", suggesting a deprecated ontology entry that may map poorly to a current clinical entity. It is also a susceptibility concept rather than a treatable disease state, so it is unclear whether a clinical indication would mean primary prevention or acute treatment.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

All 20 registrations are valid single-ingredient products. The registration records contain no approved indication text. The five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 112106 | Ionozem CD 120mg Tablet | Strip of 10 tablets | Pfizer Ltd |
| 183456 | Q-DIL 90MG TABLET | Strip of 10 tablets | Aurobindo Pharma Ltd |
| 69353 | Diltime 30mg Tablet | Strip of 10 tablets | Zydus Cadila |
| 64863 | Dilcardia 90mg Tablet SR | Strip of 10 SR tablets | J B Chemicals and Pharmaceuticals Ltd |
| 37885 | Channel 60mg Tablet | Strip of 10 tablets | Micro Labs Ltd |

All products are oral formulations (tablets, capsules, and modified-, controlled- or sustained-release forms).

## Safety Considerations

- **Contraindications / risk conditions (knowledge-graph data, not label text)**: Associations include aortic stenosis, hypertrophic cardiomyopathy, hypotensive disorders, atrioventricular block, sick sinus syndrome, Wolff-Parkinson-White syndrome and Lown-Ganong-Levine syndrome, and ventricular tachycardia. Other recorded associations are kidney disease, liver disease, angioedema (including hereditary forms), neutropenia and agranulocytosis. These should be verified against the product label.
- **Drug Interactions**: 369 interactions were recorded. The listed ones are mostly Moderate, including corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), pioglitazone, bupropion, aprepitant, morphine, aspirin, canagliflozin and various calcium salts. **Loperamide is a Major interaction.**

Please also refer to the package insert for full warnings, as label-based safety data was not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high model score (99.08%) with no clinical trials or literature. The predicted disease term is obsolete and not a well-defined treatable condition, so a clinical development path cannot yet be defined.

**To proceed, the following is needed:**
- Clarify which current disease entity the obsolete term maps to, and define the intended use (primary prevention versus acute treatment)
- Detailed mechanism of action data (MOA) from DrugBank
- Package insert warnings and contraindications from Indian regulatory sources
- A literature and trial search on diltiazem in stroke prevention or cerebrovascular outcomes
- Assessment of whether the predicted indication is compatible with the available oral formulations and with the cardiac conduction and blood pressure risks noted above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

