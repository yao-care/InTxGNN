---
layout: default
title: Primidone
parent: 僅模型預測 (L5)
nav_order: 499
evidence_level: L5
indication_count: 10
---

# Primidone
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

Using the **data-report** discipline (present exactly what's in the Evidence Pack, no fabrication, no silent omission of caveats the data itself raises) to produce this report.

A note before the report: per the format rules, `predicted_indications[0]` (**trigeminal nerve neoplasm**, TxGNN rank 261) is the designated subject for the Quick Overview / evidence tables. However, the Evidence Pack's own `repurposing_rationale` for this candidate explicitly labels it as likely **knowledge-graph noise** (no trials, no literature, no plausible mechanism). I've reported it as instructed, stated that caveat prominently, and appended a full ranked table of the other 9 candidates in this multi-indication pack — including **audiogenic seizures**, which has the strongest actual evidence (L3/S1) — so the reader isn't misled by the raw TxGNN score alone.

---

# Primidone: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Primidone is a barbiturate-derivative anticonvulsant, established for the treatment of epilepsy (partial and generalized tonic-clonic seizures). The TxGNN model's top-ranked prediction for this drug is **Trigeminal Nerve Neoplasm**, but this candidate is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic rationale flags it as a likely false-positive artifact of knowledge-graph node proximity rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy — partial and secondarily generalized tonic-clonic seizures (no Taiwan license text available; drug is not locally marketed) |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Primidone in this Evidence Pack. Based on known pharmacology, Primidone (and its active metabolite phenobarbital) is a GABA-A receptor positive modulator — a mechanism that underlies its established efficacy in epilepsy and, more broadly, in various seizure and reflex-epilepsy syndromes.

Trigeminal nerve neoplasm, however, is a structural tumor of the trigeminal nerve, not a seizure or excitability disorder. There is no established biological pathway connecting GABAergic neuronal inhibition to tumor growth or regression in this tissue. The Evidence Pack's own rationale for this candidate states that the high TxGNN score most plausibly arises from the knowledge graph's proximity between "trigeminal nerve neoplasm" and unrelated but lexically/graph-adjacent nodes (e.g., trigeminal neuralgia), producing a scoring artifact rather than a genuine repurposing signal.

Given the complete absence of clinical trials or literature, and the lack of a coherent mechanistic link, this candidate should not be prioritized for further research investment at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

Primidone is **not currently marketed in Taiwan** — 0 license registrations were found (`total_licenses: 0`). No dosage form, brand name, or approved-indication text is available from local regulatory data.

---

## Safety Considerations

**Drug Interactions**: DDI screening returned **273 total known interactions** for Primidone (query completed). Representative entries from the returned sample include:

- **Major**: Morphine, Eliglustat
- **Moderate**: Doxycycline, Hydrocortisone, Cholecalciferol, Pioglitazone, Bupropion, Aprepitant, Triamcinolone, Dexamethasone, Betamethasone, Metronidazole, Calcifediol, Calcitriol, Canagliflozin, Saxagliptin, Difenoxin, Diphenoxylate, Dronabinol
- **Minor**: Cimetidine

Given Primidone's known enzyme-inducing effect (as an active barbiturate/phenobarbital precursor), interactions of this scale are expected and consistent with its known pharmacological class; the two Major-level interactions (Morphine, Eliglustat) warrant particular attention in any future clinical protocol.

Key warnings and contraindications data were not available in this Evidence Pack; please refer to the package insert for that information.

---

## Other Predicted Indications in This Evidence Pack

This is a multi-indication evidence pack (`TW-DB00794-multi`) covering 10 ranked TxGNN predictions. For completeness, the full ranked list is below — several candidates carry materially more evidentiary support than the top-ranked, purely score-driven candidate above.

| Rank | Disease | TxGNN Score | Trials / Literature | Evidence Level | Recommendation |
|------|---------|------|------|------|------|
| 1 | Trigeminal nerve neoplasm | 99.99% | 0 / 0 | L5 | Hold |
| 2 | Orgasm-induced seizures | 99.99% | 0 / 0 | L5 | Hold |
| 3 | Thinking seizures | 99.99% | 0 / 1 | L4 | Research Question |
| 4 | Startle epilepsy | 99.99% | 0 / 1 | L4 | Research Question |
| 5 | Eating seizures | 99.99% | 0 / 0 | L5 | Hold |
| 6 | Micturation-induced seizures | 99.99% | 0 / 15 | Pending | Pending |
| **7** | **Audiogenic seizures** | 99.99% | 0 / 12 | **L3** | **Research Question (S1)** |
| 8 | Reading seizures | 99.99% | 0 / 9 | L4 | Research Question |
| 9 | Trigeminal neuralgia | 99.98% | 0 / 0 | L4 | Hold |
| 10 | Beta-ketothiolase deficiency | 99.96% | 0 / 0 | L5 | Hold |

**Audiogenic seizures (rank 7)** is the strongest candidate in this pack: Primidone/phenobarbital's GABA-A mechanism is a classic pharmacological match for this reflex-epilepsy model, it has already reached decision stage S1, and it is backed by 12 literature entries (including direct animal-model studies of anticonvulsants in audiogenic seizure suppression). This candidate — not the rank-1 TxGNN score — is the more scientifically defensible starting point for any further repurposing work on Primidone.

---

## Conclusion and Next Steps

**Decision: Hold** (for Trigeminal Nerve Neoplasm, the designated top-ranked candidate)

**Rationale:**
The top TxGNN-ranked indication has zero supporting trials or literature and lacks a plausible mechanistic link to Primidone's known pharmacology; the model's own rationale attributes the high score to graph-proximity noise rather than a genuine biological signal.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action data via DrugBank API — currently a High-severity data gap (DG002)
- If pursuing repurposing research on Primidone at all, redirect attention to **audiogenic seizures** (rank 7, L3/S1), which has substantively stronger mechanistic and literature support than the top-scored candidate
- Full-text review of the 12 audiogenic-seizure and 9 reading-seizure literature entries to resolve "pending" classification/relevance fields before any further scoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

