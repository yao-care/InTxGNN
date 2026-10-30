---
layout: default
title: Iopromide
parent: Model Prediction Only (L5)
nav_order: 443
evidence_level: L5
indication_count: 9
monitor_inn: "Iopromide"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "alopecia", "myosclerosis", "hemoglobinopathy", "pseudoachondroplasia"]
last_modified_at: 2026-10-30
description: "Iopromide: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not stated in the licence records compiled for this report"
---

# Iopromide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Iopromide: From Iodinated Contrast Imaging Agent to Osteoarthritis (Prediction Only)
{: .text-alpha }

## One-Sentence Summary

Iopromide is an iodinated, non-ionic radiographic contrast agent marketed in India under the brand name Ultravist. The TxGNN model predicts it may be effective for **osteoarthritis**, but **no clinical trials and no publications** were found supporting this prediction. The signal is most likely a TxGNN model (deep learning) artifact rather than a therapeutic effect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records compiled for this report (used as a radiographic contrast agent) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.9953 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (4 of 4) – CDSCO approval status is not included in this data |
| Number of Listed Products | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, iopromide is an iodinated, non-ionic contrast medium. It attenuates X-rays for imaging and is pharmacologically inert. It has no known anti-inflammatory or chondroprotective activity.

No mechanistic link to osteoarthritis has been established. The high score (0.9953) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, rather than a treatment effect. The same pattern applies to the other top predictions: rheumatoid arthritis, several skeletal dysplasias (brachyolmia, Hunter-Thompson acromesomelic dysplasia, pseudoachondroplasia), alopecia, myosclerosis and hemoglobinopathy. None has supporting trials or literature, and none has a plausible mechanism. For hemoglobinopathy, contrast media are a safety consideration (for example in sickle cell disease), which argues against a therapeutic role.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

The licence records compiled for this report list four valid single-ingredient registrations, all held by Zydus Cadila. None includes approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 233071 | Ultravist 0.623gm Infusion | Bottle of 100 ml infusion | Not stated in records |
| 230534 | Ultravist 300mg I/ml Injection | Vial of 50 ml injection | Not stated in records |
| 230913 | Ultravist 300mg I/ml Injection | Vial of 100 ml injection | Not stated in records |
| 230682 | Ultravist 370mg I/ml Injection | Vial of 100 ml injection | Not stated in records |

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records in total. Most of the interactions listed are rated Major, including:
  - Metformin
  - Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms)
  - Vancomycin
  - Aminoglycosides (kanamycin, neomycin, streptomycin)
  - Polymyxin B
  - Aminosalicylates (mesalazine, balsalazide, olsalazine, sulfasalazine)

  Mannitol is rated Moderate. Several others (clotrimazole, acetylsalicylic acid, bupropion, dexamethasone, pantoprazole) have an unknown severity rating.
- Package insert warnings and contraindications were not available for this report. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials, no publications and no plausible mechanism. Iopromide is a pharmacologically inert imaging agent, so the osteoarthritis signal is most likely a TxGNN model (deep learning) artifact.

**To proceed, the following is needed:**
- Any direct preclinical or clinical evidence in osteoarthritis (none exists in the data compiled)
- A credible mechanistic hypothesis, supported by mechanism of action data
- Package insert warnings and contraindications from the India label
- Confirmation of approved indications from the licence or label text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

