---
layout: default
title: Griseofulvin
parent: Model Prediction Only (L5)
nav_order: 403
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-31
description: "Griseofulvin: predicted new indication Myiasis (evidence level L5). Approved use: Tinea pedis, tinea corporis, tinea unguium, tinea barbae…"
monitor_inn: "Griseofulvin"
predicted_indications: ["myiasis", "wound myiasis", "furuncular myiasis", "creeping myiasis", "echinococcus granulosus infectious disease"]
---

# Griseofulvin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Griseofulvin: From Tinea Infections to Myiasis
{: .text-alpha }

## One-Sentence Summary

Griseofulvin is an oral antifungal originally used to treat dermatophyte infections such as tinea pedis, tinea corporis, tinea unguium and tinea of the scalp or beard.
The TxGNN model predicts it may be effective for **Myiasis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, tinea corporis, tinea unguium, tinea barbae, dermatophytosis of the groin, perianal area, scalp or beard (no approved indication text is recorded in the India licence data; these are taken from the knowledge-graph indication list) |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, griseofulvin is an oral antifungal whose efficacy in dermatophyte infections is well established. It is generally understood to interfere with microtubule function and mitosis in fungal cells, and this could mechanistically be applicable to other organisms, though this has not been verified.

The link to myiasis is speculative. Myiasis is an infestation by fly larvae, and the hypothesis is that disrupting microtubule or tubulin function might affect the larvae. No data support this. Myiasis is normally managed by larval removal, wound care and antiparasitic drugs such as ivermectin, so griseofulvin has no established role.

The four highest-ranked predictions are myiasis subtypes (myiasis, furuncular myiasis, wound myiasis, creeping myiasis). Three of them have exactly the same score (0.9934). This suggests the model is propagating a shared disease-class signal rather than evidence specific to each indication. The fifth prediction, *Echinococcus granulosus* infection (0.9932), has a somewhat more plausible parallel, since albendazole-type drugs also act on parasite tubulin. Even so, griseofulvin's tubulin-binding profile differs, and no preclinical or clinical data were found. Any follow-up would need in vitro protoscolicidal or animal-model data first.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Griseofulvin is marketed in India as oral tablets. The data compiled for this report list 20 valid single-ingredient registrations and no cancelled ones. Approved indication text is not recorded for any of them. Main registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 56342 | Cygrofluvin 125mg Tablet | Strip of 10 tablets | Not recorded |
| Registration No. 85094 | Fungigris OD 500mg Tablet | Strip of 10 tablets | Not recorded |
| Registration No. 108246 | Idifulvin 250mg Tablet | Strip of 10 tablets | Not recorded |
| Registration No. 59713 | Dermonorm 500mg Tablet | Strip of 10 tablets | Not recorded |
| Registration No. 94205 | Grisovin-FP Tablet | Strip of 10 tablets | Not recorded |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** liver failure, porphyria (including inherited porphyria and other porphyrin metabolism disorders), systemic lupus erythematosus (including the paediatric form), substance abuse/dependence, and neutropenia-related conditions (agranulocytosis, neutropenia, cyclic hematopoiesis, severe congenital neutropenia and related syndromes).
- **Drug Interactions:** 234 interactions were identified. Examples include:
  - Moderate: warfarin, apixaban, rivaroxaban, ticagrelor, dicoumarol (anticoagulant and antiplatelet agents); repaglinide, saxagliptin, linagliptin (antidiabetic agents); aprepitant, rolapitant; eliglustat; naloxegol; nitisinone; fostamatinib; macimorelin; artemether, mefloquine, praziquantel.
  - Minor: acetylsalicylic acid, liraglutide.

Please refer to the package insert for label warnings and contraindications, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no clinical trials, no literature and no established mechanistic link. Standard treatments for myiasis already exist, and the identical scores across subtypes suggest a class-level artefact. Griseofulvin also has notable safety flags, including hepatic, porphyria, lupus and neutropenia-related concerns.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap for safety screening)
- Detailed mechanism of action data (MOA)
- Preclinical evidence, such as in vitro larvicidal or protoscolicidal assays or animal models, showing activity against fly larvae or *Echinococcus*
- A rationale for why a systemic antifungal would add value over current standard care (larval removal and ivermectin or albendazole)
- Route compatibility and similarity-to-original analyses, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

