---
layout: default
title: Rivastigmine
parent: Model Prediction Only (L5)
nav_order: 748
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
monitor_inn: "Rivastigmine"
predicted_indications: ["glaucoma"]
description: "Rivastigmine: predicted new indication Glaucoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Rivastigmine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Rivastigmine: Glaucoma
{: .text-alpha }

## One-Sentence Summary

Rivastigmine is a cholinesterase inhibitor originally used to treat Alzheimer's disease and related neurodegenerative conditions.
The TxGNN model predicts it may be effective for **glaucoma**, but there are currently **no registered clinical trials** and only **3 publications** (one rabbit study, two reviews) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Glaucoma |
| TxGNN Prediction Score | 0.9927 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known class pharmacology, rivastigmine inhibits both acetylcholinesterase and butyrylcholinesterase, which raises acetylcholine levels. Its efficacy in Alzheimer's disease rests on this cholinergic enhancement.

In the eye, higher acetylcholine levels can promote ciliary muscle contraction and increase outflow through the trabecular meshwork, which lowers intraocular pressure (IOP). This is analogous to cholinergic agents such as pilocarpine and physostigmine, which have been used in glaucoma. A rabbit study reported that topical rivastigmine lowered IOP in normotensive animals, and a 2024 systems genetics and molecular modelling review supports the involvement of cholinergic pathways in IOP regulation.

The very high TxGNN score is a computational prediction only and does not count as clinical evidence. The link to glaucoma currently rests on class pharmacology and animal data.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10673128](https://pubmed.ncbi.nlm.nih.gov/10673128/) | 2000 | Preclinical (rabbit) | J Ocul Pharmacol Ther | Topical rivastigmine, a selective acetylcholinesterase inhibitor, lowered intraocular pressure in normotensive rabbits |
| [39130374](https://pubmed.ncbi.nlm.nih.gov/39130374/) | 2024 | Review / computational | Front Mol Biosci | Examines cholinergic agents for IOP reduction, noting that approved M3 agonists have systemic cholinergic side effects that limit use |
| [27967267](https://pubmed.ncbi.nlm.nih.gov/27967267/) | 2017 | Review | Expert Opin Ther Pat | Patent review of acetylcholinesterase inhibitors; notes mild AChE inhibition has therapeutic relevance in Alzheimer's disease, myasthenia gravis and glaucoma |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 74369 | Exelon 1.5mg Capsule (Novartis India Ltd) | Strip of 14 capsules | Not stated |
| 75384 | Exelon Patch 15 (Novartis India Ltd) | Packet of 30 transdermal patches | Not stated |
| 184369 | Rivamer 1.5 Capsule (Sun Pharmaceutical Industries Ltd) | Strip of 10 capsules | Not stated |
| 186899 | Rivera 1.5mg Capsule (Zydus Cadila) | Strip of 10 capsules | Not stated |
| 189024 | Rivaplast 9mg Transdermal Patch (Zuventus Healthcare Ltd) | Packet of 3 transdermal patches | Not stated |

All 20 registrations are valid single-ingredient products, available as oral capsules and tablets and as transdermal patches.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these are graph-derived associations, not label text): epilepsy, basal ganglia disease, focal hand dystonia, blepharospasm, chronic obstructive pulmonary disease, asthma (including intrinsic and allergic), diarrhoeal disease, sudden cardiac arrest, heart conduction disease, atrioventricular block, sick sinus syndrome, anorexia nervosa, active peptic ulcer disease, urinary tract obstruction, and parkinsonian disorders including Parkinson disease.
- **Drug Interactions**: 170 interactions were identified. The one rated Major is **bupropion**. Many Moderate ones involve anticholinergic or antispasmodic agents (atropine, hyoscyamine, glycopyrronium, dicyclomine, trospium, clidinium, mepenzolate), which can oppose rivastigmine's effect. Others include H2 blockers (famotidine, ranitidine, cimetidine), clarithromycin, levofloxacin, metronidazole, loperamide, dolasetron and palonosetron.

Please also refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The glaucoma prediction is supported by a plausible cholinergic mechanism and a single rabbit study, but no human trials exist and the evidence level is L4. The knowledge-graph contraindication signals (e.g. asthma, COPD, cardiac conduction disorders) also warrant attention, since cholinergic agents carry systemic risk.

**To proceed, the following is needed:**
- Detailed mechanism of action data
- Package insert warnings and contraindications from the India regulator
- Confirmation of the approved indication text for the India licences
- Further preclinical work, including ocular pharmacokinetics, tolerability and replication of the IOP-lowering effect in additional models
- Assessment of whether a topical ocular formulation is feasible, since existing India products are oral or transdermal
- A systemic safety assessment for the cardiac, respiratory and gastrointestinal signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

