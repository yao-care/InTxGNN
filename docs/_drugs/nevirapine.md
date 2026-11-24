---
layout: default
title: Nevirapine
parent: Model Prediction Only (L5)
nav_order: 589
evidence_level: L5
indication_count: 3
monitor_inn: "Nevirapine"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-11-24
description: "Nevirapine: predicted new indication Simian immunodeficiency virus infection (evidence level L5). In India: 9 listed products (9 not discontinued)"
---

# Nevirapine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Nevirapine: Simian immunodeficiency virus infection
{: .text-alpha }

## One-Sentence Summary

Nevirapine is an HIV-1 reverse transcriptase inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**, but there are **no registered clinical trials** and the **14 publications** retrieved are mostly laboratory or animal-model studies, none of which test nevirapine as a treatment for this disease. This is a model prediction with little direct support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (9 of 9) – CDSCO approval status is not included in this data |
| Number of Listed Products | 9 (valid: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for nevirapine: "Nevirapine is an antiretroviral drug. […] Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) of HIV-1. Nevirapine binds directly to reverse transcriptase (RT) and blocks the RNA-dependent and DNA-dependent DNA polymerase activities by causing a disruption of the enzyme's catalytic site." ([DailyMed: nevirapine prescribing information, Aurobindo Pharma Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f6c3eed-2a5d-46ed-9a7c-59715f338a15), label version 2026-10-08; accessed 2026-11-19.) Based on known information, nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI). Its efficacy in HIV infection is established, and the predicted disease involves a closely related lentivirus that also depends on reverse transcriptase.

The high score most likely reflects this shared viral target class rather than true susceptibility. SIV reverse transcriptase is generally intrinsically resistant to NNRTIs. Only chimeric SIV/HIV constructs (SHIV) carrying the HIV-1 reverse transcriptase gene are expected to respond. The retrieved studies use such chimeras as laboratory and animal models for studying antiviral resistance. None of them evaluates nevirapine as a treatment for SIV infection itself.

The indication is relevant mainly to veterinary or preclinical-model research. It offers no human clinical need beyond the already established HIV use. No cited study directly addresses SIV infection as a treatment target for nevirapine, so the evidence level is L5.

The other two predictions are weaker:
- **Feline acquired immunodeficiency syndrome** (score 0.9985): supported by a single biochemical and structural comparison of NNRTIs against feline and human immunodeficiency virus reverse transcriptases (PMID 38031646). It is indirect and has no clinical data.
- **A rare neurodevelopmental disorder with ataxic gait, absent speech and decreased cortical white matter** (score 0.9982): no mechanistic link, trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The table lists the most relevant publications. None tests nevirapine as a treatment for SIV infection in a controlled clinical setting.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11020686](https://pubmed.ncbi.nlm.nih.gov/11020686/) | 2000 | Review | Annals of Emergency Medicine | Non-occupational HIV post-exposure prophylaxis; animal studies of antiretrovirals against SIV provide indirect support |
| [11375059](https://pubmed.ncbi.nlm.nih.gov/11375059/) | 2001 | Animal model study | AIDS Research and Human Retroviruses | RT-SHIV monkey model for studying emergence and reversal of reverse transcriptase drug resistance |
| [19195672](https://pubmed.ncbi.nlm.nih.gov/19195672/) | 2009 | Animal model study | Virology | RT-SHIV carrying HIV-1 reverse transcriptase transmits efficiently by the vaginal route in rhesus macaques |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In vitro study | Journal of Virology | SIV/HIV chimera expressing HIV-1 reverse transcriptase to study NNRTI resistance, because NNRTIs do not effectively inhibit SIV reverse transcriptase |
| [7541200](https://pubmed.ncbi.nlm.nih.gov/7541200/) | 1995 | In vitro study | Biochem Biophys Res Commun | SIV carrying HIV-1 reverse transcriptase is sensitive to NNRTIs, whereas wild-type SIV is not |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro study | Antiviral Therapy | Activity of 16 approved anti-HIV drugs against HIV-2, SIV and SHIV, relevant to treatment and prophylaxis |
| [16859727](https://pubmed.ncbi.nlm.nih.gov/16859727/) | 2006 | In vitro study | Virology | Inhibition of endogenous reverse transcription in HIV-1 and SIV virions by NRTIs and NNRTIs |
| [12234864](https://pubmed.ncbi.nlm.nih.gov/12234864/) | 2002 | In vitro study | Antimicrob Agents Chemother | Integrase inhibitor L-708,906 tested in combination with nevirapine, zidovudine and nelfinavir; combinations were subsynergistic |

## India Market Information

Nine valid single-ingredient registrations are on record. The licence records contain no approved-indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 151136 | Nevimune Tablet | Strip of 10 tablets | Valid |
| 152025 | Nevimune 400mg Tablet XR | Strip of 10 tablet xr | Valid |
| 154488 | Nevihope 200mg Tablet | Bottle of 60 tablets | Valid |
| 155632 | Nevir 200mg Tablet | Bottle of 60 tablets | Valid |
| 156337 | Nevimune Tablet | Bottle of 60 tablets | Valid |
| 156576 | Nevipan 200mg Tablet | Bottle of 60 tablets | Valid |
| 157101 | Neviretro 200mg Tablet | Strip of 10 tablets | Valid |
| 157236 | Nevirex 200mg Tablet | Strip of 10 tablets | Valid |
| 157478 | Nevir -ER Tablet | Packet of 30 tablet er | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** contraindication-type relations are recorded with liver failure, liver disease, drug-induced liver injury, gallbladder disease, chronic hepatitis B and C virus infection, rash (exanthem), Stevens-Johnson syndrome, toxic epidermal necrolysis (Lyell syndrome), rhabdomyolysis and nodular fasciitis. These point mainly to liver and severe skin reaction risks.
- **Drug Interactions:** 207 interactions are recorded. The first 20 listed are all of moderate level, including rabeprazole, bupropion, aprepitant, clarithromycin, dexamethasone, prednisolone, budesonide, ondansetron, granisetron and naltrexone.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model scoring alone. SIV reverse transcriptase is generally resistant to NNRTIs, no clinical trials exist, and no cited study directly tests nevirapine against this disease. The indication also has no apparent human clinical need beyond the existing HIV use, while nevirapine carries liver and severe skin reaction risks and a large interaction burden.

**To proceed, the following is needed:**
- Direct in vitro or animal data on nevirapine activity against wild-type SIV (not only SHIV chimeras)
- Mechanism of action data
- Package insert warnings and contraindications from the India licence holders
- A clear human or veterinary use case that justifies the safety risks

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: nevirapine prescribing information, Aurobindo Pharma Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f6c3eed-2a5d-46ed-9a7c-59715f338a15) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

