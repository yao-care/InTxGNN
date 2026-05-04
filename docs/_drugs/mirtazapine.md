---
layout: default
title: Mirtazapine
parent: 僅模型預測 (L5)
nav_order: 356
evidence_level: L5
indication_count: 3
---

# Mirtazapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Mirtazapine: From Depression to Ohdo Syndrome and Variants

## One-Sentence Summary

Mirtazapine is a noradrenergic and specific serotonergic antidepressant (NaSSA class), widely used in the treatment of major depressive disorder.
The TxGNN model predicts it may be effective for **Ohdo Syndrome and Variants**, a rare genetic neurodevelopmental disorder,
with **0 clinical trials** and **0 publications** currently supporting this direction — making this a purely computational prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major Depressive Disorder (NaSSA antidepressant) |
| Predicted New Indication | Ohdo Syndrome and Variants |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Mirtazapine belongs to the NaSSA class and acts as an antagonist at presynaptic α2-adrenergic receptors — enhancing the release of both norepinephrine and serotonin — while also blocking postsynaptic 5-HT2A, 5-HT2C, and 5-HT3 receptors as well as histamine H1 receptors. This receptor profile explains its clinical effects: antidepressant action, sedation, and appetite stimulation.

Ohdo Syndrome and Variants are rare genetic neurodevelopmental disorders caused by mutations in chromatin remodeling and transcriptional regulatory genes such as *MED13L*, *KAT6A*, and *SETD5*. These causal mechanisms operate at the level of gene expression regulation and have no direct molecular connection to Mirtazapine's receptor-based pharmacology. The TxGNN model's high prediction score most likely arises from indirect network paths in the knowledge graph — shared phenotypic nodes such as sleep disturbance, behavioral difficulties, and appetite dysregulation appear in both depression and the clinical presentation of Ohdo Syndrome — rather than any genuine disease-modifying mechanism.

In summary, while Mirtazapine's symptomatic properties (sedation, anxiolysis, appetite stimulation) could theoretically address some behavioral features of Ohdo Syndrome in a supportive capacity, there is no biologically plausible basis for a disease-modifying effect. This prediction should be treated as a computational signal requiring experimental validation before any further development consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(Search conducted on 2026-03-27 across ClinicalTrials.gov and ICTRP for all three predicted indications; result count: 0)*

---

## Literature Evidence

Currently no related literature available.

*(PubMed search conducted on 2026-03-27 for Mirtazapine × Ohdo Syndrome, Mirtazapine × BIDS Ohdo type, and Mirtazapine × benign paroxysmal torticollis of infancy; result count: 0 for all queries)*

---

## India Market Information

Mirtazapine currently holds **no regulatory approvals** in India. No product licenses are on record.

---

## Safety Considerations

**Drug Interactions**: Mirtazapine has a total of **324 known drug interactions** (source: DDInter). Selected clinically significant interactions are listed below.

**Major Interactions (require avoidance or close monitoring):**

| Interacting Drug | Level | Clinical Concern |
|-----------------|-------|-----------------|
| Bupropion | Major | Increased seizure risk; CNS toxicity |
| Lorcaserin | Major | Serotonin syndrome risk |
| Dolasetron | Major | QT prolongation; additive serotonergic effects |
| Palonosetron | Major | Serotonin syndrome risk |

**Selected Moderate Interactions:**

| Interacting Drug | Level |
|-----------------|-------|
| Morphine | Moderate |
| Clarithromycin | Moderate |
| Dexamethasone | Moderate |
| Aprepitant | Moderate |
| Cimetidine | Moderate |
| Loperamide | Moderate |
| Famotidine | Moderate |
| Levofloxacin | Moderate |
| Nabilone | Moderate |
| Dronabinol | Moderate |

Complete warnings and contraindications data (TFDA package insert) were not available at the time of this assessment. Please refer to the official package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.42%), Mirtazapine's repurposing potential for Ohdo Syndrome and Variants is not supported by any clinical trials, published literature, or direct mechanistic rationale — the underlying disease pathology (chromatin remodeling gene mutations) is fundamentally distinct from Mirtazapine's neurotransmitter receptor-based pharmacology. All three predicted indications in this Evidence Pack are rated L5, and none meet the threshold for advancement to a safety screening stage.

**To proceed, the following is needed:**

- **MOA data**: Retrieve full DrugBank entry for DB00370 to formally document receptor pharmacology and confirm mechanism assumptions
- **Safety profile**: Download and parse the TFDA (or equivalent) package insert to populate warnings, contraindications, and special population data — currently a blocking gap (DG001)
- **Preclinical plausibility check**: Identify whether any in vitro or animal model data link Mirtazapine (or its receptor targets) to phenotypic features of Ohdo Syndrome (e.g., behavioral, sleep, or feeding endpoints in relevant models)
- **Symptomatic use-case scoping**: If pursuing a purely symptomatic (not disease-modifying) rationale, document the prevalence and severity of sleep and appetite disturbances in Ohdo Syndrome patients to assess clinical need
- **Regulatory pathway**: Mirtazapine has no existing approval in India — any development pathway would require a full NDA submission, significantly raising the bar for proceeding

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

