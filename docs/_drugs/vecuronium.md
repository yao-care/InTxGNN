---
layout: default
title: Vecuronium
parent: Model Prediction Only (L5)
nav_order: 885
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Vecuronium: predicted new indication insomnia (disease) (evidence level L5). Approved use: Not stated in the licence records (approved indication text is empty)"
monitor_inn: "Vecuronium"
predicted_indications: ["insomnia (disease)", "irritable bowel syndrome"]
---

# Vecuronium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Vecuronium: From Neuromuscular Blockade in Anaesthesia to insomnia (disease)
{: .text-alpha }

## One-Sentence Summary

Vecuronium is a non-depolarising neuromuscular blocker. Its approved indication text is not available in the data compiled for this report, but it is used as a muscle relaxant in general anaesthesia.
The TxGNN model predicts it may be effective for **insomnia**, but there is only **1 registered clinical trial** (a generic paediatric pharmacokinetics study with no insomnia endpoint) and **no publications** supporting this direction.
The prediction is best read as a model artefact rather than a credible repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (approved indication text is empty) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 0.9934 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for vecuronium: "Vecuronium is a nondepolarizing neuromuscular blocking agent possessing all of the characteristic pharmacological actions of this class of drugs (curariform). It acts by competing for cholinergic receptors at the motor end-plate." ([DailyMed: vecuronium bromide prescribing information, Phlow Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b012b1b1-9e59-4525-8f4d-dae98344d15f), label version 2026-10-23; accessed 2026-11-19.) Based on known pharmacology, vecuronium blocks nicotinic acetylcholine receptors at the neuromuscular junction. This produces skeletal muscle relaxation during surgery and intubation.

The mechanistic link to insomnia is weak. Vecuronium has no sedative, hypnotic or central nervous system activity. The high TxGNN score (0.9934) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other top-ranked predictions show the same pattern. These include irritable bowel syndrome, neurocirculatory asthenia, benign prostatic hyperplasia, cauda equina syndrome, headache disorder, rhinitis, anxiety, trigeminal autonomic cephalalgia and migraine disorder. None has a plausible mechanism, and most have no direct evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3520 | Paediatric pharmacokinetics of understudied drugs given as standard of care. It does not test vecuronium for insomnia and provides no efficacy evidence. |

---

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 30516 | Brufage 10mg Injection | Vial of 1 ml Injection | Valid |
| 49186 | Cefronium 10 Injection | Vial of 1 Injection | Valid |
| 89032 | Flexivec 10mg Injection | Vial of 10 ml Injection | Valid |
| 118323 | Kabivec 4mg Injection | Vial of 2 ml Injection | Valid |
| 129231 | Lyvec 10mg Injection | Vial of 1 Injection | Valid |
| 150853 | Neovec 4mg Injection | Vial of 5 ml Injection | Valid |
| 151167 | Neovec 10mg Injection | Vial of 10 ml Injection | Valid |
| 202741 | Samvec 4mg Injection | Vial of 2 ml Injection | Valid |
| 208781 | Supervac 4mg Injection | Vial of 2 ml Injection | Valid |
| 209573 | Supervac 10mg Injection | Vial of 10 ml Injection | Valid |
| 224350 | Troyvec 10mg Injection | Vial of 5 ml Injection | Valid |
| 235167 | Vecuron 10mg Injection | Vial of 10 ml Injection | Valid |
| 235728 | Vecurofix 4 Injection | Vial of 1 Injection | Valid |
| 236872 | Vecurofix 10 Injection | Vial of 1 Injection | Valid |
| 237469 | Veroni 10mg Injection | Vial of 5 ml Injection | Valid |
| 237616 | Vecubro 4mg Injection | Vial of 1 Injection | Valid |
| 237825 | Verunium 4mg Injection | Vial of 2 ml Injection | Valid |
| 239897 | Vercurex 4mg Injection | Vial of 1 Powder for Injection | Valid |
| 239954 | Verbo 10mg Injection | Vial of 1 Injection | Valid |
| 240575 | Verbo 4mg Injection | Vial of 1 Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

There are 20 valid single-ingredient registrations in total, all injectable.

---

## Safety Considerations

- **Drug Interactions:** The interaction screening returned 85 interacting drugs. Notable **Major** interactions include:
  - Paromomycin
  - Kanamycin
  - Neomycin

  **Moderate** interactions include:
  - Aminoglycoside and tetracycline-class antibiotics (doxycycline, tetracycline, minocycline)
  - Vancomycin
  - Amphotericin B
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, prednisone)
  - Magnesium salts
  - Mannitol
  - Metoclopramide

  **Minor** interactions include ranitidine.

Please refer to the package insert for warnings and contraindications.

Because vecuronium paralyses muscles without causing sedation, using it outside a monitored anaesthetic setting carries serious risks, including patient distress and awareness.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no trials or literature supporting efficacy in insomnia, and vecuronium has no sedative or hypnotic activity. The apparent signal likely comes from its co-use with sedatives during anaesthesia.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator
- Mechanism of action data
- Any plausible mechanistic or preclinical rationale linking neuromuscular blockade to sleep regulation
- A safety assessment of using a paralysing agent outside the anaesthetic setting

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: vecuronium bromide prescribing information, Phlow Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b012b1b1-9e59-4525-8f4d-dae98344d15f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

