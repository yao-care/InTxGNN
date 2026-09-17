---
layout: default
title: Potassium Nitrate
parent: Model Prediction Only (L5)
nav_order: 685
evidence_level: L5
indication_count: 2
---

# Potassium Nitrate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Potassium Nitrate: From No Established Indication to Meningococcal Infection (Predicted)

## One-Sentence Summary

Potassium nitrate (DB11090) has no recorded therapeutic indication and is not a marketed pharmaceutical product in the current registry. TxGNN predicts potential efficacy against **meningococcal infection** (score 99.61%) and, as a secondary candidate, **sclerosing cholangitis** (score 99.21%), but **neither prediction is supported by any clinical trial or published literature**, and the evidence pack itself flags the mechanistic link as likely spurious.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on record (compound is not established as a systemic drug) |
| Predicted New Indication | Meningococcal infection |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for potassium nitrate. It is not a marketed pharmaceutical in this registry, and the evidence pack contains no clinical indication history to compare against the predicted new use.

Based on the limited public information available, potassium nitrate (KNO₃) is best known for non-therapeutic uses — a desensitizing agent in toothpaste and a food preservative (E252) — rather than as a systemic anti-infective or immunomodulatory agent. There is no known pharmacological pathway connecting it to meningococcal infection or to sclerosing cholangitis.

The evidence pack's own mechanistic assessment concludes that both predictions most likely reflect **knowledge-graph topological similarity rather than genuine biological plausibility** — for example, indirect linkage through potassium- or nitrate-related nodes in the graph — and explicitly flags the meningococcal infection prediction as a probable false positive. With zero supporting clinical trials or literature for either candidate, this assessment should be treated as a hypothesis-generation signal only, not as a repurposing lead with mechanistic grounding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Secondary Candidate: Sclerosing Cholangitis

A second TxGNN prediction (rank 2, score 99.21%, evidence level L5) links potassium nitrate to sclerosing cholangitis, a chronic autoimmune/idiopathic biliary disease. As with the primary candidate, there are no clinical trials, no literature, and no plausible mechanistic rationale connecting the compound to this condition. This candidate carries the same Hold recommendation for the same reasons.

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) is currently available. Potassium nitrate is not a marketed pharmaceutical product in this jurisdiction, so no package insert or regulatory safety documentation exists for reference.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predicted indications rest on TxGNN score alone (L5, no clinical trials, no literature), the compound has no established original indication or MOA, and the evidence pack itself assesses the mechanistic link as a likely false positive from graph-embedding similarity rather than genuine biology. A Blocking data gap (TFDA/regulatory warnings and contraindications) also means the candidate cannot yet clear a basic safety screen (S1).

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data for potassium nitrate (DrugBank/pharmacology literature)
- Resolution of the Blocking data gap: regulatory warnings/contraindications (source: national FDA product label)
- Independent pharmacological or preclinical rationale linking potassium nitrate to meningococcal infection or sclerosing cholangitis before any further evidence collection is warranted
- Re-screening in future TxGNN model versions to check whether this prediction persists or was an artifact of the current graph embedding
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

