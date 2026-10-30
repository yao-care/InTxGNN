---
layout: default
title: Lorcaserin
parent: Model Prediction Only (L5)
nav_order: 501
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
description: "Lorcaserin: predicted new indication Hypervitaminosis (evidence level L5). Approved use: Obesity disorder"
monitor_inn: "Lorcaserin"
predicted_indications: ["hypervitaminosis", "proximal 16p11.2 microdeletion syndrome", "obsolete hypertelorism (disease)", "frontorhiny"]
---

# Lorcaserin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Lorcaserin: From Obesity to Hypervitaminosis
{: .text-alpha }

## One-Sentence Summary

Lorcaserin was originally used to treat obesity, including monogenic obesity.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but the data compiled for this report contain **no clinical trials and no publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity disorder; monogenic obesity (the approved indication text in the India license record is blank) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Lorcaserin is generally known as a selective 5-HT2C receptor agonist that reduces appetite, and its efficacy was studied in obesity.

For the top-ranked prediction, hypervitaminosis, no plausible mechanistic link was identified. Hypervitaminosis results from excess vitamin intake or accumulation and is not known to involve serotonergic pathways. The very high score (0.9997) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No trial or literature evidence supports it.

Among the four predictions, the second-ranked one, **proximal 16p11.2 microdeletion syndrome** (score 0.9996), is the most biologically coherent. This syndrome is associated with early-onset obesity, hyperphagia and neurodevelopmental features, which overlaps conceptually with lorcaserin's original indications and with 5-HT2C-mediated appetite regulation. It still has no trial or literature support. The other two predictions, obsolete hypertelorism (0.9991) and frontorhiny (0.9987), are craniofacial structural anomalies with no credible mechanistic link to an appetite-pathway agonist.

Lorcaserin was also withdrawn from the US market in 2020 because of a cancer-risk signal, which would weigh heavily on any new research proposal.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 2724 | Alfence Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets (oral) | Not stated in the license record |

## Safety Considerations

- **Drug Interactions**: 190 interactions were identified in total. The 20 retrieved for this report include these **Major** interactions:
  - Fentanyl
  - Dextromethorphan
  - Tramadol
  - Alfentanil
  - Almotriptan
  - Sumatriptan
  - Amitriptyline
  - Bupropion

  Most of these are opioids, triptans and serotonergic or antidepressant drugs, which fits a serotonergic agent. **Moderate** interactions include acarbose, metformin, pioglitazone, alogliptin, albiglutide (glucose-lowering drugs), chlorpheniramine, codeine, alprostadil, amphetamine, aripiprazole, asenapine and atomoxetine.

Please refer to the package insert for other safety information (warnings and contraindications).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All four predicted indications rest only on model scores, with no clinical trials or literature (evidence level L5). Hypervitaminosis has no plausible mechanistic link, and the market withdrawal of lorcaserin in the US adds a significant safety concern.

**To proceed, the following is needed:**
- The package insert (warnings and contraindications) for Alfence Tablet, which is a blocking gap for safety screening
- Detailed mechanism of action data, from DrugBank
- If any indication is pursued, consider 16p11.2 microdeletion syndrome first, with a targeted literature and trial search and a review of the cancer-risk signal
- Confirmation of the approved indication text for the India license
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

