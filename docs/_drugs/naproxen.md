---
layout: default
title: Naproxen
parent: Model Prediction Only (L5)
nav_order: 579
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Naproxen: From Inflammatory and Musculoskeletal Pain Conditions to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a non-steroidal anti-inflammatory drug (NSAID) originally used for conditions such as rheumatoid arthritis, osteoarthritis, ankylosing spondylitis, gout, bursitis, tendinitis and migraine.
The TxGNN model predicts it may be effective for **brachydactyly-syndactyly syndrome**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bursitis, rheumatoid arthritis, ankylosing spondylitis, tendinitis, gout, migraine, osteoarthritis and related conditions (the approved indication text in the India licences is blank) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Naproxen is generally known as a non-selective COX inhibitor with anti-inflammatory and analgesic effects, and its efficacy in inflammatory joint and pain conditions is established.

Brachydactyly-syndactyly syndrome, however, is a congenital skeletal malformation with a developmental and genetic basis. Blocking prostaglandin synthesis is not expected to correct a structural limb patterning defect, so no mechanistic link is supported by the available data. The high score (99.35%) most likely reflects network proximity in the knowledge graph (for example, to skeletal and joint-related terms among naproxen's original indications) rather than a true therapeutic relationship.

The other three top-ranked predictions show the same pattern. All are rare congenital developmental syndromes, with no trials or literature:
- Colobomatous microphthalmia-rhizomelic dysplasia syndrome (99.22%)
- Acromesomelic dysplasia, Hunter-Thompson type (99.17%)
- Brachyolmia-amelogenesis imperfecta syndrome (99.06%)

At most, naproxen might relieve joint pain symptomatically in some of these patients, which is not a repurposing claim.

## India Market Information

Naproxen has 20 valid single-ingredient registrations and no cancelled ones. The data compiled for this report do not include approved indication text for these products. Main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 244550 | Xenap 250 Tablet | Strip of 10 tablets | Not stated |
| 153983 | Nalyxan 250mg Tablet | Strip of 10 tablets | Not stated |
| 152315 | Napsea Tablet | Strip of 10 tablets | Not stated |
| 151203 | Naprosyn 125mg Suspension | Bottle of 60 ml suspension | Not stated |
| 150316 | Naxdom 250 Tablet | Strip of 15 tablets | Not stated |

Available forms are oral tablets and an oral suspension. Several registrations are fixed-dose products, although the data classify all as single-ingredient (for example, the "D" and "250mg/10mg" products).

## Safety Considerations

- **Contraindications / disease associations (knowledge graph, not label text)**: Naproxen is linked to the following conditions, grouped by area:
  - Cardiovascular: hypertension, congestive heart failure, coronary artery disease, coronary atherosclerosis, myocardial infarction, coronary thrombosis, stroke, cerebrovascular disorder, cerebral infarction
  - Liver and kidney: liver failure, liver disease, kidney disease, gallbladder disease
  - Metabolic: diabetes mellitus, diabetic ketoacidosis, obesity, osteoporosis
  - Blood: blood coagulation disease, anaemia, hemoglobinopathy
  - Other: epilepsy, benign prostatic hyperplasia, substance abuse/dependence
- **Drug Interactions**: 309 interactions are recorded. The 20 listed in the data are all Moderate-level and include:
  - Acid-lowering agents: famotidine, ranitidine, cimetidine, rabeprazole, dexlansoprazole
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
  - Other: acetylsalicylic acid, metformin, chlorpropamide, mesalazine, balsalazide, aprepitant, potassium citrate, potassium bicarbonate

Please refer to the package insert for warnings and formal contraindications, as label-based data were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (L5), with no clinical trials or publications, and there is no plausible mechanistic link between COX inhibition and correcting a congenital skeletal malformation. The cardiovascular, renal, hepatic and gastrointestinal risk profile of naproxen further weakens any case for use in this setting.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) and a documented rationale linking it to the disease's biology
- Any preclinical, case-based or clinical evidence in this or related syndromes
- Package insert warnings and contraindications for the India products
- Route and formulation compatibility assessment
- Confirmation of whether any benefit would be only symptomatic (joint pain) rather than disease-modifying
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

