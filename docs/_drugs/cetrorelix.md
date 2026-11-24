---
layout: default
title: Cetrorelix
parent: Model Prediction Only (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
description: "Cetrorelix: predicted new indication hypertrichosis (evidence level L5). Approved use: Inhibition of premature LH surges in women undergoing controlled ovar…"
monitor_inn: "Cetrorelix"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "persistent fetal circulation syndrome", "familial isolated trichomegaly", "familial male-limited precocious puberty", "aromatase excess syndrome", "centra precocious puberty 1"]
---

# Cetrorelix
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

## Cetrorelix: From Controlled Ovarian Stimulation to hypertrichosis
{: .text-alpha }

## One-Sentence Summary

Cetrorelix is a GnRH receptor antagonist used to prevent premature LH surges in women undergoing controlled ovarian stimulation as part of fertility treatment.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it is a model-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Inhibition of premature LH surges in women undergoing controlled ovarian stimulation (fertility treatment). The India licence records contain no indication text, so this comes from the pharmacology data compiled for this report. |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (16 of 16) – CDSCO approval status is not included in this data |
| Number of Listed Products | 16 (valid: 16) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for cetrorelix: "GnRH induces the production and release of luteinizing hormone (LH) and follicle stimulating hormone (FSH) from the gonadotrophic cells of the anterior pituitary. Due to a positive estradiol (E2) feedback at midcycle, GnRH liberation is enhanced resulting in an LH-surge." ([DailyMed: Cetrotide (cetrorelix acetate) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=aca7768e-28a7-4027-b1d8-e66247665f79), label version 2025-09-22; accessed 2026-11-19.) From the pharmacology information, cetrorelix is a peptide antagonist of the GnRH1 receptor (GNRHR). It suppresses LH and FSH, and therefore downstream sex steroids, without the initial flare seen with GnRH agonists.

The link to hypertrichosis is weak. Hypertrichosis is not primarily driven by gonadotropins. Androgen suppression might matter only in a hormone-dependent subset of patients. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No clinical or literature evidence supports it.

The other top-ranked predictions are mostly congenital or structural conditions (for example Ambras syndrome, Dandy-Walker malformation, hair shaft abnormalities) with no plausible GnRH-axis mechanism. They look like network artifacts from shared phenotype nodes. The most biologically credible candidate in the list is **central precocious puberty**, because it is driven by early activation of the GnRH axis. However, standard care is GnRH agonist therapy, short-acting cetrorelix is not well suited to chronic paediatric use, and no direct evidence is available. Familial male-limited precocious puberty is flagged as a research question only, since its driver (activating LHCGR mutations) acts downstream of GnRH and LH.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 1632 | Asporelix 0.25mg Injection | Vial of 1 Injection | Valid |
| 34799 | Cetrotide 0.25mg Injection | Vial of 1 Injection | Valid |
| 35079 | Cetrolix 0.25mg Injection | Vial of 1 Injection | Valid |
| 35891 | Ciscure 0.25mg Injection | Vial of 2 ml Injection | Valid |
| 36933 | Cetnosurge 0.25mg Injection | Vial of 1 Injection | Valid |
| 39403 | Cetrocare 0.25mg Injection | Vial of 1 ml Injection | Valid |
| 41231 | Cetide 0.25mg Injection | Vial of 1 Injection | Valid |
| 43523 | Cetronext 0.25mg Injection | Vial of 1 Injection | Valid |
| 46480 | Cetrosar 0.25mg Injection | Vial of 1 ml Injection | Valid |
| 55541 | Creart 0.25mg Injection | Vial of 1 Injection | Valid |
| 73533 | Eurelix 0.25mg Injection | Vial of 1 Injection | Valid |
| 96301 | Gonapress 0.25mg Injection | Vial of 1 Injection | Valid |
| 163165 | Ovucet 0.25mg Injection | Vial of 1 Injection | Valid |
| 201587 | Sanrox 0.25mg Injection | Vial of 1 ml Injection | Valid |
| 202640 | Setrosil 0.25mg Injection | Vial of 1 Injection | Valid |
| 236604 | Vestova 0.25mg Injection | Vial of 2 ml Injection | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

All 16 registrations are valid single-ingredient injectable products.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hypertrichosis rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no trials or publications, and the mechanistic link is weak. Cetrorelix is well established and widely marketed in India for fertility treatment, but that does not support the predicted new use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source, since safety data are currently missing
- Detailed mechanism of action data
- Any clinical or literature evidence for hypertrichosis, ideally in a hormone-dependent subset
- If a different direction is pursued, a focused review of central precocious puberty, covering short-acting formulation suitability, paediatric safety and comparison with GnRH agonists

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cetrotide (cetrorelix acetate) prescribing information, EMD Serono, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=aca7768e-28a7-4027-b1d8-e66247665f79) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

