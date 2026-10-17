---
layout: default
title: Dabigatran Etexilate
parent: Model Prediction Only (L5)
nav_order: 225
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
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

# Dabigatran etexilate: From Anticoagulation to Sclerosing Cholangitis

## One-Sentence Summary

Dabigatran etexilate is an oral direct thrombin inhibitor marketed in India as an anticoagulant. The TxGNN model predicts it may be effective for **sclerosing cholangitis**, but this is a computational prediction only. There are **0 clinical trials** and **1 publication** linked to it, and that publication does not test dabigatran for this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the approved indication text is empty for all registrations) |
| Predicted New Indication | Sclerosing cholangitis |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, dabigatran is a direct thrombin inhibitor. Its efficacy as an anticoagulant is established, and mechanistically it might be relevant to sclerosing cholangitis.

A possible link is that thrombin signalling (through PAR receptors) contributes to liver inflammation and fibrosis. Blocking thrombin could, in theory, dampen these processes in a fibrosing bile duct disease. This remains a hypothesis. No data compiled for this report show that it applies to sclerosing cholangitis.

The very high TxGNN score reflects a pattern found in a knowledge graph. It is not evidence of benefit. The other top predictions (lipid disorders and a platelet release disorder) have no clear mechanistic connection to thrombin inhibition. This suggests the model may be picking up network-proximity artifacts.

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

All 20 registrations are valid single-ingredient products. The approved indication text is not available for any of them. The five listed below are examples.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 59733 | Dabiclot 75mg Capsule (Alkem Laboratories Ltd) | Strip of 10 capsules | Not available |
| 59500 | Dablexa 150 Capsule (Abbott) | Strip of 10 capsules | Not available |
| 65419 | Debijohn 110mg Tablet (Johnlee Pharmaceuticals Pvt Ltd) | Strip of 10 tablets | Not available |
| 63354 | Dabxiga 110mg Capsule (Lupin Ltd) | Strip of 10 capsules | Not available |
| 63256 | Dabigza 150 Capsule (Glenmark Pharmaceuticals Ltd) | Bottle of 14 capsules | Not available |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

