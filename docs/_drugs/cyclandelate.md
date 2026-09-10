---
layout: default
title: Cyclandelate
parent: 僅模型預測 (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Cyclandelate
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

# Cyclandelate: From Peripheral Vascular Disease to Migraine Prophylaxis

## One-Sentence Summary

> Cyclandelate (brand name Cyclospasmol) is a peripheral vasodilator historically used for circulatory disorders such as peripheral vascular disease and intermittent claudication.
> Among 10 TxGNN-predicted indications, **migraine disorder** stands out as the best-supported candidate, with a TxGNN score of **99.69%** and **6 randomized controlled trials** (13 publications total) directly evaluating cyclandelate for migraine prophylaxis — making it the only candidate in this evidence pack that clears an L2 evidence bar.

*(Note: this drug generated 10 TxGNN-predicted indications. This report focuses on the strongest-evidenced one, migraine disorder. A summary of the other 9 lower-priority candidates appears near the end.)*

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peripheral Vascular Disease / circulatory disorders (historical, brand name Cyclospasmol) — no structured Taiwan/India license record exists |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.69% (rank 5,863 of candidates) |
| Evidence Level | L2 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, no formal DrugBank/regulatory mechanism-of-action record is available for cyclandelate (flagged as a data gap in this evidence pack). Based on the pharmacological description found in the supporting literature (PMID 8902255), cyclandelate inhibits calcium-induced contraction of vascular smooth muscle, inhibits platelet aggregation induced by thrombin, platelet-activating factor and adenosine, and suppresses provoked serotonin (5-HT) release from platelets. This places it functionally alongside calcium-channel-blocking migraine prophylactics such as flunarizine.

Cyclandelate's original use was as a peripheral/cerebral vasodilator for circulatory disorders (Cyclospasmol). Migraine pathophysiology involves both vascular (cortical spreading depression, vasospasm) and serotonergic mechanisms — both of which overlap with cyclandelate's known pharmacology. This mechanistic bridge is why cyclandelate was actually studied and used as a migraine prophylactic agent in several European countries during the 1980s–1990s, predating this TxGNN prediction by decades — i.e., the model's high score recovers a real, previously established clinical use rather than a purely novel hypothesis.

It's worth noting the evidence is mixed: several earlier RCTs (1987–1998) reported positive prophylactic effects comparable to propranolol, pizotifen, and flunarizine, but the largest and most recent placebo-controlled trial (PMID 11298666, 2001, n=251) failed to meet its primary endpoint. This tempers the otherwise favorable historical signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1573338](https://pubmed.ncbi.nlm.nih.gov/1573338/) | 1992 | RCT | Journal of Medicine | Double-blind study (n=61 after run-in) comparing cyclandelate vs. pizotifen for migraine prophylaxis over 12 weeks; comparable efficacy and tolerance |
| [8902255](https://pubmed.ncbi.nlm.nih.gov/8902255/) | 1996 | RCT | Cephalalgia | Multicentre double-blind study (n=214) vs. placebo and propranolol; cyclandelate's calcium-antagonist profile supports prophylactic potential |
| [9584874](https://pubmed.ncbi.nlm.nih.gov/9584874/) | 1998 | RCT | Functional Neurology | Double-blind placebo-controlled study using contingent negative variation (CNV) to probe central mechanisms of cyclandelate in migraine |
| [11298666](https://pubmed.ncbi.nlm.nih.gov/11298666/) | 2001 | RCT | Cephalalgia | Largest trial (n=251), multicentre placebo-controlled; **primary endpoint (reduction in migraine days) not met** — negative result |
| [7649498](https://pubmed.ncbi.nlm.nih.gov/7649498/) | 1995 | RCT | Functional Neurology | Double-blind study vs. propranolol and placebo; responder/non-responder analysis of cyclandelate's prophylactic effect |
| [3304950](https://pubmed.ncbi.nlm.nih.gov/3304950/) | 1987 | RCT | Drugs | Double-blind trial (n=40) comparing cyclandelate 800mg BID vs. flunarizine 5mg; both significantly reduced migraine symptoms vs. baseline |
| [9829155](https://pubmed.ncbi.nlm.nih.gov/9829155/) | 1998 | Review | Drugs | Practical guide to migraine management and prevention, contextualizing prophylactic agents including calcium antagonists |
| [10463349](https://pubmed.ncbi.nlm.nih.gov/10463349/) | 1999 | Review | Journal of Neurology | Overview of antimigraine drug treatment options for acute attacks and prophylaxis |
| [9139407](https://pubmed.ncbi.nlm.nih.gov/9139407/) | 1997 | Review | Therapeutische Umschau | Migraine diagnosis, differential diagnosis and therapy overview |

---

## India Market Information

Cyclandelate is **not currently marketed in India** — 0 registered licenses on file. No dosage form, brand name, or approved indication text is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information.

No structured key warnings, contraindications, or drug-drug interaction (DDI) data were retrievable for cyclandelate in this evidence pack — the TFDA-equivalent label lookup returned no results, and the local DDI database file was unavailable at query time. This is flagged as a **Blocking** data gap in the evidence pack (DG001): safety data must be obtained before this candidate can pass the initial safety screening stage.

---

## Other Predicted Indications (Screened, Lower Priority)

For completeness, the remaining 9 TxGNN-predicted indications for cyclandelate in this evidence pack, ranked by model score:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|-----------------|-----------------|
| 1 | Prinzmetal angina | 99.80% | L5 | Hold (no clinical/literature evidence) |
| 2 | Raynaud disease | 99.73% | L4 | Research Question (1 old case-series report only) |
| 4 | Migraine with brainstem aura | 99.62% | L4 | Research Question (indirect qEEG studies, not subtype-specific) |
| 5 | Pulmonary hypertension | 99.50% | L5 | Hold (no evidence) |
| 6 | Gout | 99.43% | L5 | Hold (no mechanistic rationale, likely graph noise) |
| 7 | Kyphoscoliotic heart disease | 99.36% | L5 | Hold (no evidence) |
| 8 | Benign prostatic hyperplasia | 99.08% | L5 | Hold (cyclandelate is not an alpha-blocker; no evidence) |
| 9 | Exostosis | 99.06% | L5 | Hold (no mechanistic plausibility, likely graph noise) |
| 10 | Peripheral vascular disease | 99.04% | L3 | Hold (this drug's original historical indication, but pivotal 1984 RCT was negative) |

Notably, rank 10 (peripheral vascular disease) is cyclandelate's *original* indication as Cyclospasmol — and the key RCT (PMID 6364892) found **no effect**, which is a useful sanity check on how much weight to give TxGNN scores alone without evidence triangulation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (for the migraine disorder indication)

**Rationale:**
Migraine prophylaxis is the only indication in this candidate's prediction set with L2 evidence (multiple historical RCTs), reflecting a genuine, previously-established off-label/international use rather than a purely computational artifact. However, the largest and most recent trial (2001) was negative, and the drug is not currently marketed in India, so this is not a "Go" without further work.

**To proceed, the following is needed:**
- Obtain formal safety/label data (DG001, Blocking) — key warnings, contraindications, and DDI profile currently have no source
- Formal DrugBank/mechanism-of-action confirmation (DG002, High) to properly ground the mechanistic rationale
- A structured comparison of the positive (1987–1998) vs. negative (2001) trial results to assess whether efficacy is dose-, population-, or subtype-dependent
- Confirmation of import/registration pathway feasibility, since cyclandelate has zero current registrations in India
- The 9 lower-priority predictions (Prinzmetal angina, Raynaud disease, etc.) should remain on Hold pending any new clinical trial or literature signal — no further action needed unless new evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

