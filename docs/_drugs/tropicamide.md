---
layout: default
title: Tropicamide
parent: 僅模型預測 (L5)
nav_order: 509
evidence_level: L5
indication_count: 3
---

# Tropicamide
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

# Tropicamide: From Ophthalmic Mydriasis to Cauda Equina Syndrome

## One-Sentence Summary

Tropicamide is a short-acting antimuscarinic agent used as an ophthalmic mydriatic to dilate the pupil for examination of the lens, vitreous humor, and retina.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**,
however **no clinical trials** and **no publications** currently support this direction, making this a model-only prediction at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Short-acting mydriatic for ophthalmic examination (lens, vitreous humor, retina) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Tropicamide is a synthetic antimuscarinic compound that antagonises muscarinic acetylcholine receptors — specifically the M2, M3, M4, and M5 subtypes (CHRM2, CHRM3, CHRM4, CHRM5). Its established clinical application is topical ophthalmic use: by blocking M3 receptors in the iris sphincter and ciliary muscle, it induces pupil dilation (mydriasis) and cycloplegia, enabling fundoscopic examination. Its action onset is rapid and its duration short (mydriasis resolves in approximately 20 minutes), which is ideal for diagnostic procedures but presents a significant limitation for chronic systemic indications.

Cauda equina syndrome (CES) is a structural neurological emergency caused by compression of the lumbosacral nerve roots at the spinal canal's terminal segment. The primary and definitive treatment is urgent surgical decompression. There is no pharmacological mechanism through which a muscarinic receptor antagonist would address the root cause — nerve root compression — of CES.

The TxGNN model's high prediction score most likely reflects a multi-hop inference pathway within the knowledge graph: **CES → secondary neurogenic bladder → antimuscarinic therapy**, rather than a direct mechanistic relationship. Neurogenic bladder is a well-recognised sequela of CES, and antimuscarinics (e.g., oxybutynin, solifenacin) are standard treatments for neurogenic detrusor overactivity. This indirect path may explain the model's high confidence, but it does not constitute a repurposing rationale for the primary indication of CES itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Tropicamide has no registered products in India. There are currently **0 active marketing authorisations**.

---

## Safety Considerations

**Drug Interactions (14 recorded interactions; all classified as Unknown severity):**

The following co-medications have flagged interactions with Tropicamide in the DDInter database. Interaction severity is listed as "Unknown" for all entries, meaning the clinical significance has not been formally characterised:

| Interacting Drug | Severity | Source |
|-----------------|----------|--------|
| Atropine | Unknown | DDInter |
| Potassium chloride | Unknown | DDInter |
| Vancomycin | Unknown | DDInter |
| Simvastatin | Unknown | DDInter |
| Prednisolone | Unknown | DDInter |
| Famotidine | Unknown | DDInter |
| Warfarin | Unknown | DDInter |
| Lidocaine | Unknown | DDInter |
| Fluconazole | Unknown | DDInter |
| Brimonidine | Unknown | DDInter |

> The combination with **Atropine** warrants particular attention due to additive antimuscarinic effects (both are muscarinic receptor antagonists), which could heighten the risk of anticholinergic toxicity (urinary retention, tachycardia, dry mouth, confusion).
> The combination with **Brimonidine** is relevant given both are ophthalmic agents and may be co-administered in ophthalmic procedures.

For complete warnings and contraindications, please refer to the Tropicamide package insert (TFDA/prescribing information).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no direct mechanistic link between Tropicamide's antimuscarinic pharmacology and the pathophysiology of cauda equina syndrome, which is a structural compressive emergency requiring surgical intervention. The TxGNN high score (99.53%) is likely an artefact of multi-hop graph reasoning through neurogenic bladder as an intermediary node, rather than evidence of genuine repurposing potential for CES itself. With zero supporting clinical trials and zero supporting publications, this candidate does not meet the threshold for further development at this time.

**To revisit this candidate, the following would be needed:**

- Clarification of whether the TxGNN prediction targets CES itself or its sequela (neurogenic bladder) — if the latter, this should be re-evaluated under the **neurogenic bladder** indication (Rank 2, L4, Research Question), which carries a more coherent mechanistic rationale
- Preclinical or mechanistic evidence demonstrating any direct benefit in nerve root compression or neuroprotection
- Pharmacokinetic data for systemic (oral or parenteral) administration of Tropicamide, should a broader antimuscarinic application be pursued
- Review of TFDA/CDSCO package insert to complete the safety profile (key warnings, contraindications) — currently a blocking data gap
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

