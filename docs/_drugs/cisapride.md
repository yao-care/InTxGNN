---
layout: default
title: Cisapride
parent: Model Prediction Only (L5)
nav_order: 185
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Cisapride: predicted new indication Peptic ulcer perforation (evidence level L5). Approved use: Gastroesophageal reflux disease"
monitor_inn: "Cisapride"
predicted_indications: ["peptic ulcer perforation", "gastrojejunal ulcer", "gastric ulcer (disease)", "gastroduodenitis"]
---

# Cisapride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Cisapride: From Gastroesophageal Reflux Disease to Peptic Ulcer Perforation
{: .text-alpha }

## One-Sentence Summary

Cisapride is a prokinetic drug originally used to treat gastroesophageal reflux disease and reflux esophagitis.
The TxGNN model predicts it may be effective for **peptic ulcer perforation**, but this prediction is supported by **no clinical trials** and only **1 publication** (a review that does not address perforation).
The evidence is essentially model-based, and the biological rationale is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastroesophageal reflux disease; esophagitis; peptic esophagitis (the India licence records contain no indication text) |
| Predicted New Indication | Peptic ulcer perforation |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. From the literature, cisapride is a 5-HT4 agonist prokinetic that enhances acetylcholine release from the enteric nervous system (myenteric plexus). This improves oesophageal, gastric and intestinal motility and explains its benefit in reflux disease.

The link to the predicted indication is weak. Peptic ulcer perforation is an acute surgical complication, and cisapride has no known action in preventing or treating it. A prokinetic could even be a theoretical concern when a hollow organ is perforated. The very high TxGNN score appears to reflect network proximity to other upper GI disorders rather than a biological rationale.

Other predicted indications are more plausible, though still indirect:
- **Gastroduodenitis** is the most biologically coherent. Physiological studies show cisapride improves antroduodenal coordination and reduces biliary reflux, but there are no trials with endoscopic or histological endpoints.
- **Gastric ulcer, gastrojejunal ulcer and peptic ulcer disease** are unlikely to respond. Cisapride does not suppress acid, eradicate *H. pylori* or protect the mucosa. Evidence is limited to a rat study and small human studies, such as a double-blind duodenal ulcer relapse study (66 patients) and a gastric ulcer trial (60 patients) against ranitidine.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18097282](https://pubmed.ncbi.nlm.nih.gov/18097282/) | 2008 | Review | J Clin Gastroenterol | Gastric and enteric involvement in systemic sclerosis (delayed gastric emptying); does not address ulcer perforation |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 178527 | Prepulsid 10mg Tablet (Johnson & Johnson Ltd) | Strip of 10 tablets | Not stated |
| 181058 | Peristil 5mg Tablet (Dr Reddy's Laboratories Ltd) | Strip of 10 tablets | Not stated |
| 180786 | Peristil 1mg Suspension (Dr Reddy's Laboratories Ltd) | Bottle of 60 ml suspension | Not stated |
| 74561 | Esorid 10mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not stated |
| 94815 | Gastro 10mg Tablet (Cipla Ltd) | Strip of 10 tablets | Not stated |

Twenty single-ingredient licences are currently valid; the five above are a selection. Some are combination-labelled products (e.g. "MPS" tablets at 10 mg/125 mg), though all are recorded as single-ingredient.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: long QT syndrome (including familial), epilepsy, kidney disease, liver disease, gallbladder disease, active peptic ulcer disease, myocardial ischemia, coronary artery disease, respiratory failure, pulmonary valve insufficiency, and electrolyte or metabolic disorders (potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, hypophosphatemia, pyoureter).
- **Drug Interactions**: 302 interactions are recorded. Major ones include amiodarone, amisulpride, amitriptyline, anagrelide, abiraterone, apalutamide, tramadol, acetazolamide, hydrochlorothiazide, nifedipine, adenosine and alfuzosin. Moderate ones include famotidine, formoterol, salbutamol, hyoscyamine, loperamide and propofol. Ranitidine is minor.
- **Cardiac risk**: the literature points to QT prolongation and arrhythmia risk, which has led to market restrictions in many countries. CYP3A4 inhibitors such as clarithromycin are a particular concern in ulcer regimens.
- **Active peptic ulcer disease** appears among the knowledge-graph contraindications, which runs directly against the predicted ulcer-related indications.

Package insert warnings and contraindications could not be obtained for this report, so please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no direct literature, and cisapride has no plausible mechanism in ulcer perforation. Its QT-prolongation risk, extensive interactions, and a graph-based contraindication in active peptic ulcer disease weigh heavily against repurposing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- If pursuing this line at all, redirect to gastroduodenitis or duodenogastric reflux as a research question, with controlled trials using endoscopic or histological endpoints
- A cardiac safety and interaction management plan (ECG/QT monitoring, exclusion of CYP3A4 inhibitors and other QT-prolonging drugs)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

