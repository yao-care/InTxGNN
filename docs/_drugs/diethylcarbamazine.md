---
layout: default
title: Diethylcarbamazine
parent: Model Prediction Only (L5)
nav_order: 266
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
description: "Diethylcarbamazine: predicted new indication Syndromic lymphedema (evidence level L4). Approved use: Filariasis and related conditions (elephantiasis, lymphedema, loiasis…"
monitor_inn: "Diethylcarbamazine"
predicted_indications: ["syndromic lymphedema", "primary lymphedema"]
---

# Diethylcarbamazine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Diethylcarbamazine: From Filarial Lymphedema and Elephantiasis to Syndromic Lymphedema
{: .text-alpha }

## One-Sentence Summary

Diethylcarbamazine is an established antifilarial drug, originally used to treat filariasis and its complications such as lymphedema and elephantiasis, as well as loiasis, onchocerciasis and tropical pulmonary eosinophilia.
The TxGNN model predicts it may be effective for **syndromic lymphedema**, but there are **no clinical trials** and only **2 publications**, both on filarial infections and therefore only indirectly related.
The prediction most likely reflects network proximity to the approved filarial lymphedema indication rather than a real therapeutic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Filariasis and related conditions (elephantiasis, lymphedema, loiasis, onchocerciasis, pulmonary eosinophilia) |
| Predicted New Indication | Syndromic lymphedema |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. The literature does describe diethylcarbamazine as predominantly a microfilaricide that affects the parasite's neuromuscular system and promotes immune-mediated cellular cytotoxicity. Its benefit in filarial lymphedema comes from killing microfilariae and reducing parasite-driven lymphatic damage.

Syndromic lymphedema is a genetic condition caused by developmental defects in lymphatic vessels. It has no parasitic cause, so the antiparasitic mechanism does not apply. The two retrieved publications concern tropical pulmonary eosinophilia and filariasis with chyluria. Both are infectious conditions and give only indirect support.

The high TxGNN score most likely arises from the shared "lymphedema" label with the approved filarial indication. It should be read as a network-proximity signal, not as evidence of mechanistic fit.

Other predictions follow the same pattern. They include primary lymphedema (score 0.9925). The score comes from the TxGNN model (deep learning), is driven by the lymphedema association, and has no direct supporting studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for syndromic lymphedema.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1580599](https://pubmed.ncbi.nlm.nih.gov/1580599/) | 1992 | Review | Annual Review of Medicine | Tropical pulmonary eosinophilia is caused by immune hyperresponsiveness to filarial parasites; describes clinical presentation (nocturnal cough, wheezing, eosinophilia) |
| [24772754](https://pubmed.ncbi.nlm.nih.gov/24772754/) | 2013 | Case report | J Assoc Physicians India | A woman with filarial chyluria and nephrotic-range proteinuria was treated with renal pelvic sclerotherapy plus diethylcarbamazine and remained asymptomatic at 19 months |

Neither publication studies syndromic lymphedema. Both address infectious filarial disease.

---

## India Market Information

Diethylcarbamazine is widely marketed in India, with 20 valid single-ingredient registrations and no cancelled ones. The approved indication text is not recorded for these products. Main registrations:

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 103661 | Hetrazan 100 Tablet | Strip of 30 tablets | Pfizer Ltd |
| 25862 | Benocide 100mg Forte Tablet | Strip of 30 tablets | Glaxo SmithKline Pharmaceuticals Ltd |
| 59242 | Deecee 50mg Syrup | Bottle of 60 ml syrup | Shrinivas Gujarat Laboratories Pvt Ltd |
| 59257 | Deecee 100mg Tablet | Strip of 10 tablets | Shrinivas Gujarat Laboratories Pvt Ltd |
| 58514 | Dec Tablet | Strip of 10 tablets | Commonwealth Pharmaceuticals |

Available forms include oral tablets and syrups.

---

## Safety Considerations

Please refer to the package insert for safety information.

The retrieved literature notes one relevant class warning: diethylcarbamazine can cause severe adverse ocular events in people with onchocerciasis, which limits its use in areas where onchocerciasis or loiasis is present.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output and a shared lymphedema label. There are no trials, the literature is only indirectly relevant, and syndromic lymphedema is a genetic developmental disorder with no plausible antiparasitic mechanism. The drug is already widely marketed, so access is not the obstacle. The lack of supporting evidence is.

**To proceed, the following is needed:**
- A plausible mechanism for non-infectious lymphedema (for example anti-inflammatory or immunomodulatory effects), supported by preclinical data
- Mechanism of action data for diethylcarbamazine
- Package insert warnings and contraindications for the Indian products
- Preclinical or early clinical studies directly in syndromic or other non-filarial lymphedema
- Review of whether other high-scoring predictions have any stronger direct evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

