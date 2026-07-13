---
layout: default
title: Chlormezanone
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 1
---

# Chlormezanone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

このタスクはCLIレポートではなく、JSONエビデンスパックからの構造化レポート生成です。data-reportスキルは適用対象外と判断し、システムプロンプトの指定フォーマットに従ってレポートを作成します。

---

# Chlormezanone: From Muscle Relaxant / Anxiolytic to Insomnia

## One-Sentence Summary

Chlormezanone is a muscle relaxant and mild anxiolytic (marketed historically as Trancopal), used to relieve secondary sleep disturbances caused by rheumatic muscle stiffness and arthritis.
The TxGNN model predicts it may be effective for **Insomnia (disease)** as a primary indication,
with **0 registered clinical trials** and **3 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Muscle relaxant / anxiolytic — secondary insomnia from rheumatic conditions |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L3 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Chlormezanone (brand name: Trancopal) is a benzothiazine derivative with documented muscle-relaxant and mild tranquilizing properties. Historically, it was used to manage musculoskeletal spasm, anxiety, and the secondary insomnia that accompanies rheumatoid arthritis and osteoarthritis. Its sedative-adjacent profile makes the TxGNN model's prediction of efficacy in insomnia intuitively plausible.

The mechanistic link from rheumatic-secondary insomnia to primary insomnia rests on two proposed pathways: (1) relief of muscle spasm and pain-driven arousal leading to improved sleep continuity, and (2) a central sedating effect that lowers the arousal threshold. However, the precise mechanism of action (MOA) data is not available in this evidence pack. It is therefore not confirmed whether chlormezanone acts via GABAergic pathways (as benzodiazepines and Z-drugs do) or through other CNS-depressant mechanisms.

Critically, all three supporting publications involve **secondary insomnia in patients with rheumatic disease** — not primary insomnia in the general population. The TxGNN model may be extrapolating from this mechanistic overlap, but the clinical gap between "sleeping pill for arthritic pain" and "primary sleep disorder therapy" is significant and would require dedicated study.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [344084](https://pubmed.ncbi.nlm.nih.gov/344084/) | 1978 | Controlled Trial | J Int Med Research | Placebo-controlled double-blind study (n=85, 6 centres). Trancopal significantly improved nightly sleep quality vs placebo over 2 weeks in patients with rheumatic sleep disturbance. |
| [316373](https://pubmed.ncbi.nlm.nih.gov/316373/) | 1979 | Clinical Series | Curr Med Res Opin | Open-label assessment (n=61 general practice). 400 mg chlormezanone nightly for 2 weeks showed steady improvement; 75% rated effectiveness as good/excellent. |
| [6354600](https://pubmed.ncbi.nlm.nih.gov/6354600/) | 1983 | Clinical Series | Curr Med Res Opin | Double-blind crossover study (n=31, rheumatoid/osteoarthritis). 400 mg chlormezanone significantly more effective than placebo (p<0.025) for sleep disturbance; 400 mg preferred over 200 mg. |

---

## India Market Information

Chlormezanone has **no registered licenses** in India. The drug is currently not marketed.

---

## Safety Considerations

**Drug Interactions** (35 interactions identified; source: DDInter):

Major interactions requiring avoidance or close monitoring:

| Interacting Drug | Severity | Clinical Concern |
|-----------------|----------|-----------------|
| Morphine | **Major** | Additive CNS/respiratory depression |
| Codeine | **Major** | Additive CNS/respiratory depression |
| Hydrocodone | **Major** | Additive CNS/respiratory depression |

Notable moderate interactions:

| Interacting Drug | Severity |
|-----------------|----------|
| Bupropion | Moderate |
| Ethanol | Moderate |
| Opium | Moderate |
| Promethazine | Moderate |
| Metoclopramide | Moderate |
| Sibutramine | Moderate |
| Dronabinol / Nabilone | Moderate |
| Antihistamines (Chlorpheniramine, Cetirizine, Brompheniramine, Carbinoxamine, Clemastine, Mepyramine, Doxylamine, Azelastine) | Moderate |
| Dextromethorphan | Moderate |

The pattern of interactions (opioids, antihistamines, CNS depressants, ethanol) is consistent with a sedating/CNS-depressant drug class. Co-administration with opioids carries **Major** risk of compounded respiratory depression.

For complete warnings and contraindications, please refer to the package insert — this data was not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three supporting publications date from 1978–1983, involve secondary insomnia in rheumatic disease patients specifically, and none address primary insomnia — the predicted indication. The drug has no India marketing history, no mechanism of action data, and no current clinical trial activity in this indication.

**To proceed, the following is needed:**

- **MOA clarification**: Confirm whether chlormezanone acts via GABAergic pathways or other CNS mechanisms to assess overlap with established insomnia therapies (BZD, Z-drugs)
- **Safety package**: Obtain current package insert from any jurisdiction where the drug remains available (e.g., France historically) to extract formal contraindications, warnings, and special population restrictions
- **Primary insomnia data**: Identify whether any unpublished or post-1983 data exists for primary (non-rheumatic) insomnia
- **Regulatory standing**: Clarify the current global regulatory status of chlormezanone — the drug was withdrawn in several markets due to severe cutaneous adverse reactions (toxic epidermal necrolysis); this withdrawal history must be thoroughly reviewed before any development decision
- **Benefit-risk reassessment**: Given the historical safety signals, a formal benefit-risk analysis comparing chlormezanone against the modern insomnia therapy landscape (e.g., melatonin receptor agonists, orexin antagonists) is required before any further investment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

