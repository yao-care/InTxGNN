---
layout: default
title: Tioconazole
parent: Model Prediction Only (L5)
nav_order: 838
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-03
monitor_inn: "Tioconazole"
predicted_indications: ["vulvitis", "postmenopausal atrophic vaginitis"]
description: "Tioconazole: predicted new indication Vulvitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Tioconazole
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

## Tioconazole: Vulvitis
{: .text-alpha }

## One-Sentence Summary

Tioconazole is a topical imidazole antifungal. The TxGNN model predicts it may be useful for **vulvitis**, but there are **no registered clinical trials** and the retrieved literature (**20 publications**) addresses vaginal candidiasis rather than vulvitis as a separate condition, so the evidence for this specific prediction is limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vulvitis |
| TxGNN Prediction Score | 0.9920 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the compiled drug record. Pharmacology data indicate that tioconazole inhibits the fungal enzyme lanosterol 14-α demethylase (CYP51/ERG11). This enzyme is needed to make ergosterol, a key component of the fungal cell wall, so fungi and yeasts cannot survive without it. Tioconazole also inhibits the human enzyme CYP8B1, which takes part in bile acid synthesis.

If vulvitis is caused by Candida, the same antifungal mechanism could apply, since vulvar involvement often occurs together with vaginal yeast infection. However, the available studies address vulvovaginal candidiasis, not vulvitis as a distinct condition. There is no evidence for non-fungal vulvitis, such as contact dermatitis or lichen sclerosus. The high score most likely reflects network proximity to existing antifungal uses rather than independent evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The retrieved studies concern vaginal or vulvovaginal candidiasis, not vulvitis itself. They are context only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | RCT | Antimicrob Agents Chemother | Single-dose 6.5% tioconazole vs 3-day clotrimazole in 80 patients: 84% vs 85% remained asymptomatic at 4 weeks |
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | Double-blind placebo-controlled trial | Gynakol Rundsch | Tioconazole vs placebo in vaginal candidiasis, with assessment of systemic absorption |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Review | Drugs | Broad antimicrobial activity; topical tioconazole effective and well tolerated in superficial yeast and dermatophyte infections |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Review | Expert Rev Anti Infect Ther | Overview of non-invasive azole options for vulvovaginal candidiasis, including recurrent disease |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | Clinical study | Acta Obstet Gynecol Scand | 2% vaginal cream for 3 days: mycological cure rate 88.5% in symptomatic women |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | Open-label comparative trial | Gynakol Rundsch | 3-day tioconazole vs econazole in vaginal candidiasis |
| [6873744](https://pubmed.ncbi.nlm.nih.gov/6873744/) | 1983 | Open-label comparative trial | Gynakol Rundsch | Tioconazole cream vs econazole ovules over 3 days |
| [3216880](https://pubmed.ncbi.nlm.nih.gov/3216880/) | 1988 | Clinical study | Mycoses | Tioconazole in the treatment of vaginal candidosis |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | Randomized open study | J Int Med Res | Single-dose topical tioconazole vs 5 days of oral ketoconazole in 40 patients; both effective, topical symptoms resolved faster |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | Open non-comparative study | J Int Med Res | 2% cream for 3 days in Trichomonas vaginalis or mixed infections: 95% cured at first follow-up |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 238244 | Vcandi Gel | Vaginal gel (5 g tube) | Not specified in the compiled data |

## Safety Considerations

- **Drug Interactions**: Omeprazole (severity not classified). Tioconazole also inhibits the human enzyme CYP8B1 in pharmacology data.

For other safety information, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or studies directly address vulvitis. The available literature concerns vulvovaginal candidiasis, and the high TxGNN score appears to be a network-based signal. The evidence level is therefore L5.

**To proceed, the following is needed:**
- Studies defining which vulvitis types (for example candidal) could respond to an azole antifungal
- Clinical data in vulvitis specifically, including a comparison with standard care
- Package insert warnings and contraindications for the marketed product
- Confirmed mechanism-of-action documentation

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

