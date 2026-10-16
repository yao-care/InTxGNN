---
layout: default
title: Oxytetracycline
parent: Model Prediction Only (L5)
nav_order: 634
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Oxytetracycline: predicted new indication Chronic rhinosinusitis (evidence level L5). Approved use: Bacterial infections (e.g., urinary tract infection, bronchitis…"
monitor_inn: "Oxytetracycline"
predicted_indications: ["chronic rhinosinusitis", "chronic ethmoidal sinusitis", "paranasal sinus neoplasm (disease)", "punctate epithelial keratoconjunctivitis", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "otitis externa"]
---

# Oxytetracycline
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

# Oxytetracycline: From Bacterial Infections to Chronic Rhinosinusitis

## One-Sentence Summary

Oxytetracycline is a tetracycline-class antibiotic, originally used for bacterial infections such as urinary tract infection, bronchitis, pneumonia, and conjunctivitis.
The TxGNN model predicts it may be effective for **chronic rhinosinusitis**, but **no clinical trials and no publications** currently support this specific prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (e.g., urinary tract infection, bronchitis, pneumonia, conjunctivitis); the license records compiled do not include indication wording |
| Predicted New Indication | Chronic rhinosinusitis |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this report. Based on known information, oxytetracycline belongs to the tetracycline class of broad-spectrum antibiotics. Its efficacy in respiratory, urinary, and eye infections is established, and mechanistically it may be applicable to chronic rhinosinusitis.

Tetracyclines are also known to have anti-inflammatory and matrix metalloproteinase-inhibiting properties. Low-dose doxycycline, a related tetracycline, has been explored in chronic rhinosinusitis with nasal polyps. This offers a plausible bridge between the original infectious indications and the predicted sinus disease.

This link is **hypothetical**. No studies of oxytetracycline itself in chronic rhinosinusitis were found. The high score may partly reflect closeness to other respiratory and infectious disease nodes in the knowledge graph rather than a proven therapeutic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Oxytetracycline has 20 valid single-ingredient registrations in India and none cancelled. Dosage forms include capsules, tablets, oral solution, syrup, and injectable or infusion products. The license records do not include approved indication text. Five main registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 221265 | T M 250mg Capsule | Strip of 4 capsules | Pfizer Ltd |
| 216151 | Terramycin SF Capsule | Strip of 10 capsules | Pfizer Ltd |
| 216058 | Terramycin MD Injection | Vial of 10 ml injection | Pfizer Ltd |
| 163153 | Oxytetracycline AF Tablet | Strip of 4 tablets | Pfizer Ltd |
| 228563 | Tetracon 50mg Syrup | Bottle of 100 ml syrup | Western Remedies |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from drug-disease relationship data, not from package insert text): kidney disease, kidney failure, uremia, glomerulonephritis, liver disease, gallbladder disease, *Clostridium difficile* colitis, G6PD deficiency, potassium deficiency, atrial fibrillation, atrioventricular block, Adams-Stokes syndrome, Wolff-Parkinson-White syndrome, respiratory failure, perinatal necrotizing enterocolitis, glycogen storage disease, cystinuria, galactosemia, and pyoureter.
- **Drug Interactions**: 144 interactions were recorded. Selected ones:
  - **Major**: Vitamin A.
  - **Moderate**: Amoxicillin, balsalazide, calcium salts (phosphate, acetate), magnesium salts (oxide, sulfate, chloride), zinc salts (sulfate, acetate), potassium citrate, and multiple insulin products (aspart, degludec, detemir, glargine, glulisine, human).
  - **Minor**: Mannitol.

Please refer to the package insert for full warnings and precautions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The chronic rhinosinusitis prediction is supported only by the model score (L5), with no trials or publications for oxytetracycline in this condition. The mechanistic link, while plausible for the tetracycline class, is unverified for this drug.

**To proceed, the following is needed:**
- A targeted literature search for oxytetracycline, and for tetracyclines more broadly, in chronic rhinosinusitis, to establish whether any direct evidence exists
- Mechanism of action data
- The package insert warnings and contraindications from the Indian regulator, which are needed for safety screening
- Route and formulation compatibility assessment (sinus delivery versus the oral and injectable forms currently registered)
- A comparison against standard chronic rhinosinusitis therapy

**Note on an alternative candidate:** Among the other predictions, **otitis externa** has the most supporting literature. It includes randomized comparisons of topical oxytetracycline, polymyxin B, and hydrocortisone combinations against other treatments (e.g., 1985, 1990, 1993). The studies are mostly old, and several suggest that steroid alone or other antibiotics may perform comparably, so oxytetracycline's own contribution is uncertain. It would be a more tractable research question than chronic rhinosinusitis, but it is not the primary subject of this evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

