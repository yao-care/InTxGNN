---
layout: default
title: Salbutamol
parent: Model Prediction Only (L5)
nav_order: 761
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
monitor_inn: "Salbutamol"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture"]
description: "Salbutamol: predicted new indication Papillary conjunctivitis (evidence level L5). In India: at least 20 listed products"
---

# Salbutamol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Salbutamol: Papillary conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Salbutamol is a short-acting beta-2 adrenergic agonist (bronchodilator) that is widely marketed in India.
The TxGNN model predicts it may be relevant for **papillary conjunctivitis**, with a score of 0.9999.
However, **no clinical trials and no publications** were found for this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for salbutamol: "Albuterol sulfate is a beta 2 -adrenergic agonist. The pharmacologic effects of albuterol sulfate are attributable to activation of beta 2 -adrenergic receptors on airway smooth muscle. Activation of beta 2 -adrenergic receptors leads to the activation of adenylcyclase and to an increase in the intracellular concentration of cyclic-3', 5’-adenosine monophosphate (cyclic AMP)." ([DailyMed: Albuterol Sulfate Inhalation (albuterol sulfate) prescribing information, Amneal Pharmaceuticals NY LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e449282-ee58-4e36-b983-85c4e6f0864d), label version 2024-12-20; accessed 2026-11-19.) Salbutamol is known as a beta-2 adrenergic agonist, a class that relaxes airway smooth muscle.

Beta-2 agonists have shown some anti-inflammatory and mast-cell-stabilizing effects in the conjunctiva in preclinical models. This offers a loose biological reason why an allergic or inflammatory eye condition could be a plausible target. However, there is no direct support for papillary conjunctivitis itself: no trials, no publications, and no preclinical work specific to this disease. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Salbutamol is marketed in India. The data compiled for this report lists 20 valid registrations and no cancelled ones. The list may be partial. Several of the products below carry salbutamol together with other ingredients in their trade names, so the entries do not describe single-ingredient salbutamol approval. Approved indication text is not recorded for these entries.

<!-- review:begin in-lic-20261124c-salbutamol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The data compiled for this report lists 20 valid single-ingredient registrations and no cancelled ones." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-salbutamol-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 26 | Asthalin 100mcg Inhaler | Packet of 200 MDI Inhaler | Valid |
| 237 | Asthalin Respirator Solution | Bottle of 15 ml Solution for inhalation | Valid |
| 5045 | Astharid 2mg Tablet | Strip of 10 tablets | Valid |
| 5199 | Asthacure Plus Syrup | Bottle of 60 ml Syrup | Valid |
| 6918 | Asthavent-BR Syrup | Bottle of 100 ml Syrup | Valid |
| 7563 | Aerotide Forte 400mcg/200mcg Diskette | Packet of 8 inhaler | Valid |
| 10026 | Aerotide 200 mcg/100 mcg Inhaler | Packet of 1 Inhaler | Valid |
| 26954 | Bromosal Syrup | Bottle of 100 ml Syrup | Valid |
| 33151 | Bros Expectorant | Bottle of 60 ml Expectorant | Valid |
| 38713 | Combimist 2.5mg/500mg Respules | Strip of 1 ml Respules | Valid |
| 45636 | Combimist 200mg/40mcg Respicap | Bottle of 30 respicaps | Valid |
| 52644 | Cyvent 2mg/10mg Tablet | Strip of 10 tablets | Valid |
| 138786 | Megavent Tablet | Strip of 10 tablets | Valid |
| 152359 | Nova Ventiphylline Forte Tablet | Strip of 10 tablets | Valid |
| 210597 | Salbusun 2mg Tablet | Strip of 10 tablets | Valid |
| 233983 | Ventirex-Plus Syrup | Bottle of 100 ml Syrup | Valid |
| 234023 | Ventiphylline Syrup | Bottle of 100 ml Syrup | Valid |
| 234871 | Ventipra MDI 100 mcg/20 mcg Inhaler | Packet of 200 MDI Inhaler | Valid |
| 237125 | Vent ET 2mg/100mg Tablet | Strip of 10 tablets | Valid |
| 251522 | Zefin 2mg/8mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications / cautions to review**: Disease associations recorded for this drug include hypertension, long QT syndrome, epilepsy, potassium deficiency, diabetes mellitus, diabetic ketoacidosis, metabolic acidosis, benign prostatic hyperplasia, ocular hypertension, angle-closure glaucoma, hyperthyroidism (including Graves disease and thyrotoxicosis), bladder neck obstruction, myocardial ischemia, coronary artery disease, sudden cardiac arrest and heart conduction disease. These are not taken from label text and should be checked against the package insert.
- **Drug Interactions**: 754 interactions are recorded. Examples include moderate-level interactions with acarbose, famotidine, epinephrine, clarithromycin, cisapride, canagliflozin, dapagliflozin, alogliptin and chlorpropamide (glucose-lowering drugs and QT-active drugs are of particular note), and minor interactions with corticosteroids such as hydrocortisone, budesonide, dexamethasone and betamethasone.

Package insert warnings were not available, so the label should be reviewed before any further work.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score (0.9999) but no trials, no literature and no disease-specific mechanistic data, so the evidence level is L5.

**To proceed, the following is needed:**
- Disease-specific preclinical or clinical evidence for salbutamol in papillary conjunctivitis
- Mechanism-of-action data
- Package insert warnings and contraindications
- A suitable ocular formulation and route assessment, since the marketed forms are oral and inhaled products
- Review of the systemic cardiovascular and metabolic safety signals listed above

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Albuterol Sulfate Inhalation (albuterol sulfate) prescribing information, Amneal Pharmaceuticals NY LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2e449282-ee58-4e36-b983-85c4e6f0864d) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

