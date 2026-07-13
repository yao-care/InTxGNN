---
layout: default
title: Capreomycin
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Capreomycin
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

# Capreomycin: From Tuberculosis to Gout

## One-Sentence Summary

Capreomycin is a second-line cyclic polypeptide antibiotic used for drug-resistant tuberculosis (TB), with no registered products in India.
The TxGNN model predicts it may be effective for **Gout**, with **0 clinical trials** and **0 publications** currently supporting this direction.
This prediction carries the lowest possible evidence level (L5), and the mechanistic link between an anti-mycobacterial antibiotic and uric acid metabolism is considered extremely weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Tuberculosis (drug-resistant) — no India regulatory license on record; based on pharmacological classification |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological classification, Capreomycin is a cyclic polypeptide antibiotic that exerts its antibacterial effect by binding to the 70S ribosomal subunit, disrupting translocation and inhibiting protein synthesis in *Mycobacterium tuberculosis*. It is strictly classified as a second-line anti-TB agent and has no known activity against non-mycobacterial organisms.

Gout is a metabolic disease driven by the deposition of monosodium urate crystals in joints and soft tissues. Its pathophysiology involves impaired purine metabolism (resulting in hyperuricemia), NLRP3 inflammasome activation, and acute neutrophil-mediated inflammation. There is no known intersection between ribosomal protein synthesis inhibition in mycobacteria and uric acid metabolism or inflammasome biology.

The internal mechanistic analysis in this Evidence Pack rates credibility as **extremely low**, noting that the TxGNN Knowledge Graph (KG) prediction likely arises from topological proximity between the antibiotic node and arthritis-related disease nodes in the graph — a structural artifact rather than a biological signal. Until a plausible mechanistic hypothesis is identified, this prediction does not meet the threshold for further investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Capreomycin is **not marketed in India**. No authorizations on record.

---

## Safety Considerations

Please refer to the package insert for key warnings and contraindications (data not available in this Evidence Pack).

**Drug Interactions** — 58 interactions identified (source: DDInter). Notable interactions include:

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|---------------|
| Kanamycin | **Major** | Both are aminoglycoside-class or related antibiotics with additive nephrotoxicity and ototoxicity risk |
| Neomycin | **Major** | Similar mechanism; additive nephrotoxic and neuromuscular blockade risk |
| Amphotericin B (all formulations) | Moderate | Additive nephrotoxicity; renal function monitoring required |
| Dexamethasone | Moderate | Corticosteroids may potentiate electrolyte imbalance (hypokalemia) |
| Hydrocortisone | Moderate | Same mechanism as dexamethasone interaction |
| Betamethasone / Triamcinolone / Beclomethasone | Moderate | Class effect — corticosteroid + capreomycin electrolyte risk |
| Omeprazole / Esomeprazole / Lansoprazole / Rabeprazole / Dexlansoprazole | Moderate | Altered renal tubular handling may affect capreomycin clearance |
| Mesalazine / Balsalazide / Olsalazine | Moderate | Additive nephrotoxic potential with aminosalicylates |
| Exenatide | Moderate | Potential impact on renal drug clearance |

> **Note:** 58 total interactions are on record. The above represents the Major and a prioritized subset of Moderate interactions. Full interaction review is required before any co-administration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial evidence, no supporting literature, and no plausible mechanistic link between Capreomycin's anti-mycobacterial mechanism of action and gout pathophysiology. All 10 top-ranked TxGNN predictions for this drug are rated L5 (model prediction only), and the internal mechanistic analysis consistently concludes credibility is either "none" or "extremely low." The high TxGNN scores (>99%) most likely reflect KG topological artifacts — shared neighborhood nodes in the arthritis/musculoskeletal disease cluster — rather than genuine repurposing signals.

**To proceed, the following would be needed:**

- Identification of a credible mechanistic hypothesis connecting Capreomycin to the predicted indication (e.g., off-target NLRP3 inhibition, xanthine oxidase interaction, or anti-inflammatory activity data)
- Retrieval of Capreomycin's full mechanism of action and pharmacodynamic profile from DrugBank (currently marked as Data Gap)
- Review of Capreomycin's package insert warnings and contraindications (currently unavailable; required for any S1 safety pre-screening)
- Re-ranking of TxGNN predictions with biological plausibility filters to separate true repurposing signals from graph topology noise
- If a mechanistic hypothesis is identified: exploratory in vitro or in vivo preclinical evidence before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

