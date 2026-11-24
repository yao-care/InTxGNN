---
layout: default
title: Filgrastim
parent: Model Prediction Only (L5)
nav_order: 352
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Filgrastim: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Constitutional neutropenia"
monitor_inn: "Filgrastim"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "C1 inhibitor deficiency", "serpinopathy with toxic serpin polymerization", "fetal and neonatal alloimmune thrombocytopenia", "platelet-type bleeding disorder"]
---

# Filgrastim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Filgrastim: From Severe Congenital Neutropenia to Primary Release Disorder of Platelets
{: .text-alpha }

## One-Sentence Summary

Filgrastim is a G-CSF analog originally used to treat constitutional and severe congenital neutropenia, cyclic hematopoiesis, and chronic familial neutropenia.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no clinical trials and no publications** currently support this prediction, so it rests on a computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constitutional neutropenia; severe congenital neutropenia; cyclic hematopoiesis; chronic familial neutropenia |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for filgrastim: "Colony-stimulating factors are glycoproteins which act on hematopoietic cells by binding to specific cell surface receptors and stimulating proliferation‚ differentiation commitment‚ and some end-cell functional activation. Endogenous G-CSF is a lineage-specific colony-stimulating factor that is produced by monocytes‚ fibroblasts, and endothelial cells." ([DailyMed: Releuko (filgrastim) prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=74e1ec6e-1630-4654-895c-2bd355f939e7), label version 2026-11-10; accessed 2026-11-19.) Based on known information, filgrastim is a recombinant G-CSF analog that acts mainly on neutrophil-lineage progenitors through the G-CSF receptor. Its efficacy in neutropenic conditions is established.

Primary release disorder of platelets is a qualitative platelet function defect, involving storage pool or secretion abnormalities. No plausible G-CSF mechanism is documented for it. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so the link between the original and new indications is weak.

The other top-ranked predictions (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, collagen receptor defects, C1 inhibitor deficiency and others) show the same pattern. Each involves a defect that filgrastim does not target.

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top predicted indication.

For reference, the 10th-ranked prediction, *platelet-type bleeding disorder* (score 0.9969), retrieved seven trials. All are hematopoietic stem cell transplant studies in which filgrastim is only a supportive component. None tests filgrastim in a platelet disorder, and all were graded low relevance.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00296023](https://clinicaltrials.gov/study/NCT00296023) | NA | Completed | 25 | Low-dose allogeneic stem cell transplant for high-risk low-grade hematologic malignancies |
| [NCT00004232](https://clinicaltrials.gov/study/NCT00004232) | Phase 1 | Completed | Not reported | CD34-enriched stem cell augmentation in allogeneic transplant |
| [NCT00054236](https://clinicaltrials.gov/study/NCT00054236) | Phase 1 | Completed | 55 | Multiple cord blood unit transplant after non-myeloablative conditioning |
| [NCT00301912](https://clinicaltrials.gov/study/NCT00301912) | Phase 2 | Withdrawn | 0 | Busulfan/fludarabine preparative therapy; no data |
| [NCT00295997](https://clinicaltrials.gov/study/NCT00295997) | NA | Unknown | 35 | Non-myeloablative matched unrelated donor transplant |
| [NCT00080925](https://clinicaltrials.gov/study/NCT00080925) | Phase 1 | Completed | 20 | T-cell depleted reduced-intensity haploidentical transplant |
| [NCT00004904](https://clinicaltrials.gov/study/NCT00004904) | Phase 1 | Completed | Not reported | T-cell depleted partially matched donor transplant with CD34 "veto" cells |

## Literature Evidence

Currently no related literature available.

## India Market Information

All 20 registrations are valid single-ingredient injectables. No approved indication text was provided for any of them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 9263 | Axokine Injection | Prefilled syringe of 0.5 ml Injection | Valid |
| 72876 | Endokine 300mcg Injection | Prefilled syringe of 1 Injection | Valid |
| 73169 | Emgrast 300mcg Injection | Vial of 1 ml Injection | Valid |
| 84930 | Fillif 300mcg Injection | Prefilled syringe of 1 ml Injection | Valid |
| 85718 | Filgen 300mcg Injection | Prefilled syringe of 1 Injection | Valid |
| 86535 | Filcad 300mcg Injection | Vial of 1 Injection | Valid |
| 89966 | Ferograstim 300mcg Injection | Vial of 1 Injection | Valid |
| 95110 | Grastim Injection | Vial of 1 ml Injection | Valid |
| 96122 | Granfill 300mcg Injection | Vial of 1 ml Injection | Valid |
| 99924 | Grasipar 300mcg Injection | Vial of 1 Injection | Valid |
| 102162 | G Cyte Injection | Vial of 1 Injection | Valid |
| 108751 | Imumax 300mcg Injection | Vial of 1 Injection | Valid |
| 110381 | Innograst 300mcg Injection | Vial of 1 Injection | Valid |
| 150319 | Neukine 300mcg Injection | Prefilled syringe of 1 ml Injection | Valid |
| 152319 | Neufil 300mcg Injection | Vial of 1 ml Injection | Valid |
| 152481 | Neukine 150mcg Injection | Vial of 1 ml Injection | Valid |
| 156272 | Neugrow 300mcg Injection | Vial of 1 ml Injection | Valid |
| 158375 | Nfil Injection | Prefilled syringe of 1 Injection | Valid |
| 205803 | Sfil 300mcg Injection | Prefilled syringe of 1 Injection | Valid |
| 243969 | Xgrast 300mcg Injection | Vial of 1 ml Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 145 interactions were identified in total. The ones listed below are all rated Moderate. They are mostly cytotoxic chemotherapy, targeted anticancer agents, and radiopharmaceuticals:
  - Paclitaxel
  - Mercaptopurine
  - Azacitidine
  - Bendamustine
  - Arsenic trioxide
  - Alemtuzumab
  - Aldesleukin
  - Abemaciclib
  - Acalabrutinib
  - Ibritumomab tiuxetan
  - Tositumomab (including I-131)
  - Iobenguane (I-131)
  - Fludeoxyglucose (18F)
  - Levamisole

Please refer to the package insert for warnings and contraindications, as no label-based data were available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (Evidence Level L5). No trial or publication tests filgrastim in primary release disorder of platelets, and its mechanism, which acts on the neutrophil lineage, does not plausibly address a platelet secretion defect. The same is true of the other top-ranked predictions.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank, to allow a proper mechanistic-link analysis
- Package insert warnings and contraindications from Indian manufacturers, which are required before any safety screening
- A literature search for any direct evidence of G-CSF in platelet function disorders
- Preclinical or mechanistic studies showing a plausible G-CSF effect on platelet release function
- Route compatibility and similarity-to-original assessments, which are still pending

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Releuko (filgrastim) prescribing information, Amneal Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=74e1ec6e-1630-4654-895c-2bd355f939e7) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

