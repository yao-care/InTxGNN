---
layout: default
title: Verapamil
parent: Model Prediction Only (L5)
nav_order: 886
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Verapamil: predicted new indication Obsolete bundle branch block (evidence level L5). Approved use: Hypertension, atrial fibrillation, acute coronary syndrome…"
monitor_inn: "Verapamil"
predicted_indications: ["obsolete bundle branch block", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "periodic paralysis with transient compartment-like syndrome"]
---

# Verapamil
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Verapamil: From Hypertension and Arrhythmia to Obsolete Bundle Branch Block

## One-Sentence Summary

Verapamil is a calcium channel blocker, originally used for hypertension, atrial fibrillation, acute coronary syndrome, Prinzmetal angina and ventricular tachycardia.
The TxGNN model's top-ranked prediction is **obsolete bundle branch block**, but there are **0 clinical trials** and **0 publications** supporting it. The prediction rests on the model alone and is probably a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, atrial fibrillation, acute coronary syndrome, Prinzmetal angina, ventricular tachycardia (from the knowledge graph; no approved-indication text is available in the India licence records) |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 17 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Verapamil is a well-known L-type calcium channel blocker. It slows conduction through the atrioventricular (AV) node and relaxes vascular smooth muscle, which explains its use in hypertension, angina and supraventricular arrhythmias.

For the top prediction, this mechanism does **not** offer a therapeutic rationale. Slowing AV conduction is not a treatment for bundle branch block and may worsen conduction disease. The disease term is also marked as obsolete, which points to an artifact of the knowledge graph rather than a real clinical signal.

Other predictions are somewhat more plausible mechanistically but equally unsupported by direct evidence:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Malignant renovascular hypertension | 99.27% | L5 | Class-level link through blood pressure lowering; the two retrieved papers do not test verapamil |
| 3 | Malignant hypertensive renal disease | 99.27% | L5 | Plausible blood pressure effect; no specific data |
| 4 | Pulmonary hypertension owing to lung disease and/or hypoxia | 99.26% | L4 | Only indirect preclinical data; calcium channel blockers may impair hypoxic pulmonary vasoconstriction and gas exchange |
| 5 | Pulmonary hypertension with unclear multifactorial mechanism | 99.26% | L5 | Calcium channel blockers are used only in the small vasoreactive subset, and verapamil is generally avoided because of negative inotropy |
| 6 | Braddock syndrome | 99.15% | L5 | No identifiable mechanistic rationale |
| 7 | Periodic paralysis with transient compartment-like syndrome | 99.08% | L5 | Speculative channelopathy link only |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction (obsolete bundle branch block), currently no related literature is available.

For the second-ranked prediction (malignant renovascular hypertension), two papers were retrieved. Neither tests verapamil in this condition.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22147655](https://pubmed.ncbi.nlm.nih.gov/22147655/) | 2012 | Review | Hormone and Metabolic Research | Factors affecting the aldosterone/renin ratio; malignant or renovascular hypertension and some antihypertensives can cause false-negative screening for primary aldosteronism |
| [10224210](https://pubmed.ncbi.nlm.nih.gov/10224210/) | 1999 | Case report | Pediatrics | Solitary renal myofibromatosis described as a previously unreported cause of renovascular hypertension in infants |

For the fourth-ranked prediction (pulmonary hypertension due to lung disease/hypoxia), the retrieved papers are mostly preclinical or off-topic. The most relevant are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9440591](https://pubmed.ncbi.nlm.nih.gov/9440591/) | 1998 | Review | Chest | Multifocal atrial tachycardia in patients with severe illness, mostly COPD; tangential to the predicted indication |
| [1353873](https://pubmed.ncbi.nlm.nih.gov/1353873/) | 1992 | Review | Pathologie-biologie | Calcium channel blockers (including verapamil) for migraine prevention; efficacy not firmly demonstrated; off-topic |
| [24977753](https://pubmed.ncbi.nlm.nih.gov/24977753/) | 2014 | Preclinical | J Trauma Acute Care Surg | Verapamil helped preserve cytoskeletal function in an in vitro intestinal model of hypoxia-reoxygenation |
| [21962069](https://pubmed.ncbi.nlm.nih.gov/21962069/) | 2011 | Preclinical | High Alt Med Biol | Long-term hypoxia and L-type calcium channels in sheep pulmonary artery contractility |
| [9768801](https://pubmed.ncbi.nlm.nih.gov/9768801/) | 1998 | Preclinical | Anesth Analg | Ketamine-induced pulmonary vasodilation in isolated rat lung is partly mediated by L-type calcium channels (verapamil used as a tool) |
| [2429105](https://pubmed.ncbi.nlm.nih.gov/2429105/) | 1986 | Review | J Cardiovasc Pharmacol | Physiological mechanisms of ventricular hypertrophy |

## India Market Information

Verapamil has 17 valid single-ingredient registrations and no cancelled ones. Approved-indication text is not recorded for any of them. The five main entries are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 34075 | Calaptin 40 Tablet (Abbott) | Strip of 30 tablets | Not stated |
| 233892 | Vpl 5mg Injection (Samarth Life Sciences) | Vial of 2 ml injection | Not stated |
| 237647 | Verap 40mg Tablet (Mano Pharma) | Strip of 10 tablets | Not stated |
| 37262 | Calaptin 240 SR Tablet (Abbott) | Strip of 15 sustained-release tablets | Not stated |
| 239131 | Vasopten 120mg Tablet (Torrent) | Strip of 10 tablets | Not stated |

Both oral and injectable forms are marketed.

## Safety Considerations

**Contraindications flagged by the knowledge graph** (drug-disease links, not label text):
- Cardiac: heart failure, atrioventricular block, aortic stenosis and other aortic valve disease, hypertrophic cardiomyopathy, hypotensive disorder, ventricular tachycardia (including catecholaminergic and infantile forms)
- Neuromuscular: myasthenia gravis and other neuromuscular junction disease
- Hepatic, renal and other: liver disease, kidney disease, renal artery obstruction, gallbladder disease, pyoureter
- Haematological: neutropenia, agranulocytosis
- Immune and tissue: angioedema (several forms, including hereditary), connective tissue, bone and cartilage disease

Atrioventricular block and heart failure are especially relevant to the top prediction, because verapamil could worsen conduction disease.

**Drug Interactions:** 328 interactions were identified. Examples from the retrieved list:
- **Major:** Loperamide
- **Moderate:** Clarithromycin, Cimetidine, Bupropion, Aprepitant, Metformin, Canagliflozin, Acetylsalicylic acid, several corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), and several calcium salts
- **Minor:** Morphine

Package insert warnings and contraindications could not be retrieved. Please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All seven predictions are supported by model scores only, with no clinical trials and no direct literature. The top prediction (obsolete bundle branch block) is mechanistically implausible and carries a safety concern. Verapamil is also contraindicated in atrioventricular block and heart failure. The pulmonary hypertension predictions carry safety concerns of their own.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Review of the hypertension-related predictions (ranks 2 and 3) against existing hypertension use. They overlap with the approved indication and may add little new value.
- Targeted literature and trial searches for any prediction that moves forward
- A safety assessment for conduction disease and pulmonary hypertension before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

