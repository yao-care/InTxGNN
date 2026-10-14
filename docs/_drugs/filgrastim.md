---
layout: default
title: Filgrastim
parent: Model Prediction Only (L5)
nav_order: 352
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Filgrastim: From Severe Congenital Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim is a G-CSF analog originally used to treat constitutional and severe congenital neutropenia, cyclic hematopoiesis, and chronic familial neutropenia.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but **no clinical trials and no publications** currently support this prediction, so it rests on a computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constitutional neutropenia; severe congenital neutropenia; cyclic hematopoiesis; chronic familial neutropenia |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, filgrastim is a recombinant G-CSF analog that acts mainly on neutrophil-lineage progenitors through the G-CSF receptor. Its efficacy in neutropenic conditions is established.

Primary release disorder of platelets is a qualitative platelet function defect, involving storage pool or secretion abnormalities. No plausible G-CSF mechanism is documented for it. The high TxGNN score is a graph-based prediction only, so the link between the original and new indications is weak.

The other top-ranked predictions (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome, collagen receptor defects, C1 inhibitor deficiency and others) show the same pattern. Each involves a defect that filgrastim does not target.

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top predicted indication.

For reference, the 10th-ranked prediction, *platelet-type bleeding disorder* (score 99.69%), retrieved seven trials. All are hematopoietic stem cell transplant studies in which filgrastim is only a supportive component. None tests filgrastim in a platelet disorder, and all were graded low relevance.

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

All 20 registrations are valid single-ingredient injectables. No approved indication text was provided for any of them. The five main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 84930 | Fillif 300mcg Injection (Torrent) | Prefilled syringe, 1 ml | Not stated |
| 89966 | Ferograstim 300mcg Injection (Feron Healthcare) | Vial | Not stated |
| 95110 | Grastim Injection (Dr Reddy's) | Vial, 1 ml | Not stated |
| 243969 | Xgrast 300mcg Injection (Emcure) | Vial, 1 ml | Not stated |
| 150319 | Neukine 300mcg Injection (Intas) | Prefilled syringe, 1 ml | Not stated |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

