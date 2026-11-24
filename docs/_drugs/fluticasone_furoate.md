---
layout: default
title: Fluticasone Furoate
parent: Model Prediction Only (L5)
nav_order: 374
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-24
description: "Fluticasone Furoate: predicted new indication Atopic eczema (evidence level L5). Approved use: Asthma, allergic asthma, intrinsic asthma, allergic rhinitis…"
monitor_inn: "Fluticasone furoate"
predicted_indications: ["atopic eczema", "bronchitis", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "contact dermatitis", "occupational dermatitis", "phototoxic dermatitis"]
---

# Fluticasone Furoate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Fluticasone Furoate: From Asthma and Allergic Rhinitis to Atopic Eczema
{: .text-alpha }

## One-Sentence Summary

Fluticasone furoate is an intranasal and inhaled corticosteroid, originally used to treat asthma and allergic rhinitis.
The TxGNN model predicts it may be effective for **atopic eczema**, but there are **no registered clinical trials** and **2 publications** that only touch on the topic indirectly (one on adrenal suppression with intranasal steroids, one immunotherapy case report). This is a model-only prediction with very limited direct support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, allergic asthma, intrinsic asthma, allergic rhinitis, vasomotor rhinitis |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for fluticasone furoate: "Fluticasone furoate is a synthetic trifluorinated corticosteroid with anti-inflammatory activity. Fluticasone furoate has been shown in vitro to exhibit a binding affinity for the human glucocorticoid receptor that is approximately 29.9 times that of dexamethasone and 1.7 times that of fluticasone propionate." ([DailyMed: Fluticasone Furoate Ellipta (fluticasone furoate) prescribing information, Prasco Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d3e797fc-2636-49a0-b89e-5246b18ee440), label version 2025-03-06; accessed 2026-11-19.) Based on known pharmacology, fluticasone furoate is a potent glucocorticoid receptor agonist with anti-inflammatory and immunosuppressive effects. Its efficacy in allergic airway disease (asthma and allergic rhinitis) is established.

Atopic eczema, asthma and allergic rhinitis are all allergic (atopic) conditions that often occur together. Topical corticosteroids are standard therapy for atopic eczema, so a class-level rationale exists.

The main limitation is formulation. Fluticasone furoate is developed for intranasal and inhaled delivery, and no dermal formulation or skin trial is supported by the data. The prediction therefore rests on class-level reasoning rather than drug-specific evidence.

### Other predicted indications

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Bronchitis | 0.9989 | L5 | The most evidence-supported alternative. Indirect evidence from COPD, chronic cough and asthma studies; phenotype and drug-specific contribution unclear |
| 2-Hydroxyethyl methacrylate sensitization | 0.9987 | L5 | Score only, no studies |
| Dermatitis, atopic | 0.9981 | L5 | Duplicate of atopic eczema; consider merging |
| Contact dermatitis | 0.9946 | L5 | Class-level rationale only |
| Occupational dermatitis | 0.9933 | L5 | Computational prediction only |
| Phototoxic dermatitis | 0.9912 | L5 | Computational prediction only |

## Clinical Trial Evidence

Currently no related clinical trials registered for atopic eczema.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19571596](https://pubmed.ncbi.nlm.nih.gov/19571596/) | 2009 | Review | Neuroimmunomodulation | Reviews adrenal suppression with intranasal corticosteroids in allergic rhinitis, which often coexists with asthma and atopic dermatitis. This is a safety topic and does not test the drug in eczema |
| [40066386](https://pubmed.ncbi.nlm.nih.gov/40066386/) | 2025 | Case report | Indian J Otolaryngol Head Neck Surg | Allergen immunotherapy in a patient with autoimmune disease. It does not test fluticasone furoate in eczema |

## India Market Information

Twenty single-ingredient registrations are valid in India, all nasal sprays; none are cancelled. The data compiled for this report do not include approved indication text.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 5449 | Aramol-F 2 Nasal Spray | Bottle of 120 MDI Nasal Spray | Valid |
| 72535 | Ezicas F 360 Nasal Spray | Bottle of 16 gm Nasal Spray | Valid |
| 84092 | Furamist Nasal Spray | Bottle of 6 gm Nasal Spray | Valid |
| 84258 | Flutiways AZ Nasal Spray | Pump bottle of 70 MDI Nasal Spray | Valid |
| 84752 | Fluoren Nasal Spray | Bottle of 120 MDI Nasal Spray | Valid |
| 85196 | Flution-F Nasal Spray | Bottle of 120 MDI Nasal Spray | Valid |
| 86054 | Furasan Nasal Spray | Bottle of 10 ml Nasal Spray | Valid |
| 86420 | Flyzone-FT Nasal Spray | Pump bottle of 12 ml Nasal Spray | Valid |
| 87090 | Flocare 27.5mcg Nasal Spray | Bottle of 6 gm Nasal Spray | Valid |
| 87998 | FT For 27.5mcg Nasal Spray | Bottle of 1 Nasal Spray | Valid |
| 89142 | Flovetol FT Nasal Spray | Bottle of 6 gm Nasal Spray | Valid |
| 89574 | Flospray 50mcg Nasal Spray | Bottle of 10 ml Nasal Spray | Valid |
| 108857 | Innomist-F 27.5mcg Nasal Spray | Bottle of 120 MDI Nasal Spray | Valid |
| 152092 | Nozispray Nasal Spray | Pump bottle of 120 MDI Nasal Spray | Valid |
| 162387 | Odnase Nasal Spray | Bottle of 6 gm Nasal Spray | Valid |
| 162797 | Orpa Nasal Spray | Bottle of 120 MDI Nasal Spray | Valid |
| 186895 | Ryno Nasal Spray | Bottle of 120 MDI Nasal Spray | Valid |
| 187637 | Rinomist-FP Nasal Spray | Bottle of 100 MDI Nasal Spray | Valid |
| 200078 | Spiroflut Nasal Spray | Bottle of 6 gm Nasal Spray | Valid |
| 200258 | Spiroflut A Nasal Spray | Packet of 7 ml Nasal Spray | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text)**: measles, herpes simplex virus keratitis, adrenocortical insufficiency, Addison disease, varicella zoster infection, fungal infectious disease, dermatophytosis, pulmonary tuberculosis, ocular hypertension, glaucoma, parasitic infection, infectious disease, lower respiratory tract disease, paranasal sinus disease, nasal cavity disease, upper respiratory tract disease, adrenal gland hyperfunction, Cushing syndrome.
- **Related literature note**: Intranasal corticosteroids can suppress the hypothalamic-pituitary-adrenal axis (PMID 19571596), which matters if the drug were used over larger skin areas or for long periods.

Please refer to the package insert for full warnings, contraindications and drug interaction information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no clinical trials, the literature does not test the drug in eczema, and there is no dermal formulation. The evidence is class-level reasoning only. Of the predicted indications, bronchitis (L3) has the most supporting evidence and may be worth separate consideration as a research question.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator (currently missing and blocking safety screening)
- Mechanism of action data from DrugBank
- Evidence that fluticasone furoate works in atopic eczema, or a feasible dermal formulation
- Comparison against established topical corticosteroids
- If pursuing bronchitis, a defined phenotype (chronic bronchitis within COPD, eosinophilic bronchitis, or chronic cough) and drug-specific evidence

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Fluticasone Furoate Ellipta (fluticasone furoate) prescribing information, Prasco Laboratories](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d3e797fc-2636-49a0-b89e-5246b18ee440) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

