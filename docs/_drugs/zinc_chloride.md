---
layout: default
title: Zinc Chloride
parent: Model Prediction Only (L5)
nav_order: 905
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Zinc Chloride: predicted new indication Severe nonproliferative diabetic retinopathy (evidence level L5). Approved use: Not recorded"
monitor_inn: "Zinc chloride"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "Sjogren syndrome", "dry eye syndrome"]
---

# Zinc Chloride
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

## Zinc Chloride: From an Unspecified Original Indication to Severe Nonproliferative Diabetic Retinopathy
{: .text-alpha }

## One-Sentence Summary

Zinc chloride is marketed in India as an injectable (Zincshot Injection), but the data compiled for this report do not record an approved indication.
The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy**, and also ranks **Sjogren syndrome** and **dry eye syndrome** highly.
Currently there are **0 clinical trials** and **0 publications** supporting any of these predictions, so this is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (the approved indication text on the India license is empty) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 0.9934 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

Other predicted indications:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|------|
| 2 | Sjogren syndrome | 0.9918 | L5 | Hold |
| 3 | Dry eye syndrome | 0.9918 | L5 | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for zinc chloride: "Zinc is an essential trace element. Zinc functions as a cofactor of various enzymes including DNA polymerases, RNA polymerases, alcohol dehydrogenase, and alkaline phosphatases. Zinc is a coordinator of protein structural folding, such as folding of “Zinc finger” motif that interacts with a variety of proteins, lipids, and nucleic acids." ([DailyMed: zinc sulfate prescribing information, Camber Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49698d00-f44b-4b1f-ae34-6b9067911757), label version 2026-03-04; accessed 2026-11-19.) Zinc chloride is a zinc salt supplied as an injectable product in India. Because no approved indication is recorded, the relationship between its original use and the new indication cannot be assessed.

A plausible but untested link exists through zinc's biology. Zinc is a cofactor for antioxidant enzymes such as Cu/Zn superoxide dismutase, which may bear on oxidative stress and retinal microvascular damage in diabetes. This is a hypothesis only and is not supported by any trial or publication in the data compiled for this report.

For the other two predictions, zinc is involved in immune regulation and epithelial integrity (relevant to Sjogren syndrome), and in ocular surface maintenance, wound healing, and anti-inflammatory activity (relevant to dry eye syndrome). These rationales are also speculative. The high TxGNN scores (0.9918 for Sjogren syndrome and 0.9918 for dry eye syndrome) reflect model output, not clinical proof.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 247261 | Zincshot Injection | Vial of 10 ml Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

The only available route is injectable. Whether this is compatible with the route needed for the predicted eye or exocrine-gland indications has not been assessed.

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** The TxGNN knowledge graph links zinc chloride to contraindications in methemoglobinemia, sulfhemoglobinemia, G6PD deficiency, glycogen storage disease, cystinuria, galactosemia, pyruvate dehydrogenase E3 deficiency, methemoglobin reductase deficiency, Wilson disease, iron metabolism disease, and hereditary hemochromatosis. These come from graph edges and should be verified against the product label.
- **Drug Interactions:** 76 interactions are recorded. Most of those listed are Minor, including corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone) and several immunosuppressants and biologics (e.g., abatacept, adalimumab, azathioprine, anakinra, baricitinib). Moderate interactions include **tetracycline, minocycline, and levofloxacin**, where zinc may reduce antibiotic absorption. Spacing the doses is a common precaution, but this should be confirmed.

Please refer to the package insert for warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three predictions rest on model scores alone (L5), with no registered clinical trials or publications. The original indication and mechanism of action are not recorded, and the package insert safety information is missing, which blocks safety screening.

**To proceed, the following is needed:**
- Obtain and parse the package insert for Zincshot Injection (approved indication, warnings, contraindications)
- Obtain mechanism of action data (e.g., from DrugBank)
- Search for clinical and preclinical evidence on zinc in diabetic retinopathy, Sjogren syndrome, and dry eye
- Assess route compatibility, since the marketed product is an injection and the predicted indications may need topical or oral delivery
- Review the knowledge-graph contraindications (especially Wilson disease, hemochromatosis, G6PD deficiency) against the label

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: zinc sulfate prescribing information, Camber Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49698d00-f44b-4b1f-ae34-6b9067911757) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

