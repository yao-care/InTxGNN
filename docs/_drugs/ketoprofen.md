---
layout: default
title: Ketoprofen
parent: Model Prediction Only (L5)
nav_order: 463
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ketoprofen: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Rheumatoid arthritis, osteoarthritis, arthropathy"
monitor_inn: "Ketoprofen"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "pseudoachondroplasia", "WHIM syndrome", "juvenile arthritis due to defect in LACC1"]
---

# Ketoprofen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Ketoprofen: From Rheumatoid Arthritis and Osteoarthritis to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ketoprofen is a non-steroidal anti-inflammatory drug (NSAID) originally used for arthritis conditions such as rheumatoid arthritis and osteoarthritis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. It rests on a model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, osteoarthritis, arthropathy (from the knowledge graph; no approved indication text is available in the India licence records) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, ketoprofen is an NSAID that inhibits cyclooxygenase (COX) enzymes and reduces prostaglandin-mediated inflammation and pain. Its efficacy in arthritis conditions is established.

For the top-ranked prediction, the mechanistic link is **not supported**. Acromesomelic dysplasia, Hunter-Thompson type is a skeletal dysplasia caused by loss-of-function mutations in CDMP1/GDF5. COX inhibition is not expected to correct this genetic defect. The very high TxGNN score (99.98%) is a model output only, with no trial or literature backing.

Several lower-ranked predictions are more coherent with ketoprofen's pharmacology, though none has supporting studies in the data compiled for this report:
- **Spondyloarthropathy, susceptibility to** (score 99.86%): NSAIDs are established first-line symptomatic therapy for spondyloarthritis, making this the most biologically plausible candidate. Class-level evidence should be verified through a dedicated literature search.
- **Juvenile arthritis due to defect in LACC1** (score 99.74%): NSAIDs are commonly used for symptom control in juvenile arthritis, but the link is indirect and symptomatic.
- **Pseudoachondroplasia** (score 99.95%): ketoprofen might relieve joint pain and inflammation, but it would not modify the underlying disease.
- **Myosclerosis** (score 99.98%): a weak, speculative link through symptomatic anti-inflammatory and analgesic effects.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 164666 | Ostofen 50mg Capsule | Strip of 10 capsules | Not stated |
| 115867 | Ketopatch 30mg Transdermal Patch | Packet of 1 transdermal patch | Not stated |
| 116005 | Ketofen 100mg Tablet | Strip of 10 tablets | Not stated |
| 236233 | Vofane 5mg Injection | Vial of 10 ml injection | Not stated |
| 121924 | Lupiflex 8 Tablet | Strip of 10 tablets | Not stated |

A total of 20 valid single-ingredient registrations exist. Formulations include oral capsules and tablets, transdermal patches and plasters, and an injection.

## Safety Considerations

- **Contraindications (from knowledge graph associations, not label text)**: hypertension and hypertensive disorder, liver failure, kidney disease, peptic ulcer disease (including active), blood coagulation disease, myocardial infarction, coronary thrombosis, cardiovascular and heart disease, hemoglobinopathy, pyoureter.
- **Drug Interactions**: 226 interactions were identified in total. Examples from the compiled list:
  - *Moderate*: acetylsalicylic acid, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), metformin, glimepiride, chlorpropamide, mesalazine, balsalazide, naltrexone, potassium citrate and bicarbonate, picosulfuric acid, polyethylene glycol with electrolytes.
  - *Minor*: famotidine, ranitidine, cimetidine, linaclotide.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a model score, with no clinical trials or literature, and no plausible mechanistic link between COX inhibition and the genetic basis of acromesomelic dysplasia, Hunter-Thompson type. The knowledge-graph contraindications (cardiovascular, renal, hepatic, gastrointestinal) also warrant caution.

**To proceed, the following is needed:**
- Mechanism of action data for ketoprofen
- Package insert warnings and contraindications for the Indian market
- A dedicated literature and trial search for the more plausible candidates, especially spondyloarthropathy and LACC1-related juvenile arthritis, which are better suited as research questions than the top-ranked prediction
- Confirmation of the approved indications in the India licence records
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

