---
layout: default
title: Milrinone
parent: Model Prediction Only (L5)
nav_order: 554
evidence_level: L5
indication_count: 10
---

# Milrinone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Milrinone: From Heart Failure to Alopecia

**Note on indication choice:** The top-ranked TxGNN prediction is alopecia (rank 1), but it has no supporting trials or literature. The data compiled for this report contain much stronger evidence for two lower-ranked predictions (congestive heart failure and acute pulmonary heart disease). Both are discussed in the sections below.

## One-Sentence Summary

Milrinone is a PDE3 inhibitor and inodilator, used in India as an injection for cardiac conditions such as heart failure. The TxGNN model's top prediction is **alopecia**, but it has **0 clinical trials** and **0 publications** behind it, so it is a model prediction only. Of the lower-ranked predictions, **acute pulmonary heart disease** has **1 Phase 4 trial** and **20 publications**, and **headache disorder** has **4 case reports and case series** (all on reversible cerebral vasoconstriction syndrome).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Indian licence records (approved indication text is empty for all 8 licences). The literature and pharmacology data describe use in congestive heart failure. |
| Predicted New Indication | Alopecia (top-ranked) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 for alopecia (model prediction only) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

Other predictions in brief:

| Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|
| Hypotrichosis simplex of the scalp | 99.90% | L5 | Hold |
| Congenital hypotrichosis milia | 99.89% | L5 | Hold |
| Diffuse alopecia areata | 99.88% | L5 | Hold |
| Headache disorder | 99.46% | L4 | Research question |
| Congestive heart failure | 99.45% | L1 | Proceed with Guardrails (established use, not true repurposing) |
| Migraine disorder | 99.45% | L5 | Hold |
| Migraine with brainstem aura | 99.38% | L5 | Hold |
| Trigeminal autonomic cephalalgia | 99.25% | L5 | Hold |
| Acute pulmonary heart disease | 99.19% | L1 | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Milrinone inhibits phosphodiesterase 3 (PDE3). This raises cAMP in cardiac muscle and vascular smooth muscle, giving a positive inotropic effect and vasodilation. Pharmacology records in the compiled data also list activity at PDE2A, PDE3A, PDE3B and PDE5A. Detailed mechanism-of-action data from DrugBank are not available.

For **alopecia** and the other hair disorders, there is no documented mechanistic link. A speculative connection through scalp perfusion or cAMP signalling in the hair follicle exists, but nothing supports it. For diffuse alopecia areata, PDE4 inhibition has some immunomodulatory relevance, but PDE3 inhibition by milrinone has no demonstrated role. The high scores probably reflect network proximity to other hair-related disease nodes, not biology.

The two better-supported directions are more plausible:
- **Acute pulmonary heart disease:** PDE3 inhibition lowers pulmonary vascular resistance and improves right ventricular contractility. Inhaled milrinone gives pulmonary vasodilation with less systemic hypotension. The evidence is partly indirect, because the trial population was heterogeneous.
- **Headache disorder:** The literature concerns reversible cerebral vasoconstriction syndrome (RCVS), where milrinone is given intravenously or intra-arterially to relieve vasoconstriction. This supports RCVS specifically, not headache disorders in general. For migraine and cluster-type headache, vasodilators can trigger attacks, so the direction of effect is uncertain.

## Clinical Trial Evidence

**Alopecia and the other hair disorders, migraine disorders and trigeminal autonomic cephalalgia:** Currently no related clinical trials registered.

**Acute pulmonary heart disease:**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03207165](https://clinicaltrials.gov/study/NCT03207165) | Phase 4 | Completed | 192 | Randomised comparison of milrinone vs dobutamine in critically ill coronary care patients. The population is heterogeneous and not specific to acute pulmonary heart disease. |

**Congestive heart failure (established use, shown for context):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07186062](https://clinicaltrials.gov/study/NCT07186062) | Phase 4 | Completed | 60 | Levosimendan vs dobutamine vs milrinone in acute decompensated heart failure with impaired renal function |
| [NCT01956006](https://clinicaltrials.gov/study/NCT01956006) | Phase 1/2 | Completed | 26 | Pilot of slow-release oral milrinone in advanced heart failure, with haemodynamic and safety data |
| [NCT01849094](https://clinicaltrials.gov/study/NCT01849094) | Phase 1/2 | Completed | 9 | Safety, pharmacokinetics and haemodynamic effect of a slow-release oral milrinone formulation |
| [NCT04718350](https://clinicaltrials.gov/study/NCT04718350) | N/A | Completed | 40 | IV levosimendan vs inhaled milrinone in cardiac surgery patients with pulmonary hypertension |
| [NCT02077010](https://clinicaltrials.gov/study/NCT02077010) | Phase 1 | Completed | 10 | Nebulised inhaled milrinone in hospitalised advanced heart failure |
| [NCT05450328](https://clinicaltrials.gov/study/NCT05450328) | Phase 2 | Recruiting | 141 | Inhaled milrinone and epoprostenol to prevent difficult cardiac bypass separation |
| [NCT00338455](https://clinicaltrials.gov/study/NCT00338455) | Phase 2 | Terminated | 16 | Nesiritide in transplant-eligible heart failure patients on dobutamine or milrinone. Milrinone is only peripheral. |
| [NCT02644057](https://clinicaltrials.gov/study/NCT02644057) | Phase 2 | Withdrawn | 0 | Dobutamine vs milrinone for renal recovery in cardiorenal syndrome. No patients enrolled. |

## Literature Evidence

**Headache disorder (RCVS only):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18647181](https://pubmed.ncbi.nlm.nih.gov/18647181/) | 2009 | Case report | Headache | Intra-arterial milrinone used in a patient with RCVS who deteriorated despite calcium channel blockers |
| [34784343](https://pubmed.ncbi.nlm.nih.gov/34784343/) | 2021 | Case report | Am J Case Rep | RCVS on a background of eclampsia that responded to milrinone infusion |
| [25440342](https://pubmed.ncbi.nlm.nih.gov/25440342/) | 2015 | Case series | J Stroke Cerebrovasc Dis | Diagnostic approach for RCVS |
| [42733499](https://pubmed.ncbi.nlm.nih.gov/42733499/) | 2026 | Case report | AJOG Glob Rep | Peripartum RCVS requiring a multimodal approach |

**Acute pulmonary heart disease (selected):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8903534](https://pubmed.ncbi.nlm.nih.gov/8903534/) | 1996 | Randomised open-label trial | Clin Cardiol | 24-hour milrinone vs dobutamine infusion in 33 patients with heart failure after acute myocardial infarction |
| [2035427](https://pubmed.ncbi.nlm.nih.gov/2035427/) | 1991 | Phase III multicentre study | Am Heart J | Extended IV milrinone in 189 patients with severe chronic heart failure improved haemodynamics |
| [7728786](https://pubmed.ncbi.nlm.nih.gov/7728786/) | 1995 | PK/haemodynamic study | Cardiology | Single oral milrinone doses raised cardiac index and lowered wedge pressure in 31 patients with acute heart failure |
| [20056439](https://pubmed.ncbi.nlm.nih.gov/20056439/) | 2010 | Clinical study | J Cardiothorac Vasc Anesth | Inhaled nitroglycerin vs inhaled milrinone in children with congenital heart disease and pulmonary hypertension |
| [11792300](https://pubmed.ncbi.nlm.nih.gov/11792300/) | 2001 | Clinical study | Rev Esp Anestesiol Reanim | Inhaled prostacyclin with inhaled milrinone for pulmonary hypertension |
| [8659556](https://pubmed.ncbi.nlm.nih.gov/8659556/) | 1996 | Review | Am J Med Sci | Basic and clinical pharmacology of milrinone |

**Congestive heart failure (selected):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25625413](https://pubmed.ncbi.nlm.nih.gov/25625413/) | 2015 | Systematic review / meta-analysis | Basic Clin Pharmacol Toxicol | Safety and efficacy of milrinone in acute heart failure after acute myocardial infarction |
| [3591689](https://pubmed.ncbi.nlm.nih.gov/3591689/) | 1987 | Randomised comparison | Am J Cardiol | IV milrinone vs dobutamine in 79 patients with class III–IV heart failure |
| [4019930](https://pubmed.ncbi.nlm.nih.gov/4019930/) | 1985 | Clinical study | J Am Coll Cardiol | Acute and chronic haemodynamic response to oral milrinone in 37 patients with severe heart failure |
| [31865433](https://pubmed.ncbi.nlm.nih.gov/31865433/) | 2020 | Retrospective comparative study | Heart Vessels | Milrinone vs olprinone in 288 hospitalised heart failure patients |
| [37322827](https://pubmed.ncbi.nlm.nih.gov/37322827/) | 2023 | Cohort | ESC Heart Fail | Milrinone vs dobutamine in cardiogenic shock from acute decompensated heart failure |
| [41296998](https://pubmed.ncbi.nlm.nih.gov/41296998/) | 2025 | Review | Cardiol Rev | Current evidence and future directions for milrinone in advanced heart failure |

**Alopecia and other hair disorders, migraine disorders, trigeminal autonomic cephalalgia:** Currently no related literature available.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 145052 | Milyrataj-IV 1mg Injection | Vial of 10 ml injection | Not stated |
| 140289 | Myolong 10mg Injection | Vial of 10 ml injection | Not stated |
| 193347 | Renota 10mg Injection | Vial of 10 ml injection | Not stated |
| 135241 | Milicor 10mg Injection | Vial of 10 ml injection | Not stated |
| 143098 | Milrilact 10mg Injection | Vial of 10 ml injection | Not stated |

Eight single-ingredient licences are valid in total (the table lists the first five), with no cancelled licences. All are injectable forms, which is relevant to any topical use such as hair disorders, since no topical formulation is available.

## Safety Considerations

- **Contraindications flagged by the knowledge graph** (drug-disease edges, not label text): kidney disease, hypotensive disorder, myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease, hypertrophic cardiomyopathy (including familial), pulmonary valve stenosis, hemoglobinopathy, and pyoureter.
- **Drug interactions (moderate, from DDInter):** amifostine, diatrizoate, anagrelide, ozanimod, procarbazine.
- **Clinical guardrails:** The long-term oral formulation has been associated with increased mortality (PROMISE), so use is limited to short-term IV support or palliative use. Watch for arrhythmia and hypotension, and adjust the dose for renal impairment. For acute pulmonary heart disease, vasopressor support is often needed.
- **Headache-type indications:** Vasodilators can trigger migraine and cluster headache attacks, which is a safety concern for those predictions.

Package insert warnings were not available for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked alopecia prediction and the other hair, migraine and cephalalgia predictions)

**Rationale:**
- Alopecia and the related hair disorders have no clinical trials, no literature and no plausible mechanism. The high scores appear to be model artefacts.
- Acute pulmonary heart disease (**Proceed with Guardrails**) has the strongest supported direction, though the evidence is partly indirect. Congestive heart failure is an established use rather than repurposing.
- Headache disorder remains a research question limited to RCVS case reports.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator (a blocking gap for safety screening)
- Approved indication text for the Indian licences
- Detailed mechanism-of-action data from DrugBank
- For acute pulmonary heart disease: trials in right heart failure or pulmonary hypertension specifically, rather than heterogeneous critically ill populations
- For RCVS: controlled data beyond case reports before any broader headache claim
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

