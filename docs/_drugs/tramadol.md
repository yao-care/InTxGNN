---
layout: default
title: Tramadol
parent: Model Prediction Only (L5)
nav_order: 852
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Tramadol"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "juvenile idiopathic arthritis", "juvenile arthritis due to defect in LACC1", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis"]
description: "Tramadol: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). In India: at least 20 listed products"
---

# Tramadol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Tramadol: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Tramadol is an opioid-type analgesic, and the TxGNN model (deep learning) may link it to osteoarthritis and related joint disease based on similarities the model learned between related diseases, not biological evidence.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder.
**No clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for tramadol: "Tramadol Hydrochloride Extended-Release Capsules contain tramadol, an opioid agonist, and an inhibitor of reuptake of norepinephrine and serotonin. Although its mode of action is not completely understood, from animal tests, at least two complementary mechanisms appear applicable: binding of parent and M1 metabolite to mu-opioid receptors and weak inhibition of reuptake of norepinephrine and serotonin." ([DailyMed: Tramadol Hydrochloride Extended-Release (tramadol hydrochloride) prescribing information, Trigen Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c0bc7218-3fd0-4646-96f4-25355fc84aa9), label version 2026-01-23; accessed 2026-11-19.) Tramadol is generally understood as an analgesic acting through mu-opioid receptor agonism and serotonin/noradrenaline reuptake inhibition. Its use in osteoarthritis pain is symptomatic relief rather than disease modification.

The predicted disease is a rare genetic skeletal dysplasia caused by a defect in the CDMP1/GDF5 pathway. No mechanistic link to tramadol could be identified. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. At most, tramadol could offer symptomatic pain relief, not treatment of the underlying disorder.

Other top-ranked predictions show the same pattern. Brachyolmia, brachyolmia-amelogenesis imperfecta syndrome, myosclerosis and several juvenile arthritis types have no direct mechanistic link either. Pseudoachondroplasia is the most plausible of the group, because early joint degeneration and chronic pain could make symptomatic analgesia relevant. Even there, no disease-specific evidence exists.

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 17540 | Astol 50mg Capsule | Strip of 10 capsules | Valid |
| 29311 | Brisdol Plus 37.5mg/325mg Tablet | Strip of 10 tablets | Valid |
| 31316 | Bestodol 50mg Injection | Vial of 1 ml Injection | Valid |
| 62032 | Dolosal P 37.5mg/325mg Tablet | Strip of 10 tablets | Valid |
| 63718 | Dolfen-P 50mg/500mg Tablet | Strip of 10 tablets | Valid |
| 93758 | Famatos Injection | Ampoule of 2 ml Injection | Valid |
| 101297 | Gdolovoid Tablet | Strip of 10 tablets | Valid |
| 167014 | OC Dol 50mg Tablet | Strip of 10 tablets | Valid |
| 171207 | Opibind P 37.5mg/325mg Tablet | Strip of 10 tablets | Valid |
| 171386 | Ozitram 50mg/500mg Tablet | Strip of 10 tablets | Valid |
| 213538 | Smdol 50mg Injection | Vial of 2 ml Injection | Valid |
| 219929 | Tranzex 50mg Injection | Vial of 2 ml Injection | Valid |
| 223817 | Tramplas P Tablet | Strip of 10 tablets | Valid |
| 224197 | Trick-T Tablet | Strip of 10 tablets | Valid |
| 226410 | Traflam-P Tablet | Strip of 10 tablets | Valid |
| 227690 | T Dol 50mg Injection | Vial of 1 ml Injection | Valid |
| 228641 | Termeg 60mg Tablet | Strip of 10 tablets | Valid |
| 229710 | Tramakan 100mg Injection | Vial of 1 Injection | Valid |
| 229909 | Tramrig 50mg Injection | Ampoule of 1 ml Injection | Valid |
| 232522 | Ultrafine 37.5mg/325mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

All 20 registrations are valid entries (none cancelled). Products are available as oral capsules and tablets, including some tramadol/paracetamol-type strengths, and as injections.

<!-- review:begin in-lic-20261124-tramadol-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All 20 registrations are valid single-ingredient entries (none cancelled)." Removed: it described the products as single-ingredient (or as having no combination products), which does not match the Indian medicine data (the Indian Medicine Dataset): some of the recorded products are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124-tramadol-1 -->

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text): hypertension, liver failure, liver disease, cirrhosis, epilepsy, respiratory failure, serotonin syndrome, paracetamol poisoning, substance abuse/dependence, alcohol withdrawal, diabetic ketoacidosis, anxiety and dysthymic disorders, hyperlipidemia, pseudotumor cerebri/intracranial hypertension, and central nervous system infections.
- **Drug Interactions**: 321 interactions were recorded. Major-level examples include alvimopan, bupropion, cisapride, dexfenfluramine, diethylpropion, dolasetron, dronabinol, ephedrine and fenfluramine. Moderate-level examples include atropine, bisacodyl, cimetidine, clarithromycin, famotidine and several anticholinergics.
- **Paediatric use**: several predicted indications are juvenile arthritis types. Opioid use in children raises concerns such as CYP2D6 ultra-rapid metabolism and respiratory depression.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5), with no clinical trials or relevant literature. The disease is a rare genetic skeletal disorder that tramadol's pharmacology does not address. The one literature item found for another predicted indication (juvenile idiopathic arthritis) concerns ketoprofen, not tramadol.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator, which are currently missing and block safety screening
- Detailed mechanism of action data
- Evidence of any disease-specific pain benefit, if symptomatic analgesia is the intended goal, with a clearly defined target population
- A review of whether another predicted indication with a more plausible pain-related rationale, such as pseudoachondroplasia, would be a better candidate

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Tramadol Hydrochloride Extended-Release (tramadol hydrochloride) prescribing information, Trigen Laboratories, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c0bc7218-3fd0-4646-96f4-25355fc84aa9) |
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

