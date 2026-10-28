---
layout: default
title: Capecitabine
parent: Model Prediction Only (L5)
nav_order: 138
evidence_level: L5
indication_count: 1
monitor_inn: "Capecitabine"
predicted_indications: ["gastric adenocarcinoma and proximal polyposis of the stomach"]
last_modified_at: 2026-10-23
description: "Capecitabine: predicted new indication Gastric adenocarcinoma and proximal polyposis of the stomach (evidence level L5). Approved use: Relations recorded in the knowledge graph: metastasis from malig…"
---

# Capecitabine
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

## Capecitabine: From Gastric Cancer to Gastric Adenocarcinoma and Proximal Polyposis of the Stomach
{: .text-alpha }

## One-Sentence Summary

Capecitabine is an oral chemotherapy drug whose recorded uses in the knowledge graph include colon cancer metastasis and gastric cancer.
The TxGNN model predicts it may be effective for **gastric adenocarcinoma and proximal polyposis of the stomach (GAPPS)**,
but currently there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relations recorded in the knowledge graph: metastasis from malignant tumour of colon, gastric cancer, gastric neoplasm, diffuse gastric adenocarcinoma, gastric linitis plastica, gastric carcinoma (no approved indication text is available in the local licence records) |
| Predicted New Indication | Gastric adenocarcinoma and proximal polyposis of the stomach |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | At least 20 single-ingredient licences (the list may be partial) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, capecitabine is an oral prodrug of 5-fluorouracil, a fluoropyrimidine that inhibits thymidylate synthase and disrupts DNA synthesis in rapidly dividing tumour cells.

The TxGNN model (deep learning) links capecitabine to gastric adenocarcinoma and proximal polyposis of the stomach. This may reflect similarities the model learned between related diseases, such as several gastric cancer types, not biological evidence. GAPPS is a rare hereditary syndrome, associated with APC promoter 1B mutations, with fundic gland polyposis and an increased risk of gastric adenocarcinoma. The plausible connection is that capecitabine would act on the gastric adenocarcinoma component, not on the polyposis or the underlying genetic defect.

The very high score is therefore largely consistent with the existing gastric cancer relations and is not a true repurposing signal. No GAPPS-specific evidence was found, so this reasoning is unvalidated.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## India Market Information

At least 20 single-ingredient capecitabine licences are valid (the list may be partial). The licence records contain no approved indication text. Main examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 44781 | Cabita 500mg Tablet | Strip of 10 tablets | Not stated in the records |
| 152605 | Naprocap 500mg Tablet | Strip of 10 tablets | Not stated in the records |
| 249367 | Zocitab 500mg Tablet | Strip of 10 tablets | Not stated in the records |
| 41089 | Capcel 500 Tablet | Strip of 10 tablets | Not stated in the records |
| 34293 | Capegard 500 Tablet | Strip of 10 tablets | Not stated in the records |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions. The knowledge graph records neutropenia, thrombocytopenia, agranulocytosis and anaemia as contraindication-related conditions. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count, liver and renal function (given the conditions listed below) |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication-related conditions (knowledge graph relations, not label text):** liver disease, gallbladder disease, thrombocytopenia, infectious disease, neutropenia, agranulocytosis, coronary artery disease, anaemia, macrocytic anaemia, hyperbilirubinaemia, hereditary hyperbilirubinaemia, Gilbert syndrome, impaired renal function, sudden cardiac arrest, heart conduction disease, necrotizing enterocolitis, stomatitis, and dihydropyrimidine dehydrogenase deficiency.
- **Drug Interactions:** 335 interactions were recorded. Moderate-level examples are metronidazole and tinidazole. Minor-level examples are aluminium hydroxide, levofloxacin, magaldrate, and magnesium carbonate, hydroxide and oxide. Many others have an unknown severity level (e.g. pantoprazole, omeprazole, lansoprazole, metformin, glimepiride, morphine, simvastatin, prednisone).

Package insert warnings were not available, so please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5), with no trials or publications on this disease. The link mostly reflects capecitabine's existing gastric cancer use rather than a new therapeutic opportunity for the polyposis syndrome.

**To proceed, the following is needed:**
- GAPPS-specific clinical or case evidence for capecitabine
- Mechanism of action data
- Package insert warnings and contraindications from the India licence holders, for safety screening
- Approved indication text for the local licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

