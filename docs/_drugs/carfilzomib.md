---
layout: default
title: Carfilzomib
parent: Model Prediction Only (L5)
nav_order: 148
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Carfilzomib: predicted new indication Melanoma (evidence level L5). Approved use: Plasma cell myeloma"
monitor_inn: "Carfilzomib"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "vulvar melanoma (disease)", "melanoma"]
---

# Carfilzomib
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

## Carfilzomib: From Plasma Cell Myeloma to Melanoma
{: .text-alpha }

## One-Sentence Summary

Carfilzomib is an irreversible proteasome inhibitor, originally used to treat plasma cell myeloma (multiple myeloma).
The TxGNN model predicts it may be effective for **melanoma** and several melanoma subtypes.
However, **no clinical trials** are registered for this direction, and the only direct support is **one preclinical cell-line study**, so the evidence is still at the hypothesis stage.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plasma cell myeloma |
| Predicted New Indication | Melanoma (the top-ranked prediction is "CMM7", a poorly defined entity; the best-supported prediction is melanoma) |
| TxGNN Prediction Score | 0.9937 for the top-ranked prediction (CMM7); 0.9903 for melanoma |
| Evidence Level | L5 for melanoma (preclinical only); L5 for the other predicted melanoma subtypes |
| India Market Status | Marketed (valid licences: 3 of 3) |
| Number of Registrations | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, carfilzomib is an irreversible proteasome inhibitor. Its efficacy in plasma cell myeloma is established, and mechanistically it may be applicable to melanoma.

Blocking the proteasome causes misfolded and pro-apoptotic proteins to accumulate, which can push cancer cells toward programmed cell death. Myeloma cells are particularly dependent on this pathway, and melanoma cells may share part of this dependence. This link is plausible but unverified.

The only direct support is a 2021 laboratory study (PMID 33671902) in mouse B16-F1 melanoma cells. It reported that carfilzomib combined with bortezomib increased apoptosis. Results from mouse cell lines cannot be assumed to apply to human patients, and no human efficacy or safety data in melanoma were found.

Other predicted subtypes carry additional concerns:
- **Pediatric leptomeningeal melanoma**: carfilzomib has limited central nervous system penetration, and pediatric safety data are lacking.
- **Epithelioid cell uveal melanoma**: uveal melanoma is biologically distinct from cutaneous melanoma, so cell-line findings may not transfer.
- **Vulvar melanoma**: no mucosal melanoma-specific data are available.
- **CMM7**: the disease entity is not clearly defined in the supplied data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Literature for the melanoma prediction (all preclinical or computational; none are clinical studies):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | In vitro preclinical study | Biology | Carfilzomib combined with bortezomib enhanced apoptosis in B16-F1 melanoma cells, with activation of several caspases |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Computational study | J Biomol Struct Dyn | Docking and simulation study of repurposing clinical drugs against kinase targets across ten cancer types, including melanoma |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Preclinical mechanistic study (indirect) | Mol Cancer Res | ZFAND2A (AIRAP-like) gene regulates cell survival in human melanoma through cIAP2; indirect relevance |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Preclinical mechanistic study (indirect) | Matrix Biol | Bortezomib and carfilzomib raised heparanase expression via NF-κB in tumour cells, which may promote aggressive tumour behaviour; indirect relevance |

No literature was found for the other predicted subtypes (CMM7, pediatric leptomeningeal melanoma, epithelioid cell uveal melanoma, vulvar melanoma).

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 116250 | Kyprolis 60mg Injection (Dr Reddy's Laboratories Ltd) | Vial of 1 injection | Not stated in the available data |
| 38691 | Carzomib 60mg Injection (Hetero Healthcare Limited) | Vial of 1 injection | Not stated in the available data |
| 36183 | Carfilnat Injection (Natco Pharma Ltd) | Vial of 1 injection | Not stated in the available data |

All three registrations are valid single-agent injectable products.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (proteasome inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; typically CBC, liver and renal function |
| Handling Protection | Follow institutional cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: 227 interactions were recorded in the DDInter database. Examples of those flagged **Major**:
  - Anabolic steroids: oxandrolone, oxymetholone, stanozolol
  - Deferiprone
  - Samarium (153Sm) lexidronam
  - Haemostatic and coagulation products: aminocaproic acid, recombinant antihemophilic factor, von Willebrand factor, avatrombopag, human C1-esterase inhibitor, recombinant factor VIIa, coagulation factor X, conestat alfa
- Examples flagged **Moderate**: metronidazole, tinidazole, naltrexone, rosuvastatin, simvastatin, palifermin, strontium chloride Sr-89.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction scores are high, but the evidence is limited to one mouse cell-line study and indirect or computational papers, with no clinical trials. The top-ranked prediction (CMM7) is not clearly defined, and the other subtypes have specific biological or pharmacological concerns. Melanoma overall is best treated as a research question rather than a candidate for development.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-registered products
- Mechanism of action data
- Clarification of what "CMM7" refers to
- Further preclinical work in human melanoma models, including single-agent carfilzomib and comparison with existing melanoma therapies
- Assessment of carfilzomib exposure in the target tissue (especially central nervous system and uveal sites)
- A review of drug interaction risks, particularly for the major interactions listed above, before any clinical study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

