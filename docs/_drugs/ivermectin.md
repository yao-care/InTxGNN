---
layout: default
title: Ivermectin
parent: 僅模型預測 (L5)
nav_order: 262
evidence_level: L5
indication_count: 10
---

# Ivermectin
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

# Ivermectin: From Antiparasitic Therapy to Vulvovaginal Candidiasis

## One-Sentence Summary

Ivermectin is a broad-spectrum macrocyclic lactone antiparasitic agent, established for treating strongyloidiasis, onchocerciasis, and scabies.
The TxGNN model predicts it may be effective for **Vulvovaginal Candidiasis** with a score of **99.95%**,
yet **0 clinical trials** and **0 publications** currently support this direction — placing this prediction at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antiparasitic infections (strongyloidiasis, onchocerciasis, scabies) |
| Predicted New Indication | Vulvovaginal Candidiasis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the source data. Based on established pharmacological knowledge, Ivermectin is a macrocyclic lactone that works by binding selectively to glutamate-gated chloride channels (GluCl) and GABA-gated ion channels in the nerve and muscle cells of invertebrates — structures that are absent in fungi, mammals, and most bacteria. This highly targeted action is the basis for its safety in humans and its established efficacy against helminths and ectoparasites (e.g., *Strongyloides stercoralis*, *Onchocerca volvulus*, *Sarcoptes scabiei*).

Vulvovaginal candidiasis is caused by *Candida* species (predominantly *Candida albicans*), a eukaryotic fungal pathogen. *Candida* cells do not possess GluCl channels or the relevant invertebrate-type GABA receptors that ivermectin targets. A handful of in vitro studies have noted weak antifungal signals, but the minimum inhibitory concentrations (MICs) reported are orders of magnitude higher than plasma concentrations achievable with standard clinical dosing — making clinical translation biologically implausible under current evidence.

The TxGNN model's high prediction score (99.95%) most likely reflects shared network topology in the knowledge graph — for instance, co-occurrence of drug–disease nodes within gynecological or infectious disease clusters — rather than a pharmacologically meaningful mechanistic link. This is a textbook case where a high statistical prediction score and biological plausibility diverge sharply, and where the evidence gap cannot be bridged without foundational mechanistic work.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ivermectin in vulvovaginal candidiasis.

---

## Literature Evidence

Currently no related literature available for Ivermectin in vulvovaginal candidiasis.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** All safety fields (key warnings, contraindications, drug interactions) were flagged as data gaps in this evidence pack. Ivermectin is known from general pharmacology to carry important precautions including avoidance in patients with CNS disorders affecting the blood-brain barrier, pregnancy (animal teratogenicity data), and children weighing less than 15 kg. These should be reviewed from the official prescribing information before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score of 99.95%, the biological case for Ivermectin in vulvovaginal candidiasis is critically weak — *Candida* lacks the invertebrate ion channel targets that ivermectin acts upon, no clinical trials have been initiated, and no supporting publications exist. Advancing this candidate without foundational mechanistic evidence would not be scientifically justified.

**To proceed, the following is needed:**
- **Mechanistic feasibility study**: In vitro MIC/MFC assays of ivermectin against *C. albicans* at clinically achievable plasma concentrations (typically < 100 ng/mL)
- **Secondary mechanism exploration**: Assess whether ivermectin's importin α/β nuclear transport inhibition or P-glycoprotein modulation has any relevance to *Candida* pathogenesis or azole resistance
- **Safety data retrieval**: Obtain and parse the full prescribing information to populate key warnings, contraindications, and drug interaction profile (currently all data gaps)
- **MOA documentation**: Query DrugBank API for the full mechanistic profile (flagged as High severity data gap DG002)
- **Regulatory feasibility**: Confirm whether any regulatory pathway exists in India for an unregistered antiparasitic being repurposed for a fungal indication

---

> ⚠️ *This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

