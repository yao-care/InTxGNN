---
layout: default
title: Tamsulosin
parent: 僅模型預測 (L5)
nav_order: 799
evidence_level: L5
indication_count: 10
---

# Tamsulosin
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

# Tamsulosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tamsulosin is a selective alpha-1A adrenergic receptor antagonist, used to relieve urinary symptoms associated with benign prostatic hyperplasia (BPH). The TxGNN model's top-ranked prediction is **Ambras type hypertrichosis universalis congenita**, a rare congenital hair-overgrowth disorder — but there are currently **0 clinical trials** and **0 publications** supporting this link, and the evidence pack's own mechanistic assessment explicitly states there is no known biological rationale connecting alpha-1 blockade to this condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign Prostatic Hyperplasia (BPH) — inferred from repurposing-rationale text; no India product license data available |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% (raw score 0.99996) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Tamsulosin's mechanism of action — repeatedly referenced across this evidence pack's rationale fields — is selective antagonism of alpha-1A adrenergic receptors, relaxing smooth muscle in the prostate and bladder neck to relieve BPH-related lower urinary tract symptoms. A formal, curated MOA record (e.g. from DrugBank) is currently a data gap (DG002).

Ambras type hypertrichosis universalis congenita is a rare congenital disorder caused by chromosomal rearrangement, resulting in generalized excessive hair growth from birth. There is no established pharmacological pathway connecting alpha-1 adrenergic receptor antagonism to hair follicle development or congenital chromosomal disease. The evidence pack's own mechanistic assessment for this candidate states explicitly: *"alpha-1 腎上腺素受體拮抗與毛囊發育無已知機轉關聯，無合理性"* — i.e., there is no known mechanistic link and no plausibility.

Notably, this is not an isolated case: several other top-10 TxGNN candidates for Tamsulosin are also hair/follicle-related rare diseases (hypertrichosis, hypotrichosis, alopecia areata, congenital hair shaft abnormalities), each similarly lacking mechanistic support in their own rationale text. This pattern suggests the extremely high raw TxGNN score reflects a graph-topology artifact (e.g., a cluster of rare, sparsely-connected diseases receiving inflated scores) rather than genuine biological signal, and should be interpreted with caution rather than taken at face value.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Tamsulosin currently has **no registered product licenses** in the India regulatory dataset used for this evidence pack (`market_status: 未上市 / Not Marketed`, `total_licenses: 0`). No approved-indication or dosage-form data is available to summarize.

---

## Safety Considerations

- **Drug Interactions**: A total of **202 drug–drug interactions** were identified. The interactions provided include one **Major**-severity interaction (Clarithromycin) and multiple **Moderate**-severity interactions, including:
  - **Opioids**: Morphine, Morphine (liposomal), Opium
  - **SGLT2 inhibitors**: Canagliflozin, Dapagliflozin, Empagliflozin, Ertugliflozin
  - **Azole antifungals**: Clotrimazole, Miconazole
  - **CNS/appetite agents**: Bupropion, Lorcaserin, Dexfenfluramine, Fenfluramine, Dronabinol, Nabilone
  - **Others**: Aprepitant, Cimetidine, Eliglustat, Glycerol phenylbutyrate

  This is a partial list (20 of 202 total interactions); a full interaction check against the patient's concomitant medications is required before any clinical use.

Key warnings and contraindications from the official label are currently a data gap (see Conclusion below) — please refer to the package insert once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Ambras type hypertrichosis) has no supporting clinical trials or literature (Evidence Level L5) and the evidence pack's own mechanistic analysis finds no plausible biological rationale. Combined with the absence of India market registration and a **Blocking**-severity data gap in TFDA label warnings/contraindications, this candidate cannot proceed to safety evaluation (S1) at this time.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) — download and parse from TFDA official site (DG001, Blocking)
- Formal MOA record via DrugBank API query (DG002, High)
- Any preclinical or mechanistic study directly linking alpha-1 adrenergic antagonism to hair follicle biology or Ambras-type hypertrichosis, if repurposing is to be pursued
- Given the apparent hair-disease clustering artifact across multiple top-10 candidates, consider a model-level review of this candidate set before further evaluation of any single prediction (including rank 9, "alopecia," which has the pack's only L4-level evidence but is still indirect/non-mechanistic)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

