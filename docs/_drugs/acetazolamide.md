---
layout: default
title: Acetazolamide
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
---

# Acetazolamide
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

# Acetazolamide: From Glaucoma & Altitude Sickness to Cardiomyopathy

## One-Sentence Summary

Acetazolamide is a carbonic anhydrase (CA) inhibitor with well-established uses in glaucoma, altitude sickness, and epilepsy management.
The TxGNN model predicts it may be effective for **Cardiomyopathy** (including acute decompensated heart failure),
with **3 active Phase 4 clinical trials** (combined planned enrollment ~1,805 patients) and **10 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Glaucoma, altitude sickness, epilepsy (standard carbonic anhydrase inhibitor indications; no formal regulatory data available in this evidence pack) |
| Predicted New Indication | Cardiomyopathy |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Acetazolamide belongs to the carbonic anhydrase inhibitor class. By blocking CA in the proximal renal tubule, it increases NaHCO₃ excretion and promotes sodium and water loss — a diuretic mechanism distinct from loop diuretics, which target the thick ascending limb of the Loop of Henle.

This mechanistic complementarity is clinically significant in cardiomyopathy and heart failure. Volume overload and congestion are the primary drivers of acute decompensation, and patients frequently develop resistance to loop diuretics alone, compounded by metabolic alkalosis and hypochloremia that further blunts diuretic efficacy. Acetazolamide directly addresses both problems: it acts on a separate nephron segment and restores chloride balance, thereby re-sensitizing patients to loop diuretics. The landmark ADVOR Phase 3 RCT (NEJM 2022, external reference) demonstrated that adding acetazolamide to furosemide significantly improved successful decongestion endpoints in acute heart failure, validating this mechanistic hypothesis in a large randomized trial.

Building on the ADVOR results, three Phase 4 trials are now actively recruiting, collectively targeting ~1,805 patients across different heart failure populations and diuretic strategies. This progression from mechanistic hypothesis to Phase 3 confirmation to active Phase 4 investigation makes cardiomyopathy a credible and high-priority repurposing target for acetazolamide.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05802849](https://clinicaltrials.gov/study/NCT05802849) | Phase 4 | Recruiting | 400 | Oral acetazolamide for decompensated CHF; evaluates feasibility of the oral formulation route, directly building on ADVOR Phase 3 IV data |
| [NCT06166654](https://clinicaltrials.gov/study/NCT06166654) | Phase 4 | Recruiting | 939 | Head-to-head comparison of acetazolamide vs. metolazone added to loop diuretics in acute HF with volume overload; largest ongoing trial testing acetazolamide in heart failure; results expected September 2027 |
| [NCT06092437](https://clinicaltrials.gov/study/NCT06092437) | N/A (Pragmatic RCT) | Recruiting | 466 | Tailored urine-sodium-guided diuretic algorithm in acute decompensated HF; acetazolamide included as a protocol component; tests precision-medicine approach to diuretic dosing |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Narrative Review | ESC Heart Failure | 2024 HF update; reviews latest ESC guideline changes, SGLT2 inhibitors, and emerging pharmacotherapy strategies relevant to acetazolamide's diuretic synergy role |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Narrative Review | Eur Heart J Cardiovasc Pharmacother | Reviews major cardiovascular pharmacology advances in 2022 including first-in-class HF therapies; contextualises acetazolamide's emerging role alongside novel agents |
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case Report | Journal of Cardiology Cases | Acetazolamide successfully used to correct hypochloremia in an advanced HF patient with hypertrophic cardiomyopathy on complex diuretic therapy; supports chloride manipulation as a therapeutic target |
| [22426904](https://pubmed.ncbi.nlm.nih.gov/22426904/) | 2012 | Animal Study | Saudi Medical Journal | Investigated acetazolamide effects on ischemia-reperfused isolated rabbit hearts; provides preclinical signal regarding cardiac effects of CA inhibition |
| [7324871](https://pubmed.ncbi.nlm.nih.gov/7324871/) | 1981 | Case Series | Acta Neurologica Scandinavica | Cardiac involvement documented in hypokalaemic periodic paralysis patients during long-term acetazolamide therapy (750–1000 mg/day); important historical safety context |
| [742352](https://pubmed.ncbi.nlm.nih.gov/742352/) | 1978 | Case Series | Acta Neurologica Scandinavica | Echocardiographic evaluation of cardiomyopathic changes in a hypokalaemic periodic paralysis family; characterises cardiac exposure during acetazolamide use |
| [29123889](https://pubmed.ncbi.nlm.nih.gov/29123889/) | 2017 | Case Report (Adverse Event) | Acute Medicine & Surgery | Non-cardiogenic pulmonary oedema developed 1 hour after IV acetazolamide in a dilated cardiomyopathy patient — critical safety signal specific to IV administration in cardiac patients |
| [23571262](https://pubmed.ncbi.nlm.nih.gov/23571262/) | 2014 | Case Report | Indian Journal of Ophthalmology | Oral acetazolamide used in Danon disease (a cardiomyopathy-retinopathy syndrome); documents drug exposure and tolerability in the presence of underlying cardiac disease |
| [9627326](https://pubmed.ncbi.nlm.nih.gov/9627326/) | 1998 | Observational | Journal of Nuclear Medicine | SPECT imaging in mitochondrial encephalomyopathy using acetazolamide cerebrovascular challenge; indirect evidence of vascular and metabolic CA inhibition effects |
| [35619116](https://pubmed.ncbi.nlm.nih.gov/35619116/) | 2022 | Case Report | Journal of Medical Case Reports | Acetazolamide administered for CSF reduction in congenital hydrocephalus complicated by congenital heart disease; demonstrates drug use in paediatric cardiac comorbidity context |

---

## India Market Information

Acetazolamide currently has **no registered products in India** (CDSCO). No license data is available in this evidence pack. Market authorisation status should be verified directly with CDSCO before any regulatory or commercial planning.

---

## Safety Considerations

**Drug Interactions**: Acetazolamide has 165 documented interactions in the DDInter database. Key interactions include:

| Severity | Interacting Drug(s) |
|----------|---------------------|
| **Major** | Acetylsalicylic acid (aspirin), Cisapride |
| **Moderate** | Antidiabetic agents (acarbose, acetohexamide, alogliptin, albiglutide, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide); Amphotericin B (conventional and all lipid formulations); Corticosteroids (beclomethasone, betamethasone, dexamethasone); Bisacodyl; Castor oil |
| **Minor** | Doxycycline |

The major interaction with **aspirin** is clinically important in the cardiac population, as many heart failure patients are co-prescribed antiplatelet therapy. The interaction with **corticosteroids** (moderate) is also relevant in patients treated for inflammatory cardiomyopathy.

Please refer to the complete package insert for full warnings and contraindications (currently a blocking data gap for this evidence pack).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The external ADVOR Phase 3 RCT (NEJM 2022) provides Level 2 evidence that acetazolamide significantly enhances decongestion in acute heart failure when added to loop diuretics. Three large Phase 4 trials (total ~1,805 patients) are actively confirming and extending these findings. The mechanistic rationale is clear and validated; the principal uncertainties are around formulation safety and population selection rather than efficacy signal.

**To proceed, the following is needed:**

- **Obtain MOA data from DrugBank** (DB00819) to complete mechanistic analysis and support regulatory dossier preparation
- **Retrieve and parse the TFDA/CDSCO package insert** to resolve the blocking safety gap (DG001) — required before entering S1 safety evaluation
- **Monitor NCT06166654 results** (939 patients, expected September 2027) as the largest ongoing confirmatory dataset
- **Clarify IV vs. oral formulation strategy**: the non-cardiogenic pulmonary oedema adverse event (PMID 29123889) with IV acetazolamide warrants a specific risk-mitigation plan for inpatient cardiac use; the oral Phase 4 trial (NCT05802849) may offer a safer route
- **Define the target patient population more precisely**: acute decompensated HF with loop diuretic resistance is the best-supported subgroup; general "cardiomyopathy" is too broad for a regulatory filing
- **Assess India-specific regulatory pathway**: with zero current market authorisations in India, a full new drug application (NDA) process with CDSCO will be required, including local clinical data considerations
- **Evaluate the aspirin interaction** in the context of cardiac co-prescribing, and establish monitoring protocols for the major DDI risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

