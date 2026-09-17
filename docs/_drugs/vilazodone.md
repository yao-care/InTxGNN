---
layout: default
title: Vilazodone
parent: Model Prediction Only (L5)
nav_order: 879
evidence_level: L5
indication_count: 10
---

# Vilazodone
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

Using no additional skill — this is a direct content-generation task governed by the report template already supplied in full. Proceeding directly.

---

# Vilazodone: From Major Depressive Disorder to Dysthymic Disorder

## One-Sentence Summary

> Vilazodone is a serotonin partial agonist/reuptake inhibitor (SPARI) originally developed and FDA-approved for Major Depressive Disorder (MDD) in adults.
> The TxGNN model predicts it may be effective for **Dysthymic Disorder**, with a **99.79% prediction score**,
> but currently **no clinical trials or published literature** directly support this specific indication — this is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (MDD) — per literature within this evidence pack; no India/Taiwan regulatory label available (drug not marketed) |
| Predicted New Indication | Dysthymic Disorder |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available (data gap DG002). Based on literature evidence within this pack, vilazodone combines selective serotonin reuptake inhibition (SSRI) with partial 5-HT1A receptor agonism — a mechanism approved by the FDA for adult MDD, supported by four positive short-term Phase 3 randomized placebo-controlled trials (per PMID 35726313, PMID 21951984).

Dysthymic disorder (persistent depressive disorder) sits within the broader depression spectrum, so the SSRI+5-HT1A mechanism is theoretically plausible for this condition. However, this rationale is purely mechanistic reasoning by class effect — there is no vilazodone-specific clinical trial or publication addressing dysthymic disorder in the evidence pack. The 99.79% TxGNN score reflects knowledge-graph proximity to depression-related nodes, not observed clinical efficacy.

**Note for context:** Among the other candidates in this evidence pack, *neurotic depression* and *melancholia* — both recognized as MDD subtypes/synonyms rather than truly distinct indications — carry substantially stronger evidence (L1, multiple systematic reviews/network meta-analyses, one completed Phase 4 trial). These largely reflect vilazodone's already-approved MDD indication rather than genuine repurposing and may warrant separate evaluation as "life-cycle management" rather than novel repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for dysthymic disorder specifically.

---

## Literature Evidence

Currently no related literature available for dysthymic disorder specifically.

---

## Safety Considerations

- **Drug Interactions**: Query completed, **171 total interactions** identified (DDInter). Major-level interactions in the sampled data include: **Bupropion, Clarithromycin, Lorcaserin, Diethylpropion, Dolasetron, Palonosetron, Phentermine** — consistent with known serotonergic drug class risks (serotonin syndrome, QT-prolongation potential agents, CYP3A4 interactions). Moderate-level interactions include several sulfonylureas/insulins (Pioglitazone, Chlorpropamide, Glimepiride, insulin analogs), aspirin, dexamethasone, morphine, and bowel-prep agents (polyethylene glycol, picosulfuric acid, sodium sulfate).
- Detailed key warnings and contraindications are not currently available (data gap DG001 — India/local label warnings pending retrieval and parsing).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for dysthymic disorder is high, but there is zero direct clinical trial or literature evidence — only a theoretical class-effect rationale. This does not meet the bar to proceed without further validation, and the drug is not currently marketed in India, so no local safety label exists to support even a guarded launch.

**To proceed, the following is needed:**
- Mechanism of action documentation (DG002)
- India/local package insert warnings and contraindications (DG001)
- Dedicated preclinical or clinical evidence for dysthymic disorder specifically (current evidence only supports the already-approved MDD indication)
- Consider re-scoping: evaluate *melancholia* and *neurotic depression* (L1, S3, Proceed with Guardrails) separately, as these have materially stronger evidence within this same pack
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

