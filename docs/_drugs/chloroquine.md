---
layout: default
title: Chloroquine
parent: Model Prediction Only (L5)
nav_order: 174
evidence_level: L5
indication_count: 4
monitor_inn: "Chloroquine"
predicted_indications: ["rheumatoid factor-positive polyarticular juvenile idiopathic arthritis", "rheumatoid nodulosis", "juvenile chronic polyarthritis", "juvenile idiopathic arthritis"]
last_modified_at: 2026-11-24
description: "Chloroquine: predicted new indication rheumatoid factor-positive polyarticular juvenile idiopathic arthritis (evidence level L5). In India: at least 20 listed products"
---

# Chloroquine
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

## Chloroquine: Antimalarial and immunomodulatory 4-aminoquinoline → rheumatoid factor-positive polyarticular juvenile idiopathic arthritis
{: .text-alpha }

## One-Sentence Summary

Chloroquine is an established antimalarial and immunomodulatory agent that is marketed in India.
The TxGNN model predicts it may be effective for **rheumatoid factor-positive polyarticular juvenile idiopathic arthritis**,
but currently **0 clinical trials** and only **1 indirect publication** (a study of a different drug) support this direction, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | rheumatoid factor-positive polyarticular juvenile idiopathic arthritis |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for chloroquine: "Chloroquine, a 4-aminoquinoline, is an anti-protozoal agent. The precise mechanism by which chloroquine exhibits activity is not known. Chloroquine, may exert its effect against Plasmodium species by concentrating in the acid vesicles of the parasite and by inhibiting polymerization of heme." ([DailyMed: chloroquine phosphate prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=06c69e2b-211b-4746-9f3a-f86d36520570), label version 2026-10-21; accessed 2026-11-19.) Based on general pharmacological knowledge, chloroquine acts as an immunomodulator by raising lysosomal pH, interfering with autophagy and antigen presentation, and reducing pro-inflammatory cytokine production. These effects are the reason it has long been used as a slow-acting antirheumatic agent.

Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis closely resembles adult seropositive rheumatoid arthritis in its joint-centred, autoantibody-associated inflammation. This similarity explains the very high model score, but the score reflects proximity to rheumatoid disease rather than clinical proof in children.

The only publication retrieved for this specific disease concerns leflunomide, not chloroquine. No study in the data directly tests chloroquine in this condition, so the rationale remains theoretical.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Prospective cohort | The Journal of Rheumatology | Real-life long-term experience with leflunomide in juvenile idiopathic arthritis; does not evaluate chloroquine |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## India Market Information

At least 20 valid single-ingredient registrations are recorded; the list may be partial. Approved indication text is not recorded in the local data.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 18912 | Amoquin 50mg Syrup | Bottle of 60 ml Syrup | Valid |
| 24267 | Arquin 250mg Syrup | Bottle of 450 ml Syrup | Valid |
| 32661 | Bitaquine 40mg Injection | Vial of 30 ml Injection | Valid |
| 32698 | Babyquin 125mg Syrup | Bottle of 60 ml Syrup | Valid |
| 33730 | Babyquin 80mg Drop | Packet of 15 ml Drop | Valid |
| 42381 | Ceequine 250mg Tablet | Strip of 10 tablets | Valid |
| 79394 | Emquin 64.5mg Injection | Vial of 15 ml Injection | Valid |
| 127608 | Leoquin EC 250mg Tablet | Strip of 10 tablets | Valid |
| 128289 | Lariquin 500mg Tablet | Strip of 10 tablets | Valid |
| 139540 | Malacure 250mg Tablet | Strip of 10 tablets | Valid |
| 144057 | Malaquin 250mg Suspension | Bottle of 60 ml Suspension | Valid |
| 144526 | Malabest 250mg Tablet | Bottle of 100 tablets | Valid |
| 147098 | Malarbin 50mg Suspension | Bottle of 60 ml Suspension | Valid |
| 147598 | Malswift 40mg Injection | Vial of 30 ml Injection | Valid |
| 148233 | Malgo 250mg Tablet | Strip of 10 tablets | Valid |
| 180500 | Paraquin DS 500mg Tablet | Strip of 6 tablets | Valid |
| 184048 | Quinowin 250mg Tablet | Strip of 10 tablets | Valid |
| 184408 | Resochin Tablet | Strip of 10 tablets | Valid |
| 197203 | Rimoquin Injection | Vial of 30 ml Injection | Valid |
| 197396 | Ros Q 500mg Tablet | Strip of 6 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications / conditions requiring caution (from drug-disease relations, not label text)**: epilepsy, porphyria, liver disease, eye and retinal disease, vision and hearing disorders, psoriasis, neutropenia, agranulocytosis, leukopenia, anemia, G6PD deficiency, substance abuse/dependence, and certain metabolic disorders (glycogen storage disease, cystinuria, galactosemia).
- **Drug Interactions**: 467 interactions are recorded. Major-level examples include agalsidase beta, bupropion, cisapride, clarithromycin, dolasetron and granisetron (several of these are QT-prolonging or otherwise high-risk combinations). Moderate-level examples include antacids, cimetidine, famotidine, metronidazole, and sulfonylureas and insulin (glucose-lowering effects).
- **Cardiac signal in related literature**: a case report describes third-degree atrioventricular block under chloroquine therapy in a patient with juvenile-onset arthritis. This warrants attention in any paediatric use.

Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials and no study that tests chloroquine in this disease, so the evidence level is L5. Cardiac and retinal safety concerns add caution for paediatric use.

**To proceed, the following is needed:**
- Studies directly evaluating chloroquine in RF-positive polyarticular JIA
- Mechanism of action data
- Package insert warnings and contraindications from the India label
- Paediatric dosing and a cardiac and ophthalmic safety monitoring plan

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: chloroquine phosphate prescribing information, Rising Pharma Holdings, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=06c69e2b-211b-4746-9f3a-f86d36520570) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

