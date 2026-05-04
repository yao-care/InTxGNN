---
layout: default
title: Lamotrigine
parent: 僅模型預測 (L5)
nav_order: 273
evidence_level: L5
indication_count: 9
---

# Lamotrigine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Lamotrigine: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Lamotrigine is a second-generation broad-spectrum antiepileptic drug (AED) widely used globally for epilepsy and bipolar disorder, though it holds no current marketing authorisation in India.
The TxGNN model assigns it a top-ranked prediction score of **99.97%** for **Trigeminal Nerve Neoplasm**,
yet **no clinical trials** and **no published literature** currently support this specific direction — placing it at evidence level L5.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from India regulatory data (globally approved for epilepsy and bipolar disorder) |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on the extensive clinical literature retrieved during evidence collection, Lamotrigine is known to exert its antiseizure effect primarily by blocking voltage-gated sodium channels (NaV1.x), thereby stabilising neuronal membranes and preventing abnormal repetitive firing. It also suppresses presynaptic glutamate release. These mechanisms underpin its efficacy across focal epilepsy, generalised epilepsy, Lennox-Gastaut syndrome, and trigeminal neuralgia — all conditions driven by neuronal hyperexcitability rather than neoplastic proliferation.

Trigeminal nerve neoplasm, by contrast, involves abnormal cell growth along the trigeminal nerve (cranial nerve V). This is a fundamentally different pathophysiological process from aberrant electrical discharge. There is no established biological rationale for why sodium channel stabilisation or glutamate inhibition would suppress tumour growth, invasion, or survival in trigeminal nerve tumours. The extremely high TxGNN score (0.9997) most likely reflects the structural proximity of the "trigeminal nerve" node to pain and seizure pathway nodes in the knowledge graph, rather than a genuine pharmacological relationship to neoplastic disease.

It is worth noting that Lamotrigine's second-ranked TxGNN prediction — **trigeminal neuralgia** (score: 99.89%, L3 evidence, 19 publications) — is mechanistically far better supported. Trigeminal neuralgia is driven by the same NaV-mediated hyperexcitability that Lamotrigine directly targets, and published literature explicitly documents its clinical use for this condition. This contrast underscores that the rank-1 prediction for trigeminal nerve neoplasm is likely a knowledge-graph artefact and not a biologically meaningful repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Lamotrigine currently holds **no marketing authorisations** in India. There are zero registered licenses in the database, and the drug is classified as **not marketed**.

---

## Safety Considerations

**Drug Interactions**: 149 drug interactions have been identified (source: DDInter). Key interactions are summarised below:

| Interacting Drug | Severity Level |
|-----------------|---------------|
| Morphine | Moderate |
| Morphine (liposomal) | Moderate |
| Opium | Moderate |
| Dronabinol | Moderate |
| Nabilone | Moderate |
| Metoclopramide | Moderate |
| Orlistat | Moderate |
| Metformin | Minor |
| Calcitriol, Glimepiride, Doxycycline, Clotrimazole, Phentermine, Pantoprazole, Mesalazine, Omeprazole, Sucralfate, Rosiglitazone, Lansoprazole, Vancomycin | Unknown level |

Please refer to the full package insert for complete warnings and contraindications, which were not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial evidence and no published literature supporting the use of Lamotrigine in trigeminal nerve neoplasm. The TxGNN rank-1 score almost certainly reflects graph-level topological proximity (trigeminal nerve node adjacent to seizure/pain pathways) rather than a genuine mechanistic or clinical repurposing signal. Sodium channel blockade has no established antitumour rationale in this cancer type.

**To proceed, the following is needed:**

- A credible biological hypothesis explaining why NaV channel blockade or glutamate inhibition would affect trigeminal nerve tumour growth, survival, or progression
- Preclinical (in vitro/in vivo) data testing Lamotrigine in trigeminal nerve neoplasm or neurofibroma models
- Graph topology audit: confirm whether the TxGNN high score is an artefact of trigeminal nerve node connectivity to epilepsy/pain pathways
- Retrieval of Lamotrigine MOA data from DrugBank (currently a High-severity data gap)
- Retrieval of TFDA/CDSCO package insert to obtain formal warnings and contraindications (currently a Blocking-severity data gap)

---

> **Note for research teams**: If the objective is to identify the most actionable repurposing candidate from this evidence pack, **Trigeminal Neuralgia** (rank 2, TxGNN score 99.89%, Evidence Level L3, 19 publications including clinical guidelines and direct comparative trials of Lamotrigine vs. Carbamazepine) represents a substantially stronger starting point and warrants a dedicated evaluation report.

---

*This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application. Data cut-off: 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

