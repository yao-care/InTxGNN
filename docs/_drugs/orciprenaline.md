---
layout: default
title: Orciprenaline
parent: High Evidence (L1-L2)
nav_order: 615
evidence_level: L2
indication_count: 10
---

# Orciprenaline
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Orciprenaline: From Bronchial Asthma/Bronchospasm to Obstructive Lung Disease

## One-Sentence Summary

Orciprenaline (metaproterenol, DrugBank DB00816) is a non-selective β2-adrenergic agonist historically used as an inhaled bronchodilator for bronchial asthma and airway obstruction. The TxGNN model's top prediction — **Obstructive Lung Disease** — largely re-confirms this established pharmacological role rather than identifying a truly novel indication, and is currently supported by **5 clinical trials** and **20 publications**, though only one trial/publication set directly studies orciprenaline itself rather than related β2-agonists (fenoterol, salbutamol, etc.).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented — the drug is unmarketed in India (0 licenses), so no official indication text exists. Literature consistently identifies its historical use as a bronchodilator for bronchial asthma/bronchospasm. |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.9953% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data from DrugBank is currently unavailable (`original_moa`: Data Gap). Based on the evidence assembled, orciprenaline is a non-selective **β2-adrenergic receptor agonist** that directly relaxes bronchial smooth muscle — a textbook bronchodilator mechanism that maps directly onto the core pathophysiology of obstructive lung disease (increased airway resistance).

This is not a mechanistically distant repurposing story: multiple retrieved publications (e.g., PMID 8834341, 8341859, 1974678) describe orciprenaline/metaproterenol being directly compared against other β2-agonists (fenoterol, salbutamol, tulobuterol) and anticholinergics in exactly this disease population. In other words, TxGNN's highest-scoring prediction appears to be substantially rediscovering the drug's known, established pharmacological class use rather than surfacing a genuinely new therapeutic hypothesis — a useful sanity check on model validity, but weaker as a "new indication" business case.

A caveat: most of the clinical trial evidence retrieved involves *comparator* drugs (ipratropium, fenoterol, tiotropium) rather than orciprenaline as the study drug itself, so trial-level relevance grading is mixed (B/C), with only the literature directly confirming orciprenaline/metaproterenol's own efficacy in this population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01095016](https://clinicaltrials.gov/study/NCT01095016) | Phase 3 | Completed | 32 | Open-label, randomized, cross-over trial comparing Meptin® Swinghaler and Berotec N® aerosol in mild-to-moderate stable asthma (Grade B — bronchodilator class trial; orciprenaline not confirmed as study drug). |
| [NCT00274066](https://clinicaltrials.gov/study/NCT00274066) | Phase 3 | Completed | 65 | Evaluated acute bronchodilator effect of ipratropium and fenoterol vs. placebo on top of tiotropium in COPD (Grade C — comparator drugs, not orciprenaline). |
| [NCT01933984](https://clinicaltrials.gov/study/NCT01933984) | N/A | Completed | 51 | Individualized vs. fixed dosing of inhaled bronchodilator to reduce airway resistance in intubated COPD patients (Grade B — class-relevant, drug identity unconfirmed). |
| [NCT05183841](https://clinicaltrials.gov/study/NCT05183841) | N/A | Unknown | 40 | Effect of bronchodilators on exercise capacity in bronchiectasis patients (Grade C — atypical obstructive population, status unknown). |
| [NCT00460577](https://clinicaltrials.gov/study/NCT00460577) | Phase 4 | Completed | 60 | Randomized double-dummy trial: formoterol vs. nebulized ipratropium+fenoterol in children (5–<12y) with acute bronchial obstruction (Grade C — formoterol-based, indirect evidence). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8834341](https://pubmed.ncbi.nlm.nih.gov/8834341/) | 1996 | RCT | European Respiratory Journal | Double-blind study directly comparing nebulized glycopyrrolate and **metaproterenol (orciprenaline)**, alone and combined, for bronchodilation in stable COPD. |
| [8341859](https://pubmed.ncbi.nlm.nih.gov/8341859/) | 1993 | RCT | Respiration | Double-blind, randomized cross-over trial comparing fenoterol/ipratropium bromide with salbutamol in chronic obstructive lung disease (24 patients). |
| [7345424](https://pubmed.ncbi.nlm.nih.gov/7345424/) | 1981 | Review | Praxis und Klinik der Pneumologie | Review of bronchospasmolytic (bronchodilator) drug classes, covering β-adrenergic agents including orciprenaline. |
| [6142760](https://pubmed.ncbi.nlm.nih.gov/6142760/) | 1983 | Review | Clinical Reviews in Allergy | Review of adrenergic drugs used in obstructive airway disease. |
| [4942356](https://pubmed.ncbi.nlm.nih.gov/4942356/) | 1970 | Review | Medizinische Klinik | Review on allergic bronchial asthma management. |
| [2951816](https://pubmed.ncbi.nlm.nih.gov/2951816/) | 1986 | Cohort | Respiration | Controlled long-term (≥84 day) study of fenoterol + ipratropium bromide aerosol combination in chronic obstructive lung disease. |
| [2879458](https://pubmed.ncbi.nlm.nih.gov/2879458/) | 1987 | Cohort | The American Journal of Medicine | Double-blind ER study (199 patients) of nebulized anticholinergic and sympathomimetic regimens in acute airway obstruction (asthma/COAD). |
| [2951811](https://pubmed.ncbi.nlm.nih.gov/2951811/) | 1986 | Cohort | Respiration | Compared fenoterol-ipratropium combination with terbutaline in chronic obstructive lung disease (ventilatory response, tolerance, side effects). |
| [7701449](https://pubmed.ncbi.nlm.nih.gov/7701449/) | 1995 | Cohort | Thorax | Studied effect of high-dose β2-agonist on mechanical loading and control of breathing in severe COPD. |
| [1974678](https://pubmed.ncbi.nlm.nih.gov/1974678/) | 1990 | Cohort | Lung | Two-month double-blind cross-over study: tulobuterol aerosol vs. fenoterol aerosol in chronic obstructive lung disease (36 patients). |

---

## Safety Considerations

No structured warnings or contraindications data is currently available (Data Gap DG001, flagged **Blocking** — TFDA/local label PDF has not yet been retrieved and parsed).

**Drug Interactions**: A DDI query (DDInter, 374 total interactions identified) returned one **Major** interaction and several Moderate/Minor ones among the sampled results:

| Interacting Drug | Level |
|---|---|
| Dolasetron | Major |
| Acarbose, Isometheptene, Famotidine, Epinephrine, Albiglutide, Alogliptin, Canagliflozin, Metformin, Chlorpropamide, Clarithromycin, Dapagliflozin, Diethylpropion, Dulaglutide | Moderate |
| Hydrocortisone, Triamcinolone, Dexamethasone, Beclomethasone dipropionate, Betamethasone, Budesonide | Minor |

Given 374 total interactions on file, this is only a partial sample — a full DDI screen against the patient's concomitant medications is required before any clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic rationale is strong (β2-agonist bronchodilator directly addressing obstructive airway pathophysiology) and is corroborated by one RCT studying orciprenaline/metaproterenol itself (PMID 8834341) plus a body of class-level evidence (L2). However, the drug is unmarketed in India (0 licenses) and formal label safety data (warnings/contraindications) is missing and flagged as a **Blocking** data gap — this must be resolved before any S1 safety assessment can proceed.

**To proceed, the following is needed:**
- Retrieve and parse TFDA/local label PDF for warnings, contraindications, and dosing (DG001, Blocking)
- Obtain formal DrugBank MOA record to replace the current Data Gap (DG002)
- Clarify whether any of the 5 retrieved trials actually dosed orciprenaline directly, versus comparator β2-agonists, to firm up the evidence grade
- Full DDI screen against target patient population's concomitant medications (374 total interactions on file, only 20 sampled here)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

