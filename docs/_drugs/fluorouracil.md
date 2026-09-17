---
layout: default
title: Fluorouracil
parent: Model Prediction Only (L5)
nav_order: 363
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

# Fluorouracil: From Unrecorded Original Indication to Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina

## One-Sentence Summary

Fluorouracil (DrugBank DB00544) is a long-established fluoropyrimidine antimetabolite; however, no Taiwan license or original-indication data is on file for this record (the product is currently **not marketed**). The TxGNN model's top-ranked prediction is **botryoid-type embryonal rhabdomyosarcoma of the vagina**, but this specific candidate is supported by **zero clinical trials and zero publications** — it rests entirely on the knowledge-graph score, with no direct evidence behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Taiwan license or original-indication data on file |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for Fluorouracil is not available in this evidence pack (flagged as a High-severity data gap). Based on known information, Fluorouracil is a fluoropyrimidine antimetabolite; related entries in this same prediction set describe it as a thymidylate synthase inhibitor that blocks DNA synthesis and is cytotoxic to rapidly dividing cells — a mechanism broadly applicable to high-proliferation malignancies.

The top-ranked candidate here, botryoid-type embryonal rhabdomyosarcoma of the vagina, is a rare pediatric soft-tissue sarcoma subtype. Per the model's own rationale, this prediction "shares a theoretical antimetabolite rationale with the broader rhabdomyosarcoma disease category, but has no clinical trial or literature support — it is a TxGNN knowledge-graph inference score only." In other words, the mechanistic plausibility is inherited at the drug-class level, not established for this specific, rare tumor entity.

It is worth noting that other TxGNN candidates for Fluorouracil in this same evidence pack — general rhabdomyosarcoma (rank 2, L4, 5 supporting publications) and liver sarcoma (rank 7, L3, 5 clinical trials + 20 publications) — carry meaningfully stronger evidence than this rank-1 candidate. Those may warrant separate evaluation as more actionable repurposing leads.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

No registration records found. The `taiwan_regulatory` dataset lists 0 licenses and market status "Not Marketed" — no product registration details are available to summarize.

---

## Cytotoxicity

Fluorouracil is a conventional cytotoxic antineoplastic (fluoropyrimidine antimetabolite class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

**Drug Interactions**: A DDI query returned 361 total recorded interactions. Interactions with a defined severity grade include:
- **Moderate**: Metronidazole, Tinidazole
- **Minor**: Cimetidine, Levofloxacin

The remaining recorded interactions (e.g., Calcitriol, Doxycycline, Clotrimazole, Pantoprazole, Glimepiride, Morphine, Metformin, Omeprazole, Sucralfate, Palonosetron, Rosiglitazone, Lansoprazole, Vancomycin, Atropine, Lactulose, Triamcinolone, and others) are graded "Unknown" in this dataset and require individual review before any clinical use.

Key warnings and contraindications are not available in this evidence pack (flagged as a Blocking-severity data gap) — please refer to the package insert for this information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (botryoid-type embryonal rhabdomyosarcoma of the vagina) has no clinical trial or literature support — it is evidence level L5, model prediction only. Combined with the absence of TFDA safety/labeling data (Blocking gap) and MOA data (High-severity gap), there is insufficient basis to advance this specific candidate.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a Blocking data gap
- Confirmed mechanism-of-action data from DrugBank
- If pursuing repurposing further, consider re-scoping evaluation to the higher-evidence candidates in this same pack: general rhabdomyosarcoma (L4) or liver sarcoma (L3, 5 trials + 20 publications), which have substantially more supporting data than this rank-1 candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

