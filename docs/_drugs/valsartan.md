---
layout: default
title: Valsartan
parent: 僅模型預測 (L5)
nav_order: 517
evidence_level: L5
indication_count: 7
---

# Valsartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Valsartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Valsartan is an angiotensin II type 1 receptor blocker (ARB) with well-established use in hypertension, heart failure, and post-myocardial infarction management.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, with **0 clinical trials** and **1 experimental publication** currently supporting this direction.
Overall evidence is at the preclinical/mechanistic level (L4), and a formal research programme is required before clinical translation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, heart failure, post-myocardial infarction (ARB class) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## All Predicted Indications at a Glance

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation |
|------|-----------|------------|---------------|---------------|
| 1 | Malignant hypertensive renal disease | 99.97% | L4 | Research Question |
| 2 | Malignant renovascular hypertension | 99.97% | L4 | Research Question |
| 3 | Pulmonary hypertension owing to lung disease / hypoxia | 99.97% | L5 | Hold |
| 4 | Pulmonary hypertension with unclear multifactorial mechanism | 99.97% | L5 | Hold |
| 5 | Braddock syndrome | 99.96% | L5 | Hold |
| 6 | Chronic pulmonary heart disease | 99.58% | L3 | Research Question |
| 7 | Prinzmetal angina | 99.45% | L5 | Hold |

The remainder of this report provides detailed evidence for **Indication #1 (Malignant Hypertensive Renal Disease)**, the top-ranked prediction.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data could not be retrieved in this query cycle (DrugBank data gap). Based on established pharmacology, Valsartan selectively blocks the angiotensin II type 1 (AT1) receptor, preventing angiotensin II from triggering vasoconstriction, aldosterone secretion, and downstream pro-fibrotic and pro-inflammatory cascades. In the kidney, AT1 blockade reduces intraglomerular pressure and suppresses mesangial fibrosis — effects that are central to renoprotective ARB therapy.

Malignant hypertensive renal disease is defined by fulminant RAAS hyperactivation: fibrinoid necrosis of renal arterioles, rapidly progressive renal insufficiency, and microangiopathic haemolysis. This is precisely the disease context where AT1 receptor blockade has the strongest theoretical rationale, as Ang II-mediated constriction of efferent arterioles and direct pro-fibrotic signalling are core pathological drivers. The TxGNN model likely captured the dense co-occurrence of "ARB / Valsartan / malignant hypertension / renal disease" nodes in the knowledge graph, reflecting this mechanistic logic.

The sole supporting publication (PMID 24368192) investigates avosentan — an endothelin receptor antagonist, not Valsartan — in RAAS double-transgenic rats that overexpress both human renin and angiotensinogen. Although the drug class differs, the shared RAAS-overactivation pathology makes this an indirect mechanistic analogue. A complementary study in Indication #2 (PMID 11560862, *Circulation* 2001) directly tests AT1 receptor blockade in lethal malignant hypertension and kidney inflammation in an animal model, providing the closest mechanistic support to Valsartan's specific action — but this evidence remains preclinical, with no subsequent RCT follow-up in over two decades.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Valsartan in malignant hypertensive renal disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Animal / Experimental | Pharmacological Research | Avosentan (endothelin antagonist) protects against hypertensive nephropathy in RAAS double-transgenic rats at sub-fluid-retention doses; provides indirect mechanistic analogy for RAAS-targeted renal protection but does not directly study Valsartan |

---

## India Market Information

Valsartan currently holds **no registered product licences** in India under CDSCO. The drug is not commercially available in the Indian market. Any future repurposing programme targeting India would need to address the full regulatory pathway for market authorisation prior to clinical investigation.

---

## Safety Considerations

**Drug Interactions:** A total of **254 interactions** were identified. Key interactions are listed below.

**Major interactions — require active management:**

| Interacting Drug | Level | Clinical Concern |
|----------------|-------|-----------------|
| Potassium Bicarbonate | Major | Risk of hyperkalaemia; concurrent use should be avoided or require close electrolyte monitoring |
| Potassium Chloride | Major | Risk of hyperkalaemia; serum potassium must be monitored regularly |

**Moderate interactions — representative examples:**

| Interacting Drug / Class | Level | Clinical Concern |
|--------------------------|-------|-----------------|
| Insulin (all formulations: human, aspart, degludec, detemir, glargine, glulisine, lispro, isophane, zinc, inhalation) | Moderate | ARBs may enhance hypoglycaemic effect; blood glucose monitoring recommended |
| Hydrocortisone | Moderate | Corticosteroids can attenuate antihypertensive effect |
| Exenatide | Moderate | Enhanced hypoglycaemic effect possible |
| Eluxadoline | Moderate | Monitor for altered GI or haemodynamic effects |
| Polyethylene Glycol 3350 with electrolytes | Moderate | Electrolyte balance (particularly potassium) requires management |

> Detailed warnings and contraindications could not be retrieved in this query cycle (CDSCO/package insert data gap). Please refer to the approved package insert for full safety information before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although Valsartan's AT1 receptor blockade mechanism is strongly theoretically applicable to malignant hypertensive renal disease — where RAAS hyperactivation is a core driver — the current evidence base consists solely of a single indirect animal study using a different drug. There are no registered clinical trials for this specific indication, and Valsartan is not marketed in India (0 CDSCO authorisations). The evidence is not sufficient to progress beyond a research hypothesis at this time.

**To proceed, the following is needed:**

- **Retrieve CDSCO/package insert safety data** (warnings and contraindications) to complete the S1 safety gate assessment — currently a blocking data gap
- **Obtain DrugBank MOA documentation** for Valsartan to formally confirm and document mechanistic links for the dossier
- **Conduct a targeted literature review** specifically on ARB-class drugs (candesartan, losartan, olmesartan) in malignant hypertension and hypertensive nephropathy to establish class-level evidence
- **Identify if any investigator-initiated trials** exist outside ClinicalTrials.gov (e.g., EU Clinical Trials Register, WHO ICTRP) for ARBs in malignant hypertensive nephropathy
- **Design a pilot clinical study** or seek academic collaboration for a proof-of-concept trial evaluating Valsartan or an ARB comparator in malignant hypertensive renal disease
- **Establish a regulatory strategy for India market entry** before any clinical development programme can be initiated in-country
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

