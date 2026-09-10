---
layout: default
title: Sorafenib
parent: 僅模型預測 (L5)
nav_order: 776
evidence_level: L5
indication_count: 10
---

# Sorafenib
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

# Sorafenib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Sorafenib is a multi-target tyrosine kinase inhibitor originally approved for renal cell carcinoma (RCC) and hepatocellular carcinoma (HCC). The TxGNN model predicts it may also be effective for **Liposarcoma**, with **2 clinical trials** and **8 publications** currently supporting this direction — including one completed Phase 2 trial that directly tested sorafenib in advanced soft tissue sarcoma.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Renal cell carcinoma (also approved for hepatocellular carcinoma; no formal original-indication field on file, inferred from evidence-pack rationale/literature) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available directly from DrugBank in this evidence pack (flagged as a High-severity data gap, DG002). Based on the mechanistic rationale attached to this candidate, sorafenib is a multi-target kinase inhibitor acting on the RAF/MEK/ERK signaling cascade as well as VEGFR-1/2/3, PDGFR-β, and c-KIT — the same anti-angiogenic and anti-proliferative machinery that underlies its approved use in renal cell carcinoma and hepatocellular carcinoma.

Liposarcoma, particularly the dedifferentiated subtype, frequently shows PTEN down-regulation with consequent activation of RTK/MAPK signaling (supported by preclinical xenograft data, PMID 23416162), giving a plausible molecular link to sorafenib's mechanism. Soft tissue sarcomas as a broader class have shown activity signals with sorafenib and related multikinase inhibitors (regorafenib), which supports biological plausibility.

However, monotherapy response rates for sorafenib across soft tissue sarcoma have generally been modest in completed trials, so the mechanistic rationale is reasonable but not yet strongly validated by efficacy data specific to liposarcoma.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00217620](https://clinicaltrials.gov/study/NCT00217620) | Phase 2 | Completed | 51 | Direct sorafenib (BAY 43-9006) trial in advanced soft tissue sarcomas (includes liposarcoma); tests anti-angiogenic/anti-proliferative activity. |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 basket study of regorafenib (sorafenib-related multikinase inhibitor) across selected sarcoma subtypes, building on prior sorafenib activity signals in sarcoma. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21751200](https://pubmed.ncbi.nlm.nih.gov/21751200/) | 2012 | RCT (Phase 2) | Cancer | SWOG S0505: sorafenib in advanced soft tissue sarcoma — evaluates a multitargeted TKI (RAF, VEGFR1-3, PDGFR-β, KIT) relevant to sarcoma biology. |
| [24554062](https://pubmed.ncbi.nlm.nih.gov/24554062/) | 2014 | Phase 1 Trial | Annals of Surgical Oncology | Neoadjuvant conformal radiotherapy plus sorafenib in extremity soft tissue sarcoma, based on synergy between anti-angiogenic therapy and RT. |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Review | Frontiers in Oncology | PDOX mouse models identify effective combination therapies (incl. CDK inhibitor palbociclib) for sarcoma; relevant to multi-pathway targeting rationale. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Histology-subtype-directed medical treatment of soft tissue sarcomas, including targeted therapy options. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Annals of Oncology | Histology- and non-histology-driven therapy in soft tissue sarcoma, noting trabectedin's high activity specifically in myxoid liposarcoma. |
| [18413802](https://pubmed.ncbi.nlm.nih.gov/18413802/) | 2008 | Preclinical | Molecular Cancer Therapeutics | Sorafenib inhibits growth and MAPK signaling in dedifferentiated liposarcoma cell lines (LS141, DDLS), supporting direct in vitro activity. |
| [23416162](https://pubmed.ncbi.nlm.nih.gov/23416162/) | 2013 | Preclinical (Xenograft) | American Journal of Pathology | Novel dedifferentiated liposarcoma xenograft models show PTEN down-regulation as a malignant signature, informing PI3K/RTK pathway targeting rationale. |
| [25075796](https://pubmed.ncbi.nlm.nih.gov/25075796/) | 2014 | Case Report | Anti-Cancer Drugs | Response to trabectedin (different drug) in synovial sarcoma with lung metastases — indirect sarcoma-class context only. |

---

## India Market Information

Sorafenib is currently **not marketed in India** per the available registry data (0 registrations on file). No authorization number, product name, dosage form, or approved indication text is available for extraction.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor: RAF/MEK/ERK, VEGFR, PDGFR-β, c-KIT) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: A total of **509 documented drug-drug interactions** were catalogued (source: DDInter). One **Major**-level interaction was flagged with **Dolasetron**. Multiple **Moderate**-level interactions were identified, including Famotidine, Loperamide, Dexamethasone, Clarithromycin, Levofloxacin, Palonosetron, Naldemedine, Naltrexone, Metreleptin, Bisacodyl, Cholic Acid, Picosulfuric acid, Polyethylene glycol (3350 with electrolytes), Sodium sulfate, Lactitol, and Lactulose. **Minor**-level interactions were noted with Dapagliflozin, Naloxegol, and Metronidazole.

Key warnings and contraindications are not available in the current evidence pack (blocked pending TFDA package insert retrieval — DG001). Please refer to the package insert for complete safety information once available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 trial directly tested sorafenib in advanced soft tissue sarcoma (including liposarcoma), and preclinical/xenograft data support a PTEN/RTK-MAPK mechanistic link specific to dedifferentiated liposarcoma. However, monotherapy efficacy across soft tissue sarcoma has been modest, and this drug is currently unregistered in India, so guardrails are warranted before clinical application.

**To proceed, the following is needed:**
- TFDA/local package insert data to close the Blocking safety gap (DG001) before any S1 safety review can proceed
- DrugBank-sourced mechanism of action detail to formally close DG002
- Liposarcoma-subtype-specific efficacy data (especially dedifferentiated subtype) to confirm PTEN-pathway responsiveness beyond the single completed Phase 2 trial
- Confirmation of India market authorization pathway, since the drug currently has zero registrations on file

---

## Appendix: Other Predicted Indications Screened

This evidence pack screened 10 candidate indications for sorafenib. For completeness, the other 9 ranked predictions are summarized below (not detailed in the main report body, which follows the top-ranked candidate):

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|-----------------|-----------------|
| 2 | Ovarian myxoid liposarcoma | 99.76% | L4 | Research Question |
| 3 | RCC with Xp11.2/TFE3 fusion | 99.65% | L4 | Research Question |
| 4 | RCC associated with neuroblastoma | 99.65% | L4 | Research Question |
| 5 | Unclassified renal cell carcinoma | 99.65% | **L1** | Proceed with Guardrails |
| 6 | Childhood kidney cell carcinoma | 99.57% | L2 | Research Question |
| 7 | Female breast carcinoma | 99.53% | L2 | **Hold** |
| 8 | Renal pelvis carcinoma | 99.40% | L2 | Research Question |
| 9 | Vulva sarcoma | 99.37% | L4 | Research Question |
| 10 | Dermatofibrosarcoma protuberans | 99.35% | L4 | Research Question |

Notably, **Unclassified RCC (Rank 5)** carries the highest evidence level (L1) of the entire set, supported by a completed Phase 3 sequencing trial (NCT01613846, n=544) — this candidate may warrant a dedicated evaluation report in its own right. Conversely, **Female breast carcinoma (Rank 7)** accumulated 14 clinical trials but a "Hold" recommendation, as most trials were early-phase, terminated, or of unknown status without any resulting approved indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

