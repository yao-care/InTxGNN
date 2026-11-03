---
layout: default
title: Luliconazole
parent: Model Prediction Only (L5)
nav_order: 509
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-03
monitor_inn: "Luliconazole"
predicted_indications: ["endothrix infectious disease", "ectothrix infectious disease"]
description: "Luliconazole: predicted new indication Endothrix infectious disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Luliconazole
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

## Luliconazole: Endothrix infectious disease
{: .text-alpha }

## One-Sentence Summary

Luliconazole is a topical imidazole antifungal, originally used for tinea pedis, tinea corporis and other dermatophyte infections of the skin.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Endothrix infectious disease |
| TxGNN Prediction Score | 0.9910 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, luliconazole is a topical imidazole antifungal that inhibits lanosterol 14-alpha-demethylase, an enzyme needed to make ergosterol, a key component of the fungal cell membrane. Its efficacy in dermatophyte infections is established, and mechanistically it may be applicable to pityriasis versicolor.

Pityriasis versicolor is a superficial skin infection caused by *Malassezia* yeasts, and these organisms are susceptible to azole antifungals. Published work also notes that luliconazole has broad activity against dermatophytes, *Candida* and *Malassezia*. Because the drug is already marketed in India as a topical product for dermatophytosis, its topical use is familiar and the new indication is a short step from the existing one.

Superficial mycosis is close to an on-label extension. The hair-shaft and deep follicular infections are less promising, because topical drugs penetrate poorly there and oral therapy is usually standard.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27559523](https://pubmed.ncbi.nlm.nih.gov/27559523/) | 2016 | RCT (prospective, open, randomized) | Indian Dermatology Online Journal | Compared topical ketoconazole and topical luliconazole in pityriasis versicolor at a tertiary care hospital in eastern India. No abstract was available, so results are not summarized here. |
| [29198426](https://pubmed.ncbi.nlm.nih.gov/29198426/) | 2018 | In vitro study | Journal de Mycologie Medicale | Luliconazole inhibits sterol 14-α-demethylase and is active against dermatophytes, *Candida* and *Malassezia*. It has been used clinically for pityriasis versicolor and dermatophytosis. |

## India Market Information

There are 20 valid single-ingredient registrations, all topical (creams and lotions). Approved indication text was not available for these registrations. The main ones are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 127415 | Lucaf 1% Cream (Gary Pharmaceuticals) | Cream, 20 g tube | Not stated |
| Registration No. 123876 | Lucoz Lotion (Ajanta Pharma) | Lotion, 15 ml bottle | Not stated |
| Registration No. 121984 | Ludura Lotion (Cipla) | Lotion, 30 ml bottle | Not stated |
| Registration No. 248083 | Zole 1% Cream (Sun Pharmaceutical) | Cream, 50 g tube | Not stated |
| Registration No. 121555 | Lulimac Cream (Macleods) | Cream, 20 g tube | Not stated |

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found, and no contraindication records were found in the knowledge graph.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is plausible, the drug is already marketed in India as a topical product, and a randomized comparative study already exists in pityriasis versicolor. However, the only registered trial is Phase 4 and has not yet started recruiting, and the published RCT had no abstract available for review. Evidence is therefore moderate (L3) rather than confirmatory.

**To proceed, the following is needed:**
- Results from the 2016 Indian RCT (PMID 27559523) and from NCT07333170 once available
- Package insert warnings and contraindications for the Indian products (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Confirmation of the concentration (the registered products are 1% creams, while the trial uses 2%) and the treatment duration for pityriasis versicolor
- Approved indication text for the Indian registrations

**Notes on other predicted indications:**
- **Superficial mycosis** (L3): close to the existing indication, so it is a low-risk, near on-label extension, but it is not a true new repurposing opportunity.
- **Cutaneous candidiasis** (L4): evidence is limited to animal and formulation studies, so it remains a research question.
- **Majocchi granuloma** (L4): only case reports are available, and deep infection limits topical efficacy, so it remains a research question.
- **Scalp or beard dermatophytosis, endothrix and ectothrix infections**: hold, because there is no supportive efficacy evidence and hair-follicle penetration is limited.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

