---
layout: default
title: Tegaserod
parent: Moderate Evidence (L3-L4)
nav_order: 803
evidence_level: L4
indication_count: 2
---

# Tegaserod
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Tegaserod: From Irritable Bowel Syndrome with Constipation to Migraine Disorder

## One-Sentence Summary

> Tegaserod is a 5-HT4 receptor partial agonist historically used for irritable bowel syndrome with constipation (IBS-C).
> The TxGNN model predicts it may be effective for **Migraine Disorder**,
> but this direction is currently supported by only **1 review-type publication** and **no registered clinical trials**, indicating an early-stage, low-confidence signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Irritable Bowel Syndrome with Constipation (IBS-C) — general knowledge; no Taiwan-specific approved indication text available (drug not marketed in Taiwan) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L4 |
| Taiwan Market Status | Not marketed (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002, pending DrugBank API lookup). Based on known information, Tegaserod is a 5-HT4 receptor partial agonist, primarily developed for gastrointestinal motility disorders (IBS-C). Its serotonergic activity provides a theoretical, mechanism-based rationale for exploring effects outside the GI tract, including the central nervous system.

However, the mechanistic link to migraine is indirect and weak. The established pharmacological targets for migraine treatment — the triptan class — act on 5-HT1B/1D/1F receptors, not 5-HT4. Tegaserod's 5-HT4 partial agonism does not map cleanly onto this pathway, so the predicted association should be treated as a hypothesis-generating signal rather than a validated mechanistic finding. This is compounded by tegaserod's known history of cardiovascular safety concerns, which led to its withdrawal from several markets in the past — a factor that must be weighed heavily in any repurposing evaluation, independent of the migraine signal itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19220673](https://pubmed.ncbi.nlm.nih.gov/19220673/) | 2009 | Review (Tier 3) | Journal of Gastroenterology and Hepatology | Reviews effectiveness of prokinetic agents (including tegaserod class) for conditions outside the GI tract — CNS, respiratory, urologic, metabolic. Does not specifically evaluate migraine efficacy; relevance is general/indirect. |

---

## Taiwan Market Information

Tegaserod is currently **not marketed in Taiwan** (0 registered licenses). No product authorization or approved-indication records are available in this evidence pack.

---

## Safety Considerations

- **Drug Interactions**: DrugBank/DDInter data shows **238 total recorded interactions**. Of the entries reviewed, most are graded "Unknown" severity in the source database; two have defined severity levels:
  - Ethinylestradiol — Minor
  - Digoxin — Minor
  - The remaining reviewed interactions (e.g., Cyclosporine, Fluconazole, Erythromycin, Azithromycin, Pravastatin, Tramadol, Lorazepam, Pantoprazole, Ramipril, Valsartan, Torasemide, and others) are currently ungraded in the source and require individual clinical assessment.
- **Known Historical Signal**: Tegaserod carries a documented history of cardiovascular safety concerns that previously led to market withdrawal in some jurisdictions; this should be treated as an active safety consideration independent of the migraine repurposing signal.
- **Outstanding Gap (Blocking)**: TFDA label warnings and contraindications are not yet available (DG001, severity: Blocking). This prevents the candidate from entering S1 safety pre-assessment and must be resolved before any further evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to a single Tier-3 review article with no direct migraine-specific data and no registered clinical trials (Evidence Level L4). The mechanistic rationale is indirect (5-HT4 vs. the migraine-relevant 5-HT1B/1D/1F pathway), and tegaserod's known cardiovascular safety history adds material risk. Combined with a **Blocking** data gap on TFDA label warnings/contraindications, this candidate cannot yet proceed to safety pre-assessment.

**To proceed, the following is needed:**
- TFDA label warnings and contraindications (DG001 — blocking, required for S1 safety review)
- Detailed mechanism of action data from DrugBank (DG002)
- Mechanistic/preclinical studies directly linking 5-HT4 modulation to migraine pathophysiology
- Ongoing monitoring for new trial registrations targeting migraine or related CNS indications

*Note: A second, weaker signal — Migraine with Brainstem Aura (TxGNN score 99.29%, Evidence Level L5) — was also flagged, but has no supporting clinical trials or literature. It should be monitored only, not actively pursued at this stage.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

