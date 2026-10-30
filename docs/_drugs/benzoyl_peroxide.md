---
layout: default
title: Benzoyl Peroxide
parent: Model Prediction Only (L5)
nav_order: 100
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
description: "Benzoyl Peroxide: predicted new indication Vulvar inverted follicular keratosis (evidence level L5). Approved use: Acne, atopic eczema, contact dermatitis, seborrheic dermatitis…"
monitor_inn: "Benzoyl peroxide"
predicted_indications: ["vulvar inverted follicular keratosis", "2-hydroxyethyl methacrylate sensitization", "acrodermatitis chronica atrophicans", "acne keloid"]
---

# Benzoyl Peroxide
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

## Benzoyl Peroxide: From Acne and Dermatitis to Vulvar Inverted Follicular Keratosis
{: .text-alpha }

## One-Sentence Summary

Benzoyl peroxide is a topical agent originally used for skin conditions such as acne, seborrheic dermatitis, contact dermatitis and atopic eczema.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**,
but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, atopic eczema, contact dermatitis, seborrheic dermatitis, seborrheic keratosis and related skin conditions (the licence records compiled for this report contain no approved indication text) |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, benzoyl peroxide is a topical agent already used for acne and several inflammatory and keratinocytic skin conditions, including seborrheic keratosis. Mechanistically it may be applicable to vulvar inverted follicular keratosis.

Seborrheic keratosis and inverted follicular keratosis are both benign keratinocytic lesions. Benzoyl peroxide's keratolytic and anti-inflammatory actions could plausibly extend to the new condition. This link is speculative, because no mechanism data, trials or literature support it.

Other predictions for this drug are weaker or raise concerns:
- **2-hydroxyethyl methacrylate sensitization** (score 0.9943): The model may be learning from the contact dermatitis association. Benzoyl peroxide is itself a recognised contact sensitiser and a radical initiator in acrylic and methacrylate polymerisation, so using it here could be counterproductive.
- **Acrodermatitis chronica atrophicans** (score 0.9917): This is a late Borrelia skin infection treated with systemic antibiotics. Topical benzoyl peroxide is unlikely to reach the deep dermal infection.
- **Acne keloid** (score 0.9906): This is the only prediction with any retrieved literature, and that evidence is indirect (see below). It is a plausible research question, since benzoyl peroxide is an established acne treatment.

## Literature Evidence

The only literature retrieved relates to the fourth-ranked prediction (acne keloid), not the lead prediction. It is indirect evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39090034](https://pubmed.ncbi.nlm.nih.gov/39090034/) | 2024 | Review (retrospective chart review) | Dermatology Online Journal | Treatment patterns in 77 Black paediatric patients with acne vulgaris, a population prone to scarring and keloid formation. It does not address acne keloidalis nuchae specifically. |

For the lead prediction (vulvar inverted follicular keratosis), currently no related clinical trials are registered and no related literature is available.

## India Market Information

There are 20 valid single-ingredient registrations, all topical or wash-off products. No approved indication text is available for any of them. Five representative entries are shown.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 37451 | Clindez Soap | Soap, 75 gm | Not stated |
| 191108 | Rosaklen Aqua Gel | Gel, 15 gm tube | Not stated |
| 4582 | Acnox 2.5 Gel | Gel, 20 gm tube | Not stated |
| 3191 | Acnerus Bpo Cream | Cream, 20 gm tube | Not stated |
| 25884 | Benxop Face Wash | Face wash, 50 gm tube | Not stated |

## Safety Considerations

The knowledge graph links benzoyl peroxide to a number of disease contraindications. These come from graph edges, not from label text, and should be verified against the product label. Conditions most relevant to a topical skin product include:
- **Skin and photosensitivity conditions**: photosensitivity disease, exfoliative dermatitis, dermatitis, skin atrophy
- **Vascular skin conditions**: telangiectasis, capillary disease, hereditary hemorrhagic telangiectasia
- **Viral skin lesions**: common wart, anogenital human papillomavirus infection
- **Other graph-listed conditions**: kidney disease, diabetes mellitus, diabetic ketoacidosis, adrenocortical insufficiency, Addison disease, inflammatory bowel disease (including Crohn disease and ulcerative colitis), Clostridium difficile colitis, peripheral vascular disease

Some of these look systemic and may reflect combination products (for example, with clindamycin) rather than benzoyl peroxide alone. Please also refer to the package insert for key warnings and contraindications, as these were not available for this report.

Benzoyl peroxide is a recognised contact sensitiser. This is especially relevant for application on delicate vulvar skin and for the HEMA sensitisation prediction.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication of vulvar inverted follicular keratosis is supported by a high model score only. There are no clinical trials or publications, the mechanism data is missing, and the package insert safety information has not been obtained. The sensitisation potential is also a concern for use on vulvar skin.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (a blocking gap for safety screening)
- Detailed mechanism of action data
- A literature search targeted at inverted follicular keratosis and benzoyl peroxide, including case reports
- A tolerability and sensitisation assessment for vulvar application
- Dermatology expert review of whether the diagnosis is amenable to topical keratolytic therapy
- Acne keloid (acne keloidalis nuchae) could be explored separately as a research question, since it has indirect supporting literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

