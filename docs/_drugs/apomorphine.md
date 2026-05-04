---
layout: default
title: Apomorphine
parent: 僅模型預測 (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Apomorphine
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

# Apomorphine: From Parkinson's Disease to Perisylvian Polymicrogyria with Cerebellar Hypoplasia and Arthrogryposis

## One-Sentence Summary

Apomorphine is a non-selective dopamine D1/D2 receptor agonist best known as a rescue therapy for acute "off" episodes in Parkinson's disease.
The TxGNN model predicts it may be effective for **Polymicrogyria, Perisylvian, with Cerebellar Hypoplasia and Arthrogryposis**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease (acute hypomobility "off" episodes) |
| Predicted New Indication | Polymicrogyria, Perisylvian, with Cerebellar Hypoplasia and Arthrogryposis |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Apomorphine in this evidence pack. Based on known pharmacological information, Apomorphine is a direct-acting, non-selective dopamine receptor agonist (D1 and D2) that stimulates striatal and limbic dopamine receptors without requiring intact endogenous dopamine synthesis. It is structurally related to both morphine and dopamine, crosses the blood-brain barrier rapidly, and produces central dopaminergic effects used therapeutically in Parkinson's disease off-episode management.

Polymicrogyria with perisylvian distribution, cerebellar hypoplasia, and arthrogryposis is a rare and severe congenital neurodevelopmental syndrome. Its pathogenesis stems from genetic mutations — most notably in *PIK3R2* and *GPR56* — that disrupt neuronal migration and cortical folding during fetal brain development. These structural abnormalities are established prenatally and represent a fundamental disorder of brain architecture, not an ongoing neurotransmitter imbalance amenable to pharmacological correction.

There is no recognized mechanistic pathway connecting dopamine receptor agonism to the correction or amelioration of structural neuronal migration defects. The high TxGNN score (99.75%) most likely reflects indirect node associations in the shared knowledge graph — for example, both entities co-occurring within "neurodevelopment"-related edges — rather than a genuine pharmacological relationship. This prediction should be regarded as a probable false positive, and no drug development action is warranted at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Apomorphine is currently **not marketed in India**. No product registrations or drug authorizations were identified in the regulatory database.

---

## Safety Considerations

**Drug Interactions**: A total of **173 drug interactions** have been documented for Apomorphine. The most clinically significant ones are listed below:

| Interacting Drug | Severity | Source |
|-----------------|----------|--------|
| Alosetron | **Major** | DDInter |
| Cisapride | **Major** | DDInter |
| Dolasetron | **Major** | DDInter |
| Granisetron | **Major** | DDInter |
| Famotidine | Moderate | DDInter |
| Bupropion | Moderate | DDInter |
| Clarithromycin | Moderate | DDInter |
| Levofloxacin | Moderate | DDInter |
| Metoclopramide | Moderate | DDInter |
| Loperamide | Moderate | DDInter |

> Note: The complete warnings and contraindications for Apomorphine were not available in this evidence pack. Please refer to the CDSCO-approved package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Perisylvian polymicrogyria with cerebellar hypoplasia and arthrogryposis is a structural congenital brain malformation caused by prenatal neuronal migration defects (PIK3R2/GPR56 mutations). There is no plausible mechanistic connection to dopaminergic pharmacology, and the complete absence of any clinical trials or literature support confirms this as a knowledge-graph artefact rather than a viable repurposing opportunity.

**To proceed, the following is needed:**
- Preclinical (in vitro or animal model) research to establish any mechanistic link between dopamine receptor activation and neuronal migration pathways (PIK3R2/GPR56)
- MOA data retrieval from DrugBank API (currently unavailable — identified as a High-severity data gap)
- CDSCO/India package insert download and parsing to obtain complete warnings and contraindications (identified as a Blocking data gap for safety assessment)
- Reassessment of higher-ranked evidence-supported indications (e.g., **schizophrenia**, Rank 5, Evidence Level L3) as a more actionable repurposing candidate before investing resources in L5 predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

