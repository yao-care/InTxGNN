---
layout: default
title: Sotalol
parent: Model Prediction Only (L5)
nav_order: 778
evidence_level: L5
indication_count: 7
---

# Sotalol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Sotalol: From Cardiac Arrhythmia to Sick Sinus Syndrome 2, Autosomal Dominant

## One-Sentence Summary

> Sotalol is a Class II/III antiarrhythmic (non-selective β-blocker combined with potassium-channel blockade), with an established clinical role in atrial fibrillation/flutter rhythm control and ventricular arrhythmias.
> TxGNN's top-ranked prediction is **Sick Sinus Syndrome 2, Autosomal Dominant**, but this is **not a credible repurposing signal** — sotalol suppresses sinus node automaticity and is a known contraindication in sick sinus syndrome, so the high graph score most likely reflects proximity noise rather than a real therapeutic relationship.
> Of the 7 candidates in this evidence pack, none reach a robust evidence tier; the only one with any real supporting data is an indirect stroke-risk signal (via AF rhythm control), rated **L3 / "Research Question"**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not extractable from India licensing data (0 registrations on file); per drug class and cited literature, sotalol's established use is cardiac arrhythmia — atrial fibrillation/flutter rhythm control and ventricular arrhythmias |
| Predicted New Indication | Sick sinus syndrome 2, autosomal dominant — **flagged as mechanistically implausible, see below** |
| TxGNN Prediction Score | 99.76% (rank 4825 in global candidate pool) |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

**It is not.** Sotalol's own mechanism argues against this prediction. As a non-selective β-blocker (Class II) with additional Class III potassium-channel blocking activity, sotalol reduces sinus node automaticity and heart rate. Sick sinus syndrome is a disorder of *already impaired* sinus node function — using a drug that further suppresses sinus automaticity in this population is a recognized **contraindication**, not a treatment rationale. The evidence pack's own rationale field for this candidate states this explicitly: the prediction is "opposite to established clinical pharmacology" and represents "knowledge-graph proximity misjudgment, not a therapeutic association."

The same conclusion applies to most of the lower-ranked candidates in this pack: Wildervanck syndrome, sarcoglycanopathy, macrocephaly-dysmorphic-facies-psychomotor-retardation syndrome, and the deprecated ontology term "obsolete susceptibility to ischemic stroke" all have **zero supporting trials or literature**, and no plausible mechanistic link to sotalol's β-blocking/K⁺-channel-blocking pharmacology.

The one candidate with partial biological plausibility is **stroke disorder** (rank 4): sotalol is an established rhythm-control agent for atrial fibrillation, and AF is a major risk factor for ischemic stroke, so effective rhythm control could plausibly reduce downstream stroke risk. However, none of the supporting trials use stroke as a primary endpoint for sotalol specifically — they mostly compare ablation vs. antiarrhythmic drug strategies for AF, with sotalol appearing as one comparator/control arm among several. This is indirect, extrapolated evidence, not direct proof of a stroke-prevention indication.

---

## Clinical Trial Evidence (Rank 1: Sick Sinus Syndrome 2, Autosomal Dominant)

Currently no related clinical trials registered.

## Literature Evidence (Rank 1: Sick Sinus Syndrome 2, Autosomal Dominant)

Currently no related literature available.

---

## Other Ranked Candidates in This Evidence Pack

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|------|------|------|------|
| 1 | Sick sinus syndrome 2, autosomal dominant | 99.76% | L5 | Hold | Mechanistically contraindicated, likely graph artifact |
| 2 | Wildervanck syndrome | 99.65% | L5 | Hold | No known mechanistic link; zero evidence |
| 3 | Sarcoglycanopathy | 99.64% | L5 | Hold | Cardiac involvement is a downstream complication, not a treatment target; zero evidence |
| 4 | Stroke disorder | 99.44% | L3 | **Research Question** | Only candidate with real (indirect) supporting evidence — see below |
| 5 | Manic bipolar affective disorder | 99.43% | L4 | Hold | Literature describes a **drug-safety risk** (QT prolongation with antipsychotics), not efficacy |
| 6 | Macrocephaly, dysmorphic facies, and psychomotor retardation | 99.42% | L5 | Hold | No mechanistic link; zero evidence |
| 7 | Obsolete susceptibility to ischemic stroke | 99.23% | L5 | Hold | Deprecated ontology term; should be removed from candidate list |

### Rank 4 — Stroke Disorder: Supporting Evidence (indirect, via AF rhythm control)

**Clinical Trials**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | NA | Completed | 2,204 | CABANA trial: catheter ablation vs. rate/rhythm-control drug therapy (incl. sotalol) for AF; largest comparator trial in this set |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | N/A (SLR/NMA) | Completed | 87,810 | Systematic review/network meta-analysis comparing safety of dronedarone vs. sotalol directly in AF patients |
| [NCT00007605](https://clinicaltrials.gov/study/NCT00007605) | Phase 3 | Completed | 706 | CSP #399: compares amiodarone and sotalol for maintaining sinus rhythm in AF; background notes ~75,000 AF-related strokes/year |
| [NCT02145546](https://clinicaltrials.gov/study/NCT02145546) | Phase 4 | Unknown | 600 | Sotalol, amiodarone, propafenone effects on AF burden in sick sinus syndrome patients post-pacing (post-hoc AF, not primary SSS treatment) |
| [NCT00523978](https://clinicaltrials.gov/study/NCT00523978) | Phase 3 | Completed | 245 | STOP AF: cryoablation vs. drug therapy (incl. sotalol) after failure of AAD in paroxysmal AF |
| [NCT07405671](https://clinicaltrials.gov/study/NCT07405671) | Phase 4 | Not yet recruiting | 988 | Flecainide vs. standard rhythm-control drugs (sotalol/amiodarone) in AF with stable CAD |
| [NCT05511389](https://clinicaltrials.gov/study/NCT05511389) | NA | Recruiting | 1,500 | Cardioversion shock-vector RCT for AF; disease-area overlap only |
| [NCT03118518](https://clinicaltrials.gov/study/NCT03118518) | NA | Completed | 225 | Cryoballoon ablation vs. AAD-naive paroxysmal AF |
| [NCT01447862](https://clinicaltrials.gov/study/NCT01447862) | Phase 4 | Completed | 101 | Vernakalant vs. ibutilide in recent-onset AF |
| [NCT03737929](https://clinicaltrials.gov/study/NCT03737929) | NA | Recruiting | 228 | Hybrid ablation vs. conventional catheter ablation, persistent AF |

**Literature**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | RCT | Circ Arrhythm Electrophysiol | Dronedarone vs. sotalol head-to-head in AAD-naive veterans with AF; effectiveness/safety comparison |
| [1281807](https://pubmed.ncbi.nlm.nih.gov/1281807/) | 1992 | RCT | Int J Cardiol | Sotalol efficacy/safety in complex ventricular arrhythmias (n=356), ~76% reduction in PVCs |
| [29954667](https://pubmed.ncbi.nlm.nih.gov/29954667/) | 2019 | Cohort | Int J Cardiol | Sotalol efficacy and safety in adults with congenital heart disease and arrhythmia |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohort | J Atr Fibrillation | Real-world risk of CV events/**stroke**/CHF: dronedarone vs. amiodarone and other antiarrhythmics including sotalol |
| [38011245](https://pubmed.ncbi.nlm.nih.gov/38011245/) | 2023 | Review | Circulation | Contemporary AF management in hypertrophic cardiomyopathy, including stroke risk stratification |
| [25430048](https://pubmed.ncbi.nlm.nih.gov/25430048/) | 2014 | Review | BMJ Clin Evid | Acute-onset AF management; AF increases stroke and heart failure risk |
| [39077579](https://pubmed.ncbi.nlm.nih.gov/39077579/) | 2023 | Review | Rev Cardiovasc Med | Managing AF during pregnancy, incl. antiarrhythmic risk-benefit |
| [11445058](https://pubmed.ncbi.nlm.nih.gov/11445058/) | 2001 | Review | Curr Treat Options Cardiovasc Med | Atrial flutter treatment overview |
| [37777295](https://pubmed.ncbi.nlm.nih.gov/37777295/) | 2023 | Guideline | Am J Cardiol | ACC/AHA/HRS and ESC guideline recommendations on AAD selection |
| [8346725](https://pubmed.ncbi.nlm.nih.gov/8346725/) | 1993 | Study | Am J Cardiol | Oral sotalol hemodynamic effects in patients with ventricular arrhythmias and structural heart disease |

### Rank 5 — Manic Bipolar Affective Disorder: Not an Efficacy Signal

The 3 cited references (PMID 39179332, 32124390, 10958269) describe **cardiac safety risks** — QT-prolongation/torsades risk when β-blockers like sotalol are combined with antipsychotics (e.g., risperidone), and a case report of symptomatic bradycardia during lithium therapy. This is a drug-safety caution, not evidence that sotalol treats bipolar disorder.

---

## India Market Information

Sotalol currently has **no registered license in India** (0 registrations, market status: Not Marketed). No product-level dosage form or approved-indication data is available in this evidence pack.

---

## Safety Considerations

- **Drug Interactions**: 288 documented interactions on file. Notable **Major**-severity interactions include Epinephrine, Clarithromycin, Picosulfuric acid, and Polyethylene glycol (3350 with electrolytes) — combined use warrants caution given sotalol's QT-prolonging and bradycardic pharmacology. Several **Moderate**-level interactions with anticholinergic and antidiabetic agents (e.g., Atropine, Hyoscyamine, Canagliflozin, Dapagliflozin, Cimetidine) are also on file.
- **Data Gap (Blocking)**: India label warnings and contraindications are not yet available for this drug (DG001), which currently blocks a formal S1 safety review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (sick sinus syndrome) is mechanistically implausible and likely a knowledge-graph artifact rather than a genuine repurposing signal. No candidate in this evidence pack reaches a level of evidence sufficient to justify advancing past a research hypothesis, and the one partially-supported candidate (stroke, via AF rhythm control) relies only on indirect trial evidence with no dedicated stroke endpoint. A Blocking data gap on India label warnings/contraindications (DG001) also prevents formal safety screening at this stage.

**To proceed, the following is needed:**
- Resolve DG001 (India/TFDA label warnings & contraindications) before any S1 safety review
- Resolve DG002 (confirmed MOA from DrugBank) to formally support or refute mechanistic rationale
- If pursuing the stroke-risk angle: identify or commission trials/meta-analyses using stroke incidence as a primary or pre-specified endpoint for sotalol specifically, rather than relying on ablation-vs-drug comparator trials
- Re-evaluate or exclude the top-ranked candidate (sick sinus syndrome) as likely model noise before any further workflow stage
- Remove "obsolete susceptibility to ischemic stroke" (rank 7) from active candidate tracking — it is a deprecated ontology term
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

