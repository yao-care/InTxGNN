---
layout: default
title: Dronedarone
parent: Moderate Evidence (L3-L4)
nav_order: 292
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Dronedarone: predicted new indication Stroke disorder (evidence level L3). Approved use: Atrial fibrillation"
---

# Dronedarone
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Dronedarone: From Atrial Fibrillation to Stroke Disorder

## One-Sentence Summary

Dronedarone is a multichannel-blocking antiarrhythmic drug, originally used to treat atrial fibrillation.
The TxGNN model predicts it may be effective for **stroke disorder**, but there are **no registered clinical trials** and the **20 publications** compiled for this report are mostly reviews, guidelines and post-hoc analyses in atrial fibrillation (AF) populations, not stroke-specific trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation (the India license text contains no approved indication wording, so this comes from the knowledge graph) |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L3 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dronedarone is a multichannel-blocking antiarrhythmic (it inhibits sodium, potassium and calcium currents, and has antiadrenergic effects), its use in atrial fibrillation is established, and mechanistically it may be applicable to stroke through indirect routes.

AF is a major cause of cardioembolic stroke. Any stroke benefit would most plausibly come indirectly, through rhythm or rate control. Post-hoc analyses of the ATHENA trial and a related meta-analysis reported fewer strokes in patients with paroxysmal or persistent AF taking dronedarone. One laboratory study also suggested direct anticoagulant and antiplatelet effects, and a preclinical review described protective effects on ischemia/reperfusion injury in heart and brain.

The high TxGNN score mainly reflects how closely AF and stroke are linked in the knowledge graph. It is not independent clinical evidence. Safety findings from the PALLAS trial (high-risk permanent AF) and heart failure reviews also limit how far these findings can be extended.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The table lists the most relevant publications. Evidence for stroke is mostly secondary or indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | RCT (PALLAS) | N Engl J Med | Dronedarone tested in high-risk permanent AF, where major vascular events were the focus; safety concerns arose in this population |
| [22149318](https://pubmed.ncbi.nlm.nih.gov/22149318/) | 2011 | Meta-analysis / post-hoc | Am J Cardiovasc Drugs | Pooled randomized-trial data suggested a reduced stroke risk in paroxysmal or persistent AF |
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | RCT post-hoc analysis | Clin Res Cardiol | Long-term safety and efficacy of amiodarone and dronedarone for early rhythm control in EAST-AFNET 4 |
| [25820938](https://pubmed.ncbi.nlm.nih.gov/25820938/) | 2015 | Systematic review | Cochrane Database Syst Rev | Antiarrhythmics for maintaining sinus rhythm after cardioversion of AF |
| [20396635](https://pubmed.ncbi.nlm.nih.gov/20396635/) | 2010 | Review | Clin Interv Aging | Impact of dronedarone on stroke reduction in AF and flutter |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Mechanistic study | Atherosclerosis | Dronedarone showed anticoagulant and antiplatelet effects independent of its antiarrhythmic action |
| [22366819](https://pubmed.ncbi.nlm.nih.gov/22366819/) | 2012 | Preclinical review | Cardiovasc Drugs Ther | Pleiotropic effects on ischemia/reperfusion injury in heart and brain |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort | Circ Arrhythm Electrophysiol | Dronedarone vs sotalol in antiarrhythmic-drug-naive veterans with AF |
| [41152878](https://pubmed.ncbi.nlm.nih.gov/41152878/) | 2025 | Cohort | BMC Med | Concomitant use of direct oral anticoagulants and interacting antiarrhythmics and the risk of stroke and bleeding in non-valvular AF |
| [22433576](https://pubmed.ncbi.nlm.nih.gov/22433576/) | 2012 | Guideline | Can J Cardiol | Canadian guideline update on stroke prevention and rate/rhythm control in AF |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 64181 | Dilsave 400mg Tablet (Emcure Pharmaceuticals Ltd) | Strip of 10 tablets (oral) | Not specified in the compiled data |

## Cytotoxicity

Not applicable: dronedarone is an antiarrhythmic, not an antineoplastic drug, so this section is omitted.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are graph relationships, not package insert text): long QT syndrome (including the familial form), torsades de pointes, liver failure, potassium deficiency, atrioventricular block, and sick sinus syndrome (including the familial form).
- **Drug Interactions**: 253 interactions were identified. Major-level examples include hydrocortisone, clarithromycin, loperamide, dolasetron, the amphotericin B formulations, picosulfuric acid and polyethylene glycol (3350 with electrolytes). Moderate-level examples include famotidine, cimetidine, aprepitant, dexamethasone, budesonide, saxagliptin, alvimopan, bisacodyl and castor oil.
- **Anticoagulants**: the literature indicates dronedarone can raise levels of direct oral anticoagulants (through P-gp inhibition). This matters for both stroke and bleeding risk.
- **Patient selection**: harm was seen in permanent AF and in heart failure (PALLAS and heart failure reviews).

Please refer to the package insert for the remaining safety information, since the label warnings were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L3 (reviews, guidelines and post-hoc analyses in AF populations). There are no registered trials, and no trial has stroke prevention in a non-AF population as its primary endpoint. Safety signals in permanent AF and heart failure also limit extrapolation. The other nine predictions have no trial or literature support. Most are L5 model predictions only, and several are obsolete, implausible or safety concerns (for example, sick sinus syndrome).

**To proceed, the following is needed:**
- The India package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A prespecified stroke-outcome analysis in AF populations, or a prospective study with stroke as a primary endpoint
- Clear patient selection criteria that exclude permanent AF, heart failure and conduction disorders
- A plan for managing interactions with anticoagulants and other QT-prolonging drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

