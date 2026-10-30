---
layout: default
title: Piperacillin
parent: Model Prediction Only (L5)
nav_order: 675
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
description: "Piperacillin: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Bacterial infections"
monitor_inn: "Piperacillin"
predicted_indications: ["rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "sclerosing cholangitis", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy", "WHIM syndrome"]
---

# Piperacillin
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

## Piperacillin: From Bacterial Infection Treatment to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Piperacillin is a beta-lactam antibiotic, marketed in India mainly as an injectable combined with tazobactam for bacterial infections.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but **no clinical trials** and **no supporting publications** were found for this use.
The retrieved literature only mentions rheumatoid arthritis as the background condition of patients treated for infections, so this prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (general antibacterial use; the licence records compiled for this report contain no indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Piperacillin is a beta-lactam antibiotic of the penicillin class. This class inhibits bacterial cell wall synthesis, and its efficacy in bacterial infections is well established.

No credible mechanistic link to rheumatoid arthritis was identified. Piperacillin has no known anti-inflammatory or immunomodulatory activity relevant to this autoimmune disease. The retrieved articles mention rheumatoid arthritis only because the patients had it and developed infections that were treated with antibiotics, or because of methotrexate toxicity. This reflects co-occurrence, not a therapeutic effect.

The high TxGNN score is therefore not supported by clinical or mechanistic evidence. It should be treated as a model-generated hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the retrieved publications tests piperacillin as a treatment for rheumatoid arthritis. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37599303](https://pubmed.ncbi.nlm.nih.gov/37599303/) | 2023 | Case report | Orthopadie (Heidelberg) | Prosthetic knee joint infection in an RA patient on upadacitinib; piperacillin/tazobactam was given for pneumonia. |
| [22605835](https://pubmed.ncbi.nlm.nih.gov/22605835/) | 2012 | Case report | BMJ Case Reports | Purulent pericarditis in an RA patient on methotrexate and etanercept; empirical piperacillin-tazobactam was used. |
| [41268563](https://pubmed.ncbi.nlm.nih.gov/41268563/) | 2025 | Case report | Frontiers in Immunology | Atypical bullous erysipelas caused by *E. coli* in a long-term immunosuppressed RA patient. |
| [41257433](https://pubmed.ncbi.nlm.nih.gov/41257433/) | 2026 | Cohort | British Journal of Clinical Pharmacology | Predictive model for eosinophilia in patients treated with ampicillin/sulbactam or piperacillin/tazobactam. |
| [33987340](https://pubmed.ncbi.nlm.nih.gov/33987340/) | 2021 | Cohort | Annals of Translational Medicine | Prevalence and characteristics of antibiotic-associated drug-induced liver injury. |
| [38343452](https://pubmed.ncbi.nlm.nih.gov/38343452/) | 2024 | Case report | Proceedings (Baylor Univ. Med. Center) | Low-dose methotrexate toxicity with pancytopenia in an RA patient, treated with leucovorin rescue. |
| [34178513](https://pubmed.ncbi.nlm.nih.gov/34178513/) | 2021 | Case report | Cureus | Pancytopenia from low-dose methotrexate in RA. |

## India Market Information

Piperacillin has 20 valid single-ingredient registrations, all injectable. The licence records compiled for this report contain no approved-indication text. Five representative authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 70787 | Demtaz 4000mg/500mg Injection | Vial of 1 Injection | Not recorded |
| Registration No. 209561 | Shipip-T Injection | Vial of 1 Injection | Not recorded |
| Registration No. 182013 | Piprax-T Injection | Vial of 1 Injection | Not recorded |
| Registration No. 179168 | Phyton Injection (Wockhardt) | Vial of 1 Injection | Not recorded |
| Registration No. 190635 | Revotaz 2000mg/250mg Injection (Alkem) | Vial of 10 ml Injection | Not recorded |

## Safety Considerations

- **Drug Interactions**: 81 interactions were recorded. Main ones:
  - **Major**: Vancomycin (combined use is also linked to nephrotoxicity concerns).
  - **Moderate**: Doxycycline, Tetracycline, Minocycline, Kanamycin, Streptomycin, Picosulfuric acid.
  - **Minor**: Clarithromycin.
- **Other considerations from the literature and predictions**:
  - Piperacillin is associated with drug-induced liver injury and cholestasis.
  - It can cause eosinophilia.
  - It requires renal dose adjustment.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no clinical trials, no relevant mechanism, and the literature reflects only co-occurrence of rheumatoid arthritis with infections. The other predicted indications (for example sclerosing cholangitis, diabetic nephropathy and rare genetic syndromes) are likewise unsupported, and some have safety signals that argue against use.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological link to rheumatoid arthritis
- Package insert warnings and contraindications from the Indian regulator, needed for safety screening
- Preclinical or early clinical evidence of anti-inflammatory or disease-modifying activity in rheumatoid arthritis
- Approved-indication text for the Indian registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

