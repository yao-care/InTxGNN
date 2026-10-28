---
layout: default
title: Flavoxate
parent: Model Prediction Only (L5)
nav_order: 355
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
description: "Flavoxate: predicted new indication Top-ranked: attention deficit hyperactivity disorder, inattentive type (evidence level L5). Approved use: Not stated in the India license data (the drug is used for urinary ur…"
monitor_inn: "Flavoxate"
predicted_indications: ["attention deficit hyperactivity disorder, inattentive type", "irritable bowel syndrome", "specific developmental disorder", "attention deficit-hyperactivity disorder", "cauda equina syndrome", "obsolete neurogenic bladder (disease)", "gastroduodenitis", "peptic ulcer disease"]
---

# Flavoxate
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

## Flavoxate: From Urinary Tract Smooth Muscle Relaxation to attention deficit hyperactivity disorder, inattentive type
{: .text-alpha }

## One-Sentence Summary

Flavoxate is a smooth muscle relaxant with antimuscarinic, phosphodiesterase-inhibiting and calcium-antagonist properties, used on the urinary tract and marketed in India as a 200 mg tablet.
The TxGNN model's top-ranked predictions are ADHD-related terms, but these are biologically implausible. The most plausible candidates are **neurogenic bladder** (the most biologically plausible, though the ontology term is obsolete) and **irritable bowel syndrome** (an indirect class-based link).
Currently there are **0 clinical trials** and **0 publications** supporting any of these predictions, so all rest on model prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the India license data (the drug is used for urinary urgency, frequency and bladder spasm) |
| Predicted New Indication | Top-ranked: attention deficit hyperactivity disorder, inattentive type (implausible). Most plausible: obsolete neurogenic bladder (rank 6) and irritable bowel syndrome (rank 2) |
| TxGNN Prediction Score | 0.9975 (rank 1, ADHD inattentive type); 0.9974 (irritable bowel syndrome); 0.9913 (neurogenic bladder) |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold (neurogenic bladder: Research Question) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, flavoxate relaxes smooth muscle through antimuscarinic, phosphodiesterase-inhibiting and calcium-modulating effects, acting mainly on the urinary tract.

**Neurogenic bladder (most plausible).** Flavoxate relaxes detrusor smooth muscle and is already used for urgency, frequency and bladder spasm. Neurogenic bladder with detrusor overactivity shares these symptoms. The ontology term is flagged obsolete and should be mapped to a current term (for example, neurogenic detrusor overactivity) before further assessment. Urinary retention risk in neurogenic bladder also needs evaluation.

**Irritable bowel syndrome (indirect link).** Antimuscarinic and smooth muscle relaxant activity underlies antispasmodics used in IBS, such as hyoscine and dicyclomine. This is an extrapolation from drug class only. Flavoxate acts mainly on the urinary tract, and no GI evidence was provided.

**Other predictions.**
- **ADHD (inattentive type and general) and specific developmental disorder:** No supported mechanism. Antimuscarinics are generally expected to worsen attention and cognition. These scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
- **Peptic ulcer disease and gastroduodenitis:** Antimuscarinics were historically adjuncts in peptic ulcer disease, but they have been superseded by PPIs and H2 blockers. Flavoxate has no demonstrated gastric antisecretory effect.
- **Cauda equina syndrome:** A neurosurgical emergency treated by decompression. Flavoxate could at most relieve associated bladder symptoms, could delay urgent care, and may worsen urinary retention.

---

## India Market Information

Twenty valid single-ingredient registrations exist, all as oral tablets (strip of 10 tablets). The license data contains no approved indication text. The first five are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 88147 | Flavistrong 200 Tablet | Strip of 10 tablets | Not stated |
| 210103 | Solvoid Tablet | Strip of 10 tablets | Not stated |
| 93896 | Flyvo 200mg Tablet | Strip of 10 tablets | Not stated |
| 231735 | Urific 200mg Tablet | Strip of 10 tablets | Not stated |
| 167505 | Oriflav 200 Tablet | Strip of 10 tablets | Not stated |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (drug-disease contraindication edges, not label text): angle-closure glaucoma, closed-angle glaucoma, pyloric stenosis, paralytic ileus, intestinal obstruction, familial visceral myopathy, active peptic ulcer disease, urinary tract obstruction.
  - Note that active peptic ulcer disease appears here as a contraindication, which conflicts with the peptic ulcer disease repurposing prediction.
- **Drug Interactions:** 74 interactions were identified in total.
  - **Major:** potassium citrate, potassium chloride.
  - **Moderate (examples):** other antimuscarinics and antispasmodics (hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, trospium, scopolamine, propantheline, methscopolamine, mepenzolate); opioids and GI motility-affecting drugs (morphine, loperamide, eluxadoline, metoclopramide, prucalopride, pramlintide); cannabinoids (dronabinol, nabilone).

Please refer to the package insert for label warnings and contraindications, which are not available in the compiled data.

---

## Conclusion and Next Steps

**Decision: Hold** (neurogenic bladder: Research Question)

**Rationale:**
All predictions are supported by model scores only, with no clinical trials or literature, so the evidence level is L5. Neurogenic bladder is biologically plausible and worth a targeted literature review, IBS has only a class-level link, and the ADHD-related predictions are implausible and likely artifacts.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulator (blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Mapping of the obsolete neurogenic bladder term to a current term, then a targeted literature and trial search
- Assessment of urinary retention risk in neurogenic bladder
- Targeted literature search for flavoxate in IBS and other GI spasm
- Approved indication text for the Indian licenses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

