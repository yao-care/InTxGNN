---
layout: default
title: Favipiravir
parent: Model Prediction Only (L5)
nav_order: 339
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Favipiravir: predicted new indication acquired hemophagocytic lymphohistiocytosis associated with malignant disease (evidence level L5). Approved use: Influenza"
monitor_inn: "Favipiravir"
predicted_indications: ["acquired hemophagocytic lymphohistiocytosis associated with malignant disease", "hemophagocytic syndrome associated with an infection", "cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency"]
---

# Favipiravir
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

## Favipiravir: From Influenza to Acquired Hemophagocytic Lymphohistiocytosis Associated with Malignant Disease
{: .text-alpha }

## One-Sentence Summary

Favipiravir is an antiviral originally used to treat influenza.
The TxGNN model predicts it may be effective for **acquired hemophagocytic lymphohistiocytosis associated with malignant disease**, but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza |
| Predicted New Indication | Acquired hemophagocytic lymphohistiocytosis associated with malignant disease |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of favipiravir as: RNA-directed RNA polymerase inhibitor ([ChEMBL CHEMBL221722 (favipiravir): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL221722), CC BY-SA 3.0; accessed 2026-11-19.) Based on general knowledge, favipiravir is a viral RNA-dependent RNA polymerase inhibitor, and its efficacy in influenza is established.

The predicted new indication is a different kind of disease. Malignancy-associated hemophagocytic lymphohistiocytosis (HLH) is driven by immune dysregulation and cytokine storm, not by a viral target. No plausible direct mechanistic link is evident, and the high score is a model output only.

A related prediction is worth noting as a research question. For **hemophagocytic syndrome associated with an infection** (same score, 0.9941), an indirect link is plausible: RNA viruses can trigger HLH, and treating the trigger virus might reduce the downstream hyperinflammation. The two papers retrieved for that prediction concern severe fever with thrombocytopenia syndrome and Heartland virus disease. They do not test favipiravir in HLH. That prediction is rated L4 with a "Research Question" status.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

For reference, the two papers found for the second-ranked prediction (infection-associated hemophagocytic syndrome) are background reviews only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30098914](https://pubmed.ncbi.nlm.nih.gov/30098914/) | 2018 | Review | Journal of Infection and Chemotherapy | Pathophysiology of severe fever with thrombocytopenia syndrome (a tick-borne viral hemorrhagic fever) and development of specific antiviral therapy |
| [38399689](https://pubmed.ncbi.nlm.nih.gov/38399689/) | 2024 | Review | Microorganisms | Review of Heartland virus disease, a tick-borne infection with fever, leukopenia and thrombocytopenia |

## India Market Information

Approved indication text was not available for these products.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 13798 | Actavir 400 Tablet | Strip of 10 tablets | Valid |
| 32317 | Balflu 400 Tablet | Strip of 10 tablets | Valid |
| 46588 | Codifab 400 Tablet | Strip of 10 tablets | Valid |
| 85734 | Feravir 400 Tablet | Strip of 10 tablets | Valid |
| 87361 | Fenzavir 400mg Tablet | Strip of 10 tablets | Valid |
| 87492 | Favenza 800 Tablet | Strip of 10 tablets | Valid |
| 88151 | Fabixa 800mg Tablet | Strip of 10 tablets | Valid |
| 88641 | Favicovid 400mg Tablet | Strip of 10 tablets | Valid |
| 88998 | Fivid Tablet | Strip of 34 tablets | Valid |
| 89107 | Favmac 200mg Tablet | Strip of 34 tablets | Valid |
| 89221 | Favtris 200 Tablet | Strip of 10 tablets | Valid |
| 90506 | Favivent 400mg Tablet | Strip of 10 tablets | Valid |
| 91040 | Ferasun 400mg Tablet | Strip of 17 tablets | Valid |
| 91545 | Favi 19 800mg Tablet | Strip of 10 tablets | Valid |
| 91601 | Foivir 200mg Tablet | Strip of 10 tablets | Valid |
| 91923 | Favisure 400mg Tablet | Strip of 10 tablets | Valid |
| 92071 | Fabivion 200mg Tablet | Strip of 34 tablets | Valid |
| 92497 | Flu-Ppy 400 Tablet | Strip of 10 tablets | Valid |
| 140668 | Monoflu 800 Tablet | Strip of 10 tablets | Valid |
| 207344 | Syvir 200 Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All products are oral tablets.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, and no plausible direct mechanistic link between a viral polymerase inhibitor and malignancy-associated HLH, which is driven by immune dysregulation. The infection-associated HLH prediction is a more reasonable research question, but it is also unsupported by any favipiravir data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently missing, and a blocker for safety screening)
- Detailed mechanism of action data (MOA)
- Any preclinical or clinical evidence of favipiravir in HLH, particularly the infection-associated form
- A mechanistic analysis comparing the original and new indications

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL221722 (favipiravir): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL221722) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

