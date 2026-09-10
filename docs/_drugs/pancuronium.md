---
layout: default
title: Pancuronium
parent: 僅模型預測 (L5)
nav_order: 634
evidence_level: L5
indication_count: 10
---

# Pancuronium
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

# Pancuronium: From Neuromuscular Blockade to Cauda Equina Syndrome

## One-Sentence Summary

Pancuronium is a non-depolarizing neuromuscular blocking agent used as a skeletal muscle relaxant adjunct during general anesthesia. The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but this ranks among the model's weakest possible signals: **0 clinical trials** and **0 publications** currently support this specific link, and the drug's own mechanism review flags the prediction as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Skeletal muscle relaxant / neuromuscular blockade adjunct to general anesthesia (non-depolarizing agent) — no formal Taiwan license text on file |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the mechanistic annotations carried within the evidence itself, Pancuronium is a non-depolarizing neuromuscular blocker acting on nicotinic acetylcholine receptors at the skeletal muscle motor end-plate, producing muscle paralysis for surgical/ventilatory purposes only.

Cauda equina syndrome is a neurosurgical emergency caused by mechanical compression of the lumbosacral nerve roots, requiring surgical decompression. There is no pharmacological pathway by which a peripherally-acting neuromuscular blocker could treat the underlying compressive lesion. The evidence pack's own rationale for this candidate explicitly states that no mechanism supports a treatment effect, and attributes the high TxGNN score to a likely **knowledge-graph artifact** — probable spurious linkage through shared downstream symptoms (e.g., urinary retention, limb weakness) that co-occur with both pancuronium's known effects and cauda equina syndrome's clinical presentation, rather than genuine therapeutic relevance.

This assessment is consistent across the full prediction set for this drug: all 10 top-ranked TxGNN candidates (cauda equina syndrome, IBS, neurogenic bladder, neurocirculatory asthenia, migraine variants, mitral valve prolapse/MVP1, autonomic nervous system disease) were independently reviewed and none has a plausible mechanistic basis. The two candidates with any literature at all (neurocirculatory asthenia, autonomic nervous system disease) are supported only by anesthesia-safety case reports describing how pancuronium behaves *in patients who already have* those conditions — not evidence that pancuronium treats them. All 10 candidates carry a "Hold" recommendation in the source data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Pancuronium currently holds no marketing license in Taiwan (market status: 未上市, 0 registrations on file), so no product/dosage-form registry data is available.

---

## Safety Considerations

- **Drug Interactions**: DDI screening returned 71 total interaction records; among the detailed entries, **Major**-level interactions include Paromomycin, Kanamycin, and Neomycin (aminoglycosides potentiate neuromuscular blockade). **Moderate**-level interactions include other aminoglycosides/tetracyclines (Doxycycline, Tetracycline, Minocycline, Vancomycin), corticosteroids (Hydrocortisone, Dexamethasone, Betamethasone, Triamcinolone), magnesium salts (Magnesium sulfate, Magnesium chloride), Mannitol, Metoclopramide, Trospium, and Amphotericin B (including lipid complex).

Key warnings and contraindications from the product label are not yet available (Blocking data gap, DG001) — refer to the package insert once obtained for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (99.95%) reflects a model-only prediction (L5) with no supporting clinical trials or literature, and the mechanistic review indicates the signal is likely a knowledge-graph false positive rather than a genuine repurposing lead. The drug is also unregistered in Taiwan, and a Blocking data gap (missing TFDA label warnings/contraindications) prevents even an initial S1 safety screen.

**To proceed, the following is needed:**
- TFDA package insert (warnings/contraindications) to close the Blocking gap (DG001) before any safety review can begin
- Detailed mechanism of action data (DG002) to properly evaluate mechanistic plausibility
- Independent pharmacological or preclinical evidence specifically linking pancuronium to cauda equina syndrome, since none currently exists
- If pursuing an alternative candidate from this drug's prediction set, "autonomic nervous system disease" (L4, decision stage S1) has the most literature volume (14 papers), though it too requires re-evaluation since existing citations describe anesthesia safety in affected patients rather than therapeutic effect
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

