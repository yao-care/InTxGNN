---
layout: default
title: Benzydamine
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 1
---

# Benzydamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Benzydamine: From Oral/Pharyngeal Anti-inflammatory to Benign Prostatic Hyperplasia

## One-Sentence Summary

Benzydamine is a non-steroidal anti-inflammatory drug (NSAID) with local anesthetic properties, commonly used for oral mucositis, pharyngitis, and gynaecological inflammation.
The TxGNN model predicts it may be effective for **Benign Prostatic Hyperplasia (BPH)**,
with a high prediction score of **99.26%**; however, **no supporting clinical trials or published literature** were identified, making this a model-only prediction at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Oral/pharyngeal inflammation (oral mucositis, pharyngitis); detailed regulatory indication data not available in India |
| Predicted New Indication | Benign Prostatic Hyperplasia (BPH) |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 — Model prediction only; no clinical trials or literature identified |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for Benzydamine is not available in the current dataset. Based on established pharmacological knowledge, Benzydamine is a benzimidazole-derived NSAID with three theoretically relevant mechanisms that may connect it to BPH pathophysiology.

**Anti-inflammatory axis:** BPH pathogenesis is closely linked to chronic low-grade inflammation within the prostatic microenvironment, characterised by elevated levels of IL-6, IL-8, and TNF-α. Benzydamine is known to inhibit TNF-α translation and COX-dependent prostaglandin synthesis, which may theoretically attenuate the inflammatory proliferative stimulus in prostate tissue. This represents the strongest mechanistic rationale, though evidence remains indirect and organ-level data are absent.

**Local anesthetic and sensory nerve modulation:** Benzydamine's sodium channel blocking activity may influence prostatic sensory afferent input, potentially improving subjective lower urinary tract symptoms (LUTS) perception without addressing the underlying tissue hyperplasia. Additionally, limited pharmacological data suggest a weak alpha-adrenoceptor antagonist activity, loosely analogous to tamsulosin; however, the potency is far below that of standard alpha-blockers and findings across literature are inconsistent. A critical limitation is that Benzydamine's low systemic bioavailability from topical formulations may preclude therapeutically relevant prostatic tissue concentrations.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Benzydamine is currently **not marketed in India**. No drug approvals or product registrations were found in the regulatory dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(All available safety fields — key warnings, contraindications, and drug-drug interactions — contained no retrievable data in the current Evidence Pack. Full safety evaluation requires manual review of the CDSCO/manufacturer prescribing information.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a very high prediction score (99.26%), but all three evidence queries (ClinicalTrials.gov, ICTRP, PubMed) returned zero results for Benzydamine in BPH. With no human or preclinical in-vivo data, and critical gaps in both MOA characterisation and safety profiling, this candidate cannot advance past the hypothesis stage.

**To proceed, the following is needed:**

- **Safety data remediation (Blocking):** Obtain and parse the official prescribing information (package insert) to extract key warnings and contraindications before any S1 safety assessment can begin
- **MOA confirmation:** Retrieve structured mechanism of action data from DrugBank API (DB09084) to formally confirm TNF-α inhibition, COX inhibition, and sodium channel blocking as the operative pharmacology
- **Preclinical evidence search:** Conduct a broader literature search using MeSH terms (e.g., "benzydamine" AND "prostate" OR "LUTS" OR "alpha-adrenergic") and expand to non-English databases; current query may have been too restrictive
- **Prostatic pharmacokinetic data:** Determine whether systemic absorption is sufficient to achieve therapeutic concentrations in prostate tissue — this is a critical feasibility gate given Benzydamine's historically topical usage
- **Exploratory in-vitro or in-vivo BPH model study:** If mechanistic plausibility is confirmed, a preclinical proof-of-concept study would be the minimum threshold to elevate this candidate from L5 to L4
- **India regulatory pathway:** Since Benzydamine has no existing India registration, a full new drug application pathway would apply — factoring this into the development timeline is essential
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

