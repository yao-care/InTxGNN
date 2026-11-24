---
layout: default
title: Enalaprilat
parent: Model Prediction Only (L5)
nav_order: 305
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Enalaprilat: predicted new indication Primary hereditary glaucoma (evidence level L5). Approved use: Hypertensive disorder, hypertension, congestive heart failure…"
monitor_inn: "Enalaprilat"
predicted_indications: ["primary hereditary glaucoma"]
---

# Enalaprilat
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

## Enalaprilat: From Hypertension and Heart Failure to Primary Hereditary Glaucoma
{: .text-alpha }

## One-Sentence Summary

Enalaprilat is an injectable ACE inhibitor (the active form of enalapril), originally used to treat hypertension and heart failure.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**,
but at present there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the computational score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder, hypertension, congestive heart failure, heart failure (the licence record contains no approved indication text) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 0.9909 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for enalaprilat: "Intravenous enalaprilat, or oral enalapril, after hydrolysis to enalaprilat, inhibits ACE in human subjects and animals. ACE is a peptidyl dipeptidase that catalyzes the conversion of angiotensin I to the vasoconstrictor substance, angiotensin II." ([DailyMed: enalaprilat prescribing information, Dr. Reddys Laboratories Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5d398da1-020c-ccb1-a775-ce8e0b29d621), label version 2024-06-07; accessed 2026-11-19.) Based on known information, enalaprilat is the active diacid metabolite of enalapril and an angiotensin-converting enzyme (ACE) inhibitor. Its efficacy in hypertension and heart failure is established, and it may mechanistically be applicable to glaucoma through the renin-angiotensin system.

A plausible but unproven link is the local renin-angiotensin system in the eye, which is expressed in the ciliary body and trabecular meshwork. In theory, ACE inhibition could lower intraocular pressure by altering aqueous humor dynamics or by improving ocular perfusion. This remains hypothetical.

There are important caveats. Primary hereditary glaucoma (for example, congenital or juvenile forms) is typically driven by structural developmental defects of the anterior chamber angle or by mutations in genes such as MYOC, CYP1B1 and FOXC1. These pathways are not clearly modulated by ACE inhibition. In addition, enalaprilat is available only as an intravenous injection, which makes it impractical for a chronic eye condition. The high TxGNN score is a computational prediction with no clinical validation.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 72883 | Envas Injection | Ampoule of 1 ml Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: The drug-disease contraindication links in the TxGNN knowledge graph include angioedema, acquired angioedema, renin-angiotensin-aldosterone system-blocker-induced angioedema, non-histaminic angioedema, hereditary angioedema, and hereditary angioedema with C1 inhibitor deficiency.
- **Drug Interactions**: The only recorded item is pharmacological, not a drug-drug interaction: enalaprilat's target is angiotensin-converting enzyme (ACE), which is its intended mechanism.

Please refer to the package insert for other safety information, such as warnings.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high computational prediction score. No clinical trials or publications were found, the mechanistic link to hereditary glaucoma is speculative, and the intravenous-only formulation does not suit a chronic ocular indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for Envas Injection, to allow safety screening
- Detailed mechanism of action data (for example, from DrugBank)
- Preclinical or clinical evidence that ACE inhibition lowers intraocular pressure or benefits hereditary glaucoma
- An assessment of route and formulation feasibility (for example, topical or other ocular delivery)

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available from the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: enalaprilat prescribing information, Dr. Reddys Laboratories Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5d398da1-020c-ccb1-a775-ce8e0b29d621) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

