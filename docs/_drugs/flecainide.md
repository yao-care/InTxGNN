---
layout: default
title: Flecainide
parent: Moderate Evidence (L3-L4)
nav_order: 356
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Flecainide: predicted new indication Stroke disorder (evidence level L3). Approved use: Atrial fibrillation"
---

# Flecainide
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

# Flecainide: From Atrial Fibrillation to Stroke Disorder

## One-Sentence Summary

Flecainide is a class 1C sodium channel blocker, originally used for rhythm control in atrial fibrillation.
The TxGNN model predicts it may be useful for **stroke disorder**, but the support is indirect: **1 Phase 3 clinical trial** (focused on arrhythmia after PFO closure rather than stroke itself) and **20 publications**, most of which address atrial fibrillation management rather than stroke prevention.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation (the licence records compiled for this report contain no approved indication text) |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, flecainide is a class 1C antiarrhythmic that blocks cardiac sodium channels, and it is used to maintain sinus rhythm in atrial fibrillation (AF).

AF is a major cause of cardioembolic stroke. By reducing AF burden, flecainide could in theory lower stroke risk indirectly. This is why a knowledge-graph model links the two conditions.

The link is only indirect, however. No data compiled for this report show that flecainide itself reduces stroke incidence. The only trial tests whether flecainide reduces atrial arrhythmia after patent foramen ovale (PFO) closure, which is an arrhythmia endpoint, not a stroke-recurrence endpoint. In addition, class 1C agents are generally not recommended in structural or ischaemic heart disease, which limits their use in many stroke patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05213104](https://clinicaltrials.gov/study/NCT05213104) | Phase 3 | Active, not recruiting | 186 | Flecainide to lower the risk of atrial arrhythmia after PFO closure (PFO closure is done for secondary stroke prevention). The primary endpoint is arrhythmia, so this is indirect evidence for stroke. Results are not yet available. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38702961](https://pubmed.ncbi.nlm.nih.gov/38702961/) | 2024 | RCT | Europace | EAST-AFNET 4 analysis of the safety and efficacy of long-term sodium channel blocker (flecainide/propafenone) early rhythm control; addresses proarrhythmia concerns |
| [25820938](https://pubmed.ncbi.nlm.nih.gov/25820938/) | 2015 | Meta-analysis | Cochrane Database Syst Rev | Antiarrhythmics for maintaining sinus rhythm after AF cardioversion; effect on mortality and other clinical outcomes |
| [30067936](https://pubmed.ncbi.nlm.nih.gov/30067936/) | 2018 | Guideline | Med J Aust | Australian clinical guidelines for AF diagnosis and management |
| [41152878](https://pubmed.ncbi.nlm.nih.gov/41152878/) | 2025 | Cohort | BMC Med | Concomitant use of DOACs and interacting antiarrhythmics and risk of stroke and bleeding in non-valvular AF |
| [41954064](https://pubmed.ncbi.nlm.nih.gov/41954064/) | 2026 | Cohort | J Am Heart Assoc | Long-term outcomes with class 1C antiarrhythmics in AF; cardiovascular benefit over rate control remains unclear |
| [25430048](https://pubmed.ncbi.nlm.nih.gov/25430048/) | 2014 | Review | BMJ Clin Evid | Acute-onset AF increases the risk of stroke and heart failure |
| [19265095](https://pubmed.ncbi.nlm.nih.gov/19265095/) | 2009 | Review | Chest | Acute AF management; thromboembolism is a key clinical sequela |
| [27884575](https://pubmed.ncbi.nlm.nih.gov/27884575/) | 2017 | Case report | J Emerg Med | Flecainide overdose unmasking a Brugada pattern on ECG |
| [8729366](https://pubmed.ncbi.nlm.nih.gov/8729366/) | 1995 | Study | Arch Mal Coeur Vaiss | Atrial electrophysiological study of 38 patients with unexplained ischaemic cerebrovascular events, including the effect of intravenous flecainide on atrial arrhythmia induction |
| [37109225](https://pubmed.ncbi.nlm.nih.gov/37109225/) | 2023 | RCT (pilot) | J Clin Med | Carvedilol vs flecainide for idiopathic PVCs from the ventricular outflow tract |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 84570 | Flecarite 100 Tablet (Torrent Pharmaceuticals Ltd) | Strip of 10 tablets | Not stated in the data compiled |
| Registration No. 84282 | Flecarite 50 Tablet (Torrent Pharmaceuticals Ltd) | Strip of 10 tablets | Not stated in the data compiled |

---

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text)**: kidney disease, liver disease, gallbladder disease, potassium deficiency disease, myocardial infarction and coronary thrombosis, haemoglobinopathy, atrioventricular block, sick sinus syndrome (including the familial form), and pyoureter.
- **Drug Interactions**: 215 interactions are recorded. Major-level interactions include **dolasetron** and **eliglustat**. Moderate-level interactions include famotidine, cimetidine, loperamide, bupropion, lorcaserin, clarithromycin, levofloxacin, palonosetron, trospium, and several laxatives and bowel-preparation agents (bisacodyl, picosulfuric acid, lactulose, lactitol, sodium sulfate, polyethylene glycol). Minor-level interactions include ascorbic acid, potassium citrate, and metronidazole. Interactions with direct oral anticoagulants are also relevant in stroke patients (see PMID 41152878).
- **Other**: Case reports describe a Brugada pattern unmasked by flecainide overdose. Several of the associated conditions (ischaemic heart disease, conduction disease) are common in stroke populations, which narrows the eligible patient group.

Please also refer to the package insert, as label warnings were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The stroke prediction rests on an indirect pathway through AF rhythm control. The single Phase 3 trial measures post-PFO-closure arrhythmia, not stroke, and no data show a direct reduction in stroke by flecainide. Contraindications in ischaemic and structural heart disease further limit applicability. The other predicted indications (for example, the obsolete ischaemic stroke susceptibility entry and "cerebrovascular disorder", which largely duplicates the stroke entry) add no independent support.

**To proceed, the following is needed:**
- Results from NCT05213104, and ideally a trial with stroke or thromboembolic recurrence as the endpoint
- Package insert warnings and contraindications for the Indian products (Flecarite 50 and 100), as these are currently missing
- Mechanism of action data
- Analysis of how flecainide's safety profile fits the stroke population, including ischaemic heart disease and anticoagulant co-prescription
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

