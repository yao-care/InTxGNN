---
layout: default
title: Quinidine
parent: Model Prediction Only (L5)
nav_order: 717
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Quinidine: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Atrial fibrillation, malaria"
monitor_inn: "Quinidine"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis"]
---

# Quinidine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Quinidine: From Atrial Fibrillation and Malaria to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Quinidine is a class Ia antiarrhythmic originally used to treat atrial fibrillation and malaria.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**,
but currently **no clinical trials and no publications** support this direction. It is a computational prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation, malaria (from the knowledge graph; the India label text has no indication recorded) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.27% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, quinidine is a class Ia antiarrhythmic that blocks sodium and potassium channels and also has anticholinergic and antimalarial activity. Its efficacy in atrial fibrillation and malaria is established.

NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2). These mutations cause inappropriate water reabsorption in the renal collecting duct even when vasopressin is undetectable. No established mechanism links quinidine to V2 receptor signalling or aquaporin-2 regulation. A speculative route might involve ion-channel modulation in renal tubular cells, but nothing in the available data supports it.

The high TxGNN score (0.993) therefore reflects a pattern found in the knowledge graph, not demonstrated biology or clinical benefit. Current NSIAD management relies on fluid restriction, urea, and sometimes vaptan-class or other agents. None of these involve quinidine.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 152504 | Natcardine 100mg Tablet | Strip of 10 tablets (oral) | Not recorded |

The product is a single-ingredient preparation made by Franco-Indian Pharmaceuticals Pvt Ltd. Its registration status is valid.

---

## Safety Considerations

- **Contraindications / disease associations (knowledge graph, not label text):**
  - Cardiac conditions: long QT syndrome (including familial), torsades de pointes, atrioventricular block, progressive familial heart block, left bundle branch block, heart failure, digitalis poisoning
  - Organ function: kidney disease, liver disease, gallbladder disease
  - Neuromuscular conditions: myasthenia gravis (including adult-onset), neuromuscular junction disease
  - Other conditions: thrombocytopenia, potassium deficiency, hypotensive disorder, psoriasis, parapsoriasis, pulmonary emphysema, oesophageal dyskinesia, pyoureter
- **Drug Interactions:** 345 interactions are recorded. The main ones listed are:
  - **Major:** loperamide, clarithromycin, picosulfuric acid, polyethylene glycol (3350 with electrolytes), dolasetron, eliglustat, palonosetron
  - **Moderate (examples):** famotidine, ranitidine, cimetidine, metformin, aprepitant, acetylsalicylic acid, bisacodyl, glycopyrronium, chlorpropamide, potassium citrate, eluxadoline, glimepiride, trospium
- **Repurposing-specific concern:** Quinidine carries a risk of QT prolongation and torsades de pointes. NSIAD patients are often hyponatraemic, and electrolyte disturbances further raise arrhythmia risk.

The India package insert warnings and contraindications were not available. Please refer to the package insert for label-based safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical, literature or mechanistic support. The cardiac safety profile of quinidine is a particular concern in a population prone to electrolyte imbalance.

**To proceed, the following is needed:**
- Mechanism of action data, plus any evidence linking quinidine to V2 receptor or aquaporin-2 pathways
- Preclinical or in vitro studies testing quinidine in AVPR2 gain-of-function models
- The India package insert (warnings and contraindications) for formal safety screening
- A cardiac and electrolyte safety assessment (QT risk, hyponatraemia) specific to NSIAD patients
- Comparison against current standard options (fluid restriction, urea, vaptan-class agents)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

