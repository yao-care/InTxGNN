---
layout: default
title: Dutasteride
parent: Model Prediction Only (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dutasteride: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
monitor_inn: "Dutasteride"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "migraine with brainstem aura", "familial isolated trichomegaly"]
---

# Dutasteride
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

# Dutasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is a 5-alpha reductase inhibitor, originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but there are currently **0 clinical trials** and **0 publications** directly supporting this prediction, so it rests on computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, dutasteride inhibits 5-alpha reductase types 1 and 2, which lowers dihydrotestosterone (DHT). Its efficacy in BPH is established, and DHT suppression is also relevant to androgen-driven hair follicle disorders such as androgenetic alopecia.

The link to the predicted indication is weak. Ambras syndrome is a genetic disorder of hair follicle development, linked to regulatory changes affecting TRPS1. It is not primarily androgen-driven, so the mechanistic connection is speculative. The very high TxGNN score is a computational prediction only, likely reflecting network associations with hair-related phenotypes.

Other top-ranked predictions are similar in nature. Most are hair or hair-follicle conditions (hypertrichosis, hypotrichosis simplex of the scalp, congenital hypotrichosis milia, genetic hair shaft abnormality, familial trichomegaly), and several have no clear mechanistic link at all (a dental/periodontal malformation syndrome, a Dandy-Walker malformation syndrome, migraine with brainstem aura). None has clinical trial support in the data compiled. The only literature found was for diffuse alopecia areata (rank 8): a 2026 narrative review on androgenetic alopecia in women (PMID 41714473). It concerns a different condition and offers only indirect context.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the lead prediction (Ambras type hypertrichosis universalis congenita). The only publication found across the top 10 predictions relates to a lower-ranked prediction, diffuse alopecia areata, and is shown for context only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41714473](https://pubmed.ncbi.nlm.nih.gov/41714473/) | 2026 | Review | American Journal of Clinical Dermatology | Narrative review of the pathophysiology, evaluation and treatment of androgenetic alopecia in women; it does not address alopecia areata or Ambras syndrome |

## India Market Information

The data compiled for this report show 20 valid single-ingredient registrations, with no combination products and no cancelled licences. Approved indication text is not available for any of them. The main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 63850 | Dutabact 0.5mg Tablet | Strip of 10 tablets | Ikon Remedies Pvt Ltd |
| 63574 | Deetor 0.5mg Tablet | Strip of 10 tablets | Johnlee Pharmaceuticals Pvt Ltd |
| 59391 | Dute 0.5mg Tablet | Strip of 10 tablets | Tetramed Biotek Pvt Ltd |
| 97762 | Genericart Dutasteride 0.5mg Tablet | Strip of 10 tablets | Swast Aushadhi Seva Generic Medicine Store |
| 27111 | Bioduta 0.5mg Tablet | Strip of 10 tablets | Bios Lab |

All products are oral formulations (tablets, plus one dispersible tablet, AGA-DT).

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, liver disease, gallbladder disease, priapism, intraoperative floppy iris syndrome.
- **Drug Interactions**: 122 interactions were identified in total. The moderate-level ones are aprepitant, cimetidine, clarithromycin, clotrimazole and miconazole. Others, such as simvastatin, omeprazole, metformin and prednisone, have an unclassified severity level.
- **Population considerations**: Dutasteride is not suitable for use in pregnancy or in children. This is particularly important for Ambras syndrome and Dandy-Walker-type conditions, which are congenital or paediatric.

Please refer to the package insert for further safety information, as label warnings and contraindications are not available in the data compiled.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score, but it is supported by no clinical trials or directly relevant literature (Evidence Level L5). The mechanistic link between DHT suppression and Ambras syndrome is speculative, because the condition is a genetic follicle-development disorder rather than an androgen-driven one. The paediatric and pregnancy restrictions on dutasteride add further concern.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- Preclinical or mechanistic evidence linking 5-alpha reductase inhibition to TRPS1-related follicle biology
- A review of whether a better-supported hair-related candidate (for example, androgen-dependent hirsutism or androgenetic alopecia) would be a more sensible repurposing target than the rare genetic conditions currently ranked highest
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

