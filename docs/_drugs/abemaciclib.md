---
layout: default
title: Abemaciclib
parent: Moderate Evidence (L3-L4)
nav_order: 13
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Abemaciclib: predicted new indication Rheumatoid arthritis (evidence level L4). Approved use: Not stated in the licence records compiled for this report (abemacicl…"
monitor_inn: "Abemaciclib"
predicted_indications: ["rheumatoid arthritis", "hyperthyroidism", "multiple endocrine neoplasia", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "homozygous familial hypercholesterolemia", "heart disease", "Laubry-Pezzi syndrome", "Pierre Robin syndrome associated with a chromosomal anomaly", "Jeune syndrome situs inversus", "amyotrophic lateral sclerosis"]
---

# Abemaciclib
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Abemaciclib: From Breast Cancer (CDK4/6 Inhibitor) to Rheumatoid Arthritis

## One-Sentence Summary

Abemaciclib is an oral CDK4/6 inhibitor marketed in India as Ramiven tablets. It is used in HR+/HER2- breast cancer, but the licence records compiled for this report contain no indication text.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but this is supported by **0 clinical trials** and only **2 publications**. One is a safety and epidemiology cohort study and the other is preclinical, so the prediction remains a research question.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records compiled for this report (abemaciclib is a CDK4/6 inhibitor used in HR+/HER2- breast cancer, per the literature) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 97.32% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Abemaciclib belongs to the CDK4/6 inhibitor class. Its efficacy in HR+/HER2- breast cancer is established, and the class acts by blocking cell-cycle progression.

Mechanistically, this may apply to rheumatoid arthritis (RA). RA is driven partly by overproliferation and defective apoptosis of fibroblast-like synoviocytes. CDK4/6 inhibition could plausibly suppress this proliferation and modulate immune cell cycling.

The supporting evidence is thin, however. The only clinical-population study is a retrospective analysis of immune-mediated diseases in breast cancer patients taking CDK4/6 inhibitors. It is a safety and epidemiology signal, not efficacy evidence. The 2026 nanoplatform study is preclinical and concerns synoviocyte targeting, not clinical use of abemaciclib. The high TxGNN score is therefore a hypothesis, not a validated finding.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Cohort | The Oncologist | Examined the prevalence of pre-existing and emerging autoimmune diseases in HR+/HER2- breast cancer patients on CDK4/6 inhibitors plus endocrine therapy. This is a safety/epidemiology signal, not RA efficacy evidence. |
| [42289719](https://pubmed.ncbi.nlm.nih.gov/42289719/) | 2026 | Preclinical | Journal of Nanobiotechnology | A pH-responsive nanoplatform (Mn/Si-Abe@BSA) loaded with abemaciclib induces cell-cycle arrest and apoptosis in fibroblast-like synoviocytes in RA models. |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 187040 | Ramiven 200mg Tablet | Strip of 14 tablets | Not stated |
| 187031 | Ramiven 100mg Tablet | Strip of 7 tablets | Not stated |
| 190816 | Ramiven 200mg Tablet | Strip of 7 tablets | Not stated |
| 184868 | Ramiven 150mg Tablet | Strip of 7 tablets | Not stated |

All four licences are valid, are held by Eli Lilly and Company India Pvt Ltd, and cover single-ingredient oral tablets.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. Literature also points to cardiovascular monitoring (QTc, thromboembolism, arrhythmia) and renal function. |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 210 interactions were recorded, and the 19 listed in the compiled data are mostly Moderate.
  - **Major**: clarithromycin, cobicistat, deferiprone, samarium (153Sm) lexidronam, lumacaftor.
  - **Moderate** (examples): aprepitant, dexamethasone, metformin, fluconazole, erythromycin, ticagrelor, roflumilast, chloramphenicol.
- **Literature safety signals** (not label text): cardiovascular toxicity of CDK4/6 inhibitors, including thromboembolic events with abemaciclib, QTc prolongation, atrial arrhythmia and kidney injury in pharmacovigilance data. These are relevant to any use in a non-oncology population.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The RA prediction has a high model score but no registered clinical trials and no efficacy data in humans. The only supporting work is one preclinical nanoplatform study and one safety-focused cohort study. Chronic CDK4/6 inhibition also carries notable cardiovascular and other toxicity signals, which weigh on the risk-benefit balance in a non-cancer population. This is best treated as a research question rather than a development candidate.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications for the India-marketed products (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank to support the mechanistic-link analysis
- Preclinical efficacy data for abemaciclib itself in RA models (for example, synoviocyte proliferation and arthritis animal models)
- A risk-benefit assessment of long-term CDK4/6 inhibition in an autoimmune population, including cardiovascular safety and immunological effects
- Review of other TxGNN predictions that have some supporting evidence, such as multiple endocrine neoplasia and amyotrophic lateral sclerosis (both preclinical or indirect only). Heart disease is not supported, because the literature points to cardiotoxicity rather than benefit.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

