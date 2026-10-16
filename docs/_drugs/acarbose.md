---
layout: default
title: Acarbose
parent: Model Prediction Only (L5)
nav_order: 15
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Acarbose: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Acarbose"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Acarbose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Acarbose: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome

## One-Sentence Summary

Acarbose is an intestinal alpha-glucosidase inhibitor, originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**,
but **no clinical trials and no related publications** currently support this prediction, so it remains a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acarbose is an alpha-glucosidase inhibitor that acts in the gut, slowing carbohydrate digestion and reducing post-meal blood glucose rises. Its efficacy in type 2 diabetes is established.

A plausible mechanistic link to stiff person syndrome is not evident. Stiff person syndrome is an autoimmune neurological disorder involving the GABAergic system and anti-GAD65 antibodies. The only conceivable connection is that GAD-antibody-related autoimmune diabetes can co-occur with it. That is an association between diseases, not evidence that acarbose treats the neurological condition. The high score most likely reflects proximity in the knowledge graph rather than true biology.

The next-ranked predictions show the same pattern:

- **Focal stiff limb syndrome** (99.65%): likely driven by its proximity to stiff person syndrome. No mechanism has been identified.
- **Thiamine-responsive dysfunction syndrome** (99.62%): overlaps with diabetes, but acarbose would not address the underlying thiamine transporter defect.
- **Opsismodysplasia** (99.62%): a rare skeletal dysplasia with no recognised link to glucosidase inhibition.
- **Localized lipodystrophies** (99.17% to 99.25%): any link would be indirect, via glucose and lipid metabolism.
- **Pancreatic agenesis** (99.16%): the only prediction with retrieved literature, but none of it is disease-specific. Patients need insulin and enzyme replacement, which acarbose cannot replace.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top-ranked prediction (classic stiff person syndrome).

Literature was retrieved only for the ninth-ranked prediction, pancreatic agenesis. It is general diabetes material, and none of it evaluates acarbose in that condition. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21697254](https://pubmed.ncbi.nlm.nih.gov/21697254/) | 2011 | Review | J Clin Endocrinol Metab | Preserving β-cell function as the key to preventing progression from prediabetes to type 2 diabetes |
| [9506190](https://pubmed.ncbi.nlm.nih.gov/9506190/) | 1998 | Review | Adv Intern Med | Overview of type 2 diabetes and its metabolic abnormalities |
| [12877088](https://pubmed.ncbi.nlm.nih.gov/12877088/) | 2003 | Review | Nihon Rinsho | Alpha-glucosidase inhibitors for postprandial hyperglycaemia in hypertensive type 2 diabetes |
| [15449970](https://pubmed.ncbi.nlm.nih.gov/15449970/) | 2004 | Review | Am J Cardiovasc Drugs | Links between heart failure and impaired glucose metabolism |
| [10094112](https://pubmed.ncbi.nlm.nih.gov/10094112/) | 1999 | Preclinical (animal study) | Metabolism | Acarbose prevented and reversed metabolic abnormalities in the OLETF diabetic rat |
| [30572448](https://pubmed.ncbi.nlm.nih.gov/30572448/) | 2018 | Case report | Medicine | Three cases of insulin autoimmune syndrome |
| [34562871](https://pubmed.ncbi.nlm.nih.gov/34562871/) | 2021 | Case report | Diabetes Metab Syndr | Continuous glucose monitoring and rituximab in insulin autoimmune syndrome |

## India Market Information

Twenty single-ingredient registrations are valid. All are oral tablets (strips of 10). The data compiled for this report contain no approved indication text. Five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 94291 | Glucobay 25 Tablet (Bayer Zydus Pharma) | Strip of 10 tablets | Not available |
| 6328 | AC 50mg Tablet (USV Ltd) | Strip of 10 tablets | Not available |
| 13805 | Acarjohn 25 Tablet (Johnlee Pharmaceuticals) | Strip of 10 tablets | Not available |
| 59993 | DavaIndia Acarbose 25mg Tablet (Davaindia Generic Pharmacy) | Strip of 10 tablets | Not available |
| 24270 | Acarwin 50mg Tablet (Intra Labs India) | Strip of 10 tablets | Not available |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (not label text): kidney disease, pyoureter, liver disease, gallbladder disease, cirrhosis of liver, inflammatory bowel disease, hypoglycemia, and injury.
- **Drug Interactions**: 371 interactions were recorded. The first 20 reviewed include these moderate-level ones:
  - Acetazolamide
  - Salbutamol
  - Aloe Vera Leaf
  - Alpelisib
  - Amprenavir
  - Aripiprazole
  - Asenapine
  - Asparaginase (both forms)
  - Atazanavir
  - Bedaquiline
  - Bendroflumethiazide
  - Benzphetamine
  - Benzthiazide
  - Betamethasone

  Minor-level ones include albiglutide, alclometasone (topical), lipoic acid, amcinonide, and anisindione.

Please also refer to the package insert for the full safety profile. Label warnings and contraindications were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score. There are no clinical trials or publications for classic stiff person syndrome. Acarbose acts in the gut, and no plausible mechanism links it to this autoimmune neurological disorder. The other top-ranked predictions have the same weakness.

**To proceed, the following is needed:**
- Mechanism of action data for acarbose (for example, from DrugBank)
- Package insert warnings and contraindications from the India regulatory source, needed for safety screening
- Any preclinical or clinical rationale linking alpha-glucosidase inhibition to stiff person syndrome or the GABAergic/anti-GAD65 pathway
- A systematic literature search specific to acarbose and each predicted disease before reconsidering
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

