---
layout: default
title: Eplerenone
parent: Model Prediction Only (L5)
nav_order: 316
evidence_level: L5
indication_count: 4
monitor_inn: "Eplerenone"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome"]
last_modified_at: 2026-10-31
description: "Eplerenone: predicted new indication Pulmonary hypertension owing to lung disease and/or hypoxia (evidence level L5). Approved use: Hypertension"
---

# Eplerenone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Eplerenone: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia
{: .text-alpha }

## One-Sentence Summary

Eplerenone is a selective mineralocorticoid receptor antagonist; hypertension is its original indication.
The TxGNN model predicts it may be useful for **pulmonary hypertension owing to lung disease and/or hypoxia**,
but there are **0 clinical trials** and **13 publications** (mostly preclinical or indirectly related), so this remains a research question.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (relation recorded in the knowledge graph; no approved indication text is available in the local licence records) |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 0.9950 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, eplerenone is a selective mineralocorticoid receptor (MR) antagonist, so it blocks aldosterone-driven signalling, which is mechanistically plausible for the predicted indication.

Preclinical work links hypoxia to MR activation and tissue fibrosis. Chronic intermittent hypoxia drove MR-dependent renal fibrosis in rats (PMID 35346763), and eplerenone improved atrial remodelling in a similar model (PMID 35568141). In pulmonary arterial hypertension (PAH) models, hypoxia raises aldosterone synthesis in pulmonary artery endothelial cells and promotes vascular fibrosis (PMID 25001622). MR antagonists, including eplerenone, reduced pulmonary vascular remodelling in rat models (PMIDs 29499691, 35043674).

These findings give a plausible but indirect link between the original indication (hypertension, which is also an MR-related vascular condition) and hypoxia-related pulmonary vascular disease. However, none of the cited studies measures pulmonary arterial pressure or pulmonary vascular resistance in patients with pulmonary hypertension due to lung disease or hypoxia. The very high TxGNN score is a computational prediction, not clinical evidence. Because the PAH studies address a different disease classification from the predicted one, they do not count as direct evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27230560](https://pubmed.ncbi.nlm.nih.gov/27230560/) | 2016 | Clinical study | Pol Arch Med Wewn | Eplerenone in resistant hypertension with obstructive sleep apnoea; assessed effect on apnoea severity and arterial stiffness (indirect relevance) |
| [41483355](https://pubmed.ncbi.nlm.nih.gov/41483355/) | 2026 | Review | Curr Hypertens Rep | Reviews aldosterone blockade for OSA-related hypertension, blood pressure control and oxygenation |
| [35043674](https://pubmed.ncbi.nlm.nih.gov/35043674/) | 2022 | Preclinical (rat) | Am J Physiol Lung Cell Mol Physiol | Eplerenone and spironolactone in established PAH (SU5416-hypoxia model); improved interventricular dependence |
| [29499691](https://pubmed.ncbi.nlm.nih.gov/29499691/) | 2018 | Preclinical | BMC Pulm Med | Eplerenone attenuated pulmonary vascular remodelling more than right ventricular remodelling in PAH |
| [25001622](https://pubmed.ncbi.nlm.nih.gov/25001622/) | 2014 | Preclinical | Circulation | Hypoxia upregulates StAR and aldosterone synthesis in pulmonary artery endothelial cells, promoting vascular fibrosis |
| [27006450](https://pubmed.ncbi.nlm.nih.gov/27006450/) | 2016 | Preclinical | FASEB J | Aldosterone upregulates Raptor (mTORC1) in pulmonary artery smooth muscle cells, promoting PAH |
| [35568141](https://pubmed.ncbi.nlm.nih.gov/35568141/) | 2022 | Preclinical (rat) | Cardiovasc Pathol | Eplerenone improved atrial remodelling induced by chronic intermittent hypoxia |
| [35346763](https://pubmed.ncbi.nlm.nih.gov/35346763/) | 2022 | Preclinical (rat) | Exp Gerontol | Chronic intermittent hypoxia induced renal fibrosis through MR activation |
| [39707386](https://pubmed.ncbi.nlm.nih.gov/39707386/) | 2024 | Preclinical | Cell Commun Signal | Eplerenone reduced cirrhosis-associated changes in hepatocyte glucose and lipid metabolism, with hypoxia-induced MR activation |
| [29682743](https://pubmed.ncbi.nlm.nih.gov/29682743/) | 2018 | Preclinical (animal) | Br J Pharmacol | Eplerenone prevented liver decompensation in cirrhosis |

## India Market Information

At least 20 licences are recorded, and this list may be partial. All are valid single-ingredient records. No approved indication text is available in the local records, and some product names suggest co-packaged kits, so this table shows only five of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 73151 | Ezuric 25mg Tablet (Alkem Laboratories) | Strip of 10 tablets | Not stated in the records |
| 77511 | Eplomax 25mg Tablet (Shinto Organics) | Strip of 10 tablets | Not stated in the records |
| 174802 | Planep 50 Tablet (Lupin) | Strip of 15 tablets | Not stated in the records |
| 72354 | Eptus 25 Tablet (Glenmark) | Strip of 15 tablets | Not stated in the records |
| 73625 | Eplerite 50 Tablet (Cipla) | Strip of 10 tablets | Not stated in the records |

## Safety Considerations

- **Knowledge-graph contraindication relations** (not label text): liver disease, gallbladder disease, diabetic nephropathy, impaired renal function disease.
- **Drug Interactions**: 108 interactions are recorded. Major-level examples include aprepitant, clarithromycin, clotrimazole, and potassium products (potassium citrate, potassium bicarbonate, potassium chloride). Moderate-level examples include corticosteroids (hydrocortisone, dexamethasone, prednisone), aspirin, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin) and bupropion.

Please refer to the package insert for warnings and contraindications from label text, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication directly studies eplerenone in pulmonary hypertension due to lung disease or hypoxia. The support is a high model score and indirect preclinical or related-condition studies, so the evidence level is L5.

**To proceed, the following is needed:**
- Clinical or well-designed preclinical studies that measure pulmonary arterial pressure and vascular resistance in this specific disease
- Detailed mechanism of action data
- Package insert warnings and contraindications from the Indian labels, including hyperkalaemia and renal-impairment risks
- Approved indication text from the local licence records, to confirm the original use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

