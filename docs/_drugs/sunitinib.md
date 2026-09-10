---
layout: default
title: Sunitinib
parent: 僅模型預測 (L5)
nav_order: 794
evidence_level: L5
indication_count: 10
---

# Sunitinib
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

# Sunitinib: From GIST / Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

> Sunitinib is a multi-target receptor tyrosine kinase inhibitor originally used for gastrointestinal stromal tumor (GIST) and renal cell carcinoma (this evidence pack contains no Taiwan-specific approved-indication text — see Data Gaps below; the original-indication reference here is drawn from mentions within the trial descriptions in this evidence pack).
> The TxGNN model predicts it may also be effective for **Liposarcoma**,
> with **3 clinical trials** and **no dedicated publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | GIST, Renal Cell Carcinoma (inferred from trial descriptions in this evidence pack; formal Taiwan-approved indication text not available) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L2 |
| Taiwan Market Status | Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in the formal drug record (flagged as a High-severity data gap, DG002). Based on the mechanistic rationale captured elsewhere in this evidence pack, Sunitinib is a multi-target receptor tyrosine kinase inhibitor that blocks VEGFR1-3, PDGFRα/β, and KIT. Its efficacy in renal cell carcinoma and GIST is well established internationally, and this same anti-angiogenic/anti-PDGFR activity is mechanistically plausible in other solid tumors that depend on these pathways.

Liposarcoma — particularly the myxoid and dedifferentiated subtypes — frequently shows angiogenesis dependence and, in a subset of cases, PDGFR pathway dysregulation, providing biological plausibility for repurposing. However, liposarcoma is not primarily driven by classic Sunitinib targets in the way GIST (KIT-driven) or clear-cell RCC (VHL/VEGF-driven) are; well-known liposarcoma drivers such as MDM2 amplification fall outside Sunitinib's known target spectrum. As a result, the mechanistic link is assessed as moderate strength rather than direct.

Supporting this plausibility, the available trials were not designed exclusively for liposarcoma but enrolled it as part of a broader soft-tissue sarcoma (STS) population, meaning liposarcoma-specific efficacy signals are diluted within mixed-histology results.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Phase 2 | Completed | 48 | Open-label single-site study of Sunitinib malate in unresectable/metastatic soft tissue sarcoma (leiomyosarcoma, liposarcoma, fibrosarcoma, MFH); dose given days 1–28 of a 42-day cycle. Relevance grade B — broad sarcoma umbrella trial, not liposarcoma-specific. |
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Phase 2 | Completed | 53 | Multicenter continuous-dosing study of Sunitinib in non-GIST sarcomas, including metastatic/locally advanced/recurrent disease. Relevance grade B — liposarcoma likely a subgroup, not the primary endpoint population. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 blanket protocol studying oral kinase inhibitors across selected sarcoma subtypes. **Note: the study drug tested was regorafenib, not sunitinib** — relevance grade C, cannot be used as direct sunitinib evidence. |

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Currently not marketed in Taiwan (market status: 未上市); no license/registration records are available in this evidence pack.

---

## Cytotoxicity

Sunitinib is an antineoplastic agent (multi-target receptor tyrosine kinase inhibitor), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — multi-target receptor tyrosine kinase inhibitor (VEGFR1-3 / PDGFRα/β / KIT) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: DDI query returned **405 total interactions**. Notable examples include:
  - **Major**: Dolasetron
  - **Moderate**: Famotidine, Loperamide, Dexamethasone, Bisacodyl, Chlorpropamide, Clarithromycin, Picosulfuric acid, Polyethylene glycol (3350 with electrolytes), Palonosetron, Glimepiride, Sodium sulfate, and multiple insulin formulations (aspart, degludec, detemir, glargine, glulisine, human isophane, human regular, inhaled rapid-acting)

Key warnings and contraindications are not available in this evidence pack (flagged as Blocking-severity data gap, DG001 — TFDA label warnings/contraindications). Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for liposarcoma specifically is limited to Phase 2 sarcoma-umbrella trials in which liposarcoma is a subgroup rather than the primary study population (Evidence Level L2, Decision Stage S2 — "Research Question"), and the mechanistic link, while plausible, is only moderate strength given liposarcoma's typical MDM2-driven biology. Combined with the drug's non-marketed status in Taiwan and blocking safety data gaps, this candidate is not yet ready to proceed.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (Blocking gap, DG001)
- Formal MOA documentation (High-priority gap, DG002)
- Liposarcoma-specific (rather than mixed-sarcoma) clinical trial or cohort data
- Taiwan regulatory/licensing pathway assessment given current "not marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

