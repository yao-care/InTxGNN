---
layout: default
title: Lubiprostone
parent: 僅模型預測 (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
---

# Lubiprostone
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

# Lubiprostone: From Chronic Constipation to Alopecia

## One-Sentence Summary

Lubiprostone is a prostaglandin E1 (PGE1) derivative primarily used for chronic constipation and irritable bowel syndrome, working through chloride channel (ClC-2) activation and EP receptor agonism in the gastrointestinal tract.
The TxGNN model predicts it may have potential utility in **Alopecia (hair loss)**, ranked #1 among all predicted new indications with a score of **99.93%**.
However, this prediction is supported by **no clinical trials** and **no published literature**, placing it at the lowest evidence level (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic constipation; Irritable bowel syndrome (IBS) |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Lubiprostone is a bicyclic fatty acid derived from prostaglandin E1 (PGE1). It activates type-2 chloride channels (ClC-2) in intestinal epithelial cells, promoting fluid secretion and intestinal motility. It also acts as an EP4 and EP1 receptor agonist, contributing to its gastrointestinal effects. The drug's primary design is for luminal (gut-local) action, with extremely low systemic bioavailability.

The mechanistic basis for the alopecia prediction is indirect but theoretically plausible. EP4 receptor activation has been shown in vitro to promote dermal papilla cell proliferation, which is important for the hair growth cycle. Additionally, prostaglandin D2 (PGD2) is a known inhibitor of hair growth (as studied by the Cotsarelis laboratory), and EP4 agonism may theoretically counteract PGD2-mediated hair follicle suppression. The TxGNN model likely identified this connection via knowledge graph linkages between the PGE2/EP4 signalling pathway and hair follicle biology.

However, it is critical to note that this mechanistic link is highly indirect and speculative. Lubiprostone's known systemic exposure is negligible after oral administration, making any hair follicle-level pharmacological effect extremely unlikely via the current oral dosage form. No preclinical animal studies or human clinical research have explored lubiprostone for any form of alopecia. The high TxGNN score likely reflects knowledge graph proximity between "prostaglandin pathways" and "hair follicle cycle nodes" rather than a validated pharmacological relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Lubiprostone in alopecia.

---

## Literature Evidence

Currently no related literature available for Lubiprostone in alopecia.

---

## India Market Information

Lubiprostone is not currently approved or marketed in India. No drug licenses are on record.

---

## Safety Considerations

**Drug Interactions:**

| Interacting Drug | Severity | Source | Notes |
|-----------------|----------|--------|-------|
| Idelalisib | Moderate | DDInter | Monitor for potential interaction; clinical significance in the context of hair loss treatment would require evaluation |

> For complete safety information including warnings, contraindications, and precautions, please refer to the originator product (Amitiza®) package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Lubiprostone carry an L5 evidence level with zero supporting clinical trials or published literature. The mechanistic link between Lubiprostone's EP4/ClC-2 pharmacology and alopecia is theoretically interesting but extremely indirect, and the drug's near-zero systemic bioavailability creates a fundamental pharmacokinetic barrier to any extra-intestinal indication.

**To proceed, the following is needed:**

- **MOA clarification**: Obtain complete DrugBank mechanism of action data, particularly regarding EP receptor subtype selectivity (EP1/EP2/EP4) and ClC-2 channel activation
- **Safety data**: Retrieve TFDA/FDA package insert to identify key warnings and contraindications (currently a blocking data gap)
- **Preclinical proof-of-concept**: At minimum, in vitro studies using dermal papilla cells or ex vivo hair follicle organ culture with lubiprostone are needed before any clinical consideration
- **Formulation feasibility**: Evaluate whether a topical or locally-delivered formulation could bypass the systemic bioavailability limitation — this is a prerequisite for any hair follicle indication
- **Alternative higher-plausibility indications**: Consider prioritising pulmonary hypertension (Rank #5) for further evaluation, as it has the strongest mechanistic rationale among all predicted indications (prostacyclin-like EP4 agonism → pulmonary vasodilation), though systemic bioavailability remains a concern there as well

---

> **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

