---
layout: default
title: Trimethoprim
parent: 僅模型預測 (L5)
nav_order: 861
evidence_level: L5
indication_count: 2
---

# Trimethoprim
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Trimethoprim: From Antibacterial Use to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

> Trimethoprim (DrugBank DB00440) is a dihydrofolate reductase (DHFR) inhibitor with well-established antibacterial activity, though no original-indication or MOA data is documented in this evidence pack.
> The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — evidence-free, model-only inference.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (drug not marketed locally, no license records; MOA marked as data gap) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Trimethoprim is not available in this evidence pack (data gap DG002). Based on the mechanistic text accompanying the pack's second predicted indication, Trimethoprim inhibits bacterial dihydrofolate reductase (DHFR), blocking folate synthesis — this is a well-established antibacterial mechanism with no direct antiviral or anti-inflammatory action.

Punctate epithelial keratoconjunctivitis is typically caused by viral pathogens (most commonly adenovirus). The evidence pack's own rationale explicitly notes that Trimethoprim's antibacterial mechanism has no direct pathophysiological relevance to this condition, and that the prediction likely arises from an indirect knowledge-graph relationship — possibly transmitted through shared connections to other conjunctival/ocular-surface disease nodes — rather than from a validated biological pathway.

Notably, a second, lower-ranked TxGNN prediction for this same drug — **bacterial conjunctivitis** (score 99.17%) — is supported by a much stronger evidence base (3 clinical trials, 20 publications, evidence level L1) and reflects Trimethoprim's already-established ophthalmic antibacterial use (e.g., the trimethoprim/polymyxin B combination product Polytrim). That prediction essentially validates existing clinical practice rather than proposing a novel use, and offers useful mechanistic contrast: it is antibacterial-consistent, while the keratoconjunctivitis prediction discussed here is not.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

Trimethoprim is currently **not marketed** under this regulatory dataset (market status: Not Marketed; 0 registrations on file). No license or approved-indication records are available to summarize.

## Safety Considerations

- **Drug Interactions**: Query completed, 106 total interactions identified. Notable examples include:
  - **Major**: Potassium citrate, Potassium bicarbonate, Potassium chloride, Potassium gluconate
  - **Moderate**: Metformin, Pioglitazone, Rosiglitazone, Repaglinide, Balsalazide, Picosulfuric acid, Sapropterin
  - Additional interactions of unknown severity level are recorded (e.g., Doxycycline, Omeprazole, Vancomycin, Simvastatin) and should be reviewed individually.

Key warnings and contraindications are not currently available in this evidence pack (data gap DG001, blocking severity — TFDA label warnings/contraindications not yet retrieved).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction rests entirely on TxGNN model inference with no supporting clinical trials or literature, and the drug's known antibacterial mechanism has no direct pathophysiological link to a typically viral condition. Evidence level L5 does not support progression.

**To proceed, the following is needed:**
- Confirmed mechanism of action data for Trimethoprim (data gap DG002)
- TFDA-equivalent label warnings and contraindications (data gap DG001, blocking — required before any S1 safety review)
- Preclinical or mechanistic evidence linking DHFR inhibition (or any secondary activity) to viral keratoconjunctivitis, if this indication is to be pursued further
- As an alternative, near-term repurposing opportunity: the better-evidenced **bacterial conjunctivitis** prediction (L1, Proceed with Guardrails) may warrant separate evaluation, since it is backed by an existing approved ophthalmic combination product and substantial clinical/literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

