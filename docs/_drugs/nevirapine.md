---
layout: default
title: Nevirapine
parent: Model Prediction Only (L5)
nav_order: 589
evidence_level: L5
indication_count: 3
monitor_inn: "Nevirapine"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-30
description: "Nevirapine: predicted new indication Simian immunodeficiency virus infection (evidence level L5). Approved use: Not recorded in the local data"
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
| Number of Registrations | 9 (valid: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI). Its efficacy in HIV infection is established, and the predicted disease involves a closely related lentivirus that also depends on reverse transcriptase.

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

Nine valid single-ingredient registrations are on record. The licence records contain no approved-indication text. The first five are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 157101 | Neviretro 200mg Tablet (Alkem Laboratories) | Strip of 10 tablets | Not stated in records |
| 152025 | Nevimune 400mg Tablet XR (Cipla) | Strip of 10 extended-release tablets | Not stated in records |
| 155632 | Nevir 200mg Tablet (Emcure) | Bottle of 60 tablets | Not stated in records |
| 157236 | Nevirex 200mg Tablet (Veritaz Healthcare) | Strip of 10 tablets | Not stated in records |
| 156337 | Nevimune Tablet (Cipla) | Bottle of 60 tablets | Not stated in records |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

