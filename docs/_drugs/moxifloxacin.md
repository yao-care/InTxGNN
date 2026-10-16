---
layout: default
title: Moxifloxacin
parent: Model Prediction Only (L5)
nav_order: 571
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Moxifloxacin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Bacterial infections"
---

# Moxifloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Moxifloxacin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Moxifloxacin is a fluoroquinolone antibiotic originally used to treat bacterial infections such as pneumonia, conjunctivitis, peritonitis and plague.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (streptococcal, staphylococcal, pneumonia, peritonitis, conjunctivitis, plague and others, per the knowledge graph; no approved indication text in the India licence records) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Moxifloxacin belongs to the fluoroquinolone class of antibacterials, which inhibit bacterial DNA gyrase and topoisomerase IV. Its efficacy is established in bacterial infections.

That mechanism has no known effect on serum viscosity or on the raised polyclonal immunoglobulins that characterise hyperviscosity syndrome. The expert review of the data found no plausible mechanistic link. The high TxGNN score is a model output only and should not be read as evidence of benefit.

The other top-ranked predictions show the same pattern. Hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant haematological disease, monoclonal gammopathy, congenital haematological disorder and haematopoietic neoplasm have no supporting mechanism either. The single exception is **bubonic plague**, ranked 10th (score 99.41%). It is close to the existing label, since plague and pneumonic plague are already among the original indications. Its evidence is preclinical (see below).

## Clinical Trial Evidence

Currently no related clinical trials are registered for polyclonal hyperviscosity syndrome.

For context, trials linked to other predicted indications are indirect and not relevant to this one:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00324324](https://clinicaltrials.gov/study/NCT00324324) | Phase 3 | Terminated | 240 | Moxifloxacin vs placebo for preventing bacterial infection after allogeneic stem cell transplant (linked to congenital haematological disorder; indirect) |
| [NCT00062231](https://clinicaltrials.gov/study/NCT00062231) | NA | Terminated | 351 | Moxifloxacin alone vs ciprofloxacin plus amoxicillin/clavulanate for fever in low-risk neutropenic cancer patients (indirect) |
| [NCT07023029](https://clinicaltrials.gov/study/NCT07023029) | Phase 1 | Completed | 33 | Etavopivat cardiac repolarisation study in healthy volunteers; moxifloxacin probably a QT positive control, so no efficacy evidence |

## Literature Evidence

Currently no related literature is available for polyclonal hyperviscosity syndrome.

For the closest-to-label alternative (bubonic plague), the following preclinical and safety publications exist:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15555886](https://pubmed.ncbi.nlm.nih.gov/15555886/) | 2004 | Animal model | Int J Antimicrob Agents | Moxifloxacin, gatifloxacin and ciprofloxacin gave full protection in mouse models of systemic and pneumonic plague |
| [20052916](https://pubmed.ncbi.nlm.nih.gov/20052916/) | 2009 | Animal model | Antibiot Khimioter | Levofloxacin and moxifloxacin were highly active against Y. pestis strains in mice (ED50 5.5–14.0 mg/kg) |
| [21115791](https://pubmed.ncbi.nlm.nih.gov/21115791/) | 2011 | In vitro model | Antimicrob Agents Chemother | A pharmacodynamic model was used to derive a moxifloxacin regimen that optimises Y. pestis kill and prevents resistance |
| [21486959](https://pubmed.ncbi.nlm.nih.gov/21486959/) | 2011 | In vitro model | Antimicrob Agents Chemother | Comparative efficacy of candidate antibiotics against Y. pestis |
| [29623187](https://pubmed.ncbi.nlm.nih.gov/29623187/) | 2018 | Case report | Ther Adv Drug Saf | Moxifloxacin-induced tinnitus in an older adult (safety report) |

## India Market Information

Moxifloxacin has 20 valid single-ingredient registrations, with no cancelled ones. Approved indication text is not available in the records. Main registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 136016 | Moximac IV 400mg Infusion | 100 ml infusion bottle | Not available |
| 88744 | Fleximox 400 Tablet | Strip of 10 tablets | Not available |
| 133597 | Moxiflox Tablet (Cipla) | Strip of 5 tablets | Not available |
| 209948 | Staxom 400mg Infusion (Sun Pharma) | 250 ml infusion bottle | Not available |
| 239370 | Vodamox Eye Ointment | 5 g tube | Not available |

Available routes: oral (tablets, capsules), injectable (infusion) and ophthalmic (eye drops, eye ointment).

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text):** long QT syndrome, familial long QT syndrome, torsades de pointes, heart conduction disease, sudden cardiac arrest, myocardial ischemia, coronary artery disease, epilepsy, cirrhosis of the liver, drug-induced liver injury, potassium deficiency, tendinitis, peripheral neuropathy and peripheral nervous system disease, myasthenia gravis and neuromuscular junction disease, *Clostridium difficile* colitis, and necrotizing enterocolitis.
- **Drug Interactions:** 336 interactions were identified. Major-level ones in the sample include hydrocortisone, dexamethasone, betamethasone, triamcinolone (corticosteroids, notably relevant to tendon risk), bupropion and chlorpropamide. Moderate-level ones include antidiabetic agents (metformin, pioglitazone, alogliptin, canagliflozin, acarbose, albiglutide), famotidine, loperamide, aspirin, and calcium and potassium salts.
- **Additional concerns for the predictions:** fluoroquinolones carry a known warning for peripheral neuropathy, which is directly relevant to the predicted neuropathy-associated haematological disease. They are also known to cause blood sugar disturbances, which is relevant to congenital analbuminemia.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for polyclonal hyperviscosity syndrome is supported only by the model score (L5), with no trials, no literature and no plausible mechanism. Across all ten predictions, only bubonic plague has a coherent rationale, and that is essentially an existing label use backed by preclinical data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (the safety screening cannot proceed without them)
- Mechanism of action data from DrugBank
- Any mechanistic or clinical evidence linking moxifloxacin to hyperviscosity, otherwise deprioritise this candidate
- If a plague-related direction is pursued, human clinical data and confirmation of the approved indication text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

