---
layout: default
title: Midodrine
parent: Model Prediction Only (L5)
nav_order: 551
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Midodrine: predicted new indication Variably protease-sensitive prionopathy (evidence level L5). Approved use: Orthostatic hypotension, postural orthostatic tachycardia syndrome…"
monitor_inn: "Midodrine"
predicted_indications: ["variably protease-sensitive prionopathy", "faciodigitogenital syndrome", "attention deficit-hyperactivity disorder", "hypotensive disorder", "attention deficit hyperactivity disorder, inattentive type", "sinoatrial node disease", "monogenic obesity", "specific developmental disorder", "obsolete hypertelorism (disease)", "sinoatrial block"]
---

# Midodrine
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

# Midodrine: From Orthostatic Hypotension to Variably Protease-Sensitive Prionopathy

## One-Sentence Summary

Midodrine is an oral alpha-1 adrenergic agonist originally used to treat orthostatic hypotension and related autonomic disorders (multiple system atrophy, postural orthostatic tachycardia syndrome).
The TxGNN model's top-ranked prediction is **variably protease-sensitive prionopathy**, but **no clinical trials and no publications** support it, so it rests on a graph-based score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy (from the knowledge graph; the registration records list no indication text) |
| Predicted New Indication | Variably protease-sensitive prionopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled records. Midodrine is known to be a prodrug whose active metabolite, desglymidodrine, is a peripheral alpha-1 adrenergic agonist. It raises arteriolar and venous tone and therefore blood pressure. This fits its use in orthostatic hypotension.

Variably protease-sensitive prionopathy is a neurodegenerative protein-misfolding disease. **No identifiable mechanistic link** connects alpha-1 vasoconstriction to prion pathology. The very high score (99.99%) is a graph-based artefact until proven otherwise. At most, midodrine might offer symptomatic relief of autonomic dysfunction if it occurred in these patients. It would not modify the disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Midodrine has 20 valid single-ingredient registrations, all oral tablets, and none is cancelled. The registration records contain no approved-indication text. Five main registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 35010 | Cipmido 5mg Tablet (Cipla Ltd) | Strip of 30 tablets | Not stated in registration records |
| 136336 | Midorise 10 Tablet (Torrent Pharmaceuticals Ltd) | Strip of 10 tablets | Not stated in registration records |
| 134466 | Midora Tablet (Dr Reddy's Laboratories Ltd) | Strip of 30 tablets | Not stated in registration records |
| 108355 | Inramed 5 Tablet (Mylan Pharmaceuticals Pvt Ltd) | Strip of 10 tablets | Not stated in registration records |
| 133846 | Midodrive Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 20 tablets | Not stated in registration records |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease contraindication edges, not label text): adrenal gland pheochromocytoma, phaeochromocytoma, sympathetic paraganglioma, adrenal gland cancer, duodenum cancer, small intestine cancer, heart cancer, thyrotoxicosis, hyperthyroidism, Graves disease.
- **Drug Interactions**: 81 known interactions. Examples:
  - Moderate: other sympathomimetics and vasoconstrictors such as epinephrine (including ophthalmic and topical forms), ephedrine, phentermine, diethylpropion, mazindol, sibutramine and isometheptene. Also bupropion, lorcaserin, trospium, rolapitant and glycerol phenylbutyrate.
  - Minor: ranitidine, cimetidine and metformin.
- **Pharmacological cautions from the evaluation**: supine hypertension (avoid late-day dosing), urinary retention, and reflex bradycardia or conduction problems.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no literature and no plausible mechanistic link, so it is purely computational (L5).

**Best-supported alternative among the model's predictions:** *hypotensive disorder* (score 99.90%, evidence level L2, Proceed with Guardrails). It is backed by one completed Phase 2 trial, [NCT02893553](https://clinicaltrials.gov/study/NCT02893553) (n=21, hypotension in spinal cord injury), and several reviews and guideline-type papers, plus a randomised trial of midodrine with octreotide in hepatorenal syndrome ([PMID 25644760](https://pubmed.ncbi.nlm.nih.gov/25644760/)). This is largely a re-confirmation of the existing orthostatic hypotension use, not true repurposing.

**To proceed, the following is needed:**
- Any preclinical or clinical rationale linking midodrine to prion disease, or a decision to deprioritise this prediction
- Detailed mechanism of action data
- Package insert warnings and contraindications for India-marketed products, plus the approved-indication text
- A safety plan covering supine hypertension, bradycardia and the many drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

