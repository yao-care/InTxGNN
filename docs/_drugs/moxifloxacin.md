---
layout: default
title: Moxifloxacin
parent: 僅模型預測 (L5)
nav_order: 437
evidence_level: L5
indication_count: 10
---

# Moxifloxacin
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

# Moxifloxacin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Moxifloxacin is a broad-spectrum fourth-generation fluoroquinolone antibiotic used clinically for bacterial infections including community-acquired pneumonia, complicated skin and skin-structure infections, and intra-abdominal infections.
The TxGNN model predicts it may be effective for **Polyclonal Hyperviscosity Syndrome**, with **0 clinical trials** and **0 publications** currently supporting this direction.
Notably, among all 10 predicted indications, **Bubonic Plague** (rank 10) emerges as the only candidate with a direct mechanistic basis and preclinical evidence (L3), while the majority of top-ranked predictions — including the #1 indication — lack any established clinical or mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from India regulatory data (clinically used for bacterial infections) |
| Predicted New Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data sources queried. Based on established pharmacological knowledge, Moxifloxacin is a fluoroquinolone antibiotic that exerts bactericidal activity by inhibiting bacterial DNA gyrase (GyrA/GyrB) and topoisomerase IV — enzymes essential for DNA replication and transcription in bacteria. This mechanism is entirely directed at prokaryotic targets and has no recognized activity against human cellular pathways.

Polyclonal hyperviscosity syndrome arises from elevated plasma viscosity caused by an excess of polyclonal immunoglobulins, typically driven by inflammatory, autoimmune, or reactive conditions. There is no plausible direct mechanistic link between Moxifloxacin's antibacterial mode of action and the immunoglobulin dysregulation underlying this syndrome. The TxGNN model likely generated this prediction through indirect knowledge graph connections — for instance, associating chronic bacterial infections as potential drivers of polyclonal immunoglobulin elevation — rather than any direct therapeutic pathway.

The high TxGNN score (99.98%) reflects model confidence based on graph topology and co-occurrence patterns, not clinical efficacy. Without mechanistic plausibility and with zero supporting evidence, this prediction should be treated as a graph artifact rather than a repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Moxifloxacin has no approved registrations in India in the current dataset. No authorization records, product names, dosage forms, or approved indications are available for review.

---

## Safety Considerations

**Drug Interactions** (336 total interactions identified; Major-level interactions highlighted below):

| Interacting Drug | Level | Clinical Concern |
|-----------------|-------|-----------------|
| Hydrocortisone | Major | QT prolongation risk via electrolyte imbalance (hypokalemia) |
| Dexamethasone | Major | QT prolongation risk via electrolyte imbalance (hypokalemia) |
| Betamethasone | Major | QT prolongation risk via electrolyte imbalance (hypokalemia) |
| Triamcinolone | Major | QT prolongation risk via electrolyte imbalance (hypokalemia) |
| Bupropion | Major | Fluoroquinolones lower seizure threshold; additive CNS risk |
| Chlorpropamide | Major | Risk of hypoglycemia with fluoroquinolones |

Representative moderate interactions (total 336 documented) include: Acarbose, Famotidine, Metformin, Pioglitazone, Alogliptin, Canagliflozin, Albiglutide, Loperamide, Acetylsalicylic acid, Balsalazide, Bisacodyl, Calcium Phosphate, Calcium acetate, and Potassium citrate.

> The QT-prolongation risk associated with Moxifloxacin is clinically significant enough that it was selected as the **positive control drug** in a cardiac repolarisation study (NCT07023029), reinforcing that this is an established, well-characterized safety signal.

Please refer to the package insert for complete warnings and contraindications, as formal labeling data was not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (polyclonal hyperviscosity syndrome) has zero mechanistic plausibility, no clinical trial support, and no published literature — meeting only the L5 threshold (model prediction only). Proceeding with development based solely on a graph score is not justified.

**Broader Landscape Across All 10 Predicted Indications:**

Of the 10 predicted indications reviewed, the evidence quality is generally poor for repurposing purposes:

| Rank | Indication | Evidence Level | Recommendation | Notes |
|------|-----------|---------------|----------------|-------|
| 1 | Polyclonal hyperviscosity syndrome | L5 | Hold | No mechanistic link, no evidence |
| 2 | Hyperamylasemia | L5 | Hold | Potential safety concern (fluoroquinolones linked to pancreatitis) |
| 3 | Congenital analbuminemia | L5 | Hold | Only incidental case report; no link to Moxifloxacin |
| 4 | Blood group incompatibility | L5 | Hold | No mechanistic link; transfusion medicine domain |
| 5 | Premalignant hematological system disease | L5 | Hold | Indirect immunodeficiency connection only |
| 6 | Monoclonal gammopathy | L4 | Hold | Evidence reflects infection management in immunocompromised patients, not disease treatment |
| 7 | Hematological disease with peripheral neuropathy | L5 | Hold | **Safety concern**: fluoroquinolones may worsen peripheral neuropathy |
| 8 | Congenital hematological disorder | L4 | Hold | Moxifloxacin appears as QT positive control, not treatment |
| 9 | Hematopoietic and lymphoid system neoplasm | L5 | Hold | No antitumour mechanism |
| **10** | **Bubonic plague** | **L3** | **Research Question** | **Direct mechanistic link; multiple animal and in vitro PK/PD studies confirm activity against *Yersinia pestis*** |

**Bubonic plague is the only indication warranting further attention.** Moxifloxacin inhibits *Y. pestis* DNA gyrase with potent in vitro activity, and is already referenced in CDC bioterrorism response guidelines as an alternative to streptomycin. Multiple animal studies and in vitro PK/PD models confirm efficacy. The absence of human clinical trials reflects the ethical impracticality of conducting plague RCTs, not lack of scientific basis.

**To advance the Bubonic Plague indication to the next stage, the following is needed:**

- Formal MOA data retrieval from DrugBank API (DG002 remediation)
- Review of TFDA/India regulatory package insert for warnings and contraindications (DG001 remediation)
- Assessment of regulatory pathway as a bioterrorism countermeasure (Emergency Use Authorization framework)
- Systematic review of existing animal-to-human dose extrapolation data
- QT monitoring protocol design given Moxifloxacin's established cardiac safety signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

