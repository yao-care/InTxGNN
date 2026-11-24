---
layout: default
title: Dabigatran Etexilate
parent: Model Prediction Only (L5)
nav_order: 225
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
description: "Dabigatran Etexilate: predicted new indication Sclerosing cholangitis (evidence level L5). Approved use: Not stated in the data compiled for this report"
monitor_inn: "Dabigatran etexilate"
predicted_indications: ["sclerosing cholangitis", "obsolete familial combined hyperlipidemia", "hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "primary release disorder of platelets"]
---

# Dabigatran Etexilate
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

## Dabigatran etexilate: From Anticoagulation to Sclerosing Cholangitis
{: .text-alpha }

## One-Sentence Summary

Dabigatran etexilate is an oral direct thrombin inhibitor marketed in India as an anticoagulant. The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but this is a computational prediction only. There are **0 clinical trials** and **1 publication** linked to it, and that publication does not test dabigatran for this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the approved indication text is empty for all registrations) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dabigatran etexilate: "Dabigatran and its acyl glucuronides are competitive, direct thrombin inhibitors. Because thrombin (serine protease) enables the conversion of fibrinogen into fibrin during the coagulation cascade, its inhibition prevents the development of a thrombus." ([DailyMed: Dabigatran (dabigatran etexilate) prescribing information, AvPAK](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39ac558a-b375-f3c1-e063-6394a90aa901), label version 2026-11-02; accessed 2026-11-19.) Based on general pharmacology, dabigatran is a direct thrombin inhibitor. Its efficacy as an anticoagulant is established, and mechanistically it might be relevant to sclerosing cholangitis.

A possible link is that thrombin signalling (through PAR receptors) contributes to liver inflammation and fibrosis. Blocking thrombin could, in theory, dampen these processes in a fibrosing bile duct disease. This remains a hypothesis. No data compiled for this report show that it applies to sclerosing cholangitis.

The very high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The other top predictions (lipid disorders and a platelet release disorder) have no clear mechanistic connection to thrombin inhibition. This suggests the model may be picking up learned similarities between diseases rather than a real effect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for sclerosing cholangitis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | Other (DDI/pharmacokinetic evaluation) | Clinical Pharmacokinetics | Evaluates cytochrome P450 and transporter-mediated drug interaction potential of cilofexor, an FXR agonist in development for primary sclerosing cholangitis and NASH. It does not study dabigatran efficacy. |

---

## India Market Information

All 20 registrations are valid single-ingredient products. The approved indication text is not available for any of them.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 1664 | Afogatran 150 Capsule | Strip of 10 capsules | Valid |
| 58956 | Dabigo 75mg Capsule | Strip of 10 capsules | Valid |
| 59415 | Dabipla 110mg Capsule | Strip of 10 capsules | Valid |
| 59500 | Dablexa 150 Capsule | Strip of 10 capsules | Valid |
| 59733 | Dabiclot 75mg Capsule | Strip of 10 capsules | Valid |
| 62792 | Dabirex 150 Capsule | Strip of 10 capsules | Valid |
| 63256 | Dabigza 150 Capsule | Bottle of 14 capsules | Valid |
| 63354 | Dabxiga 110mg Capsule | Strip of 10 capsules | Valid |
| 65419 | Debijohn 110mg Tablet | Strip of 10 tablets | Valid |
| 66113 | Dabimend 110 Capsule | Strip of 10 capsules | Valid |
| 66260 | Dbgron 150 Capsule | Strip of 10 capsules | Valid |
| 66701 | Debiganto 150mg Tablet | Strip of 10 tablets | Valid |
| 67121 | Dabirock 150mg Capsule | Strip of 10 capsules | Valid |
| 67767 | Dabitel 150 Capsule | Strip of 10 capsules | Valid |
| 68085 | Dabitel 110mg Capsule | Strip of 10 capsules | Valid |
| 69423 | Dabipack 150mg Capsule | Strip of 10 capsules | Valid |
| 70954 | Dabisung 75mg Capsule | Strip of 10 capsules | Valid |
| 71648 | Dabirock 75mg Capsule | Strip of 10 capsules | Valid |
| 136039 | Macdaxa 110mg Capsule | Strip of 10 capsules | Valid |
| 138058 | Macdaxa 150mg Capsule | Strip of 10 capsules | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: blood coagulation disease, anemia, macrocytic anemia, intracerebral hemorrhage. These come from drug-disease contraindication links in the TxGNN knowledge graph and should be checked against the official package insert.
- **Bleeding risk**: As an anticoagulant, dabigatran may raise bleeding risk. This matters especially for conditions involving bleeding or liver impairment.

No drug interaction records were found. Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials, and the single linked publication concerns a different drug. The mechanistic link is hypothetical, and the drug's bleeding risk is a concern in a liver and bile duct disease.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical evidence on thrombin/PAR signalling in cholestatic liver fibrosis or sclerosing cholangitis models
- Review of safety and bleeding risk in patients with cholestatic liver disease
- Confirmation of route compatibility and a literature search for dabigatran-specific studies in this disease

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Dabigatran (dabigatran etexilate) prescribing information, AvPAK](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=39ac558a-b375-f3c1-e063-6394a90aa901) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

