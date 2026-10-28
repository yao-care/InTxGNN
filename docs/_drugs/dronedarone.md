---
layout: default
title: Dronedarone
parent: Model Prediction Only (L5)
nav_order: 292
evidence_level: L5
indication_count: 9
monitor_inn: "Dronedarone"
predicted_indications: ["stroke disorder", "ABri amyloidosis", "cerebrovascular disorder", "brain stem infarction", "sick sinus syndrome 2, autosomal dominant", "duodenal obstruction", "cerebral artery occlusion", "sarcoglycanopathy", "Wildervanck syndrome"]
last_modified_at: 2026-10-28
description: "Dronedarone: predicted new indication stroke disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Dronedarone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Dronedarone: multichannel-blocking antiarrhythmic → stroke disorder
{: .text-alpha }

## One-Sentence Summary

Dronedarone is a multichannel-blocking antiarrhythmic drug.
The TxGNN model predicts it may be relevant for **stroke disorder**, but the supporting material is indirect: **no registered clinical trials** and **20 publications** that mostly concern atrial fibrillation rather than stroke as a primary endpoint.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | stroke disorder |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Literature describes dronedarone as a multichannel-blocking antiarrhythmic, structurally related to amiodarone but without iodine. It inhibits sodium, potassium and calcium currents and has antiadrenergic effects.

Atrial fibrillation is a major cause of cardioembolic stroke. If dronedarone helps stroke outcomes, the most plausible route is indirect, through rhythm or rate control in patients with atrial fibrillation. Secondary analyses of the ATHENA trial suggested lower stroke rates in paroxysmal or persistent atrial fibrillation. One laboratory study also reported anticoagulant and antiplatelet effects independent of rhythm control.

These findings come from atrial fibrillation populations and post-hoc analyses, not from trials in which stroke itself was the studied disease. Accordingly, no cited study directly addresses stroke disorder as the target condition, and the evidence level is L5. The high score mainly reflects network proximity between atrial fibrillation and stroke, and it is not independent clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The publications below were compiled for this prediction. Most are reviews, guidelines or atrial fibrillation studies.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | RCT post-hoc analysis | Clin Res Cardiol | Long-term safety and efficacy of amiodarone and dronedarone for early rhythm control in EAST-AFNET 4 |
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | RCT (PALLAS) | N Engl J Med | Dronedarone in high-risk permanent atrial fibrillation; tested whether it reduces major vascular events |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | Post-hoc analysis | Eur J Heart Fail | ATHENA analysis of atrial fibrillation with preserved or mildly reduced ejection fraction heart failure |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort | Circ Arrhythm Electrophysiol | Dronedarone vs sotalol in antiarrhythmic-naive veterans with atrial fibrillation |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Experimental | Atherosclerosis | Anticoagulant and antiplatelet effects independent of antiarrhythmic action; ATHENA reported fewer strokes and transient ischemic attacks |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Retrospective cohort | J Atr Fibrillation | Real-world risk of cardiovascular events, stroke and heart failure vs amiodarone and other antiarrhythmics |
| [38782070](https://pubmed.ncbi.nlm.nih.gov/38782070/) | 2024 | Cohort | Int J Cardiol | Antiarrhythmic drugs and cardiovascular outcomes in atrial fibrillation with coronary artery disease |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review | Vasc Health Risk Manag | Approval and efficacy of dronedarone; post hoc ATHENA data suggest lower stroke risk, with safety concerns |
| [21370206](https://pubmed.ncbi.nlm.nih.gov/21370206/) | 2011 | Review | Swiss Med Wkly | Dronedarone for atrial fibrillation management |
| [22433576](https://pubmed.ncbi.nlm.nih.gov/22433576/) | 2012 | Guideline | Can J Cardiol | Canadian guideline update on stroke prevention and rate/rhythm control in atrial fibrillation |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 64181 | Dilsave 400mg Tablet | Strip of 10 tablets | Not recorded |

## Safety Considerations

- **Contraindication-related conditions:** Related records list long QT syndrome (including familial), torsades de pointes, liver failure, potassium deficiency, atrioventricular block and sick sinus syndrome (including familial). These are not label text.
- **Drug Interactions:** 253 interactions were recorded. Major-level examples include hydrocortisone, amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), loperamide, clarithromycin, picosulfuric acid, polyethylene glycol (3350 with electrolytes) and dolasetron. Moderate-level examples include famotidine, alvimopan, aprepitant, dexamethasone, bisacodyl, budesonide, cimetidine, saxagliptin and castor oil.
- **Other concerns from the literature:** Harm was seen in permanent atrial fibrillation and heart failure (PALLAS). Dronedarone also interacts with direct oral anticoagulants, which matters for stroke and bleeding risk.

Please also refer to the package insert, as warnings are not recorded in the local data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No registered trial and no cited study directly examines dronedarone in stroke disorder. The stroke-related signals come from post-hoc analyses in atrial fibrillation populations, and the safety signal in permanent atrial fibrillation and heart failure restricts extrapolation.

**To proceed, the following is needed:**
- A trial or well-designed study with stroke as the primary outcome
- Clear definition of the patient group (for example paroxysmal or persistent atrial fibrillation, excluding permanent atrial fibrillation and heart failure)
- Detailed mechanism of action data
- The package insert warnings and contraindications for the marketed product
- An assessment of interactions with anticoagulants
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

