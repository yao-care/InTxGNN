---
layout: default
title: Minodronic Acid
parent: Model Prediction Only (L5)
nav_order: 557
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
monitor_inn: "Minodronic acid"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "severe nonproliferative diabetic retinopathy", "bone Paget disease", "fetal and neonatal alloimmune thrombocytopenia", "juvenile Paget disease"]
description: "Minodronic Acid: predicted new indication Pseudo-von Willebrand disease (evidence level L5). In India: 2 listed products (2 not discontinued)"
---

# Minodronic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Minodronic Acid: Pseudo-von Willebrand disease
{: .text-alpha }

## One-Sentence Summary

Minodronic acid is a nitrogen-containing bisphosphonate, originally used to treat osteoporosis and postmenopausal osteoporosis.
The TxGNN model's top-ranked prediction is **pseudo-von Willebrand disease**, but **no clinical trials and no publications** were found to support it. This is a computational prediction only.
Among all seven predictions, **bone Paget disease** is the most biologically credible candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pseudo-von Willebrand disease |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (2 of 2) – CDSCO approval status is not included in this data |
| Number of Listed Products | 2 (valid: 2) |
| Recommended Decision | Hold |

**Other predicted indications**

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 1 | Pseudo-von Willebrand disease | 0.9997 | L5 | Hold |
| 2 | Primary release disorder of platelets | 0.9997 | L5 | Hold |
| 3 | Glanzmann thrombasthenia | 0.9987 | L5 | Hold |
| 4 | Severe nonproliferative diabetic retinopathy | 0.9958 | L5 | Hold |
| 5 | Bone Paget disease | 0.9932 | L5 | Research Question |
| 6 | Fetal and neonatal alloimmune thrombocytopenia | 0.9919 | L5 | Hold |
| 7 | Juvenile Paget disease | 0.9915 | L5 | Research Question |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of minodronic acid as: Farnesyl diphosphate synthase inhibitor ([ChEMBL CHEMBL319144 (minodronic acid): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL319144), CC BY-SA 3.0; accessed 2026-11-19.) Based on general pharmacology, minodronic acid is a nitrogen-containing bisphosphonate. It inhibits farnesyl pyrophosphate synthase in osteoclasts, which reduces bone resorption. This is why it works in osteoporosis.

For the top-ranked prediction, **pseudo-von Willebrand disease**, no plausible mechanistic link has been established. That disorder involves platelet GPIb-alpha hyperreactivity and abnormal von Willebrand factor binding, which have no known connection to bisphosphonate pharmacology. The same applies to primary release disorder of platelets (a granule secretion defect) and Glanzmann thrombasthenia (a loss-of-function defect of integrin alphaIIb-beta3). A bisphosphonate would not be expected to correct either. The high TxGNN scores for these conditions should be treated with caution.

The predictions with a more reasonable biological basis are the two Paget diseases:
- **Bone Paget disease** involves excessive osteoclast-mediated bone resorption. Nitrogen-containing bisphosphonates such as zoledronate and risedronate are established treatments, and minodronic acid shares the same class mechanism.
- **Juvenile Paget disease** is a rare genetic disorder (for example, OPG deficiency) with high bone turnover. Antiresorptive therapy has been used in related conditions. Paediatric safety would need dedicated evaluation.

Severe nonproliferative diabetic retinopathy might have an indirect link through anti-inflammatory or anti-angiogenic effects of this drug class, but this is unvalidated. Fetal and neonatal alloimmune thrombocytopenia is caused by maternal alloantibodies and has no apparent link to bisphosphonates. Bisphosphonates also cross the placenta and accumulate in bone, so pregnancy safety is a concern.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 143849 | Minodrone Capsule | Strip of 1 Capsule | Valid |
| 146747 | Minoshine-M Soft Gelatin Capsule | Strip of 1 Soft Gelatin Capsule | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

Both products are single-ingredient oral formulations from Pharmanova India Drugs Pvt Ltd, and both licences are currently valid.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the data compiled for this report, and no disease contraindications were recorded in the knowledge graph.

For the fetal and neonatal alloimmune thrombocytopenia prediction, pregnancy safety requires particular attention, since bisphosphonates cross the placenta and accumulate in bone.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predictions (pseudo-von Willebrand disease, primary release disorder of platelets, Glanzmann thrombasthenia) rest only on model scores, with no clinical or literature evidence and no plausible mechanism. Bone Paget disease and juvenile Paget disease are biologically reasonable and are worth investigating as research questions, but no minodronic acid data are available for them yet.

**To proceed, the following is needed:**
- Download and parse the India package insert for warnings and contraindications (a blocking gap for safety screening)
- Obtain mechanism of action data from DrugBank
- A dedicated literature and trial search for minodronic acid in bone Paget disease, including class-level bisphosphonate evidence, which may support an upgrade to L4
- Paediatric safety evaluation before any consideration of juvenile Paget disease
- Confirmation of the approved indications for the two India licences, since the indication text is blank

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data for this drug is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL319144 (minodronic acid): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL319144) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

