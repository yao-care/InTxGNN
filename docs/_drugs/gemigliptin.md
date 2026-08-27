---
layout: default
title: Gemigliptin
parent: 僅模型預測 (L5)
nav_order: 310
evidence_level: L5
indication_count: 4
---

# Gemigliptin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the drug-repurposing-report template to produce this from the Evidence Pack (all fields sourced directly from the JSON provided).

Note on adaptation: this pack is from a Taiwan (TFDA) TxGNN instance, not India/CDSCO — I've relabeled the market-status field accordingly to match the actual `taiwan_regulatory` data rather than force the template's India wording.

---

# Gemigliptin: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Gemigliptin is a DPP-4 (dipeptidyl peptidase-4) inhibitor whose established pharmacology centers on the incretin pathway, though its officially recorded original indication is currently a data gap. The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare autosomal recessive skeletal dysplasia, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests entirely on the model's statistical association.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (inferred from DPP-4 inhibitor/incretin-pathway classification referenced in the evidence pack; official indication text is a data gap) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.32% (rank 10,686) |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for gemigliptin is currently a data gap (`original_moa: [Data Gap]`), and no formally recorded original indication is available in this evidence pack. Based on the information that is available — gemigliptin is repeatedly characterized in the model's own rationale as a DPP-4 inhibitor acting on the incretin (GLP-1) pathway, a class of drugs used for type 2 diabetes management.

Opsismodysplasia, however, is a rare skeletal dysplasia caused by mutations in *INPPL1* (SHIP2), which disrupts endochondral ossification — a growth/bone pathway with no established connection to DPP-4 or incretin signaling. The evidence pack's own mechanistic assessment concludes that the high TxGNN score most likely reflects a statistical embedding association in the knowledge graph (possibly via intermediary growth- or metabolism-related nodes) rather than a biologically grounded direct mechanism. Because both the original indication and MOA fields are themselves data gaps, there is no way to cross-validate this linkage against confirmed pharmacology.

It is worth noting that three additional candidates were predicted at nearly identical confidence (thiamine-responsive dysfunction syndrome, focal stiff limb syndrome, and classic stiff person syndrome, all ~99.26–99.28%, ranks ~11,200–11,450). The latter two at least have a plausible — though still unverified — autoimmune/GAD65-diabetes comorbidity rationale for a DPP-4 immunomodulatory hypothesis; opsismodysplasia has the weakest mechanistic plausibility of the four. None of the four candidates have any supporting trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data were all queried but returned no results — DDI query status: `not_found`.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-prediction-only candidate with zero supporting clinical trials or literature, and the proposed mechanistic link between a DPP-4/incretin-pathway drug and a rare skeletal dysplasia driven by *INPPL1* mutation is speculative rather than biologically established. Combined with blocking data gaps in both TFDA labeling information and confirmed MOA, there is currently no basis to move this candidate past the earliest evaluation stage.

**To proceed, the following is needed:**
- TFDA package insert (warnings/precautions and contraindications) — currently a **Blocking** data gap (DG001)
- Confirmed mechanism-of-action data via DrugBank API — currently a **High**-severity data gap (DG002)
- Preclinical or mechanistic studies directly testing DPP-4 inhibition in bone/cartilage development relevant to opsismodysplasia
- Any future clinical trial registrations or case reports connecting gemigliptin (or the DPP-4 inhibitor class) to this indication
- Confirmation of gemigliptin's officially approved original indication(s), since this field is currently empty in the source data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

