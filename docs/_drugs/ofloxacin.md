---
layout: default
title: Ofloxacin
parent: Model Prediction Only (L5)
nav_order: 614
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ofloxacin: predicted new indication Polyclonal hyperviscosity syndrome (evidence level L5). Approved use: Typhoid fever, salmonellosis, paratyphoid fever…"
monitor_inn: "Ofloxacin"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
---

# Ofloxacin
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

# Ofloxacin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Ofloxacin is a fluoroquinolone antibacterial originally used for infections such as typhoid fever, urinary tract infection, bronchitis and bacterial pneumonia.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no relevant publications** support this prediction. It is a model-only signal and appears to be a network-level artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Typhoid fever, salmonellosis, paratyphoid fever, urinary tract infection, bronchitis, bacterial pneumonia and other bacterial infections (the Indian licence records contain no approved indication text) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, ofloxacin is a fluoroquinolone antibacterial that inhibits bacterial DNA gyrase and topoisomerase IV. Its efficacy in bacterial infections is established.

That mechanism does not plausibly extend to polyclonal hyperviscosity syndrome. This condition arises from excess serum immunoglobulins, not from bacterial infection. The very high TxGNN score appears to be a network-level prediction artifact. No clinical or literature data support it.

The other top-ranked predictions show the same pattern: hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant hematological disease, monoclonal gammopathy and congenital hematological disorder. All are model-only predictions with no plausible antibacterial mechanism. For hematological disease with acquired peripheral neuropathy, the fluoroquinolone neuropathy warning argues against use.

Two lower-ranked predictions deserve brief mention:
- **Septicemic plague (rank 8, TxGNN score 99.79%)** is the only prediction with biological plausibility. Ofloxacin is active in vitro against *Yersinia pestis* (PMIDs 8540736, 8913481), and several animal studies show efficacy. This is an extension of its existing anti-infective use, not a novel repurposing. Ciprofloxacin and levofloxacin have stronger established evidence for plague, and the data here do not show ofloxacin to be preferred.
- **Punctate epithelial keratoconjunctivitis (rank 10)** is only indirectly linked, through ophthalmic ofloxacin treating secondary bacterial infection. This is unsupported, because the condition is often viral or allergic.

## Clinical Trial Evidence

Currently no related clinical trials registered for polyclonal hyperviscosity syndrome.

## Literature Evidence

Currently no related literature available for polyclonal hyperviscosity syndrome.

For reference, the only indication with a body of literature is septicemic plague. Its studies are in vitro or animal work, with no human trials:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro | Antimicrob Agents Chemother | Ofloxacin was among the active agents against 78 *Y. pestis* strains; ceftriaxone and ciprofloxacin were most active |
| [8913481](https://pubmed.ncbi.nlm.nih.gov/8913481/) | 1996 | In vitro | Antimicrob Agents Chemother | Ofloxacin and levofloxacin were highly active against 100 human isolates (MIC90 < 0.03 µg/ml) |
| [8203841](https://pubmed.ncbi.nlm.nih.gov/8203841/) | 1994 | Animal | Antimicrob Agents Chemother | Ofloxacin was active in a murine *Y. pestis* infection model alongside other antibiotics |
| [9517950](https://pubmed.ncbi.nlm.nih.gov/9517950/) | 1998 | Animal | Antimicrob Agents Chemother | Mouse model of pneumonic plague comparing streptomycin with other antibiotics |
| [16127904](https://pubmed.ncbi.nlm.nih.gov/16127904/) | 2002 | Animal | Antibiot Khimioter | Ofloxacin (MIC 0.08 mg/L) was effective for prophylaxis and treatment of experimental plague in mice |
| [10987101](https://pubmed.ncbi.nlm.nih.gov/10987101/) | 2000 | Animal | Antibiot Khimioter | Fluoroquinolones including ofloxacin impaired post-vaccine immunity in mice |

## India Market Information

Twenty valid single-ingredient registrations are on record. The licence records contain no approved indication text. Main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 3728 | Aliox 200mg Tablet | Strip of 10 tablets | Not stated |
| 86208 | Flavospas D 200 mg/200 mg Tablet | Strip of 10 tablets | Not stated |
| 171335 | Oflatoz 50mg Oral Suspension | Bottle of 60 ml oral suspension | Not stated |
| 247177 | ZO 100mg Tablet DT | Strip of 10 dispersible tablets | Not stated |
| 87245 | Fixit OF Dry Syrup | Bottle of 30 ml dry syrup | Not stated |

## Safety Considerations

- **Contraindications / Cautions from the knowledge graph (not label text):** Conditions linked to ofloxacin include long QT syndrome, torsades de pointes, epilepsy, liver failure and liver disease, kidney disease and impaired renal function, tendinitis, peripheral neuropathy, myasthenia gravis, rhabdomyolysis, diabetes mellitus and diabetic ketoacidosis, thrombocytopenia, leukopenia, anemia, and *Clostridium difficile* colitis.
- **Drug Interactions:** 383 interactions were recorded. Major-level examples include hydrocortisone, dexamethasone, betamethasone, triamcinolone, bupropion and chlorpropamide. Moderate-level examples include antidiabetic agents (metformin, pioglitazone, acarbose, canagliflozin, alogliptin, albiglutide), famotidine, loperamide, aspirin, and calcium and potassium salts.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for polyclonal hyperviscosity syndrome rests on a model score alone (L5). There are no trials or literature, and no plausible mechanism links a bacterial topoisomerase inhibitor to a condition driven by excess immunoglobulins. The safety profile (neuropathy, QT prolongation, tendon and CNS risks) adds further caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian regulatory source (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A mechanistic rationale and any supporting preclinical or clinical data for polyclonal hyperviscosity syndrome, without which no further investment is justified
- If an anti-infective direction is of interest, a separate, lower-priority evaluation of septicemic plague, compared against ciprofloxacin and levofloxacin, which have stronger evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

