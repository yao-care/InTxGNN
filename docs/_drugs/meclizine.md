---
layout: default
title: Meclizine
parent: Model Prediction Only (L5)
nav_order: 517
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Meclizine: predicted new indication Allergic urticaria (evidence level L5). Approved use: Central nervous system origin vertigo"
monitor_inn: "Meclizine"
predicted_indications: ["allergic urticaria", "common cold", "nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "cold urticaria"]
---

# Meclizine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Meclizine: From Central Nervous System Vertigo and Motion Sickness to Allergic Urticaria

## One-Sentence Summary

Meclizine is a first-generation antihistamine, originally used to treat vertigo of central nervous system origin and motion sickness.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, but **no clinical trials and no publications** were found to support this direction, so the prediction rests on model output and drug-class reasoning alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Central nervous system origin vertigo; motion sickness (the licence records contain no approved indication text) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, meclizine is a first-generation piperazine H1-antihistamine with anticholinergic activity. Its efficacy in vertigo and motion sickness is established, and mechanistically it may be applicable to histamine-mediated conditions such as urticaria.

H1-antihistamines are the standard first-line therapy for urticaria, so the mechanistic link is plausible. However, this link rests on drug-class knowledge and the TxGNN prediction, not on any meclizine-specific data supplied for this report. Better-characterized antihistamines are already established for this condition, and non-sedating second-generation agents are generally preferred. The incremental value of meclizine is therefore unclear. Its sedation and anticholinergic burden are also relevant.

### Other Predicted Indications

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Common cold | 99.49% | L5 | Possible symptomatic relief only (rhinorrhoea, sneezing); not disease-modifying |
| 3 | Nasal cavity disease | 99.48% | L5 | Term too broad to test; a specific condition must be defined first |
| 4 | Pharyngitis | 99.45% | L5 | No antimicrobial or anti-inflammatory action; at most symptom relief |
| 5 | Acute laryngopharyngitis | 99.37% | L5 | Anticholinergic drying could worsen throat irritation |
| 6 | Cold urticaria | 99.22% | L5 | Most direct mechanistic rationale; flagged as a research question |

---

## India Market Information

Sixteen valid single-ingredient registrations exist and none are cancelled. The records contain no approved indication text. The five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 58351 | Diligan 25 Tablet (Dr Reddy's Laboratories Ltd) | Strip of 15 tablets | Not stated |
| 60901 | Diligan 50mg Tablet (Dr Reddy's Laboratories Ltd) | Strip of 15 tablets | Not stated |
| 30704 | Biozine 25mg/50mg Tablet (Remedial Healthcare) | Strip of 10 tablets | Not stated |
| 94575 | Gladvert 25mg Tablet (Gladstone Pharma India Pvt Ltd) | Strip of 15 tablets | Not stated |
| 135625 | Meclisafe 50mg/5mg Tablet SR (Pfleger Healthcare Pvt Ltd) | Strip of 10 tablets SR | Not stated |

All products are oral tablets, including sustained-release forms.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: benign prostatic hyperplasia, angle-closure (closed-angle) glaucoma, pyloric stenosis, and bladder neck obstruction. These are consistent with the drug's anticholinergic activity.
- **Drug Interactions**: 252 interactions are recorded. Most are Moderate, mainly with other anticholinergic or antispasmodic agents (hyoscyamine, atropine, glycopyrronium, dicyclomine, trospium, clidinium, mepenzolate, methscopolamine), opioids and antidiarrhoeals (morphine, opium, loperamide, eluxadoline), and others such as metoclopramide, nabilone, and eliglustat. Two **Major** interactions are listed: **potassium citrate** and **potassium chloride**.
- **Other**: Sedation and anticholinergic burden are relevant, particularly in combination with the agents above.

Please refer to the package insert for the full warnings and contraindications, as these were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score and class-level pharmacology, with no clinical trials or literature (Evidence Level L5). Established, better-tolerated antihistamines already exist for urticaria, and the package insert safety information was not available.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- A literature search for any meclizine data in allergic, chronic, or physical (including cold) urticaria. Cold urticaria is the best-supported candidate for follow-up.
- A comparison against second-generation antihistamines to determine whether meclizine adds value
- A specific condition definition if "nasal cavity disease" is to be pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

