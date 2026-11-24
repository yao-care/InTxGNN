---
layout: default
title: Ceftizoxime
parent: Model Prediction Only (L5)
nav_order: 160
evidence_level: L5
indication_count: 5
monitor_inn: "Ceftizoxime"
predicted_indications: ["Ureaplasma urethritis", "xanthogranulomatous pyelonephritis", "uterine inflammatory disease", "epiglottitis", "urogenital tuberculosis"]
last_modified_at: 2026-11-24
description: "Ceftizoxime: predicted new indication Ureaplasma urethritis (evidence level L5). Approved use: Urinary tract infection, gonorrhea…"
---

# Ceftizoxime
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ceftizoxime: From Bacterial Infections to Ureaplasma Urethritis
{: .text-alpha }

## One-Sentence Summary

Ceftizoxime is a third-generation cephalosporin antibiotic.
The TxGNN model predicts it may be effective for **Ureaplasma urethritis**, but **no clinical trials and no publications** support this prediction, and the biology argues against it (Ureaplasma has no cell wall).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, gonorrhea, pneumonia and other bacterial infections (relations recorded in the knowledge graph; the licence records compiled for this report contain no indication text) |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (18 of 18) – CDSCO approval status is not included in this data |
| Number of Listed Products | 18 (valid: 18) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Ceftizoxime belongs to the third-generation cephalosporins, which kill bacteria by binding penicillin-binding proteins and blocking cell wall synthesis.

This is the central problem for the predicted indication. *Ureaplasma* species have no cell wall, so beta-lactam antibiotics such as ceftizoxime are expected to be intrinsically ineffective. The very high TxGNN score is most likely driven by network proximity to other urogenital infections (for example gonorrhea) rather than by real biological support.

The prediction is therefore not considered mechanistically reasonable. It should be treated as a model artefact unless direct evidence emerges.

### Other predicted indications (for context)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Xanthogranulomatous pyelonephritis | 0.9988 | L5 | Plausible activity against *Proteus* and *E. coli*, but definitive treatment is usually nephrectomy; no supporting studies |
| 3 | Uterine inflammatory disease | 0.9988 | L5* | Mechanistically coherent (gonococcus and anaerobe coverage), but no cited study shows ceftizoxime efficacy in this disease |
| 4 | Epiglottitis | 0.9949 | L5 | Spectrum similar to standard third-generation cephalosporins; no studies |
| 5 | Urogenital tuberculosis | 0.9948 | L5 | Not biologically supported (mycobacterial beta-lactamase); no studies |

*The pack lists L4 for this indication, but the retrieved studies do not demonstrate ceftizoxime efficacy in uterine inflammatory disease itself (one is a preclinical hydrogel study, the other a 1988 pelvic inflammatory disease cohort), so it is reported conservatively here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ureaplasma urethritis.

---

## Literature Evidence

Currently no related literature available for Ureaplasma urethritis.

---

## India Market Information

There are 18 valid single-ingredient licences. None of the licence records include approved indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 38466 | Cefticool 1000mg Injection | Vial of 1 Injection | Valid |
| 41380 | Cefizox 500mg Injection | Vial of 1 Injection | Valid |
| 78748 | Eldcef 1gm Injection | Vial of 10 ml Injection | Valid |
| 78749 | Epocelin 1gm Injection | Vial of 1 Injection | Valid |
| 79349 | Eldecet 1gm Injection | Vial of 1 Injection | Valid |
| 83173 | Eldcef 250mg Injection | Vial of 5 ml Injection | Valid |
| 146044 | Megmazix 1gm Injection | Vial of 1 Injection | Valid |
| 179701 | Prozoxime 250mg Injection | Vial of 1 Injection | Valid |
| 202407 | Sporizox Injection | Vial of 1 Injection | Valid |
| 222719 | T Zox 1gm Injection | Vial of 10 ml Injection | Valid |
| 224494 | Trizox 1mg Injection | Vial of 1 Powder for Injection | Valid |
| 225874 | Trizox 250mg Injection | Vial of 1 Powder for Injection | Valid |
| 226829 | Toxicim 1000mg Injection | Vial of 1 Injection | Valid |
| 230404 | Unizox 1gm Injection | Vial of 20 ml Injection | Valid |
| 231575 | Unizox 250mg Injection | Vial of 1 Injection | Valid |
| 235479 | Vosizox Injection | Vial of 1 Injection | Valid |
| 248870 | Zonate 1gm Injection | Vial of 1 gm Injection | Valid |
| 250712 | Zoxiimac Injection | Vial of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

All products are injectable.

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: the knowledge graph links ceftizoxime with the following conditions as contraindications: kidney disease, pyoureter, blood coagulation disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis and congenital prothrombin deficiency.
- **Drug Interactions**: 12 interactions, all rated Moderate:
  - Aminoglycosides: kanamycin, neomycin, streptomycin, amikacin (including liposomal), gentamicin
  - Warfarin
  - Chloramphenicol
  - Picosulfuric acid
  - Ethinylestradiol
  - Mycophenolic acid
  - Pemetrexed

Please refer to the package insert for warnings and label contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or literature behind it, and *Ureaplasma* lacks a cell wall, so a cell-wall-targeting beta-lactam is not expected to work. The high TxGNN score is not backed by biology.

**To proceed, the following is needed:**
- Evidence that ceftizoxime has in vitro or clinical activity against *Ureaplasma* (currently contrary to expectation)
- Package insert warnings and contraindications from Indian licence holders
- Mechanism of action data from DrugBank
- If a urogenital or gynaecological use is of interest, consider uterine inflammatory disease (pelvic inflammatory disease) as a better-grounded research question, which would need prospective comparative data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

