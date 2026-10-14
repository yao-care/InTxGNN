---
layout: default
title: Mitomycin
parent: Model Prediction Only (L5)
nav_order: 561
evidence_level: L5
indication_count: 10
---

# Mitomycin
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

# Mitomycin: From Pancreatic Adenocarcinoma to Solid Pseudopapillary Carcinoma of the Pancreas

## One-Sentence Summary

Mitomycin is a DNA cross-linking cytotoxic agent, originally used to treat pancreatic adenocarcinoma.
The TxGNN model predicts it may be effective for **solid pseudopapillary carcinoma of the pancreas**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pancreatic adenocarcinoma (the licence records provide no indication text) |
| Predicted New Indication | Solid pseudopapillary carcinoma of the pancreas |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 16 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mitomycin is a cytotoxic DNA cross-linking (alkylating-type) agent. Its use in pancreatic adenocarcinoma is established, and mechanistically it may be applicable to other pancreatic tumours.

The predicted link likely reflects shared pancreatic neoplasm classification rather than disease-specific biology. Solid pseudopapillary neoplasms are usually treated surgically and tend to behave in a low-grade manner, so the value of cytotoxic chemotherapy is uncertain.

Other top-ranked predictions are all pancreatic tumour subtypes with the same score range (99.82%–99.86%):
- **Osteoclastic giant cell tumour of the pancreas** (99.86%): a rare tumour; no supporting evidence.
- **Pancreatic carcinoma with mixed differentiation** (99.85%): a ductal adenocarcinoma component could plausibly respond, but there are no direct data.
- **Pancreatic intraductal papillary-mucinous carcinoma** (99.85%): invasive disease is often treated like ductal adenocarcinoma, which gives only indirect plausibility.
- **Mixed ductal-endocrine carcinoma** (99.85%) and **pancreatic signet ring cell adenocarcinoma** (99.84%): the ductal or adenocarcinoma components overlap with the approved indication, but there are no subtype-specific data.
- **Malignant exocrine pancreas neoplasm** (99.84%): largely a parent term for the existing indication, so it adds little new repurposing information.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was retrieved for the top-ranked prediction. For the lower-ranked predictions, the retrieved papers are only indirectly relevant:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10897253](https://pubmed.ncbi.nlm.nih.gov/10897253/) | 2000 | Review | Strahlenther Onkol | Adjuvant and neoadjuvant radiochemotherapy in ductal pancreatic carcinoma. Relevant to the approved indication, not to IPMN specifically |
| [8361472](https://pubmed.ncbi.nlm.nih.gov/8361472/) | 1993 | Clinical study | Nihon Geka Gakkai Zasshi | Tamoxifen added to immuno-chemotherapy (including mitomycin) after resection of pancreatic carcinoma. Only indirectly relevant |
| [15983445](https://pubmed.ncbi.nlm.nih.gov/15983445/) | 2005 | Case report | Pancreatology | Pseudomyxoma peritonei with a pancreatic IPMN managed with intraperitoneal hyperthermic chemoperfusion. No evidence of mitomycin efficacy in IPMN |
| [2695183](https://pubmed.ncbi.nlm.nih.gov/2695183/) | 1989 | Review | Bull Cancer | General review of unknown primary tumours. Not specific to mitomycin |

## India Market Information

All 16 registrations are valid single-ingredient injections. The licence records contain no approved indication text. Five main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 135815 | Mitomycin 10mg Injection (Biochem Pharmaceutical Industries) | Vial of 1 injection | Not stated |
| 168193 | Oncocin 10mg Injection (Chandra Bhagat Pharma) | Vial of 1 injection | Not stated |
| 135703 | Mitomycin C 2mg Injection (Biochem Pharmaceutical Industries) | Vial of 2 ml injection | Not stated |
| 138509 | Mito 10mg Injection (Neon Laboratories) | Vial of 1 injection | Not stated |
| 140054 | Mitocin 10mg Injection (Cadila Pharmaceuticals) | Vial of 1 injection | Not stated |

All products are injectable, so the dosage form is the same as the original indication.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (DNA cross-linking agent) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. The knowledge graph links the drug to thrombocytopenia, leukopenia and anaemia as contraindicated conditions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count (with platelets), renal function, and cardiac status, based on the conditions flagged in the knowledge graph |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: kidney disease, pyoureter, thrombocytopenia, blood coagulation disease, anaemia (including macrocytic anaemia), leukopenia, haemolytic-uraemic syndrome (including the typical form), congestive heart failure, heart failure, and stomatitis.
- **Drug Interactions**: 193 interactions are recorded. Main ones with a graded severity:
  - Major: deferiprone, samarium (153Sm) lexidronam
  - Moderate: palifermin, strontium chloride Sr-89, fostamatinib
  - Minor: levofloxacin
  - Many others, such as warfarin, dexamethasone, prednisone and ondansetron, have no severity grade assigned.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). There are no clinical trials or directly relevant publications. Solid pseudopapillary neoplasms are usually managed surgically, so the benefit of cytotoxic chemotherapy is doubtful. In addition, the safety profile of mitomycin carries significant haematological, renal and cardiac concerns.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulator (currently missing, and blocking safety screening)
- Detailed mechanism of action data
- Disease-specific clinical or case-series evidence for mitomycin in the predicted pancreatic subtypes
- Review of whether the predicted subtypes are clinically distinct from the already-approved pancreatic adenocarcinoma indication
- A risk-benefit assessment of the haematological, renal and cardiac risks flagged in the knowledge graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

