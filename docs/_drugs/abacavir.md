---
layout: default
title: Abacavir
parent: Model Prediction Only (L5)
nav_order: 11
evidence_level: L5
indication_count: 3
monitor_inn: "Abacavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-11-24
description: "Abacavir: predicted new indication feline acquired immunodeficiency syndrome (evidence level L5). In India: 9 listed products (9 not discontinued)"
---

# Abacavir
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

## Abacavir: Nucleoside reverse transcriptase inhibitor → feline acquired immunodeficiency syndrome
{: .text-alpha }

## One-Sentence Summary

Abacavir is a nucleoside reverse transcriptase inhibitor (NRTI) used against HIV.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, a veterinary condition,
but the data compiled for this report contain **0 clinical trials** and only **1 publication**, an older in vitro study of a three-drug combination.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9979 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (9 of 9) – CDSCO approval status is not included in this data |
| Number of Listed Products | 9 (valid: 9) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for abacavir and lamivudine (a combination product containing abacavir): "Abacavir and lamivudine is an antiretroviral agent with activity against HIV-1." ([DailyMed: abacavir and lamivudine prescribing information, Laurus Labs Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d12e80eb-906c-4932-bb03-b4060ba1d31c), label version 2026-09-18; accessed 2026-11-19.) Based on general knowledge, abacavir belongs to the NRTI class, which blocks the reverse transcriptase enzyme that HIV uses to copy its genetic material.

Feline immunodeficiency virus (FIV) is a lentivirus whose reverse transcriptase is related to that of HIV. For this reason, it is biologically plausible that NRTIs could act against FIV. The single publication found (2002) tested a combination of zidovudine, lamivudine and abacavir against FIV in vitro. Abacavir's own contribution cannot be separated from the combination.

This is a veterinary indication with no direct human clinical relevance. The study does not directly establish efficacy of abacavir for feline AIDS in animals, so the evidence level is capped at L5.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11684314](https://pubmed.ncbi.nlm.nih.gov/11684314/) | 2002 | Preclinical combination study (inferred from title) | Antiviral Research | Zidovudine, lamivudine and abacavir combination therapy was evaluated for suppression of FIV replication in vitro. The cat is discussed as an animal model for HIV. Full text was not reviewed. |

---

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 1957 | Abamune Tablet | Strip of 30 tablets | Valid |
| 2296 | Abamune L 600 mg/300 mg Tablet | Strip of 30 tablets | Valid |
| 3740 | Albavir Tablet | Strip of 30 tablets | Valid |
| 4975 | A-Bec Tablet | Bottle of 30 tablets | Valid |
| 6233 | Abalam Tablet | Bottle of 30 tablets | Valid |
| 6487 | Albavir Tablet | Bottle of 30 tablets | Valid |
| 7370 | A Bec L 600mg/300mg Tablet | Strip of 30 tablets | Valid |
| 108303 | Inbec Tablet | Bottle of 30 tablets | Valid |
| 236242 | Virol 300mg Tablet | Bottle of 60 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

---

## Safety Considerations

- **Drug Interactions**: 93 interactions were recorded. The ones listed with a Moderate level are naltrexone and orlistat. The others shown have an unclassified level, including metformin, omeprazole, pantoprazole, lansoprazole, morphine, prednisone, hydrocortisone, vancomycin, amphotericin B and sulfasalazine.
- **Other information**: Abacavir is known to carry a risk of HLA-B*5701-associated hypersensitivity. Package insert warnings and contraindications were not available in the data compiled for this report, so please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score and one in vitro combination study from 2002 that cannot isolate abacavir's effect. The indication is also veterinary, so it has no direct human therapeutic relevance.

**To proceed, the following is needed:**
- Studies that test abacavir alone against FIV, with in vivo data in cats
- Confirmation of whether a veterinary development path is relevant to this programme
- Mechanism of action data and package insert warnings and contraindications

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: abacavir and lamivudine prescribing information, Laurus Labs Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d12e80eb-906c-4932-bb03-b4060ba1d31c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

