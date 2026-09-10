---
layout: default
title: Riluzole
parent: 僅模型預測 (L5)
nav_order: 734
evidence_level: L5
indication_count: 10
---

# Riluzole
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

# Riluzole: From Amyotrophic Lateral Sclerosis to Bilateral Parasagittal Parieto-Occipital Polymicrogyria

## One-Sentence Summary

> Riluzole is a glutamate-modulating neuroprotective agent whose only well-established clinical indication is amyotrophic lateral sclerosis (ALS).
> The TxGNN model's **top-ranked** prediction is **Bilateral Parasagittal Parieto-Occipital Polymicrogyria**, a cortical malformation disorder,
> but this prediction is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own rationale flags it as a likely false-positive with no mechanistic plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not present in registry data (drug not marketed locally); established clinical indication is **Amyotrophic Lateral Sclerosis (ALS)**, per literature cited elsewhere in this evidence pack |
| Predicted New Indication | Bilateral Parasagittal Parieto-Occipital Polymicrogyria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for riluzole is not available in this evidence pack (`original_moa` is a data gap). However, elsewhere in the pack — in the rationale for a lower-ranked candidate (ALS susceptibility, rank 8) — riluzole's mechanism is described as inhibition of presynaptic glutamate release, blockade of voltage-gated sodium channels, and antagonism of glutamate receptors, reducing motor-neuron excitotoxicity. This is consistent with riluzole's well-known role as the first approved disease-modifying therapy for ALS.

For the top-ranked prediction, **bilateral parasagittal parieto-occipital polymicrogyria**, the evidence pack's own repurposing rationale is explicit that this link is **not** mechanistically sound: polymicrogyria is a disorder of neuronal migration during cortical development, whereas riluzole acts on excitotoxic injury in mature motor neurons. There is no known developmental or migrational pathway targeted by riluzole. The rationale text states this is "a TxGNN high-score prediction lacking mechanistic plausibility or any supporting evidence."

Given this, the prediction should be treated as a candidate for further model/data-quality investigation rather than a scientifically grounded repurposing hypothesis at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

No registration records found. Riluzole is not currently marketed in India/Taiwan under the regulatory data reviewed (`total_licenses = 0`), so no product/dosage-form/indication table can be produced.

---

## Safety Considerations

**Drug Interactions**: A DDI query returned 44 total interactions on record. Notable Moderate-severity interactions include:

- Obeticholic acid
- Naltrexone
- Deferasirox
- Osilodrostat
- Anagrelide
- Asparaginase Escherichia coli
- Brentuximab vedotin
- Clofarabine
- Methotrexate
- Epirubicin

(Minor: Omeprazole, Caffeine, Theophylline, Aminophylline; several others rated "Unknown" severity — e.g., Metformin, Simvastatin, Ranitidine, Salbutamol, Ibuprofen, Cyanocobalamin.)

Formal package-insert warnings and contraindications are not available in this evidence pack; please refer to the official label once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (polymicrogyria) has no clinical, literature, or mechanistic support, and the evidence pack itself identifies it as a probable false-positive knowledge-graph association. Pursuing this candidate is not justified at this time.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001 (TFDA/regulatory label — warnings and contraindications) before any safety evaluation can proceed
- Resolve data gap DG002 (confirmed MOA from DrugBank) to support or refute mechanistic linkage claims
- Independent review of the TxGNN ranking methodology, since the highest-scored candidate in this run lacks mechanistic plausibility while a lower-ranked, evidence-rich candidate (ALS susceptibility, rank 8, L1/S3) corresponds to riluzole's already-approved indication rather than a novel repurposing opportunity
- If genuine novel candidates are desired, consider re-examining mid-ranked motor-neuron-disease-adjacent predictions in this pack (e.g., late-adult-onset lower motor neuron syndrome, Mills syndrome, ALS type 22) that at least share a plausible excitotoxicity-based mechanistic rationale, even though none currently have clinical trial or literature support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

