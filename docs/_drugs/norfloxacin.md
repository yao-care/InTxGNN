---
layout: default
title: Norfloxacin
parent: Model Prediction Only (L5)
nav_order: 608
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Norfloxacin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Typhoid fever, salmonellosis, paratyphoid fever…"
monitor_inn: "Norfloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "punctate epithelial keratoconjunctivitis", "premalignant hematological system disease", "diffuse scleroderma", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
---

# Norfloxacin
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

## Norfloxacin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome
{: .text-alpha }

## One-Sentence Summary

Norfloxacin is a fluoroquinolone antibiotic, originally used to treat urinary tract infections, typhoid and paratyphoid fever, dysentery and diarrhoeal disease, and other bacterial infections.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but this is a model-only prediction with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Typhoid fever, salmonellosis, paratyphoid fever, urinary tract infection, bronchitis and other bacterial infections (from the knowledge graph; no approved indication text is available for the Indian licences) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general knowledge, norfloxacin is a fluoroquinolone antibacterial that inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy is established in urinary tract and gastrointestinal bacterial infections.

Polyclonal hyperviscosity syndrome results from elevated immunoglobulin levels that raise blood viscosity. This is not an antibacterial target, and no plausible mechanistic link to norfloxacin was identified. The high TxGNN score (99.70%) reflects a graph-based association only, with no supporting clinical or literature data.

Other top-ranked predictions are similarly weak. For example, hyperamylasemia, congenital analbuminemia, blood group incompatibility, diffuse scleroderma and monoclonal gammopathy have no mechanistic rationale. The only biologically plausible candidate among the top 10 is **septicemic plague** (Yersinia pestis is within the fluoroquinolone spectrum). However, support is limited to preclinical studies. Norfloxacin's limited systemic exposure, mainly in urine and the gut, is also a drawback for bloodstream infections, and other fluoroquinolones are better candidates.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature is available for polyclonal hyperviscosity syndrome.

For reference, the literature found for other top-ranked predictions is indirect only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Preclinical | Antibiotiki i Khimioterapiia | Mouse study of combined fluoroquinolone and vaccine prevention of plague. Norfloxacin's effect on post-vaccine immunity was lower than that of ciprofloxacin, ofloxacin and pefloxacin (septicemic plague) |
| [11057367](https://pubmed.ncbi.nlm.nih.gov/11057367/) | 2000 | In vitro | Antibiotiki i Khimioterapiia | Experimental resistance of Vibrio cholerae to nalidixic acid and fluoroquinolones; not about plague |
| [8834911](https://pubmed.ncbi.nlm.nih.gov/8834911/) | 1996 | Cohort | Antimicrob Agents Chemother | Fluoroquinolone-resistant E. coli emerged in 40% of haematological cancer patients on norfloxacin prophylaxis (monoclonal gammopathy; tangential) |
| [22959880](https://pubmed.ncbi.nlm.nih.gov/22959880/) | 2012 | Case series | Am J Ophthalmol | Repeated corneal swabbing for microsporidial keratoconjunctivitis (punctate epithelial keratoconjunctivitis; no norfloxacin efficacy shown) |
| [12867402](https://pubmed.ncbi.nlm.nih.gov/12867402/) | 2003 | Case series | Ophthalmology | Six cases of microsporidial keratoconjunctivitis in healthy individuals (no norfloxacin efficacy shown) |

## India Market Information

Twenty valid single-ingredient registrations are listed; five main ones are shown below. No approved indication text is available for these licences.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 153214 | Norspan 400mg Tablet | Strip of 10 tablets | Not available |
| 172439 | Osoflox 400mg Tablet | Strip of 10 tablets | Not available |
| 222889 | Tamflox 400mg Tablet | Strip of 10 tablets | Not available |
| 157488 | Norflin 400mg Tablet | Strip of 10 tablets | Not available |
| 222295 | Tinimix 100mg/100mg Syrup | Bottle of 30 ml syrup | Not available |

Many other registrations are norfloxacin plus tinidazole tablets (400 mg/600 mg).

## Safety Considerations

- **Contraindications and disease associations (from the knowledge graph, not label text):** long QT syndrome, torsades de pointes, epilepsy, liver failure and liver disease, kidney disease, thrombocytopenia, tendinitis, peripheral neuropathy, rhabdomyolysis, diabetes mellitus and diabetic ketoacidosis, potassium deficiency, psychotic and other mental disorders, and anaemia.
- **Drug Interactions:** 299 interactions recorded. Examples classed as **Major**: hydrocortisone, dexamethasone, betamethasone, triamcinolone (corticosteroids, notably with tendon risk), bupropion and chlorpropamide. **Moderate** examples include metformin, pioglitazone, acarbose, famotidine, loperamide, acetylsalicylic acid, and calcium and potassium salts.

Please refer to the package insert for label warnings.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for polyclonal hyperviscosity syndrome rests on the model score alone (L5), with no trials, no publications and no plausible mechanism. Norfloxacin's known safety concerns (tendon, nerve, QT and CNS effects) offer no offsetting benefit here.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking norfloxacin to hyperviscosity or immunoglobulin biology
- Mechanism of action data and package insert warnings and contraindications for the Indian products
- If an anti-infective repositioning is sought, reprioritise toward bacterial indications such as septicemic plague, comparing norfloxacin against better-absorbed fluoroquinolones
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

