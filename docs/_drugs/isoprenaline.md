---
layout: default
title: Isoprenaline
parent: Model Prediction Only (L5)
nav_order: 450
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Isoprenaline"
predicted_indications: ["nasal cavity disease", "headache disorder", "pharyngitis", "acute laryngopharyngitis", "trigeminal autonomic cephalalgia", "bronchial disease", "endobronchial leiomyoma", "allergic urticaria", "endobronchial lipoma", "bronchus adenoma"]
description: "Isoprenaline: predicted new indication Nasal cavity disease (evidence level L5). In India: 3 listed products (3 not discontinued)"
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

## Isoprenaline: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Isoprenaline is a non-selective beta-adrenergic agonist, originally associated with common cold, nasopharyngitis, cardiac arrest and atrioventricular block.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are currently **0 clinical trials** and only **1 publication** (an unrelated case report) behind this prediction.
The evidence is model-prediction only, so this prediction should be treated as a hypothesis, not a finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (3 of 3) – CDSCO approval status is not included in this data |
| Number of Listed Products | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for isoprenaline: "Isoproterenol is a potent nonselective beta-adrenergic agonist with very low affinity for alpha‑adrenergic receptors." ([DailyMed: isoproterenol hydrochloride prescribing information, KVK-Tech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=051acbc2-7bf8-4059-e063-6394a90a115b), label version 2026-11-12; accessed 2026-11-19.) Based on known pharmacology, isoprenaline is a non-selective beta-adrenergic agonist. In theory, beta-2 stimulation could influence nasal vascular tone and mucosal secretion.

The high prediction score for nasal cavity disease comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No direct evidence supports a benefit in nasal disease.

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

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 107860 | Isolin 2mg Injection | Vial of 1 ml Injection | Valid |
| 109672 | Isuprin 2mg Injection | Vial of 1 ml Injection | Valid |
| 179288 | Pacemak 2mg Injection | Vial of 1 ml Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: isoproterenol hydrochloride prescribing information, KVK-Tech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=051acbc2-7bf8-4059-e063-6394a90a115b) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

