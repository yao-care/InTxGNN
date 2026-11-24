---
layout: default
title: Phenylpropanolamine
parent: Model Prediction Only (L5)
nav_order: 666
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "Phenylpropanolamine"
predicted_indications: ["nasal cavity disease", "rosacea conjunctivitis", "faucial diphtheria", "cervical disc degenerative disorder"]
description: "Phenylpropanolamine: predicted new indication Nasal cavity disease (evidence level L5). In India: at least 20 listed products"
---

# Phenylpropanolamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Phenylpropanolamine: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Phenylpropanolamine is a sympathomimetic decongestant, originally used for allergic rhinitis, the common cold and related upper airway and conjunctival conditions.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but the support is thin: **no registered clinical trials** and only **3 publications** (one comparative clinical pharmacology study and two preclinical animal studies).
Its serious safety history (hemorrhagic stroke risk) calls for strong caution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, phenylpropanolamine is a direct- and indirect-acting sympathomimetic. It causes alpha-adrenergic vasoconstriction of nasal mucosal blood vessels, which reduces swelling and congestion.

Its original indications (allergic and vasomotor rhinitis, nasopharyngitis, the common cold) are largely nasal conditions. "Nasal cavity disease" is a broad category that overlaps heavily with them, so this prediction looks more like a natural extension of existing use than a truly new indication. The mechanism, reducing mucosal congestion, would plausibly apply across this category.

The other predictions are weaker:
- **Acute laryngopharyngitis** (0.9998) is a close extension of the existing pharyngitis indications, supported only by the model.
- **Rosacea conjunctivitis** (0.9919) could theoretically benefit from reduced redness, but its cause (chronic inflammation, meibomian gland dysfunction) is not addressed by a decongestant.
- **Faucial diphtheria** (0.9908) and **cervical disc degenerative disorder** (0.9903) have no plausible mechanistic link. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Comparative clinical pharmacology study | American Journal of Rhinology | Compared the oral and topical decongestant effects of phenylpropanolamine and d-pseudoephedrine, using acoustic rhinometry to measure changes in nasal cavity dimensions. |
| [10582118](https://pubmed.ncbi.nlm.nih.gov/10582118/) | 1999 | Preclinical (animal) | American Journal of Rhinology | Combined histamine H1 and H3 receptor blockade produced nasal decongestion in a cat model of nasal congestion. |
| [10582116](https://pubmed.ncbi.nlm.nih.gov/10582116/) | 1999 | Preclinical (animal) | American Journal of Rhinology | Described pressure and acoustic rhinometry for measuring nasal patency in a feline congestion model. |

---

## India Market Information

All 20 registrations are valid licences. The data contain no approved-indication text.

<!-- review:begin in-lic-20261124-phenylpropanolamine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All 20 registrations are valid single-ingredient licences." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-phenylpropanolamine-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 26876 | Biorex Syrup | Bottle of 100 ml Syrup | Valid |
| 37283 | Cetcof Syrup | Bottle of 60 ml Syrup | Valid |
| 37574 | Cuf Dex Syrup | Bottle of 100 ml Syrup | Valid |
| 41490 | Copod Syrup | Bottle of 100 ml Syrup | Valid |
| 46398 | Chericold Capsule | Strip of 10 capsules | Valid |
| 51573 | Coldy Syrup | Bottle of 100 ml Syrup | Valid |
| 62698 | Dexovik Syrup | Bottle of 100 ml Syrup | Valid |
| 77062 | Elcof Syrup | Bottle of 60 ml Syrup | Valid |
| 106495 | Histomonic DX Syrup | Bottle of 100 ml Syrup | Valid |
| 118607 | Kofnok Syrup | Bottle of 100 ml Syrup | Valid |
| 139709 | Medoryl CS Syrup | Bottle of 100 ml Syrup | Valid |
| 158687 | Numinic Tablet | Strip of 10 tablets | Valid |
| 178345 | Pricoff Syrup | Bottle of 100 ml Syrup | Valid |
| 203217 | Sneez Bye Syrup | Bottle of 60 ml Syrup | Valid |
| 219285 | Triatussic 12.5 mg/2 mg/10 mg Tablet | Strip of 10 tablets | Valid |
| 221647 | Triatussiccs Syrup | Bottle of 100 ml Syrup | Valid |
| 223808 | Tussiz P Syrup | Bottle of 60 ml Syrup | Valid |
| 223840 | Tritus Plus Suspension | Bottle of 50 ml Suspension | Valid |
| 229013 | Tritus 25 mg/4 mg/15 mg Suspension | Bottle of 50 ml Suspension | Valid |
| 247361 | Zeet Exp 25mg/8mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Cardiovascular and stroke risk**: Phenylpropanolamine has been withdrawn or restricted in many markets because of hemorrhagic stroke risk. Any repurposing would need strong guardrails.
- **Disease associations flagged in the knowledge graph** (not label text): hypertension and hypotensive disorders, liver failure and liver disease, kidney disease, epilepsy, insomnia, COPD, pancreatitis, gallbladder disease, thrombocytopenia, hypothyroidism, peptic ulcer disease, inflammatory bowel disease, benign prostatic hyperplasia, gout, substance abuse/dependence, and several blood and iron-metabolism disorders (sickle cell anemia, hemophilia, hemochromatosis, Wilson disease).
- **Drug interactions**: 176 interactions were identified. Major-level ones include **bupropion, lorcaserin, diethylpropion and phentermine**. Moderate-level ones include epinephrine, isometheptene, and several antidiabetic drugs (e.g., metformin, pioglitazone, empagliflozin, dapagliflozin, repaglinide, acarbose).

Package insert warnings and contraindications were not available, so please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is limited to one comparative pharmacology study and two animal studies, with no registered clinical trials. The nasal cavity prediction largely overlaps with existing rhinitis indications. The drug's stroke and cardiovascular risks are a major concern.

**To proceed, the following is needed:**
- Mechanism of action data
- Package insert warnings and contraindications for the India-marketed products
- Controlled clinical trial data in nasal cavity disease
- A benefit-risk assessment focused on hemorrhagic stroke and blood pressure effects, with a plan for excluding high-risk patients
- Approved indication text for the India licences, to clarify how far the prediction goes beyond current use

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Indian medicine data (the Indian Medicine Dataset used by this site). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

