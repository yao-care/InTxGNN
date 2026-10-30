---
layout: default
title: Posaconazole
parent: Model Prediction Only (L5)
nav_order: 687
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Posaconazole: predicted new indication Pneumocystosis (evidence level L4). Approved use: Fungal infections (chromomycosis, coccidioidomycosis, aspergillosis…"
monitor_inn: "Posaconazole"
predicted_indications: ["pneumocystosis"]
---

# Posaconazole
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

## Posaconazole: From Invasive Fungal Infections to Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Posaconazole is a triazole antifungal originally used for invasive and superficial fungal infections such as aspergillosis, candidiasis, and histoplasmosis.
The TxGNN model predicts it may be effective for **pneumocystosis** (Pneumocystis pneumonia), but the evidence is very weak: **1 clinical trial** was found (it tested a different drug, rezafungin) and the **5 publications** retrieved are general reviews, guidelines, or retrospective studies, not direct evidence for posaconazole.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fungal infections (chromomycosis, coccidioidomycosis, aspergillosis, sporotrichosis, histoplasmosis, fusariosis, mycetoma, candidiasis, oral candidiasis, etc.). The Indian licence records contain no approved indication text. |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 0.9977 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (18 of 18) – CDSCO approval status is not included in this data |
| Number of Listed Products | 18 (valid: 18) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for the original record is not available. Based on known pharmacology, posaconazole is a triazole antifungal that inhibits fungal lanosterol 14-alpha-demethylase (CYP51), which blocks ergosterol synthesis. Its efficacy against moulds and yeasts such as Aspergillus and Candida is well established.

The link to pneumocystosis is weak. *Pneumocystis jirovecii* has little or no ergosterol in its membrane and relies on cholesterol-type sterols scavenged from the host, so the azole target is largely absent. Posaconazole is not an established treatment for Pneumocystis pneumonia; first-line therapy remains trimethoprim-sulfamethoxazole.

The very high TxGNN score (0.9977) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It should be read as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | Completed | 602 | Rezafungin (an echinocandin) vs standard antimicrobial regimen for preventing invasive fungal disease in allogeneic blood and marrow transplant recipients. It does not test posaconazole, so it gives no direct evidence; it is useful only as disease-area context. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Guideline/Review | The Lancet Infectious Diseases | British Society for Medical Mycology best-practice recommendations for diagnosing serious fungal diseases (diagnosis, not treatment) |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guideline | Zhonghua Jie He He Hu Xi Za Zhi | Chinese guidelines for diagnosis and management of invasive pulmonary fungal disease |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | Overview of invasive candidiasis, aspergillosis, cryptococcosis, and Pneumocystis pneumonia; notes that mould-active posaconazole prophylaxis reduced invasive fungal disease in high-risk haemato-oncology patients |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | Penetration of antifungal and other anti-infective agents into pulmonary epithelial lining fluid |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Retrospective cohort | Transplant Infectious Disease | Infectious complications and antimicrobial management in acute graft-versus-host disease after liver transplantation |

None of these publications shows that posaconazole is effective for Pneumocystis pneumonia.

---

## India Market Information

Posaconazole has 18 valid single-ingredient registrations in India, with no cancelled licences. Oral tablets, oral suspensions, and injections are available. The records contain no approved indication text. Five of the main registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 151535 | Noxafil Oral Suspension (MSD) | Bottle of 105 ml oral suspension | Not stated in the records |
| 176865 | Poshope Injection (Abbott) | Vial of 16.7 ml injection | Not stated in the records |
| 174772 | Posatral Tablet (Mylan) | Strip of 10 tablets | Not stated in the records |
| 176503 | Posahit 100mg Tablet (Sun Pharma) | Strip of 10 tablets | Not stated in the records |
| 175459 | Posaforce 100mg Tablet (Mankind) | Strip of 10 tablets | Not stated in the records |

---

## Safety Considerations

- **Drug Interactions**: 269 interactions were identified in the data compiled for this report. Examples of **Major** interactions:
  - Loperamide
  - Triamcinolone
  - Budesonide

  Examples of **Moderate** interactions:
  - Acid-reducing agents: famotidine, ranitidine, cimetidine, omeprazole, rabeprazole
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone
  - Others: aprepitant, clarithromycin, saxagliptin

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. The biological rationale is weak because Pneumocystis lacks the ergosterol target, no trial or publication directly tests posaconazole for pneumocystosis, and an effective first-line therapy (trimethoprim-sulfamethoxazole) already exists. The evidence level is L4 at best.

**To proceed, the following is needed:**
- Direct preclinical or clinical data on posaconazole against *Pneumocystis jirovecii*, including comparison with standard prophylaxis or treatment
- Package insert warnings and contraindications from Indian labelling, which are required before safety screening
- Verified mechanism of action data
- Approved indication text for the Indian registrations
- A drug-interaction management plan, given the many Major and Moderate interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

