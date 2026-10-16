---
layout: default
title: Maraviroc
parent: Model Prediction Only (L5)
nav_order: 515
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Maraviroc: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not available in the data compiled for this report"
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Maraviroc: From an Unspecified Original Indication to Multiple Endocrine Neoplasia

## One-Sentence Summary

Maraviroc is a CCR5 antagonist marketed in India as a single-ingredient oral tablet, but the data compiled for this report do not list an approved indication.
The TxGNN model ranks **multiple endocrine neoplasia** as its top prediction (score 99.82%), yet there are **0 clinical trials** and **0 publications** supporting it.
Among the ten predicted indications, the best-grounded hypothesis is **HER2-positive breast carcinoma**, which has one preclinical study on the CCL5–CCR5 pathway.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the data compiled for this report |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Maraviroc is generally known as a CCR5 antagonist, a chemokine-receptor blocker. The data do not state its original indication, so the link between original and new use cannot be assessed directly.

For multiple endocrine neoplasia, no evidence connects CCR5 signalling to the disease. The high TxGNN score is a computational prediction only, with no trials or literature behind it.

Other predicted indications have somewhat more plausible rationale, though all remain hypotheses:
- **HER2-positive breast carcinoma (score 99.22%)**: A preclinical study (PMID 32404410) reports that autocrine CCL5 drives trastuzumab resistance through ERK pathway activation. Blocking CCR5 is therefore a rational idea, but this is the only supporting item and is not clinical evidence.
- **Primary cutaneous T-cell lymphoma (99.72%) and T-cell non-Hodgkin lymphoma (99.50%)**: Chemokine receptors are involved in T-cell trafficking to skin. The only paper is a general review on ACKR1 and has no maraviroc-specific data.
- **Cytomegalovirus infection (99.23%)**: CCR5 has biological relevance to immune responses, but the retrieved paper is an observational study in HIV patients and gives only context-level support.
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

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 6047 | Axentri 150mg Tablet (Emcure Pharmaceuticals Ltd) | Strip of 10 tablets (oral) | Not available |

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
- A review of the major and moderate drug interactions (especially strong CYP3A inhibitors such as clarithromycin) and the knowledge-graph liver, renal, and cardiovascular flags before any new-use study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

