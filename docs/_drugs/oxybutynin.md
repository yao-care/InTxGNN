---
layout: default
title: Oxybutynin
parent: Model Prediction Only (L5)
nav_order: 630
evidence_level: L5
indication_count: 3
---

# Oxybutynin
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

# Oxybutynin: From Overactive Bladder to Restless Legs Syndrome

## One-Sentence Summary

Oxybutynin is an antimuscarinic drug originally used to treat overactive bladder, neurogenic bladder and cauda equina syndrome.
The TxGNN model predicts it may be effective for **restless legs syndrome**, but **no clinical trials and no publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Overactive bladder, neurogenic bladder, cauda equina syndrome (from the knowledge graph; no approved indication text is available in the India licence records) |
| Predicted New Indication | Restless legs syndrome |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Oxybutynin is known to be a muscarinic antagonist with direct antispasmodic activity on smooth muscle, and its efficacy in overactive bladder is established.

The link to restless legs syndrome is weak. This condition is mainly tied to dopaminergic dysfunction and brain iron deficiency, and no direct mechanistic path to muscarinic blockade has been established. Anticholinergics with central activity may even worsen restless legs symptoms. The high TxGNN score therefore appears to reflect a pattern in the knowledge graph rather than a biologically supported rationale.

**Other predictions in the candidate list**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Gastroduodenitis | 99.62% | L5 | Antimuscarinic action could in theory reduce gastric secretion and motility, but anticholinergics are not standard therapy and no evidence was provided. |
| 3 | Peptic ulcer disease | 99.31% | L4 | Same rationale as historical anticholinergic ulcer therapy, which has been displaced by proton pump inhibitors and H2 blockers. Only old, low-tier publications exist. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top prediction (restless legs syndrome), currently no related literature is available.

For the third-ranked prediction (peptic ulcer disease), the following publications were found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14173506](https://pubmed.ncbi.nlm.nih.gov/14173506/) | 1964 | Uncontrolled clinical evaluation | Current Therapeutic Research | Historical clinical evaluation of oxybutynin chloride in gastrointestinal disease (no abstract available) |
| [4380481](https://pubmed.ncbi.nlm.nih.gov/4380481/) | 1965 | Pharmacology/Review | Arch Int Pharmacodyn Ther | Describes oxybutynin as a musculotropic antispasmodic with moderate anticholinergic action |
| [2360335](https://pubmed.ncbi.nlm.nih.gov/2360335/) | 1990 | Case report | DICP (Ann Pharmacother) | Reports oxybutynin-induced reflux esophagitis, probably from reduced lower esophageal sphincter tone, a safety signal against use in upper GI disease |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 215033 | Tropan 2.5 Tablet (Sun Pharmaceutical) | Strip of 10 tablets | Not specified in the records |
| 34837 | Cystran 5 Tablet (Intas) | Strip of 10 tablets | Not specified in the records |
| 34821 | Cystran 2.5 Tablet (Intas) | Strip of 10 tablets | Not specified in the records |
| 161779 | Oxyspas 2.5 Tablet (Cipla) | Strip of 10 tablets | Not specified in the records |
| 215266 | Tropan XL 5 Tablet (Sun Pharmaceutical) | Strip of 10 extended-release tablets | Not specified in the records |

Nine valid single-ingredient registrations exist in total, all oral. The remaining four are Nocturin 5 mg and 2.5 mg (Elder), Oxyspas 5 (Cipla) and Tropan 5 (Sun Pharmaceutical).

## Safety Considerations

- **Contraindications / conditions of concern (from knowledge-graph links, not label text)**:
  - Gastrointestinal: paralytic ileus, intestinal obstruction, toxic megacolon, ulcerative colitis and inflammatory bowel disease, gastroesophageal reflux disease, esophagitis, hiatus hernia
  - Urinary and prostate: bladder neck obstruction, benign prostatic hyperplasia
  - Eye and neuromuscular: angle-closure glaucoma, myasthenia gravis
  - Cardiovascular: hypertension, coronary artery disease, heart conduction disease, sudden cardiac arrest
  - Other: kidney disease, liver disease, hyperthyroidism
- **Drug Interactions**: 205 interactions were recorded. Those listed include:
  - **Major**: potassium chloride and potassium citrate
  - **Moderate**: other anticholinergic or antispasmodic agents (atropine, hyoscyamine, glycopyrronium, dicyclomine, trospium, propantheline, clidinium, mepenzolate, methscopolamine), opioids (morphine, opium, loperamide, eluxadoline), metoclopramide, aprepitant and pramlintide
- **Additional signals**: central anticholinergic activity may worsen restless legs symptoms, and a case report links oxybutynin to reflux esophagitis.

Package insert warnings were not available in the data compiled for this report; please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5). No trials or literature support it, the mechanism does not fit known restless legs pathophysiology, and anticholinergic activity may aggravate the condition. The gastrointestinal alternatives are likewise supported only by old, low-tier evidence and carry a reflux signal.

**To proceed, the following is needed:**
- Mechanism of action data and a credible mechanistic rationale linking muscarinic antagonism to restless legs syndrome
- Preclinical or clinical evidence, including a literature search focused on anticholinergics and restless legs symptoms
- Package insert warnings and contraindications from the India licence holders, and approved indication text for the registered products
- A safety assessment of the central anticholinergic effects and the numerous drug interactions in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

