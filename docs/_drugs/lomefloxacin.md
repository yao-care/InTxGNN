---
layout: default
title: Lomefloxacin
parent: 僅模型預測 (L5)
nav_order: 492
evidence_level: L5
indication_count: 10
---

# Lomefloxacin
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

# Lomefloxacin: From Bacterial Infections to Laryngotracheitis

## One-Sentence Summary

Lomefloxacin is a second-generation fluoroquinolone antibacterial, historically used against bacterial infections (e.g., urinary and respiratory tract infections). The TxGNN model's top prediction suggests possible relevance to **laryngotracheitis**, but this direction is currently supported by **0 clinical trials** and **0 publications** — the signal comes from the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (fluoroquinolone antibacterial class) |
| Predicted New Indication | Laryngotracheitis |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Taiwan Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for lomefloxacin is not available in this evidence pack (`original_moa` is a data gap). Based on known drug-class information, lomefloxacin is a second-generation fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV, giving it broad-spectrum antibacterial activity. Its established efficacy is against bacterial infections of the urinary and respiratory tract.

The predicted new indication, laryngotracheitis, would only be mechanistically plausible if caused by a susceptible bacterial pathogen (e.g., *Haemophilus influenzae*, *Moraxella catarrhalis*). However, laryngotracheitis — particularly croup in children — is predominantly viral, and fluoroquinolones have no antiviral activity. Fluoroquinolones are also generally avoided in pediatric populations due to cartilage toxicity risk, which is the population most affected by croup-type laryngotracheitis.

Notably, all ten indications predicted for this drug (ranks 1–10) carry the same caveats: none has clinical trial or literature support, all are scored L5 (model-only), and several of the cardiovascular predictions (heart valve disease, heart conduction disease, aortic/heart aneurysm) actually correspond to **known fluoroquinolone safety signals** (QT prolongation, aortic/valve injury risk) rather than therapeutic opportunities — i.e., the model may be picking up risk-association edges in the knowledge graph rather than true repurposing candidates. This warrants caution in interpreting the ranked list as a whole.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Taiwan Market Information

Lomefloxacin is currently **not marketed** in Taiwan (0 active licenses/registrations on file), so no product-level dosage form or indication text is available.

## Safety Considerations

- **Drug Interactions**: 238 total interactions on file. Notable **Major**-level interactions include corticosteroids (Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone — increased tendon rupture risk when combined with fluoroquinolones), Bupropion, and Chlorpropamide. **Moderate**-level interactions include several antidiabetic agents (Acarbose, Metformin, Pioglitazone, Alogliptin, Albiglutide, Canagliflozin — fluoroquinolones can alter glucose regulation), Famotidine, Acetylsalicylic acid, Balsalazide, Bisacodyl, and calcium/potassium salts (Calcium Phosphate, Calcium acetate, Potassium citrate — potential chelation/absorption interference).

Detailed labeled warnings and contraindications are not yet available for this drug (TFDA label data gap); please refer to the package insert once available for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (laryngotracheitis) has no clinical trial or literature support and is model-prediction only (L5). Several of the other top-ranked predictions for this drug appear to reflect known fluoroquinolone safety risks rather than therapeutic mechanisms, raising concern about signal quality for this candidate overall. Combined with the blocking data gap on TFDA label warnings/contraindications, this candidate is not ready for further evaluation.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a blocking data gap
- Confirmed mechanism-of-action documentation from DrugBank or primary literature
- Any preclinical or case-level evidence specifically linking lomefloxacin to laryngotracheitis (bacterial etiology), to distinguish a genuine signal from a knowledge-graph artifact
- Re-review of the other 9 predicted indications given the pattern of risk-signal contamination observed here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

