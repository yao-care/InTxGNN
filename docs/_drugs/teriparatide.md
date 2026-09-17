---
layout: default
title: Teriparatide
parent: Model Prediction Only (L5)
nav_order: 817
evidence_level: L5
indication_count: 10
---

# Teriparatide
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

# Teriparatide: From Osteoporosis to Duodenal Ulcer

## One-Sentence Summary

> Teriparatide (PTH 1-34) is a parathyroid hormone analog used to treat osteoporosis in patients at high risk of fracture, acting via PTH1R-mediated stimulation of osteoblast activity.
> The TxGNN model's top-ranked prediction for this drug is **Duodenal Ulcer**, but this candidate is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags no known biological link between PTH signaling and peptic ulcer pathophysiology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Osteoporosis in patients at high risk of bone fracture (per DrugBank pharmacology annotation; no formal local label text available — drug is unmarketed) |
| Predicted New Indication | Duodenal Ulcer (disease) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a Blocking/High-severity data gap in this evidence pack). What is available from pharmacology annotations is that teriparatide acts as an agonist at the PTH1 receptor (PTH1R) and PTH2 receptor (PTH2R), driving osteoblast-mediated bone formation — this is the basis of its approved use in osteoporosis.

For the top-ranked candidate, **duodenal ulcer**, the model's own repurposing rationale explicitly states there is no known mechanistic connection: peptic ulcer pathology is driven by gastric acid secretion and mucosal defense imbalance, a pathway unrelated to PTH1R/PTH2R-mediated osteoblast signaling. No clinical trials or literature currently exist to support this link. This appears to be a case of a high TxGNN embedding-similarity score without accompanying biological plausibility, and should be treated as a low-confidence, model-only signal.

**Note for reviewers:** among this drug's top-10 predictions, one candidate — **pregnancy and lactation-associated osteoporosis (PLO)**, ranked #8 — is mechanistically coherent (it is a direct subtype of the drug's original indication) and is backed by 2 clinical trials and 18 publications, including cohort studies, with an evidence level of L3 and a "Proceed with Guardrails" recommendation. If a repurposing candidate is being selected from this evidence pack, PLO is substantially better supported than duodenal ulcer and may warrant a separate, dedicated evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Teriparatide currently has **no registered authorizations** in the local market (`total_licenses: 0`, `market_status: Not marketed / Not marketed`). No license records, product names, dosage forms, or approved indication text are available to summarize.

---

## Safety Considerations

**Drug Interactions** (from DDI database, 6 documented interactions):

| Interacting Drug | Severity Level |
|---|---|
| Calcitriol (topical) | Moderate |
| Calcipotriol (topical) | Moderate |
| Digoxin | Moderate |
| Digitoxin | Moderate |
| Hydrochlorothiazide | Minor |
| Furosemide | Minor |

No key warnings or contraindications data is currently available for this drug — please refer to the package insert for this information once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (duodenal ulcer) has no supporting clinical trials, no supporting literature, and the model's own rationale identifies no biological mechanism linking PTH1R/PTH2R agonism to peptic ulcer disease (Evidence Level L5, model prediction only). Combined with two blocking/high-severity data gaps — missing local label warnings/contraindications and missing formal MOA documentation — this candidate does not meet the threshold to proceed.

**To proceed, the following is needed:**
- Local product label (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism of action documentation via DrugBank/primary literature — currently a High-severity data gap (DG002)
- A mechanistic hypothesis or preclinical signal connecting PTH1R/PTH2R activity to duodenal ulcer pathophysiology before further evidence collection is prioritized
- If pursuing a repurposing candidate for this drug at all, consider redirecting evaluation toward **pregnancy and lactation-associated osteoporosis**, which already has L3 evidence (2 trials, 18 publications) and a "Proceed with Guardrails" recommendation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

