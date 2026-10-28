---
layout: default
title: Benzydamine
parent: Model Prediction Only (L5)
nav_order: 101
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Benzydamine: predicted new indication Benign prostatic hyperplasia (evidence level L5). Approved use: Not stated in the registration records compiled for this report"
monitor_inn: "Benzydamine"
predicted_indications: ["benign prostatic hyperplasia (disease)"]
---

# Benzydamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Benzydamine: From Local Oral and Throat Use to Benign Prostatic Hyperplasia
{: .text-alpha }

## One-Sentence Summary

Benzydamine is marketed in India mainly as a mouthwash, gargle and dental gel product.
The TxGNN model predicts it may be effective for **benign prostatic hyperplasia (BPH)**, but **no clinical trials and no publications** currently support this direction, so the prediction is computational only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records compiled for this report (the approved indication text is blank for all licenses; products are oral rinses, gargles and a dental gel) |
| Predicted New Indication | Benign prostatic hyperplasia |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general background knowledge (not from the supplied data), benzydamine is a locally acting NSAID with anti-inflammatory, analgesic and local anaesthetic properties. These are thought to involve reduced pro-inflammatory cytokines such as TNF-alpha and IL-1beta, together with membrane-stabilising effects.

A possible link to the new indication is that inflammation is believed to contribute to prostatic enlargement and lower urinary tract symptoms, so an anti-inflammatory agent could plausibly be relevant. This link is speculative. The very high TxGNN score reflects a model prediction only, and it has not been tested in preclinical or clinical studies.

There is also a practical gap: all Indian products are mouth, throat or dental formulations. No route of administration suitable for prostatic disease has been identified, and route compatibility has not yet been assessed.

## India Market Information

Benzydamine has 20 valid single-ingredient registrations in India, with no cancelled licenses. The approved indication text is not recorded for any of them. Main examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 31318 | Bensodyl 7.5mg/6mg Mouth Wash | Mouth wash, 100 ml bottle | Not recorded |
| 59047 | Dresin Mouthwash & Gargle | Gargle, 100 ml bottle | Not recorded |
| 216902 | Tantum Gel | Dental gel, 20 g tube | Not recorded |
| 215239 | Tantum Oral rinse | Mouth wash, 120 ml bottle | Not recorded |
| 29594 | Benzyda 0.15% Mouth Wash | Mouth wash, 200 ml bottle | Not recorded |

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction records were available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it is the only support. There are no clinical trials or publications for BPH, the mechanism data are missing, and all marketed products are oral or topical formulations with no clear route for a prostatic indication.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) to test the proposed anti-inflammatory link to BPH
- Package insert warnings and contraindications from the India regulator, needed before any safety screening
- Preclinical or early clinical evidence of benefit in BPH or lower urinary tract symptoms
- Assessment of whether a suitable route or formulation exists for prostatic delivery, given that current products are local oral and dental forms
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

