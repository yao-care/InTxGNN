---
layout: default
title: Exemestane
parent: 僅模型預測 (L5)
nav_order: 332
evidence_level: L5
indication_count: 7
---

# Exemestane
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Exemestane: From Breast Cancer (Endocrine Therapy) to Antithrombin Deficiency Type 2

## One-Sentence Summary

Exemestane is a steroidal aromatase inhibitor whose use in hormone receptor-positive breast cancer is documented in the literature evidence collected for this pack (structured Taiwan indication records are not available). The TxGNN model's top-ranked prediction is **Antithrombin Deficiency Type 2**, a hereditary coagulation disorder, but this prediction is supported by **0 clinical trials** and **0 publications** — it is a pure model-score signal with no mechanistic or empirical backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in structured Taiwan registry data (drug not marketed in Taiwan); literature evidence in this pack references use as endocrine therapy for hormone receptor-positive breast cancer |
| Predicted New Indication | Antithrombin Deficiency Type 2 |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is flagged as a data gap (DG002) in this pack and is not available from structured fields. Based on the literature evidence collected here, exemestane is referenced as one of the "third generation aromatase inhibitors" (alongside anastrozole and letrozole) used as standard endocrine treatment for hormone receptor-positive breast cancer — it irreversibly inhibits aromatase to lower estrogen synthesis.

Antithrombin deficiency type 2 is a hereditary disorder involving a structural or functional defect in the antithrombin protein itself, governing coagulation regulation. This is mechanistically unrelated to estrogen synthesis or aromatase inhibition — there is no known pathway connecting hormonal suppression to correction of a genetic coagulation-factor defect.

Consequently, this prediction cannot be explained by a plausible biological mechanism. It has zero supporting clinical trials or publications, and the evidence pack's own rationale annotation for this candidate explicitly characterizes it as a pure knowledge-graph similarity artifact rather than a clinically meaningful signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Exemestane currently has no registered licenses in Taiwan (0 registrations; market status: 未上市). No product/dosage-form/indication records are available.

---

## Cytotoxicity

Based on literature evidence in this pack, exemestane's documented oncology use is as a hormonal/endocrine agent (aromatase inhibitor), not a conventional cytotoxic chemotherapy drug.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted/endocrine therapy (steroidal aromatase inhibitor) — non-cytotoxic, not chemotherapy in the conventional sense |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 203 documented interactions on record. Notable examples include Dexamethasone (Moderate level) and Troglitazone (Moderate level); the majority of listed interactions (e.g., Metformin, Omeprazole, Simvastatin, Acetylsalicylic acid, Morphine) are recorded at an "Unknown" severity level, meaning clinical significance has not been graded in the source database.

Key warnings and contraindications are not available (flagged as a Blocking data gap, DG001) — please refer to the package insert for this information once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Antithrombin Deficiency Type 2) has no supporting clinical trials, no literature, and no plausible mechanistic link to exemestane's aromatase-inhibition pathway — it is classified L5 (model prediction only). Reviewing the full candidate list, no indication in this pack reaches a mechanistically and empirically supported signal: the one candidate with literature (amenorrhea) reflects a drug-induced *adverse effect* (chemotherapy/AI-induced ovarian suppression), not a therapeutic use, and the remaining candidates (thrombophilia, migraine, factor V excess, heparin cofactor II deficiency) are similarly unsupported or mechanistically implausible.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) — required before any S1 safety screening
- Confirmed mechanism of action via DrugBank API (DG002, High priority)
- If pursuing repurposing further, prioritize candidates with an identifiable, non-reverse-causal mechanistic hypothesis rather than the current top-ranked genetic coagulation disorder
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

