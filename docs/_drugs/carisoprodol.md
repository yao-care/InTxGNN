---
layout: default
title: Carisoprodol
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 1
---

# Carisoprodol
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

# Carisoprodol: From Musculoskeletal Pain to Insomnia

## One-Sentence Summary

Carisoprodol is a centrally-acting skeletal muscle relaxant approved in several markets for short-term relief of acute musculoskeletal pain and spasm.
The TxGNN model predicts it may be effective for **Insomnia**, with a high prediction score of **99.02%**.
However, actual clinical evidence supporting this repurposing direction is very limited: **0 clinical trials** and only **1 tangentially related publication** were identified, placing this at an early exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Skeletal muscle relaxant for acute musculoskeletal pain and spasm |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.02% |
| Evidence Level | L4 — Mechanism/preclinical basis only |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Carisoprodol is a prodrug of **meprobamate**: after oral administration, it is metabolised in the liver to meprobamate, a compound known to act as a **positive allosteric modulator of GABA-A receptors**. This GABAergic central nervous system depression produces sedation and anxiolysis in addition to muscle relaxation — a pharmacological profile that, in principle, overlaps with the mechanism of older hypnotic-sedative agents.

Because insomnia is partly mediated by insufficient GABAergic inhibitory tone (the same pathway targeted by benzodiazepines and Z-drugs), the TxGNN knowledge graph can plausibly link carisoprodol's mechanism to sleep-onset or sleep-maintenance benefit. The model's high score (0.990) most likely reflects this mechanistic similarity rather than observed clinical evidence.

However, this theoretical connection must be weighed against a critical safety concern: meprobamate carries a **high risk of physical dependence, tolerance, and abuse**, which is precisely why it was displaced by benzodiazepines and subsequently by non-benzodiazepine hypnotics (zolpidem, eszopiclone, etc.) decades ago. The prediction is mechanistically coherent but clinically superseded.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Carisoprodol in insomnia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22963024](https://pubmed.ncbi.nlm.nih.gov/22963024/) | 2012 | Review / Clinical Overview | American Family Physician | Review of nocturnal leg cramps; notes that recurrent, painful calf-muscle tightening can cause **severe insomnia** in up to 60% of affected adults; carisoprodol appears on the list of associated medications — indirectly linking the drug to the insomnia symptom burden rather than its treatment |

> **Note:** This publication discusses insomnia as a *consequence* of nocturnal leg cramps, not as an indication directly treated by carisoprodol. Its relevance to the repurposing hypothesis is indirect.

---

## India Market Information

Carisoprodol is **not currently registered or marketed in India**. No product authorisations were identified.

---

## Safety Considerations

**Drug Interactions (158 interactions on record):**

Key interactions by severity level:

| Severity | Interacting Drug | Clinical Implication |
|----------|-----------------|---------------------|
| **Major** | Morphine | Additive CNS/respiratory depression; avoid combination |
| **Major** | Morphine (liposomal) | Additive CNS/respiratory depression; avoid combination |
| **Moderate** | Dronabinol | Enhanced CNS depression |
| **Moderate** | Nabilone | Enhanced CNS depression |
| **Moderate** | Opium | Additive sedation and respiratory risk |
| **Moderate** | Sibutramine | CNS interaction |
| **Moderate** | Difenoxin | Enhanced CNS depression |
| **Moderate** | Diphenoxylate | Enhanced CNS depression |
| **Moderate** | Metoclopramide | CNS interaction |

> An additional 149 interactions of Unknown or lower severity are on record. The pattern of Major interactions with opioids and Moderate interactions with CNS-active agents is consistent with carisoprodol's broad central depressant profile via its meprobamate metabolite.

> Please refer to the package insert for complete warnings and contraindications — these data were not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the GABAergic mechanism of carisoprodol's active metabolite (meprobamate) provides a plausible theoretical basis for sedation/sleep promotion, there is **zero clinical trial evidence** and only **one indirectly relevant review paper** for the insomnia indication. Furthermore, the abuse and dependence liability of meprobamate creates a significant safety barrier that modern insomnia pharmacotherapy has already addressed with safer alternatives.

**To proceed, the following is needed:**

- **Formal package insert review** — Obtain and parse the full prescribing information (warnings, contraindications, abuse-potential labelling) before any clinical assessment can begin (currently a Blocking data gap)
- **Mechanism of action documentation** — Confirm MOA via DrugBank API or primary pharmacology literature; specifically quantify GABA-A binding affinity relative to approved hypnotics
- **Regulatory status clarification** — Assess whether India's CDSCO has any stance on meprobamate/carisoprodol given its international controlled-substance status (Schedule IV in the US; banned in several EU countries)
- **Abuse liability risk assessment** — Any repurposing proposal must address whether scheduling restrictions would make clinical development or market access feasible
- **Comparative effectiveness analysis** — Benchmark against existing insomnia treatments (zolpidem, eszopiclone, lemborexant) to determine whether any unmet need remains that carisoprodol could plausibly address
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

