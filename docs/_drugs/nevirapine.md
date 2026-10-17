---
layout: default
title: Nevirapine
parent: Model Prediction Only (L5)
nav_order: 589
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Nevirapine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease"
monitor_inn: "Nevirapine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
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

# Nevirapine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Nevirapine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, a veterinary condition,
but **no clinical trials** and only **1 preclinical publication** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, nevirapine is an NNRTI that targets HIV-1 reverse transcriptase, and its efficacy in HIV infection is established. Mechanistically, it could be applicable to feline immunodeficiency virus (FIV), which is also a lentivirus that depends on reverse transcriptase.

There is an important caveat. NNRTIs bind a pocket in HIV-1 reverse transcriptase that differs structurally in related lentiviruses, and they are generally poorly active against them. A 2023 study compared nevirapine, efavirenz and rilpivirine against feline and human immunodeficiency virus enzymes. The data compiled for this report do not include its specific findings on nevirapine, so activity against FIV cannot be confirmed.

The high TxGNN score is a computational prediction, not clinical evidence. This is also a veterinary indication with no direct human relevance.

Two other predictions were reviewed and are not clinically actionable:
- **Simian immunodeficiency virus infection** (score 99.85%, evidence level L4, Hold): the literature consists of in vitro and animal-model studies, and wild-type SIV reverse transcriptase is naturally resistant to NNRTIs. Chimeric SHIV viruses carrying HIV-1 reverse transcriptase are research tools for testing HIV-1 drugs, not a repurposing indication.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 99.82%, evidence level L5, Hold): there are no trials or literature and no mechanistic link can be established.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | Preclinical (biochemical/structural) | Journal of Veterinary Science | Compares NNRTIs (nevirapine, efavirenz, rilpivirine) against feline and human immunodeficiency virus reverse transcriptase to assess potential for FIV treatment. No effective treatment exists for infected cats. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 157101 | Neviretro 200mg Tablet (Alkem Laboratories) | Strip of 10 tablets | Not stated |
| 152025 | Nevimune 400mg Tablet XR (Cipla) | Strip of 10 extended-release tablets | Not stated |
| 155632 | Nevir 200mg Tablet (Emcure) | Bottle of 60 tablets | Not stated |
| 157236 | Nevirex 200mg Tablet (Veritaz Healthcare) | Strip of 10 tablets | Not stated |
| 156337 | Nevimune Tablet (Cipla) | Bottle of 60 tablets | Not stated |

Nine valid single-ingredient registrations are on record; the five above are shown. All are oral tablets.

## Safety Considerations

- **Contraindications and disease associations (from knowledge graph, not label text)**: liver failure, liver disease, gallbladder disease, drug-induced liver injury, chronic hepatitis B and C virus infection, rash (exanthem), Stevens-Johnson syndrome, toxic epidermal necrolysis (Lyell syndrome), rhabdomyolysis, nodular fasciitis.
- **Drug Interactions**: 207 interactions are recorded. The main ones listed are all moderate severity, including:
  - Corticosteroids (dexamethasone, betamethasone, budesonide, prednisolone, triamcinolone)
  - Clarithromycin
  - Bupropion
  - Aprepitant
  - Rabeprazole
  - Ondansetron and granisetron
  - Naltrexone, naloxegol and naldemedine
  - Cisapride
  - Saxagliptin and linagliptin
  - Eliglustat, nitisinone and orlistat

Package insert warnings were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is veterinary, supported only by one preclinical publication with no clinical trials, and NNRTIs are generally weakly active against non-HIV lentiviral reverse transcriptases. The high TxGNN score alone is not sufficient evidence, and the other predicted indications (SIV infection and the rare neurodevelopmental disorder) are not clinically actionable.

**To proceed, the following is needed:**
- Review of the full 2023 FIV study for nevirapine-specific results
- Mechanism of action data
- Package insert warnings and contraindications (from the India regulatory source), including the approved indication text
- In vivo efficacy and safety data in cats, if a veterinary direction is pursued
- A clear hepatotoxicity and rash risk assessment given the safety signals above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

