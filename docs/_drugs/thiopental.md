---
layout: default
title: Thiopental
parent: 僅模型預測 (L5)
nav_order: 824
evidence_level: L5
indication_count: 10
---

# Thiopental
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

Using no additional skill — this is a direct report-drafting task per the loaded prompt template; proceeding directly.

# Thiopental: From General Anesthesia Induction to Trichotillomania

## One-Sentence Summary

Thiopental is a classic ultra-short-acting barbiturate historically used for intravenous induction of general anesthesia (and, off-label, for barbiturate coma in refractory status epilepticus). The TxGNN model predicts it may be relevant to **Trichotillomania**, but this signal currently has **0 clinical trials** and **0 publications** in support — it is a pure model-generated hypothesis with no empirical or mechanistic backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved-indication text available in the regulatory dataset (drug not marketed in India); classically used as an ultra-short-acting IV anesthetic induction agent (barbiturate class) |
| Predicted New Indication | Trichotillomania |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not directly available for this drug in the evidence pack (flagged as a High-severity data gap). However, cross-referencing the rationale text attached to other predicted indications in this same evidence pack confirms Thiopental acts as a **GABA-A receptor positive allosteric modulator**, the standard mechanism underlying barbiturate sedative-hypnotic and anesthetic effects.

Trichotillomania (compulsive hair-pulling disorder) is currently understood primarily through dysregulation of glutamatergic and serotonergic/dopaminergic circuits, and treatment research has focused on agents like N-acetylcysteine, SSRIs, and glutamate modulators — not GABA-A potentiators. The evidence pack itself is explicit on this point: **"no known mechanistic link connects trichotillomania to GABA-A receptor modulation; this is a pure model prediction with no supporting data."**

In other words, the high TxGNN score reflects graph-embedding proximity in the knowledge graph, not a validated pharmacological rationale. This prediction should be treated as a hypothesis-generating signal only, not as evidence of plausible clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Thiopental has **no regulatory license records** in the current dataset — market status is "Not Marketed" with 0 total registrations. No authorization number, product name, dosage form, or approved indication text is available for India.

---

## Safety Considerations

Structured key-warning and contraindication text is not available in this dataset (regulatory label data collection is listed as a **Blocking** data gap — TFDA/label PDF not yet retrieved/parsed). Please refer to the official package insert for warnings and contraindications.

**Drug Interactions** (from DDInter; 20 of 45 total documented interactions shown):

| Interacting Drug | Severity |
|---|---|
| Ethanol | Major |
| Warfarin | Major |
| Doxycycline | Moderate |
| Morphine | Moderate |
| Dronabinol | Moderate |
| Nabilone | Moderate |
| Nitisinone | Moderate |
| Methylene blue | Moderate |
| Iodide I-131 | Moderate |
| Iodide I-123 | Moderate |
| Codeine | Moderate |
| Cetirizine | Moderate |
| Hydrocodone | Moderate |
| Dextromethorphan | Moderate |
| Carbinoxamine | Moderate |
| Clemastine | Moderate |
| Pyridoxine | Minor |
| Cimetidine | Minor |
| Sulfasalazine | Minor |
| Promethazine | Minor |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Trichotillomania) has no clinical trial or literature support and no plausible mechanistic link per the evidence pack itself — it is a model-only signal (L5, Decision Stage S0). Combined with a Blocking-severity gap in regulatory label/safety data, this candidate cannot currently pass an S1 safety screen.

**To proceed, the following is needed:**
- TFDA/Indian product label (warnings, contraindications) to close the Blocking data gap (DG001)
- Confirmed mechanism-of-action data from DrugBank (DG002)
- Independent mechanistic or preclinical rationale connecting GABA-A modulation to trichotillomania before any further evidence collection is warranted

**Note:** Among the other 9 candidates in this evidence pack, *frontal lobe epilepsy* (rank 2) shows comparatively stronger — though still preliminary — support (L4, "Research Question" stage, tied to the known off-label use of thiopental-induced barbiturate coma in refractory status epilepticus) and may be a more productive avenue than the top-ranked trichotillomania signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

