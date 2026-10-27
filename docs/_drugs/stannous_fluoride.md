---
layout: default
title: Stannous Fluoride
parent: Model Prediction Only (L5)
nav_order: 788
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Stannous Fluoride: predicted new indication Meningococcal infection (evidence level L5). Approved use: No approved indication text is listed in the registration record"
monitor_inn: "Stannous fluoride"
predicted_indications: ["meningococcal infection"]
---

# Stannous Fluoride
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

## Stannous Fluoride: From Topical Oral Care to Meningococcal Infection
{: .text-alpha }

## One-Sentence Summary

Stannous fluoride is a topical oral-care ingredient, marketed in India in a toothpaste.
The TxGNN model predicts it may be effective for **meningococcal infection**, but the prediction rests on the model score alone, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication text is listed in the registration record |
| Predicted New Indication | Meningococcal infection |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Stannous fluoride is a topical oral-care agent with known antibacterial and antiplaque activity against oral bacteria, and it is marketed in India as a toothpaste. No original indication is listed in the data compiled for this report.

Meningococcal infection is caused by *Neisseria meningitidis*, which produces invasive systemic disease. No data show that the drug's antibacterial activity against oral bacteria extends to this organism. The drug is not used systemically, so any link would be speculative. The high prediction score may reflect knowledge-graph artifacts rather than a real pharmacological relationship, and the connection cannot be verified from the available data.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 200543 | Sentim-SF Toothpaste | Tube of 50 gm toothpaste | Not stated |

## Safety Considerations

- **Disease-level contraindication signal (knowledge graph, not label text)**: dental fluorosis.

Please refer to the package insert for other safety information, including warnings, contraindications, and drug interactions. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a high model score. There are no clinical trials or literature, no verifiable mechanism, and the product is a topical toothpaste with no systemic use. Package insert safety data are also missing.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to test whether any plausible link to *Neisseria meningitidis* exists
- Package insert warnings and contraindications from the India regulatory source
- In vitro antibacterial data against *Neisseria meningitidis*
- Route compatibility assessment, since invasive meningococcal disease needs systemic exposure and the current product is topical
- Clarification of the original approved indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

