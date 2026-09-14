---
layout: default
title: Zuclopenthixol
parent: 僅模型預測 (L5)
nav_order: 904
evidence_level: L5
indication_count: 9
---

# Zuclopenthixol
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

# Zuclopenthixol: From Antipsychotic Use to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

> Zuclopenthixol is described in the evidence pack's own rationale notes as a D1/D2 dopamine receptor antagonist used as an antipsychotic, though no formal original-indication or India licensing record exists for this drug.
> The TxGNN model predicts it may be effective for **Retinal Dystrophy with or without Extraocular Anomalies**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic notes flag the top hits as likely embedding artifacts rather than genuine biological signals.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented — drug holds no market license in India |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (original_moa is unresolved). Based on the information embedded in the repurposing rationale notes, Zuclopenthixol is a D1/D2 dopamine receptor antagonist, consistent with its known clinical use as an antipsychotic. No original indication text was extractable, since the drug is not currently marketed in India and no licenses are on file.

Critically, for the top-ranked candidate (Retinal Dystrophy with or without Extraocular Anomalies), the model's own rationale states there is **no known mechanistic link**: this is a genetic photoreceptor-gene disorder, and dopamine receptor antagonism has no established pathophysiological connection to it. The rationale explicitly flags the high score as a **suspected knowledge-graph embedding artifact** rather than a genuine biological signal.

This pattern repeats across all nine top-ranked candidates in this pack — hydranencephaly, congenital glycosylation disorder, Charcot-Marie-Tooth type 1G, three distinct myopia subtypes, polymicrogyria, and glycine encephalopathy. Several are developmental or genetic disorders with no plausible connection to dopamine antagonism; the myopia-related candidates are even noted as potentially **directionally implausible**, since retinal dopamine signaling is thought to *inhibit* axial elongation, meaning a D2 antagonist could theoretically worsen rather than improve the condition. None of the nine candidates have any supporting clinical trial or literature evidence, and all are scored L5 with a "Hold" recommendation by the scoring engine itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## India Market Information

Zuclopenthixol currently holds no marketing authorization in India (0 registrations on file). No product name, dosage form, or approved indication information is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predicted indication has zero supporting clinical trials or literature (Evidence Level L5), and the model's own repurposing rationale identifies it as a likely knowledge-graph artifact with no plausible mechanistic basis. This assessment is consistent across all nine top-ranked candidates in the pack, several of which are further disqualified by directional implausibility or population-specific safety concerns (e.g., antipsychotic use in pregnancy-related developmental disorders). Combined with the absence of India market presence and unresolved safety/MOA data gaps, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): official label warnings and contraindications, required before any S1 safety screening
- Resolve DG002 (High): confirmed mechanism of action via DrugBank API
- Independent mechanistic or preclinical validation to rule out KG-embedding artifact before further scoring
- Re-evaluation against lower-ranked or alternative TxGNN candidates with actual trial/literature support, given the uniform weakness of the current top-9 list
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

