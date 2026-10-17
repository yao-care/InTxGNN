---
layout: default
title: Itraconazole
parent: Model Prediction Only (L5)
nav_order: 457
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Itraconazole: predicted new indication Pneumocystosis (evidence level L5). Approved use: Esophageal candidiasis, candidemia, histoplasmosis, aspergillosis…"
monitor_inn: "Itraconazole"
predicted_indications: ["pneumocystosis"]
---

# Itraconazole
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

# Itraconazole: From Systemic Fungal Infections to Pneumocystosis

## One-Sentence Summary

Itraconazole is an azole antifungal originally used for systemic fungal infections such as candidiasis, histoplasmosis, aspergillosis, blastomycosis and sporotrichosis.
The TxGNN model predicts it may be effective for **pneumocystosis**, but the evidence is currently **model prediction only**, with **0 clinical trials** and **20 publications** (all of low relevance to this specific indication, mostly reviews, case reports and cohort studies).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Esophageal candidiasis, candidemia, histoplasmosis, aspergillosis, blastomycosis, sporotrichosis and other systemic fungal infections (listed in the knowledge graph; no approved indication text is available from Indian licences) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, itraconazole inhibits fungal lanosterol 14-alpha-demethylase (CYP51), which blocks ergosterol synthesis in the fungal cell membrane. Its efficacy in other invasive fungal infections is established.

The link to pneumocystosis is weak. *Pneumocystis jirovecii* was reclassified as a fungus, which may explain why the knowledge graph places it near other fungal diseases. However, it lacks ergosterol in its membrane and uses cholesterol instead, so the azole mechanism has no plausible target in this organism. Standard therapy (trimethoprim-sulfamethoxazole) works through folate pathway inhibition, not ergosterol disruption.

The high score of 0.993 therefore most likely reflects network proximity to other fungal indications (histoplasmosis, aspergillosis, candidiasis) rather than a true mechanistic link. This prediction should be treated with caution.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The retrieved literature mentions pneumocystosis mostly in the context of opportunistic infections in immunocompromised patients. None of it demonstrates itraconazole efficacy against *Pneumocystis*. The relevance of each item has not yet been assessed.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | Randomized, double-blind, placebo-controlled trial (Phase III) | HIV Medicine | Itraconazole capsules for prevention of deep fungal infections in HIV-infected, immunodeficient patients; the abstract provided does not report pneumocystosis results |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | Penetration of antifungal and other anti-infective agents into pulmonary epithelial lining fluid |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | Primary and secondary prophylaxis of opportunistic infections in HIV |
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Review | Clinical Infectious Diseases | Antimicrobial prophylaxis in febrile neutropenia; trimethoprim-sulfamethoxazole is highly effective against *Pneumocystis* pneumonia |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Therapy and prophylaxis of systemic protozoan infections, including *Pneumocystis carinii* |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Seminars in Respiratory Infections | Infection after lung transplantation |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Current Clinical Topics in Infectious Diseases | Prophylaxis and treatment of infection in bone marrow transplant recipients |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort | Transplantation Proceedings | Invasive fungal infections after kidney transplantation, single-centre experience |
| [2233233](https://pubmed.ncbi.nlm.nih.gov/2233233/) | 1990 | Case series | Medicine | Disseminated histoplasmosis in AIDS: clinical findings, diagnosis and treatment |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case report and review | Frontiers in Immunology | *Talaromyces marneffei* and *Pneumocystis jirovecii* coinfection in a child with a STAT1 mutation |

## India Market Information

Itraconazole is marketed in India under 20 valid single-ingredient licences. The licence data compiled for this report do not include approved indication text. The main authorisations are:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 116368 | Kapitra 100mg Capsule | Strip of 4 capsules | Not available |
| 84324 | Fungikem 200 Capsule | Strip of 4 capsules | Not available |
| 107918 | Itragreat 200 Capsule | Strip of 10 capsules | Not available |
| 97177 | Grita Tablet | Strip of 10 tablets | Not available |
| 93319 | Fuzcon I 200mg Tablet | Strip of 4 tablets | Not available |

All products are oral capsules or tablets.

## Safety Considerations

**Contraindication-related conditions (from drug-disease knowledge graph, not label text):** The knowledge graph links itraconazole to the following conditions, which may warrant caution:
- Cardiac: long QT syndrome, familial long QT syndrome, torsades de pointes, congestive heart failure, heart failure, cardiomyopathy, hypertrophic cardiomyopathy, myocardial ischemia, coronary artery disease, heart valve disease, endomyocardial fibrosis
- Hepatic and renal: liver disease, drug-induced liver injury, kidney disease, impaired renal function
- Other: chronic obstructive pulmonary disease, peripheral neuropathy, hearing loss, vision disorder, hypokalaemia (potassium deficiency), hypercalcaemia, achlorhydria

**Drug Interactions:** 295 interactions were identified. Examples of those graded **Major**:
- Loperamide
- Triamcinolone
- Budesonide

Examples graded **Moderate** include famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, aprepitant, alosetron, dexamethasone, hydrocortisone and betamethasone. Acid-suppressing drugs are notable because they can reduce absorption of itraconazole capsules.

For warnings and contraindications from the package insert, please refer to the package insert, as these are not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (Evidence Level L5). There are no registered clinical trials, and the retrieved literature does not show itraconazole activity against *Pneumocystis*. The biological rationale is also doubtful, since the organism lacks the ergosterol target and effective standard therapy already exists.

**To proceed, the following is needed:**
- Manual relevance screening of the literature, and a targeted search for in vitro, animal or clinical data on itraconazole against *Pneumocystis*
- Mechanistic evidence for a plausible target in *Pneumocystis* (e.g. sterol composition and azole sensitivity)
- Detailed mechanism of action data from DrugBank
- Package insert warnings and contraindications from Indian regulatory sources, needed before any safety screening
- A review of cardiac risk (QT prolongation, heart failure) and the major drug interactions, particularly in the immunocompromised populations in which pneumocystosis occurs
- Justification of any added value over standard trimethoprim-sulfamethoxazole therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

