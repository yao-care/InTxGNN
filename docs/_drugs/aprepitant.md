---
layout: default
title: Aprepitant
parent: 僅模型預測 (L5)
nav_order: 65
evidence_level: L5
indication_count: 10
---

# Aprepitant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Aprepitant: From Chemotherapy-Induced Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Aprepitant is a neurokinin-1 (NK1) receptor antagonist globally approved for prevention of chemotherapy-induced nausea and vomiting (CINV) and post-operative nausea and vomiting (PONV).
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chemotherapy-induced nausea and vomiting (CINV); Post-operative nausea and vomiting (PONV) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Aprepitant is a selective NK1 receptor antagonist that blocks Substance P — a neuropeptide released in the chemoreceptor trigger zone and gastrointestinal tract — from binding to its receptor, thereby preventing the emetic cascade during chemotherapy and surgery. Its efficacy in CINV and PONV is well-established in global regulatory approvals.

Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) is a rare disorder caused by gain-of-function mutations in the V2 vasopressin receptor (AVPR2), resulting in constitutive receptor activation, excessive water reabsorption by renal tubules, and dilutional hyponatremia. A theoretical mechanistic bridge exists: Substance P has been reported in preclinical models to modulate renal tubular function and interact with vasopressin signaling pathways, and NK1 receptors are expressed in kidney tissue. Blocking this neuropeptide signal could hypothetically influence water balance regulation.

However, this proposed connection is highly speculative. The V2 receptor-driven pathophysiology of NSIAD is fundamentally driven by constitutive GPCR activation at the genetic level, which NK1 antagonism cannot directly address. The high TxGNN score (99.97%) most likely reflects indirect knowledge graph linkages — e.g., via shared ontological nodes between neuropeptide signaling and renal regulation — rather than a direct and pharmacologically actionable mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Aprepitant has no current marketing authorization or registration in India.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | No records available | — | — |

---

## Safety Considerations

**Drug Interactions**: Aprepitant has 469 documented interactions in the DDInter database. It is a known CYP3A4 substrate and moderate inhibitor, which underlies its broad DDI profile. Key interactions by severity level are listed below:

| Interacting Drug | Level | Clinical Note |
|------|------|------|
| Fentanyl | **Major** | CYP3A4 inhibition → increased opioid plasma levels, respiratory depression risk |
| Acalabrutinib | **Major** | Increased targeted therapy exposure via CYP3A4 inhibition |
| Alfentanil | **Major** | Opioid toxicity risk, same mechanism as fentanyl |
| Paclitaxel | Moderate | May alter chemotherapy pharmacokinetics in oncology settings |
| Levonorgestrel | Moderate | Potential reduction in hormonal contraceptive efficacy |
| Hydrocortisone | Moderate | Increased corticosteroid exposure |
| Nifedipine | Moderate | CYP3A4-mediated increase in calcium channel blocker levels |
| Fosphenytoin | Moderate | Enzyme induction/inhibition interaction affecting anticonvulsant levels |
| Gefitinib | Moderate | CYP3A4-mediated interaction affecting EGFR inhibitor exposure |
| Dolutegravir | Minor | Limited clinical impact, monitor as needed |

> **Note**: Full warnings and contraindications from the package insert are not available in this Evidence Pack. Please refer to the official prescribing information for complete safety guidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.97%), there is zero clinical trial evidence and zero supporting literature for Aprepitant in NSIAD. This is a pure model prediction (L5), the mechanistic link is indirect and speculative, and Aprepitant is not registered in India — making any development pathway in this market highly premature.

**To proceed, the following is needed:**

- Preclinical data (animal models or in vitro) establishing a functional link between NK1 receptor antagonism and V2 vasopressin receptor activity or renal water transport
- Dedicated literature review on Substance P / NK1 signaling in renal tubular physiology
- MOA data retrieval from DrugBank (currently a blocking data gap — DG002)
- Package insert safety review including warnings, contraindications, and special population guidance (blocking data gap — DG001)
- Assessment of NSIAD disease prevalence and unmet medical need to determine whether an investigator-initiated pilot study would be feasible
- Regulatory pathway scoping for CDSCO if preclinical data proves supportive

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

