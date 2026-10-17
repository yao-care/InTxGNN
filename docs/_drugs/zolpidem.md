---
layout: default
title: Zolpidem
parent: Model Prediction Only (L5)
nav_order: 911
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Zolpidem: predicted new indication Sleep disorder, initiating and maintaining sleep (evidence level L5). Approved use: Insomnia"
monitor_inn: "Zolpidem"
predicted_indications: ["sleep disorder, initiating and maintaining sleep", "benign paroxysmal torticollis of infancy", "agoraphobia"]
---

# Zolpidem
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

# Zolpidem: From Insomnia to Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Zolpidem is a sedative-hypnotic originally used to treat insomnia.
The TxGNN model predicts it may be effective for **sleep disorder, initiating and maintaining sleep**, but this is essentially the same condition as its approved use rather than a true new indication. No clinical trials are registered for this prediction, but **20 publications** (reviews, guidelines, network meta-analyses and one Phase 3 RCT with zolpidem ER as comparator) discuss the drug in this setting.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Insomnia |
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L1 (as assigned in the data compiled for this report; see note below) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Proceed with Guardrails |

*Note on evidence level:* The L1 grade rests on a network meta-analysis, a clinical practice guideline and a Phase 3 trial in which zolpidem ER served only as an active comparator. No completed Phase 3 trials with zolpidem as the primary study drug are registered for this prediction. Because the indication is already approved, the grade reflects well-established use rather than new-indication evidence.

## Why is This Prediction Reasonable?

Zolpidem is a positive allosteric modulator of the GABA-A receptor with preferential affinity for the alpha-1 subunit, which mediates sedative-hypnotic effects. Detailed mechanism-of-action data was not included in the data compiled for this report, but this mechanism is well established in the literature.

"Difficulty initiating and maintaining sleep" is essentially a synonym for insomnia, the drug's original indication. The prediction is therefore best read as a re-labeling of the approved use, not as true repurposing. The model's high score is consistent with this, since the drug-disease link already exists in the knowledge graph.

Two other predictions were also generated, but they lack support:
- **Benign paroxysmal torticollis of infancy** (score 99.26%): no identifiable mechanistic link, no trials or literature, and sedative-hypnotics raise safety concerns in infants. This looks like a graph-based artifact. Decision: Hold.
- **Agoraphobia** (score 99.25%): the rationale is weak, because zolpidem's alpha-1 selectivity gives it minimal anxiolytic activity. Guideline-preferred treatments are SSRIs/SNRIs and CBT, and the risks of dependence, complex sleep behaviors and next-day impairment argue against use. No trials or literature support it. Decision: Hold.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Network meta-analysis | Lancet | Compared the effectiveness of drug treatments for acute and long-term management of insomnia in adults |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Clinical practice guideline | J Clin Sleep Med | AASM guideline on drug treatment of chronic insomnia in adults, covering individual drugs |
| [31880796](https://pubmed.ncbi.nlm.nih.gov/31880796/) | 2019 | RCT (Phase 3) | JAMA Netw Open | Lemborexant vs placebo and zolpidem ER in older adults with insomnia; zolpidem ER was the active comparator |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Network meta-analysis | J Manag Care Spec Pharm | Efficacy and safety of lemborexant compared with other insomnia treatments |
| [39923608](https://pubmed.ncbi.nlm.nih.gov/39923608/) | 2025 | Guideline (expert consensus) | Sleep Med | European guidance on switching or deprescribing hypnotics for chronic insomnia; lists Z-drugs including zolpidem |
| [41187937](https://pubmed.ncbi.nlm.nih.gov/41187937/) | 2025 | Guideline | Arq Neuropsiquiatr | Brazilian guideline on Z-drug abuse and dependence; use recommended for no more than four weeks |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Review | Pharmacol Rev | Z-drugs have a strong evidence base but cause cognitive impairment, tolerance, rebound insomnia, falls, abuse and dependence |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs Aging | Pharmacological management of insomnia in the elderly |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Ther | Safety and efficacy of sleep medicines in older adults |
| [22424586](https://pubmed.ncbi.nlm.nih.gov/22424586/) | 2012 | Review | Expert Opin Pharmacother | Zolpidem is a benzodiazepine-receptor agonist and the most widely prescribed hypnotic in the US |

## India Market Information

The data compiled for this report contains no approved indication text for these licences. Of the 20 valid single-ingredient registrations, the main ones are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 251751 | Zolit 10mg Tablet | Strip of 10 tablets | Not stated |
| 63322 | Dactive 12.5mg Tablet | Strip of 7 tablets | Not stated |
| 101218 | Goodnoct 6.25mg Tablet XR | Strip of 10 XR tablets | Not stated |
| 249782 | Zedem 12.5mg Tablet ER | Strip of 10 ER tablets | Not stated |
| 64429 | Dactive 10mg Tablet | Strip of 10 tablets | Not stated |

All forms are oral (immediate-release, extended-release and controlled-release tablets).

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (drug-disease edges, not label text): anxiety disorder, neurotic disorder, dysthymic disorder, liver disease, gallbladder disease, obstructive sleep apnea syndrome, sleep apnea syndrome, congenital central hypoventilation syndrome, amnestic disorder, retrograde amnesia, substance-related disorder, substance abuse/dependence, and attention deficit hyperactivity disorder (including the inattentive type).
- **Drug Interactions**: 274 interactions were identified. Major interactions include **morphine** and **liposomal morphine** (additive central nervous system and respiratory depression). Moderate interactions include bupropion, aprepitant, dexamethasone, cimetidine, clarithromycin, dronabinol, nabilone, metoclopramide, miconazole, clotrimazole, glycerol phenylbutyrate, opium, sibutramine and troglitazone.
- **Literature-reported concerns**: cognitive impairment, tolerance, rebound insomnia on discontinuation, falls, car accidents, abuse and dependence; particular caution in older adults.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for sleep disorder, initiating and maintaining sleep). **Hold** for benign paroxysmal torticollis of infancy and agoraphobia.

**Rationale:**
The first prediction is effectively the approved insomnia indication, supported by guidelines and meta-analyses, so it is not a new repurposing opportunity. The other two predictions have no clinical or literature support and carry safety concerns.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Indian labelling. This is a blocking gap for safety screening.
- Detailed mechanism of action data from DrugBank.
- Confirmation of approved indication wording on the Indian licences.
- A decision on whether the first prediction is worth pursuing, since it adds no new indication.
- Safety guardrails for older adults, patients with sleep apnea or liver disease, and those at risk of dependence, and attention to co-prescribed opioids.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

