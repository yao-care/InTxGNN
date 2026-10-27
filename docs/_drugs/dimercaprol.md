---
layout: default
title: Dimercaprol
parent: Moderate Evidence (L3-L4)
nav_order: 272
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Dimercaprol: predicted new indication Bronchitis (evidence level L4). Approved use: Not stated in the India license data (the approved indication text is…"
monitor_inn: "Dimercaprol"
predicted_indications: ["bronchitis"]
---

# Dimercaprol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **1** 
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

## Dimercaprol: From Heavy Metal Poisoning (Chelation) to Bronchitis
{: .text-alpha }

## One-Sentence Summary

Dimercaprol is a dithiol chelating agent that binds heavy metals such as mercury, arsenic, and lead. The TxGNN model predicts it may be effective for **bronchitis**, but there are **no registered clinical trials** and only **1 publication** (a 1963 case report of mercury-induced bronchitis). The prediction rests almost entirely on the computational score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license data (the approved indication text is blank) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, dimercaprol is a dithiol chelating agent that binds heavy metals such as mercury, arsenic, and lead. The India license entry does not record an approved indication.

The only linked publication is a 1963 case report describing bronchitis after acute mercury inhalation. In that setting, bronchitis is a consequence of metal poisoning. Chelation would address the underlying poisoning, not the bronchitis itself. There is no evidence that dimercaprol acts on bronchitis from other causes (infectious, allergic, or chronic obstructive).

The very high TxGNN score (99.54%) is a computational prediction only and is not backed by clinical data. The mechanistic link is therefore weak.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14068440](https://pubmed.ncbi.nlm.nih.gov/14068440/) | 1963 | Case report | The American Review of Respiratory Disease | Report of two cases of bronchitis caused by acute mercury inhalation (no abstract available; the link is to metal-toxicity-related bronchitis, not general bronchitis) |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 26751 | B A L Injection (Samarth Life Sciences Pvt Ltd) | Ampoule of 2 ml Injection | Not stated |

## Safety Considerations

- **Conditions flagged as contraindications in the knowledge graph** (derived from drug-disease links in the TxGNN knowledge graph, not from label text): hypertensive disorder, hypertension, liver disease, gallbladder disease, G6PD deficiency, glycogen storage disease, cystinuria, galactosemia.
- **Drug Interactions**: 15 interactions rated Major were found. They involve:
  - Iron products: iron, ferric carboxymaltose, tetraferric tricitrate decahydrate, ferric derisomaltose, ferrous fumarate, ferrous gluconate, ferrous sulfate anhydrous, ferumoxides, ferumoxsil, ferumoxytol, iron dextran, iron protein succinylate, iron sucrose, and sodium ferric gluconate complex.
  - Selenium.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score and a single 1963 case report in which bronchitis was a result of mercury poisoning. There are no clinical trials, and no evidence of benefit in bronchitis of other causes. The safety profile also raises concerns (knowledge-graph contraindications including hypertension and liver disease, and Major interactions with iron and selenium).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India license (currently missing, and needed before any safety screening)
- Mechanism of action data (for example from DrugBank) to test whether any mechanism links chelation to bronchitis
- Evidence of benefit in bronchitis from causes other than metal poisoning, such as preclinical or clinical studies
- Confirmation of the approved indication for the India registration
- Assessment of route compatibility (the product is injectable only)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

