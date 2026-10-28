---
layout: default
title: Capmatinib
parent: Model Prediction Only (L5)
nav_order: 139
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Capmatinib: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not stated in the available India license data (the drug is known as…"
monitor_inn: "Capmatinib"
predicted_indications: ["rheumatoid arthritis", "brachydactyly-syndactyly syndrome"]
---

# Capmatinib
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

## Capmatinib: From MET-Driven Cancer Treatment to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Capmatinib is a selective MET inhibitor and a kinase inhibitor, marketed in India as Rahika. The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are currently **no clinical trials** and only **1 general review publication** with no RA-specific data. This prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available India license data (the drug is known as a MET inhibitor for MET-altered cancers) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, capmatinib is a selective MET inhibitor. MET signaling has been implicated in synovial inflammation and angiogenesis in rheumatoid arthritis, so a mechanistic rationale is plausible.

However, the only linked publication is a general review of FDA-approved small-molecule kinase inhibitors, and it contains no RA-specific data for capmatinib. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The link between the original use (oncology) and RA is therefore hypothesis-level only.


## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Review | Pharmacological Research | General update on FDA-approved small-molecule protein kinase inhibitors; no RA-specific data for capmatinib |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 199516 | Rahika 150mg Tablet | Strip of 12 tablets | Not stated in the available data |
| 199517 | Rahika 200mg Tablet | Strip of 12 tablets | Not stated in the available data |

Both products are single-ingredient, valid, oral tablets manufactured by Novartis India Ltd.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MET tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database; 20 were reviewed here. Main ones by severity:
  - **Major**: Dexamethasone, Clarithromycin
  - **Moderate**: Metformin, Alosetron, Loperamide, Aprepitant, Empagliflozin, Glycerol phenylbutyrate, Methylnaltrexone, Metreleptin, Naldemedine, Naltrexone
  - **Minor**: Rabeprazole, Dexlansoprazole, Esomeprazole, Fidaxomicin, Lansoprazole, Naloxegol, Omeprazole, Pantoprazole
- **Cardiac signal**: A published case report describes cardiac toxicity from a pharmacokinetic interaction involving crizotinib, another MET/ALK kinase inhibitor. This is a class-level caution rather than capmatinib-specific evidence, but cardiac safety should be evaluated carefully.
- **Developmental risk**: MET signaling is involved in craniofacial development, so inhibition may carry teratogenic risk.

Please refer to the package insert for warnings and contraindications, as these were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rheumatoid arthritis prediction rests only on a high computational score and a plausible but unverified MET-signaling rationale. There are no clinical trials and no RA-specific literature (Evidence Level L5).

**To proceed, the following is needed:**
- Package insert warnings, contraindications, and approved indication text for the India licenses (currently a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- RA-specific preclinical evidence (for example, MET inhibition in synovial inflammation or arthritis models)
- A review of MET-inhibitor safety in the RA population, including cardiac and interaction risks
- If pursued at all, heart disease or chemotherapy-toxicity protection is a more evidence-supported research question than RA, though still preclinical
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

