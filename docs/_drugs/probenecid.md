---
layout: default
title: Probenecid
parent: Model Prediction Only (L5)
nav_order: 701
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
description: "Probenecid: predicted new indication Renal hypouricemia (evidence level L5). Approved use: Gout"
monitor_inn: "Probenecid"
predicted_indications: ["hypouricemia, renal", "Lesch-Nyhan syndrome", "hypoxanthine guanine phosphoribosyltransferase partial deficiency"]
---

# Probenecid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Probenecid: From Gout to Renal Hypouricemia
{: .text-alpha }

## One-Sentence Summary

Probenecid is a uricosuric drug originally used to treat gout and hyperuricemia.
The TxGNN model predicts it may be effective for **renal hypouricemia**, but there are **no registered clinical trials** and **20 publications** that only describe the disease, with none showing a benefit from probenecid.
The mechanism points in the opposite direction, so this prediction is most likely a false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout; hyperuricemia |
| Predicted New Indication | Renal hypouricemia |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. From general pharmacological knowledge, probenecid is a uricosuric that blocks the renal urate transporter URAT1 (SLC22A12) and the organic anion transporters OAT1/OAT3. This increases urate excretion in urine and lowers serum urate, which is why it works in gout.

Renal hypouricemia is mostly caused by loss-of-function mutations in URAT1, so the kidney already wastes urate. The TxGNN score most likely reflects network proximity: the drug and the disease share the same urate-transport genes and pathways. That is not a therapeutic relationship. Probenecid would be expected to worsen the condition rather than treat it. In the literature, probenecid appears only as a diagnostic probe, where the response of urate clearance to probenecid and pyrazinamide is used to classify the type of tubular defect.

**Other predictions in the model output (both rated Hold, L5):**
- **Lesch-Nyhan syndrome** (score 0.9939): The disease causes purine overproduction and severe hyperuricemia. Probenecid could lower serum urate, but it would not help the neurological and behavioral features, which are the main burden. Extra uric acid in urine raises the risk of kidney stones and nephropathy. Xanthine oxidase inhibitors such as allopurinol are the standard approach. The two retrieved papers are not relevant (a computational modeling study and a 1976 Tourette's syndrome overview).
- **Partial HPRT deficiency** (score 0.9937): This overlaps with gout and hyperuricemia, but the same overproduction and kidney-stone concerns apply. There is no direct literature and no trial.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The publications below concern renal hypouricemia. None tests probenecid as a treatment. Most are reviews, case reports or physiological studies, and none is an RCT.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clin Rheumatol | Update on hypouricemia (serum urate < 2 mg/dL) for rheumatologists, covering causes and clinical features |
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review | Mol Genet Metab | Hereditary renal hypouricemia, mostly due to loss-of-function mutations in SLC22A12 (URAT1) |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort/Genetic | J Am Soc Nephrol | SLC22A12 sequencing in 32 patients; links URAT1 genotype to urate excretion |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Review/Case report | Am J Kidney Dis | Prevention of exercise-induced acute renal failure in renal hypouricemia, with literature review |
| [8976099](https://pubmed.ncbi.nlm.nih.gov/8976099/) | 1996 | Review | Nihon Rinsho | Concept and classification of abnormalities in urate metabolism |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Case report | Nephron | Familial hypouricemia with a blunted uric acid clearance response to probenecid and pyrazinamide, indicating a reabsorption defect |
| [8341392](https://pubmed.ncbi.nlm.nih.gov/8341392/) | 1993 | Case report | Nephron | Novel renal hypouricemia type with no urate response to probenecid or pyrazinamide |
| [7099326](https://pubmed.ncbi.nlm.nih.gov/7099326/) | 1982 | Case report | Nephron | Familial renal hypouricemia in which urate excretion paradoxically decreased after probenecid |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | Case report | Nephron | Hypouricemia with enhanced urate secretion and urolithiasis; probenecid used as a diagnostic probe |
| [2709741](https://pubmed.ncbi.nlm.nih.gov/2709741/) | 1989 | Case report | Klin Wochenschr | Acute renal failure from uric acid nephropathy in a patient with renal hypouricemia; urate excretion enhanced by probenecid |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 26110 | Bencid Tablet | Strip of 10 tablets (oral) | Not specified |

---

## Safety Considerations

The drug-drug interaction data compiled for this report list 71 interactions. The main ones are:

- **Major:** phenylbutyric acid; glycerol phenylbutyrate
- **Moderate:** acetylsalicylic acid (aspirin); sulfonylureas and related glucose-lowering drugs (chlorpropamide, glimepiride, glipizide, glyburide, tolbutamide, tolazamide, acetohexamide); meglitinides (repaglinide, nateglinide)
- **Minor:** famotidine, amoxicillin, levofloxacin, eluxadoline

**Knowledge-graph contraindication signals** (from a computational knowledge graph, not from label text) include:
- Liver failure
- Kidney disease and impaired renal function
- Blood disorders: thrombocytopenia, leukopenia, agranulocytosis, neutropenia
- Peptic ulcer disease
- Muscle disorders such as myopathy and rhabdomyolysis
- Diarrheal disease and *Clostridium difficile* colitis

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is high, but it is not backed by any clinical trial or any literature showing benefit. The known pharmacology (URAT1 inhibition increasing urate excretion) would worsen renal hypouricemia, so the prediction is probably a false positive. The other two predicted indications are also unsupported and carry a kidney-stone risk.

**To proceed, the following is needed:**
- Mechanism of action data confirmed from DrugBank
- Package insert warnings and contraindications from the Indian manufacturer
- Evidence that probenecid has a therapeutic, not just a diagnostic, role in the predicted conditions. Without this, the repurposing direction should be reconsidered.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

