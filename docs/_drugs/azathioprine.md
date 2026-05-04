---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 84
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine: From Immunosuppression to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

Azathioprine (AZA) is a well-established thiopurine immunosuppressant, widely used in organ transplant rejection prevention and autoimmune diseases such as inflammatory bowel disease and systemic lupus erythematosus.
The TxGNN model assigns its highest prediction score to **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome** (TxGNN score: 99.99%),
however, **no clinical trials or publications** currently support this application, and no mechanistic rationale has been identified — making this a likely model artefact rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from India regulatory data (no registered products) |
| Predicted New Indication | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Azathioprine is a thiopurine prodrug converted in vivo to 6-mercaptopurine (6-MP) and subsequently to 6-thioguanine nucleotides (6-TGN). These active metabolites inhibit de novo purine synthesis and induce apoptosis in activated T-lymphocytes, thereby suppressing cell-mediated and humoral immune responses. Its proven efficacy in immune-mediated conditions — including Crohn's disease, ulcerative colitis, rheumatoid arthritis, and organ transplant rejection — is well documented over decades of clinical use.

Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a rare genetic developmental disorder characterised by ocular malformations (coloboma, microphthalmia) combined with proximal limb shortening and skeletal abnormalities. The condition arises from mutations affecting embryonic morphogenesis and has no established immune-mediated or inflammatory pathological component that AZA's mechanism of immunosuppression could plausibly address.

The high TxGNN model score most likely reflects an indirect or non-causal path within the knowledge graph — a known limitation of graph-based models where distant topological associations can produce spurious high-confidence predictions (overfitting or long-range path artefacts). There is currently no biological hypothesis to support this repurposing direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

No registered products in India. Azathioprine is currently not marketed in the Indian market and holds zero drug licences under India's regulatory framework.

---

## Safety Considerations

**Drug Interactions**: A total of 447 drug-drug interactions are recorded in the DDInter database. Key notable interactions are summarised below:

| Interacting Drug | Severity | Clinical Note |
|------------------|----------|---------------|
| Mesalazine | Moderate | Aminosalicylates (5-ASA derivatives) may inhibit TPMT enzyme activity, increasing 6-TGN levels and risk of myelotoxicity; monitor CBC closely when co-administered |
| Balsalazide | Moderate | Same class as mesalazine; same TPMT inhibition concern applies |
| Olsalazine | Moderate | Same class as mesalazine; same TPMT inhibition concern applies |
| Sulfasalazine | Moderate | Same class as mesalazine; same TPMT inhibition concern applies |
| Zinc acetate | Minor | Potential minor interaction; routine monitoring sufficient |
| Zinc gluconate | Minor | Potential minor interaction; routine monitoring sufficient |
| Zinc sulfate | Minor | Potential minor interaction; routine monitoring sufficient |

Package insert warnings and contraindications are not available in this Evidence Pack. Please refer to the official package insert (SmPC/PI) for complete safety information including myelosuppression risk, hepatotoxicity, increased infection susceptibility, and risk of secondary malignancy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a rare genetic developmental disorder with no immune-mediated pathology; Azathioprine's immunosuppressive mechanism has no theoretical or empirical basis for application in this condition, and the evidence base is entirely absent (L5 — model prediction only).

**To proceed with any further evaluation, the following would be needed:**
- A plausible mechanistic hypothesis linking AZA's immunosuppressive or purine-synthesis-inhibiting mechanism specifically to this genetic syndrome
- At minimum, preclinical data (in vitro or animal model) demonstrating any potential therapeutic effect
- Clarification and audit of the TxGNN knowledge graph path driving this high score, to determine whether it reflects a direct mechanistic link or an indirect associative artefact
- **Important note for prioritisation**: Within this same Evidence Pack, **Inflammatory Bowel Disease** (TxGNN Rank #5, Evidence Level L1, 50+ clinical trials, multiple Cochrane systematic reviews) and **Ulcerative Colitis** (TxGNN Rank #9, Evidence Level L1, multiple Phase 3 RCTs and Cochrane reviews) represent far more clinically actionable repurposing signals for AZA — both with strong direct mechanistic support and decades of clinical evidence. These indications should be prioritised for formal evaluation.

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

