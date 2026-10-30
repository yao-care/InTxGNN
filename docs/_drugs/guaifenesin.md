---
layout: default
title: Guaifenesin
parent: Model Prediction Only (L5)
nav_order: 404
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
monitor_inn: "Guaifenesin"
predicted_indications: ["nasal cavity disease", "faucial diphtheria", "cervical disc degenerative disorder", "papillary conjunctivitis"]
description: "Guaifenesin: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
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
| Number of Listed Products | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, guaifenesin is an expectorant that thins and loosens airway mucus. Its efficacy in rhinitis and related upper airway conditions is already recognised, and mechanistically it may be applicable to nasal cavity disease.

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

Guaifenesin has 20 valid single-ingredient registrations in India and none are cancelled. The registration records do not include approved indication text. Five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 52663 | Chestorex Tablet | Strip of 10 tablets | Not stated in the registration record |
| Registration No. 30353 | Bro Surex Syrup | Bottle of 100 ml syrup | Not stated in the registration record |
| Registration No. 247511 | Z Cof Syrup | Bottle of 100 ml syrup | Not stated in the registration record |
| Registration No. 176224 | Prodexa Tablet | Strip of 10 tablets | Not stated in the registration record |
| Registration No. 26008 | Broncorex Expectorant | Bottle of 100 ml syrup | Not stated in the registration record |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

