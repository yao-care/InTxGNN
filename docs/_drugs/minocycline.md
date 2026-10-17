---
layout: default
title: Minocycline
parent: Model Prediction Only (L5)
nav_order: 556
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Minocycline: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Urinary tract infection, bronchitis, acne, anthrax infection…"
monitor_inn: "Minocycline"
predicted_indications: ["exposure keratitis"]
---

# Minocycline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Minocycline: From Bacterial Infections and Acne to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Minocycline is a tetracycline-class antibiotic originally used for infections such as urinary tract infection, bronchitis, gonorrhea and periodontitis, and for acne.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection, bronchitis, acne, anthrax infection, periodontitis, gonorrhea and other bacterial infections (the approved indication text in the India license records is blank, so these indications come from the knowledge graph) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, minocycline is part of the tetracycline class of antibiotics. Its efficacy in bacterial infections and acne is established, and mechanistically it may be applicable to punctate epithelial keratoconjunctivitis.

A plausible, but unverified, rationale is that minocycline has anti-inflammatory and matrix metalloproteinase (MMP)-inhibiting activity. These properties are relevant to ocular surface inflammation, and tetracycline-class drugs are already used in ocular surface conditions such as meibomian gland dysfunction and blepharitis. This link comes from general pharmacology, not from the data compiled for this report.

The second-ranked prediction, **exposure keratitis** (score 99.20%), has a similar but weaker rationale. Exposure keratitis is mainly caused by incomplete eyelid closure and corneal drying, so an antibiotic would be at best an adjunct, and the predicted benefit is uncertain. Neither prediction has supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 140812 | Minop 100 Tablet | Strip of 10 tablets | Not specified |
| 108379 | Iminza 100mg Injection | Vial of 1 injection | Not specified |
| 134417 | Minolox 100 Tablet | Strip of 10 tablets | Not specified |
| 136201 | Minym 45mg Tablet ER | Strip of 10 extended-release tablets | Not specified |
| 59251 | Divaine 50 Tablet | Strip of 10 tablets | Not specified |

There are 20 valid single-ingredient registrations in total, covering oral tablets, extended-release tablets, capsules and injectable (vial) forms. No topical ophthalmic formulation appears among them.

## Cytotoxicity

Not applicable (not an antineoplastic drug), so this section is omitted.

## Safety Considerations

- **Contraindications / disease associations (from the knowledge graph, not label text)**: kidney disease, pyoureter, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, pseudotumor cerebri, intracranial hypertension, dyskinesia of esophagus.
- **Drug Interactions**: 272 interactions were identified in total. The main ones from the sample reviewed:
  - **Major**: isotretinoin, acitretin (a recognized concern is the risk of raised intracranial pressure when tetracyclines are combined with retinoids).
  - **Moderate**: ethinylestradiol, amoxicillin, ampicillin, sodium citrate, calcium acetate, calcium phosphate, bismuth subcitrate potassium, balsalazide, cannabidiol, aminolevulinic acid (topical), brentuximab vedotin, and asparaginase products.
  - **Minor**: acetazolamide, hydrochlorothiazide, amiloride, bumetanide.

Package insert warnings and contraindications were not available, so please refer to the package insert for the authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score (Evidence Level L5), with no clinical trials or publications for either punctate epithelial keratoconjunctivitis or exposure keratitis. Package insert safety data are also missing, which blocks progression to safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap)
- Detailed mechanism of action data (e.g., from DrugBank)
- A literature and trial search for tetracycline-class or minocycline use in punctate epithelial keratoconjunctivitis and other ocular surface disease
- Assessment of route compatibility, since all marketed forms are oral or injectable and a topical ophthalmic route would likely be needed
- Preclinical or early-phase evidence of benefit before reconsidering the decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

