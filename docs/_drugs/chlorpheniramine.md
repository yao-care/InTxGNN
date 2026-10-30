---
layout: default
title: Chlorpheniramine
parent: Model Prediction Only (L5)
nav_order: 175
evidence_level: L5
indication_count: 1
monitor_inn: "Chlorpheniramine"
predicted_indications: ["nasal cavity disease"]
last_modified_at: 2026-10-30
description: "Chlorpheniramine: predicted new indication nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Chlorpheniramine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Chlorpheniramine: Histamine H1 receptor antagonist → nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Chlorpheniramine is an antihistamine (histamine H1 receptor blocker) that is marketed in India in single-ingredient products.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but the supporting evidence is limited to **8 preclinical or physiology publications** and **no registered clinical trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | nasal cavity disease |
| TxGNN Prediction Score | 0.9953 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general pharmacology, chlorpheniramine blocks histamine H1 receptors, which reduces histamine-driven sneezing, nasal itching and runny nose.

"Nasal cavity disease" is a broad category. It overlaps heavily with conditions that antihistamines are already used for, so this prediction is not a clearly distinct repurposing signal. The reasoning is plausible mechanistically, but it adds little new information.

The compiled literature does not support human efficacy. One animal study suggests that relieving nasal congestion may require blocking both H1 and H3 receptors, which argues against H1 blockade alone being effective for congestion.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

All of the literature below is preclinical (animal models) or experimental physiology. None of it directly tests chlorpheniramine as a treatment for nasal cavity disease in patients, which is why the evidence level is L5.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10582118](https://pubmed.ncbi.nlm.nih.gov/10582118/) | 1999 | Animal study | American Journal of Rhinology | In a cat model, combining chlorpheniramine (H1 blocker) with an H3 blocker reduced nasal airway resistance caused by mast cell degranulation |
| [10582116](https://pubmed.ncbi.nlm.nih.gov/10582116/) | 1999 | Animal study | American Journal of Rhinology | Describes pressure and acoustic rhinometry in a cat model of nasal congestion |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Animal study | American Journal of Rhinology | A dog model of allergic nasal congestion in ragweed-sensitized animals, measured by acoustic rhinometry |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Animal study | Journal of Pharmacological and Toxicological Methods | Pharmacological characterization of a noninvasive chronic dog model of nasal congestion |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Animal study | American Journal of Rhinology | Developed an acoustic rhinometry dog model of nasal congestion induced by compound 48/80 |
| [10822083](https://pubmed.ncbi.nlm.nih.gov/10822083/) | 2000 | Animal study | Immunopharmacology | New rat model of allergic rhinitis used to evaluate H1-receptor antagonists |
| [1705288](https://pubmed.ncbi.nlm.nih.gov/1705288/) | 1990 | Animal study | Journal of Pharmacobio-Dynamics | Brown Norway rat model of allergic rhinitis used to evaluate antiallergic drugs |
| [2923378](https://pubmed.ncbi.nlm.nih.gov/2923378/) | 1989 | Human physiology study | American Review of Respiratory Disease | Sources of protein in histamine-induced nasal secretions in atopic and nonatopic subjects |

## Safety Considerations

- **Contraindications:** Label-based contraindication text is not available in the data compiled for this report.
- **Drug Interactions:** 348 interactions were found in the interaction database. The listed ones include:
  - **Major:** potassium chloride, potassium citrate
  - **Moderate:** atropine, bupropion, dicyclomine, dronabinol, eliglustat, eluxadoline, glycopyrronium, loperamide, lorcaserin, mepenzolate, methscopolamine, metoclopramide, morphine, nabilone, opium

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting studies are animal models and one physiology study, with no clinical trials. The predicted indication is also very broad and overlaps with existing antihistamine uses. One study suggests H1 blockade alone may not relieve congestion.

**To proceed, the following is needed:**
- Human clinical data for a specific, well-defined nasal condition (rather than the broad "nasal cavity disease" category)
- Mechanism-of-action data for chlorpheniramine
- Package insert warnings and contraindications from the local regulator
- Clarification of how this prediction differs from existing antihistamine uses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

