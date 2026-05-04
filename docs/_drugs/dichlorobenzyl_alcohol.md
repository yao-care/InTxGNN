---
layout: default
title: Dichlorobenzyl Alcohol
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 2
---

# Dichlorobenzyl Alcohol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Dichlorobenzyl Alcohol: From Antiseptic/Oral Care to Bronchitis

## One-Sentence Summary

Dichlorobenzyl alcohol (DCBA) is a halogenated benzyl alcohol compound traditionally used as a topical antiseptic, most commonly found in over-the-counter throat lozenge products for its antimicrobial properties.
The TxGNN model predicts it may have potential utility for **Bronchitis**, however with **0 clinical trials** and **1 marginally relevant publication** (concerning a structurally distinct compound), the evidence base is extremely thin.
At this stage, the prediction cannot be meaningfully substantiated and requires significant foundational research before any repurposing pathway can be considered.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication available (traditionally used as a topical oral antiseptic in OTC throat lozenges) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.21% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Dichlorobenzyl alcohol is a chlorinated benzyl alcohol that has been used in topical oral antiseptic formulations (e.g., Strepsils lozenges). It is known to exhibit broad-spectrum antimicrobial activity against gram-positive bacteria and has some activity against respiratory viruses, which forms the theoretical bridge to infectious airway conditions.

Acute bronchitis is predominantly caused by viral respiratory pathogens, with a smaller proportion attributable to bacterial infection. The theoretical case for DCBA rests on its surface-level antimicrobial and antiviral properties — if delivered to the airways in an appropriate formulation, it could plausibly reduce pathogen burden. However, DCBA's known use is confined to topical oral mucosa contact, and no data exist on systemic absorption, inhalational delivery, or pulmonary pharmacokinetics.

The TxGNN score of 0.992 reflects knowledge-graph topological proximity between DCBA and bronchitis-associated nodes, not a validated biological mechanism. Without MOA data and with a complete absence of bronchitis-specific studies, this prediction should be treated as a hypothesis-generation signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1036939](https://pubmed.ncbi.nlm.nih.gov/1036939/) | 1976 | Observational report (case series) | Arzneimittel-Forschung | 25 patients with chronic bronchitis treated with clenbuterol (a structurally distinct compound whose IUPAC name contains "dichlorobenzyl alcohol") showed elevated creatine kinase — **not a study of DCBA itself** |

> **Important caveat:** This publication concerns clenbuterol (4-amino-α-[(tert-butylamino)methyl]-3,5-dichlorobenzyl alcohol hydrochloride), a β₂-adrenergic agonist bronchodilator. Although "dichlorobenzyl alcohol" appears in its chemical name, clenbuterol is a pharmacologically distinct compound. This paper does **not** constitute evidence for Dichlorobenzyl alcohol (DB13269) in bronchitis.

---

## India Market Information

Dichlorobenzyl alcohol currently has no registered products in India. There are no authorization records on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests entirely on a TxGNN model score (L5 evidence) with no supporting clinical trials and no directly applicable literature. Critical data gaps — including the complete absence of MOA data, systemic safety profile, and any regulatory registration — make it premature to advance this candidate along any repurposing pathway.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank API or primary pharmacology literature
- Systemic safety and toxicology profile (DCBA is currently known only for topical/mucosal use; systemic or inhalational data are absent)
- Package insert warnings and contraindications (from regulatory source)
- Preclinical in vitro or in vivo studies demonstrating activity against bronchitis-relevant pathogens via a clinically relevant route (inhalational or systemic)
- Pharmacokinetic characterisation: absorption, distribution, lung tissue penetration
- Route-of-administration feasibility assessment before any clinical hypothesis can be formed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

