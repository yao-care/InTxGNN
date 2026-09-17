---
layout: default
title: Sumatriptan
parent: Model Prediction Only (L5)
nav_order: 793
evidence_level: L5
indication_count: 1
---

# Sumatriptan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Sumatriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

> Sumatriptan is a selective 5-HT1B/1D receptor agonist originally established for the acute treatment of migraine.
> The TxGNN model predicts it may also be effective for **Migraine with Brainstem Aura**, a subtype that has historically been *excluded* from triptan trials on theoretical safety grounds rather than lack of efficacy.
> Currently **0 dedicated clinical trials** and **20 related publications** (mostly on migraine/aura generally) support this direction, with no data specific to the brainstem-aura subtype itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine (general acute treatment) — inferred from mechanistic rationale in evidence pack; no formal Taiwan/India license text available |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 (mechanism/rationale-based; no dedicated clinical trials for this subtype) |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed formal MOA documentation for this drug is currently a data gap (`DG002`). However, the evidence pack's repurposing rationale provides substantive pharmacological detail: Sumatriptan is a selective 5-HT1B/1D receptor agonist that relieves migraine by constricting cranial blood vessels and inhibiting the release of inflammatory neuropeptides (e.g., CGRP) from perivascular trigeminal axons following trigeminovascular system activation. This mechanism underlies its established efficacy in ordinary migraine.

Migraine with brainstem aura (previously "basilar-type migraine") involves posterior-circulation (vertebrobasilar) symptoms. Triptans have traditionally been listed as a *relative contraindication* in this subtype by most guidelines (including AHS/AAN) due to a **theoretical** vasoconstrictive risk in posterior circulation vessels — not because of demonstrated lack of efficacy. As a result, patients with this aura subtype have routinely been excluded from triptan clinical trials, creating an evidence gap driven by trial-exclusion practice rather than a genuine efficacy or mechanistic uncertainty.

Supporting this interpretation, literature on sumatriptan in migraine *with* aura generally (as opposed to specifically brainstem aura) shows retained — if somewhat reduced — efficacy compared to migraine without aura, and regulatory reviews have approved sumatriptan formulations for "migraine with or without aura" as a broad label. This suggests the TxGNN signal may reflect a real but currently unverified therapeutic opportunity contingent on resolving the safety-exclusion issue specific to the brainstem-aura subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33567890](https://pubmed.ncbi.nlm.nih.gov/33567890/) | 2021 | RCT | Cephalalgia | Early sumatriptan treatment prevented PACAP38-induced migraine attacks, supporting efficacy against trigeminovascular activation relevant to aura pathophysiology |
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT | Cephalalgia | Double-blind, placebo-controlled trial: oral sumatriptan 200mg effective in acute treatment of migraine **with aura** (classical migraine) |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort/Comparative | Neurology | Sumatriptan efficacy was reduced in migraine attacks with aura vs. without aura — relevant to dosing/counseling expectations |
| [25841027](https://pubmed.ncbi.nlm.nih.gov/25841027/) | 2015 | Editorial/Review | Neurology | Commentary on whether presence of aura predicts migraine severity and triptan treatment response |
| [21469920](https://pubmed.ncbi.nlm.nih.gov/21469920/) | 2011 | Regulatory Review | Expert Rev Neurother | Needle-free subcutaneous sumatriptan (Sumavel DosePro) approved for acute treatment of migraine with or without aura, and cluster headache |
| [8559405](https://pubmed.ncbi.nlm.nih.gov/8559405/) | 1996 | Clinical Study | Neurology | Early study on subcutaneous sumatriptan's effect during the migraine aura phase itself |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Review | Cephalalgia | Critical review of clinical experience with sumatriptan in migraine and cluster headache management |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline/Review | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies, including triptans |
| [31135819](https://pubmed.ncbi.nlm.nih.gov/31135819/) | 2019 | Imaging/Mechanistic | JAMA Neurology | PET study showing sumatriptan's association with central 5-HT1B receptor binding, clarifying CNS mechanism relevant to brainstem-involving subtypes |
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | Phytother Res | RCT comparing ginger vs. sumatriptan in acute migraine (general, without aura) — supporting general efficacy evidence base |

---

## India Market Information

No registration records found. This drug is currently **not marketed** in the covered jurisdiction (`total_licenses: 0`), so no product/dosage-form/indication data is available for review.

---

## Safety Considerations

**Drug Interactions** (from DDI database, 114 total interactions on record; key high-severity findings shown below):

| Interacting Drug | Level | Note |
|---|---|---|
| Dexfenfluramine | Major | Serotonergic agent — serotonin syndrome risk |
| Fenfluramine | Major | Serotonergic agent — serotonin syndrome risk |
| Lorcaserin | Major | Serotonergic agent — serotonin syndrome risk |
| Sibutramine | Major | Serotonergic agent — serotonin syndrome risk |
| Dolasetron | Major | 5-HT3 antagonist — serotonin syndrome risk |
| Granisetron | Major | 5-HT3 antagonist — serotonin syndrome risk |
| Ondansetron | Major | 5-HT3 antagonist — serotonin syndrome risk |
| Palonosetron | Major | 5-HT3 antagonist — serotonin syndrome risk |
| Morphine | Moderate | Additive CNS/serotonergic effects |
| Morphine (liposomal) | Moderate | Additive CNS/serotonergic effects |

The Major-level interactions cluster around serotonergic agents and 5-HT3 receptor antagonists, consistent with the known class-wide serotonin syndrome risk for triptans; this should be factored into any co-medication review (notably antiemetics commonly used alongside migraine treatment).

Formal package-insert warnings and contraindications are a data gap (`DG001`, **Blocking** severity) and must be obtained before safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication targets a migraine subtype (brainstem aura) that most guidelines flag as a *relative contraindication* for triptans due to theoretical vasoconstriction risk in posterior circulation — this is a safety-driven evidence gap, not a mechanism-driven one. Combined with the absence of official label warnings/contraindications (`DG001`, Blocking) and the drug's current unmarketed status, there is insufficient basis to advance past initial safety screening (S1).

**To proceed, the following is needed:**
- Official TFDA/local label warnings and contraindications for Sumatriptan (`DG001` — download and parse product label PDF)
- Formal DrugBank-sourced MOA documentation (`DG002`)
- Targeted literature/case-series review specifically on triptan use in confirmed brainstem-aura migraine (beyond general aura literature)
- Clarification of why this subtype was historically excluded from RCTs (regulatory precedent review) before any efficacy claim can be supported
- A defined regulatory pathway, since the drug currently holds no local market authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

