---
layout: default
title: Phylloquinone
parent: 僅模型預測 (L5)
nav_order: 661
evidence_level: L5
indication_count: 9
---

# Phylloquinone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Phylloquinone: From Vitamin K–Related Use to Renal Tubular Acidosis (Model Prediction Only)

## One-Sentence Summary

> Phylloquinone (Vitamin K1, DB01022) is not currently marketed in India, and this evidence pack contains no original indication or mechanism-of-action data for the drug.
> The TxGNN model's top prediction is **Renal Tubular Acidosis** (score 99.94%), but this comes with **zero supporting clinical trials and zero literature**, and the model's own rationale flags it as a likely false-positive from a knowledge graph with sparse rare-disease data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no `original_indications` or license data provided in this evidence pack |
| Predicted New Indication | Renal Tubular Acidosis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

**Note:** This batch contains 9 TxGNN candidates for Phylloquinone (ranks 1–9, scores 99.08%–99.94%). All 9 are rare/genetic diseases, all are scored L5 with zero clinical trials or literature, and all carry a "Hold" recommendation. This pattern — high similarity in score, uniformly rare/orphan disease targets, and no supporting evidence — is consistent with the model's own stated concern (see below) that these are artifacts of sparse training data around rare-disease nodes rather than genuine repurposing signals.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Phylloquinone in this evidence pack (`original_moa: [Data Gap]`), and no original indication is recorded either. Phylloquinone is Vitamin K1, generally known in clinical practice for its role in coagulation (activation of vitamin K–dependent clotting factors) and, more broadly, in carboxylation of osteocalcin relevant to bone mineralization — but this background is general pharmacological knowledge, not something confirmed by the data supplied here.

Critically, the model's own repurposing rationale for the top candidate does **not** support a genuine mechanistic link: it states that Renal Tubular Acidosis (a disorder of renal acid-base/H⁺–HCO₃⁻ transport) has "no known or inferable physiological mechanistic connection" to Phylloquinone, and explicitly flags the 0.999 score as a **suspected false positive** arising from sparse knowledge-graph data around rare disease nodes, rather than a mechanism-driven prediction.

The same pattern repeats across ranks 2–9 (hypophosphatemic rickets, Pendred syndrome, nonsyndromic deafness, NAD(P)HX dehydratase deficiency, leukocyte adhesion deficiency, hypermanganesemia with dystonia, Fraser syndrome, Temtamy brachydactyly syndrome) — each rationale describes the mechanistic link as weak, indirect, or absent. Only the hypophosphatemic rickets link (via vitamin K's role in osteocalcin carboxylation and bone mineralization) has any biological plausibility, and even that is explicitly noted as not matching the primary FGF23/phosphate pathway driving that disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Phylloquinone is **not currently marketed** in India per this evidence pack (`market_status: 未上市`, `total_licenses: 0`). No license records are available to summarize.

---

## Safety Considerations

- **Drug Interactions**: 152 total interactions on record. Of the sample provided, most are listed with **Unknown** severity level (source: DDInter), including interactions with common agents such as Omeprazole, Pantoprazole, Morphine, Acetylsalicylic acid, Simvastatin, and Vancomycin — these require individual review rather than being treated as confirmed benign. Two interactions are classified as **Minor**: **Mineral oil** and **Orlistat** — both consistent with the known pharmacology of reduced fat-soluble vitamin (vitamin K) absorption.

Key warnings and contraindications are not available in this evidence pack — please refer to the package insert for this information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate has no clinical trial or literature support (L5 evidence only), the drug is not marketed in India, and the model's own rationale explicitly raises the possibility that the high TxGNN score is a false positive driven by sparse rare-disease training data rather than a real mechanistic signal. Two data gaps are also flagged as Blocking/High severity in this pack (missing warnings/contraindications, missing MOA), which independently prevents progression to a safety screening stage.

**To proceed, the following is needed:**
- TFDA/regulatory package insert data (warnings, contraindications) — currently a **Blocking** gap (DG001)
- Mechanism of action data via DrugBank API — currently a **High**-severity gap (DG002)
- Independent literature/preclinical search specifically for Phylloquinone and renal tubular acidosis (or bone-mineralization-related candidates such as hypophosphatemic rickets), since none currently exists
- A biological-plausibility review before further investment, given that all 9 candidates in this batch share the same "no mechanistic link / possible false positive" pattern
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

