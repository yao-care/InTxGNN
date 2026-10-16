---
layout: default
title: Topiroxostat
parent: Moderate Evidence (L3-L4)
nav_order: 849
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Topiroxostat: predicted new indication Hypouricemia, renal (evidence level L4). Approved use: Hyperuricemia, gout"
---

# Topiroxostat
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Topiroxostat: From Hyperuricemia and Gout to Renal Hypouricemia

## One-Sentence Summary

Topiroxostat is a xanthine oxidoreductase (XOR) inhibitor originally used to treat hyperuricemia and gout.
The TxGNN model predicts it may be relevant for **renal hypouricemia**, but the support is thin: **0 clinical trials** and **1 preclinical publication**.
The mechanistic logic is also counterintuitive, since the drug lowers uric acid in a condition where uric acid is already low.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricemia, gout (approved indication text not available in the India license records) |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Topiroxostat is known as an XOR inhibitor that reduces uric acid production, and its efficacy in hyperuricemia and gout is established.

Renal hypouricemia is a condition in which serum uric acid is already low, typically from loss of function in the urate transporters URAT1 (SLC22A12) or GLUT9. Further urate lowering is therefore mechanistically counterintuitive. It is not a treatment for low urate itself, and it may even add risk.

The only linked publication is a preclinical study in a mouse model of hereditary renal hypouricemia type 1. It suggests XOR inhibitors may suppress exercise-induced acute kidney injury (EIAKI), a known complication of the condition. If the drug has any role, it would be protective against that complication rather than correcting low urate. The high TxGNN score most likely reflects proximity in the knowledge network rather than a true therapeutic rationale.

Two other predictions ranked lower and have no supporting studies:
- **Partial HPRT deficiency (score 99.25%)**: purine salvage failure causes uric acid overproduction, so XOR inhibition is plausible for the hyperuricemic manifestations.
- **Lesch-Nyhan syndrome (score 99.09%)**: XOR inhibition could address the metabolic component, but would not be expected to treat the neurological and behavioral features.

Both carry a risk of xanthine accumulation and xanthine nephropathy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34799437](https://pubmed.ncbi.nlm.nih.gov/34799437/) | 2022 | Preclinical | J Am Soc Nephrol | In a new mouse model of hereditary renal hypouricemia type 1 (high-HPRT-activity Urat1-Uox double knockout), XOR inhibitors suppressed the onset of exercise-induced AKI |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 215173 | Toxur 20mg Tablet | Strip of 10 tablets | Not stated |
| 216196 | Topimac 20 Tablet | Strip of 10 tablets | Not stated |
| 218637 | Topimac 60 Tablet | Strip of 10 tablets | Not stated |
| 215845 | Topimac 40 Tablet | Strip of 10 tablets | Not stated |
| 215038 | Topiroxo 40mg Tablet | Strip of 10 tablets | Not stated |

One further registration, Topiroxo 20mg Tablet (215064), is also valid. All 6 registrations are single-ingredient oral products and none is cancelled.

---

## Safety Considerations

Please refer to the package insert for safety information.

Points from the mechanistic analysis worth noting:
- In renal hypouricemia, further urate lowering may increase risk, notably exercise-induced acute kidney injury.
- In HPRT-deficiency conditions, XOR inhibition raises hypoxanthine and xanthine levels, which carries a risk of xanthine nephropathy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence is one indirect preclinical study, with no clinical trials. The mechanism (lowering urate where it is already low) runs counter to the disease biology, so the high TxGNN score should not be read as a therapeutic signal.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory records, which currently block safety screening
- Detailed mechanism of action data (MOA)
- Confirmatory preclinical or clinical studies on whether XOR inhibition protects against exercise-induced AKI in renal hypouricemia
- A safety assessment of urate lowering and xanthine nephropathy risk in this population
- Approved indication text for the registered products
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

