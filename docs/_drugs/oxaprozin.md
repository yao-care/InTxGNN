---
layout: default
title: Oxaprozin
parent: Model Prediction Only (L5)
nav_order: 626
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
description: "Oxaprozin: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis…"
monitor_inn: "Oxaprozin"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Oxaprozin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Oxaprozin: From Rheumatoid Arthritis to Acromesomelic Dysplasia, Hunter-Thompson Type
{: .text-alpha }

## One-Sentence Summary

Oxaprozin is a non-steroidal anti-inflammatory drug (NSAID) originally used to treat rheumatoid arthritis, osteoarthritis and related joint conditions.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, juvenile idiopathic arthritis, spondyloarthropathy (the Indian licence record contains no indication text) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Oxaprozin is an NSAID, and NSAIDs act by inhibiting cyclooxygenase (COX) and reducing prostaglandin-mediated inflammation and pain. Its efficacy in inflammatory and degenerative joint disease is established.

Hunter-Thompson type acromesomelic dysplasia is a rare skeletal dysplasia caused by mutations in the CDMP1/GDF5 gene, which disrupt bone growth signalling. No plausible mechanistic link between COX inhibition and GDF5 signalling or the underlying bone growth defect has been established. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, rather than a pharmacological rationale. At best, an NSAID might offer symptomatic joint pain relief, which is not disease modification.

**Other predictions in the top 10** follow a similar pattern:
- Most are rare skeletal or developmental syndromes (brachyolmia-amelogenesis imperfecta syndrome, myosclerosis, brachyolmia, pseudoachondroplasia, colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome), with no plausible mechanism and no evidence.
- Three are close to existing indications: spondyloarthropathy susceptibility, rheumatoid nodulosis, and rheumatoid factor-positive polyarticular juvenile idiopathic arthritis. These are biologically plausible but largely extend the scope of indications Oxaprozin already covers, so they are not true repurposing. They were rated L4 (indirect evidence) and labelled "Research Question".

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 142210 | Macprox 600gm Tablet (Macleods Pharmaceuticals Pvt Ltd) | Strip of 10 tablets (oral) | Not stated in the record |

## Safety Considerations

- **Disease associations flagged as contraindications in the knowledge graph** (not label text): hypertension and hypertensive disorder, liver failure, kidney disease, active peptic ulcer disease, blood coagulation disease, myocardial infarction, coronary thrombosis, cardiovascular and heart disease, hemoglobinopathy, and pyoureter.
- **Drug Interactions**: 190 interactions were identified. Those shown in the compiled data include:
  - **Moderate**: acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), mesalazine, balsalazide, metformin, chlorpropamide, acetohexamide, exenatide, fenfluramine, dexfenfluramine, potassium citrate, picosulfuric acid, and polyethylene glycol with electrolytes.
  - **Minor**: famotidine, ranitidine, cimetidine.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported only by the TxGNN score. There are no trials or publications, and no plausible mechanistic link exists between COX inhibition and the GDF5-related skeletal defect. The safety profile of chronic NSAID use in patients with a rare, likely paediatric skeletal disorder has also not been assessed.

**To proceed, the following is needed:**
- Mechanism of action data for Oxaprozin (e.g., from DrugBank)
- Package insert warnings and contraindications for the Indian product
- Preclinical or mechanistic evidence linking Oxaprozin to GDF5 signalling or skeletal development
- If a related direction is of interest, prioritise the near-indication predictions as indication-scope extensions, supported by subtype-specific data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

