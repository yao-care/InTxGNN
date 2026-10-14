---
layout: default
title: Terlipressin
parent: Model Prediction Only (L5)
nav_order: 825
evidence_level: L5
indication_count: 10
---

# Terlipressin
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

# Terlipressin: From Portal Hypertension-Related Conditions to Pulmonary Hypertension

## One-Sentence Summary

Terlipressin is a long-acting vasopressin analogue given by injection, widely marketed in India. The TxGNN model's top-ranked predictions were eye conditions (glaucoma), but these have no supporting evidence. The best-supported prediction is **Pulmonary Hypertension**, which has **no registered clinical trials** and about **20 publications**, mostly small physiological studies, case reports and observational work.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the data compiled for this report (the Indian licence records contain no approved-indication text) |
| Predicted New Indication | Open-angle glaucoma (rank 1, TxGNN score 99.78%). Evidence review shows pulmonary hypertension (rank 3, score 99.56%) is the only prediction with meaningful supporting literature, so it is the focus of this report |
| TxGNN Prediction Score | 99.78% for open-angle glaucoma; 99.56% for pulmonary hypertension |
| Evidence Level | L5 for open-angle glaucoma; L3 for pulmonary hypertension |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold (open-angle glaucoma); Research Question for pulmonary hypertension, which is closest to Proceed with Guardrails only after further study |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, terlipressin is a synthetic vasopressin analogue that acts mainly on V1 receptors, causing systemic and splanchnic vasoconstriction.

**Open-angle glaucoma (top-ranked prediction).** No plausible mechanism for lowering intraocular pressure is apparent. Systemic vasoconstriction could in theory reduce ocular perfusion, which is a potential safety concern rather than a benefit. The very high score likely reflects knowledge-graph connectivity artefacts. No trials or literature support it. The same applies to the related eye predictions (primary hereditary glaucoma, "glaucoma 1, open angle", glaucoma, esotropia).

**Pulmonary hypertension (best-supported prediction).** Small haemodynamic studies in cirrhotic patients with portopulmonary or pulmonary hypertension suggest terlipressin may lower pulmonary vascular resistance and pressure while raising systemic pressure. Other vasoconstrictors can worsen pulmonary pressures. Case reports also describe rescue use in persistent pulmonary hypertension of the newborn with refractory shock. This selective effect gives a plausible, though unproven, rationale. The evidence is limited to small studies and case reports, and many retrieved papers concern portal hypertension, which is a different condition.

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

## Literature Evidence

Publications relevant to pulmonary hypertension:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22893473](https://pubmed.ncbi.nlm.nih.gov/22893473/) | 2012 | Cohort | Hepatobiliary Pancreat Dis Int | In 7 cirrhotic patients with pulmonary hypertension, the first terlipressin dose (2 mg) reduced pulmonary vascular resistance and improved pulmonary pressures |
| [21733953](https://pubmed.ncbi.nlm.nih.gov/21733953/) | 2012 | Cohort | Angiology | Echo study showing different effects of terlipressin on pulmonary versus systemic haemodynamics in cirrhosis with and without pulmonary hypertension |
| [18280605](https://pubmed.ncbi.nlm.nih.gov/18280605/) | 2008 | Case report | J Hepatol | Significant reduction in pulmonary arterial pressure after 1 week of terlipressin in portopulmonary hypertension |
| [15259082](https://pubmed.ncbi.nlm.nih.gov/15259082/) | 2004 | Echocardiographic study | World J Gastroenterol | Effect of terlipressin on systolic pulmonary artery pressure in cirrhosis |
| [32999121](https://pubmed.ncbi.nlm.nih.gov/32999121/) | 2020 | Case report | Indian Pediatr | Rescue terlipressin for persistent pulmonary hypertension and refractory shock in a preterm infant |
| [21292065](https://pubmed.ncbi.nlm.nih.gov/21292065/) | 2011 | Case report | J Pediatr Surg | Rescue therapy for refractory pulmonary hypertension in a neonate with congenital diaphragmatic hernia |
| [19624374](https://pubmed.ncbi.nlm.nih.gov/19624374/) | 2009 | Case series/report | Paediatr Anaesth | Role of terlipressin in severe pulmonary hypertension in congenital diaphragmatic hernia |
| [30971593](https://pubmed.ncbi.nlm.nih.gov/30971593/) | 2019 | Comparative study | Ann Card Anaesth | Terlipressin versus norepinephrine to prevent milrinone-induced systemic hypotension in cardiac surgery patients with pulmonary hypertension, hypothesised to avoid raising pulmonary pressures |
| [34179513](https://pubmed.ncbi.nlm.nih.gov/34179513/) | 2021 | Systematic review protocol | BMJ Paediatr Open | Protocol to review efficacy and safety of vasopressin and terlipressin in preterm neonates |

Note: the single paper retrieved for "glaucoma" (PMID 31841026, dobutamine reversing terlipressin's cardio-suppressive effects in cirrhosis) is unrelated to glaucoma and provides no support.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 82500 | Erlipress 1mg Injection | Vial of 10 ml injection | Not stated |
| 183301 | Qupressin 1mg Injection | Vial of 10 ml injection | Not stated |
| 223046 | Terlibax 1mg Injection | Vial of 1 injection | Not stated |
| 229294 | Terlicon Injection | Ampoule of 10 ml injection | Not stated |
| 218807 | Thinwes 1mg Injection | Vial of 10 ml injection | Not stated |

There are 20 valid single-ingredient licences in total, all injectable. Only the first five are shown.

## Safety Considerations

- **Respiratory failure and ischaemic events** are known terlipressin concerns and are particularly relevant for any pulmonary or cardiovascular use.
- Systemic vasoconstriction could theoretically reduce ocular perfusion, which is relevant to the glaucoma predictions.
- Headache is a known adverse effect of vasopressin analogues.
- Cardiovascular risks may matter in hyperthyroid patients.

Please refer to the package insert for full warnings, contraindications and drug interaction information. No label-based safety data or interaction data were available for this report.

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked glaucoma predictions and all other predictions without evidence). **Pulmonary hypertension is a Research Question** worth further study.

**Rationale:**
- The highest-scoring predictions (glaucoma and related eye conditions) have no clinical or literature support and no plausible mechanism, so they likely reflect knowledge-graph artefacts.
- Pulmonary hypertension has a plausible mechanism and small supportive studies, but the evidence is limited to small haemodynamic studies and case reports, with no registered trials.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for Indian-marketed products, and the approved indications, which are currently blank
- Mechanism of action data from DrugBank
- Controlled studies of terlipressin in pulmonary hypertension, with safety endpoints for respiratory failure and ischaemia
- Route and dosing compatibility assessment for the proposed use
- Specific evaluation in the populations where evidence exists (cirrhosis with portopulmonary hypertension, neonates)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

