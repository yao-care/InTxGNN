---
layout: default
title: Seratrodast
parent: Model Prediction Only (L5)
nav_order: 768
evidence_level: L5
indication_count: 10
---

# Seratrodast
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Seratrodast: From Asthma to Migraine with or without Aura, Susceptibility to

## One-Sentence Summary

Seratrodast is a thromboxane A2 (TP) receptor antagonist, marketed in India in oral tablet form, and the product is generally used for asthma.
The TxGNN model predicts it may be effective for **migraine with or without aura, susceptibility to**.
This prediction is supported by **no clinical trials and no publications**, so it rests on the model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license records (the drug is generally known as an asthma treatment) |
| Predicted New Indication | Migraine with or without aura, susceptibility to |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, seratrodast is a thromboxane A2 (TP) receptor antagonist, and its efficacy in asthma is the basis of its marketed use. Mechanistically, it may be applicable to migraine through modulation of thromboxane/prostanoid signalling in vascular tone and platelet activity, but this link is speculative.

An important caveat: this entry is a genetic susceptibility phenotype rather than a treatable clinical condition. The high TxGNN score (0.996) is a model prediction only, and no trials or literature support it. The related entry "migraine disorder" (score 99.54%) is a more clinically meaningful target, but it has the same lack of evidence.

Other predictions of note:
- **Pulmonary hypertension** (score 99.47%): Thromboxane A2 is a vasoconstrictor and promotes platelet aggregation and vascular smooth muscle proliferation, so TP receptor antagonism is mechanistically plausible. The only literature is a 1998 general review of eicosanoids in paediatric practice, which is indirect evidence (evidence level L4).
- **Rheumatoid arthritis** (score 99.45%): Eicosanoids take part in synovial inflammation, but there is no supporting evidence.
- Several other predictions (brachydactyly-syndactyly syndrome, colobomatous microphthalmia-rhizomelic dysplasia syndrome, atrophoderma vermiculata, leprosy) have no plausible pathway link and likely reflect graph-embedding artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for migraine with or without aura, susceptibility to.

For reference, the only publication identified for any of the top-ranked predictions relates to pulmonary hypertension:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9711442](https://pubmed.ncbi.nlm.nih.gov/9711442/) | 1998 | Review | Drugs | General review of eicosanoids (prostaglandins, thromboxanes, leukotrienes) and their inhibitors for potential use in paediatric practice; does not test seratrodast directly |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 200144 | Seretra 80 Tablet (Zuventus Healthcare Ltd) | Strip of 10 tablets | Not specified |
| 202314 | Seradair 80mg Tablet (Fourrts India Laboratories Pvt Ltd) | Strip of 10 tablets | Not specified |
| 1874 | Alatro Tablet (Lupin Ltd) | Strip of 10 tablets | Not specified |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for migraine with or without aura, susceptibility to, is supported only by a TxGNN model score, with no clinical trials or literature. The entry is also a genetic susceptibility phenotype rather than a treatable condition, so it is not a suitable development target as it stands.

**To proceed, the following is needed:**
- Obtain the India package insert (warnings, contraindications, approved indications), which is currently a blocking gap for safety screening
- Obtain mechanism of action data from DrugBank
- Reframe the target as "migraine disorder" and search for preclinical or clinical evidence on thromboxane/TP receptor antagonism in migraine
- Consider pulmonary hypertension as a more mechanistically plausible research question, starting with a targeted literature review
- Review drug interaction and safety data once available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

