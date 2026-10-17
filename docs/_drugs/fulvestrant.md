---
layout: default
title: Fulvestrant
parent: Model Prediction Only (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fulvestrant: predicted new indication HIV infectious disease (evidence level L5). Approved use: Not stated in the India licence data compiled for this report (fulves…"
monitor_inn: "Fulvestrant"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "rheumatoid arthritis", "acne (disease)", "brachydactyly-syndactyly syndrome", "hemoglobinopathy", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Fulvestrant
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

# Fulvestrant: From Breast Cancer to HIV Infectious Disease

## One-Sentence Summary

Fulvestrant is an estrogen receptor antagonist and degrader, marketed in India as an injection for hormone receptor-positive breast cancer. The TxGNN model predicts it may be effective for **HIV infectious disease**, but there are **no registered clinical trials** and only **2 publications** (one preclinical mechanistic study and one tangential HTLV-1 paper). This is a hypothesis-stage prediction, not a clinically supported one.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India licence data compiled for this report (fulvestrant is known to be used in HR-positive advanced breast cancer) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (preclinical/mechanistic evidence only) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, fulvestrant is an estrogen receptor α (ERα) antagonist and degrader. Its efficacy in HR-positive breast cancer is established, and mechanistically it may be applicable to HIV through estrogen receptor signalling.

Estrogen receptor α is expressed in CD4+ T cells and is hypothesised to influence HIV transcription and latency. A 2026 in vitro study (PMID 42430506) examined how ER ligands, including fulvestrant, and HIV latency-reversing agents interact with ERα in CD4+ T cells. This suggests fulvestrant could plausibly influence latency reversal.

This evidence is preclinical and indirect. The link between breast cancer (a hormone-driven tumour) and HIV (a retroviral infection) is only through the shared estrogen receptor pathway. No study has tested fulvestrant in people with HIV.

## Clinical Trial Evidence

Currently no related clinical trials registered for HIV infectious disease.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42430506](https://pubmed.ncbi.nlm.nih.gov/42430506/) | 2026 | Preclinical in vitro mechanistic study | JCI Insight | Examined the effect of estrogen, fulvestrant and HIV latency-reversing agents on ERα in CD4+ T cells; ER signalling may influence HIV latency |
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Cross-omics cohort analysis | Research Square | Concerns HTLV-1-associated myelopathy (a different retrovirus), not HIV; only tangentially relevant |

## India Market Information

The licence records compiled for this report contain no approved-indication text. Five of the 20 valid single-ingredient injectable registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 84979 | Faslodex 500mg Injection (AstraZeneca) | Vial of 10 ml injection | Not stated in licence data |
| Registration No. 85200 | Faslodex 250mg Injection (AstraZeneca) | Vial of 5 ml injection | Not stated in licence data |
| Registration No. 87354 | Fuvestrol Injection (Cadila Pharmaceuticals) | Prefilled syringe of 5 ml injection | Not stated in licence data |
| Registration No. 88847 | Fulvenat 120mg Injection (Natco Pharma) | Vial of 1 injection | Not stated in licence data |
| Registration No. 203927 | Strantas 250mg Injection (Intas Pharmaceuticals) | Prefilled syringe of 5 ml injection | Not stated in licence data |

All 20 registrations are valid single-ingredient injectables; none are cancelled or combination products.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/hormonal therapy (selective estrogen receptor degrader), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; liver function and platelet count are reasonable considerations given the contraindication signals below |
| Handling Protection | Please refer to the package insert and local institutional handling policy |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** liver disease, gallbladder disease, thrombocytopenia and blood coagulation disease. These come from drug-disease contraindication links in the TxGNN knowledge graph and should be verified against the official label.
- **Drug Interactions:** 92 potential interactions were identified, all with severity level unspecified. Examples include warfarin, metformin, simvastatin, prednisone, dexamethasone, morphine, ondansetron, proton pump inhibitors (omeprazole, pantoprazole, lansoprazole), H2 blockers (famotidine, ranitidine), metoclopramide, metronidazole and acetylsalicylic acid. Clinical significance has not been graded. The warfarin pairing and the thrombocytopenia/coagulation flags deserve particular attention for an injectable given by intramuscular route.

Please refer to the package insert for key warnings and contraindications; this label information was not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for HIV is a single in vitro study and a tangential HTLV-1 paper, with no clinical trials. The high TxGNN score (99.91%) reflects network proximity rather than clinical evidence. Other predicted indications fare no better: the trials matched to "multiple endocrine neoplasia" are actually breast cancer studies (the approved use), and rheumatoid arthritis evidence is indirect and possibly contradictory (estrogen blockade worsened inflammation in a rat model). Treat HIV as a research question rather than a development candidate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India licence holders (currently missing; this blocks safety screening)
- Mechanism-of-action data from DrugBank
- Further in vitro and ex vivo work on ERα antagonism and HIV latency, including whether fulvestrant reverses or reinforces latency
- Assessment of the safety of long-term estrogen blockade in people with HIV, including bone health and coagulation
- Review of drug interaction severity, especially with antiretrovirals, which were not covered in the interaction data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

