---
layout: default
title: Lincomycin
parent: 僅模型預測 (L5)
nav_order: 389
evidence_level: L5
indication_count: 3
---

# Lincomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Lincomycin: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Lincomycin is a lincosamide-class antibiotic traditionally used for serious gram-positive bacterial infections, including those resistant to penicillin.
The TxGNN model predicts it may be effective for **Hyperamylasemia**, yet there are currently **0 clinical trials** and **0 publications** directly supporting this direction.
This prediction is classified as model-only evidence (L5), and caution is warranted before drawing any clinical conclusions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections caused by gram-positive organisms (lincosamide antibiotic) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacology, Lincomycin is a lincosamide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit. Its established clinical use covers serious gram-positive bacterial infections — particularly in penicillin-allergic patients — including skin and soft tissue infections, bone and joint infections, and respiratory tract infections.

The theoretical link to hyperamylasemia is indirect at best. The proposed mechanistic pathway follows a three-step inference: if hyperamylasemia arises secondary to a bacterial infection (e.g., sepsis-related pancreatitis or infectious pancreatitis), then Lincomycin's antibacterial activity could theoretically reduce the infectious burden, which in turn might lower serum amylase. However, this is a highly indirect, multi-step reasoning chain with no pharmacological directness — Lincomycin has no known effect on pancreatic enzyme secretion, acinar cell function, or amylase metabolism.

The high TxGNN score (0.9914) most likely reflects co-occurrence patterns within the knowledge graph between infection-related nodes and amylase-elevation nodes, rather than a true drug-disease pharmacological connection. This type of topological proximity in the graph can produce high scores without biologically meaningful mechanisms. Without any supporting clinical trial or published literature evidence, this prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Lincomycin currently has **no registered products** in the India market. There are no approved licenses on record.

---

## Safety Considerations

**Drug Interactions** (21 interactions identified; showing key entries):

| Interacting Drug | Level | Clinical Note |
|-----------------|-------|---------------|
| Erythromycin | Moderate | Potential antagonism — both bind 50S ribosomal subunit; concurrent use may reduce efficacy of either agent |
| Balsalazide | Moderate | Possible interference with gut flora modulation; monitor gastrointestinal effects |
| Picosulfuric acid | Moderate | May alter gut motility and absorption; timing of administration should be considered |
| Attapulgite | Moderate | Adsorbent clays may reduce oral absorption of Lincomycin; administer at separate times |
| Kaolin | Moderate | Similar adsorption concern as Attapulgite; separate dosing recommended |
| Ethinylestradiol | Moderate | Antibiotic-mediated gut flora disruption may reduce enterohepatic recirculation of estrogens |
| Warfarin | Unknown | Antibiotic use may alter gut flora and affect vitamin K–dependent coagulation; monitor INR |
| Morphine | Unknown | Unknown interaction; exercise caution with concomitant use |
| Metformin | Unknown | Unknown interaction; monitor for unexpected adverse effects |
| Simvastatin | Unknown | Unknown interaction; clinical significance unclear |

> Please refer to the package insert for complete safety information, including key warnings and contraindications (data not available in the current Evidence Pack).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or published literature evidence supporting Lincomycin's use in hyperamylasemia, and the proposed mechanistic link is a speculative three-step indirect inference with no direct pharmacological basis. The TxGNN score, while high, likely reflects graph topology artefacts rather than a genuine drug-repurposing opportunity.

**To proceed, the following is needed:**

- **Detailed MOA data**: Retrieve from DrugBank API (DB01627) to enable proper mechanistic analysis
- **India regulatory status review**: Confirm whether Lincomycin was previously marketed or is under consideration for registration in India
- **Package insert / label retrieval**: Download from CDSCO or originator label to identify key warnings and contraindications (currently a blocking data gap)
- **Mechanistic plausibility study**: Commission a targeted literature review on Lincomycin and amylase / pancreatic function to rule out or confirm any indirect biological connection
- **Etiology stratification**: If pursuing further, define a specific hyperamylasemia subtype (e.g., confirmed infectious pancreatitis) where an antibiotic mechanism could plausibly apply — this would narrow the hypothesis to a testable clinical question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

