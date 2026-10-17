---
layout: default
title: Tioconazole
parent: Moderate Evidence (L3-L4)
nav_order: 838
evidence_level: L3
indication_count: 3
last_modified_at: 2026-10-14
description: "Tioconazole: predicted new indication Vulvovaginitis (evidence level L3). Approved use: Vulvovaginal candidiasis"
monitor_inn: "Tioconazole"
predicted_indications: ["vulvitis", "postmenopausal atrophic vaginitis"]
---

# Tioconazole
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Tioconazole: From Vulvovaginal Candidiasis to Vulvovaginitis

## One-Sentence Summary

Tioconazole is an imidazole antifungal, originally used to treat vulvovaginal candidiasis.
The TxGNN model predicts it may be effective for **vulvovaginitis**, but this is largely a broader label for the already-approved use rather than a true new indication.
Support comes from **0 registered clinical trials** and **20 publications**, most of them older studies on vaginal candidiasis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vulvovaginal candidiasis |
| Predicted New Indication | Vulvovaginitis |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L3 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled record. Based on the known drug class, tioconazole is an imidazole antifungal. In fungi and yeast it is understood to inhibit lanosterol 14-alpha-demethylase (CYP51/ERG11), blocking ergosterol synthesis and disrupting the fungal cell membrane.

Vulvovaginitis is largely caused by Candida species, so the prediction is essentially the approved vulvovaginal candidiasis use under a broader label. It generalises the existing indication rather than opening a new disease area. The evidence does not extend to non-fungal vulvovaginitis (such as bacterial vaginosis or non-infectious causes), where an azole would not be expected to work. One small open-label study did report cure in trichomoniasis and mixed vaginal infections, but this is limited evidence.

Two other predictions were also generated, with weaker support:
- **Vulvitis** (score 99.20%, evidence level L3): the mechanism applies to candidal vulvitis, which usually accompanies vaginal candidiasis. The literature is the same set as for vulvovaginitis and does not address vulvitis as a separate condition. The high score likely reflects network proximity to the approved indication.
- **Postmenopausal atrophic vaginitis** (score 99.19%, evidence level L5, Hold): no clear mechanistic link, because this condition is driven by estrogen deficiency rather than fungal infection. No trials or literature support it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | RCT | Antimicrob Agents Chemother | 80 patients; single-dose 6.5% tioconazole vs 3-day clotrimazole. 84% vs 85% remained asymptomatic at 4 weeks |
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | Double-blind placebo-controlled trial | Gynakol Rundsch | Tioconazole vs placebo in vaginal candidiasis, with assessment of systemic absorption |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Review | Drugs | Broad in vitro antimicrobial activity; trials show efficacy and safety of topical tioconazole in superficial yeast infections and vaginal candidiasis |
| [40464716](https://pubmed.ncbi.nlm.nih.gov/40464716/) | 2025 | Review | Expert Rev Anti Infect Ther | Future non-invasive azole options for vulvovaginal candidiasis, including recurrent disease |
| [3216880](https://pubmed.ncbi.nlm.nih.gov/3216880/) | 1988 | Clinical study | Mycoses | Tioconazole in the treatment of vaginal candidosis |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | Open-label comparative trial | Gynakol Rundsch | Tioconazole vs econazole, 3-day treatment of vaginal candidiasis |
| [6873744](https://pubmed.ncbi.nlm.nih.gov/6873744/) | 1983 | Open-label comparative trial | Gynakol Rundsch | Tioconazole cream vs econazole ovules, 3-day treatment |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | Clinical study | Acta Obstet Gynecol Scand | 2% vaginal cream for 3 days in 29 symptomatic women; mycological cure rate 88.5% |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | Open-label, non-comparative | J Int Med Res | 2% cream in 20 patients with T. vaginalis or mixed infections; 95% cured at first follow-up |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | Open randomised study | J Int Med Res | 40 patients; single-dose topical tioconazole 6% vs 5 days oral ketoconazole. Both eradicated infection; topical symptoms resolved faster |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 238244 | Vcandi Gel | Vaginal gel (5 g tube) | Not specified in the compiled data |

## Safety Considerations

**Drug Interactions**
- Omeprazole: interaction listed in the DDInter database, severity level unknown.
- CYP8B1 (human enzyme): tioconazole inhibits this enzyme, which participates in bile acid biosynthesis. This is a pharmacology finding rather than a drug-drug interaction.

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
For vulvovaginitis of candidal origin, evidence is reasonable. It includes randomised and placebo-controlled trials of tioconazole in vaginal candidiasis, but these are old (1980s) and no trials are registered. The prediction should be treated as a broader label for the existing indication, not a new one. Use in non-fungal vulvovaginitis, vulvitis of other causes, or atrophic vaginitis is not supported.

**To proceed, the following is needed:**
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data confirmed from DrugBank
- The approved indication text for the Indian product
- Clear restriction of the target population to candidal vulvovaginitis, with diagnostic confirmation
- Modern controlled data on non-Candida vulvovaginitis, if broader use is intended
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

