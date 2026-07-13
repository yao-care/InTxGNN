---
layout: default
title: Dimercaprol
parent: 僅模型預測 (L5)
nav_order: 234
evidence_level: L5
indication_count: 1
---

# Dimercaprol
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

# Dimercaprol: From Heavy Metal Poisoning to Bronchitis

## One-Sentence Summary

Dimercaprol (BAL — British Anti-Lewisite) is a dithiol chelating agent originally used for treatment of acute heavy metal poisoning, including arsenic, mercury, and lead toxicity.
The TxGNN model predicts it may be effective for **Bronchitis**, though the mechanistic link is extremely narrow — applicable only to mercury inhalation-induced chemical bronchitis.
No clinical trials directly involving Dimercaprol for bronchitis were identified; supporting evidence is limited to a single 1963 case report and a theoretical mechanism.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heavy metal poisoning (arsenic, mercury, gold, lead) — not registered in India |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacology, Dimercaprol (BAL) is a dithiol chelating agent that binds heavy metals — particularly mercury, arsenic, gold, and lead — through its two sulfhydryl (–SH) groups, forming stable, water-soluble chelate complexes that are renally excreted. It was originally developed as an antidote against arsenical chemical warfare agents (Lewisite) during World War II and remains the standard of care for acute heavy metal poisoning.

The mechanistic connection to bronchitis is extremely narrow: acute inhalation of mercury vapour or arsine gas can cause severe chemical tracheobronchitis. In this specific context, Dimercaprol as a systemic chelating antidote might theoretically reduce the severity or duration of metal-induced airway inflammation by lowering the toxic metal burden in bronchial tissues. A 1963 case report (PMID 14068440) describes two cases of bronchitis caused by acute mercury inhalation — the only literature directly linking the drug's mechanism to this respiratory presentation.

The TxGNN prediction score of 99.54% most likely reflects a knowledge graph inference pathway along the lines of "heavy metal poisoning → airway injury → bronchitis" rather than any genuine applicability to common infectious or non-specific bronchitis. This represents a significant risk of algorithmic false-positive prediction, as the mechanistic rationale applies only to a rare, highly specific subtype of chemical bronchitis arising from acute metal poisoning.

---

## Clinical Trial Evidence

All 24 clinical trials retrieved were assessed as irrelevant (Grade C) — they involved unrelated interventions such as Vitamin D, inhaled Cyclosporine, Montelukast, and Alvelestat, targeting transplant-related bronchiolitis obliterans or COPD subphenotypes, with no connection to Dimercaprol.

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [14068440](https://pubmed.ncbi.nlm.nih.gov/14068440/) | 1963 | Case Report | Am Rev Respir Dis | Two cases of acute bronchitis caused by mercury vapour inhalation — the only literature directly linking mercury-induced airway injury to the clinical context where Dimercaprol chelation therapy would apply |

---

## India Market Information

Dimercaprol is not currently registered or marketed in India. No product authorizations are on record. The drug is available in some Western markets (e.g., USA as BAL in Oil® injection), but has no approved products in the Indian market.

---

## Safety Considerations

**Drug Interactions — 15 Major interactions identified (Source: DDInter):**

All major interactions involve iron-containing and selenium preparations. Dimercaprol forms toxic complexes with iron in vivo; concurrent use is contraindicated.

| Category | Interacting Drugs | Severity |
|----------|-------------------|----------|
| Iron compounds (oral) | Ferrous fumarate, Ferrous gluconate, Ferrous sulfate anhydrous, Iron protein succinylate | **Major** |
| Iron compounds (intravenous) | Iron Dextran, Iron sucrose, Ferric carboxymaltose, Ferric derisomaltose, Ferumoxytol, Ferumoxides, Ferumoxsil, Sodium ferric gluconate complex, Tetraferric tricitrate decahydrate | **Major** |
| Trace elements | Selenium | **Major** |

> Iron supplementation of any form must be withheld during Dimercaprol treatment. The formation of a toxic Dimercaprol–iron complex can cause systemic harm.

For full warnings and contraindications, please refer to the package insert, as those data were not available in this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.54%), but the mechanistic bridge to bronchitis is applicable only to a rare, chemically-induced subtype from acute mercury or arsenic inhalation — not to the broad disease category of bronchitis. There is no clinical trial evidence, and only one 60-year-old case report provides any indirect support. The drug is also not registered in India, creating an additional regulatory barrier.

**To proceed, the following is needed:**
- Precise definition of the bronchitis subtype of interest (infectious vs. chemical/metal-induced) — the entire rationale hinges on this distinction
- Full mechanism of action (MOA) data from DrugBank to confirm or refute the mechanistic link
- Package insert safety data (warnings and contraindications) — currently unavailable and classified as a Blocking data gap
- Systematic case series or preclinical data demonstrating Dimercaprol's efficacy specifically in reducing the severity or duration of metal-induced bronchitis
- Regulatory pathway assessment for India market entry before any repurposing programme can advance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

