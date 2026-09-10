---
layout: default
title: Rosuvastatin
parent: 僅模型預測 (L5)
nav_order: 748
evidence_level: L5
indication_count: 10
---

# Rosuvastatin
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

# Rosuvastatin: From Hypercholesterolemia to Cholesterol-Ester Transfer Protein Deficiency

## One-Sentence Summary

> Rosuvastatin is a well-known HMG-CoA reductase inhibitor (statin) globally used to manage hypercholesterolemia and cardiovascular risk, though this Evidence Pack contains no India-specific label or licensing data.
> The TxGNN model's top-ranked prediction is **Cholesterol-Ester Transfer Protein (CETP) Deficiency**, but this is currently supported by **0 clinical trials** and only **2 loosely related case-report publications** — neither of which studies rosuvastatin directly.
> Evidence is too thin and mechanistically ambiguous to support this indication at present.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from the India regulatory dataset (no license records); rosuvastatin is globally established as an HMG-CoA reductase inhibitor for hypercholesterolemia/dyslipidemia |
| Predicted New Indication | Cholesterol-Ester Transfer Protein (CETP) Deficiency |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for this candidate is not available in the current Evidence Pack (flagged as a High-severity data gap, DG002). Based on generally known pharmacology, rosuvastatin is a potent HMG-CoA reductase inhibitor that lowers LDL-cholesterol by upregulating hepatic LDL receptors, and it also modestly raises HDL-cholesterol — properties that place it firmly within lipid-metabolism pharmacology.

CETP deficiency, however, is a rare genetic disorder in which loss of cholesteryl-ester transfer protein activity causes markedly *elevated* HDL-C rather than hypercholesterolemia. This is mechanistically distinct from rosuvastatin's LDL-lowering action, and the two supporting publications in this pack are case reports on **apoA-I deficiency** and **hepatic lipase deficiency** — related rare lipid disorders, but neither is a study of rosuvastatin treatment in CETP deficiency specifically. The link therefore appears to be an artifact of the model's proximity in "lipid metabolism disorder" concept space rather than a genuine, literature-supported therapeutic hypothesis.

Given the absence of any direct pharmacological or clinical rationale connecting rosuvastatin to CETP deficiency, this prediction should be treated as a low-confidence signal warranting further mechanistic investigation rather than a near-term repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21122686](https://pubmed.ncbi.nlm.nih.gov/21122686/) | 2010 | Case report/Review | Journal of Clinical Lipidology | Describes complete Apo A-I deficiency in an Iraqi family with premature atherosclerosis; does not evaluate rosuvastatin or CETP deficiency directly |
| [22798447](https://pubmed.ncbi.nlm.nih.gov/22798447/) | 2010 | Case report | BMJ Case Reports | Describes hepatic lipase deficiency in a Middle-Eastern male, reporting CETP activity/mass as a secondary finding; not a treatment study |

Both papers are tangential to the predicted indication — neither addresses rosuvastatin as a therapy for CETP deficiency.

---

## India Market Information

Rosuvastatin is currently **not marketed** in India under this dataset, with **0 registered licenses**. No product, dosage form, or approved-indication records are available for review.

---

## Safety Considerations

**Drug Interactions**: The DDI database records 524 total interactions for rosuvastatin. Notable examples from the sampled list include:
- **Major**: Fenofibrate, Atazanavir
- **Moderate**: Zidovudine, Paclitaxel, Adalimumab, Trastuzumab emtansine, Ethanol, Alpelisib, Amiodarone, Sodium citrate, Apalutamide, Asparaginase (E. coli / Erwinia chrysanthemi), Atorvastatin, Auranofin, Bempedoic acid, Ezetimibe
- **Minor**: Levonorgestrel, Norethisterone, Desogestrel

No key warnings or contraindications data are currently available (flagged as a Blocking data gap, DG001 — TFDA label warnings/contraindications). Please refer to the official package insert for complete safety information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (CETP deficiency) has no direct clinical or mechanistic evidence linking rosuvastatin to this disease — the two supporting publications concern unrelated rare lipid disorders. Combined with a Blocking data gap on TFDA safety labeling (DG001) and a High-severity gap on mechanism of action (DG002), this candidate cannot proceed past initial safety screening (S0).

**To proceed, the following is needed:**
- Confirmed rosuvastatin mechanism of action (MOA) data from DrugBank
- TFDA/local regulatory label with warnings and contraindications
- Direct preclinical or clinical evidence connecting rosuvastatin to CETP activity or CETP-deficiency-related lipid phenotypes
- Reassessment against alternative, better-supported candidates in this Evidence Pack (e.g., familial hypercholesterolemia, rank 2, which has extensive Phase 3 RCT support, or HIV-related cardiovascular risk reduction, rank 5, L3/S1) as these show substantially stronger evidence bases
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

