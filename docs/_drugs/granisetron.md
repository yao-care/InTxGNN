---
layout: default
title: Granisetron
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 10
---

# Granisetron
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

# Granisetron: From Antiemetic Use to Manic Bipolar Affective Disorder

## One-Sentence Summary

Granisetron is a selective 5-HT3 receptor antagonist, pharmacologically used to control nausea and vomiting via action on the peripheral and medullary vomiting center. TxGNN predicts a possible link to **manic bipolar affective disorder**, but this direction is currently supported by **0 clinical trials** and **0 publications** — a pure computational (L5) prediction with no real-world evidence behind it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No India-market indication text available (drug not marketed); pharmacologically classified as an antiemetic (5-HT3 receptor antagonist) |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| India Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data is not available for Granisetron in this evidence pack. Based on the information that is available, Granisetron acts as a selective 5-HT3 receptor antagonist, working mainly on peripheral vagal afferents and the medullary vomiting center — the pharmacological basis for its established antiemetic use.

The proposed link to manic bipolar affective disorder rests on the broader theory that serotonergic signaling participates in mood regulation (a hypothesis explored with other 5-HT3 antagonists such as ondansetron in psychiatric research). However, mania is understood to be driven primarily by dopaminergic and noradrenergic dysregulation, not 5-HT3 antagonism specifically, so there is no direct pharmacological pathway connecting Granisetron's known action to this indication.

Given this gap, the TxGNN score likely reflects indirect co-occurrence of serotonin-related nodes in the knowledge graph rather than a validated pharmacological mechanism. This caution extends to the other 9 candidates TxGNN generated for Granisetron (e.g., conjunctivitis, angioedema, urticaria, bronchitis) — each carries the same L5/Hold status, and several of their own mechanistic rationales explicitly flag the prediction as likely knowledge-graph noise rather than a genuine repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

**Drug Interactions**: DrugBank/DDInter records 461 total interactions for Granisetron. Of the sample reviewed, the following are flagged **Major**:
- Fentanyl, Dextromethorphan, Tramadol, Alfentanil, Almotriptan, Sumatriptan, Amiodarone, Amisulpride, Amitriptyline, Anagrelide

The following are flagged **Moderate**:
- Abametapir (topical), Abiraterone, Dihydrocodeine, Codeine, Famotidine, Formoterol, Adenosine, Salbutamol, Alfuzosin, Propofol

Given the volume of interactions (461 total) and the presence of multiple Major-level flags involving opioids, triptans, and QT-prolonging agents, a full interaction screen against the patient's concurrent medication list is warranted before any use.

Structured warnings and contraindications (e.g., from a TFDA-approved label) are not currently available for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (manic bipolar affective disorder) has zero supporting clinical trials or literature, and the drug's own mechanism (5-HT3 antagonism) has no established pathophysiological link to mania. This is a pure TxGNN computational signal (L5) that the underlying evidence pack itself flags as possible knowledge-graph noise.

**To proceed, the following is needed:**
- TFDA-equivalent label data (warnings/contraindications) — currently a Blocking data gap preventing any S1 safety review
- Structured mechanism-of-action data from DrugBank — currently a High-severity data gap
- Any preclinical or mechanistic studies directly linking 5-HT3 antagonism to mood/mania pathways, if this direction is to be pursued further
- Confirmation of India market/regulatory status, since the drug is currently unmarketed with zero registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

