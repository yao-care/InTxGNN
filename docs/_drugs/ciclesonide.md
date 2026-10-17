---
layout: default
title: Ciclesonide
parent: Model Prediction Only (L5)
nav_order: 182
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Ciclesonide: predicted new indication Atopic eczema (evidence level L5). Approved use: Asthma (including intrinsic and allergic asthma), allergic rhinitis…"
monitor_inn: "Ciclesonide"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "bronchitis", "contact dermatitis"]
---

# Ciclesonide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Ciclesonide: From Asthma to Atopic Eczema

## One-Sentence Summary

Ciclesonide is an inhaled corticosteroid, originally used to treat asthma and allergic rhinitis.
The TxGNN model predicts it may be effective for **atopic eczema**,
but **no clinical trials and no publications** currently support this specific direction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma (including intrinsic and allergic asthma), allergic rhinitis, vasomotor rhinitis (from the knowledge graph; the approved indication text in India licences is blank) |
| Predicted New Indication | Atopic eczema |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 19 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known pharmacology, ciclesonide is an inhaled corticosteroid prodrug. It is activated by esterases to des-ciclesonide, a glucocorticoid receptor agonist with anti-inflammatory activity.

Asthma, allergic rhinitis and atopic eczema are all allergic (atopic) inflammatory conditions, and corticosteroids are an established treatment for atopic eczema. A glucocorticoid-mediated mechanism is therefore plausible.

There are important limits. The data show no dermal formulation or skin-specific pharmacology for ciclesonide, and all marketed products in India are inhaled or nasal. The high score is a model output with no clinical support behind it.

Other predictions point the same way:
- **Dermatitis, atopic** is essentially the same disease concept as atopic eczema, so the two should be treated as one candidate, not two independent signals.
- **Asthma-related traits, susceptibility to** is a genetic trait concept closely tied to the existing asthma indication. It likely reflects current use, not a new one.
- **2-hydroxyethyl methacrylate sensitization** is a contact allergy managed mainly by allergen avoidance, so the rationale for an inhaled steroid is weak.
- **Bronchitis** and **contact dermatitis** have only indirect literature (see below).

## Literature Evidence

No literature directly addresses ciclesonide in atopic eczema. The only publications retrieved relate to other lower-ranked predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Review (guideline) | Basic & Clinical Pharmacology & Toxicology | Finnish guideline on diagnosis and pharmacotherapy of stable COPD. It gives indirect context for inhaled corticosteroids in chronic airway disease (linked to the bronchitis prediction), but is not specific to ciclesonide. |
| [22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/) | 2012 | Case report | Contact Dermatitis | Systemic allergic dermatitis caused by inhaled budesonide, with cross-reactivity in patch tests to ciclesonide (linked to the contact dermatitis prediction). This is a hypersensitivity safety signal, not evidence of benefit. |

## India Market Information

There are 19 valid single-ingredient registrations. The approved indication text is blank in all records. The five below are examples:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 215349 | Triohale Rotacap (Cipla Ltd) | Packet of 30 rotacaps | Not stated |
| 44473 | Ciclospray Nasal Spray (Cipla Ltd) | Packet of 100 MDI nasal spray | Not stated |
| 215625 | Trimium Transhaler (Lupin Ltd) | Packet of 180 MDI Transhaler | Not stated |
| 55530 | Cilomist HFA 160mcg Inhaler (Zydus Cadila) | Packet of 120 MDI inhaler | Not stated |
| 249503 | Zovair Octacap Capsule (Sun Pharmaceutical Industries Ltd) | Strip of 30 capsules | Not stated |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (not label text): herpes simplex virus keratitis, adrenocortical insufficiency, Addison disease, osteoporosis, postmenopausal osteoporosis, fungal infectious disease, dermatophytosis, ocular hypertension, glaucoma, parasitic infection.
- **Drug interactions:** 63 interactions were identified. The main ones are:
  - **Major:** cladribine.
  - **Moderate:** clarithromycin, miconazole, cobicistat, fostamatinib, fosamprenavir, atazanavir, amprenavir, ceritinib, boceprevir, conivaptan, abametapir (topical) and inhaled rapid-acting human insulin.
  - **Minor:** formoterol, salbutamol, arformoterol.
  - **Level not graded:** omeprazole, lansoprazole, prednisolone, famotidine.
- **Hypersensitivity:** a published case shows cross-reactivity between budesonide and ciclesonide in patch tests, so caution is warranted in patients with corticosteroid contact allergy.

Please refer to the package insert for warnings and complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (99.96%), and corticosteroids are a plausible class for atopic eczema. However, there are no clinical trials or literature for ciclesonide in this indication (L5), no dermal formulation exists, and the only related publication points to a hypersensitivity risk.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanism-based comparison with established topical corticosteroids
- Package insert warnings and contraindications for the Indian products
- Preclinical or early clinical evidence of ciclesonide in atopic dermatitis
- Assessment of route and formulation feasibility, since current products are inhaled or nasal only
- A safety plan covering corticosteroid cross-reactivity and the contraindicated conditions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

