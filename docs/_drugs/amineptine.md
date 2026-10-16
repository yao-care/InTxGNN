---
layout: default
title: Amineptine
parent: Model Prediction Only (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Amineptine: predicted new indication Agoraphobia (evidence level L5). Approved use: Anxiety disorder, neurotic disorder, dysthymic disorder"
monitor_inn: "Amineptine"
predicted_indications: ["agoraphobia", "benign paroxysmal torticollis of infancy", "obsessive-compulsive disorder", "neurotic depression", "migraine disorder", "melancholia", "migraine with brainstem aura", "paranoid personality disorder", "histrionic personality disorder (disease)", "schizotypal personality disorder"]
---

# Amineptine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Amineptine: From Anxiety and Dysthymic Disorders to Agoraphobia

## One-Sentence Summary

Amineptine is a dopaminergic antidepressant, originally used for anxiety disorder, neurotic disorder and dysthymic disorder.
The TxGNN model predicts it may be effective for **agoraphobia**, but there are **0 registered clinical trials** and only **1 loosely related publication** (a review that does not concern amineptine directly), so this prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder, neurotic disorder, dysthymic disorder (the India licence record lists no approved indication text) |
| Predicted New Indication | Agoraphobia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for the original record is not available. The published literature describes amineptine as a tricyclic antidepressant that selectively reduces dopamine uptake, acting on the dopaminergic system. Its original indications already include anxiety disorder, so a plausible link to phobic anxiety exists.

However, the only publication retrieved for agoraphobia is a 1995 review of reversible MAO-A inhibitors. It does not address amineptine and offers no direct support. The high TxGNN score is a model prediction, not evidence of efficacy. Agoraphobia is usually treated with serotonergic agents, and amineptine has little serotonergic activity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7717094](https://pubmed.ncbi.nlm.nih.gov/7717094/) | 1995 | Review | Acta Psychiatr Scand Suppl | Review of reversible MAO-A inhibitors (brofaromine, moclobemide, toloxatone) in depression. Amineptine appears only as a comparator, so the paper gives no direct support for agoraphobia. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 202233 | Survector 100mg Tablet (Serdia Pharmaceuticals India Pvt Ltd) | Strip of 10 tablets | Not stated in the licence record |

## Safety Considerations

Please refer to the package insert for safety information.

The literature compiled for this report also points to concerns that need guardrails in any further work:
- Hepatotoxicity and abuse/dependence have led to withdrawal or restriction of amineptine in several markets.
- Case literature reports dose-related acneiform eruptions (PMID 11730047) and chronic abuse (PMID 2275948).
- As a dopaminergic agent, it carries a theoretical risk of worsening psychotic-spectrum symptoms.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The agoraphobia prediction has no clinical trials and no direct literature, and the mechanistic rationale is weak. The safety history of amineptine (hepatotoxicity, dependence) raises the bar for any new use.

**To proceed, the following is needed:**
- Mechanism of action data and receptor-profile analysis relevant to phobic anxiety
- The India package insert (warnings, contraindications, approved indication)
- Preclinical or small exploratory clinical data in agoraphobia or panic-related anxiety
- A hepatic and dependence risk-management plan

## Other Predictions Considered

The ranked list included other predicted indications. None is stronger than agoraphobia as a true repurposing candidate:

- **Neurotic depression** and **melancholia** (99.77% and 99.77%, evidence level L3): neurotic depression overlaps with dysthymia, an existing indication, so it is essentially not new repurposing. The supporting literature is mainly dysthymia reviews and an RCT of amisulpride versus amineptine versus placebo (PMID 9892856). Evidence for melancholia is indirect. Both warrant a research question rather than a decision to proceed.
- **Obsessive-compulsive disorder**, **migraine disorder**, **migraine with brainstem aura**, **benign paroxysmal torticollis of infancy**, and **paranoid, histrionic and schizotypal personality disorders**: all L5, with no meaningful clinical or literature support. The identical scores across the personality disorders suggest a graph-based artifact, and dopaminergic stimulation could theoretically worsen paranoid or schizotypal symptoms.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

