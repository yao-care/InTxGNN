---
layout: default
title: Guaifenesin
parent: Model Prediction Only (L5)
nav_order: 404
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "Guaifenesin"
predicted_indications: ["nasal cavity disease", "faucial diphtheria", "cervical disc degenerative disorder", "papillary conjunctivitis"]
description: "Guaifenesin: predicted new indication Nasal cavity disease (evidence level L5). In India: at least 20 listed products"
---

# Guaifenesin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Guaifenesin: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Guaifenesin is an expectorant that is mainly used for upper respiratory conditions such as rhinitis, pharyngitis and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**,
but the evidence is thin: **no clinical trials** and only **1 publication** (a review) were found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of guaifenesin as: Unknown ([ChEMBL CHEMBL980 (guaifenesin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL980), CC BY-SA 3.0; accessed 2026-11-19.) Based on known information, guaifenesin is an expectorant that thins and loosens airway mucus. Its efficacy in rhinitis and related upper airway conditions is already recognised, and mechanistically it may be applicable to nasal cavity disease.

Nasal cavity disease is a broader category that includes the rhinitis conditions guaifenesin is already linked to. The plausible link is improved clearance of nasal and sinus secretions. This link is inferred and not confirmed.

The very high TxGNN score (0.9998) is a computational prediction. It probably reflects the overlap with existing rhinitis indications rather than independent evidence of a new benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12487405](https://pubmed.ncbi.nlm.nih.gov/12487405/) | 2002 | Review | Logopedics, Phoniatrics, Vocology | Treatment strategies for hidden respiratory allergies in voice users; decongestants containing guaifenesin may be useful, while antihistamines are generally avoided |

This is a single review focused on voice users. It offers only indirect support and does not test guaifenesin in nasal cavity disease.

## India Market Information

Guaifenesin has 20 valid single-ingredient registrations in India and none are cancelled. The registration records do not include approved indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 8391 | Asta Q 50mg/1.25mg/4mg Syrup | Bottle of 100 ml Syrup | Valid |
| 12594 | Alpacoff Syrup | Bottle of 100 ml Syrup | Valid |
| 26008 | Broncorex Expectorant | Bottle of 100 ml Syrup | Valid |
| 28269 | Broxyl-AP Syrup | Bottle of 60 ml Syrup | Valid |
| 30353 | Bro Surex Syrup | Bottle of 100 ml Syrup | Valid |
| 35090 | Coscoril Syrup | Bottle of 100 ml Syrup | Valid |
| 37455 | Coughex Tablet | Strip of 15 tablets | Valid |
| 42361 | Cofrest BM Syrup | Bottle of 100 ml Syrup | Valid |
| 46005 | Cecoril Syrup | Bottle of 100 ml Syrup | Valid |
| 46411 | Cinkof Syrup | Bottle of 100 ml Syrup | Valid |
| 50220 | Crf D Tablet | Strip of 10 tablets | Valid |
| 51526 | Carion X 50 mg/1.25 mg/4 mg Syrup | Bottle of 100 ml Syrup | Valid |
| 52663 | Chestorex Tablet | Strip of 10 tablets | Valid |
| 74196 | Expal Tablet | Strip of 10 tablets | Valid |
| 75826 | Ex-Dmr Tablet | Strip of 10 tablets | Valid |
| 115883 | Kuftive 100mg/8mg/2mg/10mg Tablet | Strip of 10 tablets | Valid |
| 157533 | Nextup Plus 100mg/10mg/2mg Capsule | Strip of 10 capsules | Valid |
| 176224 | Prodexa Tablet | Strip of 10 tablets | Valid |
| 220493 | Tusril Syrup | Bottle of 110 ml Syrup | Valid |
| 247511 | Z Cof Syrup | Bottle of 100 ml Syrup | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

Available forms include tablets, capsules and syrups.

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text):** The drug–disease contraindication links in the knowledge graph include hypertension, liver failure and liver disease, cirrhosis, kidney disease, epilepsy, COPD, peptic and gastric ulcer, inflammatory bowel disease, pancreatitis, porphyria, thrombocytopenia, adrenocortical insufficiency (Addison disease), hypothyroidism, anxiety and psychotic disorders, and insomnia. These links may partly reflect combination products and should be checked against the actual package insert.
- **Drug interactions:** No interaction records were found.

Please refer to the package insert for confirmed warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it likely reflects overlap with existing rhinitis indications. There are no clinical trials, only one indirect review, and the mechanism data are missing, so the evidence does not yet support a new indication.

**To proceed, the following is needed:**
- Mechanism of action data for guaifenesin
- Package insert warnings and contraindications for the India products, which are required before safety screening
- Clinical studies of guaifenesin in nasal cavity disease, or a clear definition of how this differs from the existing rhinitis indications
- Review of the knowledge-graph contraindication signals against the label

### Other Predicted Indications (Not Recommended for Now)

All have no trials or literature and are rated L5 (model prediction only):

| Predicted Indication | TxGNN Score | Comment |
|------|------|------|
| Faucial diphtheria | 0.9954 | Treatment relies on antitoxin and antibiotics; guaifenesin has no such activity (Hold) |
| Cervical disc degenerative disorder | 0.9950 | No clear mechanistic link (Hold) |
| Papillary conjunctivitis | 0.9927 | Tenuous link through allergy only; no ocular mechanism (Hold) |

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL980 (guaifenesin): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL980) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

