---
layout: default
title: Lovastatin
parent: Model Prediction Only (L5)
nav_order: 506
evidence_level: L5
indication_count: 1
monitor_inn: "Lovastatin"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-31
description: "Lovastatin: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Hyperlipidemia and related lipid disorders"
---

# Lovastatin
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

## Lovastatin: From Hyperlipidemia to Cholesterol-Ester Transfer Protein Deficiency
{: .text-alpha }

## One-Sentence Summary

Lovastatin is an HMG-CoA reductase inhibitor (statin) whose relations recorded in the knowledge graph centre on lipid disorders such as hyperlipidemia and atherosclerosis.
The TxGNN model predicts it may be relevant to **cholesterol-ester transfer protein (CETP) deficiency**, but there are **0 clinical trials** and **1 publication** (a preclinical animal study that does not directly address this disease), so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperlipidemia and related lipid disorders (relations recorded in the knowledge graph; no approved indication text is available in the local licence records) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lovastatin belongs to the statin class (HMG-CoA reductase inhibitors), which lowers LDL cholesterol.

CETP deficiency is a disorder of lipoprotein metabolism, with raised HDL cholesterol and an altered LDL particle profile. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

There is also a clinical question: CETP deficiency is usually a benign phenotype and may even be cardioprotective because of high HDL-C, so the need for treatment is unclear. The mechanistic reasoning could not be checked against curated mechanism data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19965609](https://pubmed.ncbi.nlm.nih.gov/19965609/) | 2010 | Preclinical (animal model) | Journal of Lipid Research | Knockout of StARD4, a cholesterol transfer protein, led to modest weight reduction and minor changes in lipid metabolism in mice. It does not study lovastatin or CETP deficiency directly. |

## India Market Information

At least 20 single-ingredient lovastatin licences are recorded, and the list may be partial. No approved indication text is available in these records. Five main entries:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 123364 | Lovex 10mg Tablet (Lupin Ltd) | Strip of 10 tablets | Not stated in the records |
| Registration No. 126892 | Lovacard 20mg Tablet (Cipla Ltd) | Strip of 10 tablets | Not stated in the records |
| Registration No. 14707 | Aztatin 20mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not stated in the records |
| Registration No. 128055 | Lotin 20mg Tablet (Intas Pharmaceuticals Ltd) | Strip of 10 tablets | Not stated in the records |
| Registration No. 186548 | Rovacor 20mg Tablet (Ranbaxy Laboratories Ltd) | Strip of 10 tablets | Not stated in the records |

## Safety Considerations

- **Contraindications recorded in the knowledge graph (not label text):** liver disease, gallbladder disease, thrombocytopenia, hyperglycemia, peptic ulcer disease, myopathy and other muscle diseases, rhabdomyolysis, diabetes mellitus, diabetic ketoacidosis, gout, blood coagulation disease, acute coronary syndrome, coronary artery disease, myocardial infarction, and others.
- **Drug interactions:** 247 interactions were found in total. Notable ones:
  - Major: clarithromycin.
  - Moderate: aprepitant, omeprazole, metronidazole, cimetidine, esomeprazole, lansoprazole, pantoprazole, clotrimazole, miconazole, rosuvastatin, simvastatin, tinidazole, troglitazone, naltrexone, eluxadoline, pectin.
  - Minor: exenatide.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it is a model output only. No clinical trial or publication directly studies lovastatin in CETP deficiency, so the evidence level is L5. CETP deficiency is often benign, so a treatment need is unclear. Several knowledge-graph contraindications and a major interaction (clarithromycin) also call for caution.

**To proceed, the following is needed:**
- Clarify whether CETP deficiency has an unmet therapeutic need that a statin would address.
- Obtain lovastatin mechanism of action data and check the mechanistic link to CETP deficiency.
- Obtain the package insert warnings and contraindications from the licence holders in India.
- Run a targeted search for studies of statins in CETP deficiency or related genetic HDL disorders.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

