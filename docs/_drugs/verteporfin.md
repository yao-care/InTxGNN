---
layout: default
title: Verteporfin
parent: Model Prediction Only (L5)
nav_order: 878
evidence_level: L5
indication_count: 1
---

# Verteporfin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Verteporfin: From Wet Age-Related Macular Degeneration to Mitochondrial Oxidative Phosphorylation Disorder

## One-Sentence Summary

Verteporfin is a photosensitizer publicly known for use in photodynamic therapy of wet age-related macular degeneration, though the drug's formal indication and labeling data are currently missing from this evidence pack (blocking data gap DG001). The TxGNN model predicts it may be effective for **mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies**, but this prediction is supported by **zero clinical trials** and **zero publications**, making it a pure model-output candidate at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in current data (DG001 — TFDA/CDSCO label text missing); publicly known off-record use is wet AMD via photodynamic therapy |
| Predicted New Indication | Mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (DG002). Based on publicly known pharmacology, Verteporfin (marketed elsewhere as Visudyne) is a benzoporphyrin-derivative **photosensitizer**: after intravenous administration it is activated by laser light to generate reactive oxygen species (ROS), which selectively damages abnormal choroidal neovasculature — the basis for its use in photodynamic therapy for wet AMD. Separately, the literature also describes Verteporfin as an inhibitor of the YAP/TAZ–TEAD protein–protein interaction, blocking downstream transcription of the Hippo signaling pathway.

Neither of these known mechanisms — light-activated ROS generation or YAP/TAZ–TEAD inhibition — has an established connection to mitochondrial oxidative phosphorylation (OXPHOS) disorders caused by nuclear DNA defects, which are driven by inherited deficiencies in electron transport chain (ETC) complex assembly or function. There is currently no published mechanistic hypothesis or preclinical rationale linking Verteporfin to correction or modulation of ETC complex activity.

Given this gap, the prediction should be treated as an association surfaced purely by the TxGNN knowledge-graph embedding (score 0.9949, KG rank 8547), rather than a mechanistically explainable candidate. This is consistent with the model's own scoring, which assigns this candidate to Evidence Level L5 and decision stage S0 (Hold).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Verteporfin is currently **not marketed** in India (0 registrations on file). No license or product-level data is available to summarize.

---

## Safety Considerations

**Drug Interactions**: DrugBank/DDInter data lists **117 documented interactions** in total. The 20 highest-confidence entries returned are predominantly **Moderate**-severity, clustering around two pharmacological themes consistent with Verteporfin's photosensitizing mechanism and hepatic handling:

- **Other photosensitizing agents** — increased risk of additive photosensitivity/phototoxic skin or ocular reactions: Doxycycline, Doxycycline (topical), Tetracycline, Tetracycline (topical), Minocycline, Minocycline (topical), Levofloxacin, Sulfasalazine, Beta carotene, Acetylsalicylic acid, Polymyxin B (Minor).
- **Sulfonylurea antidiabetics** — potential for altered glycemic control or additive photosensitivity: Chlorpropamide, Glimepiride, Glipizide, Glyburide, Tolazamide, Tolbutamide, Acetohexamide.
- Others noted: Mannitol, Papaverine.

No structured key warnings or contraindications are currently available (DG001, blocking); please refer to the official package insert once obtained for full prescribing safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a high TxGNN similarity score but is unsupported by any clinical trial or literature evidence (L5), and the drug's own known mechanisms (photoactivated ROS generation, YAP/TAZ–TEAD inhibition) have no established link to nuclear-DNA-related mitochondrial OXPHOS disorders. Combined with a blocking data gap on TFDA/CDSCO label warnings and contraindications (DG001), the candidate cannot yet proceed to a safety-based (S1) review.

**To proceed, the following is needed:**
- Resolve DG001: obtain official label/warning and contraindication data (TFDA/CDSCO) before any S1 safety evaluation
- Resolve DG002: confirm verified mechanism of action from DrugBank/primary literature
- Preclinical or mechanistic literature search specifically linking YAP/Hippo signaling (or ROS-mediated pathways) to nuclear-DNA-encoded ETC complex function, to establish or rule out biological plausibility
- Route compatibility assessment — Verteporfin's approved administration (IV infusion + localized laser photoactivation) may not be feasible for a systemic mitochondrial disease population; this needs explicit evaluation before further development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

