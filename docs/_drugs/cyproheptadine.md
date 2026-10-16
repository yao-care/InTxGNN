---
layout: default
title: Cyproheptadine
parent: Model Prediction Only (L5)
nav_order: 221
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Cyproheptadine: predicted new indication Allergic urticaria (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
---

# Cyproheptadine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

# Cyproheptadine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Cyproheptadine is a first-generation antihistamine, originally used for allergic and upper respiratory conditions such as allergic rhinitis, urticaria and the common cold.
The TxGNN model predicts it may be effective for **allergic urticaria**. Support is limited to **9 publications** (mostly historical) and **no registered clinical trials**. The stronger signal in the data compiled for this report is for the related condition **cold urticaria**, which has **16 publications**, including several small double-blind comparative studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, allergic and vernal conjunctivitis, familial dermatographia, urticaria, angioedema (the licence records list no approved indication text) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 (for allergic urticaria); L3 for cold urticaria, the second-ranked prediction |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known pharmacology, cyproheptadine is a first-generation H1 antihistamine with additional serotonin (5-HT2) antagonism and anticholinergic activity. Urticaria is driven largely by histamine release from mast cells, so H1 blockade is a direct mechanistic fit.

Urticaria and angioedema are already among cyproheptadine's original indications. The "allergic urticaria" prediction is therefore close to an existing use rather than true repurposing, and this proximity likely explains the very high model score.

The second-ranked prediction, **cold urticaria**, is also mechanistically plausible, since cold-triggered mast cell degranulation and histamine release respond to H1 blockade. Cyproheptadine's added anti-serotonergic activity may contribute. Modern second-generation antihistamines (including updosing) are now first-line, so cyproheptadine's current role is mainly as a historical or comparator option.

Two other predictions, nasal cavity disease (a broad, non-specific term) and acute laryngopharyngitis, rest on proximity to existing indications. No supporting studies were found for either.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

**Allergic urticaria (top prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7488341](https://pubmed.ncbi.nlm.nih.gov/7488341/) | 1995 | Comparative clinical study | Asian Pac J Allergy Immunol | Double-blind crossover of cyproheptadine vs ketotifen in 6 Thai children with cold urticaria |
| [812662](https://pubmed.ncbi.nlm.nih.gov/812662/) | 1976 | Comparative clinical study | Curr Ther Res | Relative efficacy of cyproheptadine and hydroxyzine for pruritus in allergic dermatoses |
| [1715267](https://pubmed.ncbi.nlm.nih.gov/1715267/) | 1991 | Review (indirect) | Drugs | Review of acrivastine, another H1 antihistamine, in rhinitis and urticaria; not specific to cyproheptadine |
| [1305812](https://pubmed.ncbi.nlm.nih.gov/1305812/) | 1992 | Cohort/diagnostic | Asian Pac J Allergy Immunol | Ice cube test in children with cold urticaria; only 17% remained positive at 3 minutes after 4 weeks of cyproheptadine |
| [13685954](https://pubmed.ncbi.nlm.nih.gov/13685954/) | 1961 | Early clinical study | Br Med J | Early uncontrolled report of cyproheptadine in urticaria |
| [14106555](https://pubmed.ncbi.nlm.nih.gov/14106555/) | 1964 | Clinical evaluation | J Assoc Physicians India | Early evaluation of cyproheptadine in allergic dermatosis |

**Cold urticaria (second prediction)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [334082](https://pubmed.ncbi.nlm.nih.gov/334082/) | 1977 | Double-blind RCT (small) | Arch Dermatol | Cyproheptadine vs chlorpheniramine vs placebo in 8 patients with primary acquired cold urticaria |
| [6480953](https://pubmed.ncbi.nlm.nih.gov/6480953/) | 1984 | Randomized double-blind trial | J Am Acad Dermatol | Cyproheptadine compared with doxepin, hydroxyzine and cinnarizine; doxepin was preferred |
| [2901993](https://pubmed.ncbi.nlm.nih.gov/2901993/) | 1988 | Double-blind crossover | Dermatologica | In 18 patients, cyproheptadine significantly reduced weal area vs placebo; acrivastine was more effective |
| [6102102](https://pubmed.ncbi.nlm.nih.gov/6102102/) | 1980 | Clinical study | J Allergy Clin Immunol | Patients were asymptomatic on cyproheptadine and their ice cube test normalised |
| [1364168](https://pubmed.ncbi.nlm.nih.gov/1364168/) | 1992 | Randomized single-blind crossover | J Investig Allergol Clin Immunol | Loratadine and cetirizine compared with cyproheptadine and ketotifen in 7 patients |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 41285 | Ceron Syrup | 200 ml syrup | Not specified |
| 57658 | Cypnid 4mg Tablet | Strip of 10 tablets | Not specified |
| 105795 | Hysin 1.5 mg/55 mg Drop | 30 ml drop | Not specified |
| 225110 | Triko Cyp Oral Suspension | 200 ml oral suspension | Not specified |
| 57056 | Cyprigen Tablet | Strip of 10 tablets | Not specified |

All 20 registrations are valid single-ingredient products, with none cancelled. Most are syrups.

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not label text): hypertension, peptic ulcer disease, benign prostatic hyperplasia, ocular hypertension, angle-closure glaucoma, hyperthyroidism (including Graves disease and thyrotoxicosis), and bladder neck obstruction. These are consistent with the drug's anticholinergic activity.
- **Drug interactions**: 308 interactions were recorded.
  - **Major**: potassium citrate and potassium chloride.
  - **Moderate** (mostly additive anticholinergic or CNS effects): atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, trospium, propantheline, methscopolamine, mepenzolate, morphine, opium, loperamide, eluxadoline, metoclopramide, dronabinol, nabilone, fenfluramine.
- Sedation and anticholinergic adverse effects are expected with first-generation antihistamines. Package insert warnings and contraindications are not available in the compiled data, so please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Allergic urticaria is essentially an existing indication, and the supporting evidence is mostly historical (1960s to 1990s) with no registered trials or modern RCTs. Cold urticaria has small double-blind comparative studies (L3), but second-generation antihistamines are now first-line, so cyproheptadine adds little as a new option. The other two predictions (nasal cavity disease, acute laryngopharyngitis) rest on model prediction alone.

**To proceed, the following is needed:**
- India package insert warnings and contraindications, which currently block safety screening
- Mechanism-of-action data from DrugBank
- A head-to-head comparison against current second-generation antihistamines, if cold urticaria is pursued
- A defined, specific disease entity in place of "nasal cavity disease"
- Approved indication text for the India registrations, to confirm how far the urticaria use is already labelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

