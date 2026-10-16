---
layout: default
title: Lithium Carbonate
parent: Model Prediction Only (L5)
nav_order: 495
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lithium Carbonate: predicted new indication Pseudoachondroplasia (evidence level L5). Approved use: Bipolar disorder"
---

# Lithium Carbonate
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

# Lithium Carbonate: From Bipolar Disorder to Pseudoachondroplasia

## One-Sentence Summary

Lithium carbonate is a long-established mood stabiliser, originally used to treat bipolar disorder and related affective disorders.
The TxGNN model predicts it may be effective for **pseudoachondroplasia**, but there are **0 clinical trials** and **0 publications** supporting this specific prediction. It is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bipolar disorder (the licence records contain no approved indication text; this is taken from the drug's known indications in the knowledge graph, which also lists major affective disorder, manic bipolar affective disorder, and several arthritis-related conditions) |
| Predicted New Indication | Pseudoachondroplasia |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Lithium is known to inhibit GSK-3beta and modulate Wnt signalling, which could plausibly influence cartilage and bone cell biology. This is general background knowledge, not something established by the compiled data.

Pseudoachondroplasia is a genetic skeletal dysplasia caused by COMP mutations, which lead to endoplasmic reticulum stress and retention of matrix proteins in chondrocytes. No direct link between lithium's action and this mechanism is established.

The high score most likely reflects proximity within the knowledge graph. Several of the top-ranked predictions (pseudoachondroplasia, Hunter-Thompson acromesomelic dysplasia, brachyolmia and others) belong to the skeletal dysplasia cluster, which suggests a network-driven pattern rather than a validated biological link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for pseudoachondroplasia.

For reference, the only publication found among the top ten predictions is a general 2019 review of therapeutic advances in genetic skeletal disorders ([PMID 31888683](https://pubmed.ncbi.nlm.nih.gov/31888683/), Orphanet J Rare Dis). It was linked to a different predicted indication (brachyolmia-amelogenesis imperfecta syndrome) and is not direct evidence of lithium efficacy.

## India Market Information

Showing 5 of 20 valid single-ingredient registrations. All are oral tablets, including immediate-release, SR, XR and CR forms. Approved indication text was not available in the licence records.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 53664 | Cthium 300mg Tablet | Strip of 10 tablets | Not stated in licence record |
| 49084 | Carbolith 400mg Tablet | Strip of 10 tablets | Not stated in licence record |
| 245817 | Yalithim 400mg Tablet XR | Strip of 10 tablet XR | Not stated in licence record |
| 125707 | Lithowel 450mg Tablet CR | Strip of 10 tablet CR | Not stated in licence record |
| 121118 | Licab XL Tablet | Strip of 10 tablet PR | Not stated in licence record |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (model-derived, not package-insert text): kidney disease, hypothyroidism (including myxedema and congenital hypothyroidism), diabetes insipidus (including central and neurohypophyseal forms), cognitive disorder, psoriasis and parapsoriasis, sudden cardiac arrest, heart conduction disease, and pyoureter.
- **Drug Interactions**: 252 interactions were recorded. Major-level examples include **bupropion** and **lorcaserin**. Moderate-level examples include metformin, pioglitazone, acarbose, alogliptin, canagliflozin, clarithromycin, metronidazole, morphine, famotidine, mesalazine, loperamide and potassium citrate. Minor-level examples include doxycycline, epinephrine and acetylsalicylic acid.
- **Additional caution**: Lithium is a known teratogen, a concern for any developmental or paediatric skeletal indication. This is general pharmacological knowledge, not drawn from the compiled data.

Please refer to the package insert for full warnings, as label-based warnings were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score, with no clinical trials or literature for pseudoachondroplasia (evidence level L5). Lithium has no established mechanistic link to the COMP-related disease process. Its narrow therapeutic index, its kidney and thyroid risks, and its large interaction burden further argue against advancing without supporting data.

**To proceed, the following is needed:**
- Detailed mechanism of action data for lithium
- Preclinical evidence (for example, COMP-mutant chondrocyte or mouse models) showing that GSK-3beta/Wnt modulation has a benefit
- Package insert warnings and contraindications from the India market labels, to complete safety screening
- A risk-benefit assessment for a likely paediatric population, including teratogenicity, renal and thyroid monitoring, and serum level monitoring
- A formal literature search specific to lithium and skeletal dysplasias
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

