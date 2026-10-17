---
layout: default
title: Chlorpheniramine
parent: Moderate Evidence (L3-L4)
nav_order: 175
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-14
description: "Chlorpheniramine: predicted new indication Allergic urticaria (evidence level L4). Approved use: Allergic rhinitis (other labeled indications include vasomotor rhinit…"
monitor_inn: "Chlorpheniramine"
predicted_indications: ["acute laryngopharyngitis"]
---

# Chlorpheniramine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

# Chlorpheniramine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Chlorpheniramine is a first-generation H1 antihistamine, originally used for allergic rhinitis, the common cold and urticaria.
The TxGNN model predicts it may be effective for **allergic urticaria**, but this is essentially an on-label or closely related use rather than a true repurposing signal.
Currently there are **no registered clinical trials**, and the evidence consists of **20 publications** (mostly reviews and case reports, many about other antihistamines).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (other labeled indications include vasomotor rhinitis, pharyngitis, common cold, conjunctivitis, urticaria and angioedema) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, chlorpheniramine is a first-generation alkylamine H1 antihistamine that has been used since the 1950s. Blocking the H1 receptor is the established way to relieve histamine-mediated wheals, flare and itching.

Urticaria and angioedema are already listed among its original indications. Allergic urticaria is therefore closely related to existing uses, and the high TxGNN score (0.998) is consistent with this known pharmacology. The prediction reflects proximity to known indications more than a new therapeutic direction.

Other predictions from the same model include:
- **Nasal cavity disease** (99.53%): this is a broad category overlapping with labeled rhinitis indications. The supporting literature is entirely preclinical (cat, dog and rat models). One study suggests that nasal decongestion needs combined H1 and H3 blockade, so H1 antagonism alone may not relieve congestion.
- **Acute laryngopharyngitis** (99.50%): plausible only indirectly, through the labeled pharyngitis, nasopharyngitis and common cold indications. No clinical trials or literature were found.
- **Cold urticaria** (99.13%): this has the most direct human evidence of the alternatives (see below). It is rated L3 and framed as a research question.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35652393](https://pubmed.ncbi.nlm.nih.gov/35652393/) | 2024 | Review | Curr Rev Clin Exp Pharmacol | Comprehensive review of chlorpheniramine, covering its use in allergic conditions and other uses such as chronic urticaria, asthma and depression |
| [334082](https://pubmed.ncbi.nlm.nih.gov/334082/) | 1977 | RCT | Arch Dermatol | Double-blind study in 8 patients with primary acquired cold urticaria comparing chlorpheniramine, cyproheptadine and placebo (4 mg three times daily for 7 days); this is direct human evidence for a related condition, but it is small and old |
| [11702618](https://pubmed.ncbi.nlm.nih.gov/11702618/) | 2001 | Review | Am J Clin Dermatol | Evidence-based review of antihistamines in urticaria, which remain the mainstay of treatment |
| [14977391](https://pubmed.ncbi.nlm.nih.gov/14977391/) | 2004 | Review | Drugs | Review of cetirizine in allergic disorders including urticaria (about another drug) |
| [7528133](https://pubmed.ncbi.nlm.nih.gov/7528133/) | 1994 | Review | Drugs | Loratadine was as effective as several antihistamines, including chlorpheniramine, in comparative studies |
| [2873823](https://pubmed.ncbi.nlm.nih.gov/2873823/) | 1986 | Cohort | Asian Pac J Allergy Immunol | Observational study of 142 Thai children with urticaria, describing causes and features |
| [31852144](https://pubmed.ncbi.nlm.nih.gov/31852144/) | 2019 | Case report | Medicine | Two cases of chlorpheniramine-induced anaphylaxis plus a pharmacovigilance database review |
| [26240795](https://pubmed.ncbi.nlm.nih.gov/26240795/) | 2015 | Case report | Asia Pac Allergy | Chlorpheniramine-induced anaphylaxis diagnosed by basophil activation test |
| [21217928](https://pubmed.ncbi.nlm.nih.gov/21217928/) | 2011 | Case report | Allergy Asthma Immunol Res | Chlorpheniramine hypersensitivity with aspirin intolerance (rare) |

## India Market Information

Chlorpheniramine is marketed in India with 20 valid single-ingredient registrations. Approved indication text was not available for these licenses. The main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 12652 | Avokold DS Syrup | Syrup, 60 ml bottle | Not specified |
| Registration No. 185734 | Respicure P Syrup | Syrup, 100 ml bottle | Not specified |
| Registration No. 199561 | Sinarest Paediatric Drops | Oral drops, 15 ml | Not specified |
| Registration No. 245142 | Xosal Cold Syrup | Syrup, 60 ml bottle | Not specified |
| Registration No. 247559 | Zukamin Tablet | Tablet, strip of 10 | Not specified |

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** hypertension, liver failure and liver disease, kidney disease, epilepsy, insomnia, COPD, gastric and peptic ulcer, pancreatitis, gallbladder disease, thrombocytopenia, hypothyroidism, inflammatory bowel disease, psychotic and mental disorders, diabetes mellitus and diabetic ketoacidosis, benign prostatic hyperplasia, bronchitis and hypotensive disorder.
- **Drug interactions:** 348 interactions were recorded. The two **Major** ones are **potassium chloride** and **potassium citrate**. Moderate interactions include anticholinergic agents (atropine, dicyclomine, glycopyrronium, methscopolamine), opioids (morphine, opium), bupropion, metoclopramide, loperamide and dronabinol/nabilone.
- **Literature signals:** rare hypersensitivity reactions, including anaphylaxis, have been reported with chlorpheniramine. Guidelines also favor second-generation antihistamines because of the sedation and anticholinergic burden of first-generation agents.

Please also refer to the package insert, since label warnings and contraindications were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Allergic urticaria is already covered by chlorpheniramine's labeled use, so this is not a genuine repurposing opportunity. There are no clinical trials, and the supporting literature is mostly reviews on other antihistamines. Cold urticaria is the only prediction with direct human data (L3, research question), and that evidence is a small 1977 study.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Indian products (a blocking gap for safety screening)
- Detailed mechanism of action data, for example from DrugBank
- Approved indication text for the Indian licenses
- Modern controlled evidence, if pursued, on whether chlorpheniramine offers any advantage over second-generation antihistamines in cold urticaria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

