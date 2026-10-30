---
layout: default
title: Altretamine
parent: Model Prediction Only (L5)
nav_order: 42
evidence_level: L5
indication_count: 6
monitor_inn: "Altretamine"
predicted_indications: ["female breast carcinoma", "rectum mucinous adenocarcinoma", "colon mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma", "cervical mucinous adenocarcinoma", "extrahepatic bile duct mucinous adenocarcinoma"]
last_modified_at: 2026-10-30
description: "Altretamine: predicted new indication female breast carcinoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Altretamine
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

## Altretamine: alkylating-like cytotoxic s-triazine → female breast carcinoma
{: .text-alpha }

## One-Sentence Summary

Altretamine is an oral cytotoxic chemotherapy agent of the s-triazine class.
The TxGNN model predicts it may be effective for **female breast carcinoma**, but the supporting evidence is limited: **no registered clinical trials** and **3 publications** (a systematic review, a preclinical xenograft study and a dose-intensity analysis), none of which is a clinical study in breast cancer patients.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | female breast carcinoma |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacological knowledge, altretamine (hexamethylmelamine) is an s-triazine cytotoxic agent. It is thought to need metabolic activation to reactive intermediates, including formaldehyde-releasing methylmelamines, that damage DNA. A general DNA-damaging mechanism could plausibly act in other solid tumours, including breast carcinoma.

The literature gives only indirect support. A 2023 systematic review of s-triazine anticancer agents groups altretamine with other s-triazine drugs. A 1995 preclinical study reported antitumour activity of altretamine against human breast carcinoma xenografts in nude mice. Neither study evaluated altretamine in patients with breast cancer.

Because no cited study directly addresses breast carcinoma in humans, the evidence level is capped at L5 (model prediction with only indirect or preclinical signals).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37298753](https://pubmed.ncbi.nlm.nih.gov/37298753/) | 2023 | Systematic review | Molecules | Reviews the antitumour activity of s-triazine derivatives. Notes altretamine as one of three approved s-triazine anticancer drugs. |
| [7559101](https://pubmed.ncbi.nlm.nih.gov/7559101/) | 1995 | Preclinical (in vivo xenograft) | Jpn J Cancer Res | Altretamine was tested against five human breast carcinoma xenografts, plus stomach and colon xenografts, in nude mice. Antitumour activity was reported. |
| [8411257](https://pubmed.ncbi.nlm.nih.gov/8411257/) | 1993 | Review / dose-intensity analysis | J Natl Cancer Inst | Dose-intensity analysis of multiagent chemotherapy in advanced ovarian cancer, including altretamine. Only cisplatin showed a significant association between dose intensity and response. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 45917 | Cantret Capsule (Natco Pharma Ltd) | Strip of 10 capsules | Not recorded in the local data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (s-triazine, alkylating-like agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. Leukopenia, thrombocytopenia and anaemia appear among the recorded contraindicated conditions. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count (with differential), neurological assessment (peripheral neuropathy), liver and renal function |
| Handling Protection | Follow local cytotoxic drug handling regulations |

## Safety Considerations

- **Conditions recorded as contraindicated (not label text):** thrombocytopenia, peripheral nervous system disease, peripheral neuropathy, anaemia, macrocytic anaemia, central nervous system origin vertigo, leukopenia.
- **Drug Interactions:** 120 interactions were found. Examples at **Major** level include deferiprone, adalimumab and samarium (153Sm) lexidronam. Many **Moderate** interactions were found too, including cimetidine, pyridoxine, zidovudine, ganciclovir, chloramphenicol, doxepin, alemtuzumab and roflumilast. Combinations with other myelosuppressive or immunosuppressive agents deserve particular caution.

Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (0.9991), but there are no registered clinical trials, and the only breast-specific data are preclinical xenograft results. The review and the dose-intensity analysis do not test altretamine in breast cancer patients. The safety profile (myelosuppression, neurotoxicity, many drug interactions) calls for a clear efficacy signal before further investment.

**To proceed, the following is needed:**
- Clinical data in breast carcinoma (retrospective series or early-phase trials) to move beyond L5
- Mechanism of action data and a clear mechanistic rationale for breast tissue
- Package insert warnings and contraindications from the Indian label
- A haematological and neurological safety monitoring plan, plus a review of drug interactions against standard breast cancer regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

