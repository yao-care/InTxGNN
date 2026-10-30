---
layout: default
title: Atezolizumab
parent: Model Prediction Only (L5)
nav_order: 78
evidence_level: L5
indication_count: 6
monitor_inn: "Atezolizumab"
predicted_indications: ["uterine ligament adenocarcinoma", "endocervical carcinoma", "adenoid cystic carcinoma of the cervix uteri", "uterine ligament serous adenocarcinoma", "signet ring cell variant cervical mucinous adenocarcinoma", "intestinal variant cervical mucinous adenocarcinoma"]
last_modified_at: 2026-10-30
description: "Atezolizumab: predicted new indication Uterine ligament adenocarcinoma (evidence level L5). Approved use: Transitional cell carcinoma"
---

# Atezolizumab
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

## Atezolizumab: From Transitional Cell Carcinoma to Uterine Ligament Adenocarcinoma
{: .text-alpha }

## One-Sentence Summary

Atezolizumab is an injectable antibody-based cancer immunotherapy.
The TxGNN model predicts it may be effective for **uterine ligament adenocarcinoma**, but **no clinical trials and no publications** currently support this specific prediction. It is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Transitional cell carcinoma (relation recorded in the knowledge graph; the local licence records give no indication text) |
| Predicted New Indication | Uterine ligament adenocarcinoma |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (2 of 2) – CDSCO approval status is not included in this data |
| Number of Licences | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Atezolizumab is generally known as an antibody that blocks PD-L1, which may restore T-cell activity against tumour cells. A plausible rationale is that gynaecological adenocarcinomas can express PD-L1 and may respond to this approach.

Nothing in the compiled data confirms this for uterine ligament adenocarcinoma. The score (0.9993) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The high score should not be read as clinical evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for uterine ligament adenocarcinoma.

---

## Literature Evidence

Currently no related literature available for uterine ligament adenocarcinoma.

---

## Closest Supported Alternative: Endocervical Carcinoma

The second-ranked prediction, **endocervical carcinoma** (score 0.9992), is the only prediction in this candidate with registered trials. These are early-phase studies, and no results were provided in the data.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02921269](https://clinicaltrials.gov/study/NCT02921269) | Phase 2 | Completed | 11 | Atezolizumab plus bevacizumab in recurrent, persistent or metastatic cervical cancer. The sample is very small and no results were provided. |
| [NCT03738228](https://clinicaltrials.gov/study/NCT03738228) | Phase 1 | Completed | 40 | Atezolizumab as an immune primer and with extended-field chemoradiotherapy in node-positive locally advanced cervical cancer. It gives feasibility and safety signals only. |

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37467967](https://pubmed.ncbi.nlm.nih.gov/37467967/) | 2023 | Review | Biomedical Journal | Small cell neuroendocrine carcinoma of the cervix. It notes limited data, mostly case series, and discusses emerging therapies. It is not specific to atezolizumab. |

The other predictions (adenoid cystic carcinoma of the cervix uteri, uterine ligament serous adenocarcinoma, and signet ring cell and intestinal variants of cervical mucinous adenocarcinoma) have no trials or literature in the compiled data.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 219483 | Tecentriq Injection | Vial of 14 ml injection | Roche Products India Pvt Ltd |
| 217022 | Tecentriq 1200mg Injection | Vial of 20 ml solution for infusion | Roche Products India Pvt Ltd |

Both licences are valid single-ingredient products. The licence records contain no approved-indication text, so the approved uses cannot be confirmed from the compiled data.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-L1 checkpoint inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 75 interactions in total. The first 20 reviewed include:
  - **Major**: adalimumab, baricitinib, and live BCG vaccine (Tice substrain).
  - **Moderate**: corticosteroids (hydrocortisone, prednisone, prednisolone, methylprednisolone, dexamethasone, betamethasone, budesonide, triamcinolone, deflazacort), roflumilast, azathioprine, alemtuzumab, anakinra, alefacept, and several vaccines (tetanus toxoid, anthrax, adenovirus type 4).
  - Most of these involve immunosuppressants or live or inactivated vaccines, so combination use needs review.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no trials or publications for uterine ligament adenocarcinoma, so the evidence level is L5 and the prediction rests on the model score alone. Endocervical carcinoma is the better-supported direction, but its evidence is limited to one small Phase 2 trial (n=11) and one Phase 1 trial.

**To proceed, the following is needed:**
- Mechanism of action data and PD-L1 expression data for uterine ligament adenocarcinoma
- Trial results or published outcomes for the cervical cancer studies (NCT02921269, NCT03738228)
- Package insert warnings and contraindications for the Indian products, and the approved indication text
- A decision on whether to prioritise endocervical carcinoma over the top-ranked prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

