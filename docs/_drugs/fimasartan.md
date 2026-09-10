---
layout: default
title: Fimasartan
parent: 僅模型預測 (L5)
nav_order: 350
evidence_level: L5
indication_count: 4
---

# Fimasartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Fimasartan: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Fimasartan is an angiotensin II receptor blocker (ARB), a drug class whose established indication is essential/systemic hypertension. The TxGNN model predicts it may be effective for **Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia (WHO Group 3 PH)**, but this prediction is currently supported by **0 clinical trials** and **20 literature hits that, on review, do not actually discuss Fimasartan or this indication** — the evidence base is essentially a model score with no direct corroboration.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (inferred from ARB drug class; formal indication/MOA record is a data gap) |
| Predicted New Indication | Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia (WHO Group 3) |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Fimasartan is not available in this evidence pack (marked as a data gap). Based on known information, Fimasartan belongs to the **angiotensin II receptor blocker (ARB) class**, and its efficacy in systemic/essential hypertension is well established for this drug class; the repurposing rationale text confirms Fimasartan blocks the renin-angiotensin-aldosterone system (RAAS).

However, the predicted new indication — Group 3 pulmonary hypertension (due to lung disease and/or hypoxia) — is pathophysiologically driven by **hypoxic pulmonary vasoconstriction and pulmonary parenchymal remodeling**, a mechanism distinct from systemic RAAS-driven hypertension. There is currently no established mechanistic rationale for ARB efficacy in this specific PH subtype.

Critically, the 20 literature references retrieved for this pair are general hypoxia-biology papers (cancer metabolism, brain aging, multiple sclerosis, tissue repair, etc.) — none mention Fimasartan, the ARB class, or pulmonary hypertension treatment. This indicates the literature co-occurrence is keyword noise ("hypoxia") rather than direct supporting evidence, and the mechanistic link for this prediction should be considered unproven.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | General review on hypoxia's role in brain aging/neurodegeneration; no mention of Fimasartan or PH |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | Review of hypoxia-induced cognitive impairment mechanisms; unrelated to ARBs or PH |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | Journal of Cellular Biochemistry | General review of hypoxia-mediated cell biology and disease associations |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Review | Trends in Cancer | Review of deubiquitinases and hypoxia signaling in cancer, unrelated to PH |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | Review of tumor hypoxia and radiotherapy/therapeutic resistance |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biology | Review of hypoxia's role in multiple sclerosis pathology |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review | Rev Med Inst Mex Seguro Soc | Review of hypobaric (altitude) hypoxia physiology |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Basic Research | Advanced Science | Mechanistic study of glycolysis/HIF-1α in gastric cancer under hypoxia |
| [33278780](https://pubmed.ncbi.nlm.nih.gov/33278780/) | 2021 | Basic Research | Redox Biology | Study of glucose metabolism in keloid fibroblasts under hypoxia |
| [27423661](https://pubmed.ncbi.nlm.nih.gov/27423661/) | 2016 | Basic Research | Cell and Tissue Research | Review of hypoxia/HIF-1 signaling in tissue repair and fibrosis |

**Note:** None of the above publications specifically evaluate Fimasartan or pharmacologic treatment of pulmonary hypertension. They were retrieved on the shared keyword "hypoxia" and should not be treated as direct supporting evidence for this repurposing candidate.

## India Market Information

Fimasartan currently has no registered product licenses (0 total registrations); the drug is not marketed in this market, so no authorization table is available.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Evidence level is L5 (model prediction only) — there are no clinical trials, no relevant literature, and the retrieved publications do not substantiate a mechanistic or clinical link between Fimasartan and Group 3 pulmonary hypertension. The mechanistic basis (RAAS blockade) does not clearly map onto the hypoxia/lung-disease-driven pathophysiology of the target indication.
- Three additional predicted indications in this evidence pack (unclear multifactorial PH, malignant hypertensive renal disease, malignant renovascular hypertension) carry the same "Hold" recommendation, similarly unsupported by trials or literature — two of them have somewhat stronger class-level mechanistic plausibility (ARB effect on RAAS-driven hypertensive nephropathy) but still lack any empirical evidence.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (currently a Blocking data gap — required before any S1 safety screening)
- Confirmed mechanism of action data from DrugBank (High-severity data gap)
- Disease-specific (non-keyword-matched) literature or preclinical studies directly evaluating ARBs in Group 3 pulmonary hypertension
- If pursuing the renal-hypertension-related candidates instead, dedicated evidence search for ARB use in malignant/renovascular hypertension, including renal artery stenosis safety considerations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

