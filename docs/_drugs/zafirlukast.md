---
layout: default
title: Zafirlukast
parent: Model Prediction Only (L5)
nav_order: 901
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
monitor_inn: "Zafirlukast"
predicted_indications: ["bronchitis", "obstructive lung disease"]
description: "Zafirlukast: predicted new indication Bronchitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Zafirlukast
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

## Zafirlukast: Bronchitis
{: .text-alpha }

## One-Sentence Summary

Zafirlukast is a cysteinyl leukotriene receptor antagonist, originally used to treat asthma (including intrinsic and allergic asthma).
The TxGNN model predicts it may be effective for **bronchitis**, but this rests on the model score alone: **0 clinical trials** and **0 publications** specific to this indication were found.
A second candidate, obstructive lung disease, has **18 publications**, mostly asthma-focused reviews, and no clinical trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, zafirlukast is a CysLT1 receptor antagonist. Cysteinyl leukotrienes drive bronchoconstriction, mucus secretion, vascular permeability and eosinophilic airway inflammation, and blocking them is the basis of its use in asthma.

Because these processes also occur in inflammatory bronchial conditions, there is a plausible mechanistic link between asthma and bronchitis. However, bronchitis is a heterogeneous condition (acute viral, chronic, eosinophilic), and the relevant subtype is not specified. The prediction score is the only support: no trials or publications were found for bronchitis.

For the second-ranked prediction, obstructive lung disease (score 0.9917), the high score is largely explained by asthma itself being an obstructive lung disease and the drug's existing indication. It is therefore not a strong new repurposing signal. The only COPD-related item is a review discussing leukotriene pathway inhibitors in asthma and COPD (PMID 10421833). No controlled COPD data were available.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for bronchitis, and none for obstructive lung disease.

---

## Literature Evidence

No literature is available for bronchitis. The table below lists the literature for the second-ranked prediction, obstructive lung disease. Study types were inferred from titles and abstracts and should be verified against the full texts.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10421833](https://pubmed.ncbi.nlm.nih.gov/10421833/) | 1999 | Review | Clin Exp Allergy | Leukotriene pathway inhibitors (zafirlukast, montelukast, zileuton) in asthma and chronic obstructive pulmonary disease; the only item touching COPD |
| [10023966](https://pubmed.ncbi.nlm.nih.gov/10023966/) | 1999 | Review | Lancet | Leukotriene-receptor antagonists show good antiasthmatic activity across severity levels, alone or with inhaled steroids |
| [9463793](https://pubmed.ncbi.nlm.nih.gov/9463793/) | 1998 | Review | Drugs | Pharmacology and therapeutic potential of zafirlukast in chronic asthma |
| [11270943](https://pubmed.ncbi.nlm.nih.gov/11270943/) | 2001 | Review (inferred) | Drugs | Update on zafirlukast 20 mg twice daily, shown effective in placebo-controlled studies of up to 13 weeks in asthma |
| [31544544](https://pubmed.ncbi.nlm.nih.gov/31533544/) | 2019 | Review (inferred) | Expert Rev Respir Med | Update on leukotriene treatments in asthma and related airway inflammation mechanisms |
| [26385352](https://pubmed.ncbi.nlm.nih.gov/26385352/) | 2015 | Review | Curr Allergy Asthma Rep | Antileukotrienes in upper airway inflammatory diseases, including allergic rhinitis |
| [9647602](https://pubmed.ncbi.nlm.nih.gov/9647602/) | 1998 | Review | Am J Respir Crit Care Med | Preclinical pharmacology: zafirlukast is a potent, selective CysLT1 antagonist |
| [11888331](https://pubmed.ncbi.nlm.nih.gov/11888331/) | 2002 | Pharmacokinetics | Clin Pharmacokinet | Pharmacokinetic profile; Cmax about 3 hours after oral dose; efficacy at 20–40 mg twice daily |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 247909 | Zuvair 10mg Tablet (Dr Reddy's Laboratories Ltd) | Strip of 10 tablets (oral) | Not stated in the licence record |

---

## Safety Considerations

- **Disease associations from the knowledge graph** (not label text): the TxGNN knowledge graph lists contraindication links with liver disease, cirrhosis of liver, gallbladder disease, insomnia, anxiety, anxiety disorder, neurotic disorder and dysthymic disorder. These should be confirmed against the official package insert.
- **Drug Interactions**: 376 interactions were recorded in total. Examples of moderate-level interactions include aprepitant, acetylsalicylic acid, metronidazole, budesonide, saxagliptin, eliglustat, naltrexone, nateglinide, nitisinone, repaglinide, rosuvastatin, simvastatin and tinidazole. Sibutramine is rated minor. Pantoprazole, mesalazine, morphine, metformin and omeprazole have an unknown severity level.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction rests only on a high model score (L5), with no clinical trials or publications specific to this indication. Obstructive lung disease reaches L4 only through indirect, asthma-dominated reviews, so its score mostly reflects the existing asthma indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian product (currently blocking safety screening), and the approved indication text for licence 247909
- Mechanism of action data from DrugBank
- Specification of the target bronchitis subtype (e.g., eosinophilic or chronic bronchitis)
- Controlled clinical data, such as RCTs in bronchitis or non-asthma COPD populations, plus a literature search specific to these indications
- Verification of study types against full texts
- Review of liver and gallbladder disease contraindications and the drug interaction burden for the intended population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

