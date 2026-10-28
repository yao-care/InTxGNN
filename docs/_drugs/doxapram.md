---
layout: default
title: Doxapram
parent: Model Prediction Only (L5)
nav_order: 286
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Doxapram: predicted new indication Vascular disease (evidence level L4). Approved use: Respiratory failure"
monitor_inn: "Doxapram"
predicted_indications: ["vascular disease", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "angiodysplasia of stomach", "blue toe syndrome", "hemangioendothelioma", "atheroembolism of kidney", "neurogenic thoracic outlet syndrome", "visceral calciphylaxis", "lymphangiectasis"]
---

# Doxapram
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Doxapram: From Respiratory Failure to Vascular Disease
{: .text-alpha }

## One-Sentence Summary

Doxapram is a respiratory stimulant originally used to treat respiratory failure.
The TxGNN model predicts it may be effective for **vascular disease**, but there are **no registered clinical trials** and the **12 publications** retrieved are mostly animal studies, veterinary cohorts, old case reports, and safety observations, so this is essentially a computational prediction without therapeutic support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Respiratory failure |
| Predicted New Indication | Vascular disease |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, doxapram is a respiratory stimulant that acts on peripheral carotid chemoreceptors and the brainstem respiratory centres. Its use in respiratory failure is established, but no therapeutic mechanism linking it to vascular disease has been identified.

The retrieved literature describes only indirect observations: pressor and hemodynamic effects in normovolemic and hypovolemic dogs, a 1971 report in hemorrhagic hypotension, and modulation of hypoxic pulmonary vasoconstriction in a piglet model. These are pharmacology and side-effect findings, not evidence of benefit in vascular disease.

The very high TxGNN score (about 0.9999) should be interpreted cautiously. Many unrelated vascular terms (for example thoracic outlet syndromes, blue toe syndrome, hemangioendothelioma, visceral calciphylaxis, lymphangiectasis) receive almost identical scores, which suggests a nonspecific signal rather than a disease-specific one.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8737758](https://pubmed.ncbi.nlm.nih.gov/8737758/) | 1996 | Clinical study | Eur J Clin Pharmacol | Randomized double-blind trial of doxapram vs placebo for late postoperative hypoxaemia; focus on adverse events with continuous infusion |
| [11743509](https://pubmed.ncbi.nlm.nih.gov/11743509/) | 2001 | Cohort | J Pediatr | Prolonged doxapram therapy for apnea in very low birth weight infants was associated with isolated mental developmental delay |
| [18371030](https://pubmed.ncbi.nlm.nih.gov/18371030/) | 2008 | Retrospective cohort (veterinary) | J Vet Intern Med | Caffeine vs doxapram for hypercapnia in foals with hypoxic-ischemic encephalopathy |
| [35318792](https://pubmed.ncbi.nlm.nih.gov/35318792/) | 2022 | Retrospective cohort (veterinary) | J Vet Emerg Crit Care | Cardiopulmonary arrest and resuscitation in 41 hospitalized birds |
| [10704775](https://pubmed.ncbi.nlm.nih.gov/10704775/) | 2000 | Animal study | Neurosci Lett | Doxapram accentuated white matter injury in neonatal rats after bilateral carotid artery occlusion |
| [8870121](https://pubmed.ncbi.nlm.nih.gov/8870121/) | 1996 | Animal study | Semin Perinatol | Modulators of hypoxic pulmonary vasoconstriction and response to inhaled nitric oxide in a piglet atelectasis model |
| [4398848](https://pubmed.ncbi.nlm.nih.gov/4398848/) | 1971 | Animal study | Anesth Analg | Hemodynamic responses to doxapram in normovolemic and hypovolemic dogs |
| [4397240](https://pubmed.ncbi.nlm.nih.gov/4397240/) | 1971 | Clinical/experimental | Proc Soc Exp Biol Med | Doxapram in hemorrhagic hypotension |
| [4706757](https://pubmed.ncbi.nlm.nih.gov/4706757/) | 1973 | Case report | Anesthesiology | Recovery from central respiratory failure and doxapram administration in a patient with a brainstem lesion |
| [4388361](https://pubmed.ncbi.nlm.nih.gov/4388361/) | 1966 | Human physiology study | Acta Anaesthesiol Scand Suppl | EEG effects of doxapram in humans |

None of these studies evaluates doxapram as a treatment for vascular disease.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 39172 | Caropram 20mg Injection (Khandelwal Laboratories Pvt Ltd) | Vial of 5 ml injection | Not stated in the available data |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** epilepsy, chronic obstructive pulmonary disease, asthma, kidney disease, liver disease, brain edema, hypotensive disorder, stroke and cerebrovascular disorders, pulmonary embolism, coronary artery disease, atherosclerosis, sudden cardiac arrest, heart conduction disease, and pheochromocytoma or paraganglioma.
- **Drug Interactions:** 55 interactions were identified. Major ones include bupropion, methylene blue, iobenguane (I-131), iohexol, iopamidol, and tramadol. Moderate ones include epinephrine, ephedrine, phenylephrine, pseudoephedrine, salbutamol, formoterol, and arformoterol, among others.
- **Literature safety signals:** white matter injury in neonatal rats under cerebral ischemia, adverse events with continuous infusion, and an association between prolonged use in preterm infants and developmental delay.

Many of the contraindicated conditions are cardiovascular or cerebrovascular, which runs directly counter to the predicted vascular indication. Please refer to the package insert for label warnings.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a nonspecific computational score. There are no clinical trials, no literature showing benefit in vascular disease, and the safety signals and knowledge-graph contraindications include cardiovascular and cerebrovascular conditions.

**To proceed, the following is needed:**
- Mechanism of action data to assess any plausible link to vascular pathology
- Package insert warnings and contraindications for the Indian product
- Clarification of which specific vascular condition is intended, since "vascular disease" is too broad
- Preclinical or clinical evidence of benefit in a defined vascular condition
- A review of the cardiovascular safety profile relative to the proposed use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

