---
layout: default
title: Adenosine
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 2
---

# Adenosine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Adenosine: From Supraventricular Tachycardia to Catecholaminergic Polymorphic Ventricular Tachycardia

---

## One-Sentence Summary

Adenosine is an endogenous purine nucleoside clinically used for the acute termination of supraventricular tachycardia (SVT) and as a pharmacological stress agent in cardiac imaging.
The TxGNN model predicts it may have therapeutic potential in **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)**, a rare inherited arrhythmia syndrome that can cause sudden cardiac death in young patients,
with **1 Phase 2a clinical trial** (investigating an adenosine receptor agonist in CPVT) and **13 publications** currently supporting this mechanistic direction.

> **Important note on prediction ranking:** The highest-ranked TxGNN prediction (Rank 1: "obsolete bundle branch block," score 99.94%) uses a deprecated Disease Ontology term with no mappable clinical evidence (L5 / Hold). This report therefore focuses on **Rank 2: CPVT** (score 99.42%, L3), which carries actionable mechanistic and translational signals.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Supraventricular tachycardia (SVT) termination; pharmacological cardiac stress testing |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L3 — Observational study, mechanistic literature, and 1 related Phase 2a trial |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Adenosine acts primarily through the **A1 adenosine receptor**, activating Gi/o proteins that inhibit adenylyl cyclase, suppress intracellular cAMP, and reduce protein kinase A (PKA) activity. In cardiac tissue, this produces transient AV nodal block and hyperpolarization — the mechanism behind its established use in terminating re-entrant SVT. Crucially, this is the same signalling axis that drives CPVT arrhythmogenesis: catecholamine-induced cAMP elevation → PKA hyperphosphorylation of RyR2 → diastolic sarcoplasmic reticulum (SR) calcium leak → delayed afterdepolarizations (DADs) → triggered bidirectional ventricular tachycardia. Adenosine's ability to suppress β-adrenergic/cAMP signalling positions it pharmacologically to interrupt this cascade from upstream.

A direct clinical proof of concept exists: PMID 18313614 documents ATP (which is rapidly dephosphorylated in vivo to adenosine) successfully terminating bidirectional ventricular tachycardia in a CPVT patient. Structural biology data (PMID 23747301) further show that ATP interacts directly with the CPVT-mutation-associated central domain of RyR2, suggesting an additional molecular mechanism beyond cAMP suppression alone. Complementary gene therapy studies (PMID 38776406) demonstrate that enhancing cAMP degradation (PDE2A/PDE4B overexpression) prevents CPVT-related arrhythmias in animal models — effectively reverse-validating the therapeutic logic of using adenosine to dampen cAMP.

The key practical challenge is Adenosine's ultra-short plasma half-life (~10 seconds, IV only), which limits it to acute intervention rather than chronic CPVT prophylaxis. Whether selective, longer-acting A1R agonists (e.g., the investigational AGP100 in NCT07263139) can translate this mechanism into durable benefit remains the central unanswered question for this repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT07263139](https://clinicaltrials.gov/study/NCT07263139) | Phase 2a | Recruiting | 10 | Investigating AGP100, a selective adenosine receptor agonist (putatively A1R-selective), for safety, tolerability, and exploratory efficacy in CPVT. Addresses the unmet need of patients whose arrhythmias are not fully controlled by existing treatments during exercise or stress. While AGP100 is not Adenosine itself, the trial provides pathway-level proof of concept that adenosine receptor signalling is a viable therapeutic target in CPVT. Completion expected June 2027. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Case Report | *Heart Rhythm* | ATP (converted in vivo to adenosine) successfully terminated bidirectional ventricular tachycardia in a CPVT patient — the most directly relevant clinical evidence linking the adenosine pathway to CPVT arrhythmia termination. |
| [23747301](https://pubmed.ncbi.nlm.nih.gov/23747301/) | 2013 | Basic Science | *Biochim Biophys Acta* | ATP interacts directly with the CPVT mutation-associated central domain of RyR2, suggesting adenosine/ATP may stabilize the mutant receptor through a direct molecular mechanism beyond cAMP suppression. |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Review | *Europace* | Multi-society consensus statement (ESC/HRS/APHRS/LAHRS) on pharmacological provocation testing in cardiac electrophysiology, including adenosine protocols for arrhythmia characterization — contextualizes Adenosine's established role in electrophysiology. |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Clinical Observational | *Heart Rhythm* | Postpacing repolarization abnormalities in CPVT with RyR2 mutation during EPS; highlights the limited utility of standard EP testing and the need for pharmacological approaches including catecholamine/adenosine-based protocols. |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | Basic Science | *Cardiovascular Research* | PDE2A/PDE4B gene therapy prevents heart failure and arrhythmias by improving subcellular cAMP compartmentation in mice; reverse-validates that suppressing cAMP signalling (Adenosine's mechanism via A1R) protects against CPVT-related arrhythmias. |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | In Vitro (Organ-on-Chip) | *J Physiology* | Human cardiac-neural microtissues reveal CPVT is a disease of both cardiomyocytes and sympathetic neurons; sympatho-cardiac crosstalk underpins arrhythmogenesis, reinforcing the importance of adrenergic pathway modulation — consistent with Adenosine's sympatholytic mechanism. |
| [35577932](https://pubmed.ncbi.nlm.nih.gov/35577932/) | 2022 | Basic Science | *Communications Biology* | TECRL deficiency causes aberrant mitochondrial function and aggravated CPVT phenotype in cardiomyocytes; highlights the molecular heterogeneity of CPVT subtypes that any adenosine-based therapy would need to consider. |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | Basic Science | *Science Translational Medicine* | SR calcium leak via RyR2 drives arrhythmia but not necessarily heart failure progression; RyR2 stabilization with rycal S36 improved survival — frames the calcium-handling target that Adenosine indirectly modulates via cAMP suppression. |
| [39148245](https://pubmed.ncbi.nlm.nih.gov/39148245/) | 2024 | Review | *Paediatric Anaesthesia* | Review of pediatric arrhythmias including CPVT and inherited channelopathies for anesthesiologists; discusses Adenosine's role in SVT management in pediatric patients, providing real-world safety context for the age group most affected by CPVT. |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | Review | *J Assoc Physicians India* | Classification and management of idiopathic VT in structurally normal hearts; describes adenosine-sensitive VT subtypes (RVOT/LVOT tachycardias) and places CPVT in the broader differential context of adenosine-responsive arrhythmias. |

---

## Safety Considerations

**Drug Interactions:** 138 interactions identified in DDInter. The following are the most clinically significant:

| Severity | Interacting Drug | Clinical Relevance |
|----------|-----------------|-------------------|
| **Major** | Cisapride | Additive QT prolongation — risk of torsades de pointes; concurrent use contraindicated |
| **Major** | Dolasetron | Additive QT prolongation — cardiac monitoring required |
| **Major** | Papaverine | Additive vasodilation and hypotension risk; may potentiate Adenosine's haemodynamic effects |
| **Moderate** | Clarithromycin | QT prolongation risk — monitor ECG |
| **Moderate** | Levofloxacin | QT prolongation risk — monitor ECG |
| **Moderate** | Ondansetron | QT prolongation risk — monitor ECG |
| **Moderate** | Granisetron | QT prolongation risk — monitor ECG |
| **Moderate** | Famotidine | Enhanced cardiac effects — monitor |
| **Moderate** | Palonosetron | Monitor for cardiac effects |

> For complete key warnings and contraindications, please refer to the product package insert. Formal package insert data was not available in this Evidence Pack (Data Gap DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Adenosine possesses a well-grounded mechanistic basis for CPVT (A1R-mediated cAMP suppression counters the catecholamine-driven RyR2 destabilization that underlies CPVT), supported by direct clinical evidence from a case report of ATP/adenosine terminating CPVT-related bidirectional VT (PMID 18313614). However, Adenosine is not registered in India, carries no direct Phase 2/3 RCT evidence in CPVT, and its ultra-short half-life (~10 seconds, IV bolus only) renders it unsuitable for chronic arrhythmia prophylaxis in its current form. The single ongoing trial (NCT07263139) tests a related adenosine receptor agonist (AGP100), not Adenosine itself. The hypothesis is scientifically credible but requires dedicated translational development before it can be advanced to clinical evaluation.

**To proceed, the following is needed:**
- Retrieve full Adenosine MOA and safety data from DrugBank API to resolve Data Gap DG002
- Obtain package insert warnings and contraindications (Data Gap DG001) to enable S1 safety evaluation
- Confirm AGP100's chemical identity and pharmacological relationship to Adenosine — if it is a selective A1R agonist, its Phase 2a results (NCT07263139, expected 2027) will be directly informative for this repurposing hypothesis
- Conduct a systematic review specifically on adenosine/ATP use in CPVT and calcium-handling arrhythmias (RyR2-related disorders)
- Evaluate longer-acting selective A1R agonists as candidate molecules that could deliver Adenosine's mechanism with a pharmacokinetic profile suitable for chronic CPVT management
- Consider a prospective mechanistic pilot study: adenosine administration during supervised exercise stress testing in CPVT patients to assess acute arrhythmia suppression as a proof of concept
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

