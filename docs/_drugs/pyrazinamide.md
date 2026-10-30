---
layout: default
title: Pyrazinamide
parent: Model Prediction Only (L5)
nav_order: 713
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Pyrazinamide: predicted new indication Infectious otitis media (evidence level L5). Approved use: Pulmonary tuberculosis, meningeal tuberculosis, tuberculous meningitis"
monitor_inn: "Pyrazinamide"
predicted_indications: ["infectious otitis media", "middle ear disease", "otosalpingitis", "chronic otitis media", "suppurative otitis media", "non-suppurative otitis media", "middle ear cholesterol granuloma", "allergic otitis media", "Lyme disease", "infectious otitis interna"]
---

# Pyrazinamide
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

## Pyrazinamide: From Tuberculosis to Infectious Otitis Media
{: .text-alpha }

## One-Sentence Summary

Pyrazinamide is a first-line anti-tuberculosis drug, originally used for pulmonary tuberculosis and tuberculous meningitis.
The TxGNN model predicts it may be effective for **infectious otitis media** with a very high score, but **no clinical trials and no publications** directly support this prediction.
The only supporting literature across the ear-related predictions concerns rare **tuberculous** middle ear infection, which is an extension of the existing TB indication rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis, meningeal tuberculosis, tuberculous meningitis (the approved indication text in the India licence records is empty) |
| Predicted New Indication | Infectious otitis media |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (at least 20) – CDSCO approval status is not included in this data |
| Number of Listed Products | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pyrazinamide is a component of standard multidrug anti-tuberculosis therapy. Its efficacy in tuberculosis is established, and it is active only against *Mycobacterium tuberculosis*, through the acid-dependent activity of its metabolite pyrazinoic acid.

The prediction for infectious otitis media is **not mechanistically convincing**. Pyrazinamide has no recognised activity against the usual otitis media pathogens (*S. pneumoniae*, *H. influenzae*, *M. catarrhalis*). The high score comes from the TxGNN model (deep learning) and most likely reflects similarities the model learned between related diseases, such as tuberculous otitis, not biological evidence or a validated mechanism.

Other ear-related predictions fall into two groups:
- **Tuberculous subsets** (middle ear disease, chronic and suppurative otitis media): pyrazinamide is already part of anti-TB regimens, so this extends the approved TB indication to an extrapulmonary site.
- **Non-infectious or non-mycobacterial conditions** (non-suppurative, allergic, cholesterol granuloma): there is no plausible mechanism. The scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for infectious otitis media or any of the other top-10 predicted indications.

---

## Literature Evidence

No literature was retrieved for infectious otitis media. The table below lists the most relevant publications retrieved for closely related predictions (middle ear disease and chronic otitis media). All are low-tier evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26785789](https://pubmed.ncbi.nlm.nih.gov/26785789/) | 2013 | Case report | Int J Mycobacteriol | Nasal and middle ear tuberculosis in a 55-year-old woman, treated with rifampicin, isoniazid and pyrazinamide for 9 months; no recurrence after one year |
| [15168420](https://pubmed.ncbi.nlm.nih.gov/15168420/) | 2004 | Case report | Am J Kidney Dis | Tuberculous otitis media in a renal transplant recipient after repeated empiric antibiotic courses |
| [41783873](https://pubmed.ncbi.nlm.nih.gov/41783873/) | 2026 | Case report | Cureus | Tuberculous otitis media presenting as otorrhea; delayed diagnosis because of rarity |
| [8011030](https://pubmed.ncbi.nlm.nih.gov/8011030/) | 1994 | Clinical observation | Laryngo-Rhino-Otologie | 12 patients with TB first found in the head and neck area, one with middle ear involvement |
| [21439219](https://pubmed.ncbi.nlm.nih.gov/21439219/) | 2011 | Animal study (mouse) | J Am Assoc Lab Anim Sci | Torticollis in TB-infected mice, including some on pyrazinamide-containing regimens; not a treatment-efficacy study |

---

## India Market Information

Pyrazinamide has 20 valid single-ingredient registrations in India. The approved indication text is not recorded in the licence data. Five main registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 180681 | PYRA 500MG TABLET (Kopran Ltd) | Strip of 10 tablets | Not specified |
| 12536 | Actizid 750mg Tablet (Overseas Healthcare Pvt Ltd) | Strip of 10 tablets | Not specified |
| 83965 | Eurozide 750mg Tablet (Euro Biogenics) | Strip of 10 tablets | Not specified |
| 174379 | P Zide 500 Tablet (Cadila Pharmaceuticals Ltd) | Strip of 10 tablets | Not specified |
| 136891 | Macrozide 1000 Tablet (Macleods Pharmaceuticals Pvt Ltd) | Strip of 6 tablets | Not specified |

All products are oral tablets.

---

## Safety Considerations

- **Disease-level cautions (from knowledge graph contraindication links, not label text)**: liver failure and acute liver failure, hepatitis, liver disease, gallbladder disease, porphyria (including inherited porphyria and porphyrin metabolism disease), gout, diabetes mellitus and diabetic ketoacidosis, peripheral nervous system disease and peripheral neuropathy, substance abuse/dependence, and slow acetylator status.
- **Drug Interactions**: 56 interactions were identified. Those graded Moderate are **picosulfuric acid** and **naltrexone**. Others, with severity not graded, include pantoprazole, omeprazole, lansoprazole, ranitidine, famotidine, mesalazine, sulfasalazine, morphine, vancomycin, streptomycin, amphotericin B, prednisone, prednisolone, metronidazole, aspirin, glyburide, amoxicillin and potassium chloride.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (infectious otitis media) rests on a computational score alone, with no trials, no literature and no plausible mechanism against common otitis media pathogens. The only supporting evidence is a handful of case reports on tuberculous ear infection, which is already covered by standard anti-TB therapy.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-marketed products (currently a blocking gap for safety screening)
- Mechanism of action data
- Narrowing the question to **tuberculous otitis media**, where a systematic review of case series could clarify the role of pyrazinamide, rather than pursuing general infectious otitis media
- Inner ear and middle ear penetration data for pyrazinamide
- For the Lyme disease prediction (rank 9, flagged as a research question): preclinical validation of activity against *B. burgdorferi* persisters before any clinical consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

