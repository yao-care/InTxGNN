---
layout: default
title: Metamizole
parent: Moderate Evidence (L3-L4)
nav_order: 530
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Metamizole: predicted new indication Rheumatoid arthritis (evidence level L4). Approved use: Not stated in the approval records compiled for this report (analgesi…"
monitor_inn: "Metamizole"
predicted_indications: ["rheumatoid arthritis", "migraine disorder", "migraine with or without aura, susceptibility to", "exostosis", "migraine with brainstem aura", "gout", "antithrombin deficiency type 2", "brachydactyly-syndactyly syndrome", "tendinitis", "factor 5 excess with spontaneous thrombosis"]
---

# Metamizole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

## Metamizole: From Analgesic/Antipyretic Use to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Metamizole is a non-opioid analgesic and antipyretic that is marketed in India as both tablets and injections.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but **no clinical trials** are registered and the **9 publications** retrieved mainly address safety and prescribing patterns, not efficacy.
The evidence for this prediction is therefore weak. The only migraine-related prediction with some supportive literature is a stronger research question.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the approval records compiled for this report (analgesic/antipyretic use is inferred from the drug class) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general knowledge, metamizole is a non-opioid analgesic and antipyretic with weak anti-inflammatory activity. It is thought to act through central COX inhibition and possibly through cannabinoid and opioidergic pathways.

This could plausibly give symptomatic pain relief in rheumatic disease. However, there is no evidence that it modifies the course of rheumatoid arthritis. The retrieved literature is about safety (agranulocytosis when used alongside methotrexate, drug interactions, hypersensitivity) and prescribing patterns, not about efficacy. The high TxGNN score is not supported by clinical data.

**Other predictions reviewed:**
- **Migraine disorder (99.72%)**: The most plausible alternative. The literature includes a small randomized, single-blind comparison of intravenous dipyrone versus lysine clonixinate in severe migraine attacks, plus reviews and clinical surveys. Evidence level L3, a research question. A preclinical study also raises a caution signal for medication-overuse headache.
- **Migraine with or without aura, susceptibility to (99.70%)**: Essentially a duplicate of the migraine disorder entry; it is not independent evidence.
- **Migraine with brainstem aura (99.67%)**: Only a primary care survey was found; there is no subtype-specific evidence.
- **Exostosis, gout, tendinitis, antithrombin deficiency type 2, brachydactyly-syndactyly syndrome, factor 5 excess with spontaneous thrombosis**: No clinical or literature evidence. For gout and tendinitis, only symptomatic pain relief is conceivable. For the genetic and coagulation disorders, no plausible mechanism exists.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42604876](https://pubmed.ncbi.nlm.nih.gov/42604876/) | 2026 | Pharmacovigilance analysis | Naunyn-Schmiedeberg's Arch Pharmacol | Analysis of whether agranulocytosis is disproportionately reported when metamizole is used with methotrexate for RA |
| [40188149](https://pubmed.ncbi.nlm.nih.gov/40188149/) | 2025 | Pharmacovigilance analysis | Arthritis Res Ther | Methotrexate-related kidney and liver adverse reactions in RA, and the effect of concomitant analgesics |
| [33825975](https://pubmed.ncbi.nlm.nih.gov/33825975/) | 2021 | Claims data analysis | Z Rheumatol | Analgesic prescription frequency in RA, axSpA, PsA and SLE in Germany |
| [21412604](https://pubmed.ncbi.nlm.nih.gov/21412604/) | 2011 | Observational | Rev Bras Reumatol | Potential drug interactions in RA patients with polypharmacy |
| [18679134](https://pubmed.ncbi.nlm.nih.gov/18679134/) | 2008 | Observational cohort | J Clin Rheumatol | Drug allergy frequency in SLE compared with RA |
| [23238666](https://pubmed.ncbi.nlm.nih.gov/23238666/) | 2013 | Pharmacodynamic review | Thromb Haemost | NSAID interference with the antiplatelet effect of aspirin |

None of these studies tests whether metamizole treats rheumatoid arthritis.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 844 | ANALGIN 500MG TABLET (Alkem Laboratories) | Strip of 10 tablets | Not specified in the records |
| 17378 | Andep 0.5mg Tablet (Ravian Pharmaceuticals) | Strip of 10 tablets | Not specified in the records |
| 26735 | Bral 500mg Tablet (Micro Labs) | Strip of 10 tablets | Not specified in the records |
| 231303 | Ultragin 500mg Injection (Pfizer) | Vial of 30 ml injection | Not specified in the records |
| 153086 | Novalgin RC 0.5% Injection (Sanofi India) | Vial of 30 ml injection | Not specified in the records |

All five registrations are valid single-ingredient products, covering oral and injectable routes.

---

## Safety Considerations

Please refer to the package insert for safety information.

The retrieved literature does flag the following signals:
- **Agranulocytosis**: Metamizole is itself associated with agranulocytosis, and a pharmacovigilance study examined this risk when it is used alongside methotrexate in RA. Several reviews note it is banned in some countries because of life-threatening blood disorders.
- **Hypersensitivity**: A case report describes toxic epidermal necrolysis after metamizole.
- **Medication-overuse headache**: A preclinical rat study suggests repeated exposure may induce latent sensitization.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For rheumatoid arthritis, there are no registered trials and no efficacy studies, only safety and prescribing-pattern literature. The high model score is not supported by clinical data. Migraine has more supportive literature, but this is a small regional randomized comparison and heterogeneous reviews, and the agranulocytosis risk limits use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator, including approved indications (a blocking gap for safety screening)
- Mechanism of action data
- For migraine, a focused evidence review of randomized trials, followed by a benefit-risk assessment that accounts for agranulocytosis
- For rheumatoid arthritis, direct efficacy evidence before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

