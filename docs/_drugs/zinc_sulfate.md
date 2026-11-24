---
layout: default
title: Zinc Sulfate
parent: Model Prediction Only (L5)
nav_order: 908
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "Zinc sulfate"
predicted_indications: ["pharyngitis", "nasal cavity disease", "acute laryngopharyngitis", "congenital prothrombin deficiency"]
description: "Zinc Sulfate: predicted new indication Pharyngitis (evidence level L5). In India: 5 listed products (5 not discontinued)"
---

# Zinc Sulfate
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

## Zinc Sulfate: Pharyngitis
{: .text-alpha }

## One-Sentence Summary

Zinc sulfate is a zinc salt used as a mineral supplement. The TxGNN model predicts it may be relevant to **pharyngitis**, with a score of 0.9985. However, the only trial in pharyngitis itself found no benefit, so the direct evidence is weak. The evidence rests on **1 clinical trial** in a related condition and **2 publications**, only one of which is a randomized trial in pharyngitis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (5 of 5) – CDSCO approval status is not included in this data |
| Number of Listed Products | 5 (valid: 5) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for zinc sulfate: "Zinc is an essential trace element. Zinc functions as a cofactor of various enzymes including DNA polymerases, RNA polymerases, alcohol dehydrogenase, and alkaline phosphatases. Zinc is a coordinator of protein structural folding, such as folding of “Zinc finger” motif that interacts with a variety of proteins, lipids, and nucleic acids." ([DailyMed: zinc sulfate prescribing information, Camber Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49698d00-f44b-4b1f-ae34-6b9067911757), label version 2026-03-04; accessed 2026-11-19.) In general, zinc is thought to have local antiviral and mucosal-protective effects, and may modulate local inflammation and mucosal repair. In theory, zinc lozenges or supplementation could reduce throat pain or irritation.

The link is only partly transferable, however. The available data concern postoperative sore throat and radiation-induced mucosal injury, not infectious pharyngitis. The one randomized trial in pharyngitis itself (radiation-induced) did not show a benefit of zinc sulfate. For this reason the prediction is best treated as a research question rather than an established direction.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | Not applicable | Completed | 87 | Randomized, double-blinded, placebo-controlled study of preoperative zinc lozenges for postoperative sore throat after intubation. This is a related condition, not pharyngitis. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | J Med Assoc Thai | Double-blind, placebo-controlled trial of zinc sulfate for radiation-induced oral mucositis and pharyngitis in head and neck cancer patients; no benefit was found. |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | Case report/series | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | Long-lasting taste disturbance after tonsillectomy, with discussion of a possible role of zinc deficiency. |

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 246414 | Zynwin Tablet | Strip of 10 tablets | Valid |
| 246829 | Zincolak Capsule | Strip of 10 capsules | Valid |
| 247901 | Zia 20 Tablet DT | Strip of 10 tablet dt | Valid |
| 248768 | Zod-Plus Oral Drops | Bottle of 30 ml Oral Drops | Valid |
| 249010 | Zia 200 Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 103 interactions are recorded. Moderate-level ones include alendronic acid, risedronic acid, ibandronate, tetracycline and baloxavir marboxil. Many others are minor, for example abatacept, adalimumab, and corticosteroids such as hydrocortisone and dexamethasone.

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 because no study directly supports zinc sulfate in pharyngitis. The only randomized trial in pharyngitis found no benefit, and the lozenge trial addressed postoperative sore throat, a related condition. A high model score alone is not enough to justify moving forward.

**To proceed, the following is needed:**
- A well-designed randomized trial in the target form of pharyngitis (for example, infectious pharyngitis)
- Mechanism of action data
- Package insert warnings and contraindications from the local licences

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: zinc sulfate prescribing information, Camber Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=49698d00-f44b-4b1f-ae34-6b9067911757) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

