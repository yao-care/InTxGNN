---
layout: default
title: Nitrofurantoin
parent: Model Prediction Only (L5)
nav_order: 602
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Nitrofurantoin: predicted new indication Rheumatoid arthritis (evidence level L5). Approved use: Not stated in the Indian licence records (antibacterial use in urinar…"
monitor_inn: "Nitrofurantoin"
predicted_indications: ["rheumatoid arthritis", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy", "brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "sclerosing cholangitis", "methemoglobinemia, alpha type", "gout", "methemoglobinemia"]
---

# Nitrofurantoin
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

## Nitrofurantoin: From Urinary Tract Infection to Rheumatoid Arthritis
{: .text-alpha }

## One-Sentence Summary

Nitrofurantoin is an antibacterial agent marketed in India as an oral urinary-tract product, and the data compiled for this report do not include a formal approved-indication text.
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but there are **0 clinical trials** and the retrieved publications describe **harm rather than benefit**.
This prediction is best viewed as a network-proximity artifact, not a credible repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Indian licence records (antibacterial use in urinary tract infection is described in the retrieved literature) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Nitrofurantoin is an antibacterial agent used for urinary tract infections, but no credible therapeutic mechanism links it to rheumatoid arthritis (RA).

The very high TxGNN score (0.9989) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The retrieved literature points the other way: nitrofurantoin is a recognised cause of pulmonary toxicity and fibrosis, and a case report describes a methotrexate–nitrofurantoin interaction causing irreversible pulmonary fibrosis in a patient with RA. A self-controlled case series examined antibiotic exposure and RA flares. None of this supports efficacy.

Other predictions for this drug show the same pattern. Several are rare genetic syndromes with no plausible link. Others (methemoglobinemia, sclerosing cholangitis) reflect known adverse effects of nitrofurantoin, not therapeutic opportunities.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort (self-controlled case series) | Scientific Reports | Studied the association between antibiotic exposure and RA flares in a UK cohort of 31,992 newly diagnosed RA patients; this is a safety/association question, not evidence of benefit |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | A 94-year-old woman with RA on methotrexate developed irreversible pulmonary fibrosis after nitrofurantoin treatment |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Lists nitrofurantoin among drugs causing pulmonary fibrosis; RA is noted as a predisposing systemic disease |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du Praticien | Reviews drug-induced interstitial lung disease, including nitrofurantoin |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | Poor prognosis in RA patients hospitalised for interstitial lung fibrosis; not related to nitrofurantoin efficacy |

None of these publications reports a therapeutic benefit of nitrofurantoin in RA.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 231227 | Utab 100mg Tablet SR | Sustained-release tablet (strip of 10) | Not specified |
| 230421 | Urosafe 100mg Tablet | Tablet (strip of 10) | Not specified |
| 134606 | Martifur MR 50mg Tablet | Modified-release tablet (strip of 10) | Not specified |
| 150745 | Nifutin Tablet SR | Sustained-release tablet (strip of 10) | Not specified |
| 151351 | Nitro 100mg Capsule | Capsule (strip of 10) | Not specified |

There are 20 valid single-ingredient registrations in total; the table lists 5.

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: diabetes mellitus, diabetic ketoacidosis, anuria, impaired renal function, peripheral neuropathy, interstitial lung disease, pulmonary fibrosis, G6PD deficiency, drug-induced liver injury, hepatitis, obstructive jaundice, biliary tract disease, vitamin B12 deficiency, optic neuritis, *Clostridium difficile* colitis, and others.
- **Drug Interactions**: 172 interactions were identified. Moderate-level ones include balsalazide, metronidazole, picosulfuric acid, naltrexone, rosuvastatin and simvastatin. Minor ones include anticholinergics (atropine, hyoscyamine, dicyclomine, glycopyrronium, scopolamine) and magnesium-containing antacids.
- **Relevant to RA patients**: the literature documents a serious pulmonary interaction with methotrexate, a common RA drug.
- **Other adverse associations in the retrieved literature**: methemoglobinemia and haemolysis (especially in G6PD deficiency), and drug-induced liver injury, including autoimmune-like hepatitis.

Package insert warnings were not available; please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The RA prediction has no clinical trials and no supportive literature, and the available evidence shows nitrofurantoin as a source of harm (pulmonary fibrosis, methotrexate interaction) in RA patients. The high TxGNN score is not backed by any plausible mechanism.

**To proceed, the following is needed:**
- Detailed mechanism of action data and a credible mechanistic hypothesis for RA
- Package insert warnings and contraindications for the Indian products
- Preclinical evidence of anti-inflammatory or immunomodulatory activity relevant to RA
- A risk assessment addressing pulmonary, hepatic and haematological toxicity, and co-prescription with methotrexate
- Review of the other nine predictions, none of which currently shows a therapeutic signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

