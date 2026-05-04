---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinol: From Gout / Hyperuricemia to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a xanthine oxidase (XO) inhibitor with a well-established role in treating gout, hyperuricemia, and preventing tumor lysis syndrome.
The TxGNN model predicts it may be effective for **Hepatic Porphyria**, with **0 clinical trials** and **2 publications** currently supporting this direction.
Evidence remains at the preclinical/mechanistic level (L4), and a critical bidirectional safety concern — Allopurinol may paradoxically worsen acute porphyric attacks — makes safety clarification an absolute prerequisite before any forward progression.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout, hyperuricemia, tumor lysis syndrome prevention |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Allopurinol is a structural analogue of hypoxanthine that competitively inhibits xanthine oxidase (XO), blocking the conversion of hypoxanthine and xanthine to uric acid. This reduces serum urate levels and forms the basis of its efficacy in gout and hyperuricemia.

Two mechanistic pathways connect Allopurinol to hepatic porphyria. First, XO inhibition reduces reactive oxygen species (ROS) generation; since oxidative stress can dysregulate heme biosynthesis, a reduced ROS burden could theoretically dampen aberrant porphyrin accumulation. Second, Allopurinol may indirectly modulate ALAS1 (5-aminolevulinate synthase 1) — the rate-limiting, feedback-controlled enzyme in heme biosynthesis. ALAS1 upregulation is the central driver of acute porphyric attacks, particularly in Porphyria Cutanea Tarda (PCT), making it a compelling but delicate regulatory target.

There is, however, a critical bidirectional risk: in acute hepatic porphyrias, some evidence suggests that Allopurinol can itself upregulate ALAS1, potentially precipitating or worsening porphyric attacks. This paradoxical hazard means that safety evaluation must be fully resolved before any efficacy work proceeds. The TxGNN model's high confidence score most likely reflects shared knowledge-graph node proximity between Allopurinol, purine metabolism, and heme pathway diseases — not direct therapeutic proof.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis / Mechanistic Review | Medical Hypotheses | Proposes metabolic targeting of hepatic ALAS1 by inhibiting heme utilisation through tryptophan 2,3-dioxygenase (TDO) as a novel therapy for acute hepatic porphyrias; provides theoretical framework linking the hepatic heme regulatory pool to porphyric attack triggers, relevant to any drug acting on this axis |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal Study (Rat) | Biochemical Pharmacology | Demonstrated that carbamazepine exacerbates hepatic porphyria by depleting the hepatic heme pool via tryptophan pyrrolase induction; establishes the heme utilisation–ALAS1 negative-feedback axis as the core safety screening framework for drugs evaluated in porphyria |

---

## India Market Information

Allopurinol currently has no registered products in India. No regulatory license data is available.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No registrations on record |

---

## Safety Considerations

**Drug Interactions (217 total identified; top interactions listed below):**

| Interacting Drug | Severity |
|-----------------|----------|
| Aluminum hydroxide | Moderate |
| Attapulgite | Moderate |
| Kaolin | Moderate |
| Magaldrate | Moderate |
| Sucralfate | Moderate |
| Amoxicillin | Minor |
| Chlorpropamide | Minor |
| Glimepiride | Unknown |
| Metformin | Unknown |
| Morphine | Unknown |
| Omeprazole | Unknown |
| Pantoprazole | Unknown |
| Mesalazine | Unknown |

> Complete warning and contraindication data are not available in this Evidence Pack. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only two mechanistic/animal-level publications support this repurposing direction (L4), with no clinical trials registered in hepatic porphyria. More critically, Allopurinol carries a documented bidirectional risk in acute porphyric conditions — it may paradoxically upregulate ALAS1 and precipitate attacks — making safety clarification a blocking requirement before this candidate can advance.

**To proceed, the following is needed:**

- **Porphyrinogenicity screening**: Verify whether Allopurinol is listed as a porphyria-unsafe or porphyria-safe drug in established reference databases (e.g., European Porphyria Network drug database, NAPOS, Drug Database for Acute Porphyria)
- **Full MOA documentation**: Retrieve mechanism of action data from DrugBank (DB00437) to confirm the ALAS1–XO pathway interaction hypothesis
- **CDSCO / package insert review**: Obtain complete warnings, contraindications, and hepatic safety data to enable S1 safety pre-screening
- **Porphyria subtype stratification**: Distinguish between Porphyria Cutanea Tarda (PCT, non-acute) and Acute Intermittent Porphyria (AIP, acute) — Allopurinol's risk profile may differ substantially between subtypes
- **Preclinical in vivo study**: Design a study in an established porphyria animal model (e.g., phenobarbital-induced AIP mouse model or uroporphyrinogen decarboxylase-deficient PCT model) to determine whether Allopurinol reduces or worsens porphyrin accumulation
- **If safety signals are cleared**: Consider a Phase 2 proof-of-concept trial in PCT patients, where the oxidative-stress/heme-regulatory mechanistic rationale is most biologically plausible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

