---
layout: default
title: Tamsulosin
parent: Model Prediction Only (L5)
nav_order: 806
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Tamsulosin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
monitor_inn: "Tamsulosin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine with brainstem aura"]
---

# Tamsulosin
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

## Tamsulosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita
{: .text-alpha }

## One-Sentence Summary

Tamsulosin is an alpha-1 adrenergic receptor blocker originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but **no clinical trials and no supporting publications** were found for this prediction.
The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Tamsulosin is known as an alpha-1A/1D adrenergic receptor antagonist. It relaxes smooth muscle in the prostate and bladder neck, which improves urinary flow in BPH.

The new indication is a rare congenital hair-growth disorder with a genetic developmental basis. No credible pathway links alpha-1 adrenergic blockade to this condition. The very high score (rank 202 in the model's output) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top predictions fall into similar groups, with no supporting evidence:
- Hair and skin conditions: hypertrichosis, isolated genetic hair shaft abnormality, hypotrichosis simplex of the scalp, congenital hypotrichosis milia, diffuse alopecia areata and alopecia.
- Congenital malformation syndromes: one with a dental/periodontal component and one with a Dandy-Walker malformation.
- Neurological: migraine with brainstem aura.

For hypertrichosis, any hair-growth effect would be an adverse-effect signal, not a therapeutic one, and the direction of effect is undetermined.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the lead prediction.

For the ninth-ranked prediction (alopecia), two publications were retrieved, but neither supports tamsulosin as a treatment:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33175100](https://pubmed.ncbi.nlm.nih.gov/33175100/) | 2021 | Cohort / pharmacovigilance | JAMA Dermatology | Suicidality and psychological adverse events with finasteride (not tamsulosin) |
| [32826647](https://pubmed.ncbi.nlm.nih.gov/32826647/) | 2021 | Cross-sectional | Cornea | Meibomian gland changes in men with BPH (ocular findings, not alopecia treatment) |

## India Market Information

The 20 registrations are all valid single-ingredient licences. Five main ones are listed below; the approved indication text is not available in the compiled data.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 224386 | Tamsugrap Tablet | Strip of 10 tablets | Not specified |
| 233227 | Veltam 0.4 Tablet MR | Strip of 15 modified-release tablets | Not specified |
| 230204 | Urimax 0.4 Capsule MR | Strip of 20 modified-release capsules | Not specified |
| 128535 | Losin 0.4mg Tablet | Strip of 10 tablets | Not specified |
| 96101 | Geriflo-D Tablet SR | Bottle of 15 sustained-release tablets | Not specified |

All available dosage forms are oral.

## Safety Considerations

- **Contraindications / risk conditions (from the knowledge graph, not label text)**: multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, liver disease, gallbladder disease, priapism, and intraoperative floppy iris syndrome.
- **Drug Interactions**: 202 interactions are recorded. The only **Major** interaction among those listed is **clarithromycin**. Moderate interactions include bupropion, aprepitant, morphine, lorcaserin, cimetidine, the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), clotrimazole, miconazole, fenfluramine, dexfenfluramine, eliglustat, dronabinol, nabilone and opium.
- **Tolerability note**: Tamsulosin's vasodilatory and hypotensive effects could be a concern in any new population, for example in migraine.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials, no supporting literature, and no plausible mechanism linking alpha-1 blockade to this rare genetic hair disorder. Evidence is model prediction only (L5). The same holds for the other nine top predictions.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA), for example from DrugBank
- Package insert warnings and contraindications from the India regulatory source, needed before safety screening
- Any preclinical or mechanistic evidence linking alpha-1 adrenergic signalling to hair follicle biology
- Review of whether the TxGNN model (deep learning) score reflects similarities the model learned between related diseases rather than biological evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

