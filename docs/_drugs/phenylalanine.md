---
layout: default
title: Phenylalanine
parent: Model Prediction Only (L5)
nav_order: 664
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Phenylalanine: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not available"
monitor_inn: "Phenylalanine"
predicted_indications: ["sclerosing cholangitis", "congenital prothrombin deficiency"]
---

# Phenylalanine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Phenylalanine: From an Unspecified Original Indication to Sclerosing Cholangitis

## One-Sentence Summary

Phenylalanine is an essential aromatic amino acid, marketed in India as a single-ingredient oral tablet, but no approved indication is recorded for it in the data compiled for this report.
The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but there are **0 clinical trials** and only **3 indirect publications** (none showing a therapeutic effect), so this is a computational hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the approved indication text on the registration is blank) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L4 (indirect metabolic/biomarker literature only; no studies of phenylalanine as a treatment) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Phenylalanine is an essential amino acid and a precursor of tyrosine, but the data compiled for this report provide no established pathway linking it to sclerosing cholangitis, and no approved original indication to compare against.

The only related literature is indirect. A 2005 cohort study examined plasma tyrosine (a phenylalanine metabolite) and fatigue in primary biliary cirrhosis and primary sclerosing cholangitis. It suggests altered aromatic amino acid metabolism in cholestatic liver disease, but it does not show that giving phenylalanine helps. A 2020 serum metabolomics study in cholangiocarcinoma, a related biliary condition, treats amino acids as disease biomarkers, not treatments. A 1990 paper concerns a different compound (the chemotactic peptide formyl-methionyl-leucyl-phenylalanine) and is not evidence for phenylalanine as a drug.

The high TxGNN score therefore reflects knowledge-graph patterns only and is not supported by clinical evidence.

A second prediction, **congenital prothrombin deficiency** (score 99.26%), has no trials or literature at all. Congenital prothrombin deficiency is a factor II coagulation deficiency, and phenylalanine is not known to correct it. It is treated as a hypothesis only (Evidence Level L5, Hold).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | Examined the relation between plasma tyrosine and fatigue in primary biliary cirrhosis and primary sclerosing cholangitis; identifies amino acid abnormalities but no treatment effect |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Cohort | Journal of Clinical and Experimental Hepatology | Serum metabolomic profiling in cholangiocarcinoma versus benign hepatobiliary disease, searching for biomarkers |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Laboratory assay | Journal of Gastroenterology and Hepatology | Radio-immunoassay of a bacterial chemotactic peptide showing enterohepatic circulation; a different compound, not direct evidence |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 135152 | Melaroc Tablet (Rivan Pharma) | Strip of 10 tablets | Not stated |

## Safety Considerations

- **Disease contraindications flagged in the knowledge graph** (these come from drug-disease relationship data, not from product label text):
  - Kidney and urinary: kidney disease, chronic kidney disease, chronic renal failure syndrome, end stage renal failure, nephrolithiasis, nephrolithiasis susceptibility caused by SLC26A1, nephrocalcinosis, acute urate nephropathy, pyoureter
  - Calcium and phosphorus: hypercalcemia disease, humoral hypercalcemia of malignancy, phosphorus metabolism disease, sarcoidosis
  - Cardiac: heart disease, cardiovascular disease, ventricular fibrillation, digitalis poisoning
  - Phenylalanine metabolism: phenylketonuria, disorder of phenylalanine metabolism

Phenylketonuria and other phenylalanine metabolism disorders are the most directly relevant, since they involve impaired handling of this very amino acid. For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for sclerosing cholangitis rests on a high model score and indirect metabolic literature, with no clinical trials and no demonstrated therapeutic mechanism. The second prediction (congenital prothrombin deficiency) has no supporting evidence at all. The long list of knowledge-graph contraindications, including renal and cardiac disease, adds caution.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication for the Indian product (Melaroc Tablet), which are currently missing
- Mechanism of action data (for example, from DrugBank) to assess any biological link to cholestatic biliary disease
- Preclinical or mechanistic studies testing phenylalanine or its metabolites in sclerosing cholangitis models
- Evaluation of route and formulation suitability (currently only an oral tablet is registered)
- A safety review of the knowledge-graph contraindications, especially renal, cardiac and phenylalanine-metabolism disorders, for the likely patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

