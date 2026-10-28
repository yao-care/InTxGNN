---
layout: default
title: Decitabine
parent: Model Prediction Only (L5)
nav_order: 237
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Decitabine: predicted new indication Refractory cytopenia of childhood (evidence level L4). Approved use: Myeloid leukaemia / acute myeloid leukaemia (several subtypes)"
monitor_inn: "Decitabine"
predicted_indications: ["refractory cytopenia of childhood"]
---

# Decitabine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Decitabine: From Acute Myeloid Leukaemia to Refractory Cytopenia of Childhood
{: .text-alpha }

## One-Sentence Summary

Decitabine is a hypomethylating anticancer drug, originally used for myeloid leukaemias such as acute myeloid leukaemia (AML).
The TxGNN model predicts it may be effective for **Refractory Cytopenia of Childhood (RCC)**, the main provisional subtype of paediatric myelodysplastic syndrome (MDS).
Currently there are **no registered clinical trials** and **2 publications** (one single-centre cohort study and one case report) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myeloid leukaemia / acute myeloid leukaemia (several subtypes) |
| Predicted New Indication | Refractory cytopenia of childhood |
| TxGNN Prediction Score | 0.9903 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 16 of 16) |
| Number of Registrations | 16 (valid: 16) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, decitabine is a hypomethylating agent (a DNA methyltransferase inhibitor). Its use in myeloid malignancies, including adult MDS and AML, is established, and mechanistically it may be applicable to refractory cytopenia of childhood.

RCC is the main provisional subtype of paediatric MDS. It shares features with adult myeloid disease, namely clonal myeloid dysplasia and aberrant DNA methylation. This offers a plausible biological rationale for using a hypomethylating drug.

This link is inferred from the drug class and adult use, not from curated mechanism data. The high TxGNN score is a computational prediction and does not count as clinical evidence.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35624441](https://pubmed.ncbi.nlm.nih.gov/35624441/) | 2022 | Cohort | BMC Pediatrics | Single-centre, 10-year experience with decitabine plus a minimally myelosuppressive regimen as a bridge to allogeneic stem cell transplantation in children with MDS |
| [42125547](https://pubmed.ncbi.nlm.nih.gov/42125547/) | 2026 | Case report | Experimental and Therapeutic Medicine | Decitabine monotherapy in an 8-year-old with RCC who was ineligible for transplantation or immunosuppressive therapy |

Both studies are in paediatric MDS and are small and uncontrolled. Neither is a randomised trial.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 64774 | Decita Injection (Natco Pharma) | Vial injection | Not specified |
| 64196 | Decitas 30 Injection (Intas) | Vial injection | Not specified |
| 66073 | Deczuba 50mg Injection (Glenmark) | Vial injection | Not specified |
| 62905 | Decitex 50mg Injection (Sun Pharma) | Vial injection | Not specified |
| 61800 | Dacogen Injection (Johnson & Johnson) | Vial (1 ml) injection | Not specified |

There are 16 valid single-ingredient registrations in total, all injectable.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (hypomethylating nucleoside analogue) |
| Myelosuppression Risk | High (the knowledge graph lists neutropenia, thrombocytopenia and agranulocytosis as contraindication-related conditions) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for detailed guidance.

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** kidney disease, liver disease, gallbladder disease, pyoureter, thrombocytopenia, neutropenia, agranulocytosis, diabetes mellitus and diabetic ketoacidosis.
- **Drug Interactions:** 120 interactions were identified. Major ones include:
  - Deferiprone
  - Samarium (153Sm) lexidronam
  - Adalimumab
  - Baricitinib

  Moderate ones include mercaptopurine, zidovudine, gemcitabine, ganciclovir, azathioprine, alemtuzumab, aldesleukin, chloramphenicol and live or inactivated vaccines.
  Many of these involve additive myelosuppression or immunosuppression.

Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible, but support is limited to one single-centre cohort and one case report. There are no registered clinical trials. The evidence level is L4, and the TxGNN score alone is not clinical evidence. In addition, the package insert safety review is not yet possible, which blocks safety screening.

**To proceed, the following is needed:**
- India package insert warnings and contraindications (download and parse the label PDF)
- Curated mechanism of action data from DrugBank
- A systematic literature search for paediatric MDS and RCC studies
- Registered or planned clinical trials in paediatric MDS
- A paediatric-specific safety assessment, including myelosuppression and dosing
- Confirmation of route compatibility (decitabine is injectable only) and of the approved indication wording in the India registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

