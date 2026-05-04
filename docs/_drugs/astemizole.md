---
layout: default
title: Astemizole
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 1
---

# Astemizole
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

# Astemizole: From Allergic Rhinitis to Rosacea Conjunctivitis

## One-Sentence Summary

Astemizole is a second-generation H1 antihistamine historically used for allergic conditions such as allergic rhinitis and urticaria, but withdrawn from global markets in 1999 due to life-threatening cardiac toxicity.
The TxGNN model predicts it may have potential in **Rosacea Conjunctivitis**,
with a high computational score of **99.78%** — however, **no clinical trials and no published literature** currently support this direction, making this a purely model-driven prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis, urticaria (antihistamine; not listed in India registry — drug is not marketed) |
| Predicted New Indication | Rosacea Conjunctivitis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Astemizole is a second-generation H1 histamine receptor antagonist (antihistamine). Its mechanism relies on selectively blocking H1 receptors, thereby suppressing the inflammatory cascade triggered by histamine released from mast cells — without the sedation profile of first-generation antihistamines.

Rosacea conjunctivitis is a form of ocular inflammation associated with rosacea, a chronic skin condition with a prominent inflammatory component. Conjunctival mast cells release histamine upon activation, contributing to redness, itching, and irritation. On mechanistic grounds, H1 blockade could theoretically dampen this histamine-mediated ocular inflammation, providing the biological rationale for TxGNN's prediction.

However, this theoretical link is overshadowed by a critical safety reality. **Astemizole was withdrawn from the US FDA and EU markets in 1999** due to its blockade of the hERG cardiac potassium channel, leading to QTc interval prolongation and potentially fatal arrhythmias (Torsades de Pointes). With 276 known drug-drug interactions, it is classified as an extremely high-risk compound. The prediction score of 99.78%, while mathematically impressive, reflects graph-based structural similarity rather than clinical viability.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Astemizole currently holds no approved drug licenses in India. The drug is not marketed and has no active registrations on record.

---

## Safety Considerations

**Drug Interactions (276 total interactions identified):**

Below are selected interactions of note, prioritised by severity:

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Clarithromycin | **Major** | CYP3A4 inhibition raises astemizole plasma levels → increased QTc risk |
| Aprepitant | **Major** | CYP3A4 inhibition → elevated astemizole exposure |
| Cimetidine | **Major** | Inhibits hepatic metabolism → QTc prolongation risk |
| Miconazole | **Major** | Antifungal CYP inhibition → cardiac arrhythmia risk |
| Dolasetron | **Major** | Additive QTc prolongation |
| Picosulfuric acid | **Major** | Electrolyte-mediated QTc potentiation |
| Polyethylene glycol (3350 with electrolytes) | **Major** | Electrolyte shifts → increased arrhythmia risk |
| Sodium sulfate | **Major** | Electrolyte disturbance interaction |
| Ondansetron | Moderate | Additive QTc effects (5-HT3 antagonist) |
| Palonosetron | Moderate | Additive QTc effects |
| Levofloxacin | Moderate | Fluoroquinolone-related QTc additive effect |
| Famotidine | Moderate | H2/H1 pathway overlap, QT monitoring advised |
| Loperamide | Moderate | Cardiac conduction caution |

> ⚠️ **Critical Safety Note:** Astemizole's hERG channel blockade and resultant QTc prolongation risk led to its global market withdrawal in 1999. It should be regarded as a **withdrawn compound** with an **unacceptable cardiac safety profile** for any new indication development without a specific cardiac risk mitigation programme.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a high prediction score (99.78%) based on mechanistic graph proximity between H1 antagonism and histamine-mediated conjunctival inflammation, astemizole carries a black-box cardiac safety profile that resulted in its global withdrawal. With zero supporting clinical trials, zero published literature, 276 drug-drug interactions, and no India market presence, the benefit-risk ratio for pursuing this candidate is currently unfavourable.

**To reconsider this direction, the following would be needed:**

- **Cardiac safety re-evaluation**: Evidence that a topical ophthalmic formulation achieves negligible systemic exposure, thereby circumventing QTc risk
- **Preclinical proof-of-concept**: In vitro or in vivo data demonstrating efficacy in a rosacea conjunctivitis model
- **Regulatory pathway consultation**: Assessment of whether the 1999 withdrawal creates insurmountable barriers to any new IND filing
- **Comparative analysis**: Head-to-head mechanistic comparison against safer second-generation antihistamines (e.g., olopatadine, azelastine) already approved for ophthalmic use
- **MOA data gap resolution**: Confirm via DrugBank API whether any additional pharmacological activity (beyond H1 antagonism) contributes to TxGNN's prediction
- **Full safety document retrieval**: Package insert warnings and contraindications should be sourced before any further development consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

