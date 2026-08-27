---
layout: default
title: Ketoprofen
parent: 僅模型預測 (L5)
nav_order: 361
evidence_level: L5
indication_count: 10
---

# Ketoprofen
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

# Ketoprofen: From Pain and Inflammatory Conditions to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ketoprofen is a propionic acid non-steroidal anti-inflammatory drug (NSAID), conventionally used for pain management and inflammatory conditions.
The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type** with a prediction score of 99.98%,
however **0 clinical trials and 0 publications** currently support this direction — indicating that the high score most likely reflects a knowledge graph topology artifact rather than a clinically actionable therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no India regulatory approval on record) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Ketoprofen is a non-selective COX-1/COX-2 inhibitor belonging to the propionic acid NSAID class. It acts by blocking cyclooxygenase enzymes, thereby reducing the synthesis of prostaglandins (PGE2) and prostacyclins (PGI2) — key mediators of pain, fever, and inflammation. This mechanism underlies its established role in musculoskeletal and inflammatory conditions such as rheumatoid arthritis, osteoarthritis, and spondyloarthropathies.

Acromesomelic dysplasia, Hunter-Thompson type is a rare autosomal recessive skeletal dysplasia caused by loss-of-function mutations in the **GDF5 (CDMP1)** gene. The resulting defect in GDF5/BMP signaling disrupts chondrogenesis and skeletogenesis, producing disproportionate shortening of the middle and distal limb segments. This is a developmental genetic disease, not an inflammatory condition.

There is no established or theoretically plausible mechanistic link between Ketoprofen's COX inhibitory activity and the GDF5/BMP morphogenetic signaling axis. The 99.98% TxGNN score most likely arises from **non-specific topological clustering** of skeletal disease nodes within the knowledge graph — a recognized limitation of graph-based machine learning when disease node neighborhoods overlap structurally but not biologically. This prediction should be treated as a model artifact requiring no further clinical translation effort.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions**: Ketoprofen has **226 recorded drug interactions** in the DDInter database. Key interactions by severity level are summarized below:

| Severity | Interacting Drugs |
|----------|-------------------|
| **Moderate** | Hydrocortisone, Triamcinolone, Dexamethasone, Betamethasone, Budesonide, Acetylsalicylic acid, Metformin, Chlorpropamide, Glimepiride, Mesalazine, Balsalazide, Naltrexone, Potassium citrate, Potassium bicarbonate, Picosulfuric acid, Polyethylene glycol (3350 with electrolytes) |
| **Minor** | Famotidine, Ranitidine, Cimetidine, Linaclotide |

> Key warnings and contraindications are currently unavailable in this evidence pack. Please refer to the approved package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-predicted indication — acromesomelic dysplasia, Hunter-Thompson type — has no mechanistic rationale connecting Ketoprofen's COX inhibitory pathway to the underlying GDF5/BMP skeletal morphogenesis defect. With zero clinical trials and zero supporting publications, this is classified as an L5 prediction and likely represents a knowledge graph false positive due to skeletal disease node topology.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking)**: Retrieve CDSCO/TFDA package insert PDF to extract key warnings and contraindications — required before any safety pre-screening (S1 stage) can be initiated
- **Resolve DG002 (High)**: Query DrugBank API for complete MOA data to enable mechanistic relevance analysis across all predicted indications
- **Reprioritize candidate evaluation**: Among the 10 predicted indications, **Spondyloarthropathy (Rank 8, TxGNN 99.86%, Evidence Level L4)** presents a substantially stronger case — NSAIDs are ASAS/EULAR first-line agents for this condition, and 1 supporting literature reference (PMID [20470931](https://pubmed.ncbi.nlm.nih.gov/20470931/)) provides indirect validation; this candidate warrants a dedicated follow-on evaluation report
- **India market entry assessment**: Ketoprofen has no India registration on record; if repurposing development proceeds for any indication, a market feasibility analysis and regulatory pathway review will be required
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

