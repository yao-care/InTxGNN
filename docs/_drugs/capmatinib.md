---
layout: default
title: Capmatinib
parent: 僅模型預測 (L5)
nav_order: 139
evidence_level: L5
indication_count: 10
---

# Capmatinib
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

---

# Capmatinib: From Non-Small Cell Lung Cancer (METex14) to Rheumatoid Arthritis

## One-Sentence Summary

Capmatinib (Tabrecta) is a selective c-Met tyrosine kinase inhibitor approved by the FDA for adults with metastatic non-small cell lung cancer (NSCLC) harboring MET exon 14 (METex14) skipping mutations.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 clinical trials** and **1 publication** (a broad narrative review of kinase inhibitors, not specific to RA) currently supporting this direction. Evidence for this repurposing direction is minimal and remains at the hypothesis stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | NSCLC with MET exon 14 skipping mutations (FDA-approved; not registered in India) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Capmatinib is a highly selective inhibitor of the MET (c-Met / hepatocyte growth factor receptor) tyrosine kinase. In its approved oncology indication, it works by blocking MET phosphorylation triggered by aberrant METex14 splicing, thereby suppressing downstream RAS/MAPK and PI3K/AKT signaling that drives tumor cell proliferation and survival. Detailed MOA data was not available from this Evidence Pack, but the mechanism above is well-established from the approved label.

The biological rationale for exploring Capmatinib in Rheumatoid Arthritis centers on the role of the HGF/c-Met axis in synovial pathology. In RA joints, c-Met is overexpressed in synovial fibroblasts (FLS). When HGF activates MET in these cells, it promotes FLS proliferation, migration, resistance to apoptosis, secretion of pro-inflammatory cytokines (IL-6, MMP-1/3), and angiogenesis — all of which drive the pannus formation and joint destruction characteristic of progressive RA. Blocking MET could theoretically interrupt this cascade.

However, this mechanistic bridge is entirely inferential at this stage. The Evidence Pack retrieved no preclinical RA studies using Capmatinib, no registered clinical trials, and only one general-purpose narrative review of FDA-approved kinase inhibitors. The prediction likely reflects the density of HGF/MET pathway nodes within the TxGNN knowledge graph connecting oncology and inflammatory disease rather than direct experimental validation. Caution is warranted before allocating resources to this direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Capmatinib in Rheumatoid Arthritis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Narrative Review | Pharmacological Research | Comprehensive survey of 62 FDA-approved small molecule kinase inhibitors including MET inhibitors; does not investigate Capmatinib in RA specifically — included as background on kinase inhibitor class |

---

## India Market Information

Capmatinib is not registered or marketed in India. No CDSCO-approved products are on record as of the data cutoff (2026-06-21).

---

## Cytotoxicity

Capmatinib is an antineoplastic targeted therapy approved for cancer treatment and meets the criteria for inclusion of this section.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Selective MET (c-Met) tyrosine kinase inhibitor |
| Myelosuppression Risk | Low (peripheral edema, nausea, and vomiting are more common than hematologic toxicity in the approved oncology indication) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function (ALT/AST/bilirubin), renal function (creatinine), pulmonary function / chest imaging (interstitial lung disease / pneumonitis monitoring), QTc interval (ECG), peripheral edema |
| Handling Protection | Follow institutional cytotoxic drug handling protocols applicable to oral targeted oncology agents |

---

## Safety Considerations

All safety data fields (key warnings, contraindications, drug interactions) were not retrievable from this Evidence Pack.

> Please refer to the Tabrecta (Capmatinib) package insert for complete safety information, including known risks of interstitial lung disease/pneumonitis, peripheral edema, embryo-fetal toxicity, and photosensitivity reactions. Note also that MET inhibitors as a class may affect cardiac conduction (QTc prolongation); this is particularly relevant when considering repurposing into non-oncology populations where baseline monitoring intensity may differ.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests entirely on the TxGNN model score (L5); there are no registered clinical trials, no preclinical RA studies with Capmatinib, and no direct literature support for this indication. While the HGF/MET pathway is mechanistically active in RA synovium, the hypothesis has not been experimentally tested in this context, and the single retrieved publication does not address RA at all.

**To proceed, the following is needed:**

- **Safety baseline**: Download and parse the Tabrecta package insert to complete S1 safety screening — this is a blocking data gap before any further evaluation
- **MOA documentation**: Retrieve full DrugBank entry (DB11791) to confirm mechanism and known off-target effects
- **Preclinical feasibility**: Conduct a targeted literature search for MET inhibitors (broader class: tivantinib, tepotinib, crizotinib) in RA animal models (e.g., collagen-induced arthritis) to validate the pathway hypothesis before committing to Capmatinib specifically
- **Sub-indication scoping**: "Rheumatoid Arthritis" is a heterogeneous disease — identify whether the target population would be refractory RA with documented elevated HGF/MET synovial expression, which is a more tractable and addressable hypothesis
- **Dose-exposure assessment**: Evaluate whether NSCLC therapeutic doses (400 mg BID) are compatible with tolerability expectations in a non-cancer RA population with long-term use requirements
- **Reverse safety check**: Verify that Capmatinib's known AEs (ILD, peripheral edema, QTc effects, photosensitivity) are acceptable for chronic RA dosing, where the risk-benefit calculus differs substantially from terminal cancer
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

