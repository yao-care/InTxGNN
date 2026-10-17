---
layout: default
title: Altretamine
parent: Moderate Evidence (L3-L4)
nav_order: 42
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Altretamine: predicted new indication Female breast carcinoma (evidence level L4). Approved use: Ovarian cancer"
monitor_inn: "Altretamine"
predicted_indications: ["female breast carcinoma", "rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "extrahepatic bile duct mucinous adenocarcinoma"]
---

# Altretamine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Altretamine: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Altretamine is an oral cytotoxic agent originally used to treat ovarian cancer.
The TxGNN model predicts it may be effective for **female breast carcinoma**, but **no clinical trials** are registered for this use. Support is limited to **3 publications**, which include a systematic review, a preclinical xenograft study and a dose-intensity analysis in ovarian cancer.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (including ovarian adenocarcinoma and ovarian germ cell tumours; the India licence has no indication text) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Based on general pharmacological knowledge, altretamine (hexamethylmelamine) is an s-triazine, alkylating-like cytotoxic agent. It is thought to need metabolic activation to reactive intermediates, such as formaldehyde-releasing methylmelamines, that damage DNA. This mechanism is not specific to one tumour type, so it could plausibly act in breast carcinoma.

The only direct signal comes from a 1995 preclinical study. In nude mice, altretamine showed antitumour activity against human breast carcinoma xenografts, and also against stomach and colon carcinoma xenografts. A 2023 systematic review of s-triazine derivatives also discusses altretamine as an approved s-triazine anticancer drug, though it mentions breast cancer in connection with gedatolisib rather than altretamine.

The high TxGNN score reflects knowledge-graph proximity between cancers. It is not proof of clinical benefit. No human efficacy data in breast cancer were supplied.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37298753](https://pubmed.ncbi.nlm.nih.gov/37298753/) | 2023 | Systematic review | Molecules | Reviews s-triazine derivatives as anticancer scaffolds. Altretamine is noted as approved for refractory ovarian cancer. |
| [7559101](https://pubmed.ncbi.nlm.nih.gov/7559101/) | 1995 | Preclinical (in vivo xenograft) | Jpn J Cancer Res | Altretamine (hexamethylmelamine) showed antitumour activity against human breast, stomach and colon carcinoma xenografts in nude mice. |
| [8411257](https://pubmed.ncbi.nlm.nih.gov/8411257/) | 1993 | Review / dose-intensity analysis | J Natl Cancer Inst | Dose-intensity analysis of multiagent chemotherapy in advanced ovarian cancer. Only cisplatin showed a significant association between dose intensity and response. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 45917 | Cantret Capsule (Natco Pharma Ltd) | Strip of 10 capsules | Not stated in the licence data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (s-triazine, alkylating-like agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. The knowledge graph lists thrombocytopenia, leukopenia and anaemia as contraindication-related conditions, which suggests haematological toxicity is a concern. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function, and neurological assessment (the knowledge graph flags peripheral neuropathy) |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text)**: thrombocytopenia, leukopenia, anaemia (including macrocytic anaemia), peripheral neuropathy and other peripheral nervous system disease, and central nervous system origin vertigo.
- **Drug Interactions**: 120 interactions were identified. Major-level examples include deferiprone, adalimumab and samarium (153Sm) lexidronam. Moderate-level examples include cimetidine, pyridoxine, chloramphenicol, doxepin, zidovudine, ganciclovir, alemtuzumab and strontium chloride Sr-89. Minor-level examples include levofloxacin and gemifloxacin. Many of these involve additive myelosuppression or immunosuppression.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score, a single preclinical xenograft study and indirect review literature. No clinical trials or human efficacy data exist for breast carcinoma. The evidence is at L4, and the safety profile (myelosuppression, neurotoxicity, many interactions) calls for caution. Altretamine is also not a standard breast cancer therapy.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for Cantret Capsule, which are needed before safety screening.
- Mechanism of action data from DrugBank.
- Clinical data in breast cancer, such as earlier phase 2 studies, with a comparison against current standard therapy.
- A review of the other predicted indications (germ cell tumours, mucinous adenocarcinomas of other organs). These are all prediction-only (L5) and largely overlap with existing ovarian indications or rest on histology similarity.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

