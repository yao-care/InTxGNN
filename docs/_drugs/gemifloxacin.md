---
layout: default
title: Gemifloxacin
parent: Model Prediction Only (L5)
nav_order: 390
evidence_level: L5
indication_count: 10
monitor_inn: "Gemifloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "endomyometritis"]
last_modified_at: 2026-10-23
description: "Gemifloxacin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Bacterial pneumonia"
---

# Gemifloxacin
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

## Gemifloxacin: From Bacterial Pneumonia to Polyclonal Hyperviscosity Syndrome
{: .text-alpha }

## One-Sentence Summary

Gemifloxacin is a fluoroquinolone antibacterial.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** support this prediction. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial pneumonia (relation recorded in the knowledge graph; the local licence records provide no indication text) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | at least 20 |
| Number of approvals | At least 20 licences (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, gemifloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV. This explains its antibacterial activity in pneumonia.

Polyclonal hyperviscosity syndrome results from raised polyclonal immunoglobulin levels and is not an infectious process. No plausible mechanistic link to an antibacterial has been identified. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, so the prediction should be treated with strong caution.

Other predicted diseases in the same list show a similar pattern. Most are haematological or genetic conditions with no mechanistic rationale. Two have some antibacterial plausibility, but neither has direct evidence:
- **Septicemic plague** (L4 in the data compiled for this report, though no direct study is cited, so L5 applies under the evidence ceiling): *Yersinia pestis* is susceptible to fluoroquinolones, and other drugs in the class are used for plague. Approved alternatives already exist.
- **Endomyometritis**: limited anaerobic coverage and no gemifloxacin-specific data on uterine tissue penetration.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Gemifloxacin is marketed in India as a single-ingredient product. Twenty licences are listed, and the list may be partial. No approved indication text is available in the licence records. Five main licences are shown below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 31898 | Biogem 200mg Injection | Vial of 1 injection | United Biotech Pvt Ltd |
| 32541 | Biogem 1000mg Injection | Vial of 1 injection | United Biotech Pvt Ltd |
| 102277 | Gametop 320mg Tablet | Strip of 10 tablets | Solitaire Pharmacia Pvt Ltd |
| 94597 | G-Cin Tablet | Strip of 5 tablets | Lupin Ltd |
| 29736 | Biogem 320mg Tablet | Strip of 5 tablets | Biochem Pharmaceutical Industries |

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph links gemifloxacin to several conditions as contraindications, including long QT syndrome, torsades de pointes, epilepsy, anxiety and neurotic disorders, potassium deficiency, tendinitis, peripheral neuropathy, *Clostridium difficile* colitis, impaired renal function, and myasthenia gravis. These need confirmation against the package insert.
- **Drug Interactions:** 273 interactions were found. Major-level interactions include hydrocortisone, betamethasone, chlorpropamide and dolasetron. Moderate-level interactions include antidiabetic agents (metformin, pioglitazone, empagliflozin, dapagliflozin, canagliflozin, alogliptin, acarbose), acetylsalicylic acid, clarithromycin, famotidine, loperamide and calcium acetate.
- **Class concern:** Fluoroquinolones carry a boxed warning for peripheral neuropathy. This is a particular concern for the predicted haematological disease associated with acquired peripheral neuropathy.

Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication studies gemifloxacin in polyclonal hyperviscosity syndrome, and no plausible mechanism links an antibacterial to this condition. The prediction rests on model score alone (L5).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- A biological rationale for the prediction, otherwise the candidate should be dropped
- If the team wants to pursue the more plausible antibacterial candidates (septicemic plague, endomyometritis), in vitro MIC data and animal model data first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

