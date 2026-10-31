---
layout: default
title: Mometasone
parent: Model Prediction Only (L5)
nav_order: 566
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Mometasone: predicted new indication Primary cutaneous T-cell lymphoma (evidence level L5). Approved use: Not stated in the Indian licence data. Reference pharmacology describ…"
monitor_inn: "Mometasone"
predicted_indications: ["primary cutaneous T-cell lymphoma"]
---

# Mometasone
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

## Mometasone: From Corticosteroid-Responsive Inflammatory Conditions to Primary Cutaneous T-Cell Lymphoma
{: .text-alpha }

## One-Sentence Summary

Mometasone is a potent corticosteroid marketed in India as nasal sprays and topical creams, ointment and gel, used for allergic and inflammatory conditions.
The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma**,
but there are currently **no registered clinical trials** and only **2 case reports** that mention it, so the support is mainly a model prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Indian licence data. Reference pharmacology describes intranasal use for asthma, allergic rhinitis and nasal polyposis, and topical use for allergic skin disorders |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 0.9936 |
| Evidence Level | L5 (model prediction only; the two case reports do not provide mometasone-specific evidence) |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on known pharmacology, mometasone is a potent corticosteroid that acts on the glucocorticoid receptor (NR3C1). Activating this receptor suppresses T-cell activation and inflammatory cytokine production, and gives anti-inflammatory, immunosuppressive and antiproliferative effects.

Primary cutaneous T-cell lymphomas, the most common being mycosis fungoides, are driven by malignant T cells in the skin. Topical corticosteroids are an accepted skin-directed treatment for early-stage (patch/plaque) disease. This gives the prediction a plausible biological link, particularly for the topical forms of mometasone, which are already marketed in India.

The high score should be read with caution. It likely reflects class-level corticosteroid associations rather than mometasone-specific data, and none of the data compiled here shows mometasone benefiting patients with this lymphoma.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case report | Proceedings (Baylor University Medical Center) | Refractory cutaneous pseudolymphoma (a benign look-alike of lymphoma) that failed mometasone and tacrolimus, then was treated with tapinarof. It does not support mometasone efficacy |
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case report | Journal of Cutaneous Pathology | Childhood mycosis fungoides with a CD8+ CD56+ cytotoxic immunophenotype in an 11-year-old boy. The abstract excerpt available does not describe mometasone results |

## India Market Information

Twenty valid single-ingredient licences are registered; the five main ones are listed below. Approved indication text is not provided in the licence records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 108133 | Isomet-M Nasal Spray | 100 MDI nasal spray | Not stated |
| 1872 | Aquamet Nasal Spray | 12 ml bottle, nasal spray | Not stated |
| 72468 | Elocon Cream | 10 g tube, cream | Not stated |
| 137979 | Midsone 0.1% Cream | 15 g tube, cream | Not stated |
| 48801 | Clearoid 0.1% Gel | 10 g tube, gel | Not stated |

The 20 licences cover nasal sprays, creams, an ointment and a gel. The topical forms are relevant to a skin-directed use in cutaneous lymphoma.

## Safety Considerations

- **Drug Interactions**: The interaction query completed with one entry, which is a pharmacological target relationship (glucocorticoid receptor, NR3C1) rather than an interaction with another drug.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high and topical corticosteroids are an accepted option in early-stage mycosis fungoides, but no mometasone-specific clinical trials or supporting studies were found. The evidence is a model prediction only, and the package insert safety information is missing.

**To proceed, the following is needed:**
- Mometasone-specific clinical or observational data in primary cutaneous T-cell lymphoma, such as early-stage mycosis fungoides
- Detailed mechanism-of-action data from DrugBank
- Package insert warnings and contraindications for the marketed Indian products
- Approved indication text for the Indian licences, to confirm the original indication
- Confirmation that the topical products are suitable for this use (route and formulation compatibility)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

