---
layout: default
title: Chlordiazepoxide
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
---

# Chlordiazepoxide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Chlordiazepoxide: From Anxiety to Insomnia

## One-Sentence Summary

Chlordiazepoxide (Librium) is the first synthesized benzodiazepine, historically used as an anxiolytic for anxiety disorders and alcohol withdrawal management.
The TxGNN model predicts it may be effective for **Insomnia**,
with **0 relevant clinical trials** and **6 publications** currently supporting this specific direction.
Given concerns about long-acting metabolites and the availability of superior alternatives, the current recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (0 registrations in India; drug is well-established as anxiolytic globally) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the provided dataset. Based on known information, Chlordiazepoxide belongs to the benzodiazepine class — the first of its kind, synthesized by Leo Sternbach in 1955. As a benzodiazepine, it acts as a positive allosteric modulator at GABA-A receptors, enhancing chloride ion influx and producing central nervous system depression including anxiolytic, anticonvulsant, muscle relaxant, and sedative-hypnotic effects. This central sedation provides a theoretically sound basis for its potential application in insomnia.

Anxiety disorders and insomnia are frequently comorbid conditions, and the sedative properties of benzodiazepines as a class have been utilized historically for sleep-onset difficulties. Chlordiazepoxide's sedative profile is pharmacologically consistent with sleep induction, and the TxGNN knowledge graph likely captured the well-documented "GABA-A enhancement → CNS depression → hypnosis" pathway when generating this prediction.

However, chlordiazepoxide is a long-acting benzodiazepine with active metabolites (desmethylchlordiazepoxide, t½ >36 hours) that accumulate significantly, especially in elderly patients, raising concerns about residual daytime sedation, cognitive impairment, fall risk, and dependence. Shorter-acting benzodiazepines (e.g., temazepam) and non-benzodiazepine hypnotics (z-drugs) have largely supplanted long-acting agents in modern insomnia guidelines. The prediction is mechanistically plausible but clinically dated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

> *One trial was returned by the database query (NCT01109030) but was assessed as entirely irrelevant (Grade C): it evaluated Pioglitazone as an adjunct to Citalopram for moderate-to-severe depression, with no design connection to Chlordiazepoxide or insomnia. It is excluded from this evidence summary.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [4628683](https://pubmed.ncbi.nlm.nih.gov/4628683/) | 1972 | RCT | Current Therapeutic Research | Comparative clinical evaluation of molindone vs. chlordiazepoxide in anxious outpatients; provides direct chlordiazepoxide efficacy data in a CNS indication |
| [2883822](https://pubmed.ncbi.nlm.nih.gov/2883822/) | 1986 | Review | Acta Psychiatrica Scandinavica (Suppl) | Reviews age-related pharmacodynamic changes of benzodiazepines; elderly subjects show 2–3× increased CNS sensitivity, raising safety concerns for hypnotic use |
| [6111745](https://pubmed.ncbi.nlm.nih.gov/6111745/) | 1981 | Review | The Medical Letter | Comparative guide to benzodiazepine selection for anxiety and insomnia; contextualizes chlordiazepoxide within the class |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opinion on Drug Metabolism & Toxicology | Pharmacokinetics of anxiolytics including benzodiazepines; discusses clinical implications of drug disposition for this class |
| [30680986](https://pubmed.ncbi.nlm.nih.gov/30680986/) | 2019 | Cross-sectional | Medicinski Glasnik | Prevalence of potentially inappropriate medications in elderly patients; benzodiazepines including chlordiazepoxide are flagged under Beers 2012 criteria, highlighting safety concerns in older adults |
| [14085195](https://pubmed.ncbi.nlm.nih.gov/14085195/) | 1963 | Case Series | Acta Psychiatrica Scandinavica | Early clinical report on treatment of anxiety neuroses and psychosomatic syndromes with a Librium metabolite (RO 4-5360); historical record only |

---

## Safety Considerations

**Drug Interactions (104 interactions identified in total):**

**Major interactions — require close monitoring or avoidance:**
- **Morphine** and **Morphine (liposomal)**: Concurrent use with opioids carries a risk of profound CNS and respiratory depression; potentially fatal combination.

**Moderate interactions (selected key examples):**
- **Cimetidine**: CYP inhibition may increase chlordiazepoxide plasma levels
- **Clarithromycin**: CYP3A4 inhibition may further elevate benzodiazepine exposure
- **Opium / Nabilone / Dronabinol**: Additive CNS depressant effects
- **Bupropion**: Increased seizure risk
- **Metoclopramide**: Additive sedation
- **Sibutramine**: Risk of CNS toxicity
- **Teduglutide**: May increase benzodiazepine intestinal absorption

**Minor interactions:** Antacid preparations (aluminum hydroxide, calcium carbonate, magnesium hydroxide, magnesium oxide, magaldrate, magnesium carbonate) may delay absorption without significantly reducing overall bioavailability.

Please refer to the package insert for complete warnings and contraindications, as formal India regulatory safety data (CDSCO labeling) was not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While chlordiazepoxide has a mechanistically plausible basis for use in insomnia via GABA-A mediated sedation, no dedicated clinical trials exist for this indication, the available literature is predominantly class-level rather than drug-specific, and modern insomnia guidelines favor shorter-acting agents with superior safety profiles. The drug is additionally not marketed in India, making this a low-priority repurposing candidate at this time.

**To proceed, the following is needed:**
- Retrieve full MOA data from DrugBank API (DG002) to enable mechanistic-link scoring
- Obtain India regulatory package insert (CDSCO / FDA India label) to complete the safety profile (DG001 — currently blocking S1 safety assessment)
- Identify a specific clinical sub-population or niche (e.g., alcohol withdrawal-associated insomnia) where chlordiazepoxide's combined anxiolytic-hypnotic profile may offer a meaningful advantage over modern alternatives
- Commission or identify a systematic review specifically evaluating chlordiazepoxide (not benzodiazepines as a class) for insomnia outcomes
- Conduct a formal regulatory feasibility assessment before any clinical development in India, given current zero-registration status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

