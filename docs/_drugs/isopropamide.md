---
layout: default
title: Isopropamide
parent: Model Prediction Only (L5)
nav_order: 451
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Isopropamide: predicted new indication Gastroduodenitis (evidence level L5). Approved use: Peptic ulcer disease"
monitor_inn: "Isopropamide"
predicted_indications: ["gastroduodenitis", "overactive bladder (disease)"]
---

# Isopropamide
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

# Isopropamide: From Peptic Ulcer Disease to Gastroduodenitis

## One-Sentence Summary

Isopropamide is an antimuscarinic (anticholinergic) drug originally used to treat peptic ulcer disease.
The TxGNN model predicts it may be effective for **gastroduodenitis**,
but currently there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease (the licence records contain no indication text, so this comes from the knowledge-graph indication data) |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, isopropamide is a quaternary ammonium antimuscarinic agent. Its use in peptic ulcer disease is established, and mechanistically it may be applicable to gastroduodenitis.

Blocking muscarinic receptors can reduce gastric acid secretion and gastrointestinal motility and spasm. These effects are plausibly relevant to inflammatory conditions of the stomach and duodenum. Gastroduodenitis is also closely related to the approved use, peptic ulcer disease, since both affect the same part of the upper gastrointestinal tract.

This link is inferred from the drug class and has not been confirmed. The very high TxGNN score is likely driven by how close this disease is to the existing peptic ulcer indication.

**A second prediction** is overactive bladder (score 99.88%). Antimuscarinics are an established class for this condition, because they reduce involuntary bladder muscle contractions. However, isopropamide is a quaternary ammonium compound with limited tissue penetration, and no bladder-specific data are available. It would also need to be compared against better-characterised approved antimuscarinics such as oxybutynin, tolterodine and solifenacin. It also has no supporting trials or literature and is rated L5 / Hold.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 201096 | Stelabid 5mg/1mg Tablet | Strip of 10 tablets | Not specified |
| 199806 | Stelbid Tablet | Strip of 10 tablets | Not specified |
| 202024 | Stelbid 5mg/2mg Tablet | Strip of 10 tablets | Not specified |
| 202131 | Spascol 5mg/1mg Tablet | Strip of 10 tablets | Not specified |
| 96257 | Gastobid Tablet | Strip of 10 tablets | Not specified |

All 6 registrations are valid single-ingredient entries (the table lists the first 5). The remaining registration is Stelbid 2 Tablet (200066). All are oral tablets.

## Safety Considerations

- **Conditions flagged in the knowledge graph as contraindications** (from drug-disease relationships in the TxGNN knowledge graph, not from package insert text):
  - Cardiovascular: hypertension, orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy, long QT syndrome (including familial), torsades de pointes, coronary artery disease, myocardial infarction, coronary thrombosis
  - Neurological: epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm
  - Gastrointestinal, hepatic and renal: gastric ulcer, kidney disease, pyoureter, liver disease, gallbladder disease
  - Haematological: thrombocytopenia, neutropenia, agranulocytosis
  - Other: hyperglycaemia, benign prostatic hyperplasia, obesity disorders (including monogenic obesity), substance abuse/dependence, female breast carcinoma
- **Class-related adverse effects** to consider: dry mouth, constipation, urinary retention, and cognitive effects.

Please refer to the package insert for label-based warnings, contraindications and drug interaction information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score and class-level mechanistic reasoning. No clinical trials or publications support it, and neither label-based safety data nor mechanism of action data are available. Gastroduodenitis is closely related to the approved peptic ulcer use, which makes the prediction plausible but not yet evidence-backed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator, to enable safety screening
- Detailed mechanism of action data (for example from DrugBank)
- Clinical or observational evidence for gastroduodenitis (trials or literature)
- Approved indication text for the registered products
- Route and dosing compatibility assessment for the new indication
- For overactive bladder, a comparison against approved antimuscarinics and an assessment of tissue penetration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

