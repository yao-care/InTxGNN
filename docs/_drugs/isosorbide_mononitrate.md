---
layout: default
title: Isosorbide Mononitrate
parent: Model Prediction Only (L5)
nav_order: 453
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Isosorbide Mononitrate: predicted new indication Hypertrichosis (disease) (evidence level L5). Approved use: Not stated in the available licence data"
---

# Isosorbide Mononitrate
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

# Isosorbide Mononitrate: From Angina-Type Nitrate Therapy to Hypertrichosis (Top Prediction)

> Note: The data compiled for this report do not include the approved indication text for the Indian licenses. The drug's original use is therefore described from general pharmacological knowledge (an organic nitrate vasodilator used in ischaemic heart disease) and not from the licence records.

## One-Sentence Summary

Isosorbide mononitrate is an organic nitrate vasodilator, a nitric oxide (NO) donor that is marketed in India and is generally used for ischaemic heart disease.
The TxGNN model's top-ranked prediction is **hypertrichosis**, but there are **0 clinical trials** and **0 publications** supporting it. This is a model prediction only.
The only prediction with any related literature is **pulmonary arterial hypertension** (rank 10, 2 indirect publications, no trials).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the available licence data |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, isosorbide mononitrate is an NO donor. It raises cGMP in vascular smooth muscle and causes vasodilation.

The link to hypertrichosis is speculative. Vasodilators such as minoxidil are known to cause hypertrichosis, and improved follicular perfusion through NO/cGMP signalling has been discussed in hair biology. No evidence shows that isosorbide mononitrate has this effect. The high score is best read as a model output without clinical support.

The other top-ranked predictions are even less plausible. They are mostly congenital or genetic conditions: Ambras syndrome, hair shaft abnormalities, congenital hypotrichosis, and Dandy-Walker or dental malformation syndromes. Their mechanisms are unrelated to a nitrate vasodilator, and they are likely artefacts of graph proximity. Alopecia and diffuse alopecia areata have only indirect or no mechanistic support. Alopecia areata is autoimmune, and nitrate vasodilation does not address it.

**Pulmonary arterial hypertension (PAH)** is the most biologically plausible candidate (score 99.94%, evidence level L4). PAH involves impaired NO-sGC-cGMP signalling, which parallels approved PDE5 inhibitors and sGC stimulators such as riociguat. However, organic nitrates have not shown benefit in PAH. They may also cause tolerance and ventilation/perfusion mismatch, and there are no PAH-specific trials. This is a research question, not a treatment recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered for hypertrichosis or any other predicted indication.

## Literature Evidence

No literature is available for hypertrichosis. The only literature found relates to the PAH prediction, and both papers are indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16422873](https://pubmed.ncbi.nlm.nih.gov/16422873/) | 2005 | Clinical hemodynamic study | J Sex Med | Hemodynamic effects of sildenafil and isosorbide mononitrate in men with coronary artery disease and erectile dysfunction. The population did not have PAH. |
| [29705351](https://pubmed.ncbi.nlm.nih.gov/29705351/) | 2018 | Preclinical animal study | Life Sci | Stimulation of NO-sensitive soluble guanylate cyclase in monocrotaline-induced pulmonary hypertensive rats. Isosorbide mononitrate was not tested directly. |

## India Market Information

There are 20 valid single-ingredient licences. The approved indication text is not provided in the licence records. Five examples are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 158789 | Natriem 60mg Tablet (Emcure) | Strip of 10 tablets | Not stated |
| 134325 | Monit 20 Tablet (Intas) | Strip of 15 tablets | Not stated |
| 107828 | Ismo Retard Tablet ER (Abbott) | Strip of 7 extended-release tablets | Not stated |
| 136199 | Monotrate SR 60 Tablet (Sun Pharma) | Strip of 10 prolonged-release tablets | Not stated |
| 142358 | Monocontin 50mg Tablet (Modi Mundi Pharma) | Strip of 7 tablets | Not stated |

All products are oral formulations (tablets, sustained-release tablets and capsules).

## Safety Considerations

- **Contraindications (from knowledge graph, not label text)**: The TxGNN knowledge graph links the drug to these conditions: hypotensive disorder, hypertrophic cardiomyopathy, myocardial infarction, coronary thrombosis, hemoglobinopathy, anaemia (including macrocytic anaemia), hyperthyroidism, Graves disease, thyrotoxicosis, and intracerebral haemorrhage.
- **Drug Interactions**: 189 interactions were recorded. Examples classified as Moderate include bupropion, morphine, opium, dronabinol, nabilone, sapropterin, and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), as well as rosiglitazone. Omeprazole is classified as Minor. Several others (for example calcitriol, pantoprazole, glimepiride and metformin) have an unknown severity level.

Package insert warnings were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top predictions (hypertrichosis, alopecia and related hair or congenital disorders) rest on model scores alone. They have no trials, no literature, and no credible mechanism (evidence level L5). PAH is mechanistically plausible but only weakly and indirectly supported (L4), and clinical experience suggests nitrates are not effective there. Repurposing is not supported at present.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from Indian regulatory sources, which are currently a blocking gap
- Mechanism of action data from DrugBank
- Approved indication text for the Indian licences
- For PAH, a focused review of nitrate tolerance and V/Q mismatch, followed by preclinical or small haemodynamic studies before any clinical development
- For hair-related indications, mechanistic or preclinical data showing a follicular effect, and a safety assessment of hypotension given the vasodilator action
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

