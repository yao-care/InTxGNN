---
layout: default
title: Imatinib
parent: 僅模型預測 (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
---

# Imatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Imatinib: From Chronic Myeloid Leukaemia to Heart Fibrosarcoma

## One-Sentence Summary

Imatinib (Gleevec/Glivec) is a selective tyrosine kinase inhibitor originally developed for chronic myeloid leukaemia (CML) and gastrointestinal stromal tumours (GIST), acting by blocking BCR-ABL, c-KIT, and PDGFR-α/β kinase activity.
The TxGNN model predicts it may have activity against **Heart Fibrosarcoma** with a prediction score of 99.94%; however, only **1 general publication** — a 2008 editorial whose title explicitly states "not robust evidence" — currently exists in this direction, representing the lowest-actionable evidence tier.
The high model score almost certainly reflects generalisation from mechanistically related fibrosarcoma subtypes (e.g. DFSP, where imatinib is already an FDA/EMA-approved treatment) rather than disease-specific evidence for this rare cardiac entity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Myeloid Leukaemia (CML) / Gastrointestinal Stromal Tumour (GIST) — inferred from literature; India regulatory records not yet loaded in system |
| Predicted New Indication | Heart Fibrosarcoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| India Market Status | Not marketed (data gap — CDSCO records not available in system) |
| Number of Registrations | 0 (data gap) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Imatinib is a small-molecule inhibitor that selectively targets three tyrosine kinases: BCR-ABL (the driving fusion oncogene in Philadelphia chromosome-positive CML), c-KIT (mutated in GIST, systemic mastocytosis, and other tumours), and PDGFR-α/β (platelet-derived growth factor receptors). These three targets share a conserved ATP-binding pocket, which imatinib occupies to block downstream proliferative signalling. Its remarkable efficacy in CML and GIST established the concept of oncogene-targeted therapy, and the same PDGFR-β inhibitory mechanism later supported FDA (2006) and EMA approval for dermatofibrosarcoma protuberans (DFSP), a fibroblastic tumour driven by the COL1A1-PDGFB fusion gene.

Currently, detailed mechanism of action data is not available in this evidence pack (Data Gap DG002). Based on established pharmacology, imatinib's anti-PDGFR-β activity is the most plausible rationale for its predicted efficacy in fibrosarcoma-type tumours. Some fibrosarcomas do express PDGFR-α/β at varying levels, providing a theoretical basis for tyrosine kinase inhibition. The TxGNN knowledge graph model likely inferred this connection by traversing the PDGFR pathway nodes linking imatinib's known activity to fibroblastic neoplasm disease nodes.

In practice, however, heart fibrosarcoma is an ultra-rare primary cardiac malignancy (annual incidence estimated below 1 per million), and no molecular profiling studies have characterised PDGFR expression levels or driving mutations in this specific tumour type. The single retrieved publication is a general editorial reviewing imatinib's expanding indications across multiple disease areas — it contains no data specific to cardiac fibrosarcoma. The model's prediction here is best understood as extrapolation from better-characterised fibroblastic tumours rather than a disease-specific signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Heart Fibrosarcoma and Imatinib.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Editorial/Commentary | Prescrire International | General review of imatinib's expanding indications, including Ph+ ALL and beyond CML/GIST. The article's own title notes "not robust evidence" for newer indications. No data specific to heart fibrosarcoma. Cited here as the sole retrieved publication; does not constitute targeted support for this indication. |

---

## Cytotoxicity

Imatinib is a targeted antineoplastic agent (TKI) used for haematological and solid tumour malignancies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Tyrosine kinase inhibitor (BCR-ABL / c-KIT / PDGFR class); not a conventional cytotoxic agent |
| Myelosuppression Risk | Moderate — neutropenia and thrombocytopenia are among the most frequent adverse effects, particularly during the initial months of treatment; severe myelosuppression (Grade 3–4) reported in 10–30% of CML patients |
| Emetogenicity Classification | Low to moderate (oral tablet formulation; nausea common but typically manageable with food intake) |
| Monitoring Items | CBC with differential (every 2 weeks for first 3 months, then monthly or as clinically indicated); liver function tests (ALT, AST, bilirubin — monthly for first 3 months); renal function; weight and fluid retention assessment |
| Handling Protection | Standard cytotoxic handling precautions apply for oral formulation — avoid crushing tablets; wear gloves when handling damaged tablets; follow institutional cytotoxic drug disposal protocols |

---

## Safety Considerations

- **Drug Interactions**: 675 total documented interactions (DDInter database). Selected clinically important interactions:
  - **Major — Eliglustat**: Imatinib is a CYP3A4 inhibitor; co-administration markedly increases eliglustat exposure, risking QT prolongation and cardiac arrhythmia. Avoid concurrent use.
  - **Major — Naloxegol**: Imatinib inhibits CYP3A4-mediated naloxegol metabolism, substantially increasing opioid receptor antagonist levels. Avoid concurrent use or reduce naloxegol dose with close monitoring.
  - **Moderate — CYP3A4 inhibitors (Clarithromycin, Aprepitant)**: May increase imatinib plasma concentrations; monitor for imatinib toxicity (fluid retention, myelosuppression, hepatotoxicity).
  - **Moderate — CYP3A4 inducers (Dexamethasone, Budesonide, Triamcinolone, Betamethasone, Hydrocortisone)**: May reduce imatinib exposure and diminish efficacy; consider dose adjustment.
  - **Moderate — CYP2C8/3A4 substrates (Pioglitazone, Glimepiride, Saxagliptin)**: Imatinib inhibits CYP2C8, potentially increasing exposure and hypoglycaemic risk; monitor blood glucose closely.
  - **Moderate — Opioid-related agents (Morphine, Naltrexone, Naldemedine)**: Pharmacokinetic and/or pharmacodynamic interactions; clinical significance varies — assess case by case.

Please refer to the package insert for complete warnings and contraindications, including cardiac monitoring requirements, hepatotoxicity precautions, and pregnancy/reproductive toxicity.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Heart fibrosarcoma is an ultra-rare disease (< 1 per million per year) with no published molecular profiling to confirm PDGFR expression or other imatinib-sensitive driver alterations, and the sole retrieved publication is a general 2008 editorial that explicitly acknowledges a lack of robust evidence — it does not address cardiac fibrosarcoma in any specific way. Advancing this indication without foundational molecular and preclinical data would not be scientifically defensible.

**To proceed, the following is needed:**
- Molecular profiling of heart fibrosarcoma specimens for PDGFR-α/β expression (IHC and/or gene fusion analysis) to establish a mechanistic rationale
- Retrieval and review of imatinib's complete MOA profile from DrugBank (Data Gap DG002) to enable proper mechanistic analysis
- Verification of Imatinib's CDSCO registration and package insert review (Data Gap DG001, currently Blocking) for India-specific regulatory and safety assessment
- Case reports or preclinical studies specifically investigating imatinib activity in primary cardiac sarcomas
- Consultation of basket trial registries (e.g. NCT00154388 and similar designs) to determine whether cardiac fibrosarcoma patients with confirmed imatinib-sensitive targets may qualify for enrolment
- If molecular characterisation reveals PDGFR activation, reclassification of this prediction and re-evaluation under the fibroblastic neoplasm (Rank 2, Evidence Level L2, **Proceed with Guardrails**) pathway, where the evidence base is considerably stronger and FDA/EMA approval for the DFSP subtype already exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

