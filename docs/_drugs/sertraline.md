---
layout: default
title: Sertraline
parent: 僅模型預測 (L5)
nav_order: 763
evidence_level: L5
indication_count: 8
---

# Sertraline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Sertraline: From SSRI Antidepressant Therapy to Agoraphobia

## One-Sentence Summary

> Sertraline is a widely used Selective Serotonin Reuptake Inhibitor (SSRI); detailed original indication text and mechanism-of-action data are not available in this dataset (drug not marketed in India — see Data Gaps DG001/DG002).
> TxGNN generated 8 psychiatric-disorder predictions for sertraline, most supported only by weak or unrelated literature. Among them, **Agoraphobia** stands out,
> with **4 clinical trials** (including a completed Phase 4 RCT) and **20 publications** — including a Cochrane and a BMJ network meta-analysis — supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in dataset (India: 未上市/not marketed; MOA and indication data gaps — DG001, DG002) |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L1 |
| India Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002). Based on known information, Sertraline is a Selective Serotonin Reuptake Inhibitor (SSRI); its pharmacology centers on inhibiting presynaptic serotonin reuptake, which is mechanistically linked to mood and anxiety-spectrum regulation.

Agoraphobia most commonly presents as a component of panic disorder, and SSRIs — sertraline specifically — are an established first-line pharmacological class for panic disorder with agoraphobia in multiple jurisdictions. This means the TxGNN signal here is less a novel repurposing hypothesis and more a **confirmatory match** to an already well-characterized pharmacological relationship, which is reflected in the unusually strong clinical trial and literature base (L1, S3).

By contrast, the other 7 TxGNN predictions in this pack (paranoid, schizoid, histrionic, schizotypal, dependent, and narcissistic personality disorders, plus benign paroxysmal torticollis of infancy) are supported only by tangential or unrelated literature (e.g., lupus erythematosus case reports, alpha-interferon psychiatric side-effect reviews), reflecting a known TxGNN false-positive pattern driven by disease-ontology proximity of personality disorders in the knowledge graph, rather than genuine mechanistic or clinical signal. These remain at **Hold**.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00677352](https://clinicaltrials.gov/study/NCT00677352) | Phase 4 | Completed | 321 | Randomized, double-blind, multicenter trial comparing sertraline vs. paroxetine for panic disorder efficacy and safety (Grade A relevance) |
| [NCT00182533](https://clinicaltrials.gov/study/NCT00182533) | Phase 4 | Terminated | 170 | Sertraline in generalized social phobia with anxiety comorbidity, evaluating safety/efficacy in patients with co-occurring conditions |
| [NCT05210153](https://clinicaltrials.gov/study/NCT05210153) | N/A | Unknown | 148 | Plasma drug level monitoring and CYP2C19 genotyping for sertraline dose personalization in depression/anxiety treatment |
| [NCT05930912](https://clinicaltrials.gov/study/NCT05930912) | N/A | Unknown | 1 | Psychoanalytic treatment study in ASD with anxiety-spectrum comorbidities including avoidant personality disorder (low relevance, n=1) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35045991](https://pubmed.ncbi.nlm.nih.gov/35045991/) | 2022 | Network Meta-analysis | BMJ | Identifies SSRI drug classes/agents with highest remission and lowest adverse-event rates for panic disorder with/without agoraphobia |
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Network Meta-analysis | Cochrane Database Syst Rev | Compares pharmacological treatments, including sertraline, for panic disorder in adults |
| [16053461](https://pubmed.ncbi.nlm.nih.gov/16053461/) | 2005 | RCT | Bosn J Basic Med Sci | 12-week placebo-controlled trial comparing sertraline and alprazolam in panic disorder with/without agoraphobia |
| [12191627](https://pubmed.ncbi.nlm.nih.gov/12191627/) | 2002 | RCT (pooled) | J Psychiatr Res | Pooled data from 4 sertraline vs. placebo trials (N=544); early improvement predicted endpoint remission in panic disorder |
| [16505130](https://pubmed.ncbi.nlm.nih.gov/16505130/) | 2006 | RCT | Am J Geriatr Psychiatry | CBT vs. sertraline for anxiety disorders in older adults |
| [16292466](https://pubmed.ncbi.nlm.nih.gov/16292466/) | 2006 | Pooled RCT Analysis | Arch Womens Ment Health | Sex differences in clinical presentation and sertraline response in panic disorder with/without agoraphobia |
| [36573969](https://pubmed.ncbi.nlm.nih.gov/36573969/) | 2022 | Review | JAMA | Overview of anxiety disorders (34% lifetime prevalence), including panic disorder/agoraphobia treatment landscape |
| [38299123](https://pubmed.ncbi.nlm.nih.gov/38299123/) | 2024 | Case Review | Epilepsy Behav Rep | Case of panic disorder progressing to agoraphobia, managed with psychopharmacological treatment |
| [11110016](https://pubmed.ncbi.nlm.nih.gov/11110016/) | 2000 | Review | Int Clin Psychopharmacol | SSRIs including sertraline shown superior to placebo for panic disorder, agoraphobia, and associated depressive symptoms |
| [37676054](https://pubmed.ncbi.nlm.nih.gov/37676054/) | 2023 | Systematic Review | Expert Rev Neurother | Systematic review of pharmacological management of panic disorder in older patients |

---

## India Market Information

Sertraline currently has **no marketing authorization records in India** in this dataset (market status: 未上市 / not marketed; 0 registrations).

---

## Safety Considerations

Package-insert-level warnings and contraindications are not available in this dataset (DG001, Blocking severity — TFDA/India label data pending).

**Drug Interactions** (396 total documented interactions; major-severity examples below):

| Interacting Drug | Level | Source |
|---|---|---|
| Bupropion | Major | ddinter |
| Lorcaserin | Major | ddinter |
| Diethylpropion | Major | ddinter |
| Dolasetron | Major | ddinter |
| Eliglustat | Major | ddinter |
| Palonosetron | Major | ddinter |
| Phentermine | Major | ddinter |

Additional moderate-level interactions on file include famotidine, loperamide, morphine, acetylsalicylic acid, clarithromycin, glimepiride, and insulin aspart, among others.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The agoraphobia prediction is backed by L1-level evidence — a completed Phase 4 RCT plus a Cochrane and a BMJ network meta-analysis — confirming an already-established SSRI class effect rather than a purely speculative signal. However, India-specific regulatory, MOA, and labeling data are entirely missing, and 7 of the 8 TxGNN predictions in this pack are low-confidence noise that should not be advanced.

**To proceed, the following is needed:**
- TFDA/India package insert: warnings, contraindications, precautions (DG001, Blocking)
- Confirmed mechanism-of-action documentation (DG002)
- Current India regulatory/licensing status verification (dataset shows 0 registrations / not marketed)
- No further action needed on the other 7 predicted indications (paranoid, schizoid, histrionic, schizotypal, dependent, narcissistic personality disorders; benign paroxysmal torticollis of infancy) — retain at Hold pending stronger evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

