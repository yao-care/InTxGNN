---
layout: default
title: Aztreonam
parent: Model Prediction Only (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
monitor_inn: "Aztreonam"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
last_modified_at: 2026-10-28
description: "Aztreonam: predicted new indication hyperamylasemia (evidence level L5). Approved use: Not recorded in the local data"
---

# Aztreonam
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

## Aztreonam: Monobactam antibiotic → hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Aztreonam is a monobactam antibiotic that acts against gram-negative bacteria and is supplied in India as an injection.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but **no clinical trials and no publications** were found for this condition, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | hyperamylasemia |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for aztreonam is not available in the data compiled for this report. From general pharmacology, aztreonam is a monobactam that inhibits bacterial cell wall synthesis by binding penicillin-binding protein 3 (PBP3), and it is active against gram-negative aerobic bacteria.

Hyperamylasemia is a laboratory finding, an elevated blood amylase level, and not an infectious process. An antibacterial acting on PBP3 has no known effect on amylase production or clearance. The review of this prediction found no plausible mechanistic link, and the high score looks like an artifact of the model rather than a signal supported by clinical data.

Other predictions are listed for the same drug, but all of them are of lower rank and none has direct supporting evidence that would justify replacing this main prediction. They are not discussed further here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Twenty single-ingredient aztreonam injection licences are currently valid. The list is based on partial records and may not be complete. Approved indication text is not recorded for these licences.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 12233 | Azinox 500mg Injection | vial of 1 Injection | Not recorded |
| 7051 | Azotum 2gm Injection | vial of 1 Injection | Not recorded |
| 1376 | Azom 1gm Injection | vial of 1 Injection | Not recorded |
| 36994 | Cromobact Injection | vial of 1 Injection | Not recorded |
| 7396 | Aztrone 2gm Injection | vial of 1 Injection | Not recorded |

---

## Safety Considerations

- **Drug Interactions**: 27 interactions were recorded. Those rated Moderate are picosulfuric acid, dicoumarol and warfarin. Others are listed without a severity level, for example vancomycin, amikacin, amphotericin B, tacrolimus, heparin, metronidazole, morphine and several proton pump inhibitors (pantoprazole, omeprazole, lansoprazole).
- **Conditions of concern**: Caution is noted in people with kidney disease, liver disease, gallbladder disease, Clostridium difficile colitis, perinatal necrotizing enterocolitis, bronchial disease and pyoureter.

Please refer to the package insert for warnings and contraindications, as label text was not available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials or publications for hyperamylasemia, and no plausible mechanism links a PBP3-targeting antibacterial to an elevated amylase level. The prediction is supported only by the model score.

**To proceed, the following is needed:**
- Detailed mechanism-of-action data and a credible biological rationale linking aztreonam to amylase regulation
- Any clinical or preclinical study that directly examines hyperamylasemia
- Package insert warnings and contraindications from the India licence holders
- A safety review for patients with kidney, liver or gallbladder disease and for those taking warfarin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

