---
layout: default
title: Ozenoxacin
parent: 僅模型預測 (L5)
nav_order: 629
evidence_level: L5
indication_count: 10
---

# Ozenoxacin
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

# Ozenoxacin: From Impetigo to Malaria

## One-Sentence Summary

Ozenoxacin is a topical, non-fluorinated quinolone antibacterial originally used to treat impetigo caused by susceptible Gram-positive skin bacteria. The TxGNN model predicts it may be effective for **Malaria**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests entirely on structural analogy within the quinolone compound family, not on any documented antiparasitic evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Impetigo (topical Gram-positive skin infections) — noted in evidence rationale; not confirmed via a Taiwan license record, as the drug is not marketed in Taiwan |
| Predicted New Indication | Malaria |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known information, Ozenoxacin is a topical non-fluorinated quinolone antibacterial that inhibits bacterial DNA gyrase and topoisomerase IV, and it has proven efficacy against Gram-positive bacteria in impetigo.

Malaria, by contrast, is caused by *Plasmodium* protozoan parasites replicating via apicoplast DNA machinery. Some quinolone-family compounds have loosely analogous structural scaffolds to agents explored against apicoplast DNA replication, which is likely why the knowledge graph surfaced this association. However, there is no direct pharmacological or clinical evidence that ozenoxacin itself has antiplasmodial activity — the link is a structural class analogy rather than a validated mechanistic pathway.

Given that ozenoxacin is a topical formulation with only local skin bacterial activity demonstrated, and malaria requires systemic antiparasitic exposure, the mechanistic plausibility of this prediction is weak. This is reflected in the L5 evidence tier (model prediction only, no supporting studies).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Ozenoxacin is not currently marketed in Taiwan (0 registrations), so no license records are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all currently unavailable — TFDA label data is flagged as a Blocking data gap, and no DDI database match was found due to a missing local data file.)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN model score, there is zero clinical trial or literature support for an ozenoxacin–malaria link, and the mechanistic rationale is speculative (structural class analogy only, contradicted by the drug's topical-only, Gram-positive-only activity profile). Safety data needed for even a preliminary review is also missing.

**To proceed, the following is needed:**
- TFDA package insert / warnings and contraindications data (currently a Blocking gap)
- Confirmed mechanism of action data from DrugBank (currently a High-severity gap)
- Any in vitro/preclinical evidence of antiplasmodial activity for ozenoxacin specifically (not just the quinolone class)
- DDI database repair/reload (local ddinter data file is missing, causing query errors)
- Re-run evidence search periodically, as this candidate currently sits at decision stage S0 with no trial or literature signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

