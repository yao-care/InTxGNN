---
layout: default
title: Terbutaline
parent: Model Prediction Only (L5)
nav_order: 814
evidence_level: L5
indication_count: 3
---

# Terbutaline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

Using no specialized skill here — this is a direct content-generation task fully specified by the user's report prompt; I'll follow it exactly against the supplied Evidence Pack.

# Terbutaline: From No Registered Indication (Not Marketed Locally) to Obstructive Lung Disease

## One-Sentence Summary

> Terbutaline (DrugBank DB00871) currently holds **zero product registrations** in this jurisdiction, and no original-indication text is on file in this evidence pack.
> The TxGNN model's top prediction is **Obstructive Lung Disease**, backed by **48 clinical trials** and **20 publications** —
> but nearly all of this evidence reflects Terbutaline's long-established role as a β2-agonist bronchodilator in asthma/COPD, rather than a genuinely novel indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — no local product license exists to extract indication text from (market status: not marketed) |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Local Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A formal, structured mechanism-of-action record for Terbutaline is not available in this evidence pack (data gap DG002). However, the clinical trial evidence within the pack itself is unambiguous: across dozens of studies, Terbutaline (marketed internationally as Bricanyl® Turbuhaler) is consistently used as a short-acting β2-adrenergic receptor agonist bronchodilator, deployed as rescue/reliever therapy alongside inhaled corticosteroids (budesonide, beclomethasone) and other bronchodilators (salbutamol, ipratropium) in the management of asthma and COPD.

The predicted new indication, "Obstructive Lung Disease," is the umbrella pathophysiological category that already encompasses asthma and COPD — the exact conditions Terbutaline has been studied in for over four decades. Mechanistically, β2-agonism relaxes airway smooth muscle and relieves bronchoconstriction, which is precisely the pathology underlying obstructive lung disease. This tight mechanistic fit is almost certainly why TxGNN assigns this prediction its very high score.

Because of this overlap, this candidate should be read not as a novel repurposing hypothesis but as the model correctly recovering a **well-established indication**. Its practical value for a repurposing pipeline is therefore limited to the question of local registration/import feasibility (the drug has 0 current licenses here), rather than discovery of new pharmacological activity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01096017](https://clinicaltrials.gov/study/NCT01096017) | Phase 3 | Completed | 24 | Terbutaline Turbuhaler 0.4mg vs. Salbutamol pMDI 200μg, crossover, Japanese adult asthma patients |
| [NCT02322788](https://clinicaltrials.gov/study/NCT02322788) | Phase 3 | Completed | 95 | Bricanyl Turbuhaler M3 vs. M2 — protective effect on methacholine-induced bronchoconstriction, mild-moderate asthma |
| [NCT00849095](https://clinicaltrials.gov/study/NCT00849095) | Phase 3 | Completed | 860 | As-needed budesonide/formoterol vs. regular budesonide/formoterol + as-needed terbutaline, mild-moderate persistent asthma |
| [NCT00839800](https://clinicaltrials.gov/study/NCT00839800) | Phase 3 | Completed | 2,091 | Symbicort SMART vs. Symbicort + as-needed terbutaline, 12-month multinational asthma trial |
| [NCT02149199](https://clinicaltrials.gov/study/NCT02149199) | Phase 3 | Completed | 3,850 | Symbicort as-needed vs. terbutaline as-needed vs. Pulmicort BID + terbutaline as-needed, adult/adolescent asthma |
| [NCT02224157](https://clinicaltrials.gov/study/NCT02224157) | Phase 3 | Completed | 4,215 | Symbicort as-needed vs. Pulmicort BID + terbutaline as-needed, adult/adolescent asthma |
| [NCT00242775](https://clinicaltrials.gov/study/NCT00242775) | Phase 3 | Completed | 2,100 | Symbicort vs. Seretide + terbutaline as-needed (AHEAD trial), persistent asthma |
| [NCT01944033](https://clinicaltrials.gov/study/NCT01944033) | Phase 3 | Completed | 250 | β2-agonist alone vs. β2-agonist + ipratropium bromide in acute COPD exacerbation |
| [NCT06626620](https://clinicaltrials.gov/study/NCT06626620) | Phase 3 | Completed | 120 | IV magnesium sulfate vs. terbutaline for pediatric acute asthma exacerbation |
| [NCT00750568](https://clinicaltrials.gov/study/NCT00750568) | N/A | Unknown | 36 | PK/PD of continuous IV terbutaline infusion in pediatric severe status asthmaticus |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30156361](https://pubmed.ncbi.nlm.nih.gov/30156361/) | 2019 | RCT | Acad Emerg Med | Nebulized terbutaline + ipratropium vs. terbutaline alone in AECOPD requiring non-invasive ventilation |
| [1615190](https://pubmed.ncbi.nlm.nih.gov/1615190/) | 1992 | RCT | Respiratory Medicine | Placebo-controlled crossover: inhaled terbutaline improves FEV1, FVC, dyspnoea, walking distance in COPD |
| [3073804](https://pubmed.ncbi.nlm.nih.gov/3073804/) | 1988 | RCT | Br J Dis Chest | Double-blind crossover: oral terbutaline increases diaphragmatic contraction force in COPD |
| [3044105](https://pubmed.ncbi.nlm.nih.gov/3044105/) | 1988 | RCT | Am J Med Sci | Placebo-controlled crossover: oral terbutaline augments cardiac performance in COPD |
| [10384064](https://pubmed.ncbi.nlm.nih.gov/10384064/) | 1999 | RCT | Lung | Double-blind, placebo-controlled crossover: terbutaline effects on exercise capacity and lung function in COPD |
| [2031046](https://pubmed.ncbi.nlm.nih.gov/2031046/) | 1991 | RCT | Pneumologie | Randomized crossover: nebulized terbutaline + positive expiratory pressure in COPD |
| [2951811](https://pubmed.ncbi.nlm.nih.gov/2951811/) | 1986 | RCT | Respiration | Randomized single-blind: fenoterol-ipratropium combo vs. terbutaline in COLD |
| [6988343](https://pubmed.ncbi.nlm.nih.gov/6988343/) | 1980 | RCT | Int J Clin Pharmacol Ther Toxicol | Double-blind: clenbuterol vs. terbutaline bronchodilator effects in COLD |
| [6107217](https://pubmed.ncbi.nlm.nih.gov/6107217/) | 1980 | RCT | Chest | Double-blind crossover: beta-blocker interaction with terbutaline in COLD patients |
| [33065789](https://pubmed.ncbi.nlm.nih.gov/33065789/) | 2020 | Clinical Study | Ann Palliat Med | N-acetylcysteine + terbutaline sulfate in elderly COPD — apoptosis/anti-apoptosis mechanism |

---

## Safety Considerations

- **Drug Interactions**: DDI screening identified **406 total interactions**. Representative *Moderate*-level interactions include: Acarbose, Isometheptene, Famotidine, Epinephrine, Albiglutide, Alogliptin, Pioglitazone, Loperamide, Bisacodyl, Canagliflozin, Chlorpropamide, Clarithromycin, Picosulfuric acid, and Polyethylene glycol (3350 w/ electrolytes). Representative *Minor*-level interactions include corticosteroids commonly co-prescribed in obstructive lung disease regimens: Hydrocortisone, Triamcinolone, Dexamethasone, Beclomethasone dipropionate, Betamethasone, and Budesonide.

Formal local product-label warnings and contraindications are not yet available in this evidence pack (see DG001 below).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking-severity data gap (DG001 — local product label warnings/contraindications) explicitly prevents this candidate from entering the S1 safety pre-screen stage, and Terbutaline holds zero current registrations locally. Additionally, the top predicted indication (Obstructive Lung Disease) substantially overlaps with Terbutaline's decades-established use as a bronchodilator in asthma/COPD, so the strategic value here is primarily about registration/import feasibility rather than discovering a genuinely new therapeutic application.

**To proceed, the following is needed:**
- Local product label (key warnings, contraindications) — DG001, Blocking
- Formal DrugBank/mechanism-of-action record — DG002, High
- Assessment of registration/import pathway given 0 current licenses
- Clarification of why "obstructive lung disease" surfaces as a *new* candidate despite Terbutaline's extensive existing use in this exact disease category (possible knowledge-graph mapping artifact worth a methodology review)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

