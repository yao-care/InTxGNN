---
layout: default
title: Midodrine
parent: Model Prediction Only (L5)
nav_order: 551
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Midodrine"
predicted_indications: ["variably protease-sensitive prionopathy", "faciodigitogenital syndrome", "attention deficit-hyperactivity disorder", "hypotensive disorder", "attention deficit hyperactivity disorder, inattentive type", "sinoatrial node disease", "monogenic obesity", "specific developmental disorder", "obsolete hypertelorism (disease)", "sinoatrial block"]
description: "Midodrine: predicted new indication Variably protease-sensitive prionopathy (evidence level L5). In India: at least 20 listed products"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Midodrine: Variably protease-sensitive prionopathy
{: .text-alpha }

## One-Sentence Summary

Midodrine is an oral alpha-1 adrenergic agonist originally used to treat orthostatic hypotension and related autonomic disorders (multiple system atrophy, postural orthostatic tachycardia syndrome).
The TxGNN model's top-ranked prediction is **variably protease-sensitive prionopathy**, but **no clinical trials and no publications** support it. It rests on a TxGNN model (deep learning) score alone, which may reflect similarities the model learned between related diseases, not biological evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Variably protease-sensitive prionopathy |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for midodrine: "Midodrine hydrochloride forms an active metabolite, desglymidodrine, that is an alpha 1 -agonist, and exerts its actions via activation of the alpha-adrenergic receptors of the arteriolar and venous vasculature, producing an increase in vascular tone and elevation of blood pressure. Desglymidodrine does not stimulate cardiac beta-adrenergic receptors." ([DailyMed: midodrine hydrochloride prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5a6705af-bb72-4edb-863a-93a351bd6dba), label version 2026-11-12; accessed 2026-11-19.) Midodrine is known to be a prodrug whose active metabolite, desglymidodrine, is a peripheral alpha-1 adrenergic agonist. It raises arteriolar and venous tone and therefore blood pressure. This fits its use in orthostatic hypotension.

Variably protease-sensitive prionopathy is a neurodegenerative protein-misfolding disease. **No identifiable mechanistic link** connects alpha-1 vasoconstriction to prion pathology. The very high score (0.9999) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At most, midodrine might offer symptomatic relief of autonomic dysfunction if it occurred in these patients. It would not modify the disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Midodrine has 20 valid single-ingredient registrations, all oral tablets, and none is cancelled. The registration records contain no approved-indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 810 | Aladrine 2.5mg Tablet | Bottle of 60 tablets | Valid |
| 1433 | Actiful 2.5mg Tablet | Strip of 15 tablets | Valid |
| 34778 | Cipmido 2.5mg Tablet | Strip of 20 tablets | Valid |
| 35010 | Cipmido 5mg Tablet | Strip of 30 tablets | Valid |
| 94213 | Gutron 2.5mg Tablet | Strip of 20 tablets | Valid |
| 104034 | Hypodrin 2.5 Tablet | Strip of 10 tablets | Valid |
| 108184 | Inramed 2.5 Tablet | Bottle of 100 tablets | Valid |
| 108355 | Inramed 5 Tablet | Strip of 10 tablets | Valid |
| 113966 | Jolavi Tablet | Strip of 10 tablets | Valid |
| 133820 | Midgeo Tablet | Strip of 10 tablets | Valid |
| 133846 | Midodrive Tablet | Strip of 20 tablets | Valid |
| 134070 | Midorise 5 Tablet | Strip of 10 tablets | Valid |
| 134247 | Midotab 2.5 Tablet | Strip of 20 tablets | Valid |
| 134375 | Midorise 2.5 Tablet | Strip of 20 tablets | Valid |
| 134466 | Midora Tablet | Strip of 30 tablets | Valid |
| 136213 | Midotril 2.5mg Tablet | Strip of 20 tablets | Valid |
| 136336 | Midorise 10 Tablet | Strip of 10 tablets | Valid |
| 136807 | Midores 2.5 Tablet | Strip of 10 tablets | Valid |
| 243791 | Xidorin Tablet | Strip of 20 tablets | Valid |
| 243853 | Xidorin 5 Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

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

**Best-supported alternative among the model's predictions:** *hypotensive disorder* (score 0.9990, evidence level L2, Proceed with Guardrails). It is backed by one completed Phase 2 trial, [NCT02893553](https://clinicaltrials.gov/study/NCT02893553) (n=21, hypotension in spinal cord injury), and several reviews and guideline-type papers, plus a randomised trial of midodrine with octreotide in hepatorenal syndrome ([PMID 25644760](https://pubmed.ncbi.nlm.nih.gov/25644760/)). This is largely a re-confirmation of the existing orthostatic hypotension use, not true repurposing.

**To proceed, the following is needed:**
- Any preclinical or clinical rationale linking midodrine to prion disease, or a decision to deprioritise this prediction
- Detailed mechanism of action data
- Package insert warnings and contraindications for India-marketed products, plus the approved-indication text
- A safety plan covering supine hypertension, bradycardia and the many drug interactions

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled records" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: midodrine hydrochloride prescribing information, Bryant Ranch Prepack](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5a6705af-bb72-4edb-863a-93a351bd6dba) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

