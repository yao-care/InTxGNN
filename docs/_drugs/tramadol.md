---
layout: default
title: Tramadol
parent: Model Prediction Only (L5)
nav_order: 852
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tramadol: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Osteoarthritis, arthropathy"
monitor_inn: "Tramadol"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "juvenile idiopathic arthritis", "juvenile arthritis due to defect in LACC1", "rheumatoid nodulosis", "rheumatoid factor-positive polyarticular juvenile idiopathic arthritis"]
---

# Tramadol
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

# Tramadol: From Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Tramadol is an opioid-type analgesic, and the knowledge graph links it to osteoarthritis and related joint disease.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder.
**No clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoarthritis, arthropathy (from the knowledge graph; no approved indication text is available in the India licence records) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Tramadol is generally understood as an analgesic acting through mu-opioid receptor agonism and serotonin/noradrenaline reuptake inhibition. Its use in osteoarthritis pain is symptomatic relief rather than disease modification.

The predicted disease is a rare genetic skeletal dysplasia caused by a defect in the CDMP1/GDF5 pathway. No mechanistic link to tramadol could be identified. The high score most likely reflects the knowledge graph's proximity between skeletal and joint disease nodes shared with the original osteoarthritis indications, not a real biological connection. At most, tramadol could offer symptomatic pain relief, not treatment of the underlying disorder.

Other top-ranked predictions show the same pattern. Brachyolmia, brachyolmia-amelogenesis imperfecta syndrome, myosclerosis and several juvenile arthritis types have no direct mechanistic link either. Pseudoachondroplasia is the most plausible of the group, because early joint degeneration and chronic pain could make symptomatic analgesia relevant. Even there, no disease-specific evidence exists.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 17540 | Astol 50mg Capsule | Strip of 10 capsules | Not specified |
| 171207 | Opibind P 37.5mg/325mg Tablet | Strip of 10 tablets | Not specified |
| 62032 | Dolosal P 37.5mg/325mg Tablet | Strip of 10 tablets | Not specified |
| 219929 | Tranzex 50mg Injection | Vial of 2 ml injection | Not specified |
| 229909 | Tramrig 50mg Injection | Ampoule of 1 ml injection | Not specified |

All 20 registrations are valid single-ingredient entries (none cancelled). Products are available as oral capsules and tablets, including some tramadol/paracetamol-type strengths, and as injections.

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

