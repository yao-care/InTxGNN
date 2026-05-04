---
layout: default
title: Meclizine
parent: 僅模型預測 (L5)
nav_order: 314
evidence_level: L5
indication_count: 6
---

# Meclizine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Meclizine: From Motion Sickness / Vertigo to Allergic Urticaria

## One-Sentence Summary

Meclizine is a first-generation H1 antihistamine, classically used to treat motion sickness, vertigo, and associated nausea and vomiting.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, which is mechanistically plausible as H1 antagonists are first-line therapy for urticaria as a class — however, there are **0 clinical trials** and **0 publications** directly supporting this specific use of Meclizine, and clinical preference has shifted to second-generation non-sedating antihistamines.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Motion sickness; Vertigo-associated nausea and vomiting |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally available in this evidence pack. Based on established pharmacological knowledge, Meclizine is a first-generation H1 receptor antagonist with additional anticholinergic properties. It suppresses the vestibular system and central histamine signalling, explaining its efficacy in motion sickness and vertigo-related nausea.

Allergic urticaria is driven by mast cell degranulation and histamine release, with H1 receptor blockade serving as the universally accepted first-line mechanism. In this sense, TxGNN's prediction reflects a valid **class-effect mechanistic link**: blocking H1 receptors directly counters the wheal-and-flare cascade underlying urticaria. The transition from vestibular/CNS histamine blockade (motion sickness) to peripheral H1 blockade (urticaria) represents a shift in target organ, not a change in core mechanism.

That said, clinical guidelines for urticaria have firmly moved toward second-generation, non-sedating H1 antihistamines (cetirizine, loratadine, fexofenadine, bilastine) due to superior tolerability and absence of CNS sedation. Meclizine's pronounced sedating and anticholinergic side effects make it a poor candidate for the chronic, long-term management that urticaria typically requires. No independent clinical studies specifically evaluate Meclizine for allergic urticaria, and this prediction is best understood as a class-level signal rather than a compound-specific opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for allergic urticaria.

> **Note:** One trial was identified in the broader evidence sweep ([NCT01537471](https://clinicaltrials.gov/study/NCT01537471)) but is associated with the **common cold** query and investigates Pre-Pulse Inhibition (a neuropsychiatric biomarker) — it has no relevance to allergic urticaria and is excluded here.

---

## Literature Evidence

Currently no related literature available for allergic urticaria.

---

## India Market Information

Meclizine currently has **no registered products** in India. The drug is not marketed and holds zero approved licenses with CDSCO. Any introduction for a new indication would require a full new drug application process from the ground up.

---

## Safety Considerations

**Drug Interactions (252 total interactions identified; top interactions listed below):**

| Severity | Interacting Drug | Clinical Concern |
|----------|-----------------|------------------|
| **Major** | Potassium citrate | Significant interaction — monitor closely |
| **Major** | Potassium chloride | Significant interaction — monitor closely |
| Moderate | Hyoscyamine | Additive anticholinergic effects (dry mouth, urinary retention, constipation) |
| Moderate | Atropine | Additive anticholinergic effects |
| Moderate | Glycopyrronium | Additive anticholinergic effects |
| Moderate | Glycopyrronium (topical) | Additive anticholinergic effects |
| Moderate | Dicyclomine | Additive anticholinergic effects |
| Moderate | Methscopolamine | Additive anticholinergic effects |
| Moderate | Mepenzolate | Additive anticholinergic effects |
| Moderate | Clidinium | Additive anticholinergic effects |
| Moderate | Trospium | Additive anticholinergic effects |
| Moderate | Morphine | Risk of enhanced CNS/respiratory depression |
| Moderate | Morphine (liposomal) | Risk of enhanced CNS/respiratory depression |
| Moderate | Opium | Risk of enhanced CNS/respiratory depression |
| Moderate | Nabilone | Additive CNS depressant effects |
| Moderate | Metoclopramide | Opposing effects on GI motility; reduced metoclopramide efficacy |
| Moderate | Loperamide | Additive GI motility reduction |
| Moderate | Eluxadoline | Additive GI effects |
| Moderate | Eliglustat | Interaction potential |
| Moderate | Glycerol phenylbutyrate | Interaction potential |

> Package insert warnings and contraindications are not currently available (data gap DG001). Please refer to the official prescribing information before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although Meclizine's H1 antagonism provides a mechanistically coherent basis for allergic urticaria, there is a complete absence of direct clinical evidence for this specific drug in this indication, clinical guidelines actively prefer second-generation antihistamines, and the drug holds zero market authorisations in India — making a near-term repurposing pathway impractical without substantial additional investigation.

**To proceed, the following is needed:**
- Direct clinical evidence (even pilot or observational studies) comparing Meclizine to second-generation antihistamines in allergic urticaria
- Identification of a specific patient subgroup where Meclizine's sedating or anticholinergic profile might confer a clinical advantage (e.g., urticaria with concurrent sleep disturbance)
- Formal MOA documentation from DrugBank (data gap DG002 — currently unresolved)
- Retrieval of CDSCO package insert for complete warnings and contraindications (data gap DG001 — blocking severity)
- Market feasibility analysis for India entry given zero existing regulatory footprint
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

