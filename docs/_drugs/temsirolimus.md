---
layout: default
title: Temsirolimus
parent: High Evidence (L1-L2)
nav_order: 814
evidence_level: L2
indication_count: 3
last_modified_at: 2026-10-14
description: "Temsirolimus: predicted new indication Liposarcoma (evidence level L2). Approved use: Mantle cell lymphoma, renal cell carcinoma"
---

# Temsirolimus
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **3** 
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

# Temsirolimus: From Mantle Cell Lymphoma and Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Temsirolimus is an mTOR inhibitor originally used to treat renal cell carcinoma and mantle cell lymphoma.
The TxGNN model predicts it may be effective for **liposarcoma**,
with **2 clinical trials** (both in sarcoma populations, not liposarcoma-specific) and **1 publication** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Mantle cell lymphoma, renal cell carcinoma (the approved-indication text in the India licence records is blank, so this comes from the knowledge-graph indication list) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L2 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold (research question; further evidence needed) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the pathway analysis, temsirolimus inhibits mTOR (through the FKBP12 complex), a node downstream of PI3K/AKT signalling. Its efficacy in renal cell carcinoma and mantle cell lymphoma is established, and mechanistically it may be applicable to liposarcoma.

Activation of the mTOR pathway and of IGF-1R/PI3K signalling has been implicated in sarcoma growth, including liposarcoma. Blocking IGF-1R together with mTOR (as with cixutumumab plus temsirolimus) targets the compensatory feedback activation of AKT. Combining temsirolimus with a liposarcoma-active cytotoxic such as liposomal doxorubicin is also plausible.

The high TxGNN score is consistent with this pathway rationale, but it remains a computational prediction. Two other predicted indications, ovarian myxoid liposarcoma (99.47%) and vulva sarcoma (99.09%), have no supporting trials or literature and are likely extrapolations from the same sarcoma-pathway signal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Temsirolimus (Torisel) plus liposomal doxorubicin in recurrent advanced soft tissue and bone sarcomas; aims to identify a safe dose and assess effectiveness. Population is mixed, and liposarcoma-specific results are not confirmed. |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab plus temsirolimus in pediatric patients with recurrent or refractory solid tumours including sarcoma. Limited direct relevance to adult liposarcoma; supports the mTOR/IGF-1R combination rationale only. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du cancer | Review of targeted treatments for rare connective tissue tumours and sarcomas, organised by molecular subgroup. The abstract excerpt available does not describe temsirolimus-specific findings. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 210129 | Sirotem Injection (Celon Laboratories Ltd) | Vial of 1 ml injection | Not stated in the licence record |
| Registration No. 222031 | Torisel Kit (Pfizer Ltd) | Vial of 1 ml injection | Not stated in the licence record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; given the knowledge-graph flags, consider blood glucose, lipids, liver and renal function, bilirubin, and respiratory status |
| Handling Protection | Please refer to the package insert warnings and precautions; follow institutional antineoplastic handling policy |

## Safety Considerations

- **Drug Interactions**: 540 interactions were identified in the interaction databases. Examples of those rated **Major**: amphotericin B (including the lipid complex), dexamethasone, and clarithromycin. Examples rated **Moderate** include hydrocortisone, other corticosteroids (triamcinolone, betamethasone, budesonide), aprepitant, cimetidine, mesalazine, balsalazide, and several antidiabetic drugs (acarbose, metformin, pioglitazone, alogliptin, albiglutide, canagliflozin, dapagliflozin, chlorpropamide).
- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text, so they should be verified against the package insert):
  - Metabolic: hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, hyperlipidaemia (including familial)
  - Organ function: kidney disease, liver disease, gallbladder disease, hyperbilirubinaemia (including Gilbert syndrome), interstitial lung disease
  - Cerebrovascular: stroke, cerebrovascular disorder, cerebral infarction
  - Central nervous system tumours: brain cancer and several astrocytoma, glioblastoma and oligodendroglial tumour types

Package insert warnings and contraindications were not available for this report; please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Temsirolimus has a plausible mTOR/PI3K pathway rationale for liposarcoma and a very high model score. However, the only supporting trials are a small mixed-sarcoma Phase 1/2 study and a paediatric Phase 2 study, with no liposarcoma-specific efficacy data and no confirmatory trials. The package insert safety review is also incomplete, so the case is best treated as a research question rather than a candidate for advancement.

**To proceed, the following is needed:**
- Liposarcoma-specific results (subgroup data) from NCT00949325 and related sarcoma studies
- Package insert warnings and contraindications from the India licence holders, to complete safety screening
- Detailed mechanism of action data
- A review of the knowledge-graph contraindication signals (metabolic, hepatic, pulmonary, cerebrovascular) against label text, and a drug-interaction management plan (especially with dexamethasone, clarithromycin, and amphotericin B)
- Preclinical or translational evidence of mTOR pathway dependence in liposarcoma subtypes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

