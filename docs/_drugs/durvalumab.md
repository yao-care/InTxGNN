---
layout: default
title: Durvalumab
parent: Model Prediction Only (L5)
nav_order: 294
evidence_level: L5
indication_count: 6
monitor_inn: "Durvalumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-10-30
description: "Durvalumab: predicted new indication Uterine ligament adenocarcinoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Durvalumab
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Durvalumab: Uterine ligament adenocarcinoma
{: .text-alpha }

## One-Sentence Summary

Durvalumab is a PD-L1 immune checkpoint antibody. The knowledge graph records transitional cell carcinoma as its original indication (a relation recorded in the knowledge graph, not a confirmed approved indication).
The TxGNN model predicts it may be effective for **uterine ligament adenocarcinoma**, but **no clinical trials and no publications** currently support this specific prediction. The prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Uterine ligament adenocarcinoma |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (2 of 2) – CDSCO approval status is not included in this data |
| Number of Listed Products | 2 (valid: 2) |
| Number of Approvals | 2 licences (both single-ingredient, valid) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Durvalumab is known as a PD-L1 inhibitor: by blocking PD-L1 it can restore T-cell antitumour activity. Its link to the original indication comes from the TxGNN model (deep learning); the score comes from the model and may reflect similarities the model learned between related diseases, not biological evidence.

Gynaecological adenocarcinomas could, in principle, express PD-L1 and respond to checkpoint blockade. However, this is only a hypothesis. No trial, publication or tumour-specific PD-L1 data for uterine ligament adenocarcinoma was provided, so the very high TxGNN score is a computational prediction only.

### Other Predicted Indications (for context)

| Rank | Predicted Disease | TxGNN Score | Evidence Level |
|------|------|------|------|
| 2 | Endocervical carcinoma | 0.9991 | L5 (see note below) |
| 3 | Adenoid cystic carcinoma of the cervix uteri | 0.9991 | L5 |
| 4 | Uterine ligament serous adenocarcinoma | 0.9991 | L5 |
| 5 | Signet ring cell variant cervical mucinous adenocarcinoma | 0.9990 | L5 |
| 6 | Intestinal variant cervical mucinous adenocarcinoma | 0.9990 | L5 |

Note: the one trial linked to endocervical carcinoma is a Phase 1 study in recurrent or metastatic cervical, vaginal or vulvar cancer. It does not address the top-ranked disease, uterine ligament adenocarcinoma, and does not state which histologies were enrolled. It is therefore not counted as evidence for the top-ranked prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered for uterine ligament adenocarcinoma.

For reference, the nearest related study, listed under the rank-2 prediction (endocervical carcinoma):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03452332](https://clinicaltrials.gov/study/NCT03452332) | Phase 1 | Completed | 20 | Hypofractionated radiotherapy plus durvalumab and tremelimumab in recurrent or metastatic cervical, vaginal or vulvar cancer; early safety and feasibility study, no efficacy results available |

## Literature Evidence

Currently no related literature available for uterine ligament adenocarcinoma.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 108524 | Imfinzi Injection (AstraZeneca) | Vial of 10 ml injection | Indication text not available |
| Registration No. 108392 | Imfinzi Injection (AstraZeneca) | Vial of 2.4 ml injection | Indication text not available |

## Safety Considerations

- **Drug Interactions**: 81 interactions were recorded. Examples:
  - **Major**: adalimumab
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, prednisolone, prednisone, methylprednisolone, budesonide, betamethasone, triamcinolone, deflazacort), roflumilast, alefacept, alemtuzumab, anakinra, anthrax vaccine, tetanus toxoid vaccine
  - **Minor**: zinc salts (acetate, gluconate, sulfate, chloride)

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for uterine ligament adenocarcinoma rests solely on a TxGNN score of 0.9992. No clinical trials or publications address this disease, so the evidence level is L5.

**To proceed, the following is needed:**
- Disease-specific evidence (trials, case series or PD-L1 expression data) for uterine ligament adenocarcinoma
- Mechanism of action data for durvalumab
- Package insert warnings and contraindications, which are required before any safety screening
- Indication text for the two licences, to confirm the approved uses in India
- If cervical cancer is of interest, a more relevant research question than the top-ranked disease, since the Phase 1 trial NCT03452332 offers early safety data in that setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

