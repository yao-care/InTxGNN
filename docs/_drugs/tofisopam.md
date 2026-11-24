---
layout: default
title: Tofisopam
parent: Model Prediction Only (L5)
nav_order: 843
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Tofisopam: predicted new indication insomnia (evidence level L5). Approved use: Not recorded in the compiled data"
monitor_inn: "Tofisopam"
drugbank_id: DB08811
predicted_indications: ["insomnia (disease)"]
---

# Tofisopam
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

## Tofisopam: Predicted New Indication Insomnia (Original Indication Not Recorded in Data)
{: .text-alpha }

## One-Sentence Summary

Tofisopam is a single-ingredient oral tablet marketed in India, but the data compiled for this report do not record its approved indication.
The TxGNN model predicts it may be effective for **insomnia**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction is therefore model-derived only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the compiled data (all license entries have empty indication text) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 0.9916 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (11 of 11) – CDSCO approval status is not included in this data |
| Number of Listed Products | 11 (valid: 11) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. The compiled data record neither a mechanism nor an approved indication for tofisopam, so a mechanistic link to insomnia cannot be verified from the available information.

From general pharmacology (outside the compiled data, to be verified), tofisopam is a 2,3-benzodiazepine that does not act through classical GABA-A benzodiazepine-site agonism. It is generally described as non-sedating, anxiolytic and activating. That profile argues against a straightforward hypnotic effect.

The high score of 0.9916 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as other benzodiazepines, not biological evidence. No pathway-level support is available.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

All 11 registrations are valid single-ingredient oral tablets (strips of 10 tablets). Approved indication text is not recorded for any of them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 150675 | Nextril 50 Tablet | Strip of 10 tablets | Valid |
| 152030 | Nextril 100mg Tablet | Strip of 10 tablets | Valid |
| 214929 | Toficalm 50 Tablet | Strip of 10 tablets | Valid |
| 215517 | Toficalm 100 Tablet | Strip of 10 tablets | Valid |
| 215998 | Tofisern 50mg Tablet | Strip of 10 tablets | Valid |
| 216609 | Tolrina 50mg Tablet | Strip of 10 tablets | Valid |
| 217663 | Tofisern 100mg Tablet | Strip of 10 tablets | Valid |
| 217884 | Tofiryd 50 Tablet | Strip of 10 tablets | Valid |
| 217889 | Tolrina 100mg Tablet | Strip of 10 tablets | Valid |
| 218347 | Tofypeace 50 Tablet | Strip of 10 tablets | Valid |
| 224070 | Tofiryd 100 Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or publications. The available pharmacology also suggests that a non-sedating, activating profile is not consistent with a hypnotic effect. Safety information and the approved indication are missing as well.

**To proceed, the following is needed:**
- The package insert from the India regulatory source, to confirm the approved indication, warnings and contraindications
- Mechanism of action data (for example from DrugBank) to test whether any plausible link to sleep regulation exists
- A targeted search of trials and literature on tofisopam in insomnia and sleep outcomes
- Preclinical or exploratory clinical data on sleep effects before reconsidering the decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

