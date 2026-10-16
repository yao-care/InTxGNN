---
layout: default
title: Dexchlorpheniramine
parent: Moderate Evidence (L3-L4)
nav_order: 250
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-14
description: "Dexchlorpheniramine: predicted new indication Allergic urticaria (evidence level L4). Approved use: Allergic rhinitis, vasomotor rhinitis, allergic conjunctivitis…"
monitor_inn: "Dexchlorpheniramine"
predicted_indications: ["allergic urticaria", "cold urticaria"]
---

# Dexchlorpheniramine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Dexchlorpheniramine: From Allergic Rhinitis and Urticaria to Allergic Urticaria

## One-Sentence Summary

Dexchlorpheniramine is a first-generation H1 antihistamine, originally used for allergic rhinitis, allergic conjunctivitis, urticaria and angioedema.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, but there are **no registered clinical trials** and only **3 publications**, none of which is a clinical efficacy trial in urticaria patients.
Allergic urticaria is largely a subtype of an indication the drug already covers, so this is a weak repurposing signal rather than a new-use discovery.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, allergic conjunctivitis, urticaria, angioedema (from the knowledge graph; no approved indication text is available for the Indian licences) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dexchlorpheniramine is a first-generation H1 antihistamine, its use in allergic conditions is established, and mechanistically it may be applicable to allergic urticaria.

Allergic urticaria is driven by histamine released from mast cells, which is the pathway H1 antagonists block. Urticaria and angioedema are already among the drug's known indications. The prediction is therefore biologically consistent, but it mostly restates an existing use.

A second predicted condition, **cold urticaria** (score 99.61%), is a physical urticaria that also involves mast cell degranulation and histamine release, so H1 blockade is plausible. However, no trials or literature specific to this drug were found. It is supported only by the model score and class-level reasoning (evidence level L5, Hold).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | Randomised phase I trial (pharmacodynamic) | Eur J Pharm Sci | Compared oral bilastine, parenteral dexchlorpheniramine and a new parenteral bilastine formulation for inhibition of the histamine-induced wheal and flare response; dexchlorpheniramine was the comparator |
| [29723372](https://pubmed.ncbi.nlm.nih.gov/29723372/) | 2018 | Pharmacodynamic study | An Bras Dermatol | Compared suppression of the histamine wheal and flare by the main H1 antihistamines marketed in Brazil |
| [39803](https://pubmed.ncbi.nlm.nih.gov/39803/) | 1979 | Case report | Dermatologica | Clinical and immunological study of one patient with acquired heat contact urticaria; the drug's specific role is not confirmed |

The first two papers use a histamine skin-test model, not patients with urticaria, so they offer only indirect support.

---

## India Market Information

The 20 valid single-ingredient registrations are all oral tablets (plain and sustained-release). Approved indication text is not available for any of them. Five examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 63240 | Dexer 2mg Tablet | Strip of 10 tablets | Not available |
| 174781 | Polamin 2mg Tablet | Strip of 10 tablets | Not available |
| 59693 | Dexodil 2mg Tablet | Strip of 10 tablets | Not available |
| 64312 | Dexgen 6mg Tablet SR | Strip of 10 tablets (SR) | Not available |
| 173658 | Polaramine 2mg Tablet | Strip of 10 tablets | Not available |

---

## Safety Considerations

Label warnings, contraindications and drug interaction data are not available, so please refer to the package insert for safety information.

The knowledge graph links the drug to contraindications in the following conditions. These come from graph relationships, not label text, and should be checked against the label:
- **Cardiovascular:** hypertension, hypotension, coronary artery disease, myocardial infarction, coronary atherosclerosis
- **Hepatic, renal and gastrointestinal:** liver disease and failure, kidney disease, pancreatitis, gallbladder disease, peptic or gastric ulcer, inflammatory bowel disease, *Clostridium difficile* colitis
- **Endocrine:** hypothyroidism, diabetes mellitus, diabetic ketoacidosis
- **Other:** epilepsy, benign prostatic hyperplasia, ocular hypertension, substance abuse/dependence, hemoglobinopathy

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Allergic urticaria falls under the drug's existing urticaria indication, and the available papers are histamine skin-test studies, not efficacy trials in patients. The prediction is plausible but adds little beyond current use, and the safety data needed for screening are missing.

**To proceed, the following is needed:**
- The package insert for the Indian products (warnings, contraindications, approved indications), which is currently a blocking gap
- Mechanism of action data from DrugBank
- Clinical efficacy data in patients with allergic urticaria and, separately, cold urticaria
- Confirmation that the knowledge-graph contraindications match label content
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

