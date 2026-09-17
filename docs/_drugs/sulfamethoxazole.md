---
layout: default
title: Sulfamethoxazole
parent: Model Prediction Only (L5)
nav_order: 790
evidence_level: L5
indication_count: 1
---

# Sulfamethoxazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Sulfamethoxazole: From Antibacterial Use to Acute Contagious Conjunctivitis

## One-Sentence Summary

> Sulfamethoxazole is a sulfonamide-class antibacterial agent; its original approved indication is not specified in the current evidence pack.
> The TxGNN model predicts it may be effective for **Acute Contagious Conjunctivitis**,
> currently supported by **0 clinical trials** and **1 publication**, with key drug-level data (mechanism of action, label warnings) still pending.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (data gap) |
| Predicted New Indication | Acute Contagious Conjunctivitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L3 (single observational study, no RCTs) |
| Taiwan Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Sulfamethoxazole is currently not available (flagged as data gap DG002, pending DrugBank API lookup). Based on known pharmacological class information, Sulfamethoxazole is a sulfonamide antibacterial, a drug class with a long history of topical ophthalmic use (e.g., sulfacetamide) for bacterial conjunctivitis due to broad-spectrum activity against common ocular pathogens.

The single supporting publication examined bacteriology and antibiotic susceptibility patterns in childhood acute bacterial conjunctivitis, which provides indirect, pathogen-level plausibility for a sulfonamide's relevance to this indication, but does not directly test Sulfamethoxazole efficacy in conjunctivitis. Given that the drug's original indication and MOA are both unconfirmed in this evidence pack, the mechanistic rationale here should be treated as preliminary and class-based rather than drug-specific.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31788487](https://pubmed.ncbi.nlm.nih.gov/31788487/) | 2019 | Retrospective observational study | Medical Hypothesis, Discovery & Innovation Ophthalmology Journal | Retrospective analysis of childhood acute bacterial conjunctivitis in Western Greece, characterizing causative bacteria and antimicrobial susceptibility patterns relevant to empiric topical antibiotic selection |

## Taiwan Market Information

Sulfamethoxazole currently has no registered licenses in Taiwan (total_licenses = 0; market status: Not Marketed). No product-level dosage form or approved indication data is available.

## Safety Considerations

- **Drug Interactions**: DDI query completed with **151 total documented interactions**. Notable interactions include:
  - **Moderate**: Sulfonylurea antidiabetics (Chlorpropamide, Glimepiride, Acetohexamide, Glipizide, Glyburide) and multiple insulin formulations (human, aspart, degludec, detemir, glargine, glulisine) — potential increased hypoglycemic effect
  - **Moderate**: Balsalazide, Picosulfuric acid
  - **Minor**: Famotidine, Clarithromycin, Cisapride, Dolasetron, Palonosetron, Granisetron

Key warnings and contraindications from the product label are not yet available (data gap DG001) — please refer to the official package insert once obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking-severity data gap (DG001 — missing TFDA label warnings/contraindications) prevents completion of the required S1 safety pre-assessment. Combined with missing MOA data (DG002), an unconfirmed original indication, zero clinical trials, and only a single non-RCT publication (Evidence Level L3), the current evidence base is insufficient to advance this candidate.

**To proceed, the following is needed:**
- Resolve DG001: obtain and parse the TFDA package insert for warnings/contraindications
- Resolve DG002: query DrugBank API for confirmed mechanism of action
- Confirm the drug's original approved indication(s), currently missing from source data
- Additional direct clinical evidence (trials or comparative studies) evaluating Sulfamethoxazole specifically in acute contagious conjunctivitis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

