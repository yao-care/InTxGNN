---
layout: default
title: Leucovorin
parent: Model Prediction Only (L5)
nav_order: 480
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-31
description: "Leucovorin: predicted new indication Primary hyperoxaluria (evidence level L5). Approved use: Megaloblastic anemia"
monitor_inn: "leucovorin"
predicted_indications: ["primary hyperoxaluria", "congenital intrinsic factor deficiency"]
---

# Leucovorin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Leucovorin: From Megaloblastic Anemia to Primary Hyperoxaluria
{: .text-alpha }

## One-Sentence Summary

Leucovorin (calcium folinate) is a reduced folate originally used to treat megaloblastic anemia.
The TxGNN model predicts it may be effective for **primary hyperoxaluria**,
but there are currently **no clinical trials and no publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Megaloblastic anemia |
| Predicted New Indication | Primary hyperoxaluria |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, leucovorin is a reduced folate (folinic acid). It bypasses dihydrofolate reductase and supports one-carbon metabolism and nucleotide synthesis. Its efficacy in megaloblastic anemia is established, where it restores folate-dependent blood cell production.

Primary hyperoxaluria is an inherited disorder of glyoxylate metabolism (for example, defects in AGXT, GRHPR or HOGA1) that causes the body to overproduce oxalate. A link between this pathway and folate-dependent metabolism is not established in the data compiled for this report. The high TxGNN score is therefore a statistical, model-based signal and should not be read as clinical support.

A second prediction, **congenital intrinsic factor deficiency** (score 0.9934), has a more plausible rationale. This condition causes vitamin B12 malabsorption, which leads to megaloblastic anemia, the original indication. Leucovorin could partly relieve the blood-related signs. However, it does not correct B12 deficiency and may mask haematological signs while neurological damage progresses, so parenteral B12 replacement remains essential. This prediction also has no trials or literature behind it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Leucovorin has 20 valid single-ingredient registrations in India and none cancelled. Approved indication text was not available for these products. The main authorizations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 36874 | Calcium Folinate Injection (Fresenius Kabi India) | Vial of 5 ml injection | Not specified |
| 123463 | Leutero 50mg Injection (Hetero Drugs) | Vial of 5 ml injection | Not specified |
| 231760 | Unifolin 15mg Injection (United Biotech) | Vial of 2 ml injection | Not specified |
| 27439 | Biovorin 15mg Injection (Biochem Pharmaceutical) | Vial of 2 ml injection | Not specified |
| 121371 | Leucorin Tablet (Samarth Life Sciences) | Strip of 10 tablets | Not specified |

Most products are injections. Oral tablets are also registered (Leucorin Tablet and Biovorin 15 Tablet).

## Safety Considerations

- **Disease-level contraindications (from the knowledge graph, not label text)**: vitamin B12 deficiency and pernicious anemia. Folate can correct the blood picture while neurological damage from B12 deficiency continues.
- **Drug Interactions**: 291 interactions were recorded. The main ones with a rated severity are:
  - Pancrelipase: Moderate
  - Sulfasalazine: Minor
  
  Many other entries (for example calcitriol, pantoprazole, glimepiride, mesalazine, doxycycline, metformin, omeprazole, morphine and vancomycin) have no severity rating.

Please refer to the package insert for further warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for primary hyperoxaluria rests only on a model score. No clinical trials or publications support it, and no mechanistic link to folate metabolism is established. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data for leucovorin, to enable a mechanistic-link analysis
- Package insert warnings and contraindications from Indian sources, which are required before safety screening
- A literature and trial search for a biological connection between folate pathways and oxalate metabolism
- Preclinical or mechanistic studies to establish plausibility
- For congenital intrinsic factor deficiency: a clinical assessment of whether leucovorin adds anything beyond B12 replacement, given the masking risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

