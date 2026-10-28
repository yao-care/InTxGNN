---
layout: default
title: Cisapride
parent: Model Prediction Only (L5)
nav_order: 185
evidence_level: L5
indication_count: 4
monitor_inn: "Cisapride"
predicted_indications: ["gastrojejunal ulcer", "peptic ulcer perforation", "gastric ulcer (disease)", "gastroduodenitis"]
last_modified_at: 2026-10-28
description: "Cisapride: predicted new indication gastrojejunal ulcer (evidence level L5). Approved use: Not recorded in the local data"
---

# Cisapride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Cisapride: 5-HT4 receptor agonist prokinetic → gastrojejunal ulcer
{: .text-alpha }

## One-Sentence Summary

Cisapride is a prokinetic agent that stimulates gut motility through the 5-HT4 receptor and is marketed in India.
The TxGNN model predicts it may be useful for **gastrojejunal ulcer**, but the data compiled for this report contain **no clinical trials** for this disease, and the **20 publications** retrieved are mostly reviews or work on related conditions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | gastrojejunal ulcer |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. From the literature, cisapride is a substituted benzamide that enhances acetylcholine release from the enteric nervous system. This stimulates motility along the gastrointestinal tract, improving gastric emptying and oesophageal clearance.

Gastrojejunal (anastomotic or marginal) ulcers occur after gastric surgery. A prokinetic could plausibly reduce acid and bile exposure of the anastomotic mucosa by speeding emptying and limiting reflux. This link is indirect. A rat study (PMID 9304418) found cisapride influenced ulcer formation and gastric secretion, but it was preclinical and did not study this disease.

No cited study directly examines cisapride in gastrojejunal ulcer. Acid suppression with proton pump inhibitors remains the standard approach. The high TxGNN score therefore remains a model-based signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of these publications studies gastrojejunal ulcer directly. They address reflux disease, gastric or duodenal ulcer, dysmotility and related topics.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8527013](https://pubmed.ncbi.nlm.nih.gov/8527013/) | 1995 | Review (risk-benefit) | Drug Safety | Reviews cisapride's benefits and risks across GI disorders including reflux disease, dyspepsia and gastroparesis |
| [2690321](https://pubmed.ncbi.nlm.nih.gov/2690321/) | 1989 | Review | Scand J Gastroenterol Suppl | Cisapride relieved reflux symptoms and healed oesophagitis, outperforming placebo and metoclopramide on symptoms |
| [1978403](https://pubmed.ncbi.nlm.nih.gov/1978403/) | 1990 | Review | Scand J Gastroenterol Suppl | Cisapride was described as the only prokinetic with proven benefit in reflux oesophagitis |
| [8409300](https://pubmed.ncbi.nlm.nih.gov/8409300/) | 1993 | Randomized double-blind trial | J Clin Gastroenterol | 60 patients with gastric ulcer compared cisapride, ranitidine and the combination (related condition, not gastrojejunal ulcer) |
| [8174950](https://pubmed.ncbi.nlm.nih.gov/8174950/) | 1993 | Double-blind placebo-controlled study | Gut | In 66 patients, cisapride was compared with placebo for preventing duodenal ulcer relapse (related condition) |
| [9304418](https://pubmed.ncbi.nlm.nih.gov/9304418/) | 1996 | Preclinical (rat) | General Pharmacology | Oral cisapride reduced experimental gastric ulcers and altered gastric secretion, compared with ranitidine and omeprazole |
| [12845759](https://pubmed.ncbi.nlm.nih.gov/12845759/) | 2000 | Clinical study | J Tongji Med Univ | Cisapride relieved symptoms in patients with delayed gastric emptying after gastric ulcer healing |
| [7601011](https://pubmed.ncbi.nlm.nih.gov/7601011/) | 1995 | Review | Drugs | Pharmacological management of reflux disease |

## India Market Information

Cisapride is marketed in India. Licence records are a partial list: at least 20 licences exist, all single-ingredient and valid. No approved-indication text is recorded in the local data. Main examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 232824 | Ulcipride 10mg Tablet | Strip of 10 tablets | Not recorded |
| 83188 | Expracid 10mg Tablet | Strip of 10 tablets | Not recorded |
| 47857 | Cisapid 1mg Suspension | Bottle of 60 ml suspension | Not recorded |
| 178527 | Prepulsid 10mg Tablet | Strip of 10 tablets | Not recorded |
| 181058 | Peristil 5mg Tablet | Strip of 10 tablets | Not recorded |

## Safety Considerations

- **Drug Interactions**: 302 interactions are recorded. Major-level ones include tramadol, nifedipine, amiodarone, amisulpride, amitriptyline, abiraterone, acetazolamide, adenosine, alfuzosin, anagrelide, apalutamide and hydrochlorothiazide. Moderate ones include famotidine, formoterol, salbutamol and loperamide.
- **Conditions of concern**: Recorded contraindication relationships include long QT syndrome (including familial), myocardial ischemia, coronary artery disease, epilepsy, kidney disease, liver disease, respiratory failure, active peptic ulcer disease, and electrolyte disturbances (potassium deficiency, hypercalcemia, hypophosphatemia). These are not taken from label text.
- **Cardiac risk**: Cisapride has been withdrawn or restricted in many markets because of QT prolongation and arrhythmia risk, many interactions arise through CYP3A4 inhibition, and this makes the risk-benefit balance unfavourable for a new use.

Please also refer to the package insert, as label warnings are not available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication directly studies cisapride in gastrojejunal ulcer, so the prediction rests on the model score alone. Together with the cardiac and interaction risks and the availability of effective acid-suppressing treatments, development is not supported at present.

**To proceed, the following is needed:**
- Direct evidence in post-surgical anastomotic or marginal ulcer, such as preclinical models or a pilot study
- Detailed mechanism of action data
- Package insert warnings and contraindications from the Indian licences
- A cardiac safety and QT monitoring plan, including management of CYP3A4-related interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

