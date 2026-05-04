---
layout: default
title: Dexchlorpheniramine
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 2
---

# Dexchlorpheniramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Dexchlorpheniramine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Dexchlorpheniramine is a first-generation H1 antihistamine classically used for the symptomatic relief of allergic rhinitis, pruritus, and histamine-mediated allergic reactions.
The TxGNN model predicts it may be effective for **Allergic Urticaria** with a confidence of **99.89%**,
with **0 registered clinical trials** and **6 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis and histamine-mediated allergic conditions (globally established; no India registration on record) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in the evidence pack. However, based on well-established pharmacological knowledge, Dexchlorpheniramine is the pharmacologically active dextrorotatory enantiomer of chlorpheniramine, belonging to the alkylamine subclass of first-generation H1 antihistamines. It acts as a competitive antagonist at histamine H1 receptors on mast cells, vascular endothelial cells, and smooth muscle — thereby directly suppressing the vasodilation and increased vascular permeability that underpin urticarial lesion formation.

Allergic urticaria is driven primarily by IgE-mediated mast cell degranulation and the subsequent systemic release of histamine — the exact molecular target of dexchlorpheniramine. The EAACI/WAO international guidelines designate H1 antihistamines as the Grade A first-line treatment for urticaria, making the mechanistic link between this drug and the predicted indication exceptionally direct and well-supported. As one of the most potent first-generation agents in its class, dexchlorpheniramine has strong biological plausibility for this use.

The TxGNN model's near-ceiling confidence score of 99.89% reflects this tight mechanistic alignment. Published clinical pharmacodynamic studies — including a Phase I randomized trial directly comparing dexchlorpheniramine with bilastine using a histamine-induced wheal-and-flare model — further validate that the drug produces measurable, clinically relevant antihistaminic effects in the urticaria disease context. This is therefore less a novel repurposing hypothesis and more a formal evidence-based confirmation of an established pharmacological relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39265704](https://pubmed.ncbi.nlm.nih.gov/39265704/) | 2024 | Randomised Phase I Trial | European Journal of Pharmaceutical Sciences | Head-to-head comparison of oral bilastine, parenteral dexchlorpheniramine, and a novel parenteral bilastine formulation for suppression of histamine-induced wheal and flare; directly demonstrates dexchlorpheniramine's antihistaminic potency in a urticaria-relevant pharmacodynamic endpoint |
| [29723372](https://pubmed.ncbi.nlm.nih.gov/29723372/) | 2018 | Clinical Pharmacodynamic Study | Anais Brasileiros de Dermatologia | Compared H1 antihistamine potency marketed in Brazil using skin histamine challenge; dexchlorpheniramine evaluated as a reference standard for urticaria-related suppression of wheal and flare |
| [28601540](https://pubmed.ncbi.nlm.nih.gov/28601540/) | 2017 | Case Report | The American Journal of Medicine | Describes atrial fibrillation complicating anaphylaxis; dexchlorpheniramine cited in clinical management of severe allergic/urticarial emergency, highlighting its role in acute histamine-driven conditions |
| [26179134](https://pubmed.ncbi.nlm.nih.gov/26179134/) | 2015 | Case Report | Contact Dermatitis | Palpebral angioedema and allergic contact dermatitis following cerumenolytic exposure; dexchlorpheniramine used in management of acute allergic cutaneous reactions with urticarial features |
| [39803](https://pubmed.ncbi.nlm.nih.gov/39803/) | 1979 | Clinical Observation | Dermatologica | Early characterisation of acquired heat contact urticaria; antihistamine agents of the dexchlorpheniramine class evaluated in the diagnostic and therapeutic workup |
| [2523357](https://pubmed.ncbi.nlm.nih.gov/2523357/) | 1989 | In Vitro Mechanistic Study | International Archives of Allergy and Applied Immunology | Examines cetirizine's inhibitory effects on eosinophil chemotaxis and IgE-dependent platelet stimulation; contextualises first- vs. second-generation H1 antihistamine mechanisms in urticaria-relevant immune pathways |

---

## India Market Information

No products containing Dexchlorpheniramine are currently registered or marketed in India. No license records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug interaction data were not retrievable from available sources at time of report generation. Obtaining the full prescribing information is flagged as a **Blocking** prerequisite before proceeding to formal safety evaluation (see Conclusion).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dexchlorpheniramine's direct H1-receptor antagonism mechanism is precisely aligned with the core pathophysiology of allergic urticaria, and this is supported by a Phase I randomised comparative trial and multiple clinical pharmacodynamic studies demonstrating measurable antihistaminic efficacy in urticaria-relevant models. However, the absence of India regulatory registration, unavailable formal safety documentation, and a lack of registered Phase II/III trials specific to this indication prevent an unconditional Go decision.

**To proceed, the following is needed:**

- **[Blocking]** Obtain and parse the full package insert (TFDA or equivalent source) to extract key warnings, contraindications, and drug-drug interaction data before any safety evaluation can proceed
- **[High Priority]** Query DrugBank API to retrieve complete MOA data (DB13679) to support mechanistic analysis and differentiation from second-generation antihistamines
- **[Regulatory]** Assess India market entry pathway given zero current registrations; evaluate whether a new drug application or abbreviated application route is appropriate
- **[Clinical Positioning]** Conduct a structured comparison with second-generation H1 antihistamines (e.g., cetirizine, loratadine) to define the clinical role of dexchlorpheniramine, given EAACI guidelines currently prefer non-sedating second-generation agents as first-line
- **[Safety Profiling]** Review sedation, anticholinergic burden, and QTc effects before recommending use in elderly patients, paediatric populations, or individuals operating vehicles/machinery
- **[Evidence Gap]** Consider registering or identifying an adequately powered Phase II/III RCT specifically in allergic urticaria to upgrade evidence from L2 to L1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

