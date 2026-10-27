---
layout: default
title: Pinaverium
parent: Model Prediction Only (L5)
nav_order: 673
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Pinaverium: predicted new indication Benign prostatic hyperplasia (evidence level L5). Approved use: Not stated in the registration data compiled for this report (general…"
monitor_inn: "Pinaverium"
predicted_indications: ["benign prostatic hyperplasia (disease)"]
---

# Pinaverium
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Pinaverium: From Irritable Bowel Syndrome (Gastrointestinal Spasm) to Benign Prostatic Hyperplasia
{: .text-alpha }

## One-Sentence Summary

Pinaverium is a gastrointestinal-selective calcium channel blocker (antispasmodic), generally used for irritable bowel syndrome. The TxGNN model predicts it may be effective for **benign prostatic hyperplasia (BPH)**, but **no clinical trials and no publications** currently support this direction. The prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report (general pharmacology: irritable bowel syndrome / GI smooth muscle spasm) |
| Predicted New Indication | Benign prostatic hyperplasia |
| TxGNN Prediction Score | 99.22% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, pinaverium is a gastrointestinal-selective L-type calcium channel blocker that relaxes gut smooth muscle, and it is used for irritable bowel syndrome.

A plausible link to BPH is that L-type calcium channels contribute to smooth muscle contraction in the prostate stroma, bladder neck and detrusor. Blocking them could theoretically lower smooth muscle tone and ease lower urinary tract symptoms. This is a hypothesis from general pharmacology, not a finding from the supplied data.

There is also a significant counterargument. Pinaverium is poorly absorbed when taken orally and is largely excreted in bile, so exposure at prostatic tissue would likely be low, which weakens the hypothesis. The TxGNN score of 0.992 is a model prediction only and gives no clinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 72414 | Eldicet Tablet (Abbott) | Strip of 10 tablets | Not stated in the registration data |

---

## Safety Considerations

Please refer to the package insert for safety information. No warning, contraindication or drug interaction data were available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN model score (Evidence Level L5), with no clinical trials or literature. Pinaverium's poor systemic absorption also makes adequate prostatic exposure doubtful.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) to allow a proper mechanistic analysis
- The approved indication and the package insert warnings and contraindications for the India registration (a blocking gap for safety screening)
- Preclinical or pharmacokinetic evidence showing the drug reaches prostate or lower urinary tract tissue
- A literature and trial search for calcium channel blockers in BPH or lower urinary tract symptoms
- Route compatibility assessment (available vs. required routes)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

