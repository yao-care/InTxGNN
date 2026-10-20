---
layout: default
title: Trimethoprim
parent: Model Prediction Only (L5)
nav_order: 868
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Trimethoprim: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Urinary tract infection"
monitor_inn: "Trimethoprim"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
---

# Trimethoprim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Trimethoprim: From Urinary Tract Infection to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is an antibacterial drug originally used for urinary tract infections and several other infections, including infectious otitis media, pneumocystosis, shigellosis and conjunctivitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **no clinical trials and no publications** currently support this specific prediction.
A second prediction, conjunctivitis, has **19 publications** but no registered trials. It largely restates an existing use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (the data compiled for this report contain no approved indication text from the India licences; the original indications come from the knowledge graph) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, trimethoprim is a dihydrofolate reductase inhibitor. It blocks bacterial folate synthesis and is active against common bacterial pathogens. It is used in ophthalmic solutions, usually combined with polymyxin B, for bacterial conjunctivitis and blepharoconjunctivitis.

The prediction most likely arises from the closeness of punctate epithelial keratoconjunctivitis to conjunctivitis in the knowledge graph. However, this condition is often viral (e.g., adenoviral) or immune-mediated. An antibacterial mechanism would therefore have limited relevance, and the link is speculative.

For the second prediction, conjunctivitis (score 99.17%), trimethoprim already counts among its original indications. It is therefore not true repurposing. It does show that the drug is supported for bacterial eye infections.

## Clinical Trial Evidence

Currently no related clinical trials registered, for either predicted indication.

## Literature Evidence

No literature was found for punctate epithelial keratoconjunctivitis. The table below covers the most relevant records for the related conjunctivitis prediction. Several other records were mostly veterinary studies, unrelated case reports or reviews, and are omitted.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30007329](https://pubmed.ncbi.nlm.nih.gov/30007329/) | 2018 | Systematic review/Meta-analysis | J Pediatric Infect Dis Soc | Antibiotic treatments, including oral trimethoprim, for neonatal chlamydial conjunctivitis |
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | Multicenter comparative study (design to be verified) | J Pediatr Ophthalmol Strabismus | Polymyxin B/trimethoprim vs 0.5% moxifloxacin ophthalmic solution: speed of clinical efficacy in bacterial conjunctivitis |
| [6204534](https://pubmed.ncbi.nlm.nih.gov/6204534/) | 1984 | Clinical evaluation (design to be verified) | Am J Ophthalmol | Efficacy and safety of trimethoprim-containing ophthalmic solutions (with sulfacetamide and polymyxin B) in bacterial conjunctivitis or blepharitis |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Survey | Clin Ther | Children with acute bacterial conjunctivitis treated with trimethoprim-polymyxin B ophthalmic solution |
| [2418736](https://pubmed.ncbi.nlm.nih.gov/2418736/) | 1985 | Clinical study | Ann Ophthalmol | Trimethoprim-polymyxin B in surface ocular bacterial infections, compared with a multi-component combination |
| [20084257](https://pubmed.ncbi.nlm.nih.gov/20084257/) | 2001 | Review | Paediatr Child Health | Etiology, clinical features and management of acute infectious conjunctivitis in children |
| [16491721](https://pubmed.ncbi.nlm.nih.gov/16491721/) | 2006 | Review | J Pediatr Ophthalmol Strabismus | Controlling contagious bacterial conjunctivitis and limiting transmission |

## India Market Information

The India licences listed no approved indication text. All five are valid single-ingredient oral tablets.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 218088 | Tmp 300mg Tablet | Strip of 10 tablets | Jagsonpal Pharmaceuticals Ltd |
| 25913 | Bacstol 200 Tablet | Strip of 10 tablets | Ipca Laboratories Ltd |
| 116418 | Keno 200mg Tablet | Strip of 10 tablets | Mancare Labs Pvt Ltd |
| 25893 | Bacstol Tablet | Strip of 10 tablets | Ipca Laboratories Ltd |
| 138103 | Metstol 100mg Tablet | Strip of 10 tablets | Renauxe Pharma India Pvt Ltd |

No ophthalmic formulation is registered among these licences, so route compatibility with an eye indication is unconfirmed.

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text):** inherited porphyria and other porphyrias, kidney disease, liver disease, thrombocytopenia, neutropenia, agranulocytosis, G6PD deficiency, folic acid deficiency anaemia, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, gallbladder disease, glycogen storage disease, cystinuria, galactosemia and pyoureter.
- **Drug Interactions:** 106 interactions were identified.
  - Major: potassium citrate, potassium bicarbonate, potassium chloride and potassium gluconate. These raise a risk of hyperkalaemia.
  - Moderate: metformin, pioglitazone, rosiglitazone, repaglinide, balsalazide, picosulfuric acid and sapropterin.
  - Several others have an unclassified severity.

Please refer to the package insert for label warnings, as these were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for punctate epithelial keratoconjunctivitis is very high, but there are no trials or publications for it. The likely cause of the condition (viral or immune-mediated) also makes an antibacterial effect doubtful. The conjunctivitis prediction has supporting literature (L3), but it is an existing indication rather than a new one.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from India sources (currently a blocking gap for safety screening)
- Confirmed mechanism-of-action data from DrugBank
- Targeted literature and trial searches for punctate epithelial keratoconjunctivitis, including its causes (bacterial vs viral)
- Verification of the design and results of the two ophthalmic solution studies (PMIDs 19043945 and 6204534)
- Assessment of ophthalmic formulation availability, since the registered products are oral tablets only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

