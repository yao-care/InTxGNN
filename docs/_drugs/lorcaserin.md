---
layout: default
title: Lorcaserin
parent: 僅模型預測 (L5)
nav_order: 367
evidence_level: L5
indication_count: 4
---

# Lorcaserin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Lorcaserin: From Obesity (Weight Management) to Hypervitaminosis

## One-Sentence Summary

Lorcaserin (brand name: Belviq) is a selective serotonin 5-HT2C receptor agonist, originally approved by the US FDA for chronic weight management in adults with obesity or overweight with at least one weight-related comorbidity — though it was subsequently withdrawn from the US market in 2020 due to cancer risk signals.
The TxGNN model predicts it may be effective for **Hypervitaminosis** (vitamin toxicity), with **0 clinical trials** and **0 publications** currently supporting this direction.
The mechanistic rationale for this prediction is weak, and this candidate warrants a Hold pending further biological plausibility review.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic weight management (obesity / overweight with comorbidity) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Lorcaserin is a highly selective serotonin 5-HT2C receptor agonist. By activating 5-HT2C receptors in the hypothalamus, it stimulates pro-opiomelanocortin (POMC) neurons to promote satiety, thereby reducing caloric intake and supporting weight loss. This central serotonergic mechanism underpins its original indication in obesity management.

Hypervitaminosis refers to toxic accumulation of fat-soluble vitamins (A, D, E, or K) in the body. The pathophysiology is primarily driven by excessive dietary or supplemental intake leading to lipid-phase storage overload and organ toxicity — a metabolic/nutritional disorder with no established connection to the serotonin 2C receptor pathway. There is no known mechanistic bridge between 5-HT2C agonism and the regulation or clearance of fat-soluble vitamins.

The repurposing team's own analysis (see `repurposing_rationale`) flags this prediction as a likely **false positive**, likely arising from indirect "metabolic abnormality" node proximity within the TxGNN knowledge graph rather than a genuine biological relationship. This candidate should be treated with caution, and the high TxGNN score should not be interpreted as pharmacological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Lorcaserin in Hypervitaminosis.

---

## Literature Evidence

Currently no related literature available for Lorcaserin in Hypervitaminosis.

---

## India Market Information

Lorcaserin has **no registered products** in India. The drug is not marketed in this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information regarding key warnings and contraindications (data not available in this Evidence Pack).

**Drug Interactions (DDI database, 190 total interactions identified):**

The following are selected interactions of clinical significance:

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Fentanyl | **Major** | Risk of serotonin syndrome with opioids acting on serotonergic pathways |
| Dextromethorphan | **Major** | Serotonin syndrome risk; dextromethorphan has weak serotonin reuptake inhibition |
| Tramadol | **Major** | Serotonin syndrome risk; tramadol inhibits serotonin and norepinephrine reuptake |
| Alfentanil | **Major** | Serotonin syndrome risk (opioid–serotonergic interaction) |
| Almotriptan | **Major** | Serotonin syndrome risk with triptans (5-HT1B/1D agonists) |
| Sumatriptan | **Major** | Serotonin syndrome risk with triptans |
| Amitriptyline | **Major** | Serotonin syndrome risk; tricyclic antidepressant with serotonin reuptake inhibition |
| Bupropion | **Major** | Combined CNS effects; potential for seizure threshold lowering |
| Metformin | Moderate | Additive blood glucose–lowering effect (hypoglycaemia risk) |
| Acarbose | Moderate | Additive hypoglycaemic effect |
| Pioglitazone | Moderate | Additive hypoglycaemic effect |
| Alogliptin | Moderate | Additive hypoglycaemic effect |
| Aripiprazole | Moderate | Pharmacodynamic interaction via dopamine/serotonin receptor overlap |
| Amphetamine | Moderate | Combined serotonergic and dopaminergic stimulation |
| Atomoxetine | Moderate | Serotonergic and noradrenergic interaction potential |

> ⚠️ **Note**: The consistent pattern of **Major** interactions with serotonergic agents (opioids, triptans, TCAs) reflects a class-level risk of **serotonin syndrome** — a potentially life-threatening condition. Any repurposing use must carefully screen for concomitant medications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high numeric score (99.97%) to the Lorcaserin → Hypervitaminosis prediction, but there is **zero supporting clinical or preclinical evidence**, and the mechanistic connection between 5-HT2C receptor agonism and fat-soluble vitamin toxicity is biologically implausible. Furthermore, Lorcaserin was withdrawn from the US market in 2020 due to an imbalance in cancer diagnoses in the CAMELLIA-TIMI 61 safety trial, adding a significant safety overhang to any repurposing effort.

**To proceed, the following is needed:**

- **Biological plausibility review**: Formal mechanistic hypothesis linking 5-HT2C agonism to hypervitaminosis pathophysiology — this should ideally be identified before any further investment
- **MOA data retrieval**: Query DrugBank API for complete mechanism of action and pharmacodynamic targets (Data Gap DG002)
- **Safety dossier**: Retrieve and parse TFDA/CDSCO package insert for full warnings and contraindications (Data Gap DG001)
- **Knowledge graph audit**: Review TxGNN graph edges linking Lorcaserin to hypervitaminosis to determine if this is a genuine signal or an artefact of indirect node proximity
- **India regulatory pathway assessment**: Since there are zero existing registrations in India, any future development would require a full new drug application process — a significant barrier for a repurposing candidate with L5 evidence
- **Market status clarification**: Lorcaserin's voluntary US market withdrawal (2020) and the underlying oncological safety signal should be fully factored into any go/no-go decision globally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

