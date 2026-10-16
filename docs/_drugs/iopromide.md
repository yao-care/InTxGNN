---
layout: default
title: Iopromide
parent: Model Prediction Only (L5)
nav_order: 443
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Iopromide: predicted new indication Osteoarthritis susceptibility (evidence level L5). Approved use: Not stated in the licence data compiled for this report"
---

# Iopromide
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

# Iopromide: From Diagnostic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iopromide is an iodinated, non-ionic radiographic contrast agent used for diagnostic imaging, and it is marketed in India as Ultravist.
The TxGNN model predicts it may be relevant to **osteoarthritis susceptibility**, but there are **no clinical trials and no publications** supporting this prediction.
This is a model-only signal with no supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data compiled for this report (iopromide is known as a radiographic contrast agent) |
| Predicted New Indication | Osteoarthritis susceptibility |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Iopromide is an iodinated, non-ionic contrast agent. It is used to enhance the visibility of structures on X-ray and CT imaging, and it has no established pharmacological target.

No mechanistic link to the predicted indication was identified. "Osteoarthritis susceptibility" describes a genetic risk trait rather than a treatable disease state, so the prediction has limited translational relevance. The high score (0.996) appears to be a graph-based signal only, likely reflecting network proximity rather than drug biology.

The other top predictions point the same way. Osteoarthritis, rheumatoid arthritis, several rare skeletal dysplasias (brachyolmia, Hunter-Thompson acromesomelic dysplasia, pseudoachondroplasia), alopecia, myosclerosis and hemoglobinopathy all lack a plausible mechanism. For some of them there are signals of concern instead:
- Contrast media have raised chondrotoxicity concerns in joints.
- Hair loss has been reported with contrast agents or radiation exposure.
- Iodinated contrast is used with caution in sickle cell disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 233071 | Ultravist 0.623gm Infusion | Bottle of 100 ml infusion | Not specified |
| 230534 | Ultravist 300mg I/ml Injection | Vial of 50 ml injection | Not specified |
| 230913 | Ultravist 300mg I/ml Injection | Vial of 100 ml injection | Not specified |
| 230682 | Ultravist 370mg I/ml Injection | Vial of 100 ml injection | Not specified |

All four registrations are valid single-ingredient products from Zydus Cadila.

---

## Safety Considerations

- **Drug Interactions**: A screening of 100 interactions was completed. The main ones listed are below.
  - **Major**: metformin, amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), mesalazine, balsalazide, olsalazine, sulfasalazine, vancomycin, kanamycin, neomycin, streptomycin, polymyxin B
  - **Moderate**: mannitol
  - **Unknown severity**: clotrimazole, acetylsalicylic acid, bupropion, dexamethasone, pantoprazole

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no clinical trials, no literature and no identified mechanism. The predicted indication is a genetic susceptibility trait, and iopromide is a diagnostic agent with some safety signals in related settings. The score does not justify further investment at present.

**To proceed, the following is needed:**
- Mechanism of action data, to test whether any biological link exists
- Package insert warnings and contraindications, which are currently missing and block safety screening
- Approved indication text for the India registrations
- Preclinical or observational evidence showing a therapeutic effect in the predicted condition
- Reassessment of whether a more clinically meaningful target, such as osteoarthritis itself, is worth pursuing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

