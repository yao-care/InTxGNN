---
layout: default
title: Invert Sugar
parent: 僅模型預測 (L5)
nav_order: 314
evidence_level: L5
indication_count: 1
---

# Invert Sugar
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

# Invert Sugar: From Parenteral Nutrition to Sclerosing Cholangitis

## One-Sentence Summary

Invert sugar (an equimolar mixture of glucose and fructose) is a parenteral nutritional agent used primarily as a caloric source in IV fluid therapy.
The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**,
however **0 clinical trials** and **0 publications** currently support this direction — this is a purely computational prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parenteral nutritional support (caloric supplementation) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Invert sugar is an equimolar mixture of glucose and fructose administered intravenously as a caloric energy source. Fructose in particular undergoes hepatic metabolism via the fructokinase (ketohexokinase) pathway, which is distinct from glucose metabolism in that it bypasses the rate-limiting step of phosphofructokinase, leading to rapid and unregulated hepatic fructose phosphorylation.

The mechanistic rationale proposed by the TxGNN knowledge graph suggests that fructose metabolism in the liver leads to transient hepatic ATP depletion, increased oxidative stress, and potential activation of the NLRP3 inflammasome — all of which could theoretically interact with the inflammatory microenvironment of the bile ducts relevant to sclerosing cholangitis. Sclerosing cholangitis is characterized by progressive biliary inflammation and fibrosis, and hepatic metabolic stress is a known modulator of biliary epithelial cell behavior.

However, it must be emphasized that this proposed link is entirely derived from knowledge graph topological similarity (TxGNN score: 0.9962) and represents a computational inference only. There is no experimental, preclinical, or clinical data connecting invert sugar administration to sclerosing cholangitis outcomes. The biological plausibility remains speculative, and the direction of any potential effect (beneficial vs. harmful) is entirely unclear.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Invert sugar currently has no registered products in India (0 authorizations on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is based solely on TxGNN knowledge graph topology (L5 evidence) with zero supporting clinical trials or publications; there is no empirical basis to justify further development at this stage, and the mechanistic link between invert sugar and sclerosing cholangitis remains entirely speculative.

**To proceed, the following is needed:**

- **MOA clarification**: Obtain full DrugBank mechanism-of-action data to assess whether any hepatic metabolic pathway has a documented relationship to biliary inflammation
- **Preclinical literature review**: Conduct a broader PubMed search using related terms (e.g., fructose + cholestasis, invert sugar + liver inflammation, fructose + NLRP3 + biliary) to determine if any indirect mechanistic evidence exists
- **Safety profile**: Retrieve the full CDSCO/regulatory package insert to assess known hepatic or biliary adverse effects of invert sugar — a drug that worsens biliary disease would be contraindicated rather than therapeutic
- **Expert consultation**: Engage a hepatologist or gastroenterologist to evaluate whether fructose-mediated hepatic ATP depletion is biologically relevant in the sclerosing cholangitis context
- **Decision gate**: Only escalate to S1 safety evaluation if preclinical mechanistic evidence or plausible indirect literature links are identified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

