---
layout: default
title: Trazodone
parent: 僅模型預測 (L5)
nav_order: 851
evidence_level: L5
indication_count: 10
---

# Trazodone
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

# Trazodone: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

> Trazodone is a serotonin-modulating antidepressant, globally approved for major depressive disorder (per literature evidence in this pack; not currently licensed in India).
> The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)**,
> with **0 registered clinical trials** and **20 publications** currently supporting this direction, including one randomized placebo-controlled trial.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (per literature evidence; no formal India license record available) |
| Predicted New Indication | Obsessive-Compulsive Disorder |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, structured mechanism-of-action data for trazodone is not available in this evidence pack (DG002). Based on the pharmacological information captured in the literature and repurposing rationale, trazodone is understood to act as a serotonin system modulator — a 5-HT2A receptor antagonist combined with weak serotonin reuptake (SERT) inhibition. Its efficacy in major depressive disorder is well established in clinical practice.

OCD is hypothesized to be driven by dysregulated serotonin (and dopamine) neurotransmission, which is the pharmacological basis for the effectiveness of potent serotonin reuptake inhibitors such as clomipramine, fluoxetine, fluvoxamine, and paroxetine in this condition. Trazodone's serotonergic activity provides a plausible, though comparatively weaker, mechanistic link to OCD relative to these standard-of-care agents — its reuptake-inhibition potency is substantially lower than clomipramine or SSRIs. One notable piece of supporting evidence (PMID 3501130) links trazodone treatment response in OCD to measurable shifts in caudate nucleus glucose metabolism on PET imaging, offering partial mechanistic corroboration beyond symptom-based outcomes.

Overall, the mechanistic rationale is moderate rather than strong: trazodone is not a first-line serotonergic agent for OCD, and most of the supporting evidence originates from case reports and small trials predating current diagnostic and treatment standards.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1629380](https://pubmed.ncbi.nlm.nih.gov/1629380/) | 1992 | RCT | J Clin Psychopharmacol | Double-blind, placebo-controlled trial of trazodone in OCD patients, testing its serotonin reuptake-inhibiting antiobsessive potential. |
| [8993077](https://pubmed.ncbi.nlm.nih.gov/8993077/) | 1996 | Review | Psychopharmacol Bull | Reviews mono- and polypharmacotherapy for OCD; notes OCD responds specifically to serotonin reuptake inhibitors. |
| [8134850](https://pubmed.ncbi.nlm.nih.gov/8134850/) | 1994 | Review | South Med J | Discusses OCD pharmacologic management and the serotonin/dopamine dysregulation hypothesis underlying SRI efficacy. |
| [8331098](https://pubmed.ncbi.nlm.nih.gov/8331098/) | 1993 | Review | J Clin Psychiatry | Reviews biological/augmentation strategies for treatment-resistant OCD combining SRIs with serotonergic adjuncts. |
| [27744763](https://pubmed.ncbi.nlm.nih.gov/27744763/) | 2017 | Review | Postgrad Med | Comprehensive review of trazodone's mechanism, formulation, and use across psychiatric/medical conditions, including non-FDA-approved indications. |
| [26088119](https://pubmed.ncbi.nlm.nih.gov/26088119/) | 2015 | Review | Curr Pharm Des | Reviews off-label trazodone use, including OCD, insomnia, GAD, panic disorder, and PTSD; weighs evidence, benefits, and risks. |
| [3501130](https://pubmed.ncbi.nlm.nih.gov/3501130/) | 1987 | Cohort | Psychopathology | Trazodone treatment response in OCD correlated with changes in caudate nucleus glucose metabolism (PET imaging). |
| [2119885](https://pubmed.ncbi.nlm.nih.gov/2119885/) | 1990 | Case Report | Clin Neuropharmacol | Trazodone administered to 9 clomipramine-resistant OCD patients; 3 showed favorable, reproducible response. |
| [4009160](https://pubmed.ncbi.nlm.nih.gov/4009160/) | 1985 | Case Report | J Nerv Ment Dis | Two treatment-resistant OCD-with-depression patients showed rapid improvement in both conditions on trazodone. |
| [8434675](https://pubmed.ncbi.nlm.nih.gov/8434675/) | 1993 | Case Report | Am J Psychiatry | Case report of trazodone treatment for comorbid OCD and trichotillomania. |

---

## India Market Information

No India market authorization currently on record — `taiwan_regulatory` reports **0 registrations** and market status **"Not marketed"** for trazodone in this dataset.

---

## Safety Considerations

- **Drug Interactions**: 258 documented interactions identified (DDInter source). Notable **Major**-level interactions include Bupropion, Lorcaserin, Dolasetron, Palonosetron, Cisapride, Dexfenfluramine, and Fenfluramine — combinations warranting particular caution (e.g., serotonergic/QT-prolongation risk). **Moderate**-level interactions include Famotidine, Loperamide, Aprepitant, Morphine, Bisacodyl, Clarithromycin, and several laxative/bowel-prep agents.

Detailed prescribing warnings and contraindications are not available in this evidence pack (blocking data gap, DG001) — these should be sourced from the official product label before any safety evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Prescribing warnings and contraindication data are missing (DG001, blocking severity), which prevents this candidate from entering the S1 safety evaluation stage. In addition, OCD evidence is limited to a single small placebo-controlled RCT and predominantly older case reports/reviews (Evidence Level L2), with no clinical trials currently registered, and trazodone has no existing market presence in India (0 licenses).

**To proceed, the following is needed:**
- Official label warnings and contraindications for trazodone (source: regulatory agency label, per DG001 remediation plan)
- Structured mechanism-of-action data via DrugBank API (DG002)
- Confirmation of India market entry pathway, given current "Not marketed" status
- Updated/contemporary controlled trials evaluating trazodone specifically for OCD, given the existing RCT evidence is from 1992 and predates current SSRI/clomipramine standard-of-care comparators
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

