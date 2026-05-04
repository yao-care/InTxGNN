---
layout: default
title: Desoximetasone
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
---

# Desoximetasone
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

# Desoximetasone: From Skin Inflammation to Alopecia Areata

## One-Sentence Summary

Desoximetasone is a potent topical corticosteroid originally used to reduce skin inflammation caused by allergic reactions, eczema, and psoriasis, acting through the glucocorticoid receptor (NR3C1) to suppress pro-inflammatory pathways.
The TxGNN model predicts it may be effective for **Alopecia Areata (圓禿)**,
with **0 registered clinical trials** and **1 RCT publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Skin inflammation from allergic reactions, eczema, and psoriasis |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Desoximetasone is a potent topical corticosteroid that binds to the glucocorticoid receptor (GR, encoded by *NR3C1*). Upon binding, the activated GR complex translocates to the nucleus and suppresses transcription of pro-inflammatory cytokines—including IL-2, IFN-γ, and TNF-α—primarily via inhibition of the NF-κB signalling pathway. This results in reduced immune cell infiltration, decreased vascular permeability, and localised immunosuppression at the site of application.

Alopecia areata (AA) is an autoimmune condition driven by CD8⁺ T-cell infiltration around the hair bulb (the "peribulbar lymphocytic infiltrate"). These T cells target hair follicles that have lost their normal immune privilege, triggering follicular apoptosis and hair loss. Desoximetasone's mechanism of action directly addresses this pathology: by suppressing IL-2 and IFN-γ production, it reduces T-cell activation and peribulbar infiltration, thereby restoring follicular immune privilege and allowing hair regrowth.

The mechanistic connection between desoximetasone's established anti-inflammatory action in eczema/psoriasis and its predicted utility in alopecia areata is therefore well-grounded. Both conditions share aberrant cutaneous immune activation as their core pathology. Notably, this prediction is supported by a published randomised double-blind placebo-controlled trial (Charuwichitratana et al., 2000), lending direct clinical credibility to the TxGNN model's top-ranked prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11030789](https://pubmed.ncbi.nlm.nih.gov/11030789/) | 2000 | RCT | Archives of Dermatology | Randomised double-blind placebo-controlled trial evaluating 0.25% desoximetasone cream in the treatment of alopecia areata |

---

## India Market Information

Desoximetasone currently holds no drug authorisations in India. No registration records are available for this product.

---

## Safety Considerations

**Drug-Target Pharmacology:**
Desoximetasone binds to the **Glucocorticoid receptor (GR / NR3C1, Entrez Gene ID: 2908)**. As a potent topical corticosteroid (synonyms: Topicort®, R-2113, HOE-304), its pharmacological activity is mediated entirely through this receptor. Known class-level safety concerns for potent topical corticosteroids include skin atrophy, telangiectasia, striae, and hypothalamic-pituitary-adrenal (HPA) axis suppression with prolonged or extensive use.

Please refer to the package insert for complete warnings, contraindications, and precaution information, as detailed safety data was not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A randomised double-blind placebo-controlled trial directly testing 0.25% desoximetasone cream in alopecia areata provides Level 2 evidence, and the mechanistic rationale linking GR-mediated immunosuppression to follicular immune privilege restoration is clear and biologically coherent. However, the drug is not currently marketed in India, and full safety documentation (package insert warnings and contraindications) is absent from the current evidence pack.

**To proceed, the following is needed:**

- Obtain and review the full prescribing information / package insert (TFDA or equivalent) for detailed warnings and contraindications
- Confirm the full text and efficacy data of PMID 11030789 (Charuwichitratana et al., 2000) to assess effect size and responder rate
- Conduct a systematic search for additional RCTs or controlled studies on topical corticosteroids (class effect) in alopecia areata to strengthen evidence grading toward L1
- Evaluate the regulatory pathway for India market entry, including required clinical data packages
- Define a safety monitoring plan covering HPA axis assessment and local skin effects for the target alopecia areata population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

