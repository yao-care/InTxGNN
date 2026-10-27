---
layout: default
title: Sodium Citrate
parent: Model Prediction Only (L5)
nav_order: 778
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Sodium Citrate: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Peptic ulcer disease, gastroesophageal reflux disease, esophagitis…"
monitor_inn: "Sodium citrate"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "acute laryngopharyngitis", "stomach disease", "postgastrectomy syndrome", "gastroduodenitis", "familial visceral myopathy", "rosacea conjunctivitis", "allergic urticaria"]
---

# Sodium Citrate
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

## Sodium Citrate: From Peptic Ulcer Disease and Reflux to Papillary Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Sodium citrate is a buffering (antacid) agent, originally associated with acid-related upper gastrointestinal and upper respiratory conditions such as peptic ulcer disease, gastroesophageal reflux disease, dyspepsia and the common cold.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**, but there are **no clinical trials and no publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastroesophageal reflux disease, esophagitis, dyspepsia, pharyngitis, common cold, rhinitis, nasopharyngitis (from the knowledge graph; the Indian product labels list no approved indication text) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, sodium citrate is a buffering agent and antacid. Its use in acid-related gastrointestinal conditions is biologically consistent, and its listed upper respiratory indications may relate to the predicted indication through related tissue and disease categories.

The link to papillary conjunctivitis is speculative. One plausible but unsupported idea is a buffering or mild antiallergic effect on the ocular surface. The high score most likely reflects graph proximity to other conjunctivitis and upper respiratory disease nodes in the knowledge graph, not demonstrated clinical benefit.

Other predictions for this drug show the same pattern. These include nasal cavity disease, acute laryngopharyngitis, stomach disease, postgastrectomy syndrome, gastroduodenitis, familial visceral myopathy, rosacea conjunctivitis and allergic urticaria. Only stomach disease and gastroduodenitis have any retrieved literature, and that literature is indirect. For example, the stomach disease results are mostly preclinical gastric cancer studies that combine sodium citrate with 3-bromopyruvate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 201195 | Serocit 46.7% Injection | Vial of 1 injection | Not stated |
| 36112 | Cool Syrup | Bottle of 200 ml syrup | Not stated |

---

## Safety Considerations

- **Drug Interactions**: 114 interactions were identified in total. The main ones are:
  - **Major**: Aluminum hydroxide.
  - **Moderate**: Doxycycline, minocycline, tetracycline, levofloxacin, acetylsalicylic acid, iron, rosuvastatin, acalabrutinib, ephedrine and pseudoephedrine.
  - **Minor**: Sulfonylureas (acetohexamide, chlorpropamide, glipizide, glyburide, tolazamide, tolbutamide), lactulose and misoprostol.
- **Disease-level cautions from the knowledge graph** (these are not label text): hypertension, pancreatitis, adrenal insufficiency (including Addison disease), benign prostatic hyperplasia, anuria, impaired renal function, rhabdomyolysis, hypercalcemia, nephrocalcinosis, coronary artery disease and myocardial infarction, metabolic acidosis, and angle-closure glaucoma or ocular hypertension.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based score. No trials or publications were found, and there is no mechanism of action data. Both marketed Indian products are for non-ocular use (an injection and an oral syrup), and the available route compatibility has not been assessed.

**To proceed, the following is needed:**
- Mechanism of action data for sodium citrate.
- Package insert warnings and contraindications for the two Indian products.
- A targeted literature search on citrate buffers or citrate-containing preparations in ocular surface disease and allergic conjunctivitis.
- An assessment of whether a suitable ophthalmic formulation and route exist.
- Preclinical or early clinical data showing a benefit in papillary conjunctivitis.
- A review of whether another predicted indication with indirect gastrointestinal support, such as gastroduodenitis, would be a better candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

