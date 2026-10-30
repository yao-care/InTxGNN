---
layout: default
title: Ibutilide
parent: Model Prediction Only (L5)
nav_order: 419
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
description: "Ibutilide: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not listed in the India license data (known pharmacology: class III a…"
monitor_inn: "Ibutilide"
predicted_indications: ["rheumatoid arthritis", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Ibutilide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Ibutilide: From Cardiac Arrhythmia to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Ibutilide is a class III antiarrhythmic drug given by injection. The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, but this is a computational prediction only, with **0 clinical trials** and **0 publications** currently supporting it. A second prediction, nephrogenic syndrome of inappropriate antidiuresis (NSIAD), is equally unsupported.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the India license data (known pharmacology: class III antiarrhythmic) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9931 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, ibutilide is a class III antiarrhythmic that blocks the delayed rectifier potassium current (IKr, hERG) and promotes a slow inward sodium current. This prolongs the cardiac action potential.

No clear link to rheumatoid arthritis biology (TNF, IL-6, JAK/STAT, B/T-cell activation) is supported by the available data. Potassium channels such as Kv1.3 and KCa3.1 are discussed in T-cell and synoviocyte biology. However, ibutilide is not known to act on them, so this connection is speculative. The high score (0.993) reflects a model prediction, not experimental or clinical support.

The second predicted indication, **nephrogenic syndrome of inappropriate antidiuresis** (score 0.9930), is caused by gain-of-function mutations in the vasopressin V2 receptor. Ibutilide has no known action on this receptor or on renal water handling. This prediction also has no trials or literature. It is unfavorable on safety grounds because hyponatremia and electrolyte disturbances increase the risk of proarrhythmia with ibutilide.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 85028 | Fibricor Injection (Zuventus Healthcare Ltd) | Vial of 10 ml injection | Not stated |

## Safety Considerations

- **Knowledge-graph contraindications** (from drug-disease contraindication links, not label text): long QT syndrome, familial long QT syndrome, torsades de pointes, potassium deficiency disease, atrioventricular dissociation, atrioventricular block, heart block.
- **Drug interactions:** 125 interactions were identified. Major ones include:
  - Macrolide and fluoroquinolone antibiotics: clarithromycin, levofloxacin
  - 5-HT3 antagonist antiemetics: ondansetron, granisetron, dolasetron, palonosetron
  - Cisapride
  - Eliglustat
  - Bowel-preparation and laxative products: picosulfuric acid, polyethylene glycol 3350 with electrolytes, sodium sulfate
  
  Moderate interactions include famotidine, loperamide, bisacodyl, lactitol, lactulose, polyethylene glycol 3350, castor oil and glycerin. Metronidazole is a minor interaction.
- **Clinical context:** Ibutilide is known to cause QT prolongation and torsades de pointes, and is given only in monitored settings. This is general pharmacological knowledge rather than data from this record.

Please also refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Both predictions rest only on model scores, with no clinical trials, no literature and no plausible mechanistic link. Ibutilide's proarrhythmic risk (QT prolongation, torsades de pointes) is a significant safety barrier for a non-cardiac indication such as rheumatoid arthritis.

**To proceed, the following is needed:**
- The India package insert (warnings and contraindications), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank
- Preclinical evidence, for example on Kv1.3/KCa3.1 channel activity in T cells and synoviocytes, to test the speculative mechanism
- A risk-benefit assessment of QT and arrhythmia risk for chronic or non-monitored use
- Confirmation of the approved indication for the registered product
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

