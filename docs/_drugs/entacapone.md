---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Entacapone
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

# Entacapone: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Entacapone is a catechol-O-methyltransferase (COMT) inhibitor used as adjunct therapy in Parkinson's disease, extending the duration of levodopa's therapeutic effect.
The TxGNN model predicts it may have potential for **PLA2G6-Associated Neurodegeneration (PLAN)**, a rare inherited neurodegenerative disorder sharing parkinsonian features;
however, this prediction is currently supported by **0 clinical trials** and **0 published literature**, placing it at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease (adjunct to levodopa/carbidopa) |
| Predicted New Indication | PLA2G6-Associated Neurodegeneration |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 — Model prediction only, no actual studies |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, Entacapone is a selective and reversible COMT inhibitor. By blocking COMT, it reduces the peripheral breakdown of levodopa into 3-O-methyldopa, increasing levodopa's bioavailability and prolonging its central dopaminergic effect. This makes it a recognised adjunct in Parkinson's disease management.

PLA2G6-associated neurodegeneration (PLAN) is a rare autosomal recessive disorder caused by mutations in the *PLA2G6* gene, which encodes phospholipase A2 group VI. The resulting enzyme deficiency leads to abnormal membrane phospholipid remodelling, mitochondrial dysfunction, and progressive iron accumulation in the basal ganglia — a form of Neurodegeneration with Brain Iron Accumulation (NBIA). Clinically, PLAN patients can present with parkinsonian features, dystonia, pyramidal signs, and cognitive decline, creating a phenotypic overlap with idiopathic Parkinson's disease.

The mechanistic plausibility is modest rather than compelling. COMT inhibition could theoretically provide symptomatic dopaminergic support for the parkinsonian features of PLAN, but it does not address the underlying phospholipase deficiency, membrane pathology, or iron accumulation. The TxGNN high score most likely reflects shared neurodegenerative phenotype nodes in the knowledge graph rather than a direct biological mechanism. Independent preclinical validation is needed before this candidate can be taken forward.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions**: Entacapone has **82 documented drug interactions** in total. The table below lists the clinically most notable moderate-level interactions:

| Interacting Drug | Level | Clinical Relevance |
|------------------|-------|--------------------|
| Epinephrine | Moderate | COMT inhibition may potentiate cardiovascular effects of catecholamines |
| Epinephrine (ophthalmic) | Moderate | Same mechanism as systemic epinephrine; monitor cardiovascular status |
| Epinephrine (topical) | Moderate | Same mechanism as systemic epinephrine |
| Morphine | Moderate | Potential additive CNS/respiratory depression |
| Morphine (liposomal) | Moderate | Same mechanism as standard morphine |
| Dronabinol | Moderate | Additive CNS effects; monitor sedation |
| Nabilone | Moderate | Additive CNS effects; monitor sedation |
| Opium | Moderate | Additive CNS/respiratory depression |
| Metoclopramide | Moderate | Metoclopramide's dopamine antagonism may attenuate therapeutic effect |
| Iron | Moderate | Iron chelates entacapone, reducing oral absorption; separate administration by ≥2 hours |

> Complete warnings and contraindications are not available in this evidence pack. Please refer to the full package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN prediction score of 99.76%, there is zero clinical or preclinical literature evidence supporting Entacapone's use in PLA2G6-associated neurodegeneration. The prediction likely reflects phenotypic overlap in the knowledge graph rather than a mechanistically driven repurposing hypothesis; proceeding without further validation would not be justified.

**To proceed, the following is needed:**

- **Mechanistic validation**: Preclinical studies (cell models or animal models of PLA2G6 deficiency) to assess whether COMT inhibition or enhanced dopaminergic tone offers any benefit in PLAN pathophysiology
- **MOA data gap resolution**: Retrieve full DrugBank MOA entry for Entacapone to enable formal mechanistic linkage analysis
- **Safety data gap resolution**: Obtain TFDA/regulatory package insert to complete warnings and contraindications review before any clinical planning
- **India regulatory pathway assessment**: Entacapone has zero registered products in the market; a full regulatory strategy would be required before any clinical use
- **Iron interaction protocol**: If PLAN patients are co-managed with iron chelation therapy, the entacapone–iron absorption interaction must be formally addressed in any dosing protocol
- **Broader phenotype review**: Assess whether other top-ranked indications with dopaminergic overlap (e.g., Lewy body dementia, rank 7; juvenile paralysis agitans, rank 4) offer stronger mechanistic and evidence support as higher-priority repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

