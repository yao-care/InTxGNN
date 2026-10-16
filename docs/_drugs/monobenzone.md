---
layout: default
title: Monobenzone
parent: Model Prediction Only (L5)
nav_order: 567
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Monobenzone: predicted new indication Dentinogenesis imperfecta (evidence level L5). Approved use: Not stated in the registration records compiled for this report (the…"
monitor_inn: "Monobenzone"
predicted_indications: ["dentinogenesis imperfecta", "deafness, autosomal dominant 39, with dentinogenesis imperfecta 1", "rectal cloacogenic carcinoma", "esophageal basaloid carcinoma", "esophagus verrucous carcinoma", "adenosquamous prostate carcinoma", "adenosquamous lung carcinoma", "acantholytic variant squamous cell breast carcinoma", "adenosquamous breast carcinoma", "gallbladder adenosquamous carcinoma"]
---

# Monobenzone
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

# Monobenzone: From Depigmentation Therapy to Dentinogenesis Imperfecta

## One-Sentence Summary

Monobenzone is a topical depigmenting agent marketed in India as creams and an ointment.
The TxGNN model predicts it may be effective for **Dentinogenesis Imperfecta**,
but **no clinical trials and no publications** currently support this prediction, so it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records compiled for this report (the drug is a topical depigmenting agent) |
| Predicted New Indication | Dentinogenesis imperfecta |
| TxGNN Prediction Score | 92.18% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, monobenzone is a tyrosinase substrate. It forms reactive quinones that selectively damage melanocytes, which is why it is used topically for depigmentation.

The predicted disease is very different from this use. Dentinogenesis imperfecta is an inherited dentin disorder caused mainly by DSPP mutations. No melanocyte or tyrosinase pathway is known to be involved, so no mechanistic link can be established. The high score (0.92) most likely reflects graph-based similarity rather than biological rationale, and the score ranks 83,079th overall.

Other top-ranked predictions show the same weakness:
- **Deafness, autosomal dominant 39, with dentinogenesis imperfecta 1:** a related DSPP disorder, probably predicted because of its similarity to the first. Melanocytes in the cochlea support hearing, so melanocytotoxicity is a concern rather than a benefit.
- **Various non-melanocytic carcinomas** (rectal cloacogenic, esophageal basaloid, esophageal verrucous, adenosquamous prostate, lung, breast and gallbladder carcinomas, and acantholytic squamous breast carcinoma): these lack the tyrosinase-dependent target, and any anticancer rationale would be speculative.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 96014 | Genquin Cream (Neova Biogene Private Limited) | Cream, 30 g tube | Not stated |
| 26186 | Benoquin Cream (Brinton Pharmaceuticals Pvt Ltd) | Cream, 30 g tube | Not stated |
| 26245 | Benoquin Ointment (Mac Laboratories Ltd) | Ointment, 20 g tube | Not stated |
| 3424 | Albaquin 20% Cream (Puneet Laboratories Pvt Ltd) | Cream, 20 g tube | Not stated |

All four registrations are valid single-ingredient products. All are topical forms, so a route-compatibility assessment for the predicted indications has not been completed.

## Safety Considerations

Please refer to the package insert for safety information.

No drug-interaction records were found, and the knowledge graph lists no contraindicated diseases for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials or publications, and no plausible mechanism links a melanocyte-selective topical agent to dentinogenesis imperfecta or to the other predicted conditions. A topical product also does not fit the likely routes of use for these diseases.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or mechanistic evidence for any link to dentin or DSPP biology
- Assessment of route compatibility and local versus systemic exposure
- Approved indication text for the Indian registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

