---
layout: default
title: Vasopressin
parent: Model Prediction Only (L5)
nav_order: 884
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
description: "Vasopressin: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Not stated in the available India license data"
monitor_inn: "Vasopressin"
predicted_indications: ["congenital prothrombin deficiency", "drug-induced osteoporosis"]
---

# Vasopressin
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

## Vasopressin: From Vasopressor Use to Congenital Prothrombin Deficiency
{: .text-alpha }

## One-Sentence Summary

Vasopressin is a peptide hormone marketed in India as an injectable. The data compiled for this report do not list an approved indication for it.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but there are **no registered clinical trials** and only **3 indirect publications** (a review and two case reports), none specific to this condition.
This is a model-only prediction with weak supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available India license data |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 (indirect mechanistic and case-level literature only; no trials) |
| India Market Status | Listed in a compiled Indian medicine price dataset (8 of 8) – CDSCO approval status is not included in this data |
| Number of Registrations | 8 (valid: 8) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Vasopressin and its analogue desmopressin (DDAVP) are known to raise plasma factor VIII and von Willebrand factor by V2 receptor-mediated release from endothelial stores. This makes the drug relevant to factor VIII and combined factor V/VIII deficiencies.

Prothrombin (factor II) is not known to be released through this pathway. The high TxGNN score is therefore most likely driven by network proximity to other coagulation disorders rather than a direct mechanism. The link to prothrombin deficiency should be regarded as weak and speculative.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | Acquired hemophilia A: diagnosis, causes, clinical spectrum and treatment options; not specific to prothrombin deficiency |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case report | Rinsho Ketsueki | DDAVP given in a patient with congenital combined factor V and factor VIII deficiency |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case report | Rinsho Ketsueki | Cesarean section managed with factor VIII concentrate in a pregnant woman with combined factor V and VIII deficiency |

All three publications are indirect. None studies vasopressin in prothrombin deficiency.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 234045 | Vasopar 20IU Injection | Vial of 1 ml injection | Not listed |
| 175541 | Petresin 20IU Injection | Ampoule of 1 ml injection | Not listed |
| 49205 | Cevas 40IU Injection | Vial of 1 ml injection | Not listed |
| 13073 | Argipress 20units Injection | Ampoule of 5 injections | Not listed |
| 181438 | Press UP 20IU Injection | Vial of 1 ml injection | Not listed |

Eight valid single-ingredient registrations exist in total; the five above are shown.

---

## Safety Considerations

**Drug Interactions:** The interaction screen identified 121 potential interactions. Examples from the screened list:
- **Major:** dolasetron, cisapride, papaverine, macimorelin
- **Moderate:** famotidine, epinephrine, loperamide, chlorpropamide, clarithromycin, levofloxacin, ondansetron, granisetron, palonosetron, promethazine, cilostazol, heparin
- **Minor:** metronidazole

Package insert warnings and contraindications were not available. Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score alone. No clinical trials exist, the literature is indirect, and the known mechanism (factor VIII and von Willebrand factor release) does not extend to prothrombin. Package insert safety data are also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed Indian products
- Approved indication text for the Indian licenses
- Detailed mechanism of action data
- Direct evidence, such as preclinical or clinical studies, of vasopressin in prothrombin (factor II) deficiency
- Comparison with established treatments such as prothrombin complex concentrates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

