---
layout: default
title: Tegaserod
parent: Model Prediction Only (L5)
nav_order: 810
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
description: "Tegaserod: predicted new indication Migraine disorder (evidence level L4). Approved use: Not available in the registration data"
monitor_inn: "Tegaserod"
predicted_indications: ["migraine disorder", "migraine with brainstem aura"]
---

# Tegaserod
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Tegaserod: From Gastrointestinal Motility Disorder to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Tegaserod is a serotonin 5-HT4 receptor partial agonist marketed in India as a single-ingredient oral tablet. The approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are currently **0 clinical trials** and only **1 review article** supporting this direction, so the prediction rests mainly on computational inference.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the registration data (the pharmacology suggests a gastrointestinal motility indication, but this is not confirmed by the data) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9947 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (8 of 8) – CDSCO approval status is not included in this data |
| Number of Registrations | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, tegaserod is a 5-HT4 receptor partial agonist with activity at other serotonin receptors, including 5-HT2B. It acts as a prokinetic agent, increasing gastrointestinal motility.

Serotonin signalling is central to migraine biology, since triptans act on 5-HT1B/1D receptors. Gastric stasis and nausea are also common during migraine attacks. A prokinetic effect could therefore plausibly improve absorption of oral abortive drugs or relieve associated gastrointestinal symptoms.

However, 5-HT4 agonism has no established direct antimigraine mechanism. The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence; it does not replace clinical evidence. The second-ranked prediction, **migraine with brainstem aura** (score 0.9929), is a migraine subtype. It most likely reflects its closeness to the parent migraine disease as learned by the model rather than independent evidence, and it has no clinical trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19220673](https://pubmed.ncbi.nlm.nih.gov/19220673/) | 2009 | Review | J Gastroenterol Hepatol | Reviews the effectiveness of prokinetic agents against diseases outside the gastrointestinal tract, including the central nervous system. It is general to the drug class and not specific to tegaserod in migraine. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 109868 | Ibsinorm 6mg Tablet (Sun Pharmaceutical) | Strip of 10 tablets | Not stated |
| 221586 | Tibs 6mg Tablet (Hetero Drugs) | Strip of 10 tablets | Not stated |
| 224479 | Tegibs 2mg Tablet (Torrent) | Strip of 10 tablets | Not stated |
| 221377 | Tegaspa 6mg Tablet (Lupin) | Strip of 10 tablets | Not stated |
| 223563 | Tegaser 6mg Tablet (Cadila) | Strip of 10 tablets | Not stated |

All 8 registrations are valid single-ingredient oral products. None are cancelled or combination products.

## Safety Considerations

- **Contraindications (from knowledge graph links, not label text)**: The TxGNN knowledge graph links tegaserod to the following conditions as contraindications:
  - Liver disease
  - Gallbladder and biliary tract disease
  - Obstructive jaundice
  - Stroke and cerebrovascular disorders
  - Cerebral infarction
  - Myocardial infarction and coronary thrombosis
  - Hemoglobinopathy
  - Ileus and intestinal obstruction
  - Diarrheal disease
  - Ischemic colitis

  The cardiovascular and cerebrovascular links are particularly relevant for migraine, because migraine patients, especially those with aura, already carry a higher stroke risk.
- **Drug Interactions**: 238 interactions were recorded. Those with a stated severity are minor, with ethinylestradiol and digoxin. Others have unclassified severity, including cyclosporine, pravastatin, valsartan, ramipril, tramadol, fluconazole, erythromycin, azithromycin, ticlopidine, pantoprazole and torasemide. Tramadol and the macrolides are worth checking if tegaserod were combined with typical migraine care.

Please refer to the package insert for label warnings, which were not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a computational score and one general review of prokinetic agents, with no clinical trials. The mechanistic link is indirect. The knowledge-graph contraindications for stroke and myocardial infarction raise a safety concern in a population at vascular risk.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication text from the India Pharma website (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search on tegaserod and 5-HT4 agonists in migraine, including migraine-associated gastroparesis and nausea
- A cardiovascular and cerebrovascular risk assessment for use in migraine patients
- Early-phase clinical evidence, for example a pilot study on absorption of oral abortive drugs or relief of gastrointestinal symptoms during attacks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

