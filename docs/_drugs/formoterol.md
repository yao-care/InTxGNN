---
layout: default
title: Formoterol
parent: Model Prediction Only (L5)
nav_order: 378
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-30
monitor_inn: "Formoterol"
predicted_indications: ["respiratory malformation", "bronchitis", "Rienhoff syndrome"]
description: "Formoterol: predicted new indication Respiratory malformation (evidence level L5). Approved use: Not recorded in the local data"
---

# Formoterol
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

## Formoterol: Respiratory malformation
{: .text-alpha }

## One-Sentence Summary

Formoterol is a long-acting beta2-agonist bronchodilator, originally used for pulmonary emphysema and asthma (intrinsic and allergic).
The TxGNN model predicts it may be effective for **respiratory malformation**, but **no clinical trials** and **no directly relevant publications** support this prediction.
The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Formoterol is known as a long-acting beta2-adrenergic agonist. It relaxes airway smooth muscle and causes bronchodilation, and it is used in obstructive airway diseases such as emphysema and asthma.

Respiratory malformation is a congenital, structural developmental defect, which is a different kind of problem from reversible airflow obstruction. No plausible mechanistic link is supported. At most, bronchodilation could relieve secondary airflow symptoms, but it would not treat the malformation itself.

The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related respiratory diseases, not biological evidence. It should not be read as evidence of a true therapeutic relationship.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Nothing in the retrieved literature studies formoterol in respiratory malformation. The publications below are only loosely related, mostly covering COPD or asthma.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35115339](https://pubmed.ncbi.nlm.nih.gov/35115339/) | 2022 | RCT (crossover) | Eur Respir J | Budesonide/formoterol vs salbutamol in adult asthma. Not related to malformation |
| [22541245](https://pubmed.ncbi.nlm.nih.gov/22541245/) | 2012 | RCT | J Allergy Clin Immunol | Long-term safety of budesonide/formoterol pMDI in African American asthmatic patients |
| [40840693](https://pubmed.ncbi.nlm.nih.gov/40840693/) | 2026 | Systematic review / meta-analysis | J Am Pharm Assoc | Budesonide/glycopyrrolate/formoterol vs glycopyrrolate/formoterol in COPD |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Review | J Asthma | Budesonide/formoterol pMDI for persistent asthma |
| [14738234](https://pubmed.ncbi.nlm.nih.gov/14738234/) | 2004 | Mechanistic clinical study | Eur Respir J | Formoterol protects against platelet-activating factor-induced effects in asthma |
| [35034195](https://pubmed.ncbi.nlm.nih.gov/35034195/) | 2022 | Physiological study | Eur J Appl Physiol | Compensatory responses to increased mechanical abnormalities in COPD during sleep |
| [24842803](https://pubmed.ncbi.nlm.nih.gov/24842803/) | 2014 | Review | Prog Neuropsychopharmacol Biol Psychiatry | Cognitive dysfunction in Down syndrome. Unrelated |
| [37691104](https://pubmed.ncbi.nlm.nih.gov/37691104/) | 2023 | Case report | J Med Case Rep | Small airway disease in long COVID. Unrelated to malformation |
| [41686546](https://pubmed.ncbi.nlm.nih.gov/41686546/) | 2026 | Case report | Medicine | Allergic bronchopulmonary mycosis after lung cancer surgery. Unrelated |

## India Market Information

Formoterol has 20 valid registrations in India, all single-ingredient registrations by classification, and none has been cancelled. Approved indication text is not available for these licences. The five main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| Registration No. 176746 | Pulmofor B 200 Inhaler | Bottle of 120 MDI inhaler | AXA Parenterals Ltd |
| Registration No. 3183 | Airwin-BF 200 Capsule | Bottle of 30 capsules | Ultimate Healthcare |
| Registration No. 199689 | Symbicort 160mcg/4.5mcg Turbuhaler | Packet of 60 MDI inhaler | AstraZeneca |
| Registration No. 61813 | Duova Rotacap | Packet of 20 rotacaps | Cipla Ltd |
| Registration No. 84129 | Formoflo 250 Transhaler | Packet of 120 MDI Transhaler | Lupin Ltd |

## Safety Considerations

Package insert warnings and contraindications are not available, so please refer to the package insert for label-based safety information. The items below come from knowledge-graph relationships, not label text.

- **Disease-level contraindication signals (knowledge graph):** hypertension and other hypertensive disorders, long QT syndrome (including the familial form), epilepsy, liver disease, gallbladder disease, measles, herpes simplex virus keratitis, and a group of pituitary and hypogonadotropic hypogonadism disorders (e.g., hypopituitarism, growth hormone deficiency, Kallmann syndrome, Sheehan syndrome).
- **Drug interactions:** 462 interactions were recorded. Examples include:
  - **Moderate:**
    - QT-related or cardiac-sensitive drugs: cisapride, clarithromycin, dolasetron.
    - Sympathomimetics: ephedrine (including nasal), isometheptene, diethylpropion.
    - Antidiabetic agents: acarbose, alogliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, albiglutide, dulaglutide.
    - Famotidine.
  - **Minor:** corticosteroids (beclomethasone, betamethasone, budesonide, dexamethasone).
- **Class-level concerns (from the literature reviewed):** LABA-related cardiovascular safety and pharmacovigilance signals. LABAs should not be used as monotherapy in asthma.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no clinical trials or relevant publications, and no plausible mechanism links a bronchodilator to a structural congenital defect.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis and preclinical data for respiratory malformation, which currently do not exist
- Detailed mechanism of action data for formoterol
- Package insert warnings and contraindications from the India regulator
- Consideration of better-supported predictions from the same model run. Bronchitis (chronic or obstructive phenotype) and obstructive lung disease both reach L1 with Phase 3 COPD evidence and a "Proceed with Guardrails" recommendation. Both largely overlap with already-approved use, so they are not novel repurposing. Asthma is an original indication and likewise confirms existing use.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

