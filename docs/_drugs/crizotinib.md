---
layout: default
title: Crizotinib
parent: Model Prediction Only (L5)
nav_order: 213
evidence_level: L5
indication_count: 9
monitor_inn: "Crizotinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "lung germ cell tumor", "pulmonary sulcus neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
last_modified_at: 2026-11-20
description: "Crizotinib: predicted new indication Gingival fibromatosis (fibromatosis, gingival) (evidence level L5). In India: 2 listed products (2 not discontinued)"
---

# Crizotinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Crizotinib: ALK/ROS1/MET tyrosine kinase inhibitor → Gingival fibromatosis (fibromatosis, gingival)
{: .text-alpha }

## One-Sentence Summary

Crizotinib is an oral kinase inhibitor that blocks ALK, ROS1 and MET.
The TxGNN model predicts it may be relevant to **gingival fibromatosis (fibromatosis, gingival)**,
but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Gingival fibromatosis (fibromatosis, gingival) |
| TxGNN Prediction Score | 0.9981 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (2 of 2) – CDSCO approval status is not included in this data |
| Number of Listed Products | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Crizotinib inhibits the receptor tyrosine kinases ALK, ROS1 and MET. This description relies on the drug's generally known targets. According to the Mechanism of Action section of the US FDA-approved prescribing information for crizotinib: "Crizotinib is an inhibitor of receptor tyrosine kinases including ALK, Hepatocyte Growth Factor Receptor (HGFR, c-Met), ROS1 (c-ros), and Recepteur d'Origine Nantais (RON). Translocations can affect the ALK gene resulting in the expression of oncogenic fusion proteins." ([DailyMed: Xalkori (crizotinib) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2a51b0de-47d6-455e-a94c-d2c737b04ff7), label version 2026-10-29; accessed 2026-11-19.)

No pathway has been shown that connects these targets to gingival fibromatosis, a condition of gum tissue overgrowth. The high TxGNN score (0.9981) is a computational output only. The analysis found no identified mechanistic link, and no similarity analysis with the drug's current use has been completed.

The prediction should therefore be treated as a hypothesis for screening, not as a supported repurposing direction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 48989 | Crizalk 250mg Capsule | Box of 60 capsules | Not recorded |
| 48988 | Crizalk 200mg Capsule | Box of 60 capsules | Not recorded |

Both registrations are single-ingredient products from Pfizer Ltd and both are currently valid.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; liver function and cardiac monitoring are generally advised for this class |
| Handling Protection | Please refer to the package insert and local cytotoxic drug handling rules |

## Safety Considerations

- **Drug Interactions**: 566 interactions were identified in total. Major-level examples include clarithromycin, cisapride, dolasetron, eliglustat and granisetron. Moderate-level examples include famotidine, metformin, loperamide, bupropion, aprepitant and dexamethasone.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score but no clinical trials, no literature and no identified mechanistic link, so the evidence level is L5. There is no basis yet to move toward development.

**To proceed, the following is needed:**
- Preclinical or mechanistic evidence linking ALK, ROS1 or MET signalling to gingival fibromatosis
- Detailed mechanism-of-action data for crizotinib
- Package insert warnings and contraindications from the local regulator
- A route and formulation assessment, since the available product is an oral capsule

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-20 | "Detailed mechanism-of-action data were not available in the data compiled for this report, so this description relies on the drug's generally known targets" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt (revised 2026-11-20; earlier version kept in the record) | [DailyMed: Xalkori (crizotinib) prescribing information, Pfizer Laboratories Div Pfizer Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2a51b0de-47d6-455e-a94c-d2c737b04ff7) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

