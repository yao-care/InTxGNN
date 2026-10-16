---
layout: default
title: Dicyclomine
parent: Model Prediction Only (L5)
nav_order: 263
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Dicyclomine: predicted new indication Cauda equina syndrome (evidence level L5). Approved use: Irritable bowel syndrome"
---

# Dicyclomine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Dicyclomine: From Irritable Bowel Syndrome to Cauda Equina Syndrome

## One-Sentence Summary

Dicyclomine is an antispasmodic (antimuscarinic) agent originally used for irritable bowel syndrome and related gastrointestinal conditions.
The TxGNN model predicts it may be effective for **cauda equina syndrome**,
but at present there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Irritable bowel syndrome (the product records compiled for India contain no approved indication text; this comes from the knowledge-graph indications, which also list Clostridium difficile colitis and neurocirculatory asthenia) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dicyclomine is an antimuscarinic/antispasmodic agent that relaxes smooth muscle. Its use in irritable bowel syndrome rests on that effect, and mechanistically it may be applicable to some symptoms of cauda equina syndrome.

The plausible link is symptomatic relief of the neurogenic bladder and bowel dysfunction (detrusor overactivity, spasm) that accompanies cauda equina syndrome. Dicyclomine would not treat the underlying nerve root compression, which requires urgent surgical decompression. This link is unverified.

There is also a specific safety concern. Anticholinergics can worsen urinary retention, which is common in cauda equina syndrome with an areflexic bladder. The second-ranked prediction, neurogenic bladder (score 99.50%), is also model-only. Its disease entry is labelled "obsolete", so it should be mapped to a current concept (e.g., neurogenic detrusor overactivity) before further evaluation. Dicyclomine's evidence base for bladder use is weaker than that of approved bladder-selective antimuscarinics such as oxybutynin.

## India Market Information

Dicyclomine has 20 valid registrations in India, all single-entry records and none cancelled. No approved indication text was available for any of them. Main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 44825 | Cefospas Tablet | Strip of 10 tablets | Not available |
| 114514 | Jonyspas Plus 20mg/250mg Tablet | Strip of 10 tablets | Not available |
| 35066 | Colispas Paed Oral Drops | Packet of 10 ml oral drops | Not available |
| 187821 | Remigan 10 mg/40 mg Drop | Packet of 15 ml drop | Not available |
| 221552 | Topspas Injection | Vial of 2 ml injection | Not available |

Available forms include oral tablets, oral drops, other drop formulations and an injection.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these are graph associations, not label text): angle-closure glaucoma, benign prostatic hyperplasia, hepatic encephalopathy/hepatic coma, liver disease and liver failure, kidney disease, gallbladder disease, gastric ulcer, hypertension, coronary artery disease, porphyria, thrombocytopenia, neutropenia, agranulocytosis, anaemia, obstructive sleep apnoea, anxiety and neurotic disorders, and substance abuse/dependence.
- **Drug Interactions**: 344 interactions are recorded. Examples (mostly Moderate) include:
  - Opioids: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol
  - Other anticholinergics and antihistamines: hyoscyamine, aclidinium, chlorpheniramine, acrivastine, phenyltoloxamine, amitriptyline
  - Others: ethanol, loperamide, amantadine, galantamine, botulinum toxin type A, acebutolol
  - Minor: acetaminophen, hydrochlorothiazide
- **Specific concern for this prediction**: anticholinergic effects may worsen urinary retention in cauda equina syndrome.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (99.66%), but there are no clinical trials or publications behind it (Evidence Level L5). Dicyclomine cannot treat the underlying cause of cauda equina syndrome, and its anticholinergic action could worsen urinary retention.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products (a blocking gap for safety screening)
- Detailed mechanism of action data (MOA)
- A literature and trial search on antimuscarinics for neurogenic bladder/bowel dysfunction in cauda equina syndrome
- Mapping of the "obsolete neurogenic bladder" term to a current disease concept
- A safety assessment of urinary retention risk
- Review of route compatibility (currently pending)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

