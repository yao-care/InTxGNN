---
layout: default
title: Sevoflurane
parent: Model Prediction Only (L5)
nav_order: 771
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Sevoflurane: predicted new indication Prinzmetal angina (evidence level L5). Approved use: General anaesthesia (inhaled anaesthetic"
monitor_inn: "Sevoflurane"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "fibromyalgia", "tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "migraine disorder", "inclusion body myositis"]
---

# Sevoflurane
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

## Sevoflurane: From General Anaesthesia to Prinzmetal Angina
{: .text-alpha }

## One-Sentence Summary

Sevoflurane is an inhaled volatile anaesthetic, marketed in India for the induction and maintenance of general anaesthesia (the registered indication text is not available in the data compiled for this report).
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but **no clinical trials and no publications** currently support this prediction.
The prediction should be regarded as a hypothesis only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anaesthesia (inhaled anaesthetic; the registered indication text is not available) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, sevoflurane is a volatile anaesthetic that potentiates GABA-A receptors and inhibits NMDA and nicotinic receptors. Its use in general anaesthesia is well established.

A plausible but unverified link is that volatile anaesthetics modulate calcium handling in vascular smooth muscle and may have vasodilatory effects relevant to coronary vasospasm, the basis of Prinzmetal angina. No trials or publications support this, and a high model score is not clinical evidence.

Practical barriers are also substantial. Sevoflurane is an inhaled agent given under anaesthetic supervision, which makes it unsuitable for the chronic or outpatient management that vasospastic angina requires.

### Other Predicted Indications (all Hold)

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Tourette syndrome | 0.9950 | L5 | Prediction only; chronic inhaled use is impractical |
| 3 | Fibromyalgia | 0.9942 | L4 | One case report of anaesthetic management, not treatment |
| 4 | Tendinitis | 0.9941 | L5 | Nine publications, all perioperative or unrelated to treating tendinitis |
| 5 | Myositis fibrosa | 0.9941 | L5 | No rationale or data |
| 6 | Idiopathic granulomatous myositis | 0.9941 | L5 | No rationale; malignant hyperthermia risk in myopathies is a concern |
| 7 | Nephrogenic syndrome of inappropriate antidiuresis | 0.9940 | L5 | No plausible mechanism |
| 8 | Trichotillomania | 0.9933 | L5 | Speculative only |
| 9 | Migraine disorder | 0.9923 | L5 | One paediatric MRI anaesthesia cohort, not migraine treatment |
| 10 | Inclusion body myositis | 0.9909 | L4 | One anaesthetic-safety case report |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Prinzmetal angina.

---

## Literature Evidence

Currently no related literature available for Prinzmetal angina.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 202762 | Sevura Inhaler For Inhalation (Neon Laboratories Ltd) | Bottle of 250 ml inhaler | Not available |
| 201485 | Sevorane Inhaler (Abbott) | Bottle of 250 ml inhaler | Not available |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: The TxGNN knowledge graph lists contraindication links with epilepsy, kidney disease, pyoureter, liver disease, gallbladder disease, hypotensive disorder, malignant hyperthermia of anaesthesia, exercise-induced malignant hyperthermia, pseudotumor cerebri, intracranial hypertension, Duchenne muscular dystrophy, muscular dystrophy, Becker muscular dystrophy and proteinuria. These should be verified against the package insert.
- **Drug Interactions**: 146 interactions were recorded. Major-level examples include:
  - Epinephrine
  - Dolasetron
  - Cisapride

  Moderate-level examples include morphine, ondansetron, palonosetron, levofloxacin, clarithromycin and famotidine.

  Combined use with other cardiovascular-active or QT-prolonging drugs requires particular caution, especially in a cardiac indication such as angina.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Prinzmetal angina prediction rests on a model score alone, with no clinical trials or publications. Sevoflurane's route of administration (inhaled, under anaesthetic supervision) is a poor fit for a chronic cardiac condition. The listed safety concerns, such as hypotension and the major interaction with epinephrine, add further caution. None of the other nine predicted indications has direct therapeutic evidence either.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulatory sources, which currently block safety screening
- Mechanism of action data (for example, from DrugBank)
- Preclinical or mechanistic studies of sevoflurane in coronary vasospasm
- Assessment of route and setting compatibility with chronic angina management
- Registered indication text for the two Indian licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

