---
layout: default
title: Glycolic Acid
parent: Model Prediction Only (L5)
nav_order: 399
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Glycolic Acid: predicted new indication atypical coarctation of aorta (evidence level L5). Approved use: Not specified (the registered product is a cosmetic-type foaming face…"
monitor_inn: "Glycolic acid"
predicted_indications: ["atypical coarctation of aorta", "non-syndromic esophageal malformation", "esophageal disease", "potassium deficiency disease", "aortic malformation", "sclerosing cholangitis", "disorder of carbohydrate absorption and transport", "hyperinsulinemic hypoglycemia, familial", "diazoxide-resistant focal hyperinsulinism due to Kir6.2 deficiency", "autosomal recessive hyperinsulinism due to SUR1 deficiency"]
---

# Glycolic Acid
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

## Glycolic Acid: From an Unspecified Original Indication to Atypical Coarctation of Aorta
{: .text-alpha }

## One-Sentence Summary

Glycolic acid is currently marketed in India as an ingredient of a topical face wash, and no approved medical indication is recorded for it.
The TxGNN model (deep learning) predicts it may be relevant to **atypical coarctation of aorta**, but this score may reflect similarities the model learned between related diseases, not biological evidence, and it is supported by **0 clinical trials** and only **indirect preclinical literature**.
The retrieved papers concern glycolic acid-containing polymers (PGA, PLGA) used as biomaterials, not glycolic acid as an active drug.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified (the registered product is a cosmetic-type foaming face wash with no approved indication text) |
| Predicted New Indication | Esophageal disease (the highest-ranked prediction, atypical coarctation of aorta, has no supporting evidence at all; esophageal disease is the highest-ranked prediction with any literature) |
| TxGNN Prediction Score | 0.9969 (esophageal disease); 0.9972 for the top-ranked atypical coarctation of aorta |
| Evidence Level | L5 (esophageal disease); L5 for the top-ranked prediction |
| India Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Glycolic acid is an alpha-hydroxy acid, and the only registered product in India is a topical face wash. No original medical indication is documented, so a link between a prior therapeutic use and the predicted indication cannot be drawn.

The retrieved literature on esophageal disease concerns polyglycolic acid (PGA) sheets and PLGA-based materials. These are used as stent coatings, scaffolds, and drug carriers to prevent or treat esophageal stricture. Glycolic acid is only a degradation monomer of these polymers. The therapeutic effect in these studies comes from the device, the carrier, or the loaded drug (paclitaxel, bFGF, triamcinolone), not from glycolic acid itself. The mechanistic link is therefore indirect and does not support a therapeutic indication for glycolic acid.

The other top predictions, including non-syndromic esophageal malformation, esophageal disease, potassium deficiency disease, sclerosing cholangitis, and several familial hyperinsulinism disorders, have no identifiable pharmacological rationale and no supporting trials or literature. Their high scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The literature below was retrieved for esophageal disease. All items are preclinical or otherwise low-tier, and several are off-topic.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37635203](https://pubmed.ncbi.nlm.nih.gov/37635203/) | 2023 | Experimental (PGA sheet, pigs) | J Gastroenterol | Polyglycolic acid sheets with bFGF tested to prevent stricture after esophageal endoscopic submucosal dissection |
| [35487426](https://pubmed.ncbi.nlm.nih.gov/35487426/) | 2022 | Preclinical | Acta Biomater | Biodegradable paclitaxel-PLGA-coated magnesium stent for benign esophageal stricture; the coating increased radial force |
| [33543561](https://pubmed.ncbi.nlm.nih.gov/33543561/) | 2021 | Preclinical | Cell Prolif | Chitosan-collagen scaffold loaded with PLGA/triamcinolone microspheres to reduce stenosis after endoscopic dissection |
| [28556975](https://pubmed.ncbi.nlm.nih.gov/28556975/) | 2017 | Case report | Dig Endosc | Polyglycolic acid mesh combined with a gastropexy device to close gastrocutaneous fistulas |
| [36238233](https://pubmed.ncbi.nlm.nih.gov/36238233/) | 2022 | Bibliometric analysis | Front Public Health | Research trends in endoscopic submucosal dissection; not specific to glycolic acid |
| [29808844](https://pubmed.ncbi.nlm.nih.gov/29808844/) | 2018 | Preclinical (off-topic) | Nanoscale | PLGA nanoparticles delivering a ruthenium radiosensitizer to oesophageal cancer cells |
| [24996905](https://pubmed.ncbi.nlm.nih.gov/24996905/) | 2014 | Genetic study (off-topic) | J Med Genet | HAO1 mutations cause isolated glycolic aciduria; unrelated to esophageal therapy |
| [41135390](https://pubmed.ncbi.nlm.nih.gov/41135390/) | 2026 | Preclinical (off-topic) | Drug Resist Updat | PROTAC delivery for drug-resistant lung cancer |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 94773 | Glucy Foaming Face Wash | Bottle of 100 ml face wash | Not specified |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found, and no contraindication links were identified in the knowledge graph.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on TxGNN model (deep learning) scores alone, which may reflect similarities the model learned between related diseases, not biological evidence. The only supporting literature for esophageal disease concerns glycolic acid-based polymers as device or carrier materials, not glycolic acid as a drug. The only registered product is a topical face wash, so there is no established therapeutic use to build on.

**To proceed, the following is needed:**
- Mechanism of action data for glycolic acid
- Package insert warnings and contraindications
- Evidence that glycolic acid itself, rather than PGA/PLGA materials, has activity in the predicted disease
- Assessment of route compatibility, since the only marketed form is topical and the predicted indications would likely require a different route
- Preclinical studies to test any plausible mechanistic hypothesis before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

