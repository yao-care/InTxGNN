---
layout: default
title: Terazosin
parent: Model Prediction Only (L5)
nav_order: 820
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Terazosin: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Hypertension and benign prostatic hyperplasia"
monitor_inn: "Terazosin"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine disorder", "migraine with brainstem aura", "Raynaud disease", "Ambras type hypertrichosis universalis congenita", "manic bipolar affective disorder", "kyphoscoliotic heart disease"]
---

# Terazosin
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

## Terazosin: From Hypertension and Benign Prostatic Hyperplasia to Hypotrichosis Simplex of the Scalp
{: .text-alpha }

## One-Sentence Summary

Terazosin is an alpha-1 adrenergic blocker, originally used to treat hypertension and benign prostatic hyperplasia.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, but there are **0 clinical trials** and **0 publications** supporting this top-ranked prediction. It is a graph-based prediction only. Among the other predictions, Raynaud disease has the most (still limited) supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and benign prostatic hyperplasia (the approved indication text in the India licence records is blank, so these indications come from the knowledge graph) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, terazosin belongs to the alpha-1 adrenergic blocker class. Its efficacy in hypertension and benign prostatic hyperplasia is established, through relaxation of vascular and prostatic smooth muscle.

For the top-ranked prediction, hypotrichosis simplex of the scalp, no plausible link to alpha-1 blockade has been established. This is a hereditary hair-follicle disorder. The high score most likely reflects proximity to hair-related phenotypes in the knowledge graph rather than a pharmacological rationale. The same holds for the other hair-related predictions (congenital hypotrichosis milia and Ambras-type hypertrichosis). For diffuse alopecia areata, an autoimmune condition, any benefit from scalp vasodilation is speculative.

Other predictions have more biological plausibility:
- **Raynaud disease**: alpha-1 blockade reduces sympathetic vasoconstriction in digital arteries. This is the strongest candidate among the predictions.
- **Migraine**: alpha-1 blockade may modulate cerebrovascular tone and sympathetic activity, but the evidence is old and small.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top-ranked prediction or for any of the other nine predicted indications.

---

## Literature Evidence

Currently no related literature is available for hypotrichosis simplex of the scalp. Publications exist for some lower-ranked predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9273472](https://pubmed.ncbi.nlm.nih.gov/9273472/) | 1997 | Clinical study (small, design to be verified) | Minerva Cardioangiologica | Raynaud disease: terazosin reduced the number, intensity and duration of vasospastic attacks in idiopathic and secondary Raynaud's phenomenon, with improved thermographic and ultrasonographic findings |
| [9074296](https://pubmed.ncbi.nlm.nih.gov/9074296/) | 1997 | Review / case series | Headache | Migraine: 10 patients on terazosin or doxazosin, with reduced frequency or severity in all but one, but 5 stopped because of side effects |
| [7911406](https://pubmed.ncbi.nlm.nih.gov/7911406/) | 1994 | Clinical study (small, open, design unclear) | La Clinica Terapeutica | Migraine without aura: open trial of 46 patients on terazosin (10), buflomedil (29) or both (7) for prophylaxis |
| [34779371](https://pubmed.ncbi.nlm.nih.gov/34779371/) | 2022 | Review | Current Cardiology Reviews | Alopecia: general review of extracardiac effects of cardiovascular drugs. The hair-related content mainly concerns minoxidil, and whether terazosin is discussed needs confirmation |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 106290 | Hypercin 2mg Tablet | Strip of 10 tablets | Not specified in the data |
| 103873 | Hytrin 1 Tablet | Strip of 10 tablets | Not specified in the data |
| 225799 | Teraz 2mg Tablet | Strip of 10 tablets | Not specified in the data |
| 249975 | Zytrin 2mg Tablet | Strip of 10 tablets | Not specified in the data |
| 216904 | Terapress 1 Tablet | Strip of 7 tablets | Not specified in the data |

There are 20 valid single-ingredient registrations in total (no combination products and no cancelled registrations). All are oral tablets. Only the first five are listed above.

---

## Safety Considerations

- **Contraindications / disease associations (knowledge graph, not label text)**: multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, priapism, intraoperative floppy iris syndrome.
- **Drug Interactions**: 137 interactions are recorded. Moderate-level examples include corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), opioids (morphine, opium), bupropion, and cannabinoids (dronabinol, nabilone).
- Known class effects include orthostatic hypotension and syncope. Any use in a new indication, especially in patients with compromised cardiopulmonary function, needs caution.

Please also refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, hypotrichosis simplex of the scalp, rests only on a graph-based score. There are no trials or publications and no plausible mechanism, so the evidence level is L5. The other hair-related predictions are similarly unsupported.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications for the India-marketed products, which are currently missing and block safety screening
- If a more promising direction is pursued, Raynaud disease (L3) and migraine (L4) are the better candidates for a research question. Both would need controlled, modern studies, since the available evidence is small and dated.
- A full-text review of PMID 34779371 to confirm whether terazosin is discussed for alopecia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

