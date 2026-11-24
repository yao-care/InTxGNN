---
layout: default
title: Pseudoephedrine
parent: Model Prediction Only (L5)
nav_order: 712
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Pseudoephedrine: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis…"
monitor_inn: "Pseudoephedrine"
predicted_indications: ["nasal cavity disease", "allergic urticaria"]
---

# Pseudoephedrine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Pseudoephedrine: From Allergic Rhinitis and Common Cold to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Pseudoephedrine is a decongestant originally used for allergic rhinitis, vasomotor rhinitis, the common cold, pharyngitis and related upper-airway conditions.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are **no registered clinical trials** and only **7 publications** (one review, one clinical pharmacology study and five animal-model studies).
This prediction largely overlaps with the drug's existing uses, so it is better seen as an extension of current use than as true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold and related conditions (the licence records contain no approved indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, pseudoephedrine is an indirect sympathomimetic with alpha-adrenergic agonist activity. It constricts blood vessels in the nasal mucosa, which reduces swelling and congestion.

Nasal cavity disease is a broad category that includes the rhinitis conditions already among pseudoephedrine's original indications. The mechanism (reducing mucosal swelling) therefore applies directly. The high TxGNN score is likely driven by this close similarity to approved rhinitis uses.

Two other predictions were also generated but are not supported. Acute laryngopharyngitis has no trials or literature, and pseudoephedrine has no known effect on laryngeal inflammation or infection. Allergic urticaria has no mechanistic rationale: pseudoephedrine has no antihistamine activity, and all retrieved papers concern antihistamines, not pseudoephedrine.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22794679](https://pubmed.ncbi.nlm.nih.gov/22794679/) | 2012 | Review | Allergy Asthma Proc | Overview of nonallergic rhinitis: inflammatory and noninflammatory causes presenting with congestion, rhinorrhea, sneezing and postnasal discharge |
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Clinical pharmacology study | Am J Rhinol | Compared oral and topical decongestant effects of phenylpropanolamine and d-pseudoephedrine on nasal cavity dimensions using acoustic rhinometry |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | Animal model (cat) | Am J Rhinol Allergy | Loratadine and montelukast combination produced decongestion; d-pseudoephedrine was also studied with and without desloratadine |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Animal model (dog) | Am J Rhinol | Model of allergic nasal congestion in ragweed-sensitized dogs |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Animal model (dog) | J Pharmacol Toxicol Methods | Pharmacological characterization of a chronic dog model of nasal congestion |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Animal model (dog) | Am J Rhinol | Acoustic rhinometry as a large-animal model for nasal congestion studies |
| [24492651](https://pubmed.ncbi.nlm.nih.gov/24492651/) | 2014 | Animal model | J Pharmacol Exp Ther | Selective α2c-adrenergic agonists evaluated in animal models of nasal congestion |

## India Market Information

Twenty licences are valid and none are cancelled. The main ones are listed below; the licence records contain no approved indication text.

<!-- review:begin in-lic-20261124c-pseudoephedrine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Twenty single-ingredient licences are valid and none are cancelled." Removed: it described the products as single-ingredient, which does not match the Indian medicine data (the Indian Medicine Dataset): some of the products held in the data are fixed-dose combinations. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261124c-pseudoephedrine-1 -->

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 1563 | Ambrolite D Syrup | Bottle of 100 ml Syrup | Valid |
| 9632 | Afdicold Drop | Packet of 15 ml Drop | Valid |
| 10517 | Afdicold Tablet | Strip of 10 tablets | Valid |
| 27113 | Broncho D Syrup | Bottle of 100 ml Syrup | Valid |
| 31595 | Brotee-D Syrup | Bottle of 100 ml Syrup | Valid |
| 33395 | Brex Expectorant | Bottle of 450 ml Expectorant | Valid |
| 39068 | Coform Syrup | Bottle of 100 ml Syrup | Valid |
| 43073 | Coldgesic Suspension | Bottle of 60 ml Suspension | Valid |
| 51888 | Cofsyryl Syrup | Bottle of 60 ml Syrup | Valid |
| 61261 | D Cof Syrup | Bottle of 100 ml Syrup | Valid |
| 63352 | Denituss D Syrup | Bottle of 100 ml Syrup | Valid |
| 70055 | Drykof 15 mg/5 mg/2.5 mg Syrup | Bottle of 100 ml Syrup | Valid |
| 80568 | Eltuss 10 mg/2.5 mg/10 mg Syrup | Bottle of 50 ml Syrup | Valid |
| 137963 | Megatuss D Syrup | Bottle of 100 ml Syrup | Valid |
| 140712 | Martus DTP Syrup | Bottle of 100 ml Syrup | Valid |
| 189886 | Ricold Tablet | Strip of 10 tablets | Valid |
| 192026 | Rekof Tablet | Strip of 10 tablets | Valid |
| 193191 | Ratifed 500 mg/2.5 mg Tablet | Strip of 10 tablets | Valid |
| 212405 | Soodohist 30mg/4mg Syrup | Bottle of 60 ml Syrup | Valid |
| 241783 | Wytuss Syrup | Bottle of 100 ml Syrup | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** hypertension and other hypertensive disorders, coronary artery disease, congestive heart failure, stroke and cerebrovascular disorders, diabetes mellitus and diabetic ketoacidosis, hypothyroidism, liver and kidney disease or failure, epilepsy, COPD, peptic ulcer disease, benign prostatic hyperplasia, and others.
- **Drug Interactions:** 150 interactions were identified. Those listed are mostly Moderate-level, with antidiabetic agents prominent: acarbose, glimepiride, glipizide, glyburide, chlorpropamide, canagliflozin, dapagliflozin, empagliflozin, exenatide, dulaglutide and several insulins. Diethylpropion is also listed as Moderate, and ascorbic acid as Minor.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Nasal cavity disease overlaps substantially with pseudoephedrine's existing rhinitis and nasal congestion uses, and the drug is widely marketed in India, so the prediction is plausible. However, there are no registered trials and the supporting literature is mostly animal-model or non-pseudoephedrine work, so this is an extension of current use rather than a newly validated indication. The other two predictions (acute laryngopharyngitis, allergic urticaria) should stay on Hold.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India Pharma sources (this is a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- A clearer definition of which nasal cavity conditions are targeted beyond current labeled rhinitis uses
- Clinical studies in the specific conditions of interest
- A cardiovascular, metabolic and interaction risk-management plan, given the many knowledge-graph contraindications

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: the single-ingredient claim | Corrected | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

