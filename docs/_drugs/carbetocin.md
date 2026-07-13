---
layout: default
title: Carbetocin
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 2
---

# Carbetocin
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

# Carbetocin: From Postpartum Haemorrhage to Isotretinoin-Like Syndrome

## One-Sentence Summary

Carbetocin is a synthetic oxytocin analogue used to prevent postpartum haemorrhage due to uterine atony following caesarean delivery, and is also under investigation as an intranasal formulation (LV-101) for Prader-Willi syndrome.
The TxGNN model predicts it may be effective for **Isotretinoin-Like Syndrome** (rank 1) and **Goodman Syndrome** (rank 2), however there are currently **0 clinical trials** and **0 publications** supporting either direction.
Both predictions are model-generated only, with very low assessed biological plausibility.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of postpartum haemorrhage due to uterine atony |
| Predicted New Indication | Isotretinoin-Like Syndrome |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Carbetocin is a synthetic analogue of oxytocin and acts as a selective agonist at the oxytocin receptor (OXTR, encoded by gene *OXTR*, Entrez ID: 5021). Activation of OXTR engages the Gq/G11–PLC–IP₃–Ca²⁺ intracellular signalling cascade, producing sustained uterine smooth muscle contraction — the pharmacological basis for its use in preventing postpartum haemorrhage. An intranasal formulation is also in development for Prader-Willi syndrome, where central oxytocinergic pathways are targeted to reduce pathological hyperphagia.

Isotretinoin-like syndrome (retinoid embryopathy) is caused by excessive activation of RAR/RXR nuclear receptors during embryonic development, impairing neural crest cell differentiation and dysregulating HOX gene expression. The hypothetical mechanistic bridge to OXTR is extremely indirect: OXTR downstream effectors (MAPK/ERK) and the retinoic acid signalling axis share remote developmental signal crossover points, but no direct experimental link has been established in any published study. The biological plausibility is therefore assessed as very low (Plausibility Score: 1/5).

The high TxGNN score most likely reflects topological proximity within the knowledge graph — Carbetocin and agents associated with rare congenital anomaly nodes may share graph neighbourhood features — rather than a genuine mechanistic relationship. This is a recognised limitation of graph-based repurposing models when applied to ultra-rare diseases with sparse annotation. The same reasoning applies to the second-ranked prediction, Goodman Syndrome (Carpenter syndrome type 2, RAB23 loss-of-function), where the Hedgehog–SMO–GLI axis has no meaningful connection to OXTR pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Carbetocin holds no drug registrations in India and is currently not marketed. No licence records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note from pharmacology data:** Carbetocin acts as an OT receptor (OXTR) agonist (synonyms: Pabal®; CAS 37025-55-1). Potential class-effect considerations include uterotonic activity, cardiovascular effects (hypotension, tachycardia), and fluid retention. Formal prescribing information including TFDA-approved warnings and contraindications was not available at the time of this report and must be obtained prior to any clinical decision.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero clinical or published evidence supporting the use of Carbetocin in isotretinoin-like syndrome or Goodman syndrome, and the mechanistic connection between OXTR agonism and either indication is biologically implausible. Proceeding with development for these indications is not justified at this stage.

**To proceed, the following is needed:**

- **Resolve Blocking data gap (DG001):** Obtain TFDA/applicable regulatory package insert to complete the safety baseline assessment — this is a prerequisite for any S1 safety evaluation
- **Resolve High-severity data gap (DG002):** Confirm full mechanism of action via DrugBank API query (DB01282) to enable mechanistic relevance scoring
- **Mechanistic literature review:** Assess whether any peer-reviewed evidence links OXTR signalling to retinoic acid pathways, neural crest development, or RAB23/Hedgehog biology before escalating this prediction
- **Re-rank repurposing candidates:** Consider screening lower-ranked TxGNN predictions with known biological plausibility (e.g., anxiety disorders, social behaviour conditions, autism spectrum disorder) where oxytocin pathway modulation has established evidence, rather than investing in the current top two model outputs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

