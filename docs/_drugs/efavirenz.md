---
layout: default
title: Efavirenz
parent: Model Prediction Only (L5)
nav_order: 298
evidence_level: L5
indication_count: 3
monitor_inn: "Efavirenz"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-11-24
description: "Efavirenz: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease, AIDS"
---

# Efavirenz
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

## Efavirenz: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Efavirenz is a non-nucleoside reverse transcriptase inhibitor originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are **0 clinical trials** and only **1 publication** (an in vitro biochemical and structural study), so the evidence is very limited. This is a veterinary indication with no human clinical relevance.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease, AIDS (relation recorded in the knowledge graph; the local licence records contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9980 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (15 of 15) – CDSCO approval status is not included in this data |
| Number of Listed Products | 15 (valid: 15) |
| Number of Approvals | 15 licences (all single-ingredient products) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for efavirenz: "Efavirenz is an antiviral drug. […] Efavirenz is an NNRTI of HIV-1. Efavirenz activity is mediated predominantly by noncompetitive inhibition of HIV-1 reverse transcriptase. HIV-2 reverse transcriptase and human cellular DNA polymerases α,β, γ, and δ are not inhibited by efavirenz." ([DailyMed: efavirenz prescribing information, Macleods Pharmaceuticals Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=13ca3456-e5bf-4bb1-af95-b1378658a358), label version 2024-06-28; accessed 2026-11-19.) Based on known information, efavirenz is an HIV-1 non-nucleoside reverse transcriptase inhibitor (NNRTI). Its use in HIV infection is recorded in the knowledge graph, and mechanistically it may be applicable to related lentiviruses.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV and causes an AIDS-like syndrome in cats. No effective treatment has been established for infected cats. The only available publication (PMID 38031646, 2023) compares NNRTIs, including efavirenz, against feline and human immunodeficiency virus reverse transcriptases in biochemical and structural terms. It tested efavirenz alongside nevirapine and rilpivirine, but the summary available does not report efavirenz-specific results.

FIV reverse transcriptase differs structurally from that of HIV-1 and is generally reported to be less susceptible to NNRTIs. The very high TxGNN score therefore should not be read as proof of efficacy. Because the study is in vitro only and does not test the disease in animals or patients, the evidence is capped at L5 under the grading rules, even though the data pack suggests L4.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | In vitro biochemical/structural study | Journal of Veterinary Science | Compared nevirapine, efavirenz and rilpivirine against feline and human immunodeficiency virus reverse transcriptases to assess NNRTI potential for treating FIV infection; efavirenz-specific results not available in the summary |

Related literature on simian immunodeficiency virus (SIV) models was also retrieved. Wild-type SIV is intrinsically resistant to NNRTIs, and those macaque studies use a chimeric virus carrying HIV-1 reverse transcriptase. They are therefore not evidence for feline AIDS and are not listed here.

## India Market Information

Efavirenz is marketed in India. All 15 licences are single-ingredient products, and none of the records contain approved-indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 73279 | Efavir 600 Tablet | Bottle of 30 tablets | Valid |
| 73774 | Efavir 200mg Capsule | Strip of 30 capsules | Valid |
| 75401 | Estiva 600 Capsule | Strip of 30 capsules | Valid |
| 76025 | Efamat 600mg Tablet | Strip of 30 tablets | Valid |
| 77133 | Efcure 600mg Tablet | Strip of 30 tablets | Valid |
| 77516 | Efavir 200mg Tablet | Bottle of 60 tablets | Valid |
| 78724 | Efarenz 600 Tablet | Bottle of 30 tablets | Valid |
| 79155 | Efferven 600mg Tablet | Strip of 30 tablets | Valid |
| 79253 | Efcure 200mg Tablet | Strip of 30 tablets | Valid |
| 80758 | Evirenz 600mg Tablet | Strip of 30 tablets | Valid |
| 81471 | Effahope 600mg Tablet | Strip of 30 tablets | Valid |
| 81571 | Evirenz 200mg Tablet | Strip of 10 tablets | Valid |
| 83003 | Efferven 200mg Capsule | Strip of 10 capsules | Valid |
| 193479 | Revenz 600mg Tablet | Strip of 10 tablets | Valid |
| 236026 | Viranz 600mg Capsule | Strip of 30 capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Knowledge-graph contraindication relations** (recorded in the knowledge graph, not taken from label text): liver failure, liver disease, fatty liver disease, non-alcoholic steatohepatitis, chronic hepatitis B and C virus infection, kidney disease, Fanconi renotubular syndrome, lactic acidosis, epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder, delusional disorder, paranoid schizophrenia, gallbladder disease, hypertriglyceridemia, obesity, hypophosphatemia, osteomalacia and rickets.
- **Drug Interactions**: 330 interactions are recorded. The only Major interaction in the retrieved list is with **dolasetron**. Moderate interactions include clarithromycin, bupropion, aprepitant, dexamethasone, hydrocortisone, betamethasone, triamcinolone, pioglitazone, saxagliptin, famotidine, rabeprazole, loperamide, dronabinol, minocycline and acarbose.

Please refer to the package insert for warnings and label contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting study is an in vitro biochemical and structural comparison, with no clinical trials and no animal or field data in cats. FIV reverse transcriptase is generally less susceptible to NNRTIs than HIV-1 reverse transcriptase, and this is a veterinary rather than human indication.

**To proceed, the following is needed:**
- Efavirenz-specific enzyme inhibition and cell-based antiviral data against FIV
- Veterinary safety and pharmacokinetic data in cats
- Mechanism of action data and package insert warnings and contraindications for the marketed products

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: efavirenz prescribing information, Macleods Pharmaceuticals Limited](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=13ca3456-e5bf-4bb1-af95-b1378658a358) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

