---
layout: default
title: Dextromethorphan
parent: Model Prediction Only (L5)
nav_order: 257
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Dextromethorphan: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Dextromethorphan"
predicted_indications: ["acute laryngopharyngitis", "faucial diphtheria", "trigeminal autonomic cephalalgia", "cervical disc degenerative disorder", "allergic urticaria"]
---

# Dextromethorphan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Dextromethorphan: From Upper Respiratory Conditions (Rhinitis, Common Cold, Pharyngitis) to Nasal Cavity Disease

## One-Sentence Summary

Dextromethorphan is a centrally acting cough suppressant, originally used for upper respiratory conditions such as allergic rhinitis, the common cold and pharyngitis.
The TxGNN model predicts it may be effective for **nasal cavity disease**,
but **no clinical trials and no publications** were found to support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis, headache disorder (from the knowledge graph; the India licence records contain no indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data were not available in the data compiled for this report. Dextromethorphan is generally known as a centrally acting antitussive that acts as a sigma-1 agonist and NMDA receptor antagonist. It has no established direct effect on the nasal mucosa.

The predicted indication, nasal cavity disease, is a broad category that overlaps with the drug's existing upper respiratory indications (allergic rhinitis, vasomotor rhinitis, rhinitis, nasopharyngitis). The prediction most likely reflects closeness to these terms in the knowledge graph rather than a distinct pharmacological mechanism.

This should therefore be read as a graph-based association, not as a mechanistically supported new use.

### Other Predicted Indications (for reference)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Acute laryngopharyngitis | 99.98% | L5 | Close to existing labelled uses; cough suppression may give symptomatic relief only. Largely an extension of current use. |
| 3 | Faucial diphtheria | 99.36% | L5 | No plausible mechanism against the infection or its toxin; at most symptomatic cough relief. |
| 4 | Trigeminal autonomic cephalalgia | 99.32% | L5 | Weak, speculative link via NMDA antagonism and headache. Safety would need review given the many recorded interactions. |
| 5 | Cervical disc degenerative disorder | 99.30% | L5 | Speculative link via NMDA antagonism and neuropathic pain pathways; would not address the structural pathology. |
| 6 | Allergic urticaria | 99.25% | L5 | No antihistaminic or mast-cell-stabilising action; likely a graph artifact. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Dextromethorphan is marketed in India with 20 valid single-ingredient registrations and no cancelled ones. Indication text is not recorded in the licence data. Five of the main registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 203717 | Stopper SF Syrup | Syrup, 100 ml bottle | Not recorded |
| 40361 | Corituss Syrup | Syrup, 100 ml bottle | Not recorded |
| 46599 | Cozia Tablet | Tablet, strip of 10 | Not recorded |
| 94831 | Glycodin Syrup | Syrup, 100 ml bottle | Not recorded |
| 225580 | Tixy Soft 10 mg/100 mg Capsule | Capsule, strip of 4 | Not recorded |

Available dosage forms are oral syrups, tablets and capsules.

## Safety Considerations

- **Drug Interactions**: 306 interactions are recorded in total. The major ones involve serotonergic agents and 5-HT3 antagonists: dexfenfluramine, fenfluramine, lorcaserin, sibutramine, dolasetron, granisetron, ondansetron and palonosetron. Moderate interactions include bupropion, morphine, cimetidine, dronabinol, eliglustat, metoclopramide, nabilone, opium, phentermine, mazindol and glycerol phenylbutyrate.
- **Knowledge-graph contraindication associations** (not label text): hypertension, long QT syndrome and torsades de pointes, liver failure and liver disease, epilepsy, COPD, kidney disease, pancreatitis, thrombocytopenia, adrenocortical insufficiency, hypothyroidism, diabetes mellitus and diabetic ketoacidosis, peptic ulcer disease, inflammatory bowel disease, benign prostatic hyperplasia, bronchitis and hypotensive disorder, among others. These need verification against the product label.

Please refer to the package insert for label warnings and contraindications, which were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on model scores. There are no clinical trials or publications, the drug has no established direct effect on nasal tissue, and the link appears to be a graph artifact of the existing rhinitis and cold indications. Package insert safety data are also missing.

**To proceed, the following is needed:**
- Mechanism-of-action data (e.g. from DrugBank) to allow a proper mechanistic assessment
- Package insert warnings and contraindications from the Indian regulator or manufacturers, to complete safety screening
- A targeted literature and trial search for nasal cavity disease, and for the more plausible candidates (acute laryngopharyngitis as symptomatic relief, and headache-related conditions via NMDA antagonism)
- Review of the serotonergic and CYP2D6-related interaction risks before any new-indication use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

