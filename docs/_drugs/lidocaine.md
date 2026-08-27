---
layout: default
title: Lidocaine
parent: 僅模型預測 (L5)
nav_order: 388
evidence_level: L5
indication_count: 10
---

# Lidocaine
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

# Lidocaine: From Local Anesthesia to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Lidocaine is a well-established Na⁺ channel blocker widely used as a local anesthetic and Class Ib antiarrhythmic agent.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**, achieving a prediction score of **99.99%**,
however **no clinical trials** and **no supporting publications** have been identified for this specific indication — evidence is currently limited to model prediction only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local anesthesia / cardiac arrhythmia (no India regulatory registration on file) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on established pharmacology, Lidocaine is a Na⁺ channel blocker that inhibits neuronal membrane depolarization by blocking voltage-gated sodium channels, producing local anesthesia and — at systemic doses — antiarrhythmic effects (Class Ib). Its use as a topical ocular surface anesthetic is well-established in ophthalmic clinical practice worldwide.

In the context of punctate epithelial keratoconjunctivitis (PEK) — a condition characterized by scattered punctate epithelial defects across the corneal and conjunctival surface, often accompanied by ocular discomfort — Lidocaine's analgesic mechanism could theoretically address acute pain arising from exposed corneal nerve endings. Sodium channel blockade may additionally confer mild anti-inflammatory properties by reducing neurogenic inflammation via suppression of neuropeptide release (e.g., Substance P), providing a biologically plausible, albeit indirect, connection to PEK symptom management.

However, this prediction carries a critical biological caveat. PEK arises from diverse etiologies including drug toxicity, post-infectious sequelae, and dry eye disease. Prolonged topical application of local anesthetics — including Lidocaine — is well-documented to inhibit corneal epithelial cell mitosis and delay wound healing, potentially worsening the very condition it might aim to treat. The high TxGNN score most likely reflects broad network-level similarity across ocular surface inflammation nodes in the knowledge graph rather than a direct, specific therapeutic mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or publications directly support Lidocaine for punctate epithelial keratoconjunctivitis, and the well-documented corneal epitheliotoxicity associated with prolonged topical anesthetic use represents a mechanistic safety concern that must be addressed before this indication can advance.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank to formally characterize anti-inflammatory potential
- India package insert retrieval and review for ophthalmic safety warnings and contraindications (currently blocking)
- Preclinical data distinguishing short-term analgesic benefit from long-term epithelial toxicity in PEK models
- Drug interaction (DDI) database query to be re-run after correcting the missing DDInter file path (`ddinter_code_A.csv`)
- Reassessment once India market status is clarified — Lidocaine formulations (gel, solution) may be available under different registration pathways not captured in the current data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

