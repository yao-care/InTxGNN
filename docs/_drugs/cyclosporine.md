---
layout: default
title: Cyclosporine
parent: Moderate Evidence (L3-L4)
nav_order: 220
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-14
description: "Cyclosporine: predicted new indication Granulomatous disease, chronic, autosomal recessive (evidence level L4). Approved use: Rheumatoid arthritis, dry eye syndrome, xerophthalmia…"
monitor_inn: "Cyclosporine"
predicted_indications: ["granulomatous disease, chronic, autosomal recessive", "brain aneurysm", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "congenital ichthyosiform erythroderma", "fetal erythroblastosis", "brachydactyly-syndactyly syndrome", "prolapse of lacrimal gland"]
---

# Cyclosporine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

## Cyclosporine: From Rheumatoid Arthritis and Dry Eye to Chronic Granulomatous Disease (Autosomal Recessive)
{: .text-alpha }

## One-Sentence Summary

Cyclosporine is a calcineurin-inhibitor immunosuppressant, originally used for rheumatoid arthritis, dry eye syndrome, xerophthalmia and Sjögren syndrome.
The TxGNN model predicts it may be effective for **autosomal recessive chronic granulomatous disease (CGD)**, but the support is thin: **0 clinical trials** and **1 publication** (a stem cell transplantation cohort study) were found.
This is essentially a model-only prediction with, at best, an indirect supportive-care link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis, dry eye syndrome, xerophthalmia, Sjögren syndrome (from knowledge-graph indication data; no approved indication text is available from the India licences) |
| Predicted New Indication | Granulomatous disease, chronic, autosomal recessive |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, cyclosporine is a calcineurin inhibitor that suppresses T-cell activation. It is widely used in transplant immunosuppression and graft-versus-host disease (GVHD) prophylaxis, and its efficacy in immune-mediated conditions such as rheumatoid arthritis and Sjögren syndrome is established.

CGD is an inherited defect of the NADPH oxidase enzyme in phagocytes, causing recurrent infections and granuloma formation. Nothing indicates that calcineurin inhibition corrects this defect. The only publication found concerns stem cell transplantation for CGD, where cyclosporine is plausibly part of the GVHD prophylaxis regimen. The link is therefore an indirect, supportive-care role rather than treatment of the underlying disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22078471](https://pubmed.ncbi.nlm.nih.gov/22078471/) | 2012 | Cohort | J Allergy Clin Immunol | Stem cell transplantation from sibling or unrelated donors in CGD showed excellent survival; matched related donor transplantation is an established treatment, and the study assesses unrelated-donor safety and efficacy. Cyclosporine is not the studied intervention. |

## India Market Information

The approved indication text is not available for these licences. A selection of the 20 valid single-ingredient registrations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 166958 | Oncyclo 50mg Capsule | Strip of 5 capsules | Not stated |
| 39039 | Cyclophil ME Oral Solution | Bottle of 50 ml oral solution | Not stated |
| 237076 | Vaktear Eye Drop | Bottle of 3 ml eye drop | Not stated |
| 202327 | Sandimmun Injection | Ampoule of 1 ml injection | Not stated |
| 41303 | Cyclomune 50mg Tablet | Strip of 10 tablets | Not stated |

Available routes across all registrations: oral, ophthalmic and injectable.

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text)**: hypertension, epilepsy, kidney disease, liver disease, gallbladder disease, infectious disease (including eye infections and conjunctivitis), hyperuricaemia, hypertriglyceridaemia, hyperbilirubinaemia (including Gilbert syndrome), thrombocytopenic purpura, pseudotumor cerebri/intracranial hypertension, and cancers including lymphoma and primary CNS lymphoma. These are especially relevant in CGD, where infection is the central clinical problem.
- **Drug Interactions**: 823 interactions were recorded. Notable examples:
  - Major: loperamide
  - Moderate: rabeprazole, hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone, amphotericin B (including the lipid complex), bupropion, aprepitant, mesalazine, balsalazide, aspirin, metronidazole, chlorpropamide, cholic acid
  - Minor: ranitidine, doxycycline

Package-insert warnings were not available; please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, one transplant-focused cohort study in which cyclosporine is not the studied intervention, and no direct mechanism against CGD. The infection-related contraindication signal is also a concern in this population.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from India (currently a blocking gap for safety screening)
- Mechanism of action data (e.g., from DrugBank)
- Evidence on cyclosporine's role in CGD transplant conditioning and GVHD prophylaxis, to determine whether a supportive-care indication is realistic
- Review of the other predictions, notably **brain aneurysm** (L3), where small, older studies in aneurysmal subarachnoid hemorrhage (vasospasm and neurological deterioration) exist but a mechanistic study suggests T-cell function is dispensable for aneurysm formation. This is better framed as a research question than a repurposing candidate. The remaining predictions (colobomatous microphthalmia-rhizomelic dysplasia syndrome, congenital ichthyosiform erythroderma, fetal erythroblastosis, brachydactyly-syndactyly syndrome, prolapse of lacrimal gland) are model-only (L5), and Hold is also recommended for them.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

