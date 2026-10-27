---
layout: default
title: Ammonium Chloride
parent: Model Prediction Only (L5)
nav_order: 54
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Ammonium Chloride: predicted new indication Acute laryngopharyngitis (evidence level L5). Approved use: Pharyngitis, common cold, nasopharyngitis"
monitor_inn: "Ammonium chloride"
predicted_indications: ["acute laryngopharyngitis", "nasal cavity disease"]
---

# Ammonium Chloride
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

## Ammonium Chloride: From Pharyngitis / Common Cold to Acute Laryngopharyngitis
{: .text-alpha }

## One-Sentence Summary

Ammonium chloride is a long-established expectorant ingredient, originally used for upper respiratory conditions such as pharyngitis, common cold and nasopharyngitis.
The TxGNN model predicts it may be effective for **acute laryngopharyngitis**,
but at present there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pharyngitis, common cold, nasopharyngitis (from the knowledge graph; the approved indication text on Indian licences is blank) |
| Predicted New Indication | Acute laryngopharyngitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ammonium chloride is an expectorant ingredient used in cough and cold syrups, and it is already linked to pharyngitis, common cold and nasopharyngitis. Mechanistically it may be applicable to acute laryngopharyngitis, but this has not been verified.

Acute laryngopharyngitis sits right next to the drug's existing indications. Both involve inflammation of the upper airway, and the throat and larynx are anatomically adjacent to the pharynx. Expectorants are traditionally thought to loosen secretions in the upper airway, which could plausibly help here.

The very high score most likely reflects how close this disease sits to existing indications in the knowledge graph, rather than independent evidence. It should be treated as a hypothesis only.

A second prediction, **nasal cavity disease** (score 99.94%, also evidence level L5), is a very broad category. It has no supporting trials or literature, and it would need to be narrowed to a specific condition, such as rhinitis or sinusitis, before it could be tested.

## India Market Information

All 20 registrations are single-ingredient entries listed as valid. The approved indication text is blank in the data compiled for this report. Five examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 152200 | Nocof Syrup | Bottle of 100 ml syrup | Not stated |
| 249589 | Zumcof DX Syrup | Bottle of 100 ml syrup | Not stated |
| 35576 | Cofdex Plus Syrup Sweet Orange | Bottle of 100 ml syrup | Not stated |
| 29960 | Becodryl Syrup | Bottle of 60 ml syrup | Not stated |
| 12881 | Adyl Expectorant | Bottle of 110 ml expectorant | Not stated |

## Safety Considerations

Package insert warnings and contraindications were not available. Please refer to the package insert for safety information.

- **Contraindication-related conditions (knowledge graph, not label text)**: The graph links ammonium chloride to conditions including liver failure, impaired renal function, anuria, hypertension, epilepsy, adrenocortical insufficiency, peptic ulcer disease, pulmonary edema, myocardial ischemia and coronary artery disease. This list is long (30 conditions) and should be confirmed against official labelling.
- **Drug Interactions**: 21 interactions were identified.
  - Moderate: amphetamine, benzphetamine, dextroamphetamine, lisdexamfetamine, metamfetamine.
  - Minor: ephedrine, pseudoephedrine, tricyclic antidepressants (amitriptyline, clomipramine, desipramine, doxepin, imipramine, nortriptyline, protriptyline, trimipramine), methadone, mexiletine, flecainide.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no clinical trials, no publications and no mechanism data. Evidence is at level L5 (model prediction only), and the safety data is incomplete.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank)
- Package insert warnings and contraindications from the Indian regulator's records, and the approved indications for each registration
- A literature and trial search specific to acute laryngopharyngitis
- A review of the knowledge-graph contraindications, especially renal, hepatic and cardiovascular conditions
- A clearer definition of the target condition and route of administration before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

