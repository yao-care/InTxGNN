---
layout: default
title: Tolmetin
parent: Model Prediction Only (L5)
nav_order: 845
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
monitor_inn: "Tolmetin"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "WHIM syndrome"]
description: "Tolmetin: predicted new indication Acromesomelic dysplasia, Hunter-Thompson type (evidence level L5). Approved use: Not recorded in the local data"
---

# Tolmetin
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

## Tolmetin: Acromesomelic dysplasia, Hunter-Thompson type
{: .text-alpha }

## One-Sentence Summary

Tolmetin is a non-steroidal anti-inflammatory drug (NSAID), originally used to treat rheumatoid arthritis, osteoarthritis and juvenile idiopathic arthritis.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder.
However, **no clinical trials and no publications** currently support this prediction, so it rests on the model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tolmetin is a non-selective COX inhibitor (NSAID). It reduces prostaglandin-mediated inflammation and pain, and its efficacy in arthritic conditions is established.

Acromesomelic dysplasia, Hunter-Thompson type, is a genetic skeletal dysplasia caused by loss-of-function of CDMP1/GDF5. This defect lies in the GDF5/BMP signaling pathway, and COX inhibition has no plausible effect on it. At best, tolmetin could give symptomatic relief of joint pain, which would not modify the disease.

The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or a true pharmacological rationale. The prediction should therefore be treated with caution.

Other top-ranked predictions show a similar pattern:
- **Pseudoachondroplasia (0.9995)**: NSAIDs are used for symptomatic joint pain in these patients, but this is a class effect and not specific to tolmetin.
- **Rheumatoid nodulosis, myosclerosis, brachyolmia and related syndromes, colobomatous microphthalmia-rhizomelic dysplasia syndrome, WHIM syndrome**: weak or no mechanistic link.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 13895 | Amtoril 600mg Tablet (Macleods Pharmaceuticals Pvt Ltd) | Oral, strip of 6 tablets | Not stated in the available data |
| 249942 | Zextra 600mg Tablet (Dr Reddy's Laboratories Ltd) | Oral, strip of 10 tablets | Not stated in the available data |

## Safety Considerations

- **Disease contraindications (from knowledge graph, not label text)**: hypertension and hypertensive disorder, cardiovascular and heart disease, myocardial infarction and coronary thrombosis, liver disease and liver failure, kidney disease, peptic ulcer disease (including active peptic ulcer), blood coagulation disease, gallbladder disease, hemoglobinopathy, pyoureter.
- **Drug Interactions**: 153 interactions were recorded in total. The 20 listed in the data compiled for this report are:
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), acetylsalicylic acid, mesalazine and balsalazide, metformin, the sulfonylureas chlorpropamide and glimepiride, naltrexone, potassium citrate and potassium bicarbonate, picosulfuric acid, and polyethylene glycol (3350 with electrolytes).
  - **Minor**: famotidine, ranitidine, cimetidine, linaclotide.

Package insert warnings and contraindications could not be retrieved; please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trial or literature support (evidence level L5). The disease is caused by a GDF5/BMP signaling defect that COX inhibition does not address, so the high score from the TxGNN model (deep learning) may reflect similarities the model learned between related diseases, not biological evidence. Tolmetin's use here would be limited to symptomatic pain relief.

**To proceed, the following is needed:**
- A confirmed mechanism of action for tolmetin from curated sources such as DrugBank
- Package insert warnings and contraindications from the Indian market labels
- Any clinical or preclinical evidence in this disease (currently none)
- A cardiovascular, gastrointestinal and renal safety assessment for the target population, given the contraindication signals above
- A review of the subtype predictions (rheumatoid factor-positive polyarticular JIA, spondyloarthropathy) as possible extensions of existing indications rather than new repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

