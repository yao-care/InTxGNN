---
layout: default
title: Betaxolol
parent: Model Prediction Only (L5)
nav_order: 107
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Betaxolol: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Hypertension, open-angle glaucoma, ocular hypertension"
---

# Betaxolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Betaxolol: From Hypertension and Open-Angle Glaucoma to Primary Hereditary Glaucoma
{: .text-alpha }

## One-Sentence Summary

Betaxolol is a cardioselective beta-1 blocker originally used for hypertension, open-angle glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but **no clinical trials and no publications** were found in the data compiled for this report, so the prediction currently rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, open-angle glaucoma, ocular hypertension (the approved indication text on the Indian licences is blank) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available. Based on known information, betaxolol is a cardioselective beta-1 adrenergic antagonist. In the eye it lowers intraocular pressure (IOP) by reducing aqueous humour production. Its efficacy in open-angle glaucoma and ocular hypertension is established, so it may be mechanistically applicable to primary hereditary glaucoma, where raised IOP is also a main driver of optic nerve damage.

Some preclinical reports also describe neuroprotective effects (for example, calcium and sodium channel modulation), which could be relevant to glaucoma generally. This has not been confirmed for the predicted indication.

There are important limits to this reasoning:
- Primary hereditary glaucoma (for example, congenital or juvenile forms linked to MYOC or CYP1B1 variants) often arises from structural developmental defects of the trabecular meshwork or the drainage angle. Medical IOP lowering is therefore usually only adjunctive or a temporary measure before surgery.
- The very high TxGNN score most likely reflects how close this disease sits to the already approved glaucoma indications in the knowledge graph, rather than independent evidence.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 95232 | Glucoptic Eye Drop (Klar Sehen Pvt Ltd) | Packet of 5 ml eye drop | Not stated |
| 29999 | Betapress 0.5% Eye Drop (Micro Labs Ltd) | Packet of 5 ml eye drop | Not stated |
| 107898 | Iobet Eye Drop (FDC Ltd) | Bottle of 5 ml eye drop | Not stated |

All three are valid single-ingredient ophthalmic products. No oral formulation is registered in the data compiled for this report.

## Safety Considerations

Package insert warnings and contraindications were not available, so please refer to the package insert for those.

- **Disease contraindications flagged in the knowledge graph** (these come from drug-disease relationship data, not from label text, and need verification against the label):
  - Respiratory: asthma (including intrinsic and allergic asthma), pulmonary emphysema, bronchial disease
  - Cardiac: atrioventricular block and atrioventricular dissociation, heart cancer
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hypoglycaemia, phaeochromocytoma and other adrenal or sympathetic tumours
  - Neuromuscular: myasthenia gravis and neuromuscular junction disease
  - Organ disease: kidney disease, liver disease, gallbladder disease, pyoureter
  - Skin: psoriasis, parapsoriasis
  - Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder
  - Other tumours: duodenum cancer, small intestine cancer
- **Drug interactions**: 173 interactions were recorded. Those listed in the compiled data are mostly moderate and include epinephrine, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), atropine and hyoscyamine, bupropion, morphine, acetohexamide, and calcium salts. Minor interactions include acetylsalicylic acid, aluminium hydroxide and attapulgite.

The doses and routes relevant to the predicted indication have not been assessed, and the ophthalmic route is the only one registered in India.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no registered clinical trials or literature. The mechanism is plausible for IOP lowering, but hereditary glaucoma often needs surgery, so the likely benefit is adjunctive.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products (a blocking gap for safety screening)
- Detailed mechanism of action data (for example, from DrugBank)
- A systematic literature and trial search for betaxolol in congenital, juvenile or other hereditary glaucoma
- Clarification of the approved indication wording on the three Indian licences
- Assessment of route and formulation suitability, particularly for paediatric patients
- Review of the knowledge-graph contraindications against the label, especially respiratory, cardiac and diabetic risks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

