---
layout: default
title: Triptorelin
parent: Model Prediction Only (L5)
nav_order: 870
evidence_level: L5
indication_count: 10
---

# Triptorelin
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

# Triptorelin: From Approved Hormonal Therapy to Precocious Puberty

## One-Sentence Summary

Triptorelin is a GnRH (gonadotropin-releasing hormone) agonist that is marketed in India, but the approved indication text is not available in the data compiled for this report.
The TxGNN model's top-scoring prediction with real supporting evidence is **precocious puberty**, backed by **8 clinical trials** and **19 publications**. However, this is already an established, marketed use of triptorelin, so it is not a true repurposing finding.
The other nine predictions (including the top-ranked hypertrichosis) have little or no supporting evidence and are most likely knowledge-graph artifacts.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (approved indication text is empty in all six registrations) |
| Predicted New Indication | Precocious puberty (the highest-ranked prediction, hypertrichosis, has only L5 evidence and no credible mechanism; precocious puberty is the best-supported of the ten) |
| TxGNN Prediction Score | 99.89% (precocious puberty); 99.997% (hypertrichosis, rank 1) |
| Evidence Level | L1 (precocious puberty) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Proceed with Guardrails (precocious puberty only) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not available in the data compiled for this report. Based on known pharmacology, triptorelin is a GnRH agonist. Continuous (non-pulsatile) stimulation desensitises pituitary GnRH receptors and lowers LH and FSH secretion. This in turn suppresses gonadal sex steroids.

This mechanism directly addresses central precocious puberty (CPP), which is caused by premature activation of the hypothalamic-pituitary-gonadal axis. The prediction is therefore mechanistically sound and consistent with the established use of GnRH agonists as the standard therapy for CPP. Because CPP is an approved, marketed use, the original-indication field in the source data appears incomplete.

Most of the other predictions lack a plausible mechanism:
- **Hypertrichosis (rank 1):** The only paper found describes ciclosporin-induced hypertrichosis in a patient who was also taking triptorelin. It is an adverse-event report, not evidence of benefit. The high score is likely a graph-proximity artifact.
- **Ambras syndrome, malformation syndromes, Dandy-Walker syndrome, hair shaft abnormalities, familial trichomegaly:** These are genetic or structural conditions with no link to GnRH signalling.
- **Allergic urticaria:** Hypersensitivity reactions are known adverse effects of GnRH analogues, so the direction of effect may be opposite to benefit.
- **Familial male-limited precocious puberty:** This is driven by activating LHCGR mutations, independent of gonadotropins, so a GnRH agonist would not address the primary driver. It would matter only if secondary central puberty develops. The retrieved literature concerns ketoconazole and letrozole, not triptorelin.
- **Aromatase excess syndrome:** The driver is peripheral aromatisation. Aromatase inhibitors are the treatment, and a GnRH agonist would at most be an adjunct.

---

## Clinical Trial Evidence

Trials for precocious puberty:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05029622](https://clinicaltrials.gov/study/NCT05029622) | Phase 3 | Completed | 66 | Open-label single-arm study of the 6-month formulation in Chinese children with CPP; primary endpoint is LH suppression to prepubertal levels at Month 6 |
| [NCT01467882](https://clinicaltrials.gov/study/NCT01467882) | Phase 3 | Completed | 44 | Efficacy, safety and pharmacokinetics of the 22.5 mg 6-month formulation in CPP |
| [NCT00564850](https://clinicaltrials.gov/study/NCT00564850) | Phase 3 | Completed | 37 | Triptorelin 11.25 mg in children with precocious puberty; proportion with suppressed LH response at 3 months |
| [NCT00909844](https://clinicaltrials.gov/study/NCT00909844) | Phase 3 | Completed | 35 | Long-term follow-up of the 11.25 mg study; maintenance of regression or stabilisation of sexual maturity |
| [NCT04736602](https://clinicaltrials.gov/study/NCT04736602) | Phase 3 | Completed | 32 | Efficacy and safety of the 3-month formulation in Chinese children with CPP |
| [NCT01278290](https://clinicaltrials.gov/study/NCT01278290) | Phase 3 | Completed | 46 | Triptorelin as a stimulation test for the early diagnosis of CPP in girls (diagnostic use) |
| [NCT06487143](https://clinicaltrials.gov/study/NCT06487143) | Phase 4 | Not yet recruiting | 134 | 3-month vs 1-month formulation: efficacy, glucose and lipid metabolism, and bone density in idiopathic CPP |
| [NCT00438217](https://clinicaltrials.gov/study/NCT00438217) | Phase 4 | Unknown | 100 | Genetic and environmental factors influencing growth rate in children with precocious puberty (indirect relevance) |

No clinical trials are registered for any of the other nine predicted indications.

---

## Literature Evidence

Publications for precocious puberty (selected):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39412628](https://pubmed.ncbi.nlm.nih.gov/39412628/) | 2024 | Phase 3 single-arm trial | Advances in Therapy | Efficacy, safety and pharmacokinetics of the 6-month formulation in Chinese children with CPP |
| [37584898](https://pubmed.ncbi.nlm.nih.gov/37584898/) | 2023 | Phase 3 single-arm trial | Advances in Therapy | Efficacy and safety of the 3-month formulation in Chinese children with CPP |
| [37266535](https://pubmed.ncbi.nlm.nih.gov/37266535/) | 2023 | Comparative study | Frontiers in Pediatrics | Efficacy and tolerability comparison of leuprolide and triptorelin in idiopathic CPP |
| [40916129](https://pubmed.ncbi.nlm.nih.gov/40916129/) | 2025 | Cohort/comparative | Annals of Pediatric Endocrinology & Metabolism | Leuprolide acetate vs triptorelin pamoate in overweight and obese girls with CPP |
| [40988204](https://pubmed.ncbi.nlm.nih.gov/40988204/) | 2025 | Clinical study | Medicine | Cluster nursing plus triptorelin in 110 children; effects on efficacy and quality of life |
| [29957076](https://pubmed.ncbi.nlm.nih.gov/29957076/) | 2018 | Review | Expert Review of Clinical Pharmacology | Triptorelin depot in CPP: adult-height outcomes and 11.25 mg/22.5 mg formulations |
| [27191050](https://pubmed.ncbi.nlm.nih.gov/27191050/) | 2016 | Review | Archives of Endocrinology and Metabolism | Diagnosis and therapeutic management of CPP |
| [26887034](https://pubmed.ncbi.nlm.nih.gov/26887034/) | 2016 | Clinical study | J Pediatr Endocrinol Metab | First study of the 22.5 mg 6-month formulation in CPP |
| [41384863](https://pubmed.ncbi.nlm.nih.gov/41384863/) | 2025 | Diagnostic accuracy study | Endocrine Connections | Subcutaneous triptorelin stimulation test vs gonadorelin for diagnosing CPP in girls |
| [36875449](https://pubmed.ncbi.nlm.nih.gov/36875449/) | 2023 | Clinical study | Frontiers in Endocrinology | Impact of the 6-month formulation on predicted adult height and basal gonadotropins |

Other predicted indications have only weak literature: one case report of ciclosporin-induced hypertrichosis (PMID 41822646, not triptorelin-specific), and two case reports on familial male-limited precocious puberty (PMIDs 36049976 and 35909557) that mainly concern ketoconazole and letrozole.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 175170 | Pamorelin LA 3.75mg Injection (Dr Reddy's Laboratories Ltd) | Vial of 1 injection | Not available |
| 175479 | Pamorelin LA 22.5mg Injection (Dr Reddy's Laboratories Ltd) | Vial of 1 injection | Not available |
| 174365 | Pamorelin LA 11.25mg Powder for Injection (Dr Reddy's Laboratories Ltd) | Vial of 1 powder for injection | Not available |
| 58621 | Decapeptyl 0.1mg Injection (Ferring Pharmaceuticals) | Vial of 1 ml injection | Not available |
| 59940 | Decapeptyl Depot Injection (Ferring Pharmaceuticals) | Vial of 1 injection | Not available |

A sixth registration, 222576 (Tryplog Injection, Life Medicare & Biotech Pvt Ltd, vial of 5 ml injection), is also valid. All six are single-ingredient injectable products and none is cancelled.

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

**Contraindication-related disease associations (knowledge graph, not label text):** The knowledge graph links triptorelin to the following conditions as potential contraindications: hypertension, kidney disease, liver disease, gallbladder disease, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, obesity (including monogenic obesity), urinary tract obstruction, pyoureter and spinal cord disease. These should be verified against the product labelling.

**Drug Interactions:** 262 interactions were identified in total. Examples include:
- **Major:** Dolasetron
- **Moderate:** antidiabetic agents (acarbose, metformin, pioglitazone, glimepiride, chlorpropamide, and the gliptins, gliflozins and GLP-1 agonists such as alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, albiglutide and dulaglutide), clarithromycin, famotidine, palonosetron, loperamide, bisacodyl, picosulfuric acid and polyethylene glycol with electrolytes

The antidiabetic interactions are consistent with the knowledge-graph signals around hyperglycaemia and diabetes, and glycaemic monitoring is advisable.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (precocious puberty only). **Hold** for all other predicted indications, including hypertrichosis.

**Rationale:**
- Precocious puberty has multiple completed Phase 3 studies (L1), including four Phase 3 trials of triptorelin formulations in CPP and a consistent literature base. It is a mechanistically sound, established use rather than a new repurposing opportunity.
- The other nine predictions have no credible mechanism and little or no clinical evidence (L4–L5), and the high TxGNN scores appear to be graph artifacts.

**To proceed, the following is needed:**
- The approved indication text for the Indian registrations, to confirm whether CPP is already labelled, since all six registrations currently have empty indication fields. If it is, no repurposing action is required.
- Package insert warnings and contraindications, which are a blocking gap for safety screening.
- Mechanism-of-action data from DrugBank.
- A safety monitoring plan for paediatric use, covering glycaemic and metabolic status, bone density and growth.
- Verification of the formulation and dose strengths (3.75 mg, 11.25 mg, 22.5 mg) against paediatric dosing in the Indian context.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

