---
layout: default
title: Cyanocobalamin
parent: Model Prediction Only (L5)
nav_order: 214
evidence_level: L5
indication_count: 1
monitor_inn: "Cyanocobalamin"
predicted_indications: ["biotin metabolic disease"]
last_modified_at: 2026-10-30
description: "Cyanocobalamin: predicted new indication biotin metabolic disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Cyanocobalamin
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

## Cyanocobalamin: vitamin B12 (cobalamin) → biotin metabolic disease
{: .text-alpha }

## One-Sentence Summary

Cyanocobalamin is a synthetic form of vitamin B12, a cobalamin cofactor used to correct B12-related deficiency states.
The TxGNN model predicts it may be relevant to **biotin metabolic disease**, but the evidence is thin: **0 clinical trials** and **1 publication** (a general review on vitamin production, not a study of this disease).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | biotin metabolic disease |
| TxGNN Prediction Score | 0.9960 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (8 of 8) – CDSCO approval status is not included in this data |
| Number of Registrations | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Cyanocobalamin is known to act as a cofactor for two enzymes: methionine synthase and methylmalonyl-CoA mutase.

Biotin metabolic diseases (for example biotinidase deficiency or holocarboxylase synthetase deficiency) involve defects in biotin recycling or in biotin-dependent carboxylases. The only link to cyanocobalamin is a loose shared pathway context: propionyl-CoA carboxylase depends on biotin, while methylmalonyl-CoA mutase depends on cobalamin, and both sit on the propionyl-CoA/methylmalonate route.

This overlap is the more likely source of the high model score than any therapeutic benefit. The score of 0.9960 reflects a model-based prediction only, and no data compiled here supports a direct treatment effect. The prediction should be treated as a hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1368195](https://pubmed.ncbi.nlm.nih.gov/1368195/) | 1992 | Review | Journal of Chemical Technology and Biotechnology | Overview of biotechnological production of vitamins and coenzymes; does not study biotin metabolic disease or treatment with cyanocobalamin |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 173652 | Polybion Injection 2ml | Ampoule of 5 injections | Not recorded |
| 94517 | Genoplex-L Syrup | Bottle of 60 ml syrup | Not recorded |
| 26103 | Bvigor Sublingual tablet Cherry | Strip of 10 sublingual tablets | Not recorded |
| 233952 | VIB 12 1000mcg Injection | Vial of 1 ml injection | Not recorded |
| 224998 | Titoebion Injection | Vial of 2 ml injection | Not recorded |

All 8 licences are single-ingredient products and currently valid; the table lists the first five.

## Safety Considerations

Please refer to the package insert for safety information.

The drug-interaction screening returned 313 records. The ones listed are mostly minor, including acid-suppressing drugs (famotidine, ranitidine, cimetidine, omeprazole, pantoprazole, esomeprazole, lansoprazole, rabeprazole) and potassium chloride. Several others have an unrated level, including metformin, glimepiride, acarbose, rosiglitazone, doxycycline, mesalazine, morphine and sucralfate.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No clinical trial or publication directly studies cyanocobalamin in biotin metabolic disease, and the mechanistic link is indirect, so the evidence level is L5.

**To proceed, the following is needed:**
- Mechanism-of-action data for cyanocobalamin, to test the proposed pathway link
- Preclinical or clinical studies directly addressing biotin metabolic disease
- Package insert warnings and contraindications from the licence holders
- Review of the large set of recorded drug interactions for relevance to the intended population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

