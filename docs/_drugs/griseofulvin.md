---
layout: default
title: Griseofulvin
parent: Model Prediction Only (L5)
nav_order: 399
evidence_level: L5
indication_count: 5
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Griseofulvin: From Dermatophytosis to Myiasis

## One-Sentence Summary

Griseofulvin is a long-established oral antifungal agent used to treat dermatophyte (ringworm) infections of the skin, hair, and nails.
The TxGNN model predicts it may be effective for **Myiasis** (parasitic skin infestation by fly larvae),
but currently only **0 clinical trials** and **1 loosely related, unclassified publication** support this direction — mechanism of action data is also unavailable.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatophytosis (ringworm) — *not captured in evidence pack; TFDA label text unavailable, see Data Gap DG001* |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| India Market Status | Not marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for Griseofulvin is not available in this evidence pack. Based on general pharmacological knowledge, Griseofulvin is a fungistatic antibiotic derived from *Penicillium griseofulvum*; it accumulates in keratin precursor cells and disrupts fungal mitotic spindle formation, making it effective against dermatophyte infections of skin, hair, and nails.

Myiasis is a parasitic skin condition caused by fly larvae infesting living tissue, not a fungal infection. There is no established pharmacological rationale connecting an antimitotic antifungal mechanism to an insect larval infestation — the two conditions share only superficial overlap as "cutaneous/dermatological infestations." The single retrieved publication (a 1970 veterinary review of parasitic skin diseases in dogs and cats) does not provide a specific mechanistic or clinical link between Griseofulvin and myiasis, and its abstract is unavailable for review.

Given the absence of MOA data, the absence of any clinical trials, and only one unclassified, decades-old, non-human veterinary literature reference, this prediction should be treated as a **model-generated hypothesis only**, without independent mechanistic or clinical corroboration at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4098614](https://pubmed.ncbi.nlm.nih.gov/4098614/) | 1970 | Pending classification | The Veterinary Record | General review of parasitic skin diseases in dogs and cats; abstract not available, specific relevance to Griseofulvin/myiasis not yet confirmed |

---

## India Market Information

Griseofulvin currently holds no registrations and is not marketed in this jurisdiction (market status: Not marketed, total licenses: 0). No authorization records are available.

---

## Safety Considerations

- **Drug Interactions**: Griseofulvin has 234 documented drug interactions in the queried database. Notable examples include:

| Interacting Drug | Level |
|---|---|
| Warfarin | Moderate |
| Dicoumarol | Moderate |
| Apixaban | Moderate |
| Rivaroxaban | Moderate |
| Ticagrelor | Moderate |
| Saxagliptin | Moderate |
| Linagliptin | Moderate |
| Repaglinide | Moderate |
| Eliglustat | Moderate |
| Artemether | Moderate |
| Mefloquine | Moderate |
| Naloxegol | Moderate |
| Acetylsalicylic acid | Minor |
| Liraglutide | Minor |

Griseofulvin is a known CYP450 (particularly CYP1A2/3A4) inducer, which is consistent with the multiple "Moderate" interactions seen with anticoagulants (Warfarin, Dicoumarol) and direct oral anticoagulants (Apixaban, Rivaroxaban) — these combinations may require closer monitoring of anticoagulation status.

Key warnings and contraindications from the local product label are not available (TFDA label data gap, see DG001 below) — please refer to the package insert for full safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by the TxGNN model score, with no clinical trials and a single, unclassified, non-human literature reference of uncertain relevance. Combined with a **Blocking** data gap on TFDA safety labeling (warnings/contraindications), this candidate cannot yet pass a basic safety screen (S1), and the drug is not currently marketed in this jurisdiction.

**To proceed, the following is needed:**
- TFDA/product label warnings and contraindications (DG001, Blocking — required before any S1 safety evaluation)
- Confirmed mechanism of action data (DG002, High priority)
- Targeted literature search for any human case reports or pharmacological studies linking Griseofulvin to myiasis or related parasitic skin conditions
- Reassessment of TxGNN rank context (rank 9559 despite high score) to understand relative confidence among other candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

