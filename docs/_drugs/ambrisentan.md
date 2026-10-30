---
layout: default
title: Ambrisentan
parent: Model Prediction Only (L5)
nav_order: 45
evidence_level: L5
indication_count: 5
monitor_inn: "Ambrisentan"
predicted_indications: ["pulmonary arteriovenous malformation (disease)", "malformation syndrome with odontal and/or periodontal component", "hypotrichosis simplex of the scalp", "hypertrichosis (disease)", "syndrome with a Dandy-Walker malformation as major feature"]
last_modified_at: 2026-10-30
description: "Ambrisentan: predicted new indication pulmonary arteriovenous malformation (disease) (evidence level L5). Approved use: Not recorded in the local data"
---

# Ambrisentan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ambrisentan: Endothelin receptor antagonist → pulmonary arteriovenous malformation (disease)
{: .text-alpha }

## One-Sentence Summary

Ambrisentan is an endothelin receptor antagonist, a drug class that relaxes and widens blood vessels.
The TxGNN model predicts it may be effective for **pulmonary arteriovenous malformation (disease)**,
but the support is thin: **0 clinical trials** and **1 publication**, a case report that does not directly study treatment of this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | pulmonary arteriovenous malformation (disease) |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (10 of 10) – CDSCO approval status is not included in this data |
| Number of Listed Products | 10 (valid: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Ambrisentan is generally understood to block the endothelin A receptor, which reduces constriction of blood vessels.

The only linked publication describes pulmonary arterial hypertension in a patient with hereditary hemorrhagic telangiectasia (HHT), a vascular malformation disorder. It is a single case-level report of two conditions occurring together. It does not show that ambrisentan treats pulmonary arteriovenous malformations. Endothelin receptor antagonism is not an established way to close or prevent such malformations.

The high TxGNN score likely reflects the model's proximity to pulmonary vascular disease rather than a demonstrated therapeutic effect. There is also a theoretical concern: dilating the pulmonary vessels could change shunt physiology in patients with these malformations.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33969094](https://pubmed.ncbi.nlm.nih.gov/33969094/) | 2021 | Case report | World Journal of Clinical Cases | Pulmonary arterial hypertension in a patient with hereditary hemorrhagic telangiectasia, with genetic analysis of family members; raises awareness of this combination of conditions |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 72527 | Endobloc T Combipack | Packet of 20 tablets | Not recorded |
| 247591 | Zambri 5mg Tablet | Strip of 10 tablets | Not recorded |
| 611 | Ambrican 5 Tablet | Strip of 10 tablets | Not recorded |
| 249050 | Zambri 10mg Tablet | Strip of 10 tablets | Not recorded |
| 109448 | Ibitan 5mg Tablet | Strip of 10 tablets | Not recorded |

## Safety Considerations

- **Disease-related cautions**: The data compiled for this report flag congestive heart failure, anemia, macrocytic anemia and pulmonary veno-occlusive disease as conditions of concern with this drug. These come from relationship data, not from label text.
- **Embryo-fetal toxicity**: Ambrisentan is teratogenic and carries a boxed warning for embryo-fetal toxicity.
- **Drug Interactions**: 112 interactions were recorded. Moderate-level ones include canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, eliglustat and naltrexone. Minor-level ones include clarithromycin, miconazole and omeprazole.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial studies ambrisentan in pulmonary arteriovenous malformation, and the only publication is a case report of a coexisting condition. There is no established mechanism, so the prediction is best treated as a model signal that needs verification.

**To proceed, the following is needed:**
- Mechanistic evidence on whether endothelin A receptor blockade affects pulmonary arteriovenous malformations
- Studies or case series that directly assess ambrisentan in patients with these malformations, including effects on shunt physiology
- Package insert warnings and contraindications from the Indian licences
- Detailed mechanism of action data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

