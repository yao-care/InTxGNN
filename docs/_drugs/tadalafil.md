---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 796
evidence_level: L5
indication_count: 8
---

# Tadalafil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Tadalafil: From Pulmonary Arterial Hypertension to Kyphoscoliotic Heart Disease

## One-Sentence Summary

> Tadalafil is a phosphodiesterase type 5 (PDE5) inhibitor best known for erectile dysfunction treatment and as an approved therapy for pulmonary arterial hypertension (PAH).
> Of eight new indications flagged by TxGNN, the only one with a plausible biological mechanism is **Kyphoscoliotic Heart Disease** (secondary pulmonary hypertension from spinal deformity),
> but this candidate currently has **zero supporting clinical trials or literature** — the model score is not backed by any real-world evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack's regulatory data (no licenses on file); publicly known approved uses include erectile dysfunction and pulmonary arterial hypertension |
| Predicted New Indication | Kyphoscoliotic Heart Disease (secondary pulmonary hypertension / cor pulmonale) |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 (model prediction only — no disease-specific trials or literature) |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not populated in this evidence pack (flagged as a High-severity data gap, DG002). Based on well-established pharmacology, however, Tadalafil is a PDE5 inhibitor: it blocks breakdown of cGMP, promoting vascular and pulmonary smooth-muscle relaxation. This exact mechanism is why Tadalafil is already an approved treatment for idiopathic pulmonary arterial hypertension.

Kyphoscoliotic heart disease is essentially cor pulmonale secondary to restrictive ventilatory impairment caused by severe spinal deformity — the end pathway is chronically elevated pulmonary vascular resistance and pulmonary hypertension. Mechanistically, this converges on the same pulmonary vascular target that Tadalafil already treats in idiopathic PAH, which is why this is the one candidate in this batch with a credible biological rationale. That said, kyphoscoliosis-associated pulmonary hypertension has a different underlying driver (mechanical/hypoxic) than idiopathic PAH, so extrapolation is not guaranteed to translate into clinical benefit, and **no trial or case report specific to this population currently exists**.

**⚠️ Note on the other model-ranked candidates in this batch:** Five of the eight predictions (Ambras hypertrichosis, generic hypertrichosis, Dandy-Walker syndrome, isolated hair shaft abnormality, familial trichomegaly) have no known biological link to PDE5 inhibition and are most likely knowledge-graph embedding artifacts — they cluster near unrelated "hair/craniofacial" disease nodes with no supporting literature at all. The periodontal-disease candidate (rank 3) returned 20 literature hits, but every one is generic periodontology literature that never mentions Tadalafil by name — it reflects a broad disease-node search, not drug-specific evidence. The migraine-with-brainstem-aura candidate (rank 8) is supported by exactly one case report, and that report describes Tadalafil **inducing** a migraine aura as an adverse effect — a risk signal, not a therapeutic one. None of these six candidates should be advanced.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Tadalafil currently has no marketing authorization on record in India (0 registrations; market status: Not marketed). No dosage form or approved-indication data is available to summarize.

---

## Safety Considerations

- **Drug Interactions**: The interaction database returns 132 known interactions for Tadalafil. Clinically flagged (Moderate level) interactions in this dataset include: Aprepitant, Dexamethasone, Lorcaserin, Canagliflozin, Cimetidine, Clarithromycin, Dapagliflozin, Empagliflozin, Sapropterin, Miconazole, Clotrimazole, Ertugliflozin, and Troglitazone. A Minor-level interaction is noted with Papaverine. Several additional interactions (e.g., Pantoprazole, Glimepiride, Doxycycline, Morphine, Metformin, Omeprazole) are recorded with an unclassified ("Unknown") severity level and warrant individual review before use.

Official warnings and contraindications (e.g., from TFDA labeling) are not currently available in this evidence pack — this is logged as a **Blocking** data gap (DG001) that must be resolved before any safety pre-assessment (S1 stage) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only candidate with a plausible mechanistic basis (kyphoscoliotic heart disease, via shared pulmonary-hypertension pathway) has no drug-specific clinical trials, case series, or literature — it is a pure computational hypothesis (L5). The remaining top-ranked candidates in this batch show no credible mechanistic link and are most likely embedding-level false positives. Combined with a blocking gap in official labeling data, this candidate set is not ready to advance past S0.

**To proceed, the following is needed:**
- TFDA package insert / labeling data (warnings, contraindications) — resolves blocking gap DG001
- Confirmed MOA documentation from DrugBank — resolves gap DG002
- A targeted literature/trial search combining "Tadalafil" with "kyphoscoliosis," "secondary pulmonary hypertension," or "cor pulmonale" (current searches return zero hits)
- Formal exclusion of the five hair/craniofacial-disorder candidates and the periodontal-disease candidate from further evaluation, given lack of drug-specific mechanistic or literature support
- If pursuing the pulmonary-hypertension hypothesis, a retrospective cohort or case-series protocol in restrictive lung disease-associated PH patients, rather than a de novo prospective trial at this evidence stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

