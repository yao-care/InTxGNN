---
layout: default
title: Cisatracurium
parent: Model Prediction Only (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Cisatracurium: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Not stated in the registration data compiled for this report (general…"
monitor_inn: "Cisatracurium"
predicted_indications: ["cauda equina syndrome", "preeclampsia", "obsolete neurogenic bladder (disease)", "migraine disorder", "thrombotic disease", "irritable bowel syndrome", "migraine with brainstem aura", "mild pre-eclampsia", "severe pre-eclampsia", "neurocirculatory asthenia"]
---

# Cisatracurium
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

## Cisatracurium: From Neuromuscular Blockade in Anaesthesia to Cauda Equina Syndrome
{: .text-alpha }

## One-Sentence Summary

Cisatracurium is a non-depolarizing neuromuscular blocking agent given by injection, used as a muscle relaxant in anaesthesia and critical care.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but there are **no clinical trials** and **no publications** supporting this prediction.
The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. There is no plausible mechanistic rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report (generally used as a neuromuscular blocker during anaesthesia) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (7 of 7) – CDSCO approval status is not included in this data |
| Number of Listed Products | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for cisatracurium: "Cisatracurium besylate binds competitively to cholinergic receptors on the motor end-plate to antagonize the action of acetylcholine, resulting in blockade of neuromuscular transmission. This action is antagonized by acetylcholinesterase inhibitors such as neostigmine." ([DailyMed: cisatracurium besylate prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=67908e20-044d-454d-9c51-bf106e817bd0), label version 2026-10-14; accessed 2026-11-19.) Cisatracurium is generally known as a non-depolarizing neuromuscular blocker that acts at nicotinic acetylcholine receptors of the motor endplate, producing skeletal muscle relaxation.

This mechanism offers no plausible link to cauda equina syndrome. That condition is a compressive neurological emergency that requires surgical decompression, not muscle paralysis. The high TxGNN score (0.9999) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or pharmacological or clinical reasoning.

The other top-ranked predictions (preeclampsia, neurogenic bladder, migraine, thrombotic disease, irritable bowel syndrome and others) show the same weakness. None has a therapeutic mechanism supported by clinical data. The two papers retrieved for preeclampsia and the one paper for thrombotic disease concern anaesthesia care in cesarean section and liver transplantation. In those papers cisatracurium would at most be an incidental co-administered anaesthetic, not a treatment for the disease.

## Clinical Trial Evidence

Currently no related clinical trials registered for cauda equina syndrome.

## Literature Evidence

Currently no related literature available for cauda equina syndrome.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 41637 | Cisblok 20mg Injection (Abbott) | Vial of 10 ml injection | Not stated |
| 42184 | Cis-Atrabloc 20 Injection (Varenyam Healthcare) | Vial of 10 ml injection | Not stated |
| 45296 | Cis-Atrabloc 10 Injection (Varenyam Healthcare) | Vial of 5 ml injection | Not stated |
| 39104 | Cisartacil 10mg Injection (Neon Laboratories) | Vial of 5 ml injection | Not stated |
| 37442 | Cisblok 10mg Injection (Abbott) | Vial of 5 ml injection | Not stated |

All 7 registrations are valid single-ingredient injectables. The table lists the first 5.

## Safety Considerations

- **Drug Interactions**: 61 interactions were identified in total. Examples from the compiled list:
  - **Major**: kanamycin, neomycin, paromomycin, polymyxin B, streptomycin. These aminoglycoside and polymyxin antibiotics can potentiate neuromuscular blockade.
  - **Moderate**: amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), doxycycline, minocycline, tetracycline, magnesium sulfate, magnesium chloride, mannitol, metoclopramide, vancomycin, neomycin (topical).
  - **Minor**: ranitidine, ranitidine (bismuth citrate).
- Magnesium sulfate is particularly relevant in severe preeclampsia, where potentiated blockade is a safety concern.
- Systemic neuromuscular blockade requires ventilatory support.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN model (deep learning) score alone, which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or literature, and no plausible mechanism links neuromuscular blockade to cauda equina syndrome. Other top-ranked predictions are similarly unsupported, and the few papers found describe incidental anaesthetic use only.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India registration, as the current safety data is incomplete
- Approved indication text for the India licences, which is currently blank
- Mechanism of action data from DrugBank
- A credible mechanistic hypothesis and preclinical evidence before any clinical consideration
- Otherwise, deprioritise this candidate in favour of repurposing candidates with supporting clinical data

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: cisatracurium besylate prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=67908e20-044d-454d-9c51-bf106e817bd0) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

