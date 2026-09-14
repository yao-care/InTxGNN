---
layout: default
title: Topiroxostat
parent: 僅模型預測 (L5)
nav_order: 842
evidence_level: L5
indication_count: 3
---

# Topiroxostat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Topiroxostat: From Xanthine Oxidoreductase Inhibition to Renal Hypouricemia (Exercise-Induced AKI Prevention)

## One-Sentence Summary

> Topiroxostat's original indication is not recorded in this evidence pack (not marketed in India, no CDSCO license data available), but it is known as a xanthine oxidoreductase (xanthine oxidase) inhibitor.
> The TxGNN model predicts it may be relevant to **renal hypouricemia (RHUC1)**,
> with **0 clinical trials** and **1 preclinical publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no CDSCO license records; original_indications field empty) |
| Predicted New Indication | Hypouricemia, renal (Renal Hypouricemia Type 1) |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L4 (single preclinical/mechanistic animal study) |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (DrugBank MOA field: Data Gap). Based on the supporting literature, however, Topiroxostat is understood to act as a **xanthine oxidoreductase (xanthine oxidase) inhibitor**, a drug class that blocks the terminal steps of purine catabolism (hypoxanthine → xanthine → uric acid).

The predicted indication, renal hypouricemia (RHUC1), is not a condition of *excess* uric acid — it is caused by loss-of-function mutations in the URAT1/SLC22A12 urate transporter, leading to abnormally *low* serum uric acid and a predisposition to exercise-induced acute kidney injury (EIAKI). The supporting study (PMID 34799437) used a high-HPRT-activity Urat1-Uox double knockout mouse model of RHUC1 and found that xanthine oxidoreductase inhibitors suppressed the onset of EIAKI. The proposed mechanism is not uric-acid lowering (uric acid is already low in these patients), but rather **reduction of oxidative purine flux and reactive oxygen species generation** during high-turnover states such as intense exercise, which appears to drive the acute kidney injury.

This gives a plausible, mechanism-based rationale for TxGNN's high similarity score: Topiroxostat shares the same enzymatic target (xanthine oxidoreductase) as the inhibitors tested in the animal model. However, this rationale currently rests on a **single preclinical mouse study** with no human clinical trial replication, so the mechanistic link — while biologically coherent — remains unconfirmed in patients.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34799437](https://pubmed.ncbi.nlm.nih.gov/34799437/) | 2022 | Preclinical (animal model) | Journal of the American Society of Nephrology (JASN) | In a high-HPRT-activity Urat1-Uox double knockout mouse model of hereditary renal hypouricemia type 1 (RHUC1), xanthine oxidoreductase inhibitors suppressed the onset of exercise-induced acute kidney injury (EIAKI), supporting a role for XOR inhibition in preventing this RHUC1 complication. |

---

## India Market Information

Topiroxostat is currently not marketed in India — no CDSCO license/registration records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Key warnings, contraindications, and drug-drug interaction data are marked as data gaps in this evidence pack (DG001, flagged as Blocking severity — "cannot proceed to S1 safety pre-assessment" without CDSCO/TFDA label data).*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence is limited to a single preclinical animal study with no clinical trials, registered ICTRP trials, or human data supporting the renal hypouricemia indication. Combined with unresolved MOA data and a **Blocking**-severity safety data gap (no label warnings/contraindications available), there is insufficient evidence to proceed to safety pre-assessment (S1) at this time.

**To proceed, the following is needed:**
- Official product label warnings and contraindications (DG001, Blocking — required before S1 safety pre-assessment)
- Confirmed mechanism of action from DrugBank or primary literature (DG002)
- Clinical or human translational evidence for the renal hypouricemia / exercise-induced AKI indication (current evidence is animal-model only)
- Drug-drug interaction data (currently not found)
- Confirmation of India market/registration status, since the drug is not currently marketed under CDSCO
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

