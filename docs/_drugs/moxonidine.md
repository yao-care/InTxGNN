---
layout: default
title: Moxonidine
parent: 僅模型預測 (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
---

# Moxonidine
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

# Moxonidine: From Hypertension to Hypotrichosis Simplex of the Scalp

---

## One-Sentence Summary

Moxonidine is a centrally-acting sympatholytic anti-hypertensive approved in many countries (though not by the FDA), which works by activating imidazoline I1 receptors and α2-adrenoceptors in the brainstem to reduce sympathetic outflow and lower blood pressure.
The TxGNN model predicts it may be effective for **Hypotrichosis Simplex of the Scalp** — a rare hereditary hair loss condition — yet there are **no clinical trials** and **no relevant publications** currently supporting this direction.
The extremely high prediction score (99.95%) is likely a knowledge graph topology artefact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (centrally-acting anti-hypertensive) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack, but receptor binding data confirms that Moxonidine acts as an agonist at **α2A, α2B, and α2C adrenoceptors** (ADRA2A/B/C) as well as at imidazoline I1 receptors in the rostral ventrolateral medulla. This central sympatholytic action reduces sympathetic nerve activity, thereby decreasing heart rate, vascular resistance, and blood pressure. It is approved as an anti-hypertensive in Europe, Australia, and other countries under brand names including Cynt® and Physiotens®.

Hypotrichosis simplex of the scalp is an autosomal dominant hereditary disorder caused by loss-of-function mutations in **LPAR6** or **LIPH** genes, which encode components of the lysophosphatidic acid signalling pathway critical for hair shaft formation and follicular keratinization. The pathophysiology is fundamentally genetic and cell-autonomous, confined to hair follicle epithelial differentiation.

There is **no known biological intersection** between Moxonidine's central I1/α2-adrenoceptor mechanism and the genetic follicular keratinization defect underlying hypotrichosis simplex of the scalp. The very high TxGNN score most likely reflects topological co-occurrence of alopecia-related disease nodes in the knowledge graph — a model artefact — rather than pharmacological plausibility. This prediction is not considered mechanistically supported at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no relevant literature available.

> **Note:** A single publication ([PMID 40007390](https://pubmed.ncbi.nlm.nih.gov/40007390/), 2024, Case Report, *Georgian Medical News*) was retrieved under the broader "alopecia" query. It describes a case of Graham-Little-Piccardi-Lasseur syndrome — a scarring alopecia variant of lichen planopilaris — and contains no mention of Moxonidine or any sympatholytic therapy. It does not constitute supporting evidence for this repurposing hypothesis.

---

## India Market Information

Moxonidine is currently **not marketed in India**. No product authorisations or registrations are on record. Any future development would require a complete new market authorisation pathway.

---

## Safety Considerations

**Known Pharmacological Targets:**
Moxonidine binds the following human adrenoceptors (receptor pharmacology data, not drug-drug interactions):

| Target | Gene | Entrez ID | Ensembl ID |
|--------|------|-----------|------------|
| α2A-adrenoceptor | ADRA2A | 150 | ENSG00000150594 |
| α2B-adrenoceptor | ADRA2B | 151 | ENSG00000274286 |
| α2C-adrenoceptor | ADRA2C | 152 | ENSG00000184160 |

Prescribing warnings and contraindications were not available in this evidence pack. Based on the drug class (centrally-acting sympatholytic), clinicians should be aware of the following known class-effect risks:

- **Cardiovascular:** Bradycardia, hypotension, including orthostatic hypotension
- **CNS:** Sedation, dizziness, dry mouth
- **Withdrawal:** Rebound hypertension upon abrupt discontinuation
- **Renal impairment:** Drug accumulation due to reduced renal clearance (eGFR < 30 mL/min is a recognised concern); dosage adjustment required

> For complete warnings and contraindications, please refer to the EMA/TGA-approved Summary of Product Characteristics (SmPC) or the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Moxonidine's central I1/α2-adrenergic mechanism has no plausible biological link to the LPAR6/LIPH genetic pathway responsible for hypotrichosis simplex of the scalp. All top-ranked predictions for hair-loss indications (Ranks 1–4, 9) are L5 evidence with no supporting clinical or preclinical data, and are assessed as knowledge graph topology effects. Moxonidine is also not currently marketed in India, adding a regulatory barrier.

**To proceed, the following is needed:**

- **Mechanistic hypothesis:** Establish any experimental evidence linking α2-adrenoceptor or I1 receptor activation to hair follicle biology before considering further evaluation
- **Complete safety data:** Retrieve and review the full EMA or TGA-approved SmPC to document contraindications, warnings, and special population restrictions (Data Gap DG001)
- **MOA confirmation:** Query DrugBank API to obtain the complete pharmacological profile and categorisation (Data Gap DG002)
- **Alternative indication review:** Consider redirecting evaluation resources toward more mechanistically plausible predictions — notably **Primary Hereditary Glaucoma** (Rank 10, Score 99.54%), where the α2-agonist class (e.g., brimonidine) is already standard of care, and **Malignant Renovascular Hypertension / Malignant Hypertensive Renal Disease** (Ranks 5–6, Score 99.67%), where Moxonidine's sympatholytic effect on renal sympathetic hyperactivity has a recognised physiological rationale — though both require dedicated safety assessments before further progression

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

