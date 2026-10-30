---
layout: default
title: Fosaprepitant
parent: Model Prediction Only (L5)
nav_order: 379
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Fosaprepitant: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Fosaprepitant"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "pneumocystosis", "leprosy", "Cryptococcal meningitis", "multiple endocrine neoplasia", "intracranial abscess", "retinitis", "Plasmodium falciparum malaria", "echinococcus granulosus infectious disease", "hyperargininemia"]
---

# Fosaprepitant
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Fosaprepitant: From Chemotherapy-Associated Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Fosaprepitant is an injectable prodrug of aprepitant, a substance P/NK1 receptor antagonist. It is marketed in India as an antiemetic. The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but **no clinical trials and no publications** currently support this prediction, so it is a computational hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the approved indication text is blank for all licences) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (15 of 15) – CDSCO approval status is not included in this data |
| Number of Listed Products | 15 (valid: 15) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, fosaprepitant is a prodrug of aprepitant and acts as an NK1 receptor antagonist. Substance P/NK1 signalling has been loosely discussed in relation to water balance.

The link to NSIAD is weak. NSIAD is a disorder caused by gain-of-function of the vasopressin V2 receptor, and no direct connection to NK1 antagonism is evident. The high TxGNN score (0.9992) is a model output only and should be treated as speculative. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction (NSIAD).

## India Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 88628 | Fosapp Injection | Vial of 1 injection | Celon Laboratories Ltd |
| 73877 | Emend 150mg Injection | Vial of 1 injection | MSD Pharmaceuticals Pvt Ltd |
| 79825 | ES Pitant 150mg Injection | Vial of 1 injection | Esperer Bioresearch Pvt Ltd |
| 86155 | Fosa 150mg Injection | Vial of 1 injection | Mylan Pharmaceuticals Pvt Ltd |
| 6281 | Amitant-IV Injection | Vial of 1 injection | Aureate Healthcare Pvt Ltd |

Fifteen valid single-ingredient licences are registered in total; the five above are shown. All are injectable products. Approved indication text is not available for any licence.

## Safety Considerations

- **Knowledge-graph contraindication signal**: liver failure (from drug-disease contraindication edges in the knowledge graph, not from label text).
- **Drug Interactions**: 158 interactions were identified. Those listed as **Major** include:
  - Eliglustat
  - Naloxegol

  Examples of **Moderate** interactions include:
  - Corticosteroids (dexamethasone, hydrocortisone, betamethasone, budesonide, triamcinolone)
  - Clarithromycin
  - Cimetidine
  - Proton pump inhibitors (rabeprazole, lansoprazole)
  - Pioglitazone
  - Glimepiride
  - Nateglinide
  - Saxagliptin
  - Miconazole
  - Dronabinol
  - Alosetron
  - Naldemedine

Please refer to the package insert for full warnings and contraindications.

## Other Predicted Indications (for Context)

| Rank | Predicted Indication | Score | Evidence Level | Note |
|------|------|------|------|------|
| 2 | Pneumocystosis | 0.9987 | L5 | No supporting data; established antimicrobials exist |
| 3 | Leprosy | 0.9982 | L5 | No clear mechanism |
| 4 | Cryptococcal meningitis | 0.9979 | L5 | Theoretical interest only |
| 5 | Multiple endocrine neoplasia | 0.9976 | L5 | NK1 antiproliferative activity is preclinical only |
| 6 | Intracranial abscess | 0.9975 | L5 | No evident mechanism |
| 7 | Retinitis | 0.9968 | L5 | One preclinical mouse study (see below) |
| 8 | *Plasmodium falciparum* malaria | 0.9964 | L5 | No established mechanism |
| 9 | Echinococcus infection | 0.9950 | L5 | No plausible mechanism |
| 10 | Hyperargininemia | 0.9941 | L5 | Likely a network-proximity artifact |

**Retinitis, the only prediction with any supporting literature:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32058829](https://pubmed.ncbi.nlm.nih.gov/32058829/) | 2021 | Preclinical (mouse) | Ocular Immunology and Inflammation | Fosaprepitant blocked UVR-B-induced NK1R expression in exposed and unexposed partner eye tissues |

This is indirect evidence, from a UV-injury cataract model rather than retinitis itself.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The NSIAD prediction rests only on a model score. There are no clinical trials or publications, and no clear mechanistic link between NK1 antagonism and V2 receptor gain-of-function. Of all ten predictions, only retinitis has any supporting evidence, and that is a single preclinical study (L4, a research question rather than a development candidate).

**To proceed, the following is needed:**
- Mechanism of action data for fosaprepitant/aprepitant, to allow a mechanistic-link analysis
- Package insert warnings and contraindications from the India regulator (a blocking gap for safety screening)
- Approved indication text for the Indian licences, to confirm the original indication
- Preclinical or mechanistic studies testing NK1 involvement in NSIAD
- If retinitis is pursued, validation in relevant retinitis models
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

