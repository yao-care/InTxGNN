---
layout: default
title: Rizatriptan
parent: 僅模型預測 (L5)
nav_order: 742
evidence_level: L5
indication_count: 2
---

# Rizatriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Rizatriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Rizatriptan is a selective 5-HT1B/1D receptor agonist established for the acute treatment of migraine. The TxGNN model predicts potential effectiveness for **Migraine with Brainstem Aura** (formerly "basilar-type migraine"), but this specific subtype has historically been treated as a relative contraindication for triptans, and no dedicated clinical trials or Taiwan regulatory data currently support this use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute treatment of migraine (general, based on drug class/mechanism; no Taiwan-approved license on file) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Rizatriptan is a selective 5-HT1B/1D receptor agonist. Its mechanism — vasoconstriction of cranial vessels and inhibition of trigeminovascular release of calcitonin gene-related peptide (CGRP) — is well established for typical migraine (with or without aura), which explains the model's confidence score.

However, the predicted indication, "migraine with brainstem aura," is a distinct clinical subtype (previously termed basilar-type migraine) involving aura symptoms attributable to brainstem/vertebrobasilar territory dysfunction. Because triptans theoretically carry a risk of vasoconstriction in the vertebrobasilar circulation, this subtype has long been considered a relative contraindication for the triptan class, and major RCTs have systematically excluded these patients. While recent guidelines have partially relaxed this stance, direct controlled-trial evidence in this specific population remains absent — meaning the TxGNN prediction reflects a plausible but historically cautioned mechanistic extension rather than a validated new use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15209688](https://pubmed.ncbi.nlm.nih.gov/15209688/) | 2004 | RCT | Headache | Placebo-controlled study showing efficacy of rizatriptan when administered early in a migraine attack |
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Clinical Report | Headache | Reports on triptan use (including rizatriptan) in basilar-type migraine and migraine with prolonged aura — the most directly relevant evidence found, but not a controlled trial |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society evidence assessment of acute migraine pharmacotherapies, including rizatriptan |
| [11687054](https://pubmed.ncbi.nlm.nih.gov/11687054/) | 2001 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Systematic review of rizatriptan efficacy/safety for acute migraine treatment |
| [17636717](https://pubmed.ncbi.nlm.nih.gov/17636717/) | 2007 | Systematic Review (Cochrane, Withdrawn) | Cochrane Database Syst Rev | Withdrawn update of the above Cochrane review on rizatriptan for acute migraine |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Review/Meta-analysis | J Headache Pain | Compares frovatriptan vs. rizatriptan, zolmitriptan, and almotriptan specifically in migraine **with aura** |
| [16336021](https://pubmed.ncbi.nlm.nih.gov/16336021/) | 2005 | Review (Pharmacoeconomic) | PharmacoEconomics | Reviews efficacy/cost-utility of rizatriptan 5mg/10mg vs. other triptans and ergotamine/caffeine |
| [15613223](https://pubmed.ncbi.nlm.nih.gov/15613223/) | 1999 | PK Study | Headache | Pharmacokinetics of rizatriptan during and between migraine attacks (gastric stasis effects) |
| [23695053](https://pubmed.ncbi.nlm.nih.gov/23695053/) | 2013 | Review/Comparative | Neurol Sci | Efficacy of frovatriptan/rizatriptan/zolmitriptan in hypertensive vs. normotensive migraine patients |
| [24867847](https://pubmed.ncbi.nlm.nih.gov/24867847/) | 2014 | Review/Comparative | Neurol Sci | Efficacy of frovatriptan/rizatriptan/zolmitriptan in normal-weight vs. obese migraine patients |

---

## Taiwan Market Information

Rizatriptan is currently **not marketed in Taiwan** — no license registrations are on file (`total_licenses: 0`). No approved indication text is available for local reference.

---

## Safety Considerations

**Drug Interactions** (80 total interactions on file; key Major-level interactions below, primarily serotonergic agents with theoretical serotonin syndrome risk):

- **Major**: Lorcaserin, Dolasetron, Palonosetron, Ondansetron, Granisetron, Dexfenfluramine, Fenfluramine, Sibutramine
- **Moderate**: Morphine, Morphine (liposomal)
- Multiple additional interactions of **Unknown** severity are on file (e.g., Pantoprazole, Omeprazole, Metformin, Prednisone) and require individual review.

Taiwan-specific label warnings and contraindications are not currently available and require retrieval from the official TFDA package insert before further safety evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Migraine with brainstem aura has historically been treated as a relative contraindication for triptans due to theoretical vertebrobasilar vasoconstriction risk, and no dedicated clinical trials support this specific use. Combined with the absence of Taiwan market registration and missing TFDA safety label data, the evidence is insufficient to advance beyond a research question at this stage.

**To proceed, the following is needed:**
- TFDA package insert data (warnings/contraindications) — currently a blocking data gap
- Confirmed mechanism of action detail from DrugBank
- Dedicated clinical evidence (trial or structured case series) in patients specifically diagnosed with migraine with brainstem aura
- Assessment of regulatory pathway, given the drug is not currently registered in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

