---
layout: default
title: Pazopanib
parent: 僅模型預測 (L5)
nav_order: 643
evidence_level: L5
indication_count: 10
---

# Pazopanib
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

# Pazopanib: From Advanced Renal Cell Carcinoma to Renal Cell Carcinoma Associated with Neuroblastoma

## One-Sentence Summary

Pazopanib is an oral multi-target tyrosine kinase inhibitor whose established use is in advanced/metastatic renal cell carcinoma (RCC) and non-adipocytic soft tissue sarcoma. The TxGNN model's top-ranked prediction in this Evidence Pack is **Renal Cell Carcinoma Associated with Neuroblastoma** — a rare RCC subtype seen in patients with a prior neuroblastoma history — but this candidate currently has **0 clinical trials** and **0 publications**, making it a pure model-only extrapolation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced/metastatic Renal Cell Carcinoma (inferred from trial/literature context embedded in this Evidence Pack; structured TFDA license text was not available — see India Market Information below) |
| Predicted New Indication | Renal Cell Carcinoma Associated with Neuroblastoma |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Pazopanib's structured mechanism-of-action field is flagged as a data gap in this Evidence Pack (DG002, High severity). However, the rationale text attached to several of the other ranked candidates consistently describes it as an oral multi-target receptor tyrosine kinase inhibitor acting on VEGFR-1/2/3, PDGFR-α/β, and KIT, producing an anti-angiogenic effect. This should be treated as a working characterization pending confirmation against the official label/DrugBank record, not as verified MOA data.

"Renal cell carcinoma associated with neuroblastoma" describes RCC arising in patients with a history of neuroblastoma — nominally still within the RCC family that pazopanib's established anti-angiogenic activity targets. That overlap is the entire basis of the prediction: there is no disease-specific mechanistic finding tying pazopanib to this subgroup, only inheritance from RCC in general.

The Evidence Pack's own rationale for this candidate is explicit about the weakness of that link: *"僅有VEGFR/PDGFR抗血管新生機轉之理論外插，此極罕見共病亞型無任何直接或間接臨床資料支持"* — i.e., theoretical mechanistic extrapolation only, with no direct or indirect clinical evidence. Accordingly this candidate sits at evidence level L5 / decision stage S0 with a Hold recommendation. By contrast, other candidates in this same pack — dermatofibrosarcoma protuberans (L2, Proceed with Guardrails), liposarcoma (L2), fibroblastic neoplasm/desmoid tumor & solitary fibrous tumor (L2), and unclassified RCC (L3) — have completed or ongoing trials plus multiple publications, and are mechanistically better substantiated (e.g., DFSP's COL1A1-PDGFB fusion directly engages pazopanib's PDGFR-β target).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(ClinicalTrials.gov, ICTRP, and PubMed queries for "Pazopanib" + "renal cell carcinoma associated with neuroblastoma" each returned 0 results as of the 2026-03-26 data pull.)*

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Pazopanib is not currently marketed in India — 0 registrations on file, no license records available. No approved-indication text, product names, or dosage forms can be extracted from this Evidence Pack.

---

## Cytotoxicity

This is an antineoplastic/oncology candidate (predicted indication is a cancer; drug is characterized in this pack's rationale text as an oncology-targeted kinase inhibitor).

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target receptor tyrosine kinase inhibitor — VEGFR-1/2/3, PDGFR-α/β, KIT — per rationale text in this Evidence Pack) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Key warnings and contraindications are not available in this Evidence Pack — TFDA label data is flagged as a **Blocking** data gap (DG001), which by itself prevents this candidate from clearing initial safety screening (S1).

**Drug Interactions**: 519 total interactions on file. Of the 20 detailed in this pack, the following are flagged **Major**:

| Interacting Drug | Level |
|---|---|
| Famotidine | Major |
| Ranitidine | Major |
| Rabeprazole | Major |
| Omeprazole | Major |
| Cimetidine | Major |
| Clarithromycin | Major |
| Dexlansoprazole | Major |
| Dolasetron | Major |
| Esomeprazole | Major |

Notably, most Major-level interactions are gastric-acid-reducing agents (H2 blockers, PPIs), consistent with pazopanib's pH-dependent oral absorption. Moderate-level interactions in this list include Pioglitazone, Loperamide, Aprepitant, Dexamethasone, Bisacodyl, Budesonide (oral and nasal), Magnesium oxide, PEG 3350, Saxagliptin, and Eliglustat.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate carries a high TxGNN similarity score (99.63%) but zero direct or indirect clinical evidence (no trials, no literature) and only theoretical mechanistic extrapolation from general RCC biology. A Blocking safety data gap (missing TFDA warnings/contraindications) independently prevents progression past initial safety screening.

**To proceed, the following is needed:**
- TFDA/label warnings and contraindications (DG001, Blocking)
- Confirmed mechanism-of-action data from DrugBank or the official label (DG002, High)
- If this ultra-rare post-neuroblastoma RCC subtype remains of interest, a case-series or registry approach is the realistic first evidentiary step, since rarity likely precludes a randomized trial
- Given the weak evidence base here, consider redirecting repurposing effort within this same Evidence Pack toward higher-evidence Pazopanib candidates already identified: dermatofibrosarcoma protuberans (L2, Proceed with Guardrails), liposarcoma (L2), fibroblastic neoplasm/desmoid tumor (L2), or unclassified RCC (L3)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

