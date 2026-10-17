---
layout: default
title: Climbazole
parent: Model Prediction Only (L5)
nav_order: 193
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Climbazole: predicted new indication Acne keloid (evidence level L5). Approved use: Seborrheic dermatitis, seborrheic keratosis"
monitor_inn: "Climbazole"
predicted_indications: ["acne keloid", "amyopathic dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "neonatal dermatomyositis", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial", "vulvar inverted follicular keratosis", "dermatitis, atopic", "newborn respiratory distress syndrome"]
---

# Climbazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Climbazole: From Seborrheic Dermatitis to Acne Keloid

## One-Sentence Summary

Climbazole is a topical azole antifungal, originally used for seborrheic dermatitis and dandruff-type scalp conditions.
The TxGNN model's top-ranked prediction is **Acne Keloid**, but it has **no clinical trials and no publications** behind it, so it rests on model prediction alone.
The most evidence-supported direction is **dermatitis** (**14 publications**, but largely about seborrheic dermatitis, the already approved use), so it is not true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Seborrheic dermatitis, seborrheic keratosis (the licence records contain no approved indication text) |
| Predicted New Indication | Acne keloid |
| TxGNN Prediction Score | 95.32% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, climbazole is a topical azole antifungal that is thought to inhibit ergosterol synthesis (CYP51, fungal C14-demethylase). Its efficacy against *Malassezia* yeasts in seborrheic dermatitis and dandruff is established, and mechanistically it might be applicable to other skin conditions with a fungal contribution.

Acne keloid (folliculitis keloidalis) is an inflammatory follicular condition that may have a *Malassezia* or bacterial contribution. However, no study supports this link for climbazole, and the TxGNN score likely reflects shared skin-disease associations in the knowledge graph rather than a demonstrated mechanism.

Other high-scoring predictions look even weaker. Amyopathic and neonatal dermatomyositis, childhood interstitial lung disease, newborn respiratory distress syndrome, and acrodermatitis chronica atrophicans have no plausible link to a topical antifungal. Two predictions are worth noting:
- **Dermatitis (rank 3, 95.05%)**: this has the only literature support, but it mostly concerns seborrheic dermatitis, which is already an approved use.
- **Atopic dermatitis (rank 9, 89.63%)**: *Malassezia* is implicated in the head and neck subtype, which gives a plausible antifungal rationale, but no climbazole-specific evidence was found.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (acne keloid) or for the other nine predicted indications.

## Literature Evidence

The top-ranked prediction (acne keloid) has no related literature. The table below covers the **dermatitis** prediction (rank 3), the only one with publications. Most of these studies concern seborrheic dermatitis and dandruff, the existing indication.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27904273](https://pubmed.ncbi.nlm.nih.gov/27904273/) | 2016 | Open-label split-face clinical study | Annals of Dermatology | Climbazole/piroctone olamine cream for facial seborrheic dermatitis; *Malassezia* is central to pathogenesis |
| [11534318](https://pubmed.ncbi.nlm.nih.gov/11534318/) | 2001 | Clinical study | Praxis | 0.65% climbazole shampoo over 4 weeks in 30 volunteers with moderate to severe scalp seborrheic dermatitis; effectiveness and tolerance assessed |
| [21272039](https://pubmed.ncbi.nlm.nih.gov/21272039/) | 2011 | Comparative efficacy study | Int J Cosmet Sci | Piroctone olamine 0.5%/climbazole 0.45% shampoo compared with 1% zinc pyrithione shampoo in moderate to severe dandruff |
| [31190937](https://pubmed.ncbi.nlm.nih.gov/31190937/) | 2019 | Prospective, assessor-blinded study | Clin Cosmet Investig Dermatol | Combination cream (hyaluronic acid, glycoprotein, glycyrretinic acid, piroctone olamine, climbazole) in 75 subjects with facial seborrheic dermatitis; climbazole's individual contribution is unclear |
| [25854670](https://pubmed.ncbi.nlm.nih.gov/25854670/) | 2015 | Case series (30 cases) | G Ital Dermatol Venereol | New topical combination for treatment and prevention of paronychia |
| [38331330](https://pubmed.ncbi.nlm.nih.gov/38331330/) | 2024 | Formulation development | Int J Pharm | Skin permeation of climbazole from topical formulations for dandruff |
| [38544350](https://pubmed.ncbi.nlm.nih.gov/38544350/) | 2024 | In vitro | J Cosmet Dermatol | Novel shampoo formulations tested against *Malassezia*; azole resistance is an emerging concern |
| [41194006](https://pubmed.ncbi.nlm.nih.gov/41194006/) | 2025 | Preclinical | BMC Microbiology | Enzymatic approach for targeted fungal growth inhibition in dandruff |
| [26083147](https://pubmed.ncbi.nlm.nih.gov/26083147/) | 2015 | Pilot study (veterinary) | Vet Dermatol | Wipes with chlorhexidine, climbazole and Tris-EDTA to reduce *Malassezia pachydermatis* on canine skin |
| [12858225](https://pubmed.ncbi.nlm.nih.gov/12858225/) | 2003 | Method study | J Cosmet Sci | Hair strand test for the antifungal effects of antidandruff preparations |

The remaining retrieved papers (scalp deposition, follicular delivery and imaging methods, and an ecotoxicity study) are not clinically relevant to repurposing.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 134358 | Medkin AD Shampoo | Shampoo, bottle of 200 ml | Not stated in licence record |
| 34828 | Ciola Shampoo | Shampoo, bottle of 100 ml | Not stated in licence record |
| 108105 | Itrakil Shampoo Anti Dandruff | Shampoo, bottle of 100 ml | Not stated in licence record |

All three registrations are valid single-ingredient products, and all are shampoos.

## Safety Considerations

Please refer to the package insert for safety information.

Points from the prediction review to keep in mind:
- No drug interaction records were found.
- Azoles may cause barrier disruption or sensitization on inflamed skin, relevant if atopic dermatitis is pursued.
- Safety in neonates has not been established, which matters for the neonatal predictions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, acne keloid, is supported only by a model score, with no trials, no literature and no established mechanism. The literature that does exist supports seborrheic dermatitis, which is already the approved use, so it does not demonstrate new repurposing value.

**To proceed, the following is needed:**
- Mechanism of action data for climbazole (for example from DrugBank) to assess mechanistic links
- Package insert warnings and contraindications for the marketed shampoos, which are currently missing and block safety screening
- Approved indication text for the three Indian registrations
- A focused literature and case review for acne keloid, and for atopic dermatitis (head and neck subtype) as the more plausible lead
- Confirmation of the design and controls of the seborrheic dermatitis studies before they are used to support any dermatitis claim
- Assessment of route compatibility, since current products are wash-off shampoos and the predicted conditions may need leave-on formulations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

