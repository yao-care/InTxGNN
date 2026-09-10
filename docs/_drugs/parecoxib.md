---
layout: default
title: Parecoxib
parent: 僅模型預測 (L5)
nav_order: 640
evidence_level: L5
indication_count: 4
---

# Parecoxib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Parecoxib: From Postoperative Pain to Migraine Disorder

## One-Sentence Summary

Parecoxib is a selective COX-2 inhibitor (the injectable prodrug of valdecoxib), internationally used for the management of acute postoperative pain; it is currently **not marketed in Taiwan**.
The TxGNN model predicts it may be effective for **Migraine Disorder**, with **0 registered clinical trials** and **1 publication** currently supporting this direction — evidence remains preliminary.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute postoperative pain (known pharmacological use; no Taiwan-approved indication text available — drug not licensed in Taiwan) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L3 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action documentation for this drug entry is not yet available. Based on known pharmacology, Parecoxib is a selective cyclooxygenase-2 (COX-2) inhibitor administered parenterally (as a prodrug of valdecoxib), with anti-inflammatory and analgesic properties historically applied to acute postoperative pain.

Migraine attacks involve neurogenic inflammation, prostaglandin release, and meningeal vasodilation — pathways that COX-2 inhibition can plausibly modulate. NSAIDs and coxibs already have an established, if limited, role as abortive therapy for acute migraine, which lends mechanistic plausibility to extending Parecoxib's use from acute pain control to acute migraine treatment.

It should be noted that three additional TxGNN-predicted indications for this drug (migraine with brainstem aura, migraine susceptibility, pulmonary hypertension) were also reviewed but assessed as low-confidence (Evidence Level L4–L5, decision stage S0, recommendation Hold) — the migraine susceptibility signal in particular reflects a genetic/comorbidity association in the knowledge graph rather than a direct pharmacological link, and the pulmonary hypertension signal is contradicted by a negative preclinical finding. Only the general "migraine disorder" prediction (rank 1) is carried forward in this report.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21996647](https://pubmed.ncbi.nlm.nih.gov/21996647/) | 2011 | RCT (pilot) | Clinical Neuropharmacology | Small pilot study comparing oral rizatriptan, IV parecoxib (40 mg), and subcutaneous sumatriptan for acute migraine attacks, exploring COX-2 inhibition as an alternative abortive strategy alongside triptans |

---

## Taiwan Market Information

Not marketed in Taiwan — no license/registration records available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: a Blocking-severity data gap exists — TFDA label warnings/contraindications have not yet been retrieved, meaning this candidate cannot currently pass an S1 safety pre-screen.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to a single small pilot RCT (L3) with no registered clinical trials directly targeting migraine, and the drug is not currently marketed in Taiwan. Critically, TFDA label warnings/contraindications are marked as a Blocking data gap, so the candidate cannot yet enter safety pre-screening (S1).

**To proceed, the following is needed:**
- Retrieve TFDA (or equivalent regulatory) label warnings and contraindications to unblock S1 safety review
- Confirm mechanism-of-action data via DrugBank to substantiate the COX-2/migraine rationale
- Identify or initiate a properly phased (Phase 2/3) RCT specifically in migraine, since existing literature is a single small pilot study
- Assess drug-drug interaction data, currently unavailable (query returned "not_found")
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

