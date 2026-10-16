---
layout: default
title: Domperidone
parent: Model Prediction Only (L5)
nav_order: 282
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Domperidone: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Dyspepsia, heartburn, epigastric pain, nausea and vomiting"
---

# Domperidone
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

# Domperidone: From Upper Gastrointestinal Symptom Management to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Domperidone is a peripheral dopamine D2/D3 receptor antagonist used to manage dyspepsia, heartburn, epigastric pain, nausea and vomiting.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**,
but **no clinical trials and no publications** currently support this direction; it is a model-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dyspepsia, heartburn, epigastric pain, nausea and vomiting (from general pharmacology information; the approved indication text in the India licences is blank) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled record. Based on known pharmacology, domperidone is a peripheral antagonist of dopamine D2 and D3 receptors (DRD2, DRD3). Its antiemetic and gastric prokinetic effects in dyspepsia and nausea are related to this action.

NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor gene (AVPR2). The mutated receptor is constitutively active, so the kidney retains water independently of arginine vasopressin. The data compiled for this report do not show a mechanistic link between dopamine D2/D3 blockade and this pathway. A plausible connection would require an effect on V2 receptor signalling or on water handling in the collecting duct, and nothing in the data supports that.

The very high TxGNN score is best read as a network-proximity signal. It may reflect shared associations with water balance, hyponatraemia or dopamine–vasopressin interactions, not a validated pharmacological mechanism. A D2/D3 antagonist would not be expected to correct a constitutively active V2 receptor. Domperidone is also known to cause hyperprolactinaemia and QT prolongation, which are unrelated to NSIAD pathophysiology.

## India Market Information

Domperidone is marketed in India, with 20 valid single-ingredient registrations and no cancelled ones. The approved indication text is blank in all of them. Five representative authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 80122 | Esomne-DSR Capsule | Strip of 10 sustained-release capsules | Not stated |
| 181124 | Pantar DM 10mg/40mg Tablet | Strip of 10 tablets | Not stated |
| 80235 | Esorna D 30mg/40mg Capsule SR | Strip of 10 sustained-release capsules | Not stated |
| 177565 | Pantif-DSR Capsule | Strip of 10 sustained-release capsules | Not stated |
| 179889 | Petu D 10mg/40mg Tablet | Strip of 10 tablets | Not stated |

All registered forms are oral (tablets, capsules and sustained-release capsules).

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: long QT syndrome, familial long QT syndrome, torsades de pointes, liver disease, gallbladder disease. These come from drug–disease contraindication links in the TxGNN knowledge graph and should be confirmed against the product labelling.
- **Drug Interactions**: The interaction query completed, but it returned only pharmacological target entries, not drug–drug interactions. These are the dopamine D2 receptor (DRD2) and D3 receptor (DRD3), which are domperidone's primary targets.
- **Other known risks**: Domperidone is known to cause QT prolongation and hyperprolactinaemia. Its benefit-risk balance has been under review by the European Medicines Agency (reported in March 2013).

Package insert warnings and contraindications for the Indian products have not been obtained. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no publications and no supported mechanism linking D2/D3 antagonism to the constitutively active V2 receptor in NSIAD. The knowledge graph also flags QT-related and hepatic concerns, and the Indian package insert safety data are still missing.

**To proceed, the following is needed:**
- Mechanism of action data for domperidone, and a mechanistic rationale connecting D2/D3 blockade (or another action) to V2 receptor signalling or collecting-duct water handling
- Package insert warnings and contraindications for the Indian products
- Approved indication text for the Indian licences
- Preclinical or literature evidence in NSIAD or related disorders of water balance
- A QT and cardiac risk assessment for the proposed patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

