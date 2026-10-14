---
layout: default
title: Protamine Sulfate
parent: Model Prediction Only (L5)
nav_order: 709
evidence_level: L5
indication_count: 10
---

# Protamine Sulfate
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

# Protamine Sulfate: From Heparin Neutralization to Helminthiasis (Animal)

## One-Sentence Summary

Protamine sulfate is a cationic, arginine-rich peptide used to neutralize heparin. The TxGNN model predicts it may be effective for **helminthiasis, animal**, but this is a computational prediction only. There are **0 clinical trials** and **0 publications** supporting this direction, so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Indian license records (the drug is known as a heparin-neutralizing agent) |
| Predicted New Indication | Helminthiasis, animal |
| TxGNN Prediction Score | 50.00% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Protamine sulfate is a cationic, arginine-rich peptide that binds and neutralizes heparin. Its use as a heparin antidote is well known, but no data connect it to anthelmintic activity.

The TxGNN score of 50% is uninformative: it does not distinguish this prediction from a random one. All of the top ten predicted indications share this same score. They are mostly veterinary conditions (classical swine fever, canine hip dysplasia, animal viral hepatitis, exudative epidermitis of swine, enzootic porcine encephalomyelitis, edema disease of swine, infectious bovine rhinotracheitis), plus gingivitis and gingival overgrowth. For the others, the only theoretical links are speculative ones, such as binding of heparan sulfate (a viral attachment factor) or antimicrobial effects of cationic peptides. None has been tested for these diseases.

For helminthiasis, no mechanistic link has been established, and the similarity to the original use has not been assessed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for helminthiasis, animal.

For reference, the only literature found in the top ten predictions relates to the rank 5 prediction, gingivitis. It is indirect and does not support a therapeutic effect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6210390](https://pubmed.ncbi.nlm.nih.gov/6210390/) | 1984 | In vitro study | J Natl Cancer Inst | Protamine sulfate reversibly inhibited serum-induced mitogenic responses in normal and neoplastic cells in vitro. Heparin and heparan sulfate neutralized the effect. |
| [16245632](https://pubmed.ncbi.nlm.nih.gov/16245632/) | 1985 | Animal observational study | Acta Odontol Latinoam | Developed a method to measure heparin in normal dog gingiva. This is not a study of protamine treatment. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 175945 | Prota 10mg Injection | Vial of 5 ml injection | Not stated |
| 152305 | Neutrahep 10mg Injection | Vial of 5 ml injection | Not stated |
| 105303 | Hepadot Injection | Vial of 5 ml injection | Not stated |
| 174388 | Protamine Sulphate 10mg Injection | Vial of 5 ml injection | Not stated |
| 175637 | Prota 50mg Injection | Vial of 5 ml injection | Not stated |

A sixth registration, 154515 (Newtain 50mg Injection), is also valid. All six registrations are single-ingredient injectables.

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction data were available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score of 50%, with no clinical trials, no relevant literature, and no plausible mechanistic link to helminthiasis. The target is a veterinary condition, while the marketed products are human injectables. The approved indications and safety information are also missing.

**To proceed, the following is needed:**
- Package insert warnings, contraindications, and approved indications for the Indian products (a blocking gap for safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- Any experimental (in vitro or in vivo) evidence of anthelmintic activity
- Assessment of route and formulation compatibility for veterinary use
- A re-ranking of predictions, since all top candidates share an uninformative score of 0.5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

