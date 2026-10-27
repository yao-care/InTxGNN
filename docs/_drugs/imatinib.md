---
layout: default
title: Imatinib
parent: Model Prediction Only (L5)
nav_order: 425
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Imatinib: predicted new indication Heart fibrosarcoma (evidence level L5). Approved use: Not stated in the India licence records (approved indication text is…"
monitor_inn: "Imatinib"
predicted_indications: ["heart fibrosarcoma", "fibroblastic neoplasm", "conventional fibrosarcoma", "kidney fibrosarcoma", "low grade fibromyxoid sarcoma", "liposarcoma", "liver fibrosarcoma", "autosomal recessive familial Mediterranean fever", "ovarian myxoid liposarcoma", "familial rhabdoid tumor"]
---

# Imatinib
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

## Imatinib: From Chronic Myelogenous Leukemia / GIST to Heart Fibrosarcoma
{: .text-alpha }

## One-Sentence Summary

Imatinib is a tyrosine kinase inhibitor originally used for BCR-ABL1-positive chronic myelogenous leukemia, gastrointestinal stromal tumor (GIST), dermatofibrosarcoma protuberans and several related conditions.
The TxGNN model's top-ranked prediction is **heart fibrosarcoma**, but for this specific indication the evidence is very thin: **no clinical trials** and **only 1 publication** (a 2008 commentary), so the prediction rests mainly on the model score.
The more evidence-supported directions among the top 10 predictions are **liposarcoma** (3 Phase 1/2 or Phase 2 trials) and **fibroblastic neoplasm** (largely dermatofibrosarcoma protuberans, which is already an approved use).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India licence records (approved indication text is empty). The knowledge graph lists systemic mastocytosis, GIST, BCR-ABL1-positive CML, chronic eosinophilic leukemia, dermatofibrosarcoma protuberans and hypereosinophilic syndrome |
| Predicted New Indication | Heart fibrosarcoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 (heart fibrosarcoma); L2 for the best-supported alternative, liposarcoma |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on widely known pharmacology, imatinib inhibits the BCR-ABL, KIT and PDGFR tyrosine kinases. Its efficacy in CML and GIST is established, and these kinases drive growth in those diseases.

The link to heart fibrosarcoma is indirect. In dermatofibrosarcoma protuberans (DFSP), a fibroblastic tumour, the COL1A1-PDGFB fusion causes constitutive PDGFR activation, which imatinib blocks. This makes a plausible but unverified connection to fibroblastic sarcomas in general. The only literature linked to heart fibrosarcoma is a 2008 commentary on new imatinib indications, which does not address cardiac tumours directly.

The fit is weaker for several other predicted sarcomas. Conventional fibrosarcoma generally lacks the COL1A1-PDGFB fusion. Liposarcoma is mainly driven by MDM2/CDK4 amplification, low grade fibromyxoid sarcoma by FUS-CREB3L2 fusions, myxoid liposarcoma by FUS-DDIT3 fusions, and rhabdoid tumors by SMARCB1 loss. None of these has an established dependence on imatinib's targets. Any benefit would probably be limited to KIT/PDGFR-positive subsets, so molecular confirmation of target dependence would be essential before extrapolating.

---

## Clinical Trial Evidence

No clinical trials are registered for heart fibrosarcoma. The trials below were retrieved for other top-10 predictions and are relevant only by analogy.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00031915](https://clinicaltrials.gov/study/NCT00031915) | Phase 2 | Completed | Not reported | Imatinib in metastatic or unresectable soft tissue and bone sarcoma (liposarcoma prediction); subtype results not available |
| [NCT00006357](https://clinicaltrials.gov/study/NCT00006357) | Phase 1/2 | Completed | 91 | Dose-finding and efficacy of STI571 (imatinib) in recurrent or refractory soft tissue sarcoma (liposarcoma prediction); no liposarcoma-specific results |
| [NCT00154388](https://clinicaltrials.gov/study/NCT00154388) | Phase 2 | Completed | 185 | Exploratory basket study in life-threatening rare malignancies with imatinib-sensitive kinases (cited for kidney fibrosarcoma and liposarcoma); no organ-specific results |

---

## Literature Evidence

**Heart fibrosarcoma (the top prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Review | Prescrire International | Commentary on new imatinib indications; evidence described as not robust, and not specific to cardiac tumours |

**Supporting literature from related predictions**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/) | 2025 | Guideline | Eur J Cancer | European interdisciplinary guideline update on DFSP diagnosis and treatment |
| [19451433](https://pubmed.ncbi.nlm.nih.gov/19451433/) | 2009 | Phase 2 trial | J Clin Oncol | Multicenter Phase 2 trial of imatinib across 10 sarcoma subtypes using a Bayesian model |
| [42062942](https://pubmed.ncbi.nlm.nih.gov/42062942/) | 2026 | Cohort | BMC Cancer | 153 Chinese DFSP patients; Mohs surgery plus postoperative imatinib |
| [25852058](https://pubmed.ncbi.nlm.nih.gov/25852058/) | 2015 | Preclinical | Mol Cancer Ther | CDKN2A/p16 loss implicates CDK4 as a target in imatinib-resistant DFSP |
| [40558511](https://pubmed.ncbi.nlm.nih.gov/40558511/) | 2025 | Preclinical | Cells | Patient-derived cell line profiling predicts imatinib sensitivity in DFSP |
| [30901500](https://pubmed.ncbi.nlm.nih.gov/30901500/) | 2019 | Preclinical | Drug Dev Res | Imatinib plus dexketoprofen liposomes against fibrosarcoma (weak supporting signal) |
| [12702540](https://pubmed.ncbi.nlm.nih.gov/12702540/) | 2003 | Report | Ann Oncol | Potential use of imatinib in c-KIT-expressing ocular melanoma and liposarcoma |
| [16158966](https://pubmed.ncbi.nlm.nih.gov/16158966/) | 2005 | Study | Anticancer Res | c-kit expression in dedifferentiated and well-differentiated liposarcomas |
| [36999599](https://pubmed.ncbi.nlm.nih.gov/36999599/) | 2023 | Review | J Surg Oncol | Surgical management of DFSP; imatinib used in advanced or unresectable disease |
| [15794712](https://pubmed.ncbi.nlm.nih.gov/15794712/) | 2005 | Review | Expert Opin Drug Saf | Development and application of imatinib |

---

## India Market Information

Imatinib is marketed in India with 20 valid single-ingredient registrations. The approved indication text is not recorded in the licence data. Five representative registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 95895 | Glivec 100mg Tablet (Novartis India Ltd) | Strip of 10 tablets | Not recorded |
| 100962 | Gleevac 100mg Tablet (Novartis India Ltd) | Bottle of 60 tablets | Not recorded |
| 111302 | Imalek 400mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 10 tablets | Not recorded |
| 108048 | Imatib 100 Tablet (Cipla Ltd) | Strip of 10 tablets | Not recorded |
| 111040 | Imatinate 400 Capsule (Khandelwal Laboratories Pvt Ltd) | Bottle of 10 capsules | Not recorded |

All products are oral (tablets or capsules).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (tyrosine kinase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert; the knowledge graph flags thrombocytopenia, neutropenia and agranulocytosis as contraindication-related conditions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC, liver and renal function (suggested given the knowledge graph flags for liver disease, kidney disease and cytopenias) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** liver failure and liver disease, kidney disease, congestive heart failure and heart failure, coronary artery disease, heart valve disease, pericardial effusion, thrombocytopenia, neutropenia, agranulocytosis, anemia, hypertension, pulmonary edema, brain edema, diabetes mellitus, diabetic ketoacidosis, hyperbilirubinemia and Gilbert syndrome, active peptic ulcer disease, hypophosphatemia, obesity, and congenital heart disease. These should be verified against the official package insert.
- **Drug Interactions:** 675 interactions were identified. Major-level examples include **eliglustat** and **naloxegol**. Moderate-level examples include corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), pioglitazone, glimepiride, saxagliptin, aprepitant, morphine, cimetidine, clarithromycin, lansoprazole, dexlansoprazole, naltrexone, naldemedine and metreleptin.
- **Case report signal:** a case of imatinib-induced drug reaction with eosinophilia and systemic symptoms (DRESS) was reported in a DFSP patient, successfully managed with desensitization ([PMID 30096127](https://pubmed.ncbi.nlm.nih.gov/30096127/)).

Given the cardiac-related flags, extra caution applies if the heart is the disease site. Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, heart fibrosarcoma, has no clinical trials and only one indirect commentary (evidence level L4), and the high model score (99.94%) is not corroborated by data. The best-supported alternatives are soft tissue sarcoma subsets (liposarcoma, L2, with Phase 2 trials but no subtype-specific results) and fibroblastic neoplasms driven by PDGFB (DFSP, already an approved use). The remaining predictions (familial Mediterranean fever, ovarian myxoid liposarcoma, familial rhabdoid tumor) are model-only (L5).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap for safety screening)
- Detailed mechanism of action data
- Subtype-level results from the soft tissue sarcoma trials (NCT00031915, NCT00006357, NCT00154388) and the 10-subtype Phase 2 trial (PMID 19451433)
- Molecular confirmation of PDGFR/KIT dependence (e.g., PDGFB rearrangement) in any target tumour type
- A cardiac safety assessment, given the knowledge graph contraindication flags for heart disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

