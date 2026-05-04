---
layout: default
title: Chlorthalidone
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 10
---

# Chlorthalidone
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

# Chlorthalidone: From Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Chlorthalidone is a thiazide-like diuretic with a long-established track record in managing hypertension and volume-overload states. The TxGNN model predicts it may be effective for **Primary Hereditary Glaucoma**, yet **no clinical trials** and **no publications** directly support this direction — the current evidence rests entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / edema (based on established drug class; formal India regulatory data unavailable) |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this evidence pack. Based on well-established pharmacological knowledge, Chlorthalidone is a thiazide-like sulfonamide diuretic that inhibits sodium–chloride cotransporters (NCC) in the distal convoluted tubule, promoting natriuresis, reducing plasma volume, and ultimately lowering systemic blood pressure.

The proposed link to primary hereditary glaucoma is indirect and speculative. Diuretics can theoretically reduce intraocular pressure (IOP) by decreasing systemic fluid volume and, to a minor extent, aqueous humor production. However, pharmacological IOP reduction depends primarily on carbonic anhydrase inhibitors (e.g., acetazolamide, dorzolamide), beta-blockers, or prostaglandin analogues — not thiazide-class diuretics, which have no established direct ocular mechanism. Primary hereditary glaucoma is driven by specific genetic defects (most commonly mutations in *MYOC*, *OPTN*, and *TBK1*), for which chlorthalidone has no known direct pharmacological target.

The high TxGNN score most likely reflects the well-documented epidemiological comorbidity between systemic hypertension and glaucoma that is encoded in the knowledge graph, rather than a true drug–disease therapeutic relationship. In the absence of any supporting clinical trial, observational, or laboratory evidence, this prediction should be treated as a hypothesis-generating signal only, not an actionable repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Chlorthalidone has no registered products in India as of the data cutoff date (April 5, 2026). No authorization numbers, brand names, or approved indications are on file.

---

## Safety Considerations

**Drug Interactions**: A total of **210 drug interactions** have been identified. The 20 interactions listed below represent a cross-section by severity level (source: DDInter):

| Severity | Interacting Drug | Clinical Note |
|----------|-----------------|---------------|
| **Major** | Cisapride | Risk of serious cardiac arrhythmia (QT prolongation); combination should be avoided |
| **Major** | Dolasetron | QT prolongation risk; avoid concurrent use |
| Moderate | Acarbose | Chlorthalidone may antagonise hypoglycaemic effect |
| Moderate | Albiglutide | Thiazide diuretics can impair glucose tolerance, reducing GLP-1 agonist efficacy |
| Moderate | Alogliptin | Similar glucose-tolerance antagonism as above |
| Moderate | Metformin | Thiazide-induced hyperglycaemia may reduce metformin effectiveness |
| Moderate | Amphotericin B | Additive hypokalaemia risk |
| Moderate | Amphotericin B (lipid complex) | Same as above |
| Moderate | Hydrocortisone | Additive electrolyte depletion (especially potassium) |
| Moderate | Dexamethasone | Additive hypokalaemia; monitor electrolytes |
| Moderate | Triamcinolone | Additive electrolyte depletion |
| Moderate | Beclomethasone dipropionate | Additive hypokalaemia risk |
| Moderate | Bupropion | Possible increased seizure risk with electrolyte imbalance |
| Moderate | Morphine | Hypotensive effects may be potentiated |
| Moderate | Omeprazole | Interaction of undetermined mechanism; monitor |
| Moderate | Rabeprazole | Same as above |
| Moderate | Cholecalciferol | Thiazides reduce urinary calcium excretion; vitamin D may exacerbate hypercalcaemia |
| Minor | Atropine | Reduced GI motility may affect absorption |
| Minor | Hyoscyamine | Same mechanism as atropine |
| Minor | Doxycycline | Minor pharmacokinetic interaction; clinical significance low |

Please refer to the package insert for complete warnings and contraindications, as key warning and contraindication data were not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.92%), there is zero direct clinical trial or literature evidence linking chlorthalidone to primary hereditary glaucoma, and the mechanistic connection is indirect at best — the genetic aetiology of this condition does not align with chlorthalidone's known pharmacology. The signal most likely arises from knowledge-graph confounding via the hypertension–glaucoma comorbidity association.

**To proceed, the following is needed:**
- Confirmed mechanism of action data (MOA) from DrugBank or primary literature, specifically examining any direct effects on intraocular pressure or aqueous humor dynamics
- Preclinical (in vitro / animal model) studies evaluating chlorthalidone in hereditary glaucoma models carrying *MYOC* or *OPTN* mutations
- Pharmacoepidemiology analysis comparing glaucoma incidence in hypertensive patients treated with chlorthalidone versus other antihypertensive classes (e.g., propensity-matched real-world data)
- Knowledge graph audit to confirm whether the TxGNN high score reflects a true drug–disease signal or a spurious comorbidity-driven confound
- India regulatory pathway assessment, given the drug is currently not marketed in India — any development would require de novo registration

> **Note:** Of the 10 predicted indications evaluated in this evidence pack, **Chronic Pulmonary Heart Disease (Rank 8)** carries the strongest supporting evidence (L3), including a 1967 Italian clinical series directly reporting chlorthalidone use in cor pulmonale (PMID [5597001](https://pubmed.ncbi.nlm.nih.gov/5597001/)). That indication may warrant a separate, dedicated research question evaluation if the development team wishes to pursue a cardiovascular angle.

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

