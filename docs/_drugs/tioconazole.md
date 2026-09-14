---
layout: default
title: Tioconazole
parent: 僅模型預測 (L5)
nav_order: 831
evidence_level: L5
indication_count: 3
---

# Tioconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using no specific skill (routine report generation task, no skill match).

# Tioconazole: From Topical Fungal Infections to Vulvovaginitis

## One-Sentence Summary

> Tioconazole is a topical imidazole antifungal historically used to treat dermatophyte and *Candida* skin/vaginal infections. The TxGNN model predicts it may also be effective for **Vulvovaginitis**, with **2 registered clinical trials** and **20 publications** currently available as supporting context.
> Most of this literature actually documents tioconazole's long-established use in vulvovaginal candidiasis rather than a formally distinct "vulvovaginitis" trial program, so this is best read as evidence for a closely adjacent, already-familiar use rather than a novel mechanism.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No India marketing authorization on file; per pharmacological reference data, tioconazole is used topically for dermatophyte (*Tinea pedis, cruris, corporis*) and *Candida* infections |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L3 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Tioconazole is an imidazole antifungal whose primary target is the fungal cytochrome P450 enzyme lanosterol 14-α demethylase (CYP51/ERG11). By blocking conversion of lanosterol to ergosterol — an essential fungal cell-membrane component — it disrupts membrane integrity and kills susceptible fungi and yeasts, most notably *Candida albicans*. It also has documented off-target inhibition of human CYP8B1, an enzyme in the bile-acid biosynthesis pathway.

Tioconazole's known clinical use already spans superficial dermatophyte infections and vaginal candidiasis. Vulvovaginitis is frequently caused by *Candida* species, so the same antifungal mechanism that clears vaginal candidiasis is mechanistically applicable whenever the underlying vulvovaginitis is fungal in origin. This is not a mechanistic leap so much as a re-labeling of an indication that overlaps heavily with tioconazole's traditional use — the drug has decades of published clinical experience (single-dose and multi-day regimens, comparisons with clotrimazole, econazole, and systemic ketoconazole) in essentially this same disease space, even though it is not registered under the specific term "vulvovaginitis" in this Evidence Pack.

Because the TxGNN score is very high (99.23%) but the drug is not currently marketed in India and no India-specific label data exists, the prediction should be understood as confirming a biologically plausible and historically supported use rather than identifying a genuinely new mechanism of action.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06056947](https://clinicaltrials.gov/study/NCT06056947) | Phase 3 | Completed | 577 | Compared new fenticonazole+tinidazole+lidocaine formulations against Gynomax® XL ovule in bacterial vaginosis, candidal vulvovaginitis, trichomonal vaginitis and mixed infections; not a tioconazole trial, but establishes the modern comparator landscape for this disease category |
| [NCT03839875](https://clinicaltrials.gov/study/NCT03839875) | Phase 4 | Completed | 116 | Open-label, single-arm study of Gynomax® XL ovule across the same mixed vaginal infection indications; again not tioconazole-specific |

*Note: neither registered trial evaluates tioconazole directly; they support the disease category rather than the drug itself.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | RCT | Antimicrob Agents Chemother | Single-dose 6.5% tioconazole ointment vs. 3-day clotrimazole in vulvovaginal candidiasis; comparable cure rates (84% vs 85% at 4 weeks) |
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | RCT (double-blind vs placebo) | Gynakologische Rundschau | Double-blind comparison of tioconazole vs placebo in vaginal candidiasis, including systemic absorption assessment |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Review | Expert Rev Anti Infect Ther | Reviews non-invasive azole treatment options for vulvovaginal candidiasis, including recurrent disease |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Review | Drugs | Comprehensive review of tioconazole's antimicrobial activity and therapeutic use in superficial mycoses, including vaginal candidiasis |
| [10470518](https://pubmed.ncbi.nlm.nih.gov/10470518/) | 1999 | Review | Comprehensive Therapy | Reviews epidemiology, diagnosis and therapy of vulvovaginitis in healthy women |
| [6873744](https://pubmed.ncbi.nlm.nih.gov/6873744/) | 1983 | Open-label comparative | Gynakologische Rundschau | 3-day tioconazole cream vs. econazole ovules in vaginal candidiasis |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | Open-label comparative | Gynakologische Rundschau | 3-day tioconazole vs. econazole treatment comparison in vaginal candidiasis |
| [4025721](https://pubmed.ncbi.nlm.nih.gov/4025721/) | 1985 | Clinical/cytological assessment | Ala J Med Sci | Clinical and cytological assessment of tioconazole in vulvovaginal candidiasis |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | RCT (open, randomized) | J Int Med Res | Single-dose topical tioconazole vs. 5-day systemic ketoconazole; topical arm had faster symptom resolution |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | Cohort study | Acta Obstet Gynecol Scand | 603-woman contraceptive-clinic cohort; tioconazole 2% cream achieved 88.5% mycological cure vs. 58.8% spontaneous cure in untreated symptomatic controls |

---

## India Market Information

Currently no marketing authorization for tioconazole is on record in India (`market_status: 未上市`, 0 registrations). No product-level details (brand name, dosage form, approved indication text) are available for this evaluation.

---

## Safety Considerations

**Drug Interactions:**
- **Omeprazole** — interaction flagged in DDInter, severity level unclassified ("Unknown")
- Pharmacology data indicate tioconazole inhibits human **CYP8B1**, an enzyme in the bile-acid biosynthesis pathway; clinical significance of this off-target activity for systemic exposure has not been characterized in the available data

No warnings or contraindication data are currently available for this drug; please refer to the package insert (once obtained) for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Substantial historical literature supports tioconazole's efficacy in vulvovaginal candidiasis (mechanistically overlapping with the predicted "vulvovaginitis" indication), but the drug has no India marketing authorization, and a **Blocking** data gap on India-specific label warnings/contraindications prevents completion of the initial safety screening (S1).

**To proceed, the following is needed:**
- India/TFDA-equivalent label data (warnings, contraindications) to clear the S1 safety gate
- Formal, sourced mechanism-of-action documentation (current MOA field is a data gap)
- Confirmation of whether tioconazole is intended for a specific route/formulation (vaginal ointment/cream) suitable for a vulvovaginitis indication in the target market
- Clarification on how "vulvovaginitis" as predicted differs from the already well-documented "vulvovaginal candidiasis" use, to determine if this represents genuinely new indication scope or label harmonization only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

