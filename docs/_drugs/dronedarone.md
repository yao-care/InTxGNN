---
layout: default
title: Dronedarone
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Dronedarone
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

# Dronedarone: From Atrial Fibrillation to Stroke Disorder

## One-Sentence Summary

Dronedarone (brand: Multaq) is a multichannel-blocking antiarrhythmic drug approved in the US and EU for the management of paroxysmal or persistent atrial fibrillation (AF) and atrial flutter, aimed at reducing cardiovascular hospitalization.
The TxGNN model predicts it may be effective against **Stroke Disorder**, with **19 clinical trials** and **20 publications** currently supporting this direction.
The evidence picture is nuanced — while post-hoc analyses of the ATHENA trial suggest stroke reduction in paroxysmal/persistent AF, the pivotal PALLAS trial (NCT01151137, n=3,236) was terminated early due to a paradoxical **increase** in stroke risk among permanent AF patients, establishing an important safety boundary for any repurposing attempt.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atrial fibrillation / atrial flutter (rhythm control; US FDA approved 2009, EMA approved 2009) |
| Predicted New Indication | Stroke Disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L2 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not currently available in the evidence pack. Based on established pharmacological knowledge, Dronedarone is a benzofuran-derived amiodarone analogue that blocks multiple ion channels (Na⁺, K⁺, Ca²⁺) and exerts antiadrenergic effects, without iodine substitution (reducing thyroid-related toxicity). Its primary clinical effect is maintenance of sinus rhythm and ventricular rate control in AF/AFL patients.

The mechanistic link between Dronedarone and stroke disorder operates via two independent pathways. The first is a **rhythm-control pathway**: maintaining sinus rhythm reduces stasis in the left atrial appendage, thereby decreasing formation of thrombi responsible for cardioembolic stroke — AF is estimated to increase stroke risk fivefold. The second is a **direct antithrombotic pathway**: a mechanistic study (PMID 28992468) demonstrated that Dronedarone inhibits PAR-1 (thrombin receptor) and the TXA₂ pathway independently of its antiarrhythmic action, reducing platelet activation and blood thrombogenicity. Post-hoc analysis of the ATHENA trial confirmed a reduced rate of stroke and TIA in patients with paroxysmal/persistent AF on Dronedarone.

However, the prediction carries a critical population-specific safety signal. The PALLAS trial showed that in **permanent AF** patients (where sinus rhythm cannot be restored), Dronedarone significantly increased the risk of stroke, heart failure, and death, leading to early termination. This heterogeneity means any repurposing effort must strictly restrict the target population to **paroxysmal or persistent AF** with preserved cardiac function — not permanent AF, and not patients with severe heart failure.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01151137](https://clinicaltrials.gov/study/NCT01151137) | Phase 3 | Terminated | 3,236 | **PALLAS trial**: Dronedarone in permanent AF with risk factors — primary endpoint included stroke/embolism/MI/CV death. Terminated early due to significantly increased stroke risk, heart failure, and CV mortality. Defines the safety boundary for use. |
| [NCT05130268](https://clinicaltrials.gov/study/NCT05130268) | Phase 4 | Completed | 339 | Pragmatic RCT of early Dronedarone vs usual care in first-detected AF. Evaluates whether early rhythm control with Dronedarone improves outcomes including stroke prevention; results published 2024–2025 (PMID 40295782, 40387892). |
| [NCT07270848](https://clinicaltrials.gov/study/NCT07270848) | Phase 4 | Not Yet Recruiting | 1,898 | Large prospective multicenter RCT comparing Dronedarone vs comparator for early rhythm control in AF diagnosed within the past year; safety and stroke-related outcomes to be assessed through 2028. |
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2,789 | **EAST trial**: Early structured rhythm control (including Dronedarone) vs usual care in AF patients; demonstrated that early rhythm control reduces composite of CV death, stroke, and hospitalization for HF/worsening rhythm symptoms (NEJM 2020). |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | Not Yet Recruiting | 1,746 | Early rhythm control therapy in acute ischemic stroke patients with AF; Dronedarone is a candidate antiarrhythmic agent. Stroke prevention is the primary research question. |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | Completed | 2,204 | **CABANA trial**: Catheter ablation vs antiarrhythmic drugs (including Dronedarone) for AF. Stroke was a secondary endpoint; provides indirect comparative data on rhythm control and cerebrovascular outcomes. |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | N/A | Completed | 87,810 | Systematic literature review and NMA comparing Dronedarone vs Sotalol safety in AF; large-scale evidence synthesis of real-world cardiovascular event risk. |
| [NCT04704050](https://clinicaltrials.gov/study/NCT04704050) | Phase 4 | Terminated | 22 | **EDORA trial**: Dronedarone vs placebo post-ablation for AF recurrence and atrial fibrosis progression; terminated early due to slow enrollment. |
| [NCT06125925](https://clinicaltrials.gov/study/NCT06125925) | N/A | Recruiting | 436 | RFCA vs antiarrhythmic drugs (potential Dronedarone) in AF patients with HFpEF; long-term cardiovascular outcome including stroke as secondary endpoint. |
| [NCT05939076](https://clinicaltrials.gov/study/NCT05939076) | Phase 3 | Not Yet Recruiting | 220 | Cryoablation vs antiarrhythmic drugs for persistent AF; AF freedom at 12 months as primary endpoint, cerebrovascular events tracked as secondary. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | Post-hoc RCT Analysis | Clinical Research in Cardiology | Evaluated long-term safety and efficacy of amiodarone and Dronedarone for early rhythm control in EAST-AFNET 4; assesses stroke-related outcomes in contemporary clinical setting. |
| [40295782](https://pubmed.ncbi.nlm.nih.gov/40295782/) | 2025 | Post-hoc RCT Analysis | Europace | Post-hoc analysis of ATHENA using EAST-AFNET 4 criteria; Dronedarone 400mg BID improved cardiovascular outcomes vs placebo in early AF patients with cardiovascular comorbidities, supporting stroke risk reduction in appropriate populations. |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Mechanistic Study | Atherosclerosis | Demonstrated Dronedarone inhibits PAR-1 (thrombin receptor) and TXA₂ pathway, exerting anticoagulant and antiplatelet effects independent of antiarrhythmic action — directly supports stroke prevention mechanism. |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Comparative Cohort | Circulation: Arrhythmia and Electrophysiology | Retrospective comparison of Dronedarone vs Sotalol in antiarrhythmic-naive veterans with AF; provides real-world comparative safety and effectiveness data including thromboembolic events. |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Pharmacoepidemiological Study | Journal of Atrial Fibrillation | Assessed risks of stroke, CV events, congestive heart failure, and liver injury for Dronedarone vs other antiarrhythmics in 10,455 US patients; real-world stroke risk quantification. |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | Post-hoc Subgroup Analysis | European Journal of Heart Failure | Post-hoc ATHENA analysis in AF/AFL with HFpEF and HFmrEF; Dronedarone reduced cardiovascular events in this subgroup, relevant to the high-risk stroke population. |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review / Drug Approval Analysis | Vascular Health and Risk Management | Summarizes Dronedarone FDA approval and ATHENA trial data; post-hoc analysis showed decreased stroke risk with Dronedarone use in paroxysmal/persistent AF patients. |
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | RCT (PALLAS) | New England Journal of Medicine | **Critical safety reference**: Dronedarone in high-risk permanent AF — trial terminated early due to increased rates of stroke, heart failure, and CV death. Essential reading for understanding population restrictions. |
| [22149318](https://pubmed.ncbi.nlm.nih.gov/22149318/) | 2011 | Systematic Review & Meta-analysis | American Journal of Cardiovascular Drugs | Meta-analysis of randomized trials on Dronedarone and stroke incidence in paroxysmal or persistent AF; quantified stroke risk reduction from ATHENA and related trials. |
| [20396635](https://pubmed.ncbi.nlm.nih.gov/20396635/) | 2010 | RCT Secondary Analysis | Clinical Interventions in Aging | Analyzed Dronedarone's impact on stroke reduction in AF/AFL treatment; provides subgroup analysis supporting stroke prevention benefit in intermittent AF. |

---

## India Market Information

Dronedarone is currently **not marketed in India**. No drug authorizations or registered products were identified in the India regulatory database.

> For reference, Dronedarone (Multaq®) is approved in the US (FDA, 2009) and EU (EMA, 2009) for the indication of maintaining sinus rhythm in adult patients with paroxysmal or persistent AF/AFL who have had a prior episode and have no current AF. These approvals explicitly exclude patients with permanent AF, decompensated heart failure, or severe hepatic impairment.

---

## Safety Considerations

**Drug-Drug Interactions (DDIs)**

Dronedarone has a substantial DDI burden with **253 documented interactions** (source: DDInter). Key major interactions include:

| Interacting Drug | Severity | Clinical Concern |
|-----------------|----------|-----------------|
| Clarithromycin | Major | CYP3A4 inhibition markedly increases Dronedarone plasma levels; risk of QT prolongation and proarrhythmia |
| Loperamide | Major | P-gp inhibition by Dronedarone may increase Loperamide exposure; cardiac conduction risk |
| Dolasetron | Major | Additive QT-prolonging effect; risk of Torsades de Pointes |
| Hydrocortisone | Major | Electrolyte disturbances (hypokalaemia) potentiate proarrhythmic risk |
| Amphotericin B (all formulations) | Major | Amphotericin-induced hypokalaemia and hypomagnesaemia increase the risk of Dronedarone-related arrhythmias |
| Polyethylene glycol (3350 with electrolytes) | Major | Electrolyte shifts may precipitate QT prolongation |
| Picosulfuric acid | Major | Bowel preparation-induced electrolyte loss heightens proarrhythmic risk |
| Famotidine | Moderate | May affect gastric pH and Dronedarone absorption |
| Dexamethasone | Moderate | Electrolyte disturbances; CYP3A4 interaction possible |
| Saxagliptin | Moderate | Dronedarone as CYP3A4/P-gp inhibitor may increase Saxagliptin exposure |

> ⚠️ **Note**: Detailed TFDA (Taiwan FDA) package insert warnings and contraindications were not available in this evidence pack. Please refer to the FDA/EMA-approved Multaq® SmPC for the full safety profile, including black-box warnings (permanent AF contraindication, hepatotoxicity, pulmonary toxicity) before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed and ongoing clinical trials — including the pivotal EAST trial (n=2,789) and ATHENA post-hoc analyses — demonstrate that Dronedarone can reduce stroke risk in **paroxysmal or persistent AF patients with preserved cardiac function**, and a mechanistic study (PMID 28992468) confirms direct antithrombotic properties independent of rhythm control. However, the PALLAS trial (n=3,236, terminated) is a hard constraint: repurposing must never extend to permanent AF patients, patients with decompensated heart failure (LVEF < 40%), or those with sick sinus syndrome without pacemaker protection.

**To proceed, the following is needed:**

- **Mechanistic data (MOA)**: Obtain full DrugBank/SmPC pharmacological profile to complete the mechanism-to-indication mapping
- **India regulatory pathway assessment**: Dronedarone is not currently marketed in India; a regulatory strategy for new indication approval or compassionate use must be defined
- **Strict patient selection criteria**: Define the eligible population (paroxysmal/persistent AF only, LVEF ≥ 40%, no permanent AF, no class III/IV HF) as a prerequisite for any prospective study design
- **Head-to-head comparison design**: Any new trial should position Dronedarone against NOACs (standard of care for AF stroke prevention) rather than placebo, given the evolved treatment landscape
- **Long-term safety monitoring plan**: Monitor for hepatotoxicity (LFTs at baseline, 1, 3, 6 months), pulmonary toxicity, and QT prolongation; a formal pharmacovigilance protocol is required given the DDI burden (253 interactions)
- **Post-hoc analysis of NCT05130268**: Results from this recently completed pragmatic RCT of early Dronedarone in first-detected AF (PMID 40295782, 40387892) should be reviewed in full before finalizing the development strategy

> **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

