---
layout: default
title: Itopride
parent: Model Prediction Only (L5)
nav_order: 456
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-30
monitor_inn: "Itopride"
predicted_indications: ["small bowel Crohn disease", "venous insufficiency (disease)", "achlorhydria", "hiatus hernia (disease)"]
description: "Itopride: predicted new indication Small bowel Crohn disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Itopride
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

## Itopride: Small bowel Crohn disease
{: .text-alpha }

## One-Sentence Summary

Itopride is a gastrointestinal prokinetic originally used to treat gastritis and related upper-GI motility symptoms.
The TxGNN model predicts it may be effective for **small bowel Crohn disease**, but this is a computational prediction only, with **no clinical trials** and **no publications** currently supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Small bowel Crohn disease |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Itopride is a dopamine D2 antagonist and acetylcholinesterase inhibitor. Together these actions enhance upper GI motility and gastric emptying. The data compiled for this report did not include a detailed, curated mechanism-of-action record, so this description rests on the mechanistic assessment prepared for the prediction.

The link between the original indication and the predicted one is weak. Gastritis and functional dyspepsia are treated with a motility-enhancing drug, whereas Crohn disease is a chronic inflammatory condition driven by immune pathways. Itopride has no known anti-inflammatory action, so no clear mechanistic bridge exists.

There is also a practical concern. Prokinetics may be unsuitable where strictures or obstruction are present, which is a recognised complication of small bowel Crohn disease.

Other predictions in the top 10 were also reviewed. A few are more plausible given itopride's prokinetic action, though still unproven:
- The one retrieved paper studies a different drug (mosapride) in rats.
- **Pylorospasm, hiatus hernia, achlorhydria**: plausible symptom-level rationales, but no evidence (L5).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for small bowel Crohn disease. The only publications retrieved relate to lower-ranked predictions and provide indirect evidence only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16821670](https://pubmed.ncbi.nlm.nih.gov/16821670/) | 2005 | Clinical study (design not confirmed) | Journal of the Indian Medical Association | ENGIP-II: itopride in non-ulcer dyspepsia; significant reductions in upper abdominal pain, heartburn frequency and related symptoms (relevant to esophageal ulcer prediction, indirect) |
| [21180236](https://pubmed.ncbi.nlm.nih.gov/21180236/) | 2010 | Review | Romanian Journal of Internal Medicine | Pragmatic approach to functional dyspepsia (relevant to esophageal ulcer prediction, indirect) |
| [21521930](https://pubmed.ncbi.nlm.nih.gov/21521930/) | 2011 | Preclinical (animal; different drug) | Journal of Pharmacological Sciences | Mosapride, a 5-HT4 agonist, on gastric distension-induced visceromotor response in rats (relevant to gastric dilatation prediction, class-level only) |

## India Market Information

Itopride has 20 valid single-ingredient registrations in India. Approved indication text was not available for these products. Five of them are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 96099 | Gitune 50mg Tablet (Intas) | Strip of 10 tablets | Not available |
| Registration No. 60573 | Discom 50mg Tablet (Hetero Drugs) | Strip of 10 tablets | Not available |
| Registration No. 108727 | Itcan 150mg Capsule SR (Hetero Healthcare) | Strip of 10 SR capsules | Not available |
| Registration No. 94181 | Ganaton Tablet (Abbott) | Strip of 10 tablets | Not available |
| Registration No. 141563 | Motiza 150mg Tablet SR (J B Chemicals) | Strip of 10 SR tablets | Not available |

## Safety Considerations

Please refer to the package insert for safety information.

No drug-interaction records were found in the data compiled for this report, and no knowledge-graph contraindications were identified.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Crohn disease prediction has no clinical or literature support and no plausible mechanistic link, and the high score appears to be a computational artifact. Itopride is widely marketed in India for its existing prokinetic use, but that offers no support for this new indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulatory source (a blocking gap for safety screening)
- Detailed mechanism-of-action data from DrugBank
- Any preclinical or clinical evidence linking itopride to intestinal inflammation (none currently exists)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

