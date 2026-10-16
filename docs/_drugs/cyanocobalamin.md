---
layout: default
title: Cyanocobalamin
parent: Model Prediction Only (L5)
nav_order: 214
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Cyanocobalamin: predicted new indication Biotin metabolic disease (evidence level L5). Approved use: Vitamin B12 deficiency, pernicious anaemia…"
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Cyanocobalamin: From Vitamin B12 Deficiency to Biotin Metabolic Disease

## One-Sentence Summary

Cyanocobalamin (vitamin B12) is originally used to treat vitamin B12 deficiency and related anaemias, including pernicious anaemia.
The TxGNN model predicts it may be effective for **biotin metabolic disease**, but this is a graph-based prediction only.
There are **no clinical trials** and only **1 loosely related publication** (a 1992 review on vitamin production), so direct evidence is essentially absent.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin B12 deficiency, pernicious anaemia, folic acid deficiency anaemia, iron deficiency anaemia and other deficiency anaemias (the Indian licence records contain no indication text; these come from the knowledge graph) |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cyanocobalamin is a form of vitamin B12 that serves as a cofactor for methionine synthase and methylmalonyl-CoA mutase. Its efficacy in B12 deficiency states is well established.

Biotin metabolic disorders (for example, biotinidase or holocarboxylase synthetase deficiency) arise from defects in biotin recycling or in biotin-dependent carboxylases. The two vitamins share only a loose pathway context: the biotin-dependent propionyl-CoA carboxylase and the cobalamin-dependent methylmalonyl-CoA mutase act in sequence in the propionyl-CoA/methylmalonate pathway.

This overlap is probably the reason for the high network score, rather than evidence of therapeutic benefit. The data compiled for this report do not support a plausible direct mechanistic link, and the prediction should be treated as a hypothesis only. Biotin disorders are conventionally treated with biotin itself, not B12.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1368195](https://pubmed.ncbi.nlm.nih.gov/1368195/) | 1992 | Review | Journal of Chemical Technology and Biotechnology | Overview of biotechnological production of vitamins and coenzymes. It concerns manufacturing, not treatment of biotin metabolic disease, so it offers no clinical support. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 173652 | Polybion Injection 2ml | Ampoule of 5 injections | Not stated in the licence record |
| 94517 | Genoplex-L Syrup | Bottle of 60 ml syrup | Not stated in the licence record |
| 26103 | Bvigor Sublingual tablet Cherry | Strip of 10 sublingual tablets | Not stated in the licence record |
| 233952 | VIB 12 1000mcg Injection | Vial of 1 ml injection | Not stated in the licence record |
| 224998 | Titoebion Injection | Vial of 2 ml injection | Not stated in the licence record |

Eight valid single-ingredient licences are registered in total; the five above are shown.

## Safety Considerations

- **Drug Interactions**: 313 interactions are recorded. The ones listed here are all minor or of unknown severity, and none is rated major.
  - Minor: acid-suppressing drugs (famotidine, ranitidine, cimetidine, nizatidine, omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole) and potassium chloride. These may reduce B12 absorption with long-term use.
  - Unknown severity: metformin, glimepiride, rosiglitazone, acarbose, mesalazine, doxycycline, morphine, sucralfate.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (99.60%) is not backed by any clinical trial or relevant publication. The only mechanistic overlap is adjacent pathway context, not therapeutic rationale. Evidence is at the model-prediction-only level (L5).

**To proceed, the following is needed:**
- Mechanism of action data for cyanocobalamin
- A literature search for B12 use in biotinidase or holocarboxylase synthetase deficiency, and any biochemical rationale
- Package insert warnings and contraindications for the Indian-marketed products
- Preclinical or mechanistic studies to test whether the predicted link has any biological basis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

