---
layout: default
title: Hydroquinone
parent: Model Prediction Only (L5)
nav_order: 413
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "Hydroquinone"
predicted_indications: ["seborrheic keratosis", "vulvar inverted follicular keratosis", "exanthem (disease)", "lichen disease"]
description: "Hydroquinone: predicted new indication Seborrheic keratosis (evidence level L5). In India: at least 20 listed products"
---

# Hydroquinone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Hydroquinone: Seborrheic keratosis
{: .text-alpha }

## One-Sentence Summary

Hydroquinone is a topical skin-lightening agent that is widely marketed in India as creams and ointments. The TxGNN model predicts it may be useful for **seborrheic keratosis**, but the supporting evidence is very thin: **0 clinical trials** and **1 publication**, which is an observational study of facial pigmentary disorders rather than of seborrheic keratosis itself.

<!-- review:begin in-lic-20261124c-hydroquinone-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Hydroquinone is a topical skin-lightening agent that is widely marketed in India as single-ingredient creams and ointments." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-hydroquinone-1 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Seborrheic keratosis |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for hydroquinone: "Topical application of hydroquinone produces a reversible depigmentation of the skin by inhibition of the enzymatic oxidation of tyrosine to 3,4-dihydroxyphenylalanine (dopa) (Denton, C. et al., 1952)1 and suppression of other melanocyte metabolic processes (Jimbow, K. et al., 1974)2. Exposure to sunlight or ultraviolet light will cause repigmentation of bleached areas (Parrish, L.A. et al., 1978)3." ([DailyMed: Hydroquinone 4% (hydroquinone) prescribing information, Acella Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=595dfc50-ee6f-41b5-ab5b-4c293aee342b), label version 2026-07-10; accessed 2026-11-19.) Based on general pharmacological knowledge, hydroquinone inhibits tyrosinase, the enzyme that drives melanin synthesis, and it is used topically to lighten hyperpigmented skin.

Seborrheic keratosis is a benign epidermal growth that is often pigmented. Reducing melanin could in theory lighten the lesions, so a mechanistic link is plausible. However, the link is indirect. Seborrheic keratosis is a proliferative lesion, not mainly a disorder of melanin production, so depigmentation would at best change the colour and not treat the growth. The very high TxGNN score is a computational prediction and should not be read as clinical evidence.

Other predictions in the model output are weaker still:
- **Vulvar inverted follicular keratosis** (score 0.9964): no trials or literature; it is usually managed by excision, and applying hydroquinone to vulvar mucosa raises irritation concerns.
- **Exanthem** (0.9942): the only trial concerned an herbal depigmenting system for melasma and does not address exanthems.
- **Lichen disease** (0.9907): hydroquinone might help the leftover pigmentation of pigmented lichenoid disorders, but it would not treat the inflammation. The one case report found benefit from topical tacrolimus, not hydroquinone.

## Clinical Trial Evidence

Currently no related clinical trials are registered for seborrheic keratosis.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Prospective observational cohort | J Plast Reconstr Aesthet Surg | Combination treatment algorithm for facial pigmentary disorders in Asian patients; addresses multiple pigmentary conditions together, not seborrheic keratosis specifically |

## India Market Information

Twenty hydroquinone products hold valid registrations, and none has been cancelled. Approved indication text is not available in the compiled records.

<!-- review:begin in-lic-20261124c-hydroquinone-2 -->

> **Review correction (2026-11-24)**: Originally stated: "Twenty single-ingredient hydroquinone products hold valid registrations, and none has been cancelled." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-hydroquinone-2 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 26784 | Bloomglow Cream | Tube of 20 gm Cream | Valid |
| 34586 | Clear Skin Cream | Tube of 15 gm Cream | Valid |
| 60870 | Dermofade Cream | Tube of 30 gm Cream | Valid |
| 65569 | Dremz Mild Cream | Tube of 20 gm Cream | Valid |
| 73468 | Eubit Cream | Tube of 15 gm Cream | Valid |
| 76990 | Eutret Cream | Tube of 15 gm Cream | Valid |
| 86595 | Femolink Cream | Tube of 20 gm Cream | Valid |
| 104455 | Hypig 15 Cream | Tube of 20 gm Cream | Valid |
| 104758 | Hqn-FT Cream | Tube of 15 gm Cream | Valid |
| 114379 | Justclean Cream | Tube of 20 gm Cream | Valid |
| 128311 | Litetone Cream | Tube of 20 gm Cream | Valid |
| 140389 | Melapex Cream | Tube of 10 gm Cream | Valid |
| 152006 | Nolasma Cream | Tube of 15 gm Cream | Valid |
| 175978 | Pinkquin Cream | Tube of 25 gm Cream | Valid |
| 206300 | Smart Glo Cream | Tube of 15 gm Cream | Valid |
| 216561 | Tintin MH Cream | Tube of 15 gm Cream | Valid |
| 219542 | Tanlite Cream | Tube of 20 gm Cream | Valid |
| 231219 | Ulite Cream | Tube of 30 gm Cream | Valid |
| 244350 | Xtralite Ointment | Tube of 20 gm Ointment | Valid |
| 244397 | Xiar HC Ointment | Tube of 20 gm Ointment | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

The data compiled for this report include no package insert warnings, contraindications or drug interactions. A knowledge-graph screen (not label text) links hydroquinone to the following conditions as potential contraindications:

- **Skin conditions:** sunburn, skin atrophy, atopic eczema, dermatitis
- **Vascular conditions:** telangiectasis, capillary disease, hereditary hemorrhagic telangiectasia, peripheral vascular disease, intermittent vascular claudication, peripheral arterial disease
- **Endocrine conditions:** adrenocortical insufficiency, Addison disease

These are model-derived signals and must be checked against the official package insert. Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score and one indirect observational study, with no clinical trial in seborrheic keratosis. The mechanism (melanin reduction) would not treat the underlying benign growth, so the evidence does not yet justify moving forward.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator, since safety screening cannot start without them
- Detailed mechanism of action data (for example from DrugBank)
- Controlled studies of hydroquinone in seborrheic keratosis, or at least in pigmented keratoses
- Confirmation of the approved indications for the registered products
- A comparison with existing treatments for seborrheic keratosis (cryotherapy, curettage) to define any realistic role, such as a cosmetic lightening adjunct

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Hydroquinone 4% (hydroquinone) prescribing information, Acella Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=595dfc50-ee6f-41b5-ab5b-4c293aee342b) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

