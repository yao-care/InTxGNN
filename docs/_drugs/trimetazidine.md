---
layout: default
title: Trimetazidine
parent: 僅模型預測 (L5)
nav_order: 860
evidence_level: L5
indication_count: 10
---

# Trimetazidine
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

# Trimetazidine: From Angina Pectoris to Endolymphatic Hydrops

## One-Sentence Summary

> Trimetazidine is a metabolic anti-ischemic agent generally used for angina pectoris; it is **not currently marketed in India**, and no local approved-indication text is available in this Evidence Pack.
> The TxGNN model predicts it may be effective for **Endolymphatic Hydrops (Ménière's disease)**,
> supported by **2 historical randomized controlled trials** and **4 additional publications**, with no registered clinical trials to date.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angina pectoris (general drug knowledge; no approved-indication text available — drug not marketed in India) |
| Predicted New Indication | Endolymphatic Hydrops (Ménière's disease) |
| TxGNN Prediction Score | 98.57% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, trimetazidine is a metabolic anti-ischemic agent that inhibits fatty acid β-oxidation and shifts cellular energy production toward glucose oxidation, thereby protecting tissue under ischemic/metabolic stress. It is best known internationally as an anti-anginal agent.

The predicted new indication — endolymphatic hydrops, the pathological hallmark of Ménière's disease — has a plausible mechanistic link: the inner ear (cochlea and vestibular organs) is highly sensitive to microcirculatory and metabolic disturbance, and vascular/metabolic dysfunction is one of the leading hypotheses for endolymphatic hydrops. Trimetazidine's protective effect against ischemic energy stress could theoretically extend to inner ear tissue.

Notably, this is not a purely theoretical extrapolation: trimetazidine (as *Vastarel 20mg*) has a documented history of clinical use for vertigo and Ménière's disease, evidenced by two 1990s double-blind RCTs comparing it against betahistine (a standard Ménière's disease therapy). This historical precedent meaningfully strengthens the plausibility of the TxGNN prediction. The same underlying mechanism also drove high TxGNN scores for closely related ontology entries — cochlear, vestibular, and cochleovestibular subtypes of active Ménière's disease (ranks 3–5) — and for benign recurrent vertigo (rank 7), where trimetazidine was again studied for residual dizziness after BPPV repositioning maneuvers.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2240994](https://pubmed.ncbi.nlm.nih.gov/2240994/) | 1990 | RCT | Ann Otolaryngol Chir Cervicofac | Double-blind trial: trimetazidine (60mg/day) vs. betahistine (24mg/day) in 40 patients with peripheral vertigo, 20 of whom had Ménière's disease, over 3 months |
| [2240995](https://pubmed.ncbi.nlm.nih.gov/2240995/) | 1990 | RCT | Ann Otolaryngol Chir Cervicofac | Double-blind trial: trimetazidine (60mg/day) vs. betahistine (36mg/day) in 45 Ménière's disease patients (cochlear symptoms: vertigo, tinnitus, hearing loss) over 2 months |
| [10367069](https://pubmed.ncbi.nlm.nih.gov/10367069/) | 1999 | Review | Ann Otolaryngol Chir Cervicofac | Synopsis of clinical trials on Vastarel 20mg (trimetazidine) contribution to vertigo treatment |
| [26208913](https://pubmed.ncbi.nlm.nih.gov/26208913/) | 2016 | Review | Eur Arch Otorhinolaryngol | Molecular rationale for histamine-pathway therapy (betahistine) via histamine receptor expression in the human endolymphatic sac — supports the vascular/ion-transport hypothesis of endolymphatic hydrops relevant to trimetazidine's proposed mechanism |
| [19454061](https://pubmed.ncbi.nlm.nih.gov/19454061/) | 2007 | Review | BMJ Clin Evid | General overview of Ménière's disease clinical course and treatment options (background) |
| [16623983](https://pubmed.ncbi.nlm.nih.gov/16623983/) | 2006 | Review | J Laryngol Otol | Case series on rare pediatric Ménière's disease (background) |

**Related-indication corroborating evidence:** [26563011](https://pubmed.ncbi.nlm.nih.gov/26563011/) (2015, RCT, *B-ENT*) evaluated trimetazidine, betahistine, and ginkgo biloba for residual dizziness after BPPV repositioning maneuvers — a mechanistically adjacent vestibular indication (predicted rank 7, "benign recurrent vertigo").

---

## India Market Information

Trimetazidine currently has no marketing authorization in India (0 registrations); no license records are available in this Evidence Pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Local regulatory warnings/contraindications (equivalent to a TFDA label) could not be retrieved for this drug (Data Gap DG001, severity: Blocking) and represent a mandatory prerequisite before any S1 safety review.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two historical double-blind RCTs plus a supporting synopsis directly evaluated trimetazidine in Ménière's disease/vertigo, and this finding is reinforced by convergent TxGNN predictions across multiple related Ménière's disease ontology entries and benign recurrent vertigo. However, the evidence is decades old, of modest scale, and the drug has no current market presence in India, so it cannot proceed without additional safety and regulatory work.

**To proceed, the following is needed:**
- Local (India-equivalent) label warnings and contraindications — currently missing and blocking any safety assessment (DG001)
- Confirmed mechanism-of-action documentation (DG002)
- Re-evaluation of trimetazidine's known systemic safety profile (e.g., movement-disorder/Parkinsonism signal reported in other markets) against inner-ear indication use
- Assessment of route/formulation availability, since no dosage form data currently exists for this market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

