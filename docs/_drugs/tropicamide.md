---
layout: default
title: Tropicamide
parent: Model Prediction Only (L5)
nav_order: 871
evidence_level: L5
indication_count: 3
---

# Tropicamide
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

# Tropicamide: From Cycloplegia to Cauda Equina Syndrome

## One-Sentence Summary

Tropicamide is a topical antimuscarinic eye drop, originally used for cycloplegia and short-acting pupil dilation (mydriasis) for eye examination.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but **no clinical trials and no publications** currently support this direction. The prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cycloplegia |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, tropicamide is a topical antimuscarinic (anticholinergic) agent. Pharmacology data show it acts on muscarinic receptors M2, M3, M4 and M5, and its efficacy in cycloplegia and mydriasis is established.

The model's link to cauda equina syndrome is probably driven by the shared antimuscarinic drug class and the bladder dysfunction that often follows this condition. Antimuscarinics can reduce detrusor overactivity. However, cauda equina syndrome typically causes an underactive bladder with urinary retention, where anticholinergics would be unhelpful or even harmful.

Tropicamide is also an ophthalmic preparation with minimal systemic exposure, so a plausible systemic mechanism is lacking. The link is purely computational and biologically weak.

Two other predictions were also reviewed, and both have the same evidence level (L5) and a Hold recommendation:
- **Obsolete neurogenic bladder (score 99.13%):** Muscarinic antagonism is a validated mechanism for neurogenic detrusor overactivity, so the class-level rationale is credible. Tropicamide has no bladder-selective profile or established dosing for this use, the disease term is obsolete in the ontology, and better-characterized antimuscarinics already exist.
- **Irritable bowel syndrome (score 99.12%):** Antispasmodic antimuscarinics are used for IBS cramping, which supports a class-level rationale. Tropicamide has no oral or systemic formulation or gastrointestinal data, and approved antispasmodics already cover this niche.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Tropicamide has 14 valid single-ingredient registrations, all ophthalmic eye drops. The approved indication text is not available in the data compiled for this report. The five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 9880 | Ahlmide P Eye Drop | Packet of 5 ml eye drop | Ahlcon Parenterals India Limited |
| 9675 | Appamide 10 mg/5 mg Eye Drop | Packet of 5 ml eye drop | Appasamy Ocular Device Pvt Ltd |
| 215295 | Tropicacyl Eye Drop | Bottle of 5 ml eye drop | Sunways India Pvt Ltd |
| 141425 | Meptrop Eye Drop | Bottle of 5 ml eye drop | Mepfarma India Pvt Ltd |
| 163729 | Optimide Eye Drop | Packet of 5 ml eye drop | Micro Labs Ltd |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** The following conditions are linked to contraindication edges for tropicamide: hypertension and hypertensive disorder, open-angle, angle-closure and closed-angle glaucoma, ocular hypertension, diabetes mellitus, diabetic ketoacidosis, sudden cardiac arrest, heart conduction disease, hyperthyroidism, Graves disease, thyrotoxicosis, myocardial ischemia and coronary artery disease.
- **Drug Interactions:** 10 interacting drugs were identified, but severity levels are unclassified. They are atropine, potassium chloride, vancomycin, simvastatin, prednisolone, famotidine, warfarin, lidocaine, fluconazole and brimonidine. Pharmacology data also list muscarinic receptor binding at M2, M3, M4 and M5.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions for cauda equina syndrome, neurogenic bladder and irritable bowel syndrome have high model scores but no clinical trials or publications. The mechanistic link is weak for an ophthalmic, minimally absorbed drug. For cauda equina syndrome, the likely bladder-retention picture makes an antimuscarinic potentially harmful.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Indian regulatory sources, which are currently missing and block safety screening
- Detailed mechanism of action data (for example from DrugBank)
- Preclinical or pharmacokinetic evidence that a systemically active, safe dose can be achieved for any non-ophthalmic use
- A review of whether the prediction is clinically meaningful for cauda equina syndrome, or whether neurogenic bladder or IBS is a more sensible direction, given that established antimuscarinics already exist for those
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

