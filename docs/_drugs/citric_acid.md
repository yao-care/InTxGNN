---
layout: default
title: Citric Acid
parent: Moderate Evidence (L3-L4)
nav_order: 188
evidence_level: L4
indication_count: 8
last_modified_at: 2026-10-14
description: "Citric Acid: predicted new indication Stomach disease (evidence level L4). Approved use: Dyspepsia"
monitor_inn: "Citric acid"
predicted_indications: ["stomach disease", "pharyngitis", "acute laryngopharyngitis", "postgastrectomy syndrome", "nasal cavity disease", "papillary conjunctivitis", "blepharoconjunctivitis", "rhinitis"]
---

# Citric Acid
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **8** 
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

## Citric Acid: From Dyspepsia to Stomach Disease
{: .text-alpha }

## One-Sentence Summary

Citric acid is a weak organic acid originally used for dyspepsia and headache disorder.
The TxGNN model predicts it may be effective for **stomach disease**, but **no clinical trials** are registered and the **18 publications** retrieved offer only indirect links, so the prediction rests mainly on the model.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dyspepsia; headache disorder (from the knowledge graph; no approved indication text is available in the India licence data) |
| Predicted New Indication | Stomach disease |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, citric acid is a weak organic acid that modulates gastric pH and is already used in gastrointestinal contexts for dyspepsia. Mechanistically, it could be relevant to other stomach conditions.

The literature shows only indirect links. A citric acid test meal has been studied to improve the accuracy of the 13C-urea breath test for detecting *H. pylori*. Other papers are general reviews on diet in ulcer disease and on *H. pylori* metabolism. **No evidence shows that citric acid treats stomach disease.** The very high TxGNN score is a computational prediction, partly explained by its similarity to the existing dyspepsia indication.

Other predicted indications (pharyngitis, acute laryngopharyngitis, postgastrectomy syndrome, nasal cavity disease, papillary conjunctivitis, blepharoconjunctivitis and rhinitis) have even weaker support. Most are L5, and the rhinitis and nasal cavity papers are indirect at best.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The retrieved publications are mostly indirect. Selected items are listed below (the most relevant to the predicted indication).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31505905](https://pubmed.ncbi.nlm.nih.gov/31505905/) | 2019 | Clinical diagnostic study | Gut and Liver | Discusses whether a citric acid test meal improves 13C-urea breath test accuracy in Asian populations (diagnostic use, not treatment) |
| [30970440](https://pubmed.ncbi.nlm.nih.gov/30970440/) | 2019 | Clinical diagnostic study | Gut and Liver | Effect of citric acid on 13C-urea breath test accuracy after *H. pylori* eradication in a region with common atrophic gastritis |
| [15854177](https://pubmed.ncbi.nlm.nih.gov/15854177/) | 2005 | Mechanistic study | Aliment Pharmacol Ther | Effect of citric, malic and ascorbic acids on intragastric urease activity |
| [2072799](https://pubmed.ncbi.nlm.nih.gov/2072799/) | 1991 | Review | Med Clin North Am | Diet and nutrition in ulcer disease; restrictive diets are not supported in the era of H2-inhibitors |
| [9889978](https://pubmed.ncbi.nlm.nih.gov/9889978/) | 1998 | Review | Adv Microb Physiol | Physiology and metabolism of *H. pylori* |
| [35900644](https://pubmed.ncbi.nlm.nih.gov/35900644/) | 2022 | Cohort / metabolomic association | Metabolomics | Higher serum citric acid and L-carnitine detected in Koreans before gastric cancer onset (biomarker association) |

---

## India Market Information

Citric acid is marketed in India as 20 valid single-ingredient registrations (no cancelled ones), mostly syrups and expectorants. Approved indication text is not available for these registrations. The five main authorisations are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 123961 | Lupihist Plus Syrup | Syrup (100 ml bottle) | Not specified |
| Registration No. 183137 | Quit Expectorant | Expectorant (100 ml bottle) | Not specified |
| Registration No. 21827 | Ableed Lotion | Lotion (60 ml bottle) | Not specified |
| Registration No. 116037 | Khasigo Syrup | Syrup (100 ml bottle) | Not specified |
| Registration No. 230529 | Uriboost Solution | Solution (200 ml bottle) | Not specified |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (drug-disease edges, not label text): hypertension, kidney disease or impaired renal function, anuria, liver disease, gallbladder disease, congestive heart failure, adrenal insufficiency (including Addison disease and congenital adrenal hyperplasia), peptic ulcer disease, gout, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, thrombocytopenia and thrombocytopenic purpura, haemophilia, anaemia, chronic diarrhoeal disease and substance abuse/dependence. Notably, **peptic ulcer disease** is listed, which is relevant to a stomach-disease indication.
- **Drug Interactions** (15 recorded):
  - **Major:** aluminium hydroxide.
  - **Moderate:** fluoroquinolone and quinolone antibacterials, including ciprofloxacin, levofloxacin, moxifloxacin, ofloxacin, norfloxacin, enoxacin, gatifloxacin, gemifloxacin, lomefloxacin, grepafloxacin, sparfloxacin, trovafloxacin, nalidixic acid and cinoxacin.

Please also refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials support the predicted indication, and the literature is indirect (diagnostic test meals, reviews and mechanistic or biomarker work). The high TxGNN score therefore remains an unvalidated model prediction, and the knowledge graph lists peptic ulcer disease as a contraindication. Evidence is at most L4 for this and one other prediction (rhinitis), and L5 for the rest. Both are best treated as research questions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator (the current safety data are incomplete)
- Detailed mechanism of action data
- Direct clinical evidence of benefit in stomach disease, such as a controlled trial
- Clarification of the safety conflict with peptic ulcer disease
- If pursuing rhinitis instead, confirmatory studies of the topical antibiofilm approach (currently preclinical only)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

