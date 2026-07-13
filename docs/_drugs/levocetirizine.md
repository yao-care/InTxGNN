---
layout: default
title: Levocetirizine
parent: 僅模型預測 (L5)
nav_order: 356
evidence_level: L5
indication_count: 3
---

# Levocetirizine
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

# Levocetirizine: From Allergic Rhinitis to Rheumatoid Arthritis

## One-Sentence Summary

Levocetirizine is a second-generation H1 antihistamine widely used for the treatment of allergic rhinitis and chronic urticaria.
The TxGNN model predicts it may have potential efficacy in **Rheumatoid Arthritis (RA)**,
with a prediction score of **99.73%**; however, **no clinical trials or supporting publications** have been identified, placing this at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, chronic urticaria (H1 antihistamine class; no India registration data available) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological class information, Levocetirizine is a selective H1 receptor antagonist (the active R-enantiomer of cetirizine). It competitively blocks peripheral H1 receptors, reducing histamine-mediated inflammatory and allergic responses with minimal central nervous system penetration.

The proposed mechanistic link to rheumatoid arthritis is indirect and largely hypothetical. Histamine has been detected in the synovial fluid of RA patients, and mast cells as well as basophils are known to participate in joint inflammation. H1 receptor blockade could theoretically suppress downstream release of pro-inflammatory cytokines such as IL-1β and TNF-α, and there is limited evidence that some antihistamines may modulate the NF-κB signalling pathway. These observations form a plausible, though highly speculative, biological rationale.

It is critical to note that the core pathophysiology of RA is T-cell–mediated autoimmunity, driven by adaptive immune responses that are not directly governed by the histamine–H1 receptor axis. The mechanistic connection is therefore considered weak, and the high TxGNN score most likely reflects graph-level proximity in the knowledge graph rather than a robust biological signal. This prediction should be treated with substantial caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Levocetirizine currently has **no registered products** in India. No authorization records are available for review.

---

## Safety Considerations

**Drug Interactions:** A total of 241 drug–drug interactions have been identified (source: DDInter). The following represent a selection of clinically relevant moderate-level interactions:

| Interacting Drug | Severity | Clinical Note |
|------|------|------|
| Morphine | Moderate | Additive CNS/respiratory depression risk |
| Fentanyl | Moderate | Enhanced sedation with opioid co-administration |
| Dihydrocodeine | Moderate | Combined CNS depressant effect |
| Promethazine | Moderate | Additive anticholinergic and sedative effects |
| Chlorpheniramine | Moderate | Combined antihistamine sedation potentiation |
| Bupropion | Moderate | Potential seizure threshold lowering |
| Ethanol | Moderate | Enhanced CNS depression |
| Metoclopramide | Moderate | CNS depression additive effect |
| Dronabinol / Nabilone | Moderate | Additive CNS sedation |
| Iodide I-131 / I-123 | Moderate | Antihistamines may reduce radioiodine uptake |

> For complete warnings, contraindications, and package insert details, please refer to the approved prescribing information. Full warning and contraindication data were not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is currently zero clinical or published evidence supporting the use of Levocetirizine in rheumatoid arthritis. The mechanistic link is highly indirect and speculative, and the drug is not marketed in India. This prediction appears to be model-generated noise rather than a clinically actionable signal; proceeding with repurposing investigation would not be warranted at this stage.

**To proceed, the following is needed:**

- Retrieval and review of the approved package insert to obtain formal warnings, contraindications, and MOA documentation
- Identification of any peer-reviewed preclinical studies examining antihistamines in animal models of RA (to upgrade from L5 to L4 evidence at minimum)
- Mechanistic validation: in vitro studies examining the effect of Levocetirizine on synoviocyte cytokine release, NF-κB activity, or mast cell degranulation in a joint-disease context
- Market landscape review: confirm current registration status in India (CDSCO) and assess whether regulatory pathway for RA indication exists
- Re-evaluate TxGNN graph topology to determine whether the high score reflects a genuine signal or an artefact of rare-disease node clustering in the knowledge graph
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

