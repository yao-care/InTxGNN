---
layout: default
title: Lactulose
parent: Model Prediction Only (L5)
nav_order: 468
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-30
description: "Lactulose: predicted new indication Acute urate nephropathy (evidence level L5). Approved use: Hepatic encephalopathy, hepatic coma, constipation"
monitor_inn: "Lactulose"
predicted_indications: ["acute urate nephropathy", "nephrolithiasis", "obstructive jaundice", "bile duct disease", "biliary tract disease", "hyperphosphatemia (disease)", "exercise-induced malignant hyperthermia", "bile duct neoplasm"]
---

# Lactulose
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Lactulose: From Hepatic Encephalopathy to Acute Urate Nephropathy
{: .text-alpha }

## One-Sentence Summary

Lactulose is a non-absorbable osmotic disaccharide, originally used to treat hepatic encephalopathy, hepatic coma and constipation.
The TxGNN model's top-ranked prediction is **acute urate nephropathy**, but it has **no clinical trials and no publications** behind it, so it is a model prediction only.
Among the other predicted indications, **obstructive jaundice** has the most support (about 20 publications, mostly small clinical and animal studies, and no registered trials), and it is the most realistic direction to pursue.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hepatic encephalopathy, hepatic coma, constipation (the licence records contain no approved indication text) |
| Predicted New Indication | Acute urate nephropathy (top-ranked); obstructive jaundice has the strongest evidence |
| TxGNN Prediction Score | 0.9989 (acute urate nephropathy) |
| Evidence Level | L5 (acute urate nephropathy); L3 (obstructive jaundice) |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Hold (acute urate nephropathy); obstructive jaundice may be taken forward as a research question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Lactulose is generally known as a non-absorbable osmotic disaccharide that acidifies colonic contents and lowers ammonia. Its efficacy in hepatic encephalopathy and constipation is well established.

**Acute urate nephropathy (rank 1).** No plausible link between lactulose and uric acid-related kidney injury is evident from the data. The very high score (0.9989) reflects model output only. Without any supporting study, it should not be treated as a credible lead.

**Obstructive jaundice (rank 3).** Here the evidence gives a coherent hypothesis. Bile duct obstruction removes bile from the gut, which impairs the intestinal barrier, allows bacterial translocation and causes endotoxaemia. Endotoxaemia contributes to postoperative renal failure and other complications. Lactulose is proposed to reduce gut endotoxin load and support the intestinal barrier. Supporting studies include a prospective clinical study (1986, 24 patients), a rabbit model of endotoxaemia (2003), and several rat studies of bacterial translocation. One study also showed that lactulose inhibits endotoxin-induced TNF production by monocytes in vitro (1990). The evidence is not uniformly positive: a 1997 review notes that a renoprotective effect has not been conclusively shown in clinical studies, and a 1989 rat study found that lactulose did not prevent bile infarction or transaminase elevation.

**Other predictions.** Bile duct disease (rank 4) largely overlaps with the obstructive jaundice evidence. Biliary tract disease (rank 5) and bile duct neoplasm (rank 8) are supported only by indirect or non-lactulose-specific studies. For bile duct neoplasm, any benefit would be supportive (infection prevention), not anti-tumour. The only item for hyperphosphatemia (rank 6) is a review of constipation in chronic kidney disease, which supports the existing constipation indication, not phosphate lowering. Nephrolithiasis (rank 2) and exercise-induced malignant hyperthermia (rank 7) have no supporting data at all.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the predicted indications.

---

## Literature Evidence

The table below covers the most relevant publications for the best-supported prediction, obstructive jaundice. Study types are as classified in the data compiled for this report. Findings are summarised from titles and abstracts only, and full texts were not reviewed.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2032107](https://pubmed.ncbi.nlm.nih.gov/2032107/) | 1991 | Prospective randomised multicentre study | Br J Surg | 102 patients with obstructive jaundice were randomised to preoperative lactulose, sodium deoxycholate or no specific treatment, to prevent postoperative renal dysfunction |
| [3768644](https://pubmed.ncbi.nlm.nih.gov/3768644/) | 1986 | Clinical and experimental study | Br J Surg | In 24 surgical patients, preoperative oral lactulose reduced portal and systemic endotoxaemia versus controls |
| [12957136](https://pubmed.ncbi.nlm.nih.gov/12957136/) | 2003 | Clinical/mechanistic study | J Surg Res | Tested lactulose against bacterial translocation and endotoxaemia in rabbits with bile duct ligation |
| [23297639](https://pubmed.ncbi.nlm.nih.gov/23297639/) | 2012 | Clinical study | Zh Mikrobiol Epidemiol Immunobiol | Bile duct decompression plus lactulose and its effect on intestinal microecology in obstructive jaundice |
| [8944448](https://pubmed.ncbi.nlm.nih.gov/8944448/) | 1996 | Clinical and experimental study | Br J Surg | Intestinal barrier dysfunction in obstructive jaundice, reversed by internal biliary drainage |
| [15782993](https://pubmed.ncbi.nlm.nih.gov/15782993/) | 2005 | Review | Hepato-gastroenterology | Argues for preoperative hydration and lactulose to prevent postoperative renal dysfunction in acute obstructive jaundice |
| [9145459](https://pubmed.ncbi.nlm.nih.gov/9145459/) | 1997 | Review/commentary | Scand J Gastroenterol Suppl | A renoprotective effect of lactulose has not been conclusively shown in clinical studies |
| [12598962](https://pubmed.ncbi.nlm.nih.gov/12598962/) | 2002 | Animal study | Pediatr Surg Int | Melatonin and lactulose effects on liver and kidneys in rats with obstructive jaundice |
| [10576346](https://pubmed.ncbi.nlm.nih.gov/10576346/) | 1999 | Animal study | Hepato-gastroenterology | Sodium deoxycholate, lactulose and glutamine on bacterial translocation in bile duct-ligated rats |
| [2614579](https://pubmed.ncbi.nlm.nih.gov/2614579/) | 1989 | Mechanistic study (rats) | J Pathol | Lactulose, polymyxin B and neomycin did not prevent bile infarction or transaminase elevation after bile duct ligation |

The other predicted indications have little or no lactulose-specific literature. Acute urate nephropathy, nephrolithiasis and exercise-induced malignant hyperthermia have none.

---

## India Market Information

There are 20 valid single-ingredient licences and no cancelled ones. The licence records contain no approved indication text. The five main authorisations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 32785 | Betalose Oral Suspension | 100 ml bottle, oral suspension | Not stated in the records |
| 64929 | Delac 10gm Syrup | 100 ml bottle, syrup | Not stated in the records |
| 122666 | Lactudos Oral Solution | 200 ml bottle, oral solution | Not stated in the records |
| 35781 | Cadilose Oral Solution | 60 ml bottle, oral solution | Not stated in the records |
| 12822 | Arolact Oral Solution | 200 ml bottle, oral solution | Not stated in the records |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (disease-level links, not label text): diabetes mellitus, diabetic ketoacidosis, appendicitis, galactosemia, glycogen storage disease, G6PD deficiency, cystinuria, glucose-galactose malabsorption.
- **Drug Interactions:** 533 interactions are recorded. The listed examples are mostly moderate, such as abiraterone, tramadol, acetazolamide, hydrocortisone, salbutamol, alfuzosin, hydrochlorothiazide, amiloride, amiodarone, amisulpride, anagrelide, propofol, apalutamide, apomorphine, triamcinolone, arsenic trioxide, lumefantrine, asenapine and atomoxetine. Sodium citrate is minor. The full list should be reviewed before any new use is planned.

Please refer to the package insert for warnings and label contraindications, which are not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction, acute urate nephropathy, has no trials, no literature and no plausible mechanism, so it is not actionable.
- Obstructive jaundice (and the overlapping bile duct disease) has a coherent mechanism and small clinical and animal studies. However, there are no registered trials, the clinical benefit is not conclusively shown, and some studies are negative or inconclusive. It is best treated as a research question, not a Go.

**To proceed, the following is needed:**
- Full-text review of the key obstructive jaundice studies, especially the 1991 randomised study (its results and the arms' outcomes were not available in the data compiled for this report)
- A literature search for newer or ongoing trials of lactulose in obstructive jaundice and perioperative renal protection
- Detailed mechanism of action data
- Package insert warnings and contraindications from the Indian licences, which block safety screening
- Review of the interaction profile and knowledge-graph contraindications (notably diabetes and galactosemia) for the target surgical population
- No further work on acute urate nephropathy, nephrolithiasis or exercise-induced malignant hyperthermia unless new supporting evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

