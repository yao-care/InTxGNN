---
layout: default
title: Griseofulvin
parent: Model Prediction Only (L5)
nav_order: 403
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
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

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for griseofulvin: "The mechanism of griseofulvin consists of binding microtubular proteins, which are required for mitosis. […] The mechanism of griseofulvin consists of binding microtubular proteins, which are required for mitosis. Activity In Vivo Griseofulvin may be active against most strains of the following dermatophytes as described in the INDICATIONS AND USAGE section: Epidermophyton floccosum, Microsporum audouinii, Microsporum canis, Microsporum gypseum, Trichophyton crateriformis, Trichophyton gallinae, Trichophyton interdigitalis, Trichophyton megnini, Trichophyton mentagrophytes, Trichophyton rubrum, Trichophyton sulphureum, Trichophyton schoenleini, Trichophyton tonsurans and Trichophyton verrucosum." ([DailyMed: griseofulvin prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98829d90-b289-4bec-a625-7af412a5cb2d), label version 2025-05-14; accessed 2026-11-19.) Based on known information, griseofulvin is an oral antifungal whose efficacy in dermatophyte infections is well established. It is generally understood to interfere with microtubule function and mitosis in fungal cells, and this could mechanistically be applicable to other organisms, though this has not been verified.

The link to myiasis is speculative. Myiasis is an infestation by fly larvae, and the hypothesis is that disrupting microtubule or tubulin function might affect the larvae. No data support this. Myiasis is normally managed by larval removal, wound care and antiparasitic drugs such as ivermectin, so griseofulvin has no established role.

The four highest-ranked predictions are myiasis subtypes (myiasis, furuncular myiasis, wound myiasis, creeping myiasis). Three of them have exactly the same score (0.9934). This suggests the model is propagating a shared disease-class signal rather than evidence specific to each indication. The fifth prediction, *Echinococcus granulosus* infection (0.9932), has a somewhat more plausible parallel, since albendazole-type drugs also act on parasite tubulin. Even so, griseofulvin's tubulin-binding profile differs, and no preclinical or clinical data were found. Any follow-up would need in vitro protoscolicidal or animal-model data first.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Griseofulvin is marketed in India as oral tablets. The data compiled for this report list 20 valid single-ingredient registrations and no cancelled ones. Approved indication text is not recorded for any of them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 12956 | Alfulvin 250mg Tablet | Strip of 10 tablets | Valid |
| 56342 | Cygrofluvin 125mg Tablet | Strip of 10 tablets | Valid |
| 59713 | Dermonorm 500mg Tablet | Strip of 10 tablets | Valid |
| 85094 | Fungigris OD 500mg Tablet | Strip of 10 tablets | Valid |
| 85528 | Fulvinem 500mg Tablet | Strip of 10 tablets | Valid |
| 94205 | Grisovin-FP Tablet | Strip of 10 tablets | Valid |
| 94284 | Griseofulvin FP 250mg Tablet | Strip of 10 tablets | Valid |
| 94536 | Grisolab 250mg Tablet | Strip of 10 tablets | Valid |
| 94993 | Geovin 250mg Tablet | Strip of 10 tablets | Valid |
| 95384 | Grisactin Forte 250mg Tablet | Strip of 10 tablets | Valid |
| 95550 | Griseoderm 250mg Tablet | Strip of 10 tablets | Valid |
| 95900 | Griscare 500 Tablet | Strip of 10 tablets | Valid |
| 96767 | Griderm 250mg Tablet | Strip of 10 tablets | Valid |
| 97351 | Gresotiv 500mg Tablet | Strip of 10 tablets | Valid |
| 98623 | Grisgeo 250mg Tablet | Strip of 10 tablets | Valid |
| 103600 | Griderm 125mg Tablet | Strip of 10 tablets | Valid |
| 108246 | Idifulvin 250mg Tablet | Strip of 10 tablets | Valid |
| 109762 | Idifulvin 125mg Tablet | Strip of 10 tablets | Valid |
| 152879 | Nufulvin 250mg Tablet | Strip of 10 tablets | Valid |
| 221656 | Tineavin 250mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: griseofulvin prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98829d90-b289-4bec-a625-7af412a5cb2d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

