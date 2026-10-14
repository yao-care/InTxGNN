---
layout: default
title: Glimepiride
parent: Model Prediction Only (L5)
nav_order: 394
evidence_level: L5
indication_count: 9
---

# Glimepiride
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

# Glimepiride: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Glimepiride is a sulfonylurea originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, glimepiride is a sulfonylurea that closes K-ATP channels on pancreatic beta cells to stimulate insulin secretion. Its efficacy in type 2 diabetes is established.

No mechanistic link to focal stiff limb syndrome is supported. This condition is closely related to stiff person syndrome, which involves anti-GAD autoimmunity and impaired GABAergic inhibition. Glimepiride has no known action on those pathways. The high score (99.75%) likely reflects shared diabetes/autoimmunity context in the knowledge graph (for example, GAD autoantibodies, which are also seen in type 1 diabetes) rather than a true drug effect.

This should be treated as a hypothesis-generating signal, not clinical evidence.

**Other predicted indications (all L5, Hold, no supporting trials):**

| Rank | Predicted Indication | Score | Note |
|------|------|------|------|
| 2 | Classic stiff person syndrome | 99.75% | Same anti-GAD autoimmunity context; no known glimepiride action on GABAergic pathways |
| 3 | Opsismodysplasia | 99.74% | Speculative link to insulin/PI3K signaling (INPPL1); untested |
| 4 | Thiamine-responsive dysfunction syndrome | 99.73% | Overlap limited to the diabetic phenotype; treatment is thiamine |
| 5–8 | Localized lipodystrophies (drug-induced, centrifugal, pressure-induced, idiopathic) | 99.56–99.62% | Likely reflects lipodystrophy-cluster similarity; no supported mechanism |
| 9 | Pancreatic agenesis | 99.55% | Mechanistically inappropriate, since glimepiride needs functional beta cells |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for the top predicted indication. For the rank 9 prediction (pancreatic agenesis), the only publication found was [PMID 12720536](https://pubmed.ncbi.nlm.nih.gov/12720536/) (2003, European Journal of Endocrinology), a study of endosonographic imaging pitfalls in suspected insulinomas. It is not relevant to treating pancreatic agenesis.

## India Market Information

Glimepiride is marketed in India with 20 valid registrations (all single-entry records, none cancelled). Approved indication text was not available in the data compiled for this report. Five examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 208521 | Supride 2mg Tablet | Strip of 10 tablets | Not specified |
| 100010 | Glimicord M 2 Forte Tablet | Strip of 10 tablets | Not specified |
| 81192 | Ecoglim MV 2mg/500mg/0.2mg Tablet SR | Strip of 10 tablets (SR) | Not specified |
| 246540 | Zoryl M 1 Forte Tablet PR | Strip of 15 tablets (PR) | Not specified |
| 15505 | Adride 4mg Tablet | Strip of 10 tablets | Not specified |

All products are oral formulations. Many are fixed-dose combinations (for example with metformin or voglibose), although they are recorded as single entries.

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: kidney disease, liver disease, gallbladder disease, congestive heart failure, pituitary hormone deficiencies (including hypopituitarism and Sheehan syndrome), hypogonadotropic hypogonadism (including Kallmann syndrome), thymus gland disease, osteoporosis (including postmenopausal), and infectious disease.
- **Drug Interactions**: 599 interacting drugs were identified. Examples at Moderate level include:
  - Beta-agonists and sympathomimetics: phenylephrine, pseudoephedrine, epinephrine, salbutamol, formoterol
  - Beta-blocker: acebutolol
  - NSAIDs: ibuprofen, ketorolac
  - Corticosteroid: hydrocortisone
  - H2 blockers: famotidine, ranitidine
  - Others: acetazolamide, hydrochlorothiazide, ethinylestradiol, ethanol, acitretin, nitazoxanide, albiglutide

  Minor-level examples include topical hydrocortisone and alclometasone.

Package insert warnings and contraindications were not available, so please refer to the package insert for the full safety profile. Hypoglycaemia is a general concern with sulfonylureas, particularly in non-diabetic patients.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications, and no plausible mechanism links glimepiride to focal stiff limb syndrome. The high TxGNN score probably reflects shared diabetes/autoimmunity network context. Treating non-diabetic patients with an insulin secretagogue also carries hypoglycaemia risk without a clear benefit.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications (a blocking gap for safety screening)
- Preclinical or mechanistic evidence for any effect on GABAergic or autoimmune pathways
- A targeted literature search on sulfonylureas in stiff person spectrum disorders
- A route and formulation compatibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

