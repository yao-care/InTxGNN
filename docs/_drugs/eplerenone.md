---
layout: default
title: Eplerenone
parent: 僅模型預測 (L5)
nav_order: 278
evidence_level: L5
indication_count: 5
---

# Eplerenone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Eplerenone: From Heart Failure to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Eplerenone is a selective mineralocorticoid receptor (MR) antagonist indicated for heart failure following acute myocardial infarction and for hypertension management.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism** (TxGNN score: 99.50%),
however, **no clinical trials** and **no publications** have been identified to directly support this specific repurposing direction, placing the current evidence at the lowest tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heart failure / Hypertension (India registration data not available) |
| Predicted New Indication | Pulmonary Hypertension with Unclear Multifactorial Mechanism |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Eplerenone is a **selective mineralocorticoid receptor (MR) antagonist** — it competitively blocks aldosterone binding to the MR, thereby reducing aldosterone-driven sodium retention, potassium loss, cardiac and vascular fibrosis, and inflammatory signalling. Its selectivity for the MR (versus androgen and progesterone receptors) distinguishes it from the older non-selective agent spironolactone.

The aldosterone/MR signalling pathway has been mechanistically implicated in pulmonary vascular remodelling, smooth muscle cell proliferation, perivascular fibrosis, and the inflammatory cascades that characterise pulmonary arterial hypertension (PAH). RAAS overactivation — including chronically elevated aldosterone — has been documented in multiple forms of PAH and may amplify right ventricular afterload and structural remodelling. Blocking this pathway with an MR antagonist is therefore a biologically plausible strategy.

Indirect support comes from exploratory clinical research with spironolactone in PAH, suggesting that non-selective MR antagonism may modestly attenuate disease progression markers. However, Eplerenone itself has no direct clinical evidence in pulmonary vascular disease. The mechanistic link is **moderate**: the pathway is relevant, but the leap from systemic cardiovascular indications to pulmonary vascular disease involves tissue-specific pharmacology that has yet to be characterised for Eplerenone specifically.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature directly linking Eplerenone to this indication is available.

> **Note:** A PubMed query for the related indication "pulmonary hypertension owing to lung disease and/or hypoxia" returned 20 publications, but all retrieved articles address general hypoxia biology (HIF-1α signalling, tumour hypoxia, neurological hypoxia) without connection to Eplerenone or mineralocorticoid receptor pharmacology. These are classified as non-relevant background literature and are not listed here.

---

## Safety Considerations

Package insert warnings and contraindications are not available in this evidence pack. Please refer to the approved prescribing information for full safety details.

**Drug Interactions** — 108 interactions identified (DDInter database). Key interactions are summarised below:

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Clarithromycin | **Major** | Strong CYP3A4 inhibitor; may markedly elevate eplerenone plasma levels |
| Clotrimazole | **Major** | CYP3A4 inhibition; increased eplerenone exposure |
| Aprepitant | **Major** | CYP3A4 inhibitor; clinically significant pharmacokinetic interaction |
| Potassium chloride | **Major** | Additive hyperkalaemia risk; monitor serum potassium closely |
| Potassium citrate | **Major** | Additive hyperkalaemia risk |
| Potassium bicarbonate | **Major** | Additive hyperkalaemia risk |
| Hydrocortisone | Moderate | Opposing mineralocorticoid effects; potential pharmacodynamic antagonism |
| Dexamethasone / Betamethasone / Budesonide / Triamcinolone / Prednisone | Moderate | Class effect: corticosteroid-aldosterone pathway interactions |
| Canagliflozin / Dapagliflozin / Empagliflozin | Moderate | Both classes affect renal potassium handling; monitor electrolytes |
| Miconazole | Moderate | CYP3A4 inhibition; monitor for elevated eplerenone levels |
| Acetylsalicylic acid | Moderate | Potential attenuation of antihypertensive/diuretic effect |
| Bupropion | Moderate | Mechanism not fully characterised; use with caution |

> Hyperkalaemia is a class-defining risk for MR antagonists. Concomitant use with potassium supplements, potassium-sparing agents, or strong CYP3A4 inhibitors warrants careful monitoring or avoidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials and no directly relevant publications have been identified for Eplerenone in pulmonary hypertension with unclear multifactorial mechanism. The current evidence classification is L5 (TxGNN model prediction only), which is insufficient to support any clinical or regulatory development decision. Additionally, the drug is not registered in India, and critical safety information (package insert warnings and contraindications) remains unavailable.

**To proceed, the following is needed:**

- **MOA documentation**: Retrieve full mechanism of action data from DrugBank API (DB00700) to formalise the mechanistic justification
- **Safety baseline**: Parse approved prescribing information (CDSCO or international label) to identify key warnings, contraindications, and dose-limiting toxicities
- **Targeted literature search**: Conduct a focused PubMed/EMBASE search using ("eplerenone" AND ("pulmonary hypertension" OR "pulmonary arterial hypertension" OR "right heart" OR "vascular remodeling")) to detect any direct evidence missed by the current query
- **Spironolactone bridge data**: Systematically review spironolactone PAH trial results (as a class-effect proxy) to assess whether the indirect mechanistic rationale is clinically substantiated
- **Hyperkalaemia risk assessment**: Given the Major DDI signals with potassium supplements, evaluate whether PAH patient populations commonly co-administer these agents, which could present a safety concern in a repurposing scenario
- **Preclinical feasibility review**: If the mechanistic and safety review is favourable, consider commissioning a preclinical study in a hypoxia-induced PAH animal model before advancing to any clinical exploration

---

> ⚠️ **Disclaimer**: This report is intended for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. Evidence data cut-off: 2026-04-04.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

