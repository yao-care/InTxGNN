---
layout: default
title: Oxytetracycline
parent: 僅模型預測 (L5)
nav_order: 628
evidence_level: L5
indication_count: 10
---

# Oxytetracycline
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

# Oxytetracycline: From Bacterial Infections to Chronic Rhinosinusitis

## One-Sentence Summary

Oxytetracycline is a broad-spectrum tetracycline-class antibiotic; no original-indication or product license data is currently on file in this Evidence Pack (drug is unlicensed/not marketed in India). The TxGNN model predicts potential efficacy for **Chronic Rhinosinusitis**, but this specific prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-driven hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (no license/registry record on file — see note below) |
| Predicted New Indication | Chronic Rhinosinusitis |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this Evidence Pack (`original_moa: [Data Gap]`). Based on established pharmacological knowledge, Oxytetracycline is a broad-spectrum tetracycline-class antibiotic that inhibits bacterial protein synthesis by binding the 30S ribosomal subunit and blocking aminoacyl-tRNA attachment. Tetracyclines also have a well-documented secondary anti-inflammatory effect through matrix metalloproteinase (MMP) inhibition, independent of their antibacterial activity.

The rationale linking Oxytetracycline to chronic rhinosinusitis rests on this dual mechanism: many cases of chronic rhinosinusitis have a bacterial component, and the antibacterial effect could theoretically address infective flares, while the MMP-inhibiting anti-inflammatory effect could theoretically address the chronic mucosal inflammation component. However, this is a **mechanistic hypothesis only** — the knowledge graph score (rank 7023, 99.61%) is not corroborated by any registered clinical trial or published literature for this specific disease.

Given the complete absence of clinical or literature evidence (L5), this prediction should be treated as hypothesis-generating rather than actionable, and is not yet suitable for further clinical development without dedicated preclinical or early-phase investigation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Oxytetracycline currently has **no marketing authorization on file in India** (`market_status: 未上市`, 0 registrations, no license records available for extraction).

---

## Safety Considerations

Key warnings and contraindications are not available in the Evidence Pack (data gap — TFDA/India label review still pending, flagged as **Blocking** in `data_gaps`).

**Drug Interactions**: A DDI query returned 144 documented interactions (ddinter source). Notable entries include:
- **Major**: Vitamin A (co-administration with tetracyclines is associated with risk of pseudotumor cerebri)
- **Moderate**: Divalent/trivalent cation-containing products that chelate tetracyclines and reduce absorption — Calcium Phosphate, Calcium Acetate, Magnesium Oxide/Sulfate/Chloride, Zinc Sulfate/Acetate, Potassium Citrate; also Amoxicillin, Balsalazide, and multiple insulin products (aspart, degludec, detemir, glargine, glulisine, human isophane/regular/inhaled)
- **Minor**: Mannitol

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Chronic Rhinosinusitis) has a high model confidence score but zero supporting clinical trials or literature (Evidence Level L5) — insufficient to justify moving past a research-hypothesis stage.

**To proceed, the following is needed:**
- TFDA/India product label (warnings, contraindications) — currently a **Blocking** data gap per `DG001`
- Detailed mechanism-of-action confirmation — currently a **High**-severity data gap per `DG002`
- Preclinical or early-phase evidence specifically for chronic rhinosinusitis before any clinical development decision

**Note on alternate candidates in this Evidence Pack:** Among the 10 predicted indications supplied, **Otitis Externa** (rank 10, score 99.27%) is materially stronger — it reaches **Evidence Level L2** with 20 supporting publications, including multiple RCTs of topical oxytetracycline/hydrocortisone/polymyxin B combinations, and carries a **Proceed with Guardrails** recommendation. **Post-bacterial disorder / osteomyelitis** (rank 6) reaches L3 but is based on a single terminated, 11-patient early-phase trial. If a repurposing candidate is needed near-term, Otitis Externa is the substantially better-supported option and may warrant its own dedicated evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

