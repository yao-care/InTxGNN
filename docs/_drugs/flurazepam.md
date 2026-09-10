---
layout: default
title: Flurazepam
parent: 僅模型預測 (L5)
nav_order: 367
evidence_level: L5
indication_count: 1
---

# Flurazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Flurazepam: From Insomnia to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

Flurazepam is a benzodiazepine hypnotic historically used to treat insomnia (sleep-onset and sleep-maintenance difficulty). The TxGNN model predicts it is effective for **Sleep Disorder, Initiating and Maintaining Sleep** — which is essentially the drug's own established use rather than a novel indication — with **0 registered clinical trials** and **20 supporting publications**, but no current Taiwan market authorization.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia (established international use as a benzodiazepine hypnotic; no Taiwan license currently on file) |
| Predicted New Indication | Sleep Disorder, Initiating and Maintaining Sleep |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L3 |
| Taiwan Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (blocked at source — see Safety Considerations). Based on the supporting literature in this evidence pack, flurazepam is a first-generation benzodiazepine hypnotic that acts on the GABA<sub>A</sub> receptor to produce sedative-hypnotic effects (PMID 37730991 describes the structural basis of GABA<sub>A</sub> receptor pharmacology targeted by this drug class).

The predicted indication — "sleep disorder, initiating and maintaining sleep" — is not a genuinely new therapeutic area for this molecule. Multiple publications in the evidence pack (e.g., PMID 1319429: "the revolution in pharmacologic treatment of insomnia began in 1970 with the availability of flurazepam") confirm that flurazepam has long been established specifically for this exact indication. TxGNN's high prediction score therefore functions largely as a **validation of known pharmacology** rather than a discovery of new therapeutic potential, which should temper enthusiasm for treating this as a repurposing opportunity.

Mechanistically, the link is strong precisely because it is not new: GABA<sub>A</sub> receptor potentiation by flurazepam directly produces sedation and sleep induction/maintenance, consistent with decades of clinical use documented in the literature evidence below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | Journal of Clinical Psychopharmacology | Randomized, double-blind, parallel-group, multicenter study of sleep, performance, and plasma levels during 14-day flurazepam vs. midazolam use in chronic insomniacs |
| [7792498](https://pubmed.ncbi.nlm.nih.gov/7792498/) | 1995 | Clinical Study | Sleep | Flurazepam 30mg and zolpidem 10mg both altered sleep perception in insomniacs vs. placebo |
| [7792497](https://pubmed.ncbi.nlm.nih.gov/7792497/) | 1995 | Clinical Study | Sleep | Comparable perception-of-sleep effects for flurazepam and zolpidem shown in normal (non-insomniac) volunteers |
| [6149491](https://pubmed.ncbi.nlm.nih.gov/6149491/) | 1984 | Clinical Study | Neuropsychobiology | Flurazepam 30mg vs. temazepam 40mg both improved sleep quality/depth/duration with measurable residual performance effects 10h post-dose |
| [1319429](https://pubmed.ncbi.nlm.nih.gov/1319429/) | 1992 | Review | The Journal of Clinical Psychiatry | Historical review establishing flurazepam as the first benzodiazepine hypnotic (1970) and its displacement by shorter half-life agents |
| [1680120](https://pubmed.ncbi.nlm.nih.gov/1680120/) | 1991 | Review | The Journal of Clinical Psychiatry | Comparative pharmacokinetic/pharmacodynamic profile of quazepam and flurazepam, noting prevention of early-morning insomnia and rebound |
| [3332464](https://pubmed.ncbi.nlm.nih.gov/3332464/) | 1987 | Review | Seminars in Neurology | Flurazepam effective for both sleep induction and maintenance, retaining efficacy over 4 weeks of nightly use |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Review | Journal of Clinical Psychopharmacology | Critical review of rebound insomnia risk after discontinuation of benzodiazepine hypnotics including flurazepam |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clinical Therapeutics | Safety and efficacy review of sleep medicines (including benzodiazepines) in older adults, where pharmacokinetics may be altered |
| [37730991](https://pubmed.ncbi.nlm.nih.gov/37730991/) | 2023 | Mechanistic Study | Nature | Cryo-EM structures of native GABA<sub>A</sub> receptor assemblies underlying the pharmacology of hypnotics such as flurazepam |

---

## Safety Considerations

**Drug Interactions**: 116 total interactions on file. Notable examples include:
- **Major**: Morphine, Morphine (liposomal) — increased CNS/respiratory depression risk
- **Moderate**: Bupropion, Omeprazole, Cimetidine, Clarithromycin, Dronabinol, Nabilone, Metoclopramide, Opium, Sibutramine, Teduglutide
- **Minor**: Magnesium oxide, Calcium carbonate, Aluminum hydroxide, Magaldrate, Magnesium carbonate, Magnesium hydroxide

Detailed key warnings and contraindications from the Taiwan package insert are not yet available (see Conclusion — this is a blocking data gap).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Taiwan-specific labeling data (warnings/contraindications) is a blocking gap that prevents a baseline safety assessment, and the drug currently has no market authorization or license in Taiwan (0 registrations). Additionally, the predicted indication substantially overlaps with flurazepam's long-established original use rather than representing a genuinely novel repurposing opportunity, which limits the incremental value of proceeding at this time.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — download and parse from TFDA official source
- Confirmed mechanism of action (MOA) data via DrugBank API query
- Clarification of whether any Taiwan-registered product exists or is planned, given current "Not Marketed" status
- Reassessment of genuine repurposing novelty versus confirmation of known indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

