---
layout: default
title: Vandetanib
parent: High Evidence (L1-L2)
nav_order: 882
evidence_level: L2
indication_count: 10
last_modified_at: 2026-10-14
description: "Vandetanib: predicted new indication Renal cell carcinoma (evidence level L2). Approved use: Thyroid gland carcinoma"
monitor_inn: "Vandetanib"
predicted_indications: ["renal cell carcinoma (disease)", "renal cell carcinoma associated with neuroblastoma", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "unclassified renal cell carcinoma", "renal pelvis carcinoma", "clear cell renal carcinoma", "childhood kidney cell carcinoma", "renal carcinoma", "angiolipoma", "familial spontaneous pneumothorax"]
---

# Vandetanib
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Vandetanib: From Thyroid Gland Carcinoma to Renal Cell Carcinoma

## One-Sentence Summary

Vandetanib is an oral multi-kinase inhibitor originally used for thyroid gland carcinoma (in the literature, advanced medullary thyroid cancer).
The TxGNN model predicts it may be effective for **renal cell carcinoma**,
with **4 clinical trials** (all Phase 1/2 or Phase 2, two terminated early with very small enrollment) and **5 publications** currently linked to this direction. The publications are mostly reviews and preclinical work, and none shows vandetanib efficacy in renal cell carcinoma.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Thyroid gland carcinoma (the license record has no indication text; this comes from the knowledge graph) |
| Predicted New Indication | Renal cell carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Vandetanib inhibits the VEGFR2, EGFR and RET tyrosine kinases. Detailed mechanism of action data is not available in the data compiled for this report, so the following relies on the known kinase targets.

In clear cell renal cell carcinoma, loss of the VHL gene stabilizes HIF and drives VEGF-dependent angiogenesis. Vandetanib's VEGFR2 inhibition acts directly on this pathway. Approved VEGFR inhibitors such as sunitinib and pazopanib have already validated the pathway in this cancer. Rarer subtypes (HLRCC/FH-deficient and SDH-deficient) may also respond to anti-angiogenic plus EGFR-targeted therapy.

The link between thyroid carcinoma and kidney cancer is therefore pathway-based: both are treated with kinase inhibitors that block angiogenic signalling. The evidence is still early. The Phase 2 trials are small or were stopped early, and no efficacy results are provided.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | Completed | 37 | Vandetanib in Von Hippel-Lindau disease with renal tumors. Directly aligned with the VEGF/HIF mechanism; no outcome data available |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | Terminated | 3 | Vandetanib in advanced clear cell renal carcinoma. Stopped after 3 patients, so no interpretable efficacy |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | Terminated | 7 | Vandetanib plus metformin in HLRCC/SDH-associated kidney cancer or sporadic papillary RCC. Hypothesis-generating only |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | Completed | 82 | Carboplatin and gemcitabine with or without vandetanib in advanced urothelial cancer. Indirect relevance to RCC |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clin Exp Metastasis | Targeted therapy combinations under evaluation in metastatic fumarate hydratase-deficient RCC; no standard regimen yet |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | ASCO Educ Book | Systemic therapy for advanced thyroid cancers, including vandetanib as a RET inhibitor in medullary thyroid cancer |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review | OncoTargets Ther | Overview of antiangiogenic agents (including vandetanib) in solid tumors |
| [42107510](https://pubmed.ncbi.nlm.nih.gov/42107510/) | 2026 | Review | Pharmacol Res | RET kinase inhibitors in RET-driven thyroid and lung cancer |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclinical (mouse model) | Mol Cancer Res | TFE3 translocation RCC mouse model that identifies new therapeutic targets and a diagnostic marker |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 38486 | Caprelsa Tablet (AstraZeneca) | Bottle of 30 tablets (oral) | Indication text not provided |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; the contraindication associations below suggest monitoring of QT interval, blood pressure, thyroid function, electrolytes (potassium, calcium), and renal function |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

**Knowledge-graph contraindication associations** (these come from the TxGNN knowledge graph, not from label text):
- Cardiovascular: hypertension, long QT syndrome (including familial), torsades de pointes, congestive heart failure
- Endocrine and metabolic: hypothyroidism, myxedema, congenital hypothyroidism, potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disorders
- Renal, pulmonary, and neurological: impaired renal function, interstitial lung disease, brain ischemia, transient ischemic attack, posterior leukoencephalopathy syndrome

**Drug Interactions:** 296 interactions were identified. Major-level interactions among those reviewed include:
- Clarithromycin
- Levofloxacin
- Dolasetron
- Palonosetron
- Picosulfuric acid
- Polyethylene glycol (3350 with electrolytes)
- Sodium sulfate

Moderate-level examples are famotidine, metformin, loperamide, dexamethasone, bisacodyl and lactitol. Several of the major interactions involve QT-prolonging or electrolyte-altering drugs, which is consistent with the long QT associations above.

**Class-level safety literature** on VEGFR inhibitors reports hepatotoxicity, proteinuria, and treatment-related mortality. Long-term vandetanib safety data come from medullary thyroid cancer, not RCC.

Package insert warnings and contraindications for the Indian product were not available in the data compiled for this report, so please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible and the drug is already marketed in India, but the RCC-specific evidence is thin. Two of the four trials were terminated with 3 and 7 patients, and the completed VHL trial has no results available. The literature does not show vandetanib efficacy in RCC. The Indian package insert safety data are also missing, which blocks safety screening. This is best treated as a research question rather than a candidate for clinical use. The other predicted indications (for example, renal pelvis carcinoma, pediatric kidney carcinoma, and familial spontaneous pneumothorax) have only indirect or no supporting evidence.

**To proceed, the following is needed:**
- Results of the completed VHL disease trial (NCT00566995)
- Package insert warnings and contraindications for Caprelsa in India
- Detailed mechanism of action data
- A safety plan covering QT prolongation, hypertension, and drug interactions
- Evidence for a specific RCC subtype (for example, VHL-associated or FH/SDH-deficient) before any larger trial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

