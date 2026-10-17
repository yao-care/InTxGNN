---
layout: default
title: Nimotuzumab
parent: Model Prediction Only (L5)
nav_order: 597
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Nimotuzumab: predicted new indication Diabetic cataract (evidence level L5). Approved use: Not listed in the available licence data"
monitor_inn: "Nimotuzumab"
predicted_indications: ["diabetic cataract", "diabetes mellitus type 2 associated cataract", "craniostenosis cataract", "tetanic cataract", "mature cataract", "immature cataract", "cortical cataract", "nuclear senile cataract", "senile cataract", "diabetic retinopathy"]
---

# Nimotuzumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Nimotuzumab: From an Unspecified Original Indication to Diabetic Cataract

## One-Sentence Summary

Nimotuzumab is an anti-EGFR monoclonal antibody that is marketed in India, but the data compiled for this report do not list an approved indication.
The TxGNN model predicts it may be effective for **diabetic cataract**, with a score of 98.6%.
There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the available licence data |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.62% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Nimotuzumab is known to be an anti-EGFR (epidermal growth factor receptor) monoclonal antibody, and this class of drug blocks EGFR-driven cell growth signalling.

The proposed link to diabetic cataract is loose. EGFR signalling has been implicated in lens epithelial cell proliferation and migration, and in posterior capsule opacification. In a hyperglycaemic setting, growth-factor signalling could plausibly contribute to lens changes.

There are important weaknesses:
- The TxGNN score is a computational prediction only, and no clinical or literature evidence supports it.
- A systemic IgG1 antibody is poorly suited to reach the avascular lens, and there is no evidence of ocular delivery.
- Several other top-ranked predictions are other cataract types (type 2 diabetes-associated, craniostenosis, tetanic, mature, immature, cortical, nuclear senile and senile cataract). They share the same score range and likely reflect similarity among cataract terms in the knowledge graph rather than separate biological links. Of these, the type 2 diabetes-associated cataract overlaps substantially with diabetic cataract.
- Among the ten predictions, **diabetic retinopathy** (score 98.33%) is the most biologically plausible, because EGFR signalling interacts with VEGF pathways and may contribute to retinal angiogenesis and inflammation. It is still hypothetical and would first need a preclinical research question.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 26825 | Biomab 50mg Injection | Vial of 1 injection | Not stated in the available data |
| Registration No. 26908 | Biomab Egfr Injection 10ml | Packet of 4 injections | Not stated in the available data |

Both registrations are valid single-ingredient products from Biocon.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-EGFR monoclonal antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. Hypomagnesaemia is a known adverse effect of anti-EGFR antibodies, so electrolytes (magnesium, calcium) would be reasonable to monitor |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

One point relevant to the predicted indications: hypomagnesaemia is a known adverse effect of anti-EGFR antibodies. It could potentially worsen calcium homeostasis, which is relevant to tetanic (hypocalcaemic) cataract.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials or publications (Evidence Level L5). A systemic antibody is also poorly suited to reach the lens, and no ocular delivery evidence exists.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India licence documents, which are required before any safety screening
- Detailed mechanism of action data
- The approved indication text for the existing licences
- Preclinical evidence for EGFR involvement in lens or retinal disease models
- Evidence of ocular delivery feasibility (e.g. intravitreal route) and ocular safety
- Consideration of diabetic retinopathy as a more plausible research direction than the cataract indications, compared against the anti-VEGF standard of care
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

