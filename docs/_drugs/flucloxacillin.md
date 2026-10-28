---
layout: default
title: Flucloxacillin
parent: Model Prediction Only (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Flucloxacillin: predicted new indication Conjunctivitis (evidence level L4). Approved use: Not stated in the available licence data (anti-staphylococcal antibac…"
monitor_inn: "Flucloxacillin"
predicted_indications: ["conjunctivitis", "rheumatoid arthritis", "leprosy", "Prinzmetal angina", "conjunctivitis (disease)", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "thrombotic disease", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis"]
---

# Flucloxacillin
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

## Flucloxacillin: From Staphylococcal Infections to Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Flucloxacillin is an anti-staphylococcal penicillin antibiotic, marketed in India in injectable and oral forms.
The TxGNN model predicts it may be effective for **conjunctivitis**, but **no clinical trials** and only **1 publication** (a case report on a different pathogen) are available, so the prediction is essentially unsupported by clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data (anti-staphylococcal antibacterial use) |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 7 of 7) |
| Number of Registrations | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, flucloxacillin is a penicillinase-resistant penicillin, a class that acts against susceptible Gram-positive bacteria, particularly *Staphylococcus aureus*. Mechanistically it may be applicable to bacterial conjunctivitis caused by susceptible Gram-positive organisms.

However, the only retrieved publication concerns gonococcal dacryoadenitis, which involves a different pathogen (*Neisseria gonorrhoeae*) and a different site (the lacrimal gland). It does not support flucloxacillin use. The high model score is therefore not backed by clinical evidence. A second, duplicate ontology entry ("conjunctivitis (disease)", score 0.9969) rests on the same single case report and should be considered together with this one.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41884366](https://pubmed.ncbi.nlm.nih.gov/41884366/) | 2026 | Case report | Case Reports in Ophthalmology | Gonococcal dacryoadenitis, a rare lacrimal gland involvement in *N. gonorrhoeae* conjunctivitis; not relevant to flucloxacillin efficacy |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 202133 | Staphonex Injection | Vial of 1 injection | Not listed |
| 88197 | Flulen Injection | Vial of 1 injection | Not listed |
| 201576 | Staphonex Injection | Vial of 1 injection | Not listed |
| 203436 | Staflowin Injection | Vial of 1 injection | Not listed |
| 203115 | Staflowin 500mg Injection | Vial of 1 injection | Not listed |

Two further registrations exist (7 in total): Staphonex 500mg Capsule (200101, strip of 4 capsules) and Stafocid 1G Injection (202440, vial of 1 injection). All 7 are valid single-ingredient products. Available routes are injectable and oral.

## Safety Considerations

No drug interaction records were found for flucloxacillin in the data compiled for this report. Please refer to the package insert for safety information.

Other predicted indications surfaced safety signals in the literature that are worth noting: case reports describe agranulocytosis with long-term flucloxacillin use and a fatal Stevens-Johnson syndrome/toxic epidermal necrolysis case in which flucloxacillin or doxycycline was suspected. One small study in rheumatoid arthritis patients found no clinically significant pharmacokinetic interaction between flucloxacillin and methotrexate.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, since no trials exist and the single publication concerns a different pathogen and site. A plausible antibacterial rationale exists for susceptible Gram-positive conjunctivitis, but it is unproven here, and other conjunctivitis therapies are already established.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently blocking safety screening)
- Approved indication text for the registered products
- Mechanism of action data from DrugBank
- Clinical or microbiological evidence for flucloxacillin in Gram-positive bacterial conjunctivitis, including ocular penetration data and route suitability (the available formulations are oral and injectable, not ophthalmic)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

