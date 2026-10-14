---
layout: default
title: Glucagon
parent: Model Prediction Only (L5)
nav_order: 395
evidence_level: L5
indication_count: 1
---

# Glucagon
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Glucagon: From Hypoglycaemia Rescue to Irritable Bowel Syndrome

## One-Sentence Summary

Glucagon is a pancreatic peptide hormone marketed in India as an injection. The approved indication text was not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **irritable bowel syndrome (IBS)**, but the supporting evidence comes mostly from the related hormone GLP-1 and its analogue ROSE-010, not glucagon itself. The data include **2 clinical trials** (both on GLP-1 pathway drugs) and **20 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (approved indication text is blank for all licences) |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L3 (observational studies and systematic reviews only; no glucagon-specific trials) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for glucagon. Glucagon is derived from proglucagon, the same precursor that gives rise to GLP-1. It is used clinically as a gastrointestinal smooth-muscle relaxant, for example during diagnostic imaging. That use suggests a plausible, but indirect, link to gut motility and visceral hypersensitivity in IBS.

Most of the supporting evidence concerns GLP-1 rather than glucagon. GLP-1 receptor activation inhibits prandial antro-duodeno-jejunal motility and slows gastrointestinal transit. This could relieve IBS symptoms, particularly pain and diarrhoea-predominant symptoms. The relationship between glucagon and these effects is an inference from the shared pathway and the gut-brain axis, not a demonstrated result.

The high TxGNN score is a computational prediction and should not be treated as clinical evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | ROSE-010 (a GLP-1 analogue) on gastrointestinal motor functions in women with constipation-predominant IBS. The population is relevant, but the drug is not glucagon. |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Native GLP-1 versus ROSE-010 on prandial gastric, duodenal and jejunal motility. It enrolled no IBS patients and offers only indirect mechanistic support. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic Review / Meta-analysis | Front Endocrinol | GLP-1 receptor agonists and IBS improvement. GLP-1 and ROSE-010 reduce gastrointestinal motility in IBS patients. |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Systematic Review | J Headache Pain | GLP-1 receptor agonists in headache and pain disorders. Only indirectly relevant. |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohort | Ann Gastroenterol | Prescription and discontinuation patterns of GLP-1 receptor agonists in IBS patients. |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Clinical study cross-analysis | Scand J Gastroenterol | ROSE-010 reduced pain during IBS attacks. The analysis aimed to identify the best-suited subpopulation. |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Exp Physiol | Role of GLP-1 and intestinal L-cells in IBS pathophysiology. |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Review | Adv Exp Med Biol | Aerosolised GLP-1 for diabetes and IBS. |
| [30023410](https://pubmed.ncbi.nlm.nih.gov/30023410/) | 2018 | Review | Cell Mol Gastroenterol Hepatol | Brain-gut-microbiome axis and its effects on motility and secretion. |
| [41480755](https://pubmed.ncbi.nlm.nih.gov/41480755/) | 2026 | Review | J Clin Invest | Mechanisms of gut-brain interaction, including incretin-based therapies. |
| [40880735](https://pubmed.ncbi.nlm.nih.gov/40880735/) | 2025 | Clinical study | Front Nutr | Circulating GLP-1 rose after a low-FODMAP diet in IBS patients. |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Review | Expert Opin Investig Drugs | Novel investigational drugs for constipation-predominant IBS. |

None of these publications tests glucagon itself in IBS.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 94555 | Glucagen 1mg Injection (Novo Nordisk India Pvt Ltd) | Vial of 1 injection | Not available |
| 95312 | Glugon 1mg Injection (United Biotech Pvt Ltd) | Vial of 1 injection | Not available |
| 95915 | Glucagen 1mg Injection (Novo Nordisk India Pvt Ltd) | Prefilled syringe, 1 ml injection | Not available |

## Safety Considerations

- **Drug Interactions**: 25 interactions were identified in total, and the 20 listed in the data are all graded Minor. They include warfarin and a broad range of beta-blockers (e.g., atenolol, metoprolol, propranolol, carvedilol, bisoprolol, labetalol, sotalol, and the ophthalmic timolol, betaxolol and carteolol).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trial has tested glucagon in IBS. The available trials and reviews concern GLP-1 and its analogue ROSE-010, so the link to glucagon is indirect. The high TxGNN score is only a model prediction, and the label-based safety data are missing. This is best treated as a research question for now.

**To proceed, the following is needed:**
- The India package insert warnings and contraindications, which are missing and block safety screening
- Mechanism of action data for glucagon
- Evidence that glucagon itself, rather than GLP-1 analogues, acts on IBS-relevant pathways
- The approved indication text for the Indian licences
- A feasibility check on injectable administration for a chronic functional bowel condition
- A small exploratory study of glucagon in IBS, if the above supports it
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

