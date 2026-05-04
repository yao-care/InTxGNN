---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 4
---

# Darunavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Darunavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Darunavir is an HIV-1 protease inhibitor, originally developed and approved as a core component of combination antiretroviral therapy (ART) for HIV-1 infection in adults and paediatric patients.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection**,
with **0 clinical trials** and **4 publications** — all non-human primate (NHP) animal model studies — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (combination antiretroviral therapy) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacological knowledge, Darunavir is a second-generation HIV-1 protease inhibitor. It binds tightly to the active site of the HIV-1 protease enzyme, blocking cleavage of the Gag-Pol polyprotein precursor into functional viral structural proteins — thereby halting viral maturation and preventing the production of new infectious viral particles. It is routinely co-administered with a pharmacokinetic booster (ritonavir or cobicistat) to maintain therapeutic plasma concentrations.

SIV (Simian Immunodeficiency Virus) and HIV-1 are closely related lentiviruses within the primate lentivirus family. Their protease enzymes share significant structural homology, which underpins the biological rationale for Darunavir's activity in SIV models. All four supporting publications use SIV-infected rhesus macaques as the experimental platform — the gold-standard animal model for studying HIV pathogenesis, ART strategies, and viral reservoir dynamics. Darunavir appears in these regimens as an established ART backbone drug.

However, a critical contextual note is required: **SIV infection in macaques is a translational bridge model for HIV research, not an independent clinical repurposing indication**. The TxGNN knowledge graph captures mechanistic similarity between SIV and HIV-1, which generates a high prediction score — but the clinical value of this output must be interpreted with care. This "repurposing" reflects Darunavir's role in pre-clinical HIV science, not a new therapeutic application for a distinct human disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Darunavir in simian immunodeficiency virus infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Animal Model (NHP/SIV) | AIDS Research and Human Retroviruses | Evaluated two novel injectable cART regimens including Darunavir in SIVmac239-infected rhesus macaques; demonstrated effective suppression of SIV replication to clinically relevant levels, supporting use of this model for HIV eradication research |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal Model (NHP/SIV) | PLoS ONE | Studied SIV-infected Chinese-origin rhesus macaques on intensive Darunavir-containing cART combined with HDAC inhibitor SAHA; investigated viral reservoir dynamics and persistence despite virologic suppression |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal Model (NHP/SIV) | PLoS Pathogens | Highly intensified multidrug ART including Darunavir in SIVmac251-infected macaques achieved long-term viral suppression across a wide range of viral loads and significantly restricted the size of the viral reservoir |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Animal Model (NHP/SIV) | AIDS (London) | Gold compound auranofin tested alongside Darunavir-containing cART in SIV monkey model; demonstrated impact on CD4+ T cell phenotype and lentiviral reservoir cell persistence, with post-ART viral containment observed |

---

## India Market Information

Darunavir currently has **no registered products in India** (0 authorizations on record). No market authorization table is available.

---

## Safety Considerations

**Drug Interactions**: Darunavir has 209 known drug-drug interactions recorded in the DDInter database. Interactions of clinical significance include:

- **Major**: Cisapride — concomitant use contraindicated; risk of serious cardiac arrhythmia due to QT prolongation
- **Moderate** (selected clinically notable examples):
  - *Antidiabetic agents*: Metformin, Pioglitazone, Acarbose, Alogliptin, Saxagliptin, Canagliflozin, Dapagliflozin, Chlorpropamide, Acetohexamide, Albiglutide — consistent with Darunavir/ritonavir's known effects on insulin sensitivity and glucose metabolism
  - *Corticosteroids*: Dexamethasone, Hydrocortisone, Betamethasone, Budesonide, Triamcinolone — reflects CYP3A4 inhibition by the ritonavir booster, potentially elevating corticosteroid exposure
  - *Antibiotics/antiemetics*: Clarithromycin, Aprepitant — bidirectional CYP3A4 interactions

The high number of moderate-level interactions with antidiabetic drugs is noteworthy given that HIV protease inhibitors are associated with metabolic syndrome and insulin resistance as a class effect.

For complete warnings and contraindications, please refer to the full prescribing information. Package insert safety data (TFDA/equivalent) was unavailable for this report and constitutes a blocking data gap (DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-predicted indication — SIV infection — is not a genuine independent clinical repurposing target. SIV-infected macaques serve as a surrogate model for human HIV research, and all four supporting publications are NHP pre-clinical studies with no human clinical trial evidence. Darunavir is already an established antiretroviral; its use in SIV models reflects translational HIV science infrastructure rather than a novel therapeutic application for a distinct disease. Furthermore, Darunavir is not currently marketed in India, limiting immediate regulatory and clinical relevance in this jurisdiction.

**To proceed, the following is needed:**

- **Clarify the research objective**: If the goal is to support HIV eradication research using SIV models, current evidence is sufficient for that purpose — but this does not constitute drug repurposing. If a genuinely new human clinical indication is sought, analysis should pivot to lower-ranked TxGNN predictions with clearer mechanistic novelty and human disease relevance.
- **Resolve blocking data gap (DG001)**: Obtain the approved prescribing information (package insert) to complete safety profiling, including key warnings and contraindications.
- **Resolve high-priority data gap (DG002)**: Retrieve confirmed MOA data from DrugBank to formally support mechanistic analyses for any repurposing hypothesis.
- **India market entry assessment**: If registration in India is a strategic goal, initiate a regulatory gap analysis — 0 current licenses means a full new drug application pathway would be required.
- **Evaluate remaining predicted indications**: Ranks 2–4 (feline AIDS, rare neurodevelopmental disorder, obsolete hyperlipidemia ontology term) all carry Hold recommendations with weak or negative mechanistic rationale; none currently merit advancement without further evidence generation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

