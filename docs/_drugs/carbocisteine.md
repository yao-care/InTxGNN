---
layout: default
title: Carbocisteine
parent: 僅模型預測 (L5)
nav_order: 146
evidence_level: L5
indication_count: 1
---

# Carbocisteine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Carbocisteine: From Mucolytic Therapy to Gout

## One-Sentence Summary

Carbocisteine is a cysteine-derived mucolytic agent conventionally used to reduce viscosity of airway secretions in respiratory conditions.
The TxGNN model predicts it may be effective for **Gout**,
with a prediction score of **99.67%** — however, there are currently **no clinical trials** and **no publications** directly supporting this repurposing direction.
This prediction is currently model-only (Evidence Level L5), and independent mechanistic plausibility remains speculative.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mucolytic agent for respiratory tract disorders (no India regulatory record) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 — Model prediction only, no actual studies |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, Carbocisteine (S-carboxymethyl-L-cysteine) is a cysteine derivative with a sulfur-containing backbone. Its established role is as a mucolytic agent that modifies the physicochemical properties of mucus secretions, primarily used in chronic obstructive pulmonary disease (COPD) and bronchitis.

The mechanistic link to gout proposed by the TxGNN knowledge graph is theoretically threefold: (1) **antioxidant activity** — the cysteine scaffold may scavenge reactive oxygen species (ROS) induced by monosodium urate crystals; (2) **anti-inflammatory effects** — existing literature shows carbocisteine can suppress NF-κB signalling and IL-8 secretion, pathways also active in acute gouty arthritis; (3) **potential xanthine oxidase (XO) interference** — sulfur-containing compounds have structural potential to inhibit XO (the enzyme responsible for uric acid synthesis), though no direct experimental evidence exists for carbocisteine.

Despite the high TxGNN score, the repurposing rationale team notes that this score likely reflects high connectivity of "inflammatory disease" nodes in the knowledge graph rather than gout-specific signalling. Respiratory mucus disorders and gout share no direct pathophysiological overlap, and the mechanistic links above remain entirely theoretical with zero clinical or in vitro validation. Until preclinical data is available, this candidate cannot advance beyond the Hold stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Carbocisteine has **no registered products** in the India regulatory database. There are no approved licenses, dosage forms, or indications on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero direct clinical or preclinical evidence linking Carbocisteine to gout — the TxGNN model prediction (L5) alone is insufficient to justify further investment without at least in vitro or animal model data supporting the proposed mechanism.

**To proceed, the following is needed:**

- **MOA confirmation**: Retrieve full DrugBank mechanism-of-action data to verify whether anti-inflammatory or antioxidant properties are pharmacologically active at therapeutic concentrations
- **Preclinical evidence**: Identify or commission in vitro studies on uric acid crystal-induced inflammation models (e.g., macrophage IL-1β suppression assay)
- **XO inhibition assay**: Test whether carbocisteine or its metabolites exhibit measurable xanthine oxidase inhibitory activity
- **Regulatory baseline**: Retrieve the India package insert (CDSCO/local label) to establish contraindications and warning profile before any indication expansion work begins
- **Literature gap fill**: Conduct a broader PubMed search covering carbocisteine + inflammation + uric acid to confirm there are truly zero indirect supporting publications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

