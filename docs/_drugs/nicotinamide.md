---
layout: default
title: Nicotinamide
parent: 僅模型預測 (L5)
nav_order: 460
evidence_level: L5
indication_count: 0
---

# Nicotinamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Nicotinamide: From Vitamin B3 Deficiency — Repurposing Prediction Pending

## One-Sentence Summary

Nicotinamide (Niacinamide) is the amide form of Vitamin B3, historically used to prevent and treat pellagra and niacin deficiency.
**No TxGNN repurposing prediction is available in this evidence pack** — the candidate has 0 registered licenses in India and two blocking data gaps (MOA and package insert).
A formal repurposing assessment cannot be completed until TxGNN output and regulatory safety data are retrieved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vitamin B3 deficiency (Pellagra) — based on general pharmacological background; not documented in regulatory data |
| Predicted New Indication | Not available — TxGNN prediction pending |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — No prediction or supporting studies linked to a specific indication |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why a Repurposing Assessment Cannot Yet Be Made

No TxGNN predicted indication is present in this evidence pack (`predicted_indications: []`), so no mechanistic bridging analysis can be performed.

Currently, detailed mechanism of action data is also not available. Based on known pharmacology, Nicotinamide is the amide form of niacin (Vitamin B3) and serves as a direct precursor to the coenzymes NAD⁺ and NADP⁺. These coenzymes are essential for cellular energy metabolism, DNA repair (PARP activity), and redox signalling — a broad mechanistic footprint that underlies research interest across metabolic, inflammatory, neurodegenerative, and dermatological disease areas.

The drug-drug interaction profile in this evidence pack is noteworthy: 64 interactions are documented, the majority involving antidiabetic agents (SGLT2 inhibitors, GLP-1 agonists, DPP-4 inhibitors, Metformin, Pioglitazone, Chlorpropamide, Acarbose). This pattern is consistent with research interest in metabolic or endocrine indications — such as type 1 diabetes prevention, where nicotinamide has been studied in large trials (e.g., ENDIT). However, without confirmed TxGNN predictions, no specific new indication can be formally evaluated or scored.

---

## Safety Considerations

**Drug-Drug Interactions — 64 interactions identified (source: DDInter)**

Key interactions by category:

| Interacting Drug | Severity | Therapeutic Class |
|-----------------|----------|-------------------|
| Canagliflozin | Moderate | SGLT2 inhibitor |
| Dapagliflozin | Moderate | SGLT2 inhibitor |
| Empagliflozin | Moderate | SGLT2 inhibitor |
| Albiglutide | Moderate | GLP-1 agonist |
| Dulaglutide | Moderate | GLP-1 agonist |
| Alogliptin | Moderate | DPP-4 inhibitor |
| Linagliptin | Moderate | DPP-4 inhibitor |
| Metformin | Moderate | Biguanide |
| Pioglitazone | Moderate | Thiazolidinedione |
| Chlorpropamide | Moderate | Sulfonylurea |
| Acarbose | Moderate | Alpha-glucosidase inhibitor |
| Methotrexate | Moderate | Antimetabolite / DMARD |
| Efavirenz | Moderate | NNRTI antiretroviral |
| Clofarabine | Moderate | Purine nucleoside analogue |
| Brentuximab vedotin | Moderate | ADC antineoplastic |
| Asparaginase (E. coli / Erwinia / Calaspargase) | Moderate | Antineoplastic enzyme |
| Cannabidiol | Moderate | Cannabinoid |
| Carbamazepine | Minor | Anticonvulsant |

> Key warnings and contraindications are not available — the regulatory package insert (DG001) has not been retrieved and is currently a **Blocking** data gap.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This evidence pack contains no TxGNN predicted indications and is missing both MOA documentation and India regulatory safety data, making it impossible to evaluate any specific repurposing hypothesis. Nicotinamide is not currently marketed in India under any registered license.

**To proceed, the following is needed:**

- **[Critical]** Run TxGNN prediction pipeline for Nicotinamide — `predicted_indications` is currently empty and is the prerequisite for all downstream analysis
- **[Blocking]** Retrieve package insert warnings and contraindications from the regulatory authority (DG001) — required before any safety assessment can proceed
- **[High]** Query DrugBank API for MOA data (DG002) — needed to assess mechanistic plausibility once a target indication is identified
- **[Advisory]** Clarify research intent: the DDI profile is dominated by antidiabetic agents, suggesting a metabolic indication is likely under consideration (e.g., type 1 diabetes prevention, NAFLD) — this should be confirmed against TxGNN output before evidence collection begins
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

