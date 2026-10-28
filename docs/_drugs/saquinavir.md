---
layout: default
title: Saquinavir
parent: Model Prediction Only (L5)
nav_order: 764
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "Saquinavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
description: "Saquinavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Saquinavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Saquinavir: Feline acquired immunodeficiency syndrome
{: .text-alpha }

## One-Sentence Summary

Saquinavir was originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV infection in cats)**, but **no clinical trials and no publications** currently support this specific prediction. It rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, saquinavir is an HIV-1 protease inhibitor. It blocks cleavage of the Gag-Pol polyprotein, so new virus particles cannot mature into infectious virions. Its efficacy in HIV infection is established.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV-1, and its protease is structurally similar. Activity against FIV protease is therefore plausible. However, FIV protease differs from HIV-1 protease in substrate specificity and inhibitor sensitivity, so activity cannot be assumed.

The very high TxGNN score mainly reflects how close this disease sits to the HIV indication in the knowledge network. It is not independent evidence of efficacy. This is also a veterinary disease, so it is a research-model question rather than a human therapeutic indication.

**Other predictions for this drug (for context):**
- **Simian immunodeficiency virus infection (L4):** In vitro studies show saquinavir inhibits SIVmac239 with an EC50 of about 55 nM, versus about 47 nM for HIV-1 (PMID 12709355). SIV is a non-human model infection.
- **AIDS related complex (L1):** This is essentially an on-label HIV indication, supported by completed Phase 2/3 trials including a 3,000-patient Phase 3 RCT (NCT00002334). It is not true repurposing.
- **Congenital HIV (L3):** Supported by observational pregnancy cohorts only, with no dedicated trial.

## Clinical Trial Evidence

Currently no related clinical trials registered for feline acquired immunodeficiency syndrome.

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 207545 | Saquin 500mg Tablet (Hetero Drugs Ltd) | Oral, strip of 10 tablets | — (not stated in the registration record) |

## Safety Considerations

- **Disease-level contraindication signals (knowledge-graph data, not label text):**
  - Cardiac conduction: long QT syndrome (including familial), torsades de pointes, atrioventricular block
  - Liver: liver failure, liver disease, cirrhosis, chronic hepatitis B and C infection
  - Metabolic: hyperglycemia, diabetes mellitus, diabetic ketoacidosis, hypertriglyceridemia, potassium deficiency
  - Other: gallbladder disease, hemophilia (including symptomatic female carriers), substance abuse/dependence
- **Drug Interactions:** 313 interactions are recorded, so the burden is heavy.
  - **Major:** triamcinolone, budesonide, clarithromycin
  - **Moderate (examples):** omeprazole, rabeprazole, famotidine, dexamethasone, hydrocortisone, betamethasone, metformin, canagliflozin, aprepitant, loperamide
- Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no trials or publications for FIV infection, and the disease is a veterinary condition. The mechanistic link is plausible but unproven, and saquinavir has major DDI and QT-related safety issues.

**To proceed, the following is needed:**
- Experimental data on saquinavir activity against FIV protease (enzyme and cell-based assays)
- Detailed mechanism of action data (MOA)
- The package insert for warnings and contraindications
- A decision on whether the veterinary indication is in scope, or whether the human on-label HIV-related predictions should be evaluated instead
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

