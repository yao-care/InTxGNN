---
layout: default
title: Empagliflozin
parent: Model Prediction Only (L5)
nav_order: 303
evidence_level: L5
indication_count: 3
monitor_inn: "Empagliflozin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia"]
last_modified_at: 2026-11-24
description: "Empagliflozin: predicted new indication Focal stiff limb syndrome (evidence level L5). In India: 20 listed products (20 not discontinued)"
---

# Empagliflozin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Empagliflozin: Focal stiff limb syndrome
{: .text-alpha }

## One-Sentence Summary

Empagliflozin is a drug used for type 2 diabetes mellitus (this use is recorded in the knowledge graph; the licence records compiled for this report contain no indication text).
The TxGNN model predicts it may be relevant to **focal stiff limb syndrome**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 0.9906 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (20 of 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 (valid: 20) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for empagliflozin: "Empagliflozin is an inhibitor of SGLT2, the predominant transporter responsible for reabsorption of glucose from the glomerular filtrate back into the circulation. By inhibiting SGLT2, empagliflozin reduces renal reabsorption of filtered glucose and lowers the renal threshold for glucose, and thereby increases urinary glucose excretion." ([DailyMed: Jardiance (empagliflozin) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=faf3dd6a-9cd0-39c2-0d2e-232cb3f67565), label version 2026-11-10; accessed 2026-11-19.) Empagliflozin is known as an SGLT2 inhibitor that acts on glucose reabsorption in the kidney's proximal tubule.

Focal stiff limb syndrome is a rare neurological disorder within the stiff person spectrum, involving impaired GABA-mediated inhibition and often anti-GAD65 autoimmunity. No established mechanistic link to empagliflozin was identified. Any connection would be speculative, such as indirect anti-inflammatory or metabolic effects, or the shared association of anti-GAD autoimmunity with diabetes.

The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases (diabetes and autoimmunity associations), not biological evidence or a pharmacological rationale.

Two other predictions had identical or near-identical scores and were likewise unsupported: classic stiff person syndrome (0.9906) and opsismodysplasia (0.9903). For stiff person syndrome, the link is comorbidity with diabetes and autoimmunity. For opsismodysplasia, the link is a skeletal dysplasia caused by INPPL1 (SHIP2) mutations that touches insulin signalling. Neither is supported by a pharmacological mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Empagliflozin is marketed in India. The records contain no approved-indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 126 | Ajaduo 25mg/5mg Tablet | Strip of 10 tablets | Valid |
| 72400 | Empaone 25mg Tablet | Strip of 10 tablets | Valid |
| 72505 | Empaone 10mg Tablet | Strip of 10 tablets | Valid |
| 94211 | Glyxambi 25mg/5mg Tablet | Strip of 10 tablets | Valid |
| 94217 | Gibtulio 25mg Tablet | Strip of 10 tablets | Valid |
| 94242 | Glyxambi 10mg/5mg Tablet | Strip of 10 tablets | Valid |
| 94310 | Gibtulio 10mg Tablet | Strip of 10 tablets | Valid |
| 94330 | Gibtulio Met 12.5mg/500mg Tablet | Strip of 10 tablets | Valid |
| 94426 | Gibtulio Met 12.5mg/1000mg Tablet | Strip of 10 tablets | Valid |
| 113866 | Jardiance 25mg Tablet | Strip of 10 tablets | Valid |
| 113870 | Jardiance 10mg Tablet | Strip of 10 tablets | Valid |
| 113878 | Jardiance Met 12.5mg/500mg Tablet | Strip of 10 tablets | Valid |
| 113886 | Jardiance Met 12.5mg/1000mg Tablet | Strip of 10 tablets | Valid |
| 113893 | Jardiance Met 5mg/500mg Tablet | Strip of 10 tablets | Valid |
| 161926 | Oboravo 25mg Tablet | Strip of 10 tablets | Valid |
| 162085 | Oboravo 10mg Tablet | Strip of 10 tablets | Valid |
| 215128 | Tiptengio 25mg/5mg Tablet | Strip of 10 tablets | Valid |
| 215270 | Tiptengio 10mg/5mg Tablet | Strip of 10 tablets | Valid |
| 233273 | Vicra 25 Tablet | Strip of 10 tablets | Valid |
| 233378 | Vicra 10 Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 369 interactions are recorded. Most of those listed are of moderate severity, for example phenylephrine, acebutolol, acetazolamide, formoterol, pseudoephedrine, nifedipine, epinephrine, ethinylestradiol, hydrocortisone, salbutamol, ethanol, furosemide and fosinopril. Hydrocortisone (topical) and alclometasone (topical) are minor.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication studies empagliflozin in focal stiff limb syndrome, and no mechanistic link is established. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or pharmacology, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for empagliflozin
- Package insert warnings and contraindications, which are required before safety screening
- Preclinical or mechanistic studies showing a plausible link to GABAergic or autoimmune pathways in stiff person spectrum disorders
- Case reports or exploratory studies in patients with focal stiff limb syndrome

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Jardiance (empagliflozin) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=faf3dd6a-9cd0-39c2-0d2e-232cb3f67565) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

