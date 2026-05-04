---
layout: default
title: Minodronic Acid
parent: 僅模型預測 (L5)
nav_order: 354
evidence_level: L5
indication_count: 7
---

# Minodronic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Minodronic Acid: From Osteoporosis to Pseudo-von Willebrand Disease

## One-Sentence Summary

Minodronic acid is a third-generation nitrogen-containing bisphosphonate approved in Japan for osteoporosis treatment, acting primarily on osteoclasts to suppress bone resorption.
The TxGNN model predicts it may be effective for **Pseudo-von Willebrand Disease**, a rare platelet disorder caused by gain-of-function mutations in the GPIbα receptor.
Currently, **no clinical trials** and **no published literature** support this specific repurposing direction, placing this prediction at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoporosis (bisphosphonate class; approved in Japan) |
| Predicted New Indication | Pseudo-von Willebrand Disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological class information, minodronic acid is a nitrogen-containing bisphosphonate that inhibits farnesyl pyrophosphate synthase (FPPS) in the mevalonate pathway. This leads to impaired prenylation of Rho GTPases, ultimately triggering osteoclast apoptosis and reducing pathological bone resorption. It is the same core mechanism shared by zoledronate, risedronate, and other bisphosphonates.

Pseudo-von Willebrand disease (pseudo-vWD) is a platelet disorder caused by gain-of-function mutations in GP1BA (encoding GPIbα), which increases the receptor's affinity for von Willebrand factor (vWF). This leads to premature platelet consumption in the circulation. While bisphosphonates can modulate Rho GTPase signalling, which is involved in platelet cytoskeletal remodelling, this pathway has no established connection to the GPIbα/vWF binding affinity that is the root cause of pseudo-vWD.

The TxGNN prediction rationale explicitly acknowledges that the high model score likely reflects **topological similarity within the knowledge graph**—specifically proximity of "platelet disorder" nodes—rather than any direct pharmacological mechanism. There is no preclinical model, case report, or theoretical framework linking bisphosphonate pharmacology to the GPIbα gain-of-function defect. This is a graph inference artefact rather than a biologically grounded prediction for this particular indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Minodronic acid has **no registered products in India** as of the data cutoff (2026-04-04). The drug is approved in Japan (brand name: Recalbon®, 50 mg oral tablet) for osteoporosis but has not received regulatory approval in India or most other markets outside Japan.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** All safety data fields (key warnings, contraindications, and drug–drug interactions) returned no retrievable data in this evidence pack. As a bisphosphonate class, standard considerations include oesophageal irritation, hypocalcaemia risk, renal function monitoring, and osteonecrosis of the jaw with prolonged use—but these are class-level inferences and not confirmed from a retrieved India-specific label.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a very high score (99.97%), but the mechanistic link between FPPS inhibition and the GPIbα gain-of-function defect underlying pseudo-vWD is absent; the prediction most likely reflects knowledge graph topology rather than pharmacology. With zero supporting clinical trials, zero publications, no India market presence, and all safety data unavailable, there is insufficient basis to advance this candidate.

**Notable exception worth separating:**
Among all 7 predicted indications in this pack, **Bone Paget Disease (rank 5)** and **Juvenile Paget Disease (rank 7)** carry a materially stronger case—bisphosphonates are the established first-line class for both conditions, and the FPPS-inhibition mechanism directly addresses the osteoclast overactivation pathology. These two indications warrant a separate **Research Question** assessment rather than a blanket Hold.

**To proceed on any indication, the following is needed:**

- **MOA data retrieval:** Pull full DrugBank entry for DB06548 to confirm mechanism, categories, and toxicity profile
- **Safety label:** Obtain the Japanese package insert (Recalbon®) as a proxy, and assess whether any India-compatible labelling pathway exists
- **Paget disease pivot:** Commission a focused literature search for minodronic acid + Paget disease (class-effect evidence from other bisphosphonates is available; minodronic acid–specific data needs verification)
- **Regulatory pathway assessment:** Evaluate feasibility of India NDA/import registration given the Japan-only approval status
- **Pseudo-vWD hypothesis validation:** Before investing further resources in rank-1 prediction, consult a haematologist to confirm whether any bisphosphonate mechanism could plausibly affect GPIbα binding—current expert consensus suggests it cannot
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

