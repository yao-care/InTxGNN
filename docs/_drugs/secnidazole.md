---
layout: default
title: Secnidazole
parent: High Evidence (L1-L2)
nav_order: 758
evidence_level: L1
indication_count: 10
---

# Secnidazole
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Secnidazole: From Established Antimicrobial Use to Vaginal Discharge (Bacterial Vaginosis / Trichomoniasis)

## One-Sentence Summary

> Secnidazole is a 5-nitroimidazole antimicrobial with an internationally validated mechanism against anaerobic bacteria and protozoa (marketed elsewhere as Solosec® for bacterial vaginosis and trichomoniasis), but it is **not currently marketed in India**.
> Among 10 TxGNN-predicted indications for this drug, the model's *highest-scoring* prediction (postmenopausal atrophic vaginitis) has no supporting evidence, while **Vaginal Discharge** — the core presenting symptom of bacterial vaginosis and trichomoniasis — is backed by **5 clinical trials** and **16 publications**, making it the most defensible repurposing signal in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in India (drug not yet marketed); internationally established for bacterial vaginosis and trichomoniasis |
| Predicted New Indication | Vaginal Discharge |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Note on indication selection:** This Evidence Pack contains 10 TxGNN-predicted indications for Secnidazole. The single top-ranked prediction by raw TxGNN score is *postmenopausal atrophic vaginitis* (99.70%), but its own rationale flags it as a likely knowledge-graph false positive (Evidence Level L5, decision = Hold) because atrophic vaginitis is an estrogen-deficiency condition unrelated to antimicrobial mechanisms. This report instead centers on **Vaginal Discharge**, the highest-evidence candidate (L1, Proceed with Guardrails), and provides the full ranking below for transparency.

### All Predicted Indications (TxGNN Ranking Overview)

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|------|------|------|
| 1 | Postmenopausal atrophic vaginitis | 99.70% | L5 | Hold |
| 2 | Ulceration of vulva | 99.42% | L5 | Hold |
| 3 | **Vaginal discharge** | 99.41% | **L1** | **Proceed with Guardrails** |
| 4 | Vulvar neoplasm | 99.37% | L5 | Hold |
| 5 | Trichomonal vulvovaginitis | 99.37% | L2 | Research Question |
| 6 | Leukoplakia of vagina | 99.34% | L5 | Hold |
| 7 | Vulvovaginal candidiasis | 99.16% | L3 | Research Question |
| 8 | Herpetic vulvovaginitis | 97.87% | L5 | Hold |
| 9 | Infective vaginitis | 94.84% | L1 | Proceed with Guardrails |
| 10 | Bullous impetigo | 89.86% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Currently, a structured mechanism-of-action (MOA) record is not available for Secnidazole in this pack. Based on known information from the collected evidence, Secnidazole is a **5-nitroimidazole antimicrobial** (same class as metronidazole and tinidazole) that disrupts DNA synthesis in anaerobic bacteria and protozoa. This mechanism underlies its international approval (e.g., US FDA as Solosec®) for single-dose treatment of bacterial vaginosis and trichomoniasis.

"Vaginal discharge" is not a distinct pathogen-driven disease but the hallmark presenting **symptom** of bacterial vaginosis (BV) and trichomoniasis — the two conditions Secnidazole's established mechanism directly treats. The TxGNN model surfacing "vaginal discharge" as a treatable target is therefore less a novel biological hypothesis and more a close restatement of the drug's already-validated use, which is why this candidate carries L1 evidence (multiple completed Phase 3 RCTs) rather than model-only support.

By contrast, several other high-scoring predictions in this pack (atrophic vaginitis, vulvar neoplasm, herpetic vulvovaginitis, bullous impetigo) involve non-infectious or non-anaerobic pathologies with no plausible link to Secnidazole's antimicrobial mechanism — these are best explained by graph proximity among "vaginal/vulvar disease" nodes rather than genuine pharmacological signal, and are correctly scored L5/Hold.

---

## Clinical Trial Evidence

*(Evidence shown for the selected indication: Vaginal Discharge)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03935217](https://clinicaltrials.gov/study/NCT03935217) | Phase 3 | Completed | 147 | Multicenter, randomized, placebo-controlled, delayed-treatment trial of single-dose Solosec® (secnidazole 2g) for trichomoniasis; directly targets a cause of vaginal discharge |
| [NCT03937869](https://clinicaltrials.gov/study/NCT03937869) | Phase 4 | Completed | 40 | Post-marketing safety study of single-dose Solosec® 2g in adolescent girls with bacterial vaginosis |
| [NCT02147899](https://clinicaltrials.gov/study/NCT02147899) | Phase 2 | Completed | 215 | Randomized, double-blind, placebo-controlled study of oral secnidazole (SYM-1219) for bacterial vaginosis; symptom endpoints included discharge |
| [NCT02111629](https://clinicaltrials.gov/study/NCT02111629) | Phase 3 | Completed | 118 | Fluconazole + secnidazole combination for symptomatic vaginal discharge in mixed BV/Candida infections (Grade B — combination confounds attribution to secnidazole alone) |
| [NCT05033743](https://clinicaltrials.gov/study/NCT05033743) | Phase 2/3 | Completed | 24 | Pilot study of once-weekly secnidazole granules as suppressive therapy to prevent recurrent BV (Grade B — chronic suppression, not acute-treatment design) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28867602](https://pubmed.ncbi.nlm.nih.gov/28867602/) | 2017 | RCT | Am J Obstet Gynecol | Phase 3, double-blind, placebo-controlled trial confirming efficacy/safety of single-dose oral secnidazole 2g for BV |
| [20885970](https://pubmed.ncbi.nlm.nih.gov/20885970/) | 2010 | RCT | Infect Dis Obstet Gynecol | Phase III non-inferiority trial: secnidazole vs. metronidazole for BV treatment |
| [31129560](https://pubmed.ncbi.nlm.nih.gov/31129560/) | 2019 | Systematic Review | Eur J Obstet Gynecol Reprod Biol | Meta-analysis confirming efficacy/safety of single-dose secnidazole 2g for BV |
| [39463760](https://pubmed.ncbi.nlm.nih.gov/39463760/) | 2024 | Systematic Review/NMA | Front Cell Infect Microbiol | Network meta-analysis comparing efficacy/safety of multiple BV drug regimens |
| [29323627](https://pubmed.ncbi.nlm.nih.gov/29323627/) | 2018 | Open-label Phase 3 | J Womens Health | Safety of single-dose secnidazole granules in women and postmenarchal adolescents with BV |
| [22529484](https://pubmed.ncbi.nlm.nih.gov/22529484/) | 2012 | Comparative Trial | Indian J Pharmacol | Head-to-head comparison of single-dose metronidazole, tinidazole, secnidazole, and ornidazole in BV |
| [29132478](https://pubmed.ncbi.nlm.nih.gov/29132478/) | 2017 | RCT | J Coll Physicians Surg Pak | Vaginal clindamycin vs. single oral-dose secnidazole for symptomatic BV |
| [9617020](https://pubmed.ncbi.nlm.nih.gov/9617020/) | 1998 | RCT (older) | Ginecol Obstet Mex | Oral itraconazole + secnidazole vs. topical vaginal ovules for symptomatic vaginitis |
| [31499057](https://pubmed.ncbi.nlm.nih.gov/31499057/) | 2020 | Review | Am J Obstet Gynecol | BV as the leading cause of abnormal vaginal discharge; treatment overview |
| [30424704](https://pubmed.ncbi.nlm.nih.gov/30424704/) | 2019 | Review | Postgrad Med | Clinical primer on BV diagnosis and treatment |

---

## India Market Information

Secnidazole currently has **no product registrations in India** (Market Status: Not Marketed; Total Licenses: 0). No approved labeling, dosage form, or indication text is available to summarize.

---

## Safety Considerations

- **Drug Interactions**: 92 documented interactions recorded (DDInter, all rated **Moderate** severity). Notable interacting agents include other nitroimidazoles (metronidazole, tinidazole), statins (atorvastatin, rosuvastatin, simvastatin), amiodarone, levodopa, radioiodine (I-123/I-131), and several oncology/immunology biologics and chemotherapy agents (paclitaxel, carboplatin, bortezomib, carfilzomib, brentuximab vedotin, trastuzumab emtansine, adalimumab, certolizumab pegol, auranofin). Given the volume and range, a full interaction review is warranted before any clinical use.

Formal package-insert warnings and contraindications are not available in this data set (flagged as a **Blocking** data gap — DG001). Please refer to the official package insert once available for complete safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2–4 trials and systematic reviews already establish Secnidazole's efficacy for bacterial vaginosis and trichomoniasis — the underlying causes of the "vaginal discharge" symptom target — giving this candidate L1 evidence strength. The primary barrier is regulatory, not scientific: the drug is not yet registered in India, and formal safety labeling data is missing.

**To proceed, the following is needed:**
- Official India product insert / warnings and contraindications (DG001, Blocking)
- Structured mechanism-of-action data from DrugBank or equivalent source (DG002, High)
- Regulatory pathway assessment for India market entry/registration (currently 0 licenses)
- Deprioritize or independently validate the top TxGNN-scored prediction (postmenopausal atrophic vaginitis) given its lack of mechanistic plausibility
- Consider parallel evaluation of "infective vaginitis" (L1, Proceed with Guardrails) and "trichomonal vulvovaginitis" (L2) as adjacent, evidence-supported label expansion candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

