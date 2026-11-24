---
layout: default
title: Chloramphenicol
parent: Model Prediction Only (L5)
nav_order: 170
evidence_level: L5
indication_count: 8
monitor_inn: "Chloramphenicol"
predicted_indications: ["diffuse scleroderma", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-11-24
description: "Chloramphenicol: predicted new indication Diffuse scleroderma (evidence level L5). In India: at least 20 listed products"
---

# Chloramphenicol
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

## Chloramphenicol: Diffuse scleroderma
{: .text-alpha }

## One-Sentence Summary

Chloramphenicol is a broad-spectrum antibacterial that is marketed in India in oral, ophthalmic and other forms.
The TxGNN model predicts it may be relevant to **diffuse scleroderma**, with a score of 0.9965.
There are **no clinical trials** and only **4 basic-research publications** on this disease, none of which tests chloramphenicol, so this is a model prediction without supporting clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 0.9965 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | at least 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology and Microbiology sections of the US FDA-approved prescribing information for chloramphenicol: "Chloramphenicol is a broad-spectrum antibiotic originally isolated from Streptomyces venezuelae. It inhibits bacterial protein synthesis by interfering with the transfer of activated amino acids from soluble RNA to ribosomes." ([DailyMed: chloramphenicol sodium succinate prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=aed29594-211d-49ef-813f-131975a8d0e3), label version 2024-10-10; accessed 2026-11-19.) Chloramphenicol is generally known as an antibacterial that acts on the prokaryotic 50S ribosomal subunit.

The retrieved papers for diffuse scleroderma concern transcriptional regulation of the alpha1(I) procollagen gene, Smad3/Sp1/p300 signalling and TGF-beta in scleroderma fibroblasts. They are preclinical studies of disease mechanisms and do not test chloramphenicol. No established mechanistic connection links a bacterial ribosome inhibitor to fibrotic signalling.

The high score is therefore a computational prediction only. Chloramphenicol's haematological toxicity is also a concern in a chronic autoimmune and fibrotic condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8702443](https://pubmed.ncbi.nlm.nih.gov/8702443/) | 1996 | Basic research | Arthritis and Rheumatism | Transcriptional regulation of the alpha1(I) procollagen gene in dermal fibroblasts from patients with recent-onset diffuse systemic sclerosis; role of intronic sequences |
| [9811061](https://pubmed.ncbi.nlm.nih.gov/9811061/) | 1998 | Basic research | Arthritis and Rheumatism | Promoter elements and transcription factors behind up-regulated alpha1(I) procollagen expression in systemic sclerosis |
| [11229480](https://pubmed.ncbi.nlm.nih.gov/11229480/) | 2001 | Basic research | Arthritis and Rheumatism | Blocking endogenous TGF-beta signalling prevents up-regulated collagen synthesis in scleroderma fibroblasts |
| [16319104](https://pubmed.ncbi.nlm.nih.gov/16319104/) | 2006 | Basic research | Rheumatology (Oxford) | Constitutively phosphorylated Smad3 interacts with Sp1 and p300 in scleroderma fibroblasts |

None of these studies evaluates chloramphenicol.

## India Market Information

At least 20 valid single-ingredient licences are recorded and the list may be partial.

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 3564 | Anchlor-DX Eye Ointment | Tube of 5 gm Eye Ointment | Valid |
| 13543 | Armycetin Capsule | Packet of 100 capsules | Valid |
| 19864 | Actimycetin Suspension | Bottle of 50 ml Suspension | Valid |
| 34365 | Chlorocol H Eye Ointment | Tube of 3 gm Eye Ointment | Valid |
| 35101 | Cortimycin Eye Ointment | Tube of 5 gm Eye Ointment | Valid |
| 35107 | Chlorophenicol 250mg Capsule | Strip of 10 capsules | Valid |
| 36618 | Cortison Optichlor Eye Ointment | Tube of 3 gm Eye Ointment | Valid |
| 38671 | Chlorocap 500mg Capsule | Strip of 10 capsules | Valid |
| 48397 | Curamycin 250mg Tablet | Strip of 10 tablets | Valid |
| 49103 | Colfen 500mg Capsule | Strip of 10 capsules | Valid |
| 56568 | Comyetin 500mg Capsule | Strip of 10 capsules | Valid |
| 104582 | Hytan C Eye Ointment | Tube of 5 gm Eye Ointment | Valid |
| 120346 | Kidopalm 125mg Syrup | Bottle of 50 ml Syrup | Valid |
| 128205 | Larmycetin 250mg Capsule | Strip of 10 capsules | Valid |
| 174906 | Polychlor DM Eye/Ear Drops | Bottle of 5 ml Eye/Ear Drops | Valid |
| 177082 | Paraxin 250mg Dragees | Strip of 10 tablets | Valid |
| 185694 | Retichlor-H Eye Ointment | Tube of 5 gm Eye Ointment | Valid |
| 221165 | Takchlor-C Eye Drop | Packet of 5 ml Eye Drop | Valid |
| 228427 | T-Mycitin 500mg Capsule | Strip of 10 capsules | Valid |
| 235428 | Vanmycetin 0.4% Eye Drop | Packet of 5 ml Eye Drop | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

Only part of the licence list is held in the data; the list may be incomplete.

<!-- licenses:end -->

## Safety Considerations

- **Disease-level cautions:** Chloramphenicol is recorded as contraindicated or to be used with caution in patients with several conditions, including kidney disease, liver disease, thrombocytopenia, anaemia, aplastic anaemia, agranulocytosis, neutropenia, peripheral neuropathy, optic neuritis, acute intermittent porphyria and paroxysmal nocturnal haemoglobinuria. These are not taken from label text, so please confirm against the package insert.
- **Drug Interactions:** 478 interactions are recorded. Major-level interactions include **cisapride** and **naloxegol**. Moderate-level examples include sulfonylureas (glimepiride, glipizide, glyburide, chlorpropamide, acetohexamide), repaglinide, saxagliptin, rosuvastatin, simvastatin, metronidazole, budesonide, aprepitant, eliglustat, iron, balsalazide, naldemedine and nitisinone.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials, the only publications are basic research that does not involve chloramphenicol, and there is no plausible mechanism linking a bacterial ribosome inhibitor to scleroderma fibrosis. The known bone-marrow toxicity adds a safety concern for a chronic condition.

**To proceed, the following is needed:**
- Mechanism-of-action data and a plausible biological rationale for fibrotic disease
- Preclinical studies testing chloramphenicol directly in scleroderma models
- Package insert warnings and contraindications from the local licence holders
- A benefit-risk assessment addressing haematological toxicity in a chronic autoimmune condition

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism-of-action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: chloramphenicol sodium succinate prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=aed29594-211d-49ef-813f-131975a8d0e3) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

