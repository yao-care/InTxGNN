---
layout: default
title: Maraviroc
parent: Model Prediction Only (L5)
nav_order: 515
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Maraviroc"
predicted_indications: ["multiple endocrine neoplasia", "acne (disease)", "primary cutaneous T-cell lymphoma", "pediatric systemic lupus erythematosus", "primary cutaneous T-cell non-Hodgkin lymphoma", "primary cutaneous B-cell lymphoma", "candidiasis", "complement component 4a deficiency", "cytomegalovirus infection", "HER2 positive breast carcinoma"]
description: "Maraviroc: predicted new indication Multiple endocrine neoplasia (evidence level L5). In India: 1 listed product (1 not discontinued)"
---

# Maraviroc
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

## Maraviroc: Multiple endocrine neoplasia
{: .text-alpha }

## One-Sentence Summary

Maraviroc is a CCR5 antagonist marketed in India as a single-ingredient oral tablet, but the data compiled for this report do not list an approved indication.
The TxGNN model ranks **multiple endocrine neoplasia** as its top prediction (score 0.9982), yet there are **0 clinical trials** and **0 publications** supporting it.
Among the ten predicted indications, the best-grounded hypothesis is **HER2-positive breast carcinoma**, which has one preclinical study on the CCL5–CCR5 pathway.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for maraviroc: "Maraviroc is an HIV-1 antiviral drug. […] Maraviroc is a member of a therapeutic class called CCR5 co-receptor antagonists. Maraviroc selectively binds to the human chemokine receptor CCR5 present on the cell membrane, preventing the interaction of HIV-1 gp120 and CCR5 necessary for CCR5-tropic HIV-1 to enter cells." ([DailyMed: Selzentry (maraviroc) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3c52dddd-0457-41cd-99e0-d30d4fd00ec5), label version 2023-11-10; accessed 2026-11-19.) Maraviroc is generally known as a CCR5 antagonist, a chemokine-receptor blocker. The data do not state its original indication, so the link between original and new use cannot be assessed directly.

For multiple endocrine neoplasia, no evidence connects CCR5 signalling to the disease. The high TxGNN score is a computational prediction only, with no trials or literature behind it.

Other predicted indications have somewhat more plausible rationale, though all remain hypotheses:
- **HER2-positive breast carcinoma (score 0.9922)**: A preclinical study (PMID 32404410) reports that autocrine CCL5 drives trastuzumab resistance through ERK pathway activation. Blocking CCR5 is therefore a rational idea, but this is the only supporting item and is not clinical evidence.
- **Primary cutaneous T-cell lymphoma (0.9972) and T-cell non-Hodgkin lymphoma (0.9950)**: Chemokine receptors are involved in T-cell trafficking to skin. The only paper is a general review on ACKR1 and has no maraviroc-specific data.
- **Cytomegalovirus infection (0.9923)**: CCR5 has biological relevance to immune responses, but the retrieved paper is an observational study in HIV patients and gives only context-level support.
- **Acne, pediatric systemic lupus erythematosus, primary cutaneous B-cell lymphoma**: Speculative links through CCR5-mediated inflammation, with no supporting data.
- **Candidiasis and complement component 4a deficiency**: No supportive evidence. The candidiasis paper is an HIV drug adverse-effects review that most likely reflects co-occurrence in HIV patients.

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the ten predicted indications.

## Literature Evidence

No literature is available for multiple endocrine neoplasia. The literature retrieved for other predicted indications is listed below for reference.

| PMID | Year | Type | Journal | Related Indication | Key Findings |
|------|-----|------|------|------|---------|
| [32404410](https://pubmed.ncbi.nlm.nih.gov/32404410/) | 2020 | Preclinical/Mechanistic | Mol Cancer Ther | HER2-positive breast carcinoma | Autocrine CCL5 mediates trastuzumab resistance via ERK pathway activation |
| [37006247](https://pubmed.ncbi.nlm.nih.gov/37006247/) | 2023 | Review | Front Immunol | Primary cutaneous T-cell lymphoma (both types) | Review of targeting ACKR1 in cancer and other diseases; indirect, conceptual support only |
| [25397464](https://pubmed.ncbi.nlm.nih.gov/25397464/) | 2014 | Cohort | J Int AIDS Soc | Cytomegalovirus infection | Innate immunity and soluble markers in HIV+ patients on antiretroviral therapy; indirect support only |
| [21671545](https://pubmed.ncbi.nlm.nih.gov/21671545/) | 2011 | Review | Am Fam Physician | Candidiasis | Common adverse effects of antiretroviral therapy; not supportive of efficacy |

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 6047 | Axentri 150mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 93 interactions were identified in the interaction database. Examples:
  - **Major**: Clarithromycin
  - **Moderate**: Aprepitant, Dexamethasone, Cimetidine, Eliglustat, Naltrexone, Clotrimazole, Miconazole, Cobicistat, Deferasirox, Promethazine, Rolapitant, Troglitazone, among others
- **Disease associations flagged in the knowledge graph** (a computational source, not label text): orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy, kidney disease (including chronic and end-stage renal failure), liver disease (including drug-induced liver injury), chronic hepatitis B and hepatitis C infection, gallbladder disease, coronary artery disease, myocardial infarction and ischaemia, coronary thrombosis, hemoglobinopathy, and infectious disease.

Please refer to the package insert for key warnings and contraindications, as label-based data are not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, multiple endocrine neoplasia, rests on a computational score alone, with no trials, no literature, and no mechanistic link. The package insert, approved indication, and mechanism data are also missing, so safety screening cannot proceed.

**To proceed, the following is needed:**
- The India package insert (warnings, contraindications, approved indication), which currently blocks safety screening
- Mechanism of action data from DrugBank
- A mechanistic rationale for CCR5 in multiple endocrine neoplasia, or a decision to prioritise another candidate
- For HER2-positive breast carcinoma, which is a reasonable research question, further preclinical work on CCL5–CCR5 blockade, followed by a review of whether early clinical studies are justified
- A review of the major and moderate drug interactions (especially strong CYP3A inhibitors such as clarithromycin) and the liver, renal, and cardiovascular flags before any new-use study

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Selzentry (maraviroc) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3c52dddd-0457-41cd-99e0-d30d4fd00ec5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

