---
layout: default
title: Amiodarone
parent: Model Prediction Only (L5)
nav_order: 52
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-03
monitor_inn: "Amiodarone"
predicted_indications: ["catecholaminergic polymorphic ventricular tachycardia", "incessant infant ventricular tachycardia", "obsolete bundle branch block", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "heparin cofactor 2 deficiency", "trichotillomania", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "gout"]
description: "Amiodarone: predicted new indication Catecholaminergic polymorphic ventricular tachycardia (evidence level L5). Approved use: Not recorded in the local data"
---

# Amiodarone
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

## Amiodarone: Catecholaminergic polymorphic ventricular tachycardia
{: .text-alpha }

## One-Sentence Summary

Amiodarone is a class III antiarrhythmic drug marketed in India in oral and injectable forms.
The TxGNN model predicts it may be effective for **catecholaminergic polymorphic ventricular tachycardia** (prediction score 0.9978), but there are **no registered clinical trials** and only **9 publications**, mostly case reports, a cohort study and general reviews, behind this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Catecholaminergic polymorphic ventricular tachycardia |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, amiodarone blocks several ion channels (potassium, sodium and calcium) and has beta-adrenergic antagonist activity. In theory this could dampen ventricular arrhythmias triggered by adrenergic stress.

Catecholaminergic polymorphic ventricular tachycardia (CPVT) is a rare inherited arrhythmia syndrome. It is triggered by exercise or emotional stress and is driven by abnormal calcium release inside heart muscle cells (RYR2 or CASQ2 gene variants). The published literature points to beta-blockers and flecainide as the effective drugs. Amiodarone is not an established therapy for CPVT, so the mechanistic link is plausible but weak, and the high model score is not backed by direct clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the retrieved publications is a controlled study of amiodarone in CPVT. They describe the disease or its management in general.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Systematic review | Life (Basel) | Clinical features, genetics and arrhythmic outcomes of CPVT patients from China |
| [39076628](https://pubmed.ncbi.nlm.nih.gov/39076628/) | 2022 | Cohort | Reviews in Cardiovascular Medicine | Clinical characteristics, genetics, healthcare use and costs of CPVT patients in a Chinese city |
| [26513538](https://pubmed.ncbi.nlm.nih.gov/26513538/) | 2015 | Review | Expert Opinion on Pharmacotherapy | Overview of drug treatment of ventricular arrhythmias |
| [22553997](https://pubmed.ncbi.nlm.nih.gov/22553997/) | 2012 | Case report | PACE | Flecainide suppressed defibrillator-induced storming in a boy with CPVT |
| [39735866](https://pubmed.ncbi.nlm.nih.gov/39735866/) | 2024 | Case report | Frontiers in Cardiovascular Medicine | Right cardiac sympathetic denervation after left denervation in a teenager with CPVT |
| [30116135](https://pubmed.ncbi.nlm.nih.gov/30116135/) | 2018 | Case report | Turk Pediatri Arsivi | Sudden cardiac arrest caused by CPVT in a 2-year-old |
| [29668588](https://pubmed.ncbi.nlm.nih.gov/29668588/) | 2018 | Case report | Medicine | Six-year delayed CPVT diagnosis (RYR2 variant) in a child |
| [37852665](https://pubmed.ncbi.nlm.nih.gov/37852665/) | 2023 | Case report | BMJ Case Reports | Young child with cardiac arrest and recurrent ventricular arrhythmia; diagnostic dilemma |

## India Market Information

At least 20 valid licences are recorded; this list may be partial. Main authorisations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 34082 | Cordarone Tablet (Sanofi India Ltd) | Strip of 15 tablets | Not listed |
| 34160 | Cordarone Injection 3ml (Sanofi India Ltd) | Vial of 3 ml injection | Not listed |
| 4090 | Amipace 200 Tablet (Lupin Ltd) | Strip of 10 tablets | Not listed |
| 76178 | Eurythmic 200mg Tablet (Troikaa Pharmaceuticals Ltd) | Strip of 10 tablets | Not listed |
| 82476 | Eurythmic 150mg Injection (Troikaa Pharmaceuticals Ltd) | Prefilled syringe of 3 ml | Not listed |

## Safety Considerations

- **Drugs with major interactions** (355 interactions recorded in total): agalsidase beta, hydrocortisone, dexamethasone, amphotericin B (including its lipid, cholesteryl sulfate and liposomal forms), cisapride, clarithromycin, clotrimazole, dolasetron and eliglustat. Moderate interactions include famotidine, cimetidine, aprepitant, bisacodyl, budesonide and castor oil.
- **Conditions of concern** (recorded as contraindication relations, not label text): long QT syndrome, torsades de pointes, sick sinus syndrome, atrioventricular block, thyroid disease (hypothyroidism and hyperthyroidism), liver disease and drug-induced liver injury, interstitial lung disease and hypersensitivity pneumonitis, optic neuritis and optic nerve disease, peripheral neuropathy, and potassium deficiency.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trials exist and no study directly tests amiodarone in CPVT, so the evidence level is L5. Beta-blockers and flecainide are the established agents, and amiodarone carries considerable safety concerns, including rhythm, thyroid, liver and lung effects.

**To proceed, the following is needed:**
- Mechanism of action data and the local package insert warnings and contraindications
- Preclinical or clinical data comparing amiodarone with beta-blockers and flecainide in CPVT
- A safety assessment for young patients, who make up most CPVT cases, covering thyroid, liver, lung and proarrhythmia risks

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

