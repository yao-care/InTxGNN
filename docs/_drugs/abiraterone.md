---
layout: default
title: Abiraterone
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 10
---

# Abiraterone
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

# Abiraterone: From Prostate Cancer to Migraine Disorder

## One-Sentence Summary

Abiraterone acetate (DrugBank: DB05812) is a selective CYP17A1 inhibitor used to treat castration-resistant prostate cancer by blocking androgen biosynthesis in the adrenal glands and tumor tissue.
The TxGNN model predicts it may be effective for **Migraine Disorder** (rank 1, score 98.81%), with migraine variants occupying three of the top five predicted slots.
However, **no clinical trials or directly relevant publications** linking Abiraterone to any migraine indication have been identified — all predictions remain at Evidence Level L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (castration-resistant; from published prescribing information — no India license on file) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 98.81% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not retrieved from DrugBank in this Evidence Pack (Data Gap DG002). Based on established pharmacology, Abiraterone is a selective inhibitor of CYP17A1 (17α-hydroxylase / 17,20-lyase), the enzyme responsible for androgen biosynthesis in the adrenal glands, testes, and tumor microenvironment. Its clinical utility in prostate cancer stems from the fact that tumor growth is driven by androgen receptor signaling even after surgical or chemical castration.

The mechanistic rationale linking Abiraterone to migraine centres on the sex-hormone axis: menstrual migraine is well-documented to be triggered by perimenstrual estrogen withdrawal. Because adrenal androgens (DHEA, androstenedione) are upstream precursors for peripheral estrogen synthesis via aromatization, CYP17A1 inhibition could theoretically reduce the substrate pool available for estrogen production, dampening hormonal fluctuations that precipitate migraine attacks. However, the direction of this effect is uncertain — blocking upstream androgens does not reliably suppress circulating estrogen in premenopausal women and may have paradoxical consequences depending on the tissue and hormonal milieu.

It is worth noting that among the full top-10 prediction list, **pulmonary hypertension (rank 5)** carries the strongest biological rationale: androgen receptors are expressed in pulmonary arterial smooth muscle cells, idiopathic pulmonary arterial hypertension (IPAH) shows a consistent female predominance (F:M ≈ 2–4:1) implicating sex-hormone signaling in disease pathobiology, and CYP17A1 inhibition could theoretically reduce androgen-driven vascular remodeling. This direction deserves closer attention than the migraine cluster, despite no directly matching evidence being retrieved.

---

## Clinical Trial Evidence

Currently no clinical trials directly investigating Abiraterone for Migraine Disorder have been registered.

> **⚠️ Data Quality Note — Pulmonary Hypertension (Rank 5):** One trial was retrieved by the evidence collector for the pulmonary hypertension query:
>
> | Trial | Phase | Status | Enrollment | Assessment |
> |-------|-------|--------|------------|------------|
> | [NCT01961843](https://clinicaltrials.gov/study/NCT01961843) | NA | Completed | 40 | **Mismatched** — This is a prostate cancer circulating tumor cell biomarker study. It was incorrectly retrieved for the pulmonary hypertension indication and should not be counted as supporting evidence. |
>
> Effective clinical trial count for all 10 predicted indications: **0**.

---

## Literature Evidence

Currently no directly relevant literature linking Abiraterone to Migraine Disorder is available.

> **⚠️ Data Quality Note — Migraine with or without Aura, Susceptibility (Rank 2):** The evidence collector returned 20 publications for this query. Upon review, all 20 are epilepsy genetics papers (SCN1A polymorphisms, MTHFR variants, POLG-related disease, GABAergic receptor studies) and are entirely unrelated to Abiraterone. This is a keyword mismatching artifact: "migraine susceptibility" was conflated with "epilepsy susceptibility" by the search algorithm. These publications should be excluded from evidence counting.
>
> **⚠️ Data Quality Note — Pulmonary Hypertension (Rank 5):** Five publications were retrieved, all of which are Abiraterone trials in prostate cancer (STAMPEDE platform, ACIS trial, COSMIC-021, bipolar androgen therapy). None relate to pulmonary hypertension. Evidence collector returned drug-matched but indication-mismatched results.
>
> Effective literature count for all 10 predicted indications: **0**.

---

## India Market Information

Abiraterone is currently **not registered or marketed in India**. No product authorizations were found in the regulatory database. A market entry pathway assessment would be required from scratch.

---

## Cytotoxicity

Abiraterone is indicated for prostate cancer and belongs to the androgen biosynthesis inhibitor class — an anticancer drug. This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted hormonal therapy (CYP17A1 / Androgen synthesis inhibitor) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low — no direct myelosuppressive mechanism; not a DNA-damaging or mitotic-targeting agent |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function (ALT/AST — hepatotoxicity risk), serum potassium (hypokalemia from mineralocorticoid excess), blood pressure, serum cortisol / adrenal function, fasting blood glucose (concomitant corticosteroid effect), cardiac monitoring (QT interval) |
| Handling Protection | Standard oral chemotherapy precautions recommended; does not require the same handling protocols as cytotoxic chemotherapy (no alkylation, no mutagenic metabolites at standard handling exposure) |

**Important co-administration requirement:** Because CYP17A1 inhibition blocks cortisol synthesis, Abiraterone must be co-administered with a corticosteroid (prednisone or prednisolone) to prevent mineralocorticoid excess syndrome (hypertension, hypokalemia, fluid retention) and adrenal crisis. Any repurposing protocol must incorporate this mandatory corticosteroid pairing.

---

## Safety Considerations

Detailed TFDA/CDSCO warning and contraindication text was not retrieved in this Evidence Pack (Data Gap DG001), and the DDI database query failed due to a missing local file (query log ID 1). Please refer to the official prescribing information for complete safety data.

Based on published prescribing information and the clinical trial literature retrieved:

- **Adrenal Insufficiency & Mineralocorticoid Excess**: Mandatory co-administration with prednisone/prednisolone is required. Abrupt discontinuation can precipitate adrenal crisis.
- **Hepatotoxicity**: Clinically significant liver enzyme elevations (ALT/AST) have been reported; LFT monitoring is required at baseline and periodically during treatment.
- **Cardiovascular Effects**: Hypertension, fluid retention, hypokalemia, and QT prolongation have been documented — particularly relevant if considering use in pulmonary hypertension patients with pre-existing cardiac vulnerability.
- **Drug Interactions**: DDI data could not be assessed due to a database file path error. Abiraterone is known to be a CYP2D6 and CYP2C8 inhibitor, and is a CYP3A4 substrate — interaction screening is critical before any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications are at Evidence Level L5 (model prediction only). The evidence collector returned zero directly relevant clinical trials or publications for Migraine Disorder, and the retrieved evidence for other indications (migraine with aura susceptibility, pulmonary hypertension) was entirely mismatched — epilepsy genetics papers and prostate cancer trials respectively. There is currently no empirical basis to advance any of these predictions.

**Most promising direction for future investigation:**
Among all 10 predictions, **Pulmonary Hypertension (rank 5)** carries the strongest biological plausibility. The androgen-PAH mechanistic hypothesis is grounded in published preclinical biology (AR expression in PASMC, sex-skewed IPAH epidemiology), and is a recognized active research area in PAH pathophysiology. This direction warrants a dedicated systematic literature search with PAH-specific queries — not drug-paired queries — to properly assess preclinical evidence.

**To proceed, the following is needed:**

- **DG001 (Blocking)**: Obtain Abiraterone prescribing information (package insert) for safety pre-screening — download and parse TFDA/FDA SPI PDF
- **DG002 (High)**: Retrieve full MOA, pharmacology, and toxicity data from DrugBank API
- **DDI database**: Fix file path error for `ddinter_code_A.csv` to enable drug interaction screening
- **Evidence collection fix**: Correct keyword-matching logic to prevent epilepsy/migraine susceptibility conflation; implement indication-specific MeSH term filtering
- **Pulmonary hypertension-specific search**: Run dedicated PubMed/ClinicalTrials queries using `"androgen" AND "pulmonary hypertension"` without drug-pairing constraint, to capture preclinical mechanistic literature
- **Regulatory pathway**: If proceeding to Phase I/II in PAH, India market entry dossier must be built from scratch (zero existing registrations)

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

