---
layout: default
title: Tetrabenazine
parent: 僅模型預測 (L5)
nav_order: 819
evidence_level: L5
indication_count: 10
---

# Tetrabenazine
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

# Tetrabenazine: From Movement Disorders to Polycystic Kidney Disease 3 With or Without Polycystic Liver Disease

## One-Sentence Summary

> Tetrabenazine is a VMAT2 inhibitor clinically used for hyperkinetic movement disorders (e.g., chorea); formal indication and MOA records are missing from this evidence pack (data gaps DG001/DG002).
> The TxGNN model predicts it may be effective for **Polycystic Kidney Disease 3 with or without Polycystic Liver Disease**,
> but **0 clinical trials** and **20 publications** were found — and none of the literature actually links Tetrabenazine to this disease. The model's own mechanistic rationale explicitly states **no known biological connection**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (`original_indications` empty). Known clinically as a VMAT2 inhibitor for movement disorders, per the drug's own repurposing rationale text. |
| Predicted New Indication | Polycystic kidney disease 3 with or without polycystic liver disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal DrugBank MOA and TFDA label data are marked as data gaps (DG001: blocking, DG002: high) in this evidence pack. However, the model's own repurposing-rationale field confirms that **Tetrabenazine is a VMAT2 (vesicular monoamine transporter 2) inhibitor**, acting on central monoaminergic neurotransmission, and is clinically associated with treatment of hyperkinetic movement disorders (e.g., chorea, tics).

The top-ranked predicted indication — ADPKD3/polycystic liver disease — is driven by *PKD1/PKD2* mutations and ciliary-protein dysfunction, a completely different biological pathway from monoamine signaling. The evidence pack's own annotation for this candidate states directly: **"無：… 與多囊腎/多囊肝之 PKD1/PKD2 或纖毛蛋白通路無已知交集"** (no known intersection between VMAT2 inhibition and the PKD1/PKD2 or ciliary pathway).

Reviewing all 10 ranked candidates for this drug, the pattern is consistent: every candidate carries an L5 evidence level and a "Hold" recommendation, and most rationale notes explicitly state "無" (none) for mechanistic linkage. The two candidates with any literature link (ranks 5 and 8) only have tangential overlap via "movement disorder" symptom descriptions in unrelated case reports — not direct evidence for the predicted rare renal/hepatic diseases. This is a case where a high TxGNN similarity score is not corroborated by mechanism or literature, and should be treated accordingly.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

*Note: None of the following literature mentions Tetrabenazine, VMAT2, or any pharmacologic intervention — these are background papers describing the biology and clinical management of polycystic kidney/liver disease itself. No literature directly supports drug efficacy for this indication.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Review | Lancet | ADPKD as a systemic disorder — renal cysts, hypertension, liver cysts; no drug repurposing discussion |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Guideline | Journal of Hepatology | EASL guidelines for managing cystic liver disease (tolvaptan discussed, not tetrabenazine) |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Review | Clinics in Liver Disease | Clinical course of ADPKD/PLD; standard therapy is tolvaptan |
| [34724412](https://pubmed.ncbi.nlm.nih.gov/34724412/) | 2022 | Review | Annual Review of Pathology | Mechanisms and treatment advances in polycystic liver disease |
| [36200122](https://pubmed.ncbi.nlm.nih.gov/36200122/) | 2022 | Review | Hepatic Medicine | PLD pathophysiology, diagnosis and treatment overview |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Genetic study | JASN | Genetic overlap between ADPKD and ADPLD (PKD1/2, PRKCSH, SEC63, ALG8, GANAB) |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Genetic study | Advances in Kidney Disease and Health | Genetic spectrum of PKD/PLD phenotypes, ciliary dysfunction |
| [28375157](https://pubmed.ncbi.nlm.nih.gov/28375157/) | 2017 | Genetic study | J Clin Invest | Identifies effector genes of polycystin-1 in isolated PCLD |
| [37943238](https://pubmed.ncbi.nlm.nih.gov/37943238/) | 2023 | Review | Advances in Kidney Disease and Health | Extrarenal manifestations and complications of PLD |
| [30652979](https://pubmed.ncbi.nlm.nih.gov/30652979/) | 2019 | Review | Current Opinion in Gastroenterology | Genetic mechanisms of polycystic liver diseases |

---

## Taiwan Market Information

Tetrabenazine is currently **not marketed in Taiwan** (`market_status: 未上市`), with 0 registered licenses — no product records available.

---

## Safety Considerations

- **Drug Interactions**: 168 total documented interactions on record. Notable entries include:

| Interacting Drug | Level |
|---|---|
| Bupropion | Major |
| Dolasetron | Major |
| Metoclopramide | Major |
| Famotidine | Moderate |
| Loperamide | Moderate |
| Morphine | Moderate |
| Clarithromycin | Moderate |
| Levofloxacin | Moderate |
| Dronabinol / Nabilone | Moderate |
| Metronidazole | Minor |

*(Full list contains 168 interactions; TFDA label warnings and contraindications are currently unavailable — see DG001 below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN similarity score (99.90%), the model's own mechanistic annotation explicitly denies any known biological link between Tetrabenazine's VMAT2/monoamine mechanism and the PKD1/PKD2-driven pathology of this predicted indication. There are zero clinical trials, and all identified literature addresses disease biology only — none references the drug. All 10 top-ranked candidates for this drug share the same L5 evidence tier and "Hold" status, and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001 — currently blocking S1 safety review)
- Confirmed DrugBank MOA record (DG002)
- Any preclinical or in vitro evidence connecting VMAT2/monoaminergic signaling to PKD1/PKD2 or ciliary-pathway biology
- Given the model's own negative mechanistic assessment, consider de-prioritizing this candidate rather than allocating further evidence-collection resources
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

