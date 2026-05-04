---
layout: default
title: Balsalazide
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
---

# Balsalazide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Balsalazide: From Ulcerative Colitis to Gout

## One-Sentence Summary

Balsalazide is a 5-aminosalicylic acid (5-ASA) prodrug internationally approved for mild-to-moderate ulcerative colitis, designed to deliver active 5-ASA directly to the distal colon.
The TxGNN model predicts it may be effective for **Gout**, with **0 clinical trials** and **0 publications** currently supporting this direction.
Evidence for this prediction is limited to computational modelling only, and the mechanistic basis is assessed as very weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ulcerative colitis (mild-to-moderate; internationally approved; not registered in India) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Balsalazide is an azo-bonded prodrug cleaved by colonic bacterial azoreductases to release 5-aminosalicylic acid (5-ASA) locally at the distal colon. Detailed mechanism of action data is not available in the current Evidence Pack. Based on the known pharmacology of its active metabolite, 5-ASA exerts anti-inflammatory effects through inhibition of NF-κB nuclear translocation, suppression of TNF-α-induced downstream signalling, and modulation of prostaglandin synthesis via COX inhibition.

Despite these broad anti-inflammatory properties, the mechanistic link to gout is **extremely weak**. Acute gout is driven by monosodium urate crystal-induced activation of the NLRP3 inflammasome and the IL-1β signalling cascade, with ensuing neutrophil infiltration into affected joints. 5-ASA has no established direct action on NLRP3 or IL-1β, nor does it affect xanthine oxidase (urate synthesis) or renal urate excretion — the two primary pharmacological targets in gout management. Chronic hyperuricaemia, which underlies recurrent attacks, also lies entirely outside Balsalazide's known mechanism.

The high TxGNN prediction score (99.75%) most likely reflects a non-specific association between "anti-inflammatory agent" and "inflammatory disease" nodes within the knowledge graph, rather than biologically specific signal. This pattern — a colonic-targeted 5-ASA prodrug scoring highly for a systemic metabolic-inflammatory condition — is a recognised artefact of graph-based repurposing models and should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Balsalazide is **not registered** in India. No marketing authorisation records are available.

---

## Safety Considerations

**Drug Interactions (196 total interactions identified via DDInter):**

| Interacting Drug | Interaction Level |
|-----------------|------------------|
| Human immunoglobulin G (intravenous) | **Major** |
| Doxycycline | Moderate |
| Ketorolac | Moderate |
| Acyclovir | Moderate |
| Ibuprofen | Moderate |
| Foscarnet | Moderate |
| Fosfomycin | Moderate |
| Gallium nitrate | Moderate |
| Amphotericin B | Moderate |
| Amikacin | Moderate |
| Celecoxib | Moderate |

A total of 196 interactions were identified: 1 Major (intravenous immunoglobulin) and 195 Moderate (predominantly antibiotics, antivirals, and NSAIDs). The Major interaction with IV immunoglobulin warrants particular attention in any clinical scenario involving concomitant immune therapy.

For complete warnings and contraindications, please refer to the originator package insert, as local labelling data for India is not available in the current Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is high (99.75%), no clinical trial or literature evidence supports Balsalazide in gout, and the core pathophysiological mechanism of gout (NLRP3 inflammasome / IL-1β axis) is not addressed by 5-ASA's known pharmacology. This prediction is assessed as a likely false-positive arising from non-specific knowledge-graph node clustering between anti-inflammatory agents and inflammatory diseases.

**To proceed, the following would be needed:**
- Preclinical mechanistic studies demonstrating 5-ASA activity specifically on the NLRP3/IL-1β pathway or urate metabolism pathways
- At least one hypothesis-generating clinical observation (e.g., lower gout incidence in IBD patients on 5-ASA therapy)
- Pharmacokinetic data confirming sufficient systemic 5-ASA exposure from oral Balsalazide (current colonic-targeted formulation is designed to limit systemic absorption)
- A clear differentiation rationale from established gout therapies (colchicine, allopurinol, febuxostat, IL-1β inhibitors) before any development pathway is considered
- Full TFDA/local package insert data to assess warnings, contraindications, and safety in the intended population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

