---
layout: default
title: Azathioprine
parent: Model Prediction Only (L5)
nav_order: 84
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Azathioprine: predicted new indication Colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). Approved use: Rheumatoid arthritis"
---

# Azathioprine
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

# Azathioprine: From Rheumatoid Arthritis to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Azathioprine is an immunosuppressant (a purine antimetabolite) originally used for rheumatoid arthritis.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, a rare developmental malformation syndrome,
but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis |
| Predicted New Indication | Colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, azathioprine is a thiopurine immunosuppressant, and its efficacy in rheumatoid arthritis and other immune-mediated conditions is established.

For this specific prediction, however, no plausible mechanistic link could be identified. The predicted condition is a rare developmental malformation syndrome. Azathioprine's immunosuppressive, purine-antimetabolite action has no known relevance to its underlying biology. The very high TxGNN score (99.999%) therefore appears to be an artifact of the graph-based model, not a signal supported by clinical or literature data.

**Better-supported predictions for this drug:** The same analysis also produced predictions with real clinical evidence, namely **inflammatory bowel disease** (25 trials and 20 publications retrieved) and **ulcerative colitis** (15 trials and 20 publications retrieved, including several Cochrane reviews). Both are already established uses of azathioprine, so their novelty as repurposing is limited. They would be better candidates for further evaluation than the top-ranked prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Azathioprine is marketed in India as single-ingredient oral tablets, with 20 valid registrations and none cancelled. The registrations listed in the compiled data carry no approved-indication text. Five of them are shown below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 11651 | Azatoz 50mg Tablet | Strip of 10 tablets | Cytoz Pharmaceuticals |
| 7004 | Azawan Tablet | Strip of 10 tablets | Rowan Bioceuticals Pvt Ltd |
| 3093 | Aprin 50mg Tablet | Strip of 10 tablets | Aegis Pharmaceuticals |
| 11695 | Azoalfa 50 Tablet | Strip of 10 tablets | Alniche Life Sciences Pvt Ltd |
| 234855 | Vaprin Tablet | Strip of 10 tablets | Zydus Cadila |

## Safety Considerations

- **Conditions flagged as contraindication-related in the knowledge graph** (not drawn from label text): pancreatitis, thrombocytopenia, anaemia (including macrocytic anaemia), impaired renal function, infectious disease (including fungal infection and dermatophytosis), lymphoma (including primary CNS lymphoma, lymphosarcoma and hepatosplenic T-cell lymphoma), hepatic vein thrombosis and Budd-Chiari syndrome.
- **Drug Interactions:** 447 interactions were recorded. The main moderate-level ones are the aminosalicylates **mesalazine, balsalazide, olsalazine and sulfasalazine**. Minor interactions include zinc salts (acetate, gluconate, sulfate).
- **Considerations for the predicted indication:** Azathioprine's myelosuppressive effects and infection risk have no offsetting mechanistic benefit in this condition.

Please also refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (Evidence Level L5) and no plausible mechanistic link to azathioprine's action. The high model score appears to be a graph-based artifact, and the safety profile offers no compensating benefit.

**To proceed, the following is needed:**
- Any mechanistic or preclinical rationale connecting purine antimetabolite immunosuppression to this syndrome's pathophysiology
- Detailed mechanism of action data for azathioprine
- Package insert warnings and contraindications for the India-marketed products
- Consideration of redirecting evaluation to the better-supported inflammatory bowel disease and ulcerative colitis predictions, with TPMT/NUDT15 genotyping and blood count and liver monitoring as guardrails
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

