---
layout: default
title: Ferrous Fumarate
parent: Model Prediction Only (L5)
nav_order: 350
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Ferrous Fumarate: predicted new indication Non-syndromic esophageal malformation (evidence level L5). Approved use: Iron deficiency anemia and related anemias (folic acid deficiency ane…"
monitor_inn: "Ferrous fumarate"
predicted_indications: ["non-syndromic esophageal malformation"]
---

# Ferrous Fumarate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Ferrous Fumarate: From Iron Deficiency Anemia to Non-Syndromic Esophageal Malformation

## One-Sentence Summary

Ferrous fumarate is an oral iron salt, originally used to treat iron deficiency anemia and related anemias.
The TxGNN model predicts it may be effective for **non-syndromic esophageal malformation**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency anemia and related anemias (folic acid deficiency anemia, anemia of prematurity, hypochromic anemia, microcytic anemia, deficiency anemia); acne is also listed in the knowledge graph. The India license record contains no approved indication text. |
| Predicted New Indication | Non-syndromic esophageal malformation |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ferrous fumarate is an oral iron salt used to replenish iron stores in iron deficiency anemias. Its efficacy in anemia is well established, but no mechanistic route to the predicted indication has been identified.

Non-syndromic esophageal malformations (for example esophageal atresia or tracheoesophageal fistula) are congenital structural defects arising from abnormal embryonic foregut development. Iron supplementation is not known to correct or treat such defects.

The very high TxGNN score (99.49%) is a knowledge-graph prediction only. It most likely reflects network proximity or shared gene/pathway associations rather than a pharmacologically plausible effect. Oral iron can also irritate the esophagus and gastrointestinal tract, which argues against benefit in a structurally abnormal esophagus. This prediction should therefore be treated with considerable caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 151094 | New CoeHB Plus Tablet (Koye Pharmaceuticals Pvt Ltd) | Strip of 10 tablets (oral) | Not stated in the license record |

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text)**: The following conditions are linked to ferrous fumarate as contraindications in the knowledge graph:
  - Iron overload and metabolism: hereditary hemochromatosis, hemosiderosis, iron metabolism disease, Wilson disease
  - Blood disorders: sickle cell anemia, hereditary persistence of fetal hemoglobin
  - Porphyrias: inherited porphyria, porphyrin metabolism disease, porphyria
  - Gastrointestinal, liver and kidney: peptic ulcer disease, liver disease, gallbladder disease, kidney disease, pyoureter
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hyperparathyroidism, osteitis fibrosa, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, potassium deficiency disease, primary hyperoxaluria
  - Cardiovascular and psychiatric: hypertension and hypertensive disorder, anxiety disorder, neurotic disorder, dysthymic disorder
  - Other: sarcoidosis

  These associations have not been verified against the package insert.

- **Drug Interactions**: 80 interactions were identified in total. The main ones are:
  - Moderate:
    - Proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole), which reduce gastric acidity and iron absorption
    - Tetracycline-class antibiotics (tetracycline, doxycycline, minocycline) and levofloxacin
    - Antacids and minerals (calcium carbonate, magnesium oxide, aluminum hydroxide, magaldrate, sodium sulfate)
    - Pancrelipase and triethylenetetramine
  - Minor: cimetidine, zinc sulfate, zinc acetate

Package insert warnings and contraindications are not available, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (Evidence Level L5), and no plausible mechanistic link between iron supplementation and a congenital esophageal structural defect was identified. The high model score alone does not justify advancing, and oral iron may irritate the esophagus.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma source (a blocking gap for safety screening)
- Mechanism of action data for ferrous fumarate (e.g., from DrugBank)
- Any preclinical or clinical evidence linking iron-related pathways to esophageal development
- A route-compatibility assessment for the predicted indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

