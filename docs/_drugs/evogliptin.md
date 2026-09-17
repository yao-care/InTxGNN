---
layout: default
title: Evogliptin
parent: Model Prediction Only (L5)
nav_order: 331
evidence_level: L5
indication_count: 5
---

# Evogliptin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

# Evogliptin: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Evogliptin (DrugBank DB12625) is a DPP-4 inhibitor whose established clinical use is glycemic control in Type 2 Diabetes Mellitus, though formal original-indication and MOA records are not present in this evidence pack. The TxGNN model's top prediction proposes **Opsismodysplasia**, a rare skeletal dysplasia, but this candidate is supported by **zero clinical trials** and **zero publications**, and the model's own mechanistic rationale concludes the link lacks biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (Evogliptin is a DPP-4 inhibitor class drug, typically indicated for Type 2 Diabetes Mellitus) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack (flagged as a High-severity data gap, DG002). Based on the model's own mechanistic annotation, Evogliptin is understood to act as a DPP-4 inhibitor, suppressing degradation of GLP-1/GIP incretin hormones to promote glucose-dependent insulin secretion and suppress glucagon — a mechanism consistent with use in Type 2 Diabetes Mellitus.

Opsismodysplasia, however, is a rare skeletal dysplasia caused by mutations in genes such as *INPPL1*/*PIEZO1*, with a pathology rooted in abnormal growth-plate cartilage metabolism. There is no established biological pathway connecting incretin/DPP-4 signaling to skeletal growth-plate regulation. The evidence pack's own repurposing rationale explicitly states that this high TxGNN score likely reflects knowledge-graph embedding similarity rather than a genuine pharmacological relationship, and that the prediction "lacks biological plausibility support."

Given this, the mechanistic rationale for this specific candidate should be treated as weak. This assessment is consistent across the pack: none of the top 5 predicted indications (opsismodysplasia, thiamine-responsive dysfunction syndrome, focal stiff limb syndrome, classic stiff person syndrome, drug-induced localized lipodystrophy) have a direct pharmacological link to DPP-4 inhibition — each rationale describes at most an indirect or speculative pathway (e.g., shared autoimmune antigen, adjacent metabolic tissue), with no experimental or clinical data to support the connection.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: Retrieval of TFDA/label warnings and contraindications is currently a **Blocking** data gap (DG001) — this prevents the candidate from entering the S1 safety pre-screening stage regardless of the strength of efficacy evidence.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five predicted indications sit at Evidence Level L5 (model prediction only, decision stage S0) with no supporting clinical trials, literature, or ICTRP records. The top-ranked candidate, opsismodysplasia, is explicitly assessed within the evidence pack as lacking biological plausibility despite its high TxGNN score. In addition, a Blocking-severity data gap for TFDA safety labeling data prevents any candidate here from advancing to the S1 safety pre-screening stage.

**To proceed, the following is needed:**
- TFDA/label warnings, contraindications, and precautions (Blocking gap, DG001)
- Confirmed original indication and detailed MOA documentation (DG002)
- Drug-drug interaction (DDI) data (currently not found)
- Preclinical or mechanistic studies specifically linking DPP-4/incretin pathways to any of the five predicted rare-disease indications
- Taiwan/India market authorization and licensing records, if regulatory filing is ever pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

