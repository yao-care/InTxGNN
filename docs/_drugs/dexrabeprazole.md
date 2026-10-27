---
layout: default
title: Dexrabeprazole
parent: Moderate Evidence (L3-L4)
nav_order: 256
evidence_level: L3
indication_count: 6
last_modified_at: 2026-10-14
description: "Dexrabeprazole: predicted new indication Active peptic ulcer disease (evidence level L3). Approved use: Gastric ulcer, peptic ulcer disease, gastroesophageal reflux disease…"
monitor_inn: "Dexrabeprazole"
predicted_indications: ["duodenal obstruction", "gastroduodenitis"]
---

# Dexrabeprazole
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **6** 
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

## Dexrabeprazole: From Acid Peptic Disorders to Active Peptic Ulcer Disease
{: .text-alpha }

## One-Sentence Summary

Dexrabeprazole is the R-enantiomer of rabeprazole, a proton pump inhibitor originally used for acid-related stomach and oesophageal conditions such as gastric ulcer, duodenal ulcer and gastroesophageal reflux disease.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, which sits very close to its existing uses, so this is closer to an on-label use than true repurposing.
Support currently consists of **0 clinical trials** and **1 publication** (a postmarketing surveillance study).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric ulcer, peptic ulcer disease, gastroesophageal reflux disease, esophagitis, duodenal ulcer, Zollinger-Ellison syndrome (from the knowledge graph; no approved indication text is available in the India licence records) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L3 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 17 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general proton pump inhibitor pharmacology, dexrabeprazole is the R-enantiomer of rabeprazole. It irreversibly blocks H+/K+-ATPase in gastric parietal cells and suppresses acid secretion.

Active peptic ulcer disease is closely aligned with the drug's known indications (gastric ulcer, duodenal ulcer, peptic ulcer disease). Acid suppression is the standard approach for ulcer healing, so the prediction is mechanistically coherent. It is essentially a near-label or on-label use.

Other lower-ranked predictions are less convincing. Peptic ulcer perforation (a surgical emergency in which a PPI is at most adjunctive), duodenal obstruction (a mechanical condition) and duodenogastric reflux (driven by bile rather than acid) have no supporting studies, and their support rests on prediction scores alone. Gastrojejunal ulcer and gastroduodenitis are mechanistically plausible but have little or no direct evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19585824](https://pubmed.ncbi.nlm.nih.gov/19585824/) | 2009 | Postmarketing surveillance (observational) | Journal of the Indian Medical Association | Study of 4,931 patients with acid peptic disorders in India. It reconfirmed safety and efficacy, and reports that dexrabeprazole at half the rabeprazole dose showed favourable pharmacokinetics and faster, greater healing than rabeprazole. It is uncontrolled and does not report outcomes specific to active peptic ulcer disease. |

One further paper (PMID 27134889, a hospital prescribing-pattern study) was linked to gastrojejunal ulcer. It is not efficacy evidence and is not listed above.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 192477 | Rozydex 10mg Tablet | Strip of 10 tablets | Not stated in the records |
| 62833 | Dexlet 10mg Tablet | Strip of 10 tablets | Not stated in the records |
| 202744 | Sulpraz 10mg/75mg Capsule | Strip of 10 capsules | Not stated in the records |
| 123491 | Levopraz 10mg/75mg Capsule | Strip of 10 capsules | Not stated in the records |
| 61569 | Dexarab 10mg Tablet | Strip of 10 tablets | Not stated in the records |

All 17 registrations are valid single-ingredient products. Only the first five are shown. Formulations are oral (tablets, capsules and sustained-release capsules).

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): liver failure, liver disease, gallbladder disease, congestive heart failure, osteoporosis, postmenopausal osteoporosis, bone fracture and chronic atrophic gastritis.

Please refer to the package insert for full warnings, contraindications and drug interaction information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Active peptic ulcer disease is essentially within dexrabeprazole's existing acid-related indications, and the drug is widely marketed in India. However, the only direct evidence is one uncontrolled postmarketing study, and package insert safety data are missing. The other predicted indications (perforation, duodenal obstruction, duodenogastric reflux, gastroduodenitis, gastrojejunal ulcer) should stay at Hold or Research Question until supporting evidence appears.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory records (a blocking gap for safety screening)
- Confirmed mechanism of action data from DrugBank
- Controlled trial evidence (for example, ulcer healing rates versus rabeprazole or another PPI)
- Review of the knowledge-graph contraindication signals (liver disease, osteoporosis and fracture risk, heart failure) against label text
- Interaction data, since the query returned no results
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

