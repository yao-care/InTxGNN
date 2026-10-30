---
layout: default
title: Fexofenadine
parent: Model Prediction Only (L5)
nav_order: 351
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Fexofenadine: predicted new indication Rosacea conjunctivitis (evidence level L5). Approved use: Allergic rhinitis (also vasomotor rhinitis, atopic…"
monitor_inn: "Fexofenadine"
predicted_indications: ["rosacea conjunctivitis"]
---

# Fexofenadine
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

## Fexofenadine: From Allergic Rhinitis to Rosacea Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Fexofenadine is a peripheral H1-receptor antagonist (antihistamine), originally used for allergic rhinitis, allergic conjunctivitis and idiopathic urticaria.
The TxGNN model predicts it may be effective for **rosacea conjunctivitis**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (also vasomotor rhinitis, atopic, papillary and vernal conjunctivitis, idiopathic urticaria) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, fexofenadine is a selective peripheral H1-receptor antagonist. Its efficacy in allergic and other forms of conjunctivitis is already recognised, and it may be mechanistically applicable to rosacea conjunctivitis.

The plausible link is symptomatic. H1 blockade could relieve histamine-mediated ocular itching, redness and hyperaemia that may accompany ocular rosacea. Fexofenadine is also not antimuscarinic, so it does not cause the tear-film drying seen with first-generation antihistamines.

The link is weak, however. Ocular rosacea is driven mainly by meibomian gland dysfunction, tear-film instability, bacterial or *Demodex*-related inflammation and neurovascular dysregulation. Antihistamines are not an established treatment for these mechanisms, and oral fexofenadine has no anti-inflammatory or antimicrobial action relevant to them. Any benefit would probably be limited to relieving an allergic-like component. The very high TxGNN score is a computational prediction and not clinical evidence.

## India Market Information

Fexofenadine has 20 valid single-ingredient registrations in India, all oral tablets. The approved indication text is not available for these registrations. The first five are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 90925 | Faxodas 120mg Tablet | Strip of 6 tablets | Shreya Life Sciences Pvt Ltd |
| 93422 | Fextree 120mg Tablet | Strip of 10 tablets | Apa Pharmaceuticals |
| 11102 | Alfexo 120mg Tablet | Strip of 10 tablets | Ernst Pharmacia |
| 85706 | Fexor 180mg Tablet | Strip of 10 tablets | Orphic Pharma (India) Ltd |
| 92135 | Fexosep 120 Tablet | Strip of 10 tablets | Sepik Life Sciences |

## Safety Considerations

- **Contraindications (from the TxGNN model (deep learning), not label text; may reflect similarities the model learned between related diseases, not biological evidence)**: The model links fexofenadine with caution in the following conditions:
  - Cardiovascular: hypertension and hypertensive disorder; coronary artery disease, coronary atherosclerosis, arteriosclerosis and atherosclerosis.
  - Metabolic and endocrine: diabetes mellitus and diabetic ketoacidosis; hyperthyroidism, Graves disease and thyrotoxicosis.
  - Renal, urinary and ocular: kidney disease and pyoureter; benign prostatic hyperplasia; angle-closure (closed-angle) glaucoma.
- **Drug Interactions**: 473 interactions are recorded. Examples classed as **Moderate**:
  - Antacids: magnesium hydroxide, aluminum hydroxide, magaldrate and magnesium carbonate.
  - Other drugs: eliglustat, eluxadoline and rolapitant.

  Examples classed as **Minor** are clarithromycin, miconazole and clotrimazole. Several other interactions (for example cimetidine, famotidine, epinephrine and doxycycline) have no assigned severity level.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications (Evidence Level L5). The mechanistic link is limited to symptomatic itch and redness relief, and antihistamines do not address the main causes of ocular rosacea.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma source, which are required before safety screening
- Mechanism of action data from DrugBank
- A literature and trial search on antihistamines in ocular rosacea, to find any real-world or preclinical support
- A review of route compatibility, since the predicted indication may favour topical ocular delivery and only oral tablets are registered in India
- Early-stage studies, for example of symptom relief in ocular rosacea patients with an allergic component, before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

