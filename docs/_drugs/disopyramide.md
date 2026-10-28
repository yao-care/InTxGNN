---
layout: default
title: Disopyramide
parent: Model Prediction Only (L5)
nav_order: 277
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Disopyramide: predicted new indication Tourette syndrome (evidence level L5). Approved use: Not stated in the India license data (the drug's known use is as an a…"
monitor_inn: "Disopyramide"
predicted_indications: ["Tourette syndrome", "attention deficit-hyperactivity disorder", "trichotillomania", "attention deficit hyperactivity disorder, inattentive type", "faciodigitogenital syndrome", "specific developmental disorder", "idiopathic neonatal atrial flutter", "chondromyxoid fibroma", "multifocal atrial tachycardia (disease)", "trigeminal nerve neoplasm"]
---

# Disopyramide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Disopyramide: From Cardiac Arrhythmia to Tourette Syndrome
{: .text-alpha }

## One-Sentence Summary

Disopyramide is a class Ia antiarrhythmic (sodium channel blocker with anticholinergic activity) marketed in India as Norpace New Capsule. The TxGNN model (deep learning) predicts it may be effective for **Tourette syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction. The score comes from the TxGNN model and may reflect similarities the model learned between related diseases, not biological evidence, and there is no pharmacological rationale behind it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license data (the drug's known use is as an antiarrhythmic) |
| Predicted New Indication | Tourette syndrome |
| TxGNN Prediction Score | 0.9986 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, disopyramide is a class Ia antiarrhythmic that blocks sodium channels and has anticholinergic activity. Its established role is in atrial and ventricular arrhythmias.

Tourette syndrome is mainly treated by modulating dopaminergic and alpha-2 adrenergic pathways, which are not primary targets of disopyramide. No clear mechanistic link was identified. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or a drug-specific pharmacological signal.

Other top-ranked predictions show the same pattern:
- **ADHD (including the inattentive subtype), trichotillomania, specific developmental disorder, faciodigitogenital syndrome:** no plausible mechanism, and no supporting evidence.
- **Chondromyxoid fibroma and trigeminal nerve neoplasm:** no antineoplastic activity is known.
- **Idiopathic neonatal atrial flutter:** mechanistically plausible, because disopyramide is used for atrial arrhythmias in adults. However, no neonatal data exist, and neonatal safety and dosing are unestablished.
- **Multifocal atrial tachycardia:** biologically plausible, but the only publication found concerns a different drug (see below).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for Tourette syndrome. The only publication in the top 10 predictions relates to multifocal atrial tachycardia (rank 9):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7418495](https://pubmed.ncbi.nlm.nih.gov/7418495/) | 1980 | Clinical study (case report) | Chest | A patient with resistant ventricular and supraventricular arrhythmias, including multifocal premature ventricular contractions, was treated with lorcainide. Quinidine, procainamide, disopyramide, propranolol and digoxin had failed to suppress the arrhythmias. This concerns a different drug, so it is only indirect evidence. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 151471 | Norpace New Capsule (RPG Life Sciences Ltd) | Strip of 10 capsules (oral) | Not stated in the license data |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

**Contraindication signals from the knowledge graph** (drug-disease links, not label text):
- **Cardiac:** long QT syndrome (including familial), atrioventricular block, atrial fibrillation, atrial flutter, cardiomyopathy (including hypertrophic), myocarditis, endomyocardial fibrosis, myocardial disorder, hypotensive disorder
- **Anticholinergic-related:** angle-closure glaucoma, benign prostatic hyperplasia, myasthenia gravis and related neuromuscular junction disease
- **Organ and metabolic:** kidney disease, liver disease, gallbladder disease, pyoureter, potassium deficiency, hypoglycemia

**Drug interactions:** 258 interactions were recorded. Main examples:
- **Major:** potassium citrate, clarithromycin, picosulfuric acid
- **Moderate:** famotidine, hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, amphotericin B, atropine, hyoscyamine, glycopyrronium, clidinium, loperamide, aprepitant, bisacodyl, chlorpropamide
- **Minor:** cimetidine

In ADHD and Tourette populations, which include many children and adolescents, the cardiovascular and anticholinergic adverse effects of disopyramide would be a particular concern.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Tourette syndrome prediction rests only on a TxGNN model (deep learning) score (L5), which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or literature, no plausible mechanism, and a cardiac and anticholinergic safety profile that is unfavorable for this population. The same applies to the other neurodevelopmental, oncologic and rare-disease predictions. Of the top 10 predictions, the arrhythmia-related ones (multifocal atrial tachycardia, idiopathic neonatal atrial flutter) are the most biologically plausible, but they also lack direct evidence.

**To proceed, the following is needed:**
- The approved indication text and package insert warnings and contraindications from the India license (this blocks safety screening)
- Detailed mechanism of action data
- Direct preclinical or clinical evidence for any predicted indication
- For arrhythmia-related predictions, specific evidence on disopyramide, including neonatal safety, dosing and pharmacokinetics for the neonatal atrial flutter prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

