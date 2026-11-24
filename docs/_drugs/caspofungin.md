---
layout: default
title: Caspofungin
parent: Model Prediction Only (L5)
nav_order: 151
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Caspofungin: predicted new indication Gastrin secretion abnormality (evidence level L5). Approved use: Esophageal candidiasis"
monitor_inn: "Caspofungin"
predicted_indications: ["gastrin secretion abnormality"]
---

# Caspofungin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Caspofungin: From Esophageal Candidiasis and Candidemia to Gastrin Secretion Abnormality
{: .text-alpha }

## One-Sentence Summary

Caspofungin is an echinocandin antifungal originally used to treat esophageal candidiasis and candidemia.
The TxGNN model ranks **gastrin secretion abnormality** as its top predicted new use, but this is a computational prediction only,
with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Esophageal candidiasis; candidemia |
| Predicted New Indication | Gastrin secretion abnormality |
| TxGNN Prediction Score | 0.9944 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Caspofungin inhibits beta-(1,3)-D-glucan synthase, an enzyme that fungi need to build their cell wall. Human cells do not have this enzyme, which is why the drug is selective for fungal infections such as *Candida*.

Esophageal candidiasis and candidemia are fungal infections. Gastrin secretion abnormality is a disorder of a human digestive hormone. We found **no plausible mechanistic link** between blocking fungal glucan synthesis and regulating gastrin. The very high score (0.9944) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. With no trials or publications behind it, this prediction should be treated as a computational hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Caspofungin has 20 valid single-ingredient registrations in India, all injectable vials. The approved indication text is not listed for these registrations.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 9575 | Asponet 50 Injection | Vial of 1 Injection | Valid |
| 10850 | Auxicasp 50mg Injection | Vial of 1 Injection | Valid |
| 28901 | Brufungin 70 Injection | Vial of 1 Injection | Valid |
| 29267 | Brufungin 50 Injection | Vial of 1 Injection | Valid |
| 35740 | Caspogin 50mg Injection | Vial of 10 ml Injection | Valid |
| 42065 | Casogyn 50mg Injection | Vial of 1 Injection | Valid |
| 43914 | Capsain 50mg Injection | Vial of 10 ml Injection | Valid |
| 44159 | Casporan 50mg Injection | Vial of 1 Injection | Valid |
| 44817 | Casfungen 50mg Injection | Vial of 1 Injection | Valid |
| 45540 | Casfungen 70mg Injection | Vial of 1 Injection | Valid |
| 45947 | Capsain 70mg Injection | Vial of 10 ml Injection | Valid |
| 47817 | Casjol 50 Injection | Vial of 1 Injection | Valid |
| 47846 | Cancigin 70mg Injection | Vial of 1 ml Injection | Valid |
| 49545 | Casporan 70mg Injection | Vial of 1 Injection | Valid |
| 50491 | Capofin 70mg Injection | Vial of 1 Injection | Valid |
| 52244 | Caspercid 50mg Injection | Vial of 1 Injection | Valid |
| 93203 | Fungicaspin 70mg Injection | Vial of 1 Injection | Valid |
| 106113 | Hospicasp 70mg Injection | Vial of 1 Injection | Valid |
| 106141 | Hospicasp 50mg Injection | Vial of 1 Injection | Valid |
| 112805 | Ibicasp 50mg Injection | Vial of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Disease associations from the knowledge graph** (these come from graph relationships, not from package insert text): liver disease, gallbladder disease, potassium deficiency disease.
- **Drug Interactions**: 81 interacting drugs were identified.
  - **Major**: dexamethasone.
  - **Moderate**: naltrexone.
  - The rest have no severity rating. They include pantoprazole, omeprazole, lansoprazole, simvastatin, amphotericin B, prednisone, hydrocortisone and potassium chloride.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has the highest score but no clinical or literature support. It also has no plausible mechanism, since caspofungin acts on a fungal enzyme and has no known role in gastrin regulation. It remains at evidence level L5.

**To proceed, the following is needed:**
- Any mechanistic or preclinical evidence linking caspofungin to gastrin regulation
- Package insert warnings and contraindications for the Indian products
- Detailed mechanism of action data from a curated source

**Note on other candidates:** Other predictions in the same list have much stronger support than this one. The best is **neonatal candidiasis** (evidence level L2), with two Phase 2 trials (NCT00330395, completed, n=16; NCT01945281, terminated, n=51) and a pediatric echinocandin meta-analysis. It would be classed as **Proceed with Guardrails**: confirm neonatal dosing and PK, monitor liver function, and clarify why the randomized trial was terminated. Neonatal candidiasis is an extension of the approved candidemia use, not a new mechanism, so it would be a more productive focus for further evaluation than the top-ranked prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

