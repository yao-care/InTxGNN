---
layout: default
title: Fosfomycin
parent: Model Prediction Only (L5)
nav_order: 380
evidence_level: L5
indication_count: 8
monitor_inn: "Fosfomycin"
predicted_indications: ["uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "epiglottitis", "urogenital tuberculosis", "laryngitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "pyelitis"]
last_modified_at: 2026-10-23
description: "Fosfomycin: predicted new indication Uterine inflammatory disease (evidence level L5). Approved use: Urinary tract infection"
---

# Fosfomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Fosfomycin: From Urinary Tract Infection to Uterine Inflammatory Disease
{: .text-alpha }

## One-Sentence Summary

Fosfomycin is an antibiotic whose use in **urinary tract infection** is recorded in the knowledge graph. The TxGNN model predicts it may be useful for **uterine inflammatory disease**, but none of the **2 clinical trials** or **1 publication** compiled for this prediction studies that disease, so the prediction currently rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (relation recorded in the knowledge graph; the licence records contain no approved-indication text) |
| Predicted New Indication | Uterine inflammatory disease |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Licences | At least 20 (the list may be partial) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Fosfomycin is described as an inhibitor of MurA, an early enzyme in bacterial cell wall synthesis. It reaches high urinary concentrations and is active against common Gram-negative pathogens such as *E. coli*. In principle, this could extend to bacterial infections of the pelvic organs or uterus.

The link between urinary tract infection and uterine inflammatory disease is mainly anatomical and based on shared bacteria. The model most likely scored the two conditions as similar for that reason. Nothing in the compiled data shows that fosfomycin works in uterine inflammation.

The two trials are general paediatric pharmacokinetic studies. The one publication concerns cystitis linked to dienogest, which is a urinary condition rather than uterine inflammation. The mechanistic argument is therefore plausible but unproven.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3,520 | Pharmacokinetics of understudied drugs given to children as standard of care. Not specific to uterine inflammatory disease and no efficacy data for it. |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5,000 | Pharmacokinetics, pharmacodynamics and safety of understudied drugs in children and young adults. No efficacy conclusion can be drawn for this indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35653789](https://pubmed.ncbi.nlm.nih.gov/35653789/) | 2022 | Cohort | Journal of Obstetrics and Gynaecology | Prospective study of acute cystitis symptoms and bacteriuria in women with endometriosis after surgery and dienogest or combined oral contraceptives. It concerns a urinary tract condition, not uterine inflammation. |

---

## India Market Information

At least 20 valid single-ingredient licences are listed, and the list may be partial. The licence records contain no approved-indication text. Five examples:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 84854 | Fosforal 3gm Granules | Sachet of 8 gm granules | Macleods Pharmaceuticals Pvt Ltd |
| 86272 | Fosvaith 4g Injection | Vial of 1 injection | Advaith Life Sciences Pvt Ltd |
| 133747 | Myfos Powder | Sachet of 8 gm powder | Sun Pharmaceutical Industries Ltd |
| 249132 | Zan-Fos Injection | Vial of 1 injection | Suzan Pharma |
| 85326 | Fosfolife Sachet | Sachet of 8 gm powder | LifeSurge BioSciences Pvt Ltd |

---

## Safety Considerations

- **Contraindication-type relations recorded in the knowledge graph (not label text):** kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis.
- **Drug Interactions (3 found):**
  - Balsalazide: moderate
  - Picosulfuric acid: moderate
  - Metoclopramide: minor

Please also refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any study of fosfomycin in uterine inflammatory disease. The two trials are general paediatric pharmacokinetic studies, and the one publication concerns a urinary condition. The evidence level is therefore L5.

**To proceed, the following is needed:**
- Clinical or observational studies of fosfomycin in uterine or pelvic inflammatory infections
- Detailed mechanism-of-action data and data on tissue penetration in the female genital tract
- Package insert warnings and contraindications for the marketed Indian products
- Confirmation of the formulation and route (oral or intravenous) that would be relevant
- Consideration of the other predicted indications compiled for this drug. Pyelitis has the strongest support, including a Phase 2/3 randomized trial of intravenous fosfomycin in complicated urinary tract infection and acute pyelonephritis (PMID 30861061). It is better treated as an extension of the urinary tract infection use than as a new disease area.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

