---
layout: default
title: Hydroxocobalamin
parent: 僅模型預測 (L5)
nav_order: 410
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Hydroxocobalamin: From Vitamin B12 Therapy to Esophageal Varices

## One-Sentence Summary

Hydroxocobalamin is a cobalamin (vitamin B12) analog whose original approved indications are not documented in this evidence pack. The TxGNN model predicts potential relevance to **esophageal varices** (both with and without bleeding), based on the drug's known nitric oxide (NO)-scavenging property, but this prediction is currently supported by **no clinical trials and no published literature**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in evidence pack (no approved indications or licenses on record; MOA is a data gap) |
| Predicted New Indication | Esophageal Varices without Bleeding (rank 1); Esophageal Varices with Bleeding (rank 2, same score) |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Hydroxocobalamin in this evidence pack (original indications and MOA are both marked as data gaps). Based on established pharmacology, hydroxocobalamin is a cobalamin derivative known for its ability to scavenge nitric oxide (NO), a property already exploited clinically in vasodilatory shock states.

The TxGNN rationale links this NO-scavenging activity to the pathophysiology of portal hypertension: in cirrhosis, excess splanchnic NO production drives vasodilation and increased portal blood flow, which contributes to the formation and progression of esophageal varices. Reducing NO activity could theoretically lower splanchnic vasodilation and portal pressure, which is the mechanistic thread connecting hydroxocobalamin to both predicted indications (varices with and without bleeding).

This link is, however, purely theoretical — it has not been tested in any preclinical or clinical study specific to portal hypertension or esophageal varices. For the "with bleeding" indication in particular, the rationale itself flags an added concern: variceal hemorrhage is an acute emergency requiring rapid hemostasis (endoscopic therapy, octreotide/terlipressin), and hydroxocobalamin's systemic vasoconstrictive effects in an actively bleeding, hemodynamically unstable patient are of unknown safety.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions** (from DDI database, 32 total interactions on record; moderate-level interactions identified):

| Interacting Drug | Level |
|---|---|
| Arsenic trioxide | Moderate |
| Chloramphenicol | Moderate |
| Iodide I-131 | Moderate |
| Iodide I-123 | Moderate |

The remaining ~28 interactions (e.g., Omeprazole, Simvastatin, Folic acid, Levothyroxine, Acetylsalicylic acid) are recorded with "Unknown" severity level in the source database — clinical significance cannot be determined from this data alone.

Key warnings and contraindications from the product label are not currently available (flagged as a **Blocking** data gap — TFDA label has not yet been retrieved and parsed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications sit at Evidence Level L5 (model prediction only) with zero supporting clinical trials or literature, and the underlying mechanistic link is speculative and untested. Compounding this, a **Blocking** data gap exists on TFDA label warnings/contraindications, which by itself prevents this candidate from entering the S1 safety review stage.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a Blocking gap
- Original approved indication(s) and mechanism of action (DrugBank) — currently a High-severity gap
- Preclinical or mechanistic studies directly testing NO-scavenging effects on portal pressure/variceal outcomes
- Clinical safety data on hydroxocobalamin's vasoconstrictive effects in hemodynamically unstable (actively bleeding) patients, specifically for the "with bleeding" indication
- Route compatibility assessment (available vs. required administration routes — currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

