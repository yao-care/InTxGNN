---
layout: default
title: Clomipramine
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
---

# Clomipramine
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

# Clomipramine: From Obsessive-Compulsive Disorder to Anxiety Disorder

## One-Sentence Summary

Clomipramine is a tricyclic antidepressant (TCA) historically established for obsessive-compulsive disorder and depression. The TxGNN model predicts it may also be effective for **Anxiety Disorder**, with **19 clinical trials** and **20 publications** currently supporting this direction — though most of the direct clinical evidence comes from closely related conditions (OCD, panic disorder) rather than "anxiety disorder" as a standalone label.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Taiwan dataset (drug is not marketed locally). Based on established pharmacology, clomipramine's approved historical indications are Obsessive-Compulsive Disorder and Depression. |
| Predicted New Indication | Anxiety Disorder |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 |
| Taiwan Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this record is flagged as a data gap, but based on well-established pharmacology, clomipramine is a tricyclic antidepressant that potently inhibits serotonin and, to a lesser extent, norepinephrine reuptake. This dual monoaminergic action is the pharmacological basis for its historical role as the first effective agent in OCD and as a reference drug for panic disorder — both of which sit within the anxiety-disorder spectrum.

Anxiety disorder, OCD, and panic disorder share overlapping serotonergic pathophysiology, which is why clomipramine's efficacy in OCD and panic/agoraphobia (see literature below) plausibly extends to the broader "anxiety disorder" category predicted by TxGNN. Several decades of RCTs (1980s–1990s) directly tested clomipramine against placebo, other TCAs, and SSRIs in these anxiety-spectrum conditions, giving the mechanistic hypothesis substantial historical clinical backing, even though few of these trials use the exact modern "anxiety disorder" label and none are recent registry trials specifically naming clomipramine.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00004310](https://clinicaltrials.gov/study/NCT00004310) | Phase 2 | Unknown | 76 | Compared IV vs. oral pulse-loading of clomipramine followed by 12-week maintenance therapy in OCD. |
| [NCT00564564](https://clinicaltrials.gov/study/NCT00564564) | Phase 4 | Completed | 21 | Open-label trial comparing SSRI+quetiapine vs. SSRI+clomipramine augmentation in OCD patients who failed SSRI monotherapy. |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completed | 26 | Randomized comparison of clomipramine vs. escitalopram (or duloxetine) to identify predictors of medication response in OCD. |
| [NCT00466609](https://clinicaltrials.gov/study/NCT00466609) | Phase 4 | Completed | 54 | Double-blind, double-dummy trial comparing fluoxetine alone, fluoxetine+quetiapine, and fluoxetine+clomipramine augmentation in SRI-refractory OCD. |
| [NCT01148316](https://clinicaltrials.gov/study/NCT01148316) | N/A | Completed | 144 | Adaptive treatment strategy study in pediatric/adolescent psychiatric disorders; clomipramine and SSRIs are noted first-line pharmacotherapy for pediatric OCD. |
| [NCT00254735](https://clinicaltrials.gov/study/NCT00254735) | Phase 3 | Completed | 44 | Quetiapine augmentation pilot study added to baseline SSRI/clomipramine treatment in severe, treatment-resistant OCD. |
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | Completed | 426 | RCT of adjunctive troriluzole vs. placebo in OCD patients with inadequate response to SSRI, clomipramine, venlafaxine, or desvenlafaxine. |
| [NCT04708834](https://clinicaltrials.gov/study/NCT04708834) | Phase 3 | Terminated | 772 | Long-term open-label safety/tolerability study of adjunctive troriluzole in OCD, a population that overlaps with clomipramine-refractory patients. |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | Completed | 124 | Evaluated whether CBT augments serotonin reuptake inhibitor (including clomipramine) treatment effectiveness in pediatric OCD partial responders. |
| [NCT05737511](https://clinicaltrials.gov/study/NCT05737511) | Phase 4 | Not Yet Recruiting | 80 | Pilot RCT of hydroxyzine vs. treatment-as-usual for panic disorder, informative for future anxiety-spectrum trial design. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Network Meta-analysis (Cochrane) | Cochrane Database Syst Rev | Compares pharmacological treatments for panic disorder in adults, contextualizing TCA efficacy including clomipramine. |
| [7795952](https://pubmed.ncbi.nlm.nih.gov/7795952/) | 1995 | RCT/Review | J Child Adolesc Psychiatr Nurs | Establishes clomipramine as the first effective TCA for OCD via serotonin reuptake blockade; reviews side-effect profile. |
| [3887445](https://pubmed.ncbi.nlm.nih.gov/3887445/) | 1985 | RCT | Psychiatry Research | 12-week double-blind trial of clomipramine vs. imipramine in OCD; both produced modest symptom reduction. |
| [1474179](https://pubmed.ncbi.nlm.nih.gov/1474179/) | 1992 | RCT | J Clin Psychopharmacol | Compared clomipramine, clonazepam, and clonidine against diphenhydramine control in OCD. |
| [1933762](https://pubmed.ncbi.nlm.nih.gov/1933762/) | 1991 | Case Report | Can J Psychiatry | IV clomipramine controlled OCD symptoms refractory to oral therapy; 3-year follow-up showed sustained remission. |
| [10665629](https://pubmed.ncbi.nlm.nih.gov/10665629/) | 1999 | RCT | J Clin Psychiatry | 12-week placebo-controlled comparison of paroxetine, clomipramine, and cognitive therapy for panic disorder. |
| [2178909](https://pubmed.ncbi.nlm.nih.gov/2178909/) | 1990 | Review | Drugs | Overview of clomipramine's pharmacology and therapeutic use in OCD and panic disorder; more effective than amitriptyline in short-term trials. |
| [8263222](https://pubmed.ncbi.nlm.nih.gov/8263222/) | 1993 | Meta-analysis | J Behav Ther Exp Psychiatry | Meta-analysis of clomipramine, fluoxetine, and behavior therapy across 25 OCD treatment studies (1975–1991). |
| [27663940](https://pubmed.ncbi.nlm.nih.gov/27663940/) | 2016 | Meta-analysis | J Am Acad Child Adolesc Psychiatry | Compares early treatment response timelines of SSRIs vs. clomipramine in pediatric OCD. |
| [9786103](https://pubmed.ncbi.nlm.nih.gov/9786103/) | 1998 | RCT | J Clin Pharm Ther | Double-blind, placebo-controlled trial testing clomipramine + nortriptyline combination vs. clomipramine alone in OCD. |

## Taiwan Market Information

Clomipramine is currently **not marketed** in Taiwan (0 registered licenses in the regulatory dataset), so no local product/indication registration data is available for this candidate.

## Safety Considerations

**Drug Interactions**: DDI screening returned 318 total interacting drugs. Notable **Major**-severity interactions include:
- Epinephrine
- Bupropion
- Lorcaserin
- Potassium citrate
- Cisapride

Additional **Moderate**-severity interactions include Famotidine, Hyoscyamine, Loperamide, Morphine, Acetylsalicylic acid, Atropine, Glycopyrronium, Cimetidine, Clarithromycin, and others (see full DDI dataset for the complete list of 318).

Key warnings and contraindication data (TFDA label) are not yet available for this candidate — this is flagged as a **Blocking** data gap for safety review.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Anxiety disorder is supported by strong historical RCT and meta-analytic evidence (L1) linking clomipramine to closely related anxiety-spectrum conditions (OCD, panic disorder), but a **Blocking** data gap — missing TFDA label warnings/contraindications — prevents a full initial safety assessment (S1), and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- Obtain TFDA/manufacturer package insert (warnings, contraindications) — currently a Blocking gap
- Confirm detailed mechanism-of-action documentation via DrugBank API — currently a High-severity gap
- Clarify whether trial/literature evidence generalizes from OCD/panic disorder to the broader "anxiety disorder" diagnostic category before advancing past S3

**Note:** This evidence pack also contains other high-evidence candidate indications for clomipramine — notably **Major Depressive Disorder** (L1, Proceed with Guardrails) and **Endogenous Depression** (L1, Proceed with Guardrails) — which may warrant separate dedicated evaluation reports given comparably strong trial/literature support.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

