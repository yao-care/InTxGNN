---
layout: default
title: Pefloxacin
parent: Model Prediction Only (L5)
nav_order: 650
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pefloxacin: predicted new indication Heart conduction disease (evidence level L5). Approved use: Not stated in the licence data (fluoroquinolone antibacterial)"
monitor_inn: "Pefloxacin"
predicted_indications: ["heart conduction disease", "heart neoplasm", "heart valve disease", "congenital anomaly of ventricular septum", "pericardium disease", "heart aneurysm", "cor biloculare", "carcinoid heart disease", "myocardial rupture", "cardiac anomalies-heterotaxy syndrome"]
---

# Pefloxacin
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

## Pefloxacin: From Bacterial Infection (Fluoroquinolone Antibacterial) to Heart Conduction Disease
{: .text-alpha }

## One-Sentence Summary

Pefloxacin is a fluoroquinolone antibacterial marketed in India, and the data compiled for this report do not list a specific approved indication.
The TxGNN model predicts it may be effective for **heart conduction disease**, but **no clinical trials and no publications** support this prediction.
The prediction is model output only, and known fluoroquinolone safety signals point in the opposite direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data (fluoroquinolone antibacterial) |
| Predicted New Indication | Heart conduction disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Pefloxacin belongs to the fluoroquinolone class, which inhibits bacterial DNA gyrase and topoisomerase IV. This is an antibacterial mechanism with no recognised role in cardiac conduction.

The prediction therefore appears weak. Fluoroquinolones are known to block the hERG potassium channel and can prolong the QT interval, so they may cause or worsen conduction abnormalities rather than treat them. The high score most likely reflects network-based associations in the knowledge graph, not a real therapeutic link.

The other top-ranked predictions (all cardiac conditions, scores 99.8% to 99.9%) show the same pattern: heart neoplasm, heart valve disease, congenital ventricular septal anomaly, pericardium disease, heart aneurysm, cor biloculare, carcinoid heart disease, myocardial rupture, and cardiac anomalies-heterotaxy syndrome. Most are structural or congenital conditions that an antibiotic cannot plausibly treat. For heart aneurysm, regulatory safety warnings link fluoroquinolones to a higher risk of aortic aneurysm and dissection, which conflicts with the predicted direction.

Only two of these predictions have any literature, and neither supports a therapeutic use:
- **Heart valve disease:** a 2000 rabbit study of pefloxacin and other quinolones in experimental *Pseudomonas aeruginosa* endocarditis. It is preclinical and relevant only to infective valve disease (L4).
- **Pericardium disease:** a 1995 Italian nocardiosis case series, indirect and incidental (L4).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the predicted indication (heart conduction disease).

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 92289 | Floxaquin P 400mg Tablet (Themis Medicare Ltd) | Strip of 4 tablets | Not stated |
| Registration No. 180984 | Pef 400mg Tablet (Agron Remedies Pvt Ltd) | Strip of 10 tablets | Not stated |
| Registration No. 183629 | Qucin 400mg Infusion (Aristo Pharmaceuticals Pvt Ltd) | Bottle of 100 ml infusion | Not stated |
| Registration No. 181664 | Pefocin 400mg Tablet (Pfizer Ltd) | Strip of 10 tablets | Not stated |
| Registration No. 176041 | Pelox 400mg Tablet (Wockhardt Ltd) | Strip of 10 tablets | Not stated |

Twelve valid single-ingredient registrations are on record in total, covering oral tablets and one intravenous infusion.

---

## Safety Considerations

- **Class-level cardiac risks (from known fluoroquinolone safety information, not from the compiled data):** QT prolongation via hERG blockade, and a regulatory warning for aortic aneurysm and dissection.
- **Tendon toxicity:** fluoroquinolones are associated with tendinopathy and tendon rupture, as illustrated by a 2021 case report with ciprofloxacin.

Please refer to the package insert for further safety information, including contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no trials or supporting literature. The proposed mechanism is biologically implausible, and known fluoroquinolone cardiac safety signals suggest potential harm in cardiac patients.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator or manufacturer, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- A cardiac safety review (QT prolongation, arrhythmia, aortic aneurysm) before any cardiac indication is considered
- Any direct clinical or mechanistic evidence for a conduction-disease benefit; otherwise, deprioritise this candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

