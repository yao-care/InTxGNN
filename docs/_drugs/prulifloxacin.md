---
layout: default
title: Prulifloxacin
parent: Model Prediction Only (L5)
nav_order: 711
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Prulifloxacin: predicted new indication Heart disease (evidence level L5). Approved use: Not stated in the India licence data compiled for this report (prulif…"
monitor_inn: "Prulifloxacin"
predicted_indications: ["heart disease", "Laubry-Pezzi syndrome", "Pierre Robin syndrome associated with a chromosomal anomaly", "genetic syndromic Pierre Robin syndrome", "partial deletion of the long arm of chromosome 7", "orofacial clefting syndrome", "pulmonary valve disease", "disorder of fucoglycosan synthesis", "mitral valve disease", "Jeune syndrome situs inversus"]
---

# Prulifloxacin
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

## Prulifloxacin: From Bacterial Infection (Fluoroquinolone Antibacterial) to Heart Disease
{: .text-alpha }

## One-Sentence Summary

Prulifloxacin is an oral fluoroquinolone antibacterial (a prodrug of ulifloxacin), marketed in India in 11 single-ingredient tablet products.
The TxGNN model predicts it may be effective for **heart disease**, but this is a model prediction only, with **0 clinical trials** and **1 preclinical publication**, and that publication concerns the drug's cardiac safety risk (proarrhythmia) rather than any benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India licence data compiled for this report (prulifloxacin is a fluoroquinolone antibacterial) |
| Predicted New Indication | Heart disease |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences: 11 of 11) |
| Number of Registrations | 11 (valid: 11) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, prulifloxacin is a prodrug of ulifloxacin, a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV. Its established role is treating bacterial infections.

**The prediction is not mechanistically reasonable.** No credible link connects a bacterial topoisomerase inhibitor to the treatment of heart disease. The high TxGNN score (0.9994, rank 1461) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The only retrieved publication on the cardiac question (PMID 15018156, 2004) is a rabbit study comparing the proarrhythmic effects and QT-interval changes of ulifloxacin and other quinolones. It examines a safety liability, not a therapeutic benefit. Fluoroquinolones as a class carry known cardiac warnings (QT prolongation, and aortic aneurysm/dissection), which argue against use in heart disease.

The other nine predictions in the top ten (for example Laubry-Pezzi syndrome, Pierre Robin syndrome, pulmonary and mitral valve disease, orofacial clefting syndrome, Jeune syndrome situs inversus) are mostly congenital or structural conditions. They also have no mechanistic rationale and no supporting trials. They are not evaluated further here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15018156](https://pubmed.ncbi.nlm.nih.gov/15018156/) | 2004 | Preclinical (rabbit model) | J Toxicol Sci | Compared proarrhythmic effects and QT prolongation of NM394 (ulifloxacin, the active metabolite of prulifloxacin) with sparfloxacin, gatifloxacin and levofloxacin. It addresses cardiac safety risk, not therapeutic benefit. |

---

## India Market Information

Eleven valid single-ingredient licences are registered, all oral tablets (strips of 5 tablets). The approved-indication text is not recorded for any of them. The five main authorisations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 180018 | Puribact 600mg Tablet (Invision Medi Sciences) | Strip of 5 tablets | Not recorded |
| 186292 | Rulizo Tablet (Sun Pharmaceutical Industries) | Strip of 5 tablets | Not recorded |
| 174477 | Pruflox Tablet (Cipla) | Strip of 5 tablets | Not recorded |
| 173748 | Percin Tablet (Lupin) | Strip of 5 tablets | Not recorded |
| 180156 | Pruquin 600mg Tablet (Alembic Pharmaceuticals) | Strip of 5 tablets | Not recorded |

---

## Safety Considerations

No label-based warnings, contraindications or drug-interaction records were available in the data compiled for this report. Please refer to the package insert for safety information.

As a class concern, fluoroquinolones are associated with QT-interval prolongation and rare ventricular arrhythmias such as torsades de pointes. This is supported by the rabbit study above. This risk is directly relevant to any proposed use in patients with heart disease.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials, no mechanistic link, and the only relevant publication points to cardiac safety risk. Fluoroquinolone cardiac warnings argue against this use.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-marketed products, which are required for any safety screening
- Mechanism of action data from DrugBank
- A specific, biologically plausible hypothesis for a cardiac indication (for example, an infective cardiac condition), with supporting preclinical data
- A cardiac safety assessment (QT and arrhythmia risk) before any further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

