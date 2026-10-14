---
layout: default
title: Cyclopentolate
parent: Model Prediction Only (L5)
nav_order: 217
evidence_level: L5
indication_count: 3
---

# Cyclopentolate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Cyclopentolate: From Cycloplegia to Cauda Equina Syndrome

## One-Sentence Summary

Cyclopentolate is a topical anticholinergic eye drop originally used to produce cycloplegia (paralysis of eye focusing muscles) and pupil dilation.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cycloplegia |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, cyclopentolate is a muscarinic antagonist (anticholinergic). It is used in the eye to relax the focusing muscle and dilate the pupil, and its efficacy for cycloplegia is established.

The only conceivable link to cauda equina syndrome is through reduced bladder detrusor activity, since anticholinergics can calm bladder overactivity. However, this link is weak. Cauda equina syndrome is a structural neurological emergency that usually requires surgical decompression. Its typical bladder presentation is urinary retention, which anticholinergics could worsen. In addition, cyclopentolate is marketed only as an ophthalmic solution, with no systemic dosing established.

The high TxGNN score is a computational prediction only and should not be read as clinical support.

### Other Predicted Indications (for context)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Neurogenic bladder (obsolete ontology term) | 99.40% | L5 | Systemic antimuscarinics are established for neurogenic detrusor overactivity, so the mechanism is plausible in principle. Cyclopentolate has no systemic dosing, has CNS toxicity concerns (confusion, seizures, especially in children), and the disease term is obsolete. Better-validated alternatives exist. |
| 3 | Irritable bowel syndrome | 99.27% | L5 | Class-level rationale only (antispasmodics such as dicyclomine and hyoscyamine). No studies of cyclopentolate and no oral formulation. |

## India Market Information

Cyclopentolate is marketed in India with 20 valid single-ingredient registrations, all ophthalmic (eye drops or ophthalmic solutions). Approved indication text was not available for these products.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 42776 | Cyclopen D Eye Drop | 5 ml Eye Drop (packet) | Not available |
| 43571 | Cylate Eye Drop | 5 ml Eye Drop (packet) | Not available |
| 76372 | Eslate Eye Drops | 5 ml Ophthalmic Solution (bottle) | Not available |
| 39143 | Cyclate Eye Drop | 5 ml Eye Drop (packet) | Not available |
| 163305 | Open Eye Drop | 5 ml Eye Drop (bottle) | Not available |

## Safety Considerations

- **Knowledge-graph-listed contraindicated conditions** (from the TxGNN knowledge graph, not label text): angle-closure glaucoma, hypertension, heart disease (including coronary artery disease, sudden cardiac arrest and heart conduction disease), arteriosclerosis and atherosclerosis, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, hyperthyroidism (Graves disease, thyrotoxicosis), brain injury or brain disease, and Down syndrome.
- **Systemic anticholinergic concerns** (from the prediction rationale): CNS effects such as confusion and seizures, especially in children. Relevant to any systemic use, which is not an established route for this drug.

Please refer to the package insert for label warnings and drug interaction information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for cauda equina syndrome has no clinical trial or literature support (Evidence Level L5). The mechanistic link is weak and potentially counterproductive, since anticholinergics may worsen urinary retention. The only available formulation is topical ophthalmic, which is unsuited to systemic use. The other predicted indications (neurogenic bladder, IBS) are likewise unsupported and already served by better-validated drugs.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-marketed products (a blocking gap for safety screening)
- Detailed mechanism of action data
- Any preclinical or clinical evidence for the predicted indication
- A feasibility assessment of a systemic formulation and route, including systemic anticholinergic safety, particularly CNS effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

