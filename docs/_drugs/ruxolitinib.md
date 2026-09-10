---
layout: default
title: Ruxolitinib
parent: 僅模型預測 (L5)
nav_order: 751
evidence_level: L5
indication_count: 10
---

# Ruxolitinib
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

Using judgment on evidence selection: TxGNN's top-ranked candidate (uterine PEComa, score 99.73%) has **zero** supporting trials or literature and mechanistically conflicts with ruxolitinib's JAK1/2 pathway (PEComa is TSC/mTOR-driven). I'm reporting instead on the highest-scoring candidate with actual evidentiary support — infection-associated HLH — and flagging this deviation transparently below.

---

# Ruxolitinib: From Myeloproliferative Neoplasms to Infection-Associated Hemophagocytic Lymphohistiocytosis (HLH)

## One-Sentence Summary

> Ruxolitinib is a JAK1/2 inhibitor; the current evidence pack does not contain its original approved indication or mechanism-of-action text (data gap), but it is publicly known as a treatment for myelofibrosis and related myeloproliferative neoplasms.
> Among 10 TxGNN-predicted indications for this drug, the model assigns a near-identical top score to **infection-associated hemophagocytic lymphohistiocytosis (HLH)** — the only candidate among the top 10 backed by an actual randomized trial and a substantial literature base (1 clinical trial cluster, 20 publications), while the single highest-scored prediction (uterine PEComa) has no supporting evidence at all.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not provided in evidence pack (data gap); publicly known use includes myelofibrosis/myeloproliferative neoplasms |
| Predicted New Indication | Infection-associated Hemophagocytic Lymphohistiocytosis (HLH) |
| TxGNN Prediction Score | 99.32% (global model rank 10,805) |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in the evidence pack (data gap DG002). Based on publicly known pharmacology, ruxolitinib is a JAK1/2 tyrosine kinase inhibitor that blocks intracellular signaling downstream of pro-inflammatory cytokines, including interferon-gamma (IFN-γ) and IL-6.

Infection-associated HLH is a cytokine-storm syndrome driven by excessive IFN-γ/IL-6 signaling transmitted through the JAK-STAT pathway. Because ruxolitinib directly inhibits this pathway, the mechanistic link to HLH is strong and specific — unlike most of the other TxGNN top-10 predictions for this drug (e.g., PEComa, lymphangioleiomyomatosis, familial rhabdoid tumor), which are driven by unrelated pathways (TSC1/TSC2-mTOR, SMARCB1 loss) and carry no supporting mechanism or clinical evidence.

This rationale is corroborated by murine mechanistic studies (PMID 31015190, 32530039) showing ruxolitinib dampens IFN-γ-driven T-cell hyperactivation in HLH models, and by a 2022 critical care consensus guideline (PMID 34605776) that references JAK inhibition as part of HLH management in critically ill patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04424056](https://clinicaltrials.gov/study/NCT04424056) | Phase 3 | Unknown | 216 | Randomized trial comparing Anakinra, Tocilizumab alone or combined with Ruxolitinib for severe COVID-19-associated hyperinflammatory disease (stage 2b/3); status unconfirmed (not verified as completed), limiting upgrade to L1 |
| [NCT07424222](https://clinicaltrials.gov/study/NCT07424222) | Phase 1 | Not yet recruiting | 16 | Pilot safety/efficacy study of ruxolitinib in immune-effector-cell–associated HLH-like syndrome (IEC-HS) after CAR-T therapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34605776](https://pubmed.ncbi.nlm.nih.gov/34605776/) | 2022 | Review/Guideline | Critical Care Medicine | Consensus-based guideline for recognition, diagnosis, and management of HLH in critically ill children and adults |
| [31943120](https://pubmed.ncbi.nlm.nih.gov/31943120/) | 2020 | Review | QJM | Adult HLH review covering diagnosis and treatment landscape |
| [35344583](https://pubmed.ncbi.nlm.nih.gov/35344583/) | 2022 | Prospective Cohort | Blood | Ruxolitinib as first-line, response-stratified therapy in pediatric HLH (registered study) |
| [32732367](https://pubmed.ncbi.nlm.nih.gov/32732367/) | 2021 | Pilot/Prospective | Haematologica | Front-line ruxolitinib in 12 children with secondary HLH |
| [40665481](https://pubmed.ncbi.nlm.nih.gov/40665481/) | 2025 | Cohort | British Journal of Haematology | Ruxolitinib-based regimen vs. HLH-94 chemotherapy in 53 pediatric EBV-HLH patients vs. 42 controls |
| [37787838](https://pubmed.ncbi.nlm.nih.gov/37787838/) | 2023 | Cohort/Case series | Annals of Hematology | Sintilimab + ruxolitinib as compassionate therapy in 12 adults with EBV-HLH |
| [38984023](https://pubmed.ncbi.nlm.nih.gov/38984023/) | 2024 | Case series | Translational Pediatrics | Ruxolitinib salvage therapy for refractory adenovirus-associated HLH post-HSCT |
| [31015190](https://pubmed.ncbi.nlm.nih.gov/31015190/) | 2019 | Mechanistic | Blood | Mechanism of ruxolitinib action in murine HLH models — inhibits IFN-γ downstream signaling |
| [32530039](https://pubmed.ncbi.nlm.nih.gov/32530039/) | 2020 | Mechanistic | Blood | JAK/STAT inhibition sensitizes CD8 T cells to dexamethasone-induced apoptosis in hyperinflammation |
| [34353999](https://pubmed.ncbi.nlm.nih.gov/34353999/) | 2021 | Review | Current Opinion in Critical Care | JAK inhibitors (including ruxolitinib) for hospitalized COVID-19-associated hyperinflammation |

---

## Taiwan Market Information

Ruxolitinib currently holds **no registration** in the Taiwan regulatory dataset (`market_status: 未上市`, 0 licenses on file).

---

## Safety Considerations

**Drug Interactions** (338 total interactions on file; selected Major-level examples):
- Clarithromycin — Major
- Cobicistat — Major
- Deferasirox — Major
- Deferiprone — Major
- Ibritumomab tiuxetan — Major
- Tositumomab / Tositumomab (I-131) — Major
- Samarium (153Sm) lexidronam — Major

Detailed key warnings and contraindications are not available in the current evidence pack (data gap DG001 — TFDA label not yet retrieved). Please refer to the package insert for full safety information once obtained.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Infection-associated HLH has a direct, well-characterized mechanistic link to ruxolitinib's JAK1/2 inhibition, and is supported by consensus guidelines, multiple cohort/case-series studies, and mechanistic trial data (L2/S2). However, the one directly relevant Phase 3 RCT (NCT04424056) has unconfirmed completion status, and the drug is not currently marketed in Taiwan.

**To proceed, the following is needed:**
- TFDA label data (warnings/contraindications) — currently blocking (DG001)
- Confirmed mechanism-of-action documentation (DG002)
- Follow-up on NCT04424056 completion/publication status
- Taiwan market-access assessment given zero current registrations
- Evaluation of the 8 other TxGNN-predicted indications in this pack, which currently lack any clinical or literature evidence and should remain on Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

