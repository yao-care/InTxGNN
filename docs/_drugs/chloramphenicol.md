---
layout: default
title: Chloramphenicol
parent: Model Prediction Only (L5)
nav_order: 170
evidence_level: L5
indication_count: 9
monitor_inn: "Chloramphenicol"
predicted_indications: ["conjunctivitis", "diffuse scleroderma", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-10-27
description: "Chloramphenicol: predicted new indication conjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Chloramphenicol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Chloramphenicol: Bacterial ribosome (50S) inhibitor antibiotic → conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Chloramphenicol is a broad-spectrum bacteriostatic antibiotic that blocks protein synthesis in bacteria.
The TxGNN model predicts it may be useful for **conjunctivitis**,
and the data compiled for this report include **no registered clinical trials** and **19 publications**, mostly reviews, commentaries and older comparative studies of topical eye use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | conjunctivitis |
| TxGNN Prediction Score | 0.9966 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | at least 20 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Chloramphenicol binds the 50S subunit of the bacterial ribosome and stops bacterial protein synthesis. Because many cases of conjunctivitis are caused by bacteria, this mechanism is directly relevant to the eye surface infections the drug would be used for.

Several marketed Indian products are already eye ointments and eye drops containing chloramphenicol, so the predicted use fits formulations that exist on the market. The literature describes topical chloramphenicol as widely used for conjunctivitis in some countries, such as the UK, and rarely used for it in others, such as the US.

Note that the original mechanism-of-action field was not available in the compiled data; the description above reflects the drug's well-known pharmacology. Several of the retrieved papers are comparative studies of eye infections (for example fusidic acid vs chloramphenicol, and moxifloxacin vs chloramphenicol), but none of them is a registered trial and the evidence is mainly comparative, observational or review-level. Because the data compiled for this report contain no clinical trials, the evidence level is held at L5 under the reporting rules, even though the literature discusses the use itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32959365](https://pubmed.ncbi.nlm.nih.gov/32959365/) | 2020 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Interventions to prevent ophthalmia neonatorum (neonatal conjunctivitis) |
| [38511104](https://pubmed.ncbi.nlm.nih.gov/38511104/) | 2024 | Comparative clinical study | Curr Ther Res | Moxifloxacin compared with chloramphenicol for bacterial eye infections |
| [3554881](https://pubmed.ncbi.nlm.nih.gov/3554881/) | 1987 | Randomized single-blind comparison | Acta Ophthalmol | Fusidic acid vs chloramphenicol drops in acute purulent conjunctivitis: success 84% vs 81% |
| [3300139](https://pubmed.ncbi.nlm.nih.gov/3300139/) | 1987 | Open randomized comparison | Acta Ophthalmol | Fusidic acid, chloramphenicol and framycetin drops in Tanzania; success 93%, 48% and 74% respectively |
| [11270936](https://pubmed.ncbi.nlm.nih.gov/11270936/) | 2001 | Review | Drugs | Comparative review of topical ophthalmic antibacterials |
| [8800624](https://pubmed.ncbi.nlm.nih.gov/8800624/) | 1996 | Safety review | Drug Saf | Debated link between ocular chloramphenicol and aplastic anaemia |
| [7498557](https://pubmed.ncbi.nlm.nih.gov/7498557/) | 1995 | Review/commentary | Eye (Lond) | Appropriate use of topical chloramphenicol |
| [10589371](https://pubmed.ncbi.nlm.nih.gov/10589371/) | 1999 | Review | Clin Pharmacokinet | Treatment of ocular infections with topical antibacterials |
| [7153511](https://pubmed.ncbi.nlm.nih.gov/7153511/) | 1982 | Clinical observation | J Hyg (Lond) | Prior chloramphenicol drops delayed symptoms in chlamydial neonatal conjunctivitis, but swabs stayed positive in 85% |
| [25833086](https://pubmed.ncbi.nlm.nih.gov/25833086/) | 2015 | Commentary | Clin Exp Ophthalmol | Over-the-counter chloramphenicol use |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 19864 | Actimycetin Suspension | Suspension, bottle of 50 ml | Not recorded |
| 3564 | Anchlor-DX Eye Ointment | Eye ointment, tube of 5 gm | Not recorded |
| 104582 | Hytan C Eye Ointment | Eye ointment, tube of 5 gm | Not recorded |
| 13543 | Armycetin Capsule | Capsule, packet of 100 | Not recorded |
| 120346 | Kidopalm 125mg Syrup | Syrup, bottle of 50 ml | Not recorded |

The list shows five of 20 valid single-ingredient licences. The records may be partial.

## Safety Considerations

- **Blood and organ-related cautions**: Safety records for this drug flag cautions in people with kidney disease, liver disease, gallbladder disease, thrombocytopenia, anaemia, aplastic anaemia, neutropenia and other blood-cell disorders, agranulocytosis, peripheral neuropathy, optic neuritis, acute intermittent porphyria and paroxysmal nocturnal hemoglobinuria. These come from drug-disease contraindication records, not from label text.
- **Aplastic anaemia**: The literature discusses a controversial link between topical ocular chloramphenicol and aplastic anaemia.
- **Stewardship**: Commentaries raise concerns about over-the-counter use and antimicrobial stewardship.
- **Drug Interactions**: 478 interactions are recorded. Major-level ones include cisapride and naloxegol. Moderate-level ones include metronidazole, aprepitant, budesonide, sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide), repaglinide, simvastatin, rosuvastatin and iron.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is a good fit for bacterial conjunctivitis and eye formulations are already marketed in India, but the compiled data contain no registered trials, and the literature is mostly comparative, review-level or commentary. The blood toxicity concern, particularly aplastic anaemia, requires safeguards.

**To proceed, the following is needed:**
- Controlled trials, or a systematic review, that directly evaluate chloramphenicol for conjunctivitis
- Package insert warnings and contraindications for the Indian products
- Confirmed mechanism-of-action data from a reference source
- A plan to limit use to the topical route, with stewardship and haematological safety guidance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

