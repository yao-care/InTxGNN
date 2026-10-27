---
layout: default
title: Isoprenaline
parent: Model Prediction Only (L5)
nav_order: 450
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Isoprenaline: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Common cold, nasopharyngitis, cardiac arrest, atrioventricular block"
monitor_inn: "Isoprenaline"
predicted_indications: ["nasal cavity disease", "headache disorder", "pharyngitis", "acute laryngopharyngitis", "trigeminal autonomic cephalalgia", "bronchial disease", "endobronchial leiomyoma", "allergic urticaria", "endobronchial lipoma", "bronchus adenoma"]
---

# Isoprenaline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Isoprenaline: From Common Cold and Cardiac Conditions to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Isoprenaline is a non-selective beta-adrenergic agonist, originally associated with common cold, nasopharyngitis, cardiac arrest and atrioventricular block.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are currently **0 clinical trials** and only **1 publication** (an unrelated case report) behind this prediction.
The evidence is model-prediction only, so this prediction should be treated as a hypothesis, not a finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Common cold, nasopharyngitis, cardiac arrest, atrioventricular block (from the knowledge graph; the approved indication text in the India licenses is empty) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, isoprenaline is a non-selective beta-adrenergic agonist. In theory, beta-2 stimulation could influence nasal vascular tone and mucosal secretion.

The knowledge graph links isoprenaline to upper respiratory conditions (common cold, nasopharyngitis). The high prediction score for nasal cavity disease probably reflects this network proximity, not an independent therapeutic rationale. No direct evidence supports a benefit in nasal disease.

The only retrieved paper describes coronary artery spasm and ventricular tachycardia after epinephrine-soaked nasal packing during intubation. It is not relevant to treating nasal disease.

Other predictions in the same analysis include **bronchial disease**, which has the strongest mechanistic plausibility (beta-2-mediated bronchodilation, historically an established use). However, isoprenaline was largely replaced by beta-2-selective agents because of cardiac beta-1 effects, so the added value is doubtful.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14711196](https://pubmed.ncbi.nlm.nih.gov/14711196/) | 2003 | Case report | Japanese Heart Journal | A 26-year-old man developed ventricular tachycardia after nasal epinephrine soaking and intubation; coronary artery spasm was found. Not relevant to treating nasal disease. |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 107860 | Isolin 2mg Injection | Vial of 1 ml injection | Not stated |
| Registration No. 179288 | Pacemak 2mg Injection | Vial of 1 ml injection | Not stated |
| Registration No. 109672 | Isuprin 2mg Injection | Vial of 1 ml injection | Not stated |

All three licences are valid single-ingredient injectable products. Only an injectable form is registered, which is a poor route match for a nasal condition.

---

## Safety Considerations

- **Contraindications (from knowledge-graph disease associations, not label text):** hypertension, diabetes mellitus, diabetic ketoacidosis, coronary artery disease, myocardial infarction, coronary thrombosis, hemoglobinopathy, hyperthyroidism, Graves disease, thyrotoxicosis.
- **Drug Interactions:** 367 interactions were recorded. Examples:
  - **Major:** dolasetron
  - **Moderate:** epinephrine, isometheptene, diethylpropion, clarithromycin, famotidine, and several antidiabetic agents (acarbose, alogliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, albiglutide, dulaglutide)
  - **Minor:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone, beclomethasone)

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no clinical trials, and the single paper is unrelated. The only available route is injectable, and the cardiovascular profile (tachycardia, arrhythmia risk) argues against use for a non-cardiac nasal condition.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanistic rationale specific to nasal disease
- Package insert warnings and contraindications from the India product labels (needed for safety screening)
- Preclinical or clinical studies of isoprenaline in nasal disease
- An assessment of route compatibility (a nasal or topical formulation does not exist in the registered products)
- Consideration of better-supported predictions, such as bronchial disease, though this would largely revisit a superseded use compared with selective beta-2 agonists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

