---
layout: default
title: Vitamin A
parent: Model Prediction Only (L5)
nav_order: 894
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vitamin A: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Vitamin deficiency disorder"
monitor_inn: "Vitamin A"
predicted_indications: ["congenital prothrombin deficiency", "biotin metabolic disease", "non-syndromic esophageal malformation", "injury", "cell proliferation disorder", "perinatal disease", "florid cemento-osseous dysplasia", "segmental odontomaxillary dysplasia", "disease by subcellular system affected", "radiation or chemically induced disorder"]
---

# Vitamin A
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

# Vitamin A: From Vitamin Deficiency Disorder to Congenital Prothrombin Deficiency (Top-Ranked Prediction), with Perinatal Disease as the Best-Supported Candidate

## One-Sentence Summary

Vitamin A is a fat-soluble vitamin originally used to treat vitamin deficiency disorders, including vitamin A deficiency.
The TxGNN model's top-ranked prediction is **congenital prothrombin deficiency**, but that prediction has **no clinical trials and no publications** behind it and is graph-based only.
Among the ten predictions, the best-supported is **perinatal disease** (specifically bronchopulmonary dysplasia in very-low-birth-weight infants), with **1 clinical trial** and **multiple Cochrane systematic reviews**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin deficiency disorder; vitamin A deficiency (the licence records list no approved indication text, so this comes from the knowledge graph) |
| Predicted New Indication | Congenital prothrombin deficiency (rank 1); best-supported alternative: perinatal disease (rank 6) |
| TxGNN Prediction Score | 99.97% (congenital prothrombin deficiency); 99.63% (perinatal disease) |
| Evidence Level | L5 (congenital prothrombin deficiency); L1 (perinatal disease) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold (congenital prothrombin deficiency); Proceed with Guardrails (perinatal disease, limited to BPD prevention in very-low-birth-weight infants) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, vitamin A (retinol) acts through its metabolite retinoic acid, which binds nuclear retinoic acid receptors to regulate cell differentiation, proliferation, and epithelial integrity. Its efficacy in correcting vitamin A deficiency is established.

**Top-ranked prediction (congenital prothrombin deficiency).** This is a coagulation factor II defect. Vitamin A has no established link to it; vitamin K is the vitamin relevant to prothrombin synthesis. The very high score appears to be a graph-based artefact, probably driven by shared "vitamin" relationships, and should not be acted on without supporting studies.

**Best-supported prediction (perinatal disease).** Vitamin A is needed for lung epithelial integrity and repair. Preterm infants are born with low vitamin A stores, and this is associated with bronchopulmonary dysplasia (BPD). Cochrane reviews of randomised trials indicate that vitamin A supplementation in very-low-birth-weight infants modestly reduces death or oxygen requirement at 36 weeks' postmenstrual age. The supporting evidence covers BPD in preterm infants, a subset of "perinatal disease", not the whole category.

**Other predictions** were mostly weak or not actionable:
- *Biotin metabolic disease, non-syndromic esophageal malformation, florid cemento-osseous dysplasia, segmental odontomaxillary dysplasia*: no direct evidence; links likely reflect graph structure. Retinoic acid signalling in foregut development is plausible for the esophageal malformation, but untested and not relevant to postnatal supplementation.
- *Disease by subcellular system affected*: an ontology classification node, not a clinical indication.
- *Injury* (L2): wound-healing reviews and two neonatal trials, but only indirectly relevant.
- *Cell proliferation disorder* and *radiation or chemically induced disorder* (L4): mechanistic and review literature only; categories too broad to define an indication.

---

## Clinical Trial Evidence

No clinical trials were found for the top-ranked prediction, congenital prothrombin deficiency. Trials for the best-supported prediction (perinatal disease) and for other predictions with trial data are shown below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01115478](https://clinicaltrials.gov/study/NCT01115478) | Not applicable | Completed | 2500 | Zinc and/or vitamin A supplementation to reduce placental malaria and adverse pregnancy outcomes (perinatal disease; partly relevant) |
| [NCT01203488](https://clinicaltrials.gov/study/NCT01203488) | Phase 1/2 | Completed | 807 | Higher-dose vitamin A vs control in extremely-low-birth-weight infants, assessing survival without BPD and sepsis risk (injury; neonatal lung injury setting) |
| [NCT02102711](https://clinicaltrials.gov/study/NCT02102711) | Not applicable | Completed | 62 | Oral vitamin A in neonates under 1500 g to prevent BPD and retinopathy of prematurity (injury; indirectly relevant) |
| [NCT04000789](https://clinicaltrials.gov/study/NCT04000789) | Not applicable | Unknown | 96 | Vitamin A + vitamin E + sodium hyaluronate eye drops vs sodium hyaluronate alone in diabetic retinopathy dry eye (cell proliferation disorder; loosely related) |

---

## Literature Evidence

No publications were found for congenital prothrombin deficiency. Key publications for the best-supported prediction (perinatal disease) and for injury are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27552058](https://pubmed.ncbi.nlm.nih.gov/27552058/) | 2016 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Vitamin A supplementation to prevent mortality and morbidity in very-low-birth-weight infants |
| [21975731](https://pubmed.ncbi.nlm.nih.gov/21975731/) | 2011 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Earlier version of the same review |
| [17943744](https://pubmed.ncbi.nlm.nih.gov/17943744/) | 2007 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Earlier version of the same review |
| [12519545](https://pubmed.ncbi.nlm.nih.gov/12519545/) | 2002 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Earlier version of the same review |
| [10796372](https://pubmed.ncbi.nlm.nih.gov/10796372/) | 2000 | Systematic review (Cochrane) | Cochrane Database Syst Rev | First version of the review; vitamin A for lung growth and epithelial integrity in preterm infants |
| [22742601](https://pubmed.ncbi.nlm.nih.gov/22742601/) | 2012 | Systematic review / meta-analysis | Paediatr Perinat Epidemiol | Vitamin A and carotenoids in pregnancy and maternal, neonatal, and infant outcomes |
| [25222155](https://pubmed.ncbi.nlm.nih.gov/25222155/) | 2014 | Review | JAMA Pediatrics | Vitamin A shortage and risk of bronchopulmonary dysplasia |
| [34181622](https://pubmed.ncbi.nlm.nih.gov/34181622/) | 2021 | Review | Plast Reconstr Surg | Systematic summary of vitamin and mineral interventions in wound care; little evidence for official recommendations |
| [34105132](https://pubmed.ncbi.nlm.nih.gov/34105132/) | 2021 | Meta-analysis | J Spec Oper Med | Vitamin A intake and fracture risk (safety signal at high intake) |
| [40901583](https://pubmed.ncbi.nlm.nih.gov/40901583/) | 2025 | Review | World J Hepatol | Vitamin A toxicity and liver pathology |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 133468 | M.V.I. Injection | Ampoule of 10 ml injection | Not stated |
| 122794 | Lycobold Capsule | Strip of 10 capsules | Not stated |
| 218506 | Tilvit Injection | Vial of 10 ml injection | Not stated |
| 233452 | Vitamin A 100000IU Syrup | Bottle of 50 ml syrup | Not stated |
| 144556 | Multiband Injection | Vial of 10 ml injection | Not stated |

Eight valid single-ingredient registrations exist in total (injection, capsule, syrup, and chewable tablet forms).

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text): kidney disease, liver disease, gallbladder disease, peptic ulcer disease, sarcoidosis, hypercalcemia, nephrocalcinosis, nephrolithiasis, hypervitaminosis, inflammatory bowel disease (including ulcerative colitis), gastroenteritis, sickle cell anemia, hemolytic anemia, hereditary hemochromatosis, hemosiderosis, Wilson disease, primary hyperoxaluria, and several other metabolic conditions.
- **Drug Interactions** (68 recorded in total; main ones listed):
  - **Major**: isotretinoin, acitretin, tretinoin (additive retinoid toxicity), and tetracycline-class antibiotics (doxycycline, tetracycline, minocycline, omadacycline, demeclocycline, eravacycline, oxytetracycline, sarecycline).
  - **Moderate**: bexarotene, bile-acid sequestrants (cholestyramine, colesevelam, colestipol), sevelamer, selpercatinib.
  - **Minor**: orlistat.
- **Dose-related concerns from the literature**: excess vitamin A is associated with liver toxicity and increased fracture risk, so dosing limits are essential, particularly in neonates and pregnancy.

---

## Conclusion and Next Steps

**Decision: Hold** for the top-ranked prediction (congenital prothrombin deficiency).
**Decision: Proceed with Guardrails** for perinatal disease, limited to BPD prevention in very-low-birth-weight infants.

**Rationale:**
- Congenital prothrombin deficiency has no trials or literature and no plausible mechanism, so the score is likely a graph artefact. Perinatal disease is supported by repeated Cochrane reviews and large neonatal trials (L1), though the benefit is modest and the evidence applies to a subset of the category.
- Injury (L2) is only indirectly supported, and the remaining predictions are L4–L5 and not actionable.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the marketed products (currently unavailable and a blocking gap for safety screening)
- Detailed mechanism of action data
- For perinatal disease: a precisely defined indication (BPD prevention in very-low-birth-weight infants), dose, route, and toxicity limits, and an assessment of how the injection burden fits the available Indian formulations
- Route compatibility assessment against the marketed forms (oral, injectable, syrup)
- Safety monitoring plan covering hepatic toxicity, bone effects, and interactions with retinoids and tetracyclines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

