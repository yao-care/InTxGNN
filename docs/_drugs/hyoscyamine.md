---
layout: default
title: Hyoscyamine
parent: Model Prediction Only (L5)
nav_order: 417
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Hyoscyamine: predicted new indication Gastroduodenitis (evidence level L5). Approved use: Peptic ulcer disease"
monitor_inn: "Hyoscyamine"
predicted_indications: ["gastroduodenitis"]
---

# Hyoscyamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Hyoscyamine: From Peptic Ulcer Disease to Gastroduodenitis
{: .text-alpha }

## One-Sentence Summary

Hyoscyamine is an antimuscarinic drug originally used to treat peptic ulcer disease.
The TxGNN model predicts it may be effective for **gastroduodenitis**,
but at present there are **no registered clinical trials** and only **1 loosely related publication** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease |
| Predicted New Indication | Gastroduodenitis |
| TxGNN Prediction Score | 0.9959 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (4 of 4) – CDSCO approval status is not included in this data |
| Number of Listed Products | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for hyoscyamine: "Hyoscyamine sulfate inhibits specifically the actions of acetylcholine on structures innervated by postganglionic cholinergic nerves and on smooth muscles that respond to acetylcholine but lack cholinergic innervation. These peripheral cholinergic receptors are present in the autonomic effector cells of the smooth muscle, cardiac muscle, the sinoatrial node, the atrioventricular node, and the exocrine glands." ([DailyMed: Nulev (hyoscyamine sulfate) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ae2a78b2-b811-11e2-9e96-0800200c9a66), label version 2025-07-15; accessed 2026-11-19.) Based on general pharmacology, hyoscyamine is a non-selective competitive antagonist of muscarinic acetylcholine receptors. Blocking M3 receptors on gastric parietal cells and on smooth muscle can reduce gastric acid secretion, gastrointestinal motility and spasm.

Peptic ulcer disease and gastroduodenitis are both upper gastrointestinal conditions. Symptom control through reduced acid secretion and reduced spasm is plausible in both. This link is inferred from general pharmacology, not from the supplied data.

The high TxGNN score (0.9959) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It is a model prediction and is not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10696836](https://pubmed.ncbi.nlm.nih.gov/10696836/) | 2000 | Review | Endoscopy | Review of premedication, preparation and surveillance for endoscopy (sedation practice, propofol use, consent). It does not directly assess hyoscyamine in gastroduodenitis, so its relevance is low. |

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 26567 | Biospan 10mg Tablet | Strip of 10 tablets | Valid |
| 75136 | Eupep Syrup | Bottle of 200 ml Syrup | Valid |
| 103672 | Hyocimax-S Tablet | Strip of 10 disintegrating strips | Valid |
| 103902 | Hyocimax-S Injection 1ml | Packet of 10 injections | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications (from knowledge-graph drug-disease links, not label text)**: The knowledge graph links hyoscyamine to a wide range of conditions where caution or avoidance may apply, including:
  - Cardiovascular: hypertension, congestive heart failure
  - Hepatic: liver failure, liver disease, cirrhosis, hepatic coma and encephalopathy
  - Renal and urinary: kidney disease, pyoureter, benign prostatic hyperplasia
  - Respiratory: chronic obstructive pulmonary disease
  - Gastrointestinal: gastric ulcer, gastritis, gallbladder disease
  - Metabolic and endocrine: diabetes mellitus, diabetic ketoacidosis, porphyria
  - Haematological: thrombocytopenia, neutropenia, agranulocytosis, blood coagulation disorders, haemophilia
  - Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder, substance abuse/dependence

  The presence of gastric ulcer and gastritis on this list deserves attention, because it overlaps with the predicted indication.
- **Drug Interactions**: 207 interactions were recorded. The examples listed are mostly Moderate, with a few Minor:
  - Opioids and analgesics: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol
  - Other anticholinergic or sedating agents: amitriptyline, amoxapine, chlorpheniramine, acrivastine, phenyltoloxamine, aclidinium, ethanol
  - Others: botulinum toxin type A, phenylephrine, acebutolol, amantadine, acetylcholine, ambenonium
  - Minor: acetaminophen, hydrochlorothiazide

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score and general pharmacological reasoning (Evidence Level L5). No clinical trials exist, and the single publication retrieved is not relevant to the question. Knowledge-graph links to gastric ulcer and gastritis as contraindications also warrant clarification before any further work.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed Indian products, which are required before safety screening can proceed
- Confirmed mechanism of action data from DrugBank
- A targeted literature search on antimuscarinic or hyoscyamine use in gastritis, duodenitis or gastroduodenitis
- Approved indication text for the four Indian registrations
- Clarification of the contraindication signal for gastric ulcer and gastritis
- Assessment of whether the available dosage forms suit the proposed use

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Nulev (hyoscyamine sulfate) prescribing information, Viatris Specialty LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ae2a78b2-b811-11e2-9e96-0800200c9a66) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

