---
layout: default
title: Zolpidem
parent: 僅模型預測 (L5)
nav_order: 902
evidence_level: L5
indication_count: 3
---

# Zolpidem
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

# Zolpidem: From Unmarketed Status in India to Insomnia (Sleep Disorder of Initiating and Maintaining Sleep)

## One-Sentence Summary

> Zolpidem is not currently registered or marketed in India, so no local approved indication exists in the regulatory record.
> The TxGNN model predicts it is effective for **Sleep Disorder, Initiating and Maintaining Sleep (Insomnia)** — which is in fact Zolpidem's well-established, globally recognized indication —
> supported by **21 publications**, including multiple Phase 3 randomized controlled trials and network meta-analyses, though **no clinical trials are currently indexed in this evidence pack**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no India market license on record. (Well-established global indication: insomnia, non-benzodiazepine hypnotic) |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep (Insomnia) |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (`original_moa: [Data Gap]`). Based on well-established pharmacological knowledge, Zolpidem is a non-benzodiazepine hypnotic ("Z-drug") that acts as a selective agonist at the α1 subunit of the GABA-A receptor. This mechanism produces sedative-hypnotic effects with a more selective receptor profile than traditional benzodiazepines, and its efficacy for insomnia has been documented internationally for over three decades.

Notably, this case differs from a typical "repurposing" scenario: the predicted indication (insomnia) is not a novel disease area for Zolpidem but its core, already-known therapeutic use. The evidence pack shows Zolpidem is **not currently registered in India** (0 licenses, market status "未上市"), so the practical significance of this TxGNN prediction is less about discovering a new mechanism and more about **confirming strong, pre-existing evidence** for a potential first-time market introduction of Zolpidem in India.

The literature evidence reflects this maturity: Zolpidem appears repeatedly as the active comparator in modern Phase 3 trials of newer hypnotics (lemborexant, daridorexant), and in multiple meta-analyses and network meta-analyses evaluating pharmacological treatments for insomnia — indicating an extensive, decades-deep evidence base rather than early-stage or purely computational signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered (the `clinical_trials` and `ictrp_trials` fields for this indication are empty; clinical trial evidence for Zolpidem is instead embedded within the literature listed below).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | Phase 3 RCT | JAMA Network Open | Direct comparison of lemborexant vs. placebo vs. zolpidem tartrate ER in older adults with insomnia disorder |
| [34688027](https://pubmed.ncbi.nlm.nih.gov/34688027/) | 2021 | Meta-analysis of RCTs | Sleep Medicine | Confirms efficacy and safety of zolpidem for insomnia treatment over one month |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Network meta-analysis | Lancet | Comparative effectiveness of pharmacological interventions (incl. zolpidem) for acute and long-term insomnia management |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Network meta-analysis | J Manag Care Spec Pharm | Comparative efficacy and safety of lemborexant and other insomnia treatments, including zolpidem |
| [36472134](https://pubmed.ncbi.nlm.nih.gov/36472134/) | 2023 | Comparative RCT-derived analysis | J Clin Sleep Med | Polysomnography-based comparison of lemborexant vs. zolpidem ER 6.25mg across insomnia subtypes |
| [37477771](https://pubmed.ncbi.nlm.nih.gov/37477771/) | 2023 | Post-hoc RCT analysis | CNS Drugs | Effects of daridorexant vs. zolpidem on number, duration, and distribution of night-time wake bouts |
| [39879708](https://pubmed.ncbi.nlm.nih.gov/39879708/) | 2025 | Post-hoc RCT analysis | Sleep Medicine | Sleep architecture effects in insomnia with comorbid mild OSA, using zolpidem as reference class comparator |
| [39374004](https://pubmed.ncbi.nlm.nih.gov/39374004/) | 2024 | RCT | JAMA Internal Medicine | Masked-taper behavioral intervention for discontinuing benzodiazepine receptor agonists (incl. zolpidem) |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Review | Pharmacological Reviews | Pharmacology and clinical applications of insomnia drugs beyond benzodiazepines, including Z-drugs |
| [37549414](https://pubmed.ncbi.nlm.nih.gov/37549414/) | 2023 | Review | The Journal of Family Practice | Updated review of insomnia management strategies in primary care |

---

## India Market Information

Zolpidem currently holds **no market registrations in India** (`market_status: 未上市`, `total_licenses: 0`). No authorization records are available to summarize.

---

## Safety Considerations

**Drug Interactions**: A total of **274 documented interactions** are on record for Zolpidem. Representative examples from the evidence pack:

- **Major**: Morphine, Morphine (liposomal) — combined use significantly increases risk of CNS/respiratory depression
- **Moderate**: Bupropion, Aprepitant, Dexamethasone, Cimetidine, Clarithromycin, Dronabinol, Nabilone, Metoclopramide, Miconazole, Clotrimazole, Glycerol phenylbutyrate, Opium, Sibutramine, Troglitazone
- **Unknown severity (requires further characterization)**: Calcitriol, Vitamin A, Phentermine, Pantoprazole

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Efficacy evidence for insomnia is strong and mature (L1, supported by multiple Phase 3 RCTs and network meta-analyses), but a **Blocking** data gap exists for local safety labeling (warnings/contraindications), which prevents the mandatory S1 safety pre-assessment. Combined with Zolpidem having zero existing India registrations, this represents a new-market-entry decision requiring complete local regulatory review before proceeding.

**To proceed, the following is needed:**
- Official India-market prescribing information / package insert warnings and contraindications (source: local regulatory authority)
- Confirmed mechanism of action documentation (DrugBank query)
- Structured risk-benefit review of the 274 recorded drug interactions, prioritizing the major-severity opioid interactions (Morphine)
- A defined regulatory pathway for first-time market registration in India, given the current absence of any local license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

