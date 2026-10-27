---
layout: default
title: Nebivolol
parent: Model Prediction Only (L5)
nav_order: 583
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Nebivolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "Nebivolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
---

# Nebivolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Nebivolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Nebivolol is a beta-blocker originally used to treat hypertension.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, nebivolol is a beta-1 selective blocker that also promotes nitric oxide-mediated vasodilation through beta-3 agonism. Its efficacy in hypertension is established, and it is marketed for that use.

Malignant hypertensive renal disease is a severe, hypertension-driven form of kidney injury. Blood-pressure lowering and possible endothelial protection give a plausible, theoretical link to the original indication.

There are important limits. Malignant hypertension is a hypertensive emergency usually managed with intravenous agents, which makes an oral beta-blocker unlikely to be first-line. The high score likely reflects closeness to the approved hypertension indication in the knowledge graph rather than independent evidence.

Other predictions with the same model score level were also reviewed:
- **Malignant renovascular hypertension** (score 99.42%): beta-blockers reduce renin release, but the link is theoretical only and no studies were supplied.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 99.39%): the only one of the five with any literature (12 papers, evidence level L4). The papers are mostly preclinical or indirect, such as nebivolol protecting liver, kidney and endothelium via AKT1/Hif-1α/eNOS signaling in animals and cells. None tests nebivolol in patients with pulmonary hypertension.
- **Pulmonary hypertension with unclear multifactorial mechanism** (score 99.39%) and **Braddock syndrome** (score 99.14%): no studies, and no evident mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

For the pulmonary hypertension (hypoxia-related) prediction, the most relevant retrieved papers are listed below. They are indirect and none studies nebivolol in pulmonary hypertension patients.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21883997](https://pubmed.ncbi.nlm.nih.gov/21883997/) | 2012 | Randomized placebo-controlled trial | Cardiovasc Ther | Nebivolol vs carvedilol on exercise capacity in healthy subjects at high-altitude hypoxia |
| [21045724](https://pubmed.ncbi.nlm.nih.gov/21045724/) | 2011 | Clinical physiology study | J Hypertens | Selective vs nonselective beta-blockade and 24-h blood pressure under hypobaric hypoxia |
| [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/) | 2013 | Clinical comparative study | Int J Cardiol | CARNEBI trial: carvedilol vs nebivolol vs bisoprolol in moderate heart failure |
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Review | Cardiovasc Drugs Ther | Respiratory effects of beta-blockers in heart failure |
| [23400988](https://pubmed.ncbi.nlm.nih.gov/23400988/) | 2013 | Clinical physiology study | Anesth Analg | Highly selective beta-1 blockade (nebivolol) impaired cerebral perfusion after hemodilution in rats |
| [36947849](https://pubmed.ncbi.nlm.nih.gov/36947849/) | 2023 | Preclinical (animal) | Can J Physiol Pharmacol | Nebivolol protected against methotrexate nephrotoxicity in rats via AKT1/Hif-1α/eNOS |
| [32128711](https://pubmed.ncbi.nlm.nih.gov/32128711/) | 2020 | Preclinical (animal) | Pharmacol Rep | Renal protective effect of nebivolol in rat acute renal injury models |
| [34693844](https://pubmed.ncbi.nlm.nih.gov/34693844/) | 2022 | Preclinical (animal) | Drug Chem Toxicol | Nebivolol reduced methotrexate liver damage via AKT1/Hif1α/eNOS |
| [35202159](https://pubmed.ncbi.nlm.nih.gov/35202159/) | 2022 | Preclinical (in vitro) | Toxins | Nebivolol protected endothelial cells from aristolochic acid oxidative stress |

## India Market Information

Nebivolol is marketed in India as oral tablets (strips of 10 tablets), with 20 valid single-ingredient registrations and no cancelled ones. Approved indication text was not available for these registrations. Five main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 157269 | Nebimax AM 5mg/5mg Tablet (Johnlee Pharmaceuticals) | Tablet | Not stated |
| 159215 | Nebiraw 5mg Tablet (Rawlley Healthcare) | Tablet | Not stated |
| 150935 | Nebistar LN 5mg/10mg Tablet (Lupin) | Tablet | Not stated |
| 152823 | Nebipil SA Tablet (Alkem Laboratories) | Tablet | Not stated |
| 156383 | Nevol 2.5mg Tablet (Medley Pharmaceuticals) | Tablet | Not stated |

## Safety Considerations

- **Disease associations flagged as contraindications in the knowledge graph** (not taken from label text): liver failure, liver disease, gallbladder disease, diabetes mellitus, diabetic ketoacidosis, peripheral vascular disease, intermittent claudication, peripheral arterial disease, hypoglycemia, atrioventricular block, bronchial disease, sick sinus syndrome, familial sick sinus syndrome.
- **Drug Interactions**: 174 interactions were identified. Those shown include mostly moderate-level interactions with:
  - Epinephrine
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
  - Anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine)
  - Bupropion
  - Morphine
  - Lorcaserin
  - SGLT2 inhibitors and antidiabetics (canagliflozin, dapagliflozin, chlorpropamide)
  - Calcium salts

  Minor interactions include acetylsalicylic acid and magnesium oxide.

Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output only (evidence level L5), with no clinical trials or literature for malignant hypertensive renal disease. Malignant hypertension is normally treated acutely with other agents. The score likely reflects proximity to nebivolol's existing hypertension indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for Indian products (currently missing and blocking safety screening)
- Mechanism of action data from DrugBank
- Clinical or well-designed preclinical evidence of nebivolol in hypertensive renal disease
- Review of the knowledge-graph contraindications (e.g., bronchial disease, atrioventricular block, diabetes) against the target population
- If a lead is wanted among the other predictions, pulmonary hypertension is the only one with any supporting literature; it remains a research question at evidence level L4
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

