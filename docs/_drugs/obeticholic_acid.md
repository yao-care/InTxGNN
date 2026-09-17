---
layout: default
title: Obeticholic Acid
parent: Model Prediction Only (L5)
nav_order: 606
evidence_level: L5
indication_count: 6
---

# Obeticholic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Obeticholic Acid: From Cholestatic Liver Disease to Rheumatoid Arthritis

## One-Sentence Summary

Obeticholic acid (DrugBank DB05990) is not currently marketed in Taiwan, and this evidence pack contains no record of its original approved indication or formal mechanism-of-action data. The TxGNN model's top prediction suggests possible activity in **Rheumatoid Arthritis**, but this is supported by **0 clinical trials** and only **3 loosely related publications** (none of which directly studies obeticholic acid in rheumatoid arthritis). Five additional lower-ranked predictions were also reviewed and are assessed as very weak or likely noise (see below).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Taiwan license data provided (drug not marketed) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 (model prediction only, no direct supporting studies) |
| Taiwan Market Status | ✗ Not Marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed, drug-label-grade mechanism-of-action data is currently a documented data gap (DG002, High severity) — DrugBank was queried but no formal MOA text is available in this pack. Based on information embedded in the model's own rationale, obeticholic acid acts as a **Farnesoid X receptor (FXR) agonist**, regulating bile acid metabolism and hepatic inflammation. This is consistent with its known international use (outside this evidence pack) for cholestatic liver conditions such as primary biliary cholangitis — though no Taiwan indication or license record exists to confirm this locally.

The proposed link to rheumatoid arthritis rests on the fact that FXR is expressed in certain immune cell populations, giving a theoretical basis for anti-inflammatory activity beyond the liver. However, the rationale accompanying this prediction explicitly states that **no literature or clinical hypothesis directly connects FXR agonism to rheumatoid arthritis pathophysiology** — the three retrieved publications discuss primary biliary cholangitis, autoimmune hepatitis animal models, and herbal-drug-induced liver injury in RA patients, none of which studies obeticholic acid in an RA context.

The remaining five model predictions (conjunctivitis; colobomatous microphthalmia-rhizomelic dysplasia syndrome; brachydactyly-syndactyly syndrome; brain small vessel disease 1 with ocular anomalies; autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome) have no clinical trials and either no literature or literature that the model's own rationale flags as **keyword co-occurrence noise** rather than genuine mechanistic signal (e.g., 19 ophthalmology case reports/reviews unrelated to bile acid or FXR biology). None of these six candidates currently rises above a purely computational signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32299307](https://pubmed.ncbi.nlm.nih.gov/32299307/) | 2020 | Review | United European Gastroenterology Journal | Diagnosis/treatment review of primary biliary cholangitis; does not address rheumatoid arthritis |
| [35903109](https://pubmed.ncbi.nlm.nih.gov/35903109/) | 2022 | Review | Frontiers in Immunology | Reviews animal models of autoimmune hepatitis and related cholestatic autoimmune liver diseases; treatment reliant on bile acid analogues, no RA linkage |
| [33704005](https://pubmed.ncbi.nlm.nih.gov/33704005/) | 2021 | Preclinical/Animal | Xenobiotica | FXR activation prevents liver injury from *Tripterygium wilfordii* preparations (used to treat RA); relevance is indirect — about hepatoprotection during RA drug therapy, not OCA's efficacy in RA itself |

---

## Taiwan Market Information

Obeticholic acid is not currently marketed in Taiwan — no license or product registration records exist in the regulatory database queried for this pack.

---

## Safety Considerations

- **Drug Interactions**: 50 interactions on record (DDInter database). Notable entries include:

| Interacting Drug | Severity |
|---|---|
| Grazoprevir | Major |
| Lidocaine, Caffeine, Alosetron, Anagrelide, Asenapine, Bendamustine, Cholestyramine, Clomipramine, Clozapine, Colesevelam, Colestipol, Cyclobenzaprine, Duloxetine, Theophylline, Aminophylline, Anisindione, Dicoumarol, Flutamide | Moderate |
| Esomeprazole | Minor |

Key warnings and contraindications are not available in this evidence pack (flagged as a Blocking data gap, DG001 — TFDA label not yet retrieved). Please refer to the package insert once available for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (rheumatoid arthritis) has no clinical trials and only tangential, non-mechanistic literature support, corresponding to evidence level L5. All other predicted indications in this candidate set are equally or more weakly supported, with several assessed by the model's own rationale as likely co-occurrence noise rather than real signal. There is no basis at this time to advance any of these indications past a purely computational hypothesis.

**To proceed, the following is needed:**
- TFDA (or equivalent) label data — key warnings and contraindications (Blocking gap, DG001)
- Formal DrugBank mechanism-of-action confirmation (High-priority gap, DG002)
- Any direct preclinical or clinical evidence specifically testing obeticholic acid/FXR agonism in rheumatoid arthritis, since none currently exists
- Reassessment of lower-ranked candidates only if new literature or trial data emerges — current evidence does not justify further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

