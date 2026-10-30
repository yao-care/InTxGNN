---
layout: default
title: Folic Acid
parent: Model Prediction Only (L5)
nav_order: 377
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Folic Acid: predicted new indication Biotin metabolic disease (evidence level L5). Approved use: Vitamin deficiency disorder"
monitor_inn: "Folic acid"
predicted_indications: ["biotin metabolic disease"]
---

# Folic Acid
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

## Folic Acid: From Vitamin Deficiency and Anemia to Biotin Metabolic Disease
{: .text-alpha }

## One-Sentence Summary

Folic acid (vitamin B9) is originally used to treat vitamin deficiency disorders and deficiency-related anemias, including folic acid deficiency anemia.
The TxGNN model predicts it may be relevant to **biotin metabolic disease**, but there are **no registered clinical trials** and the **20 publications** found are mostly general reviews on vitamins, not direct evidence for this use.
The prediction is best treated as a model-generated hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin deficiency disorder; folic acid deficiency anemia; iron deficiency anemia; hypochromic anemia; deficiency anemia; microcytic anemia (the approved indication text on the India licences is blank) |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 0.9949 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, folic acid is a water-soluble B vitamin that acts as a cofactor precursor in one-carbon metabolism. Its efficacy in folate-deficiency anemia is well established.

The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Folic acid (B9) and biotin (B7) are both B vitamins involved in cellular metabolism.

The mechanistic link is weak, though. Folic acid cannot replace biotin in biotin-dependent carboxylases. Biotin metabolic diseases, such as biotinidase deficiency and holocarboxylase synthetase deficiency, are treated with pharmacologic doses of biotin itself. No direct mechanism by which folic acid would correct the underlying defect was identified. The score is therefore more likely a "same vitamin family" association than a real therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No randomized trials or studies directly testing folic acid in biotin metabolic disease were found. The most relevant items are reviews that discuss several vitamins together.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handb Clin Neurol | Vitamin-responsive disorders (cobalamin, folate, biotin, B1, E); catalytic roles of vitamin cofactors and inborn errors of vitamin metabolism |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | Int J Mol Sci | Vitamin B12 deficiency and the nervous system; B12 links to biotin and folate in biochemical reactions |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Review | Cureus | Vitamins and type 2 diabetes; lower thiamine, pyridoxine and biotin levels in diabetes |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocr Metab Immune Disord Drug Targets | Individual and combined vitamins in type 2 diabetes |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Review | Clin Dermatol | B vitamins in dermatology; roles in cellular metabolism and erythrocyte synthesis |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Review | Arch Biochem Biophys | Micronutrient supplementation and DNA damage; deficiencies in B12, folic acid, B6 and others |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminol Enzymol | Vitamins in metabolic diseases: malabsorption, metabolic errors, and vitamin-dependent syndromes |
| [13199008](https://pubmed.ncbi.nlm.nih.gov/13199008/) | 1954 | Animal study | Biol Latina | Combined biotin and folic acid deficiency induced in rats on a purified diet |
| [16183151](https://pubmed.ncbi.nlm.nih.gov/16183151/) | 2006 | Animal study | Int J Cardiol | Folic acid reduced VCAM-1 expression in rats with hyperhomocysteinemia (not biotin-related) |
| [21496936](https://pubmed.ncbi.nlm.nih.gov/21496936/) | 2011 | Clinical study | Diabetes Res Clin Pract | Micronutrient supplementation and neuropathy scores in type 2 diabetes |

---

## India Market Information

Folic acid has 20 valid single-ingredient licences in India, none cancelled. The approved indication text is blank in the data compiled for this report. Five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 86303 | Folimet 5mg Tablet | Strip of 10 tablets | Not specified |
| 85641 | Folistat 5mg Tablet | Strip of 10 tablets | Not specified |
| 84545 | Folicel Tablet | Strip of 30 tablets | Not specified |
| 84717 | Folistar Soft Gelatin Capsule | Strip of 10 soft gelatin capsules | Not specified |
| 231606 | Unifol 15 mcg/500 mcg Injection | Vial of 10 ml | Not specified |

Both oral (tablets, soft gelatin capsules) and injectable forms are marketed.

---

## Safety Considerations

- **Drug Interactions**: 430 interactions were recorded. Most are of unknown severity. The only graded ones are Pancrelipase (Moderate) and Sulfasalazine (Minor). Other listed agents include metformin, omeprazole, pantoprazole, lansoprazole, glimepiride, prednisone, simvastatin and mesalazine, all of unknown severity.
- **Disease-related cautions (knowledge graph, not label text)**: The graph links folic acid to contraindication-type relationships with several conditions, including kidney disease, nephrolithiasis, peptic ulcer disease, diabetes mellitus, inflammatory bowel disease, ulcerative colitis, sickle cell anemia, hemolytic anemia, hereditary hemochromatosis, Wilson disease and hypercalcemia. These come from a model graph and have not been verified against package inserts. They should be reviewed with caution.

Package insert warnings and contraindications for India were not available and need to be obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score (L5). There are no clinical trials, and the literature is general vitamin reviews with no direct evidence. Folic acid cannot substitute for biotin, and biotin metabolic diseases are already treated with biotin itself.

**To proceed, the following is needed:**
- A plausible biological mechanism showing how folic acid could affect biotin-dependent pathways (e.g., biotinidase or holocarboxylase synthetase deficiency)
- Mechanism of action data for folic acid
- Preclinical or clinical studies directly testing this use
- Package insert warnings and contraindications from the India regulator, to allow safety screening
- A review of the graph-derived disease cautions against label information
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

