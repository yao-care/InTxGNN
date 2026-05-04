---
layout: default
title: Nitroprusside
parent: 僅模型預測 (L5)
nav_order: 401
evidence_level: L5
indication_count: 10
---

# Nitroprusside
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

# Nitroprusside: From Hypertensive Emergency to Pulmonary Hypertension

## One-Sentence Summary

Nitroprusside (sodium nitroprusside) is a potent intravenous nitric oxide (NO)-releasing vasodilator, established globally for hypertensive emergencies and acute cardiac decompensation, but currently not registered in India.
While TxGNN ranks migraine disorder as the #1 predicted indication, mechanistic analysis reveals nitroprusside as an NO donor is a well-documented migraine **trigger** rather than a treatment — the most clinically actionable prediction is **Pulmonary Hypertension** (TxGNN rank 8, score 99.98%).
This indication is supported by **12 clinical trials** and **20 publications**, with nitroprusside already serving as a reference vasodilator challenge agent in standard pulmonary hypertension workup.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertensive emergency / acute vasodilation (not registered in India) |
| Predicted New Indication | Pulmonary Hypertension (rank 8; highest actionable evidence level) |
| TxGNN Prediction Score | 99.98% (overall model rank 767) |
| Evidence Level | L3 (systematic review + clinical comparative studies + observational studies) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails (pulmonary hypertension) / Hold (migraine and others) |

---

## Why is This Prediction Reasonable?

**Mechanism of Action**

Formal mechanism of action data is not available in this evidence pack. Based on established pharmacology, nitroprusside spontaneously releases nitric oxide (NO) upon entering the bloodstream. NO activates soluble guanylate cyclase (sGC), elevating intracellular cyclic GMP (cGMP), which triggers vascular smooth muscle relaxation and vasodilation — affecting both systemic and pulmonary vasculature.

**Relevance to Pulmonary Hypertension**

Pulmonary hypertension (PH) is characterized by elevated pulmonary vascular resistance (PVR) and right ventricular pressure overload. The NO → sGC → cGMP pathway underlying nitroprusside's action is the same molecular target as approved PH therapies: PDE5 inhibitors (sildenafil, tadalafil) prevent cGMP degradation; sGC stimulators (riociguat) directly amplify the same cascade. Nitroprusside provides exogenous NO to the pulmonary vasculature, producing rapid, titratable PVR reduction.

In clinical practice, nitroprusside already fills two validated roles in PH: (1) **vasoreactivity challenge agent** during right heart catheterization — a mandatory assessment to distinguish reversible from fixed pulmonary hypertension, directly informing treatment selection and cardiac transplant candidacy; (2) **perioperative acute PH management** following cardiac surgery (valve replacement, cardiopulmonary bypass). Its extremely short half-life (minutes) and continuous IV titrability make it uniquely suited for these acute, intensively monitored settings — despite being unsuitable for chronic PAH management due to cyanide toxicity risk with prolonged infusion.

**⚠️ Critical Note: Migraine Predictions Are Mechanistically Paradoxical**

TxGNN ranks migraine disorder (#1), migraine with brainstem aura (#2), and migraine susceptibility (#7) among the top predictions. However, the 20 publications retrieved for migraine consistently show that nitroprusside and other NO donors are established **migraine triggers** used to reliably provoke migraine-like attacks in research models — the standard "nitric oxide migraine model." This literature does not represent therapeutic evidence; it uses nitroprusside as a provocative agent to study migraine pathophysiology. These predictions most likely reflect NO's well-known mechanistic role in migraine sensitization and represent false positives from the TxGNN model. Recommendation for all migraine-related predictions: **Hold (mechanistic contraindication)**.

---

## Clinical Trial Evidence

*(Pulmonary Hypertension — 12 trials identified; ordered by clinical relevance)*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01121458](https://clinicaltrials.gov/study/NCT01121458) | Phase 4 | Completed | 12 | CARVE study: Nitroprusside used as standard vasodilator comparator in pulmonary arterial bed vasoreactivity evaluation (clevidipine vs. SNP); directly validates SNP role in PAH hemodynamic assessment |
| [NCT00595049](https://clinicaltrials.gov/study/NCT00595049) | Phase 4 | Completed | 11 | Bosentan effect on pulmonary artery remodeling in idiopathic PAH and PAH-SSc; nitroprusside included as reference vasodilator in hemodynamic protocol |
| [NCT01597427](https://clinicaltrials.gov/study/NCT01597427) | Phase 2 | Completed | 29 | IV clonidine for mean pulmonary artery pressure reduction in patients undergoing cardiac surgery; nitroprusside used as active comparator for PH control |
| [NCT01120964](https://clinicaltrials.gov/study/NCT01120964) | Phase 1/2 | Completed | 22 | IV L-Citrulline (endogenous NO precursor) pharmacokinetics and safety in children on cardiopulmonary bypass; supports NO-mediated pulmonary pressure management approach |
| [NCT00072826](https://clinicaltrials.gov/study/NCT00072826) | Phase 1 | Completed | 44 | Atorvastatin in sickle cell disease with pulmonary hypertension; SNP used to assess endothelium-independent NO-mediated vasodilation in this PH population |
| [NCT00327080](https://clinicaltrials.gov/study/NCT00327080) | Phase 1 | Terminated | 20 | Sildenafil for HIV-associated PAH; SNP used as endothelium-independent vasodilator control in hemodynamic and endothelial function evaluation |
| [NCT03446612](https://clinicaltrials.gov/study/NCT03446612) | Phase 2 | Terminated | 6 | Daprodustat vs. darbepoetin alfa on forearm blood flow in CKD anemia; terminated early due to insufficient enrollment, results inconclusive |
| [NCT00004575](https://clinicaltrials.gov/study/NCT00004575) | Phase 1 | Completed | 15 | Miconazole as EDHF inhibitor; SNP used as endothelium-independent NO donor control in healthy volunteers |
| [NCT02767024](https://clinicaltrials.gov/study/NCT02767024) | Phase 4 | Withdrawn | 0 | IV vasodilator vs. inotrope in acute decompensated HF with low cardiac output; withdrawn before enrollment, no data generated |
| [NCT03014791](https://clinicaltrials.gov/study/NCT03014791) | N/A | Unknown | 500 | Observational study on blood pressure variation by age, weight, and ethnicity; limited direct relevance to PH treatment |

---

## Literature Evidence

*(Pulmonary Hypertension — 20 publications retrieved; top 10 listed by evidence tier)*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32176355](https://pubmed.ncbi.nlm.nih.gov/32176355/) | 2020 | Systematic Review | Journal of Cardiac Surgery | SNP vs. nicardipine for post-cardiac-surgery hypertension; meta-analysis demonstrates comparable hemodynamic efficacy and cardiac performance effects |
| [26547011](https://pubmed.ncbi.nlm.nih.gov/26547011/) | 2016 | Prospective Clinical Study | Journal of Cardiac Failure | SNP acute hemodynamic response in mixed PH + left heart disease; diastolic pressure gradient ≥7 mmHg identified as key predictor of prognosis and treatment response |
| [15725144](https://pubmed.ncbi.nlm.nih.gov/15725144/) | 2005 | Clinical Comparative Study | Journal of Cardiac Surgery | Direct comparison of inhaled prostacyclin, inhaled NO, and IV nitroprusside in PH after mitral valve replacement; provides head-to-head hemodynamic data |
| [38667742](https://pubmed.ncbi.nlm.nih.gov/38667742/) | 2024 | Clinical Study | Journal of Cardiovascular Development and Disease | Nitroprusside combined with passive leg raise during right heart catheterization to discriminate precapillary from combined PH; novel diagnostic protocol with direct SNP application |
| [35524735](https://pubmed.ncbi.nlm.nih.gov/35524735/) | 2022 | Clinical Study | European Heart Journal Acute Cardiovascular Care | SNP vasodilator challenge in functional mitral regurgitation + PH; PAWP normalization with SNP predicts favorable hemodynamic response to MitraClip |
| [22898992](https://pubmed.ncbi.nlm.nih.gov/22898992/) | 2012 | Clinical Study | Arquivos Brasileiros de Cardiologia | SNP vs. sildenafil for PH reversibility testing before cardiac transplantation; SNP associated with higher rate of systemic arterial hypotension, informing safety protocol design |
| [37980253](https://pubmed.ncbi.nlm.nih.gov/37980253/) | 2023 | Review | Transplantation Proceedings | PH in the temporary mechanical circulatory support era; nitroprusside reviewed among key acute IV vasodilator strategies for right ventricular failure management |
| [32558420](https://pubmed.ncbi.nlm.nih.gov/32558420/) | 2020 | Retrospective Study | Turkish Journal of Pediatrics | Pediatric cardiac transplantation candidates with elevated PVR; vasodilator management protocol including nitroprusside assessed for outcomes |
| [16429888](https://pubmed.ncbi.nlm.nih.gov/16429888/) | 2005 | Review | Texas Heart Institute Journal | Management of systemic and pulmonary hypertension in cardiac surgery; nitroprusside identified as primary parenteral vasodilator among NO/cGMP-pathway agents |
| [7044681](https://pubmed.ncbi.nlm.nih.gov/7044681/) | 1982 | Preclinical Study | Critical Care Medicine | Direct study of nitroprusside in pulmonary hypertension and lung fluid balance following E. coli endotoxin; earliest direct evidence of SNP effect in pulmonary vascular bed |

---

## India Market Information

Nitroprusside is currently **not registered** in India. No drug authorization records are available in the CDSCO database. Any clinical use or repurposing program would require a new product registration or import license.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** All key warnings and contraindication fields in this evidence pack returned Data Gap (TFDA package insert not yet retrieved — see remediation step DG001). Drug-drug interaction data was also unavailable. The following are critical safety signals known from global pharmacology that must be verified against the formal package insert before any clinical use:
>
> - **Cyanide toxicity**: Thiocyanate/cyanide accumulation risk with infusion rates >2 µg/kg/min or duration >48–72 hours; requires thiocyanate serum monitoring
> - **Severe systemic hypotension**: Major dose-limiting adverse effect; continuous intra-arterial blood pressure monitoring mandatory
> - **Light sensitivity**: Infusion solution degrades rapidly under light exposure; must be protected with opaque wrapping during administration
> - **Renal/hepatic impairment**: Thiocyanate clearance is reduced; dose adjustment required

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (Pulmonary Hypertension) / Hold (All Other Predicted Indications)**

**Rationale:**
The mechanistic basis (NO → sGC → cGMP → pulmonary vasodilation) is sound and already clinically validated; multiple completed studies confirm nitroprusside's established role as a vasoreactivity challenge agent and perioperative acute PH management tool, placing this indication at L3 evidence with a direct pathway to formalization. Migraine predictions (ranks 1, 2, 7) represent mechanistic false positives — nitroprusside triggers, not treats, migraine — and should not be pursued. Hair loss conditions (ranks 3–6) and kyphoscoliotic heart disease (rank 10) are L5 with no clinical evidence and no viable delivery route; recommend Hold. Benign prostatic hyperplasia (rank 9) has biological plausibility via NO/cGMP smooth muscle relaxation (analogous to PDE5 inhibitor mechanism) but no clinical evidence and systemic delivery limitations; classify as Research Question for basic science exploration only.

**To proceed with pulmonary hypertension evaluation, the following is needed:**

- **Remediate DG001**: Download TFDA/FDA package insert PDF and extract formal warnings, contraindications, and special population restrictions to enable S1 safety evaluation
- **Remediate DG002**: Query DrugBank API to obtain formal MOA documentation and complete mechanistic profile
- **India regulatory pathway**: Initiate CDSCO new product registration or import license process (drug currently not marketed in India)
- **Define indication scope**: Specify the target PH clinical context — acute vasoreactivity testing protocol, perioperative PH management post-cardiac surgery, or mixed PH hemodynamic stabilization — as each has different dosing, duration, and monitoring requirements
- **Cyanide monitoring protocol**: Establish thiocyanate serum monitoring thresholds and maximum infusion duration limits for the intended indication before any clinical protocol submission
- **Comparator analysis**: Conduct comparative safety and efficacy review against inhaled NO, IV prostacyclin, and oral sildenafil in the target PH subtype to position nitroprusside's clinical niche
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

