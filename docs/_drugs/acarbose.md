---
layout: default
title: Acarbose
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 9
---

# Acarbose
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Acarbose: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Acarbose is an intestinal alpha-glucosidase inhibitor originally used to manage postprandial blood glucose in Type 2 Diabetes by slowing carbohydrate absorption.
The TxGNN model predicts it may be effective for **Classic Stiff Person Syndrome**, with a prediction score of **99.65%**.
However, there are currently **no clinical trials** and **no publications** supporting this direction, placing this prediction at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes (postprandial hyperglycaemia management) |
| Predicted New Indication | Classic Stiff Person Syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Acarbose competitively inhibits alpha-glucosidase enzymes (maltase, glucoamylase, sucrase) in the brush border of the small intestine, delaying the breakdown and absorption of complex carbohydrates and thereby blunting postprandial blood glucose peaks. Its action is almost entirely confined to the gastrointestinal lumen, with negligible systemic absorption.

Classic Stiff Person Syndrome (SPS) is a rare autoimmune neurological disorder driven by anti-GAD65 antibodies. GAD65 (glutamic acid decarboxylase 65) is the rate-limiting enzyme for GABA synthesis in inhibitory neurons, and its autoimmune impairment leads to disinhibition of motor circuits, causing debilitating muscle rigidity and spasms. Crucially, GAD65 is also expressed in pancreatic beta cells, which is why anti-GAD65 antibodies appear in both Type 1 Diabetes and SPS — and why the TxGNN knowledge graph likely built a drug–disease connection through this shared biological node.

In practice, however, this mechanistic bridge is extremely weak. Acarbose has no known immunomodulatory activity, no central nervous system penetration, and no mechanism by which inhibiting intestinal carbohydrate-cleaving enzymes could influence the autoimmune GABAergic cascade underlying SPS. The high TxGNN score most likely reflects a graph topology artifact — a short path between the "Acarbose → Diabetes → GAD65 → SPS" nodes — rather than a pharmacologically actionable relationship. This prediction should be interpreted as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Acarbose is currently **not marketed in India** and holds **no regulatory authorizations** on record. Any future repurposing effort would require establishing a full regulatory pathway from the outset.

---

## Safety Considerations

**Drug Interactions**: Acarbose has **371 known drug interactions** in total. The following moderate-level interactions are of primary clinical relevance:

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Acetazolamide | Moderate | Carbonic anhydrase inhibition may alter glycaemic control |
| Salbutamol (Albuterol) | Moderate | Beta-agonists counteract glucose-lowering effects; monitor blood glucose |
| Aloe Vera Leaf | Moderate | Additive hypoglycaemic effect; risk of excessive glucose lowering |
| Alpelisib | Moderate | PI3K inhibitor alters glucose homeostasis; glucose monitoring required |
| Amprenavir | Moderate | Protease inhibitor may impair glucose regulation |
| Aripiprazole | Moderate | Atypical antipsychotic; may worsen glycaemic control |
| Asenapine | Moderate | Atypical antipsychotic; blood glucose monitoring advised |
| Asparaginase (E. coli) | Moderate | May impair pancreatic beta-cell function and glucose metabolism |
| Asparaginase (Erwinia) | Moderate | Same concern as E. coli-derived asparaginase |
| Atazanavir | Moderate | Protease inhibitor; glycaemia monitoring advised |
| Bedaquiline | Moderate | Monitor for effects on metabolic glucose balance |
| Bendroflumethiazide | Moderate | Thiazide diuretics antagonise hypoglycaemic effects |
| Benzthiazide | Moderate | Thiazide class; similar antagonism of glucose lowering |
| Benzphetamine | Moderate | Sympathomimetic; may impair blood glucose control |
| Betamethasone | Moderate | Corticosteroids significantly antagonise hypoglycaemic activity |

> Note: Full package insert warnings and contraindications were not available in this Evidence Pack. Please refer to the official prescribing information for complete safety data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical, translational, or mechanistic evidence supporting the use of Acarbose in Classic Stiff Person Syndrome. The TxGNN prediction almost certainly reflects a knowledge graph traversal artifact via the shared GAD65 node between diabetes and SPS pathways, rather than a genuine pharmacological opportunity. Acarbose has no immunomodulatory, neuroprotective, or GABAergic activity that could be expected to benefit SPS patients.

**To proceed, the following is needed:**

- **Mechanistic investigation**: Determine whether Acarbose or its gut metabolites have any secondary effects on systemic immune signalling, the gut–brain axis, or GABAergic pathways that could theoretically be relevant to SPS
- **Preclinical data**: Conduct or identify animal model studies of GAD65-mediated autoimmunity treated with alpha-glucosidase inhibitors before investing in human research
- **Microbiome hypothesis**: If the rationale is gut microbiome modulation (a plausible indirect path), design a mechanistic study linking alpha-glucosidase inhibition → microbiome shifts → neuroimmune outcomes
- **India regulatory groundwork**: As Acarbose is not approved in India, both the original Type 2 Diabetes indication and any repurposed indication would require a full NDA/regulatory filing
- **Safety data retrieval**: Obtain the full CDSCO-aligned package insert including warnings, contraindications, and special population data (currently a blocking data gap)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

