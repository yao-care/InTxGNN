---
layout: default
title: Filgrastim
parent: Moderate Evidence (L3-L4)
nav_order: 349
evidence_level: L4
indication_count: 10
---

# Filgrastim
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Filgrastim: From Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim is a recombinant human G-CSF, widely known for stimulating neutrophil production in the treatment of neutropenia (its official local indication text is not available in this Evidence Pack — see Data Gaps). The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, with **14 clinical trials** and **1 publication** currently associated with this direction, though none of the trials directly test filgrastim as a treatment for this platelet disorder.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neutropenia (G-CSF class use, general knowledge — no TFDA-licensed indication text available; drug not marketed locally) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.9976% |
| Evidence Level | L4 |
| India Market Status | Not marketed (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, filgrastim is a recombinant human granulocyte colony-stimulating factor (G-CSF) whose established pharmacology is to stimulate proliferation and differentiation of granulocyte precursor cells and to mobilize CD34+ hematopoietic stem cells into peripheral blood.

"Primary release disorder of platelets" (platelet storage/release pool disorder) is a defect in platelet granule content release — a platelet *functional* disorder — which has no known direct mechanistic link to G-CSF's action on the granulocyte/stem-cell lineage. The TxGNN model's very high score (0.99998) likely reflects indirect knowledge-graph proximity within the broad "hematopoiesis/blood cell" semantic neighborhood, rather than a demonstrated pharmacological mechanism.

Consistent with this, the associated clinical trials are almost entirely hematopoietic stem cell transplantation (HSCT) studies in which filgrastim is used only as supportive therapy for stem cell mobilization/engraftment — not as a treatment aimed at the platelet disorder itself. No trial in the evidence pack was designed to test filgrastim's efficacy for this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Completed | 64 | CD34+ selected vs. unselected autologous SCT in advanced MCL/DLBCL; filgrastim used for stem cell mobilization, not disease-targeted treatment |
| [NCT05170828](https://clinicaltrials.gov/study/NCT05170828) | Phase 1 | Withdrawn | 0 | Cryopreserved MMUD bone marrow transplant trial; withdrawn, no direct relevance |
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | AHSCT vs. best available therapy for resistant relapsing MS; filgrastim only as transplant support |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Post-transplant cyclophosphamide dosing for GVHD prophylaxis; no direct disease relevance |
| [NCT01503918](https://clinicaltrials.gov/study/NCT01503918) | Phase 2 | Completed | 124 | Antiviral CMV reactivation prophylaxis in critical care; unrelated to platelet disorder |
| [NCT04540120](https://clinicaltrials.gov/study/NCT04540120) | Phase 2 | Terminated | 49 | Dapansutrile for moderate COVID-19/cytokine release syndrome; unrelated |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Phase 2 | Completed | 160 | Ganciclovir/valganciclovir for CMV reactivation prevention; unrelated |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic blood SCT in high-risk pediatric sarcomas; unrelated |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic HSCT for hematologic malignancies; unrelated |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | Completed | 19 | Reduced-intensity HSCT for GATA2 mutations; unrelated |

*4 additional lower-relevance/pending trials exist in the evidence pack but are omitted here for brevity.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Cohort study | Frontiers in Immunology | G-CSF mobilization in healthy donors preferentially mobilizes lymphocyte subsets; supports known filgrastim stem-cell mobilization biology but does not address platelet release disorders directly |

---

## Safety Considerations

- **Drug Interactions**: 145 documented interactions recorded (source: DDInter), predominantly rated Moderate severity. Representative interacting agents include Iobenguane (I-131), Fludeoxyglucose (18F), Ibritumomab tiuxetan, Tositumomab (I-131), Paclitaxel, Acalabrutinib, Aldesleukin, Alemtuzumab, Arsenic trioxide, Azacitidine, and Bendamustine — largely cytotoxic chemotherapy agents and radiopharmaceuticals, reflecting the need for caution when filgrastim is co-administered with myelosuppressive or radioisotope-based treatments.

Local package-insert warnings and contraindications are not available in this Evidence Pack (flagged as a Blocking data gap — TFDA labeling has not yet been retrieved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between filgrastim's G-CSF pathway and primary platelet release disorder is weak and unconfirmed (Evidence Level L4); no clinical trial in the evidence pack directly tests this indication, the drug is not currently marketed locally, and TFDA safety labeling (warnings/contraindications) is missing — a Blocking gap that prevents even an initial safety assessment (S1).

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (Blocking data gap DG001)
- Confirmed mechanism of action documentation from DrugBank (High-severity data gap DG002)
- A disease-specific study or case series directly evaluating filgrastim in platelet release/storage pool disorders, since existing trials use it only as transplant-supportive therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

