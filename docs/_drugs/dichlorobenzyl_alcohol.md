---
layout: default
title: Dichlorobenzyl Alcohol
parent: Model Prediction Only (L5)
nav_order: 261
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
description: "Dichlorobenzyl Alcohol: predicted new indication Bronchitis (evidence level L5). Approved use: Not stated in the approval records (marketed as cough/throat lozenges)"
monitor_inn: "Dichlorobenzyl alcohol"
predicted_indications: ["bronchitis", "migraine disorder"]
---

# Dichlorobenzyl Alcohol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Dichlorobenzyl Alcohol: From Oropharyngeal Antiseptic Use to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Dichlorobenzyl alcohol is a mild antiseptic marketed in India as a throat lozenge ingredient.
The TxGNN model predicts it may be effective for **bronchitis**, but the data compiled for this report contain **no clinical trials** and **no supporting publications** for this prediction.
The prediction is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the approval records (marketed as cough/throat lozenges) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9921 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (4 of 4) – CDSCO approval status is not included in this data |
| Number of Listed Products | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dichlorobenzyl alcohol is a mild topical antiseptic typically used in throat lozenges for oropharyngeal infections. Its action is presumably local antiseptic activity against oral and pharyngeal pathogens, which is an unverified assumption.

Bronchitis is a respiratory tract condition and is related to the throat and cough settings in which the product is sold. However, a lozenge acts locally in the mouth and throat, and there is no data showing that this activity extends to the bronchi. The high score therefore comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

A second prediction, **migraine disorder** (score 0.9902), has no clinical trials, no literature, and no identified mechanistic link. It is not considered supported.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1036939](https://pubmed.ncbi.nlm.nih.gov/1036939/) | 1976 | Other (observational/case report) | Arzneimittel-Forschung | Reports elevated serum creatine kinase in 25 chronic bronchitis patients after oral clenbuterol, a different compound (a beta2-mimetic broncholytic). It does not address dichlorobenzyl alcohol and is **not** supporting evidence. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 1389 | Alkof Cough Lozenges Orange | Strip of 10 lozenges | Not stated |
| 87330 | Fastosil Lozenges Honey Lemon | Strip of 8 lozenges | Not stated |
| 87148 | Fastosil Lozenges Orange | Strip of 8 lozenges | Not stated |
| 5332 | Alkof Cough Lozenges Menthol | Strip of 10 lozenges | Not stated |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials, and the single publication retrieved concerns a different drug. A local lozenge antiseptic also has no established route to act on bronchial infection.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulatory source (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Evidence that a lozenge formulation or another route could reach the bronchial tissue
- Relevant clinical or preclinical studies of dichlorobenzyl alcohol in bronchitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

