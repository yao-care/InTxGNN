---
layout: default
title: Ofloxacin
parent: Model Prediction Only (L5)
nav_order: 614
evidence_level: L5
indication_count: 10
monitor_inn: "Ofloxacin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-10-28
description: "Ofloxacin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Not recorded in the local data"
---

# Ofloxacin
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

## Ofloxacin: Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibiotic. The TxGNN model (deep learning) predicts it may be effective for **hyperamylasemia** (score 0.9991); this score may reflect similarities the model learned between related diseases, not biological evidence. **No clinical trials and no publications** support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Licences | At least 20 (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, ofloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV. Its antibacterial activity is well established, but it is only recorded as a treatment for infections in the knowledge graph.

Hyperamylasemia is a biochemical finding. Its causes are pancreatic, salivary or renal, and it has no known antibacterial target. No plausible mechanistic link to ofloxacin could be identified. The very high TxGNN score (0.9991) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is not supported by any trial or literature, so the prediction should be treated as a computational signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indication Worth Noting: Septicemic Plague

Among the other predictions, **septicemic plague** (TxGNN score 0.9979) is the only one with a biologically plausible link. It was assessed at L4, preclinical evidence only. No human trials or registered clinical trials were found.

- In vitro studies show ofloxacin is highly active against *Yersinia pestis* ([8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/), [8913481](https://pubmed.ncbi.nlm.nih.gov/8913481/)).
- Mouse and primate models of plague suggest benefit for treatment or prophylaxis ([8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/), [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/), [9517950](https://pubmed.ncbi.nlm.nih.gov/9517950/)).
- This is largely class-level fluoroquinolone evidence and is not specific to ofloxacin. Several other retrieved papers concern resistance mechanisms or other organisms.

## India Market Information

At least 20 valid licences are recorded, all classified as single-ingredient products. The list may be partial. No approved-indication text is present in the licence records, so no approved indication can be stated from them. Five representative single-strength ofloxacin products are shown below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 3728 | Aliox 200mg Tablet | Strip of 10 tablets | Allien Pharmaceuticals |
| 170722 | Oflomus 200mg Tablet | Strip of 10 tablets | Kritikos Care |
| 169715 | Ofo 200mg Tablet | Strip of 10 tablets | Anglo-French Drugs & Industries Ltd |
| 87739 | Flozox 200mg Tablet | Strip of 10 tablets | Arovea Lifesciences Pvt Ltd |
| 164041 | Ole 200mg Tablet | Strip of 10 tablets | S P Pharma |

Some other listed product names (for example those with "OZ" or two strengths) suggest possible combination products. These should be verified before using their licences to describe single-ingredient ofloxacin.

## Safety Considerations

- **Contraindication-type relations recorded in the knowledge graph** (not label text): long QT syndrome, torsades de pointes, liver failure or disease, kidney disease and impaired renal function, epilepsy, myasthenia gravis, peripheral neuropathy, tendinitis, rhabdomyolysis, diabetes and diabetic ketoacidosis, thrombocytopenia, leukopenia, anemia, *Clostridium difficile* colitis, and drug-induced liver injury.
- **Drug interactions**: 383 interactions are recorded. Those rated Major among the first 20 listed are hydrocortisone, dexamethasone, betamethasone, triamcinolone, bupropion and chlorpropamide. Moderate ones include metformin, pioglitazone, acetylsalicylic acid, famotidine and calcium or potassium salts.
- Fluoroquinolones carry a peripheral neuropathy warning. This is a particular concern for the predicted indication "hematological disease associated with an acquired peripheral neuropathy".

Please refer to the package insert for official warnings and contraindications, as label text was not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hyperamylasemia prediction has a high model score but no trials, no literature and no plausible mechanism, so the evidence level is L5. The only biologically credible lead among the predictions is septicemic plague, which has preclinical support only.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanistic hypothesis linking ofloxacin to hyperamylasemia
- The package insert warnings and contraindications from the India licence holders
- Any direct clinical or observational study of ofloxacin in the predicted disease
- If plague is pursued instead, a review of guideline-level fluoroquinolone evidence and human data specific to ofloxacin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

