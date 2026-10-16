---
layout: default
title: Ferric Sulfate
parent: Model Prediction Only (L5)
nav_order: 348
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ferric Sulfate: predicted new indication Bronchitis (evidence level L5). Approved use: Not specified in the compiled data"
---

# Ferric Sulfate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ferric Sulfate: From an Unspecified Original Indication to Bronchitis

## One-Sentence Summary

Ferric sulfate is an iron salt that is currently marketed in India as oral tablets, but the data compiled for this report do not specify an approved indication.
The TxGNN model predicts it may be effective for **bronchitis**, but this is a model prediction only, and the **2 linked clinical trials** and **0 publications** do not directly support it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the compiled data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 97.65% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ferric sulfate is an iron salt, and in other settings it is known as an astringent and hemostatic agent. The registered products in India are oral tablets, and their approved indication text is not available in the compiled data.

No credible mechanistic link between ferric sulfate and bronchitis has been established. The high TxGNN score (0.977) is a graph-based prediction only. The two linked trials study a different iron compound (sodium ferric gluconate) in iron-deficiency anemia and appear to have been matched through iron-compound overlap, not through any relevance to bronchitis.

The other top-ranked predictions are also model-only, with no trials or publications. They include bronchial neoplasm (93.3%), gastroduodenitis (92.5%), peptic ulcer disease (91.6%), and several coagulation-related conditions. Some of these, such as antithrombin deficiency type 2 and factor 5 excess with thrombosis, are pro-thrombotic conditions where a hemostatic agent would be conceptually undesirable.

## Clinical Trial Evidence

Both trials were graded as having low relevance (Grade C) for the bronchitis hypothesis.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00224055](https://clinicaltrials.gov/study/NCT00224055) | Phase 4 | Completed | 89 | Ferrlecit (IV iron) vs oral ferrous sulfate for anemia and iron deficiency in chronic kidney disease patients not receiving erythropoietic agents. Not related to bronchitis. |
| [NCT00224042](https://clinicaltrials.gov/study/NCT00224042) | Phase 4 | Completed | 52 | Ferrlecit (IV iron) vs oral ferrous sulfate in chronic kidney disease patients receiving erythropoietic therapy. Not related to bronchitis. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 88477 | Fevincio Tablet (Akognos Life Sciences) | Strip of 10 tablets | Not specified |
| 86629 | Feroact Tablet (Edallia Pharmaceuticals Pvt Ltd) | Strip of 10 tablets | Not specified |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests on the model score alone (Evidence Level L5). The only linked trials concern a different iron compound in kidney-disease anemia, there is no supporting literature, and no mechanistic link has been identified.

**To proceed, the following is needed:**
- The India package insert, including approved indication, warnings, and contraindications. This is a blocking gap for safety screening.
- Mechanism of action data for ferric sulfate.
- Preclinical or clinical evidence specifically relevant to bronchitis, or a re-evaluation of other predictions.
- Assessment of whether the oral tablet route is compatible with a respiratory indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

