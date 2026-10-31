---
layout: default
title: Hydroquinone
parent: Model Prediction Only (L5)
nav_order: 413
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "Hydroquinone"
predicted_indications: ["seborrheic keratosis", "vulvar inverted follicular keratosis", "exanthem (disease)", "lichen disease"]
description: "Hydroquinone: predicted new indication Seborrheic keratosis (evidence level L5). Approved use: Not recorded in the local data"
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

Hydroquinone is a topical skin-lightening agent that is widely marketed in India as single-ingredient creams and ointments. The TxGNN model predicts it may be useful for **seborrheic keratosis**, but the supporting evidence is very thin: **0 clinical trials** and **1 publication**, which is an observational study of facial pigmentary disorders rather than of seborrheic keratosis itself.

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

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, hydroquinone inhibits tyrosinase, the enzyme that drives melanin synthesis, and it is used topically to lighten hyperpigmented skin.

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

Twenty single-ingredient hydroquinone products hold valid registrations, and none has been cancelled. Approved indication text is not available in the compiled records. The main registrations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 244397 | Xiar HC Ointment | Tube of 20 g ointment | Not available |
| 206300 | Smart Glo Cream | Tube of 15 g cream | Not available |
| 152006 | Nolasma Cream | Tube of 15 g cream | Not available |
| 128311 | Litetone Cream | Tube of 20 g cream | Not available |
| 114379 | Justclean Cream | Tube of 20 g cream | Not available |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

