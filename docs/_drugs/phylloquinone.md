---
layout: default
title: Phylloquinone
parent: Model Prediction Only (L5)
nav_order: 668
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-30
monitor_inn: "Phylloquinone"
predicted_indications: ["renal tubular acidosis", "hypophosphatemic rickets", "Pendred syndrome", "autosomal recessive nonsyndromic deafness", "leukocyte adhesion deficiency", "Fraser syndrome", "temtamy preaxial brachydactyly syndrome"]
description: "Phylloquinone: predicted new indication Renal tubular acidosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Phylloquinone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Phylloquinone: Renal tubular acidosis
{: .text-alpha }

## One-Sentence Summary

Phylloquinone (vitamin K1) was originally associated with bone and mineral metabolism conditions such as osteoporosis, hypercalcemia, nephrocalcinosis and congenital prothrombin deficiency.
The TxGNN model predicts it may be effective for **renal tubular acidosis**,
but currently there are **0 clinical trials** and **0 publications** supporting this prediction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Renal tubular acidosis |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (14 of 14) – CDSCO approval status is not included in this data |
| Number of Registrations | 14 (valid: 14) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, phylloquinone is a cofactor for gamma-glutamyl carboxylase, which activates vitamin K-dependent proteins such as osteocalcin and matrix Gla protein (MGP). MGP inhibits soft-tissue calcification.

There is a plausible but indirect connection to renal tubular acidosis: nephrocalcinosis, which is already among phylloquinone's associated conditions, is a common complication of distal renal tubular acidosis. However, vitamin K has no known effect on the underlying acid-base transport defect. The very high TxGNN score most likely reflects network proximity to the existing calcium and phosphate-related indications rather than a true therapeutic mechanism.

Other lower-ranked predictions show the same pattern, with weak or no mechanistic support:

| Rank | Predicted Disease | Score | Assessment |
|------|------|------|------|
| 2 | Hypophosphatemic rickets | 0.9967 | Indirect bone-mineral link; the main defect (FGF23-mediated phosphate wasting) is not addressed by vitamin K |
| 3 | Pendred syndrome | 0.9956 | No clear mechanism; likely a network artifact |
| 4 | Autosomal recessive nonsyndromic deafness | 0.9951 | No plausible mechanism |
| 6 | Leukocyte adhesion deficiency | 0.9947 | Weak and indirect; bleeding defect is not vitamin K-responsive |
| 8 | Fraser syndrome | 0.9922 | No mechanistic rationale |
| 9 | Temtamy preaxial brachydactyly syndrome | 0.9908 | Very indirect skeletal-development association |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Phylloquinone has 14 valid single-ingredient registrations in India and none cancelled. Approved indication text is not listed for these products. The main authorizations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 116181 | Kip 1mg Injection | Vial of 1 ml injection | Not stated |
| 242409 | Weldion 1mg Injection | Vial of 0.5 ml injection | Not stated |
| 116313 | Kip 10mg Injection | Vial of 1 ml injection | Not stated |
| 116164 | Kenadion 1mg Tablet | Strip of 10 tablets | Not stated |
| 177989 | Phyto K1 5mg Tablet | Strip of 10 tablets | Not stated |

Available routes include both injectable and oral (tablet) forms.

## Safety Considerations

No package insert warnings or contraindications are available in the data compiled for this report. Please refer to the package insert for safety information.

- **Disease contraindications from the knowledge graph** (these are graph associations, not label text): kidney disease, sarcoidosis, diabetes mellitus, diabetic ketoacidosis, hyperparathyroidism, hypercalcemia, nephrocalcinosis, nephrolithiasis, hyperphosphatemia, hypervitaminosis, prostate cancer, female breast carcinoma, cervical cancer, endometrial cancer, lytic metastatic bone lesions, and others. Several of these overlap with renal and mineral disorders relevant to the predicted indication, so they warrant careful review.
- **Drug Interactions**: 152 interactions were identified. The ones listed in the compiled data include:
  - Minor: mineral oil, orlistat (both may reduce absorption of fat-soluble vitamins)
  - Severity not classified: pantoprazole, omeprazole, lansoprazole, famotidine, morphine, epinephrine, amphotericin B, hydrocortisone, prednisone, loperamide, ondansetron, metronidazole, aspirin, sucralfate, vancomycin, lactulose, simvastatin, nystatin

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no registered clinical trials or publications (Evidence Level L5). The mechanistic link to renal tubular acidosis is indirect, since vitamin K does not act on the acid-base transport defect. Safety data from package inserts are also missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India products, which are a blocking gap for safety screening
- Detailed mechanism of action data from DrugBank
- A literature and trial search specific to vitamin K in renal tubular acidosis, especially its effect on nephrocalcinosis
- Review of the knowledge-graph contraindications (kidney disease, hypercalcemia, nephrocalcinosis) against the target population
- Assessment of similarity to the original indications and of route compatibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

