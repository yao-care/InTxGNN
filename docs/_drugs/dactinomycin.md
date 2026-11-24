---
layout: default
title: Dactinomycin
parent: Model Prediction Only (L5)
nav_order: 228
evidence_level: L5
indication_count: 4
monitor_inn: "Dactinomycin"
predicted_indications: ["relapsing-remitting multiple sclerosis", "liver sarcoma", "upper aerodigestive tract neoplasm", "head and neck cancer"]
last_modified_at: 2026-11-24
description: "Dactinomycin: predicted new indication relapsing-remitting multiple sclerosis (evidence level L5). In India: 6 listed products (6 not discontinued)"
---

# Dactinomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Dactinomycin: transcription-inhibiting cytotoxic antibiotic → relapsing-remitting multiple sclerosis
{: .text-alpha }

## One-Sentence Summary

Dactinomycin is a cytotoxic antibiotic that blocks RNA synthesis by binding to DNA, and it is marketed in India as an injectable.
The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis**.
There are **no clinical trials and no publications** on this disease, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (6 of 6) – CDSCO approval status is not included in this data |
| Number of Listed Products | 6 (valid: 6) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dactinomycin: "Dactinomycin is a cytotoxic actinomycin that binds DNA and inhibits RNA synthesis. The cytotoxic activity of dactinomycin has been demonstrated in animal models of different human cancers." ([DailyMed: dactinomycin prescribing information, Eugia US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5da55538-2602-4704-a9da-603c9f7ff7dc), label version 2024-06-18; accessed 2026-11-19.) Dactinomycin is known as a cytotoxic transcription inhibitor: it intercalates into DNA and blocks RNA polymerase. It also causes marked bone marrow suppression.

In theory, broad suppression of dividing cells could dampen autoreactive lymphocytes, which drive multiple sclerosis. However, the data compiled for this report support no mechanistic link between dactinomycin and this disease. Its toxicity profile makes it an unlikely choice compared with established multiple sclerosis therapies. The high score of 0.9958 is a model output only, and it is not backed by any trial or publication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 3963 | Actinocin 0.5mg Injection | Vial of 1 Injection | Valid |
| 43141 | Cosmegen 0.5mg Injection | Vial of 1 ml Injection | Valid |
| 65406 | Dactinoget 0.5mg Injection | Vial of 1 Powder for Injection | Valid |
| 67103 | Dacmozen 0.5mg Injection | Vial of 2 ml Injection | Valid |
| 69105 | Dactino 0.5mg Injection | Vial of 1 Injection | Valid |
| 223232 | Tinowel 0.5mg Injection | Vial of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antitumour antibiotic, transcription inhibitor) |
| Myelosuppression Risk | High (substantial myelosuppressive toxicity) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Conditions of concern with this drug** (from drug-disease relationship data, not label text): liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, anemia (including macrocytic anemia), aplastic anemia, varicella zoster infection, herpes zoster, hepatic vein thrombosis and Budd-Chiari syndrome.
- **Drug Interactions**: 164 interactions were found. Major ones include deferiprone and samarium (153Sm) lexidronam. Moderate ones include palifermin, strontium chloride Sr-89, fostamatinib, mercaptopurine, roflumilast and chloramphenicol.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trials or publications study this drug in relapsing-remitting multiple sclerosis, and no mechanistic link is supported. Its marked myelosuppressive toxicity makes a favourable benefit-risk balance implausible against established therapies.

**To proceed, the following is needed:**
- Mechanism-of-action data and a plausible immunological rationale
- Preclinical studies in multiple sclerosis models
- Package insert warnings and contraindications from the India product labels
- A benefit-risk assessment against current disease-modifying therapies

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: dactinomycin prescribing information, Eugia US LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5da55538-2602-4704-a9da-603c9f7ff7dc) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

