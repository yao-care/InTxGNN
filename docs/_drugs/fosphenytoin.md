---
layout: default
title: Fosphenytoin
parent: Model Prediction Only (L5)
nav_order: 382
evidence_level: L5
indication_count: 7
---

# Fosphenytoin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Fosphenytoin: From Epilepsy and Status Epilepticus to Conjunctivitis

## One-Sentence Summary

Fosphenytoin is an injectable prodrug of phenytoin, originally used to treat epilepsy and status epilepticus.
The TxGNN model's top-ranked prediction is **conjunctivitis**, but this rests on a graph-based score alone, with **0 clinical trials** and **0 publications** supporting it.
The only candidate with any published evidence is **manic bipolar affective disorder** (1 publication from 2003), which is a research question rather than an established use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy; status epilepticus |
| Predicted New Indication | Conjunctivitis (top-ranked) |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L5 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

Other predicted indications from the same analysis:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|------|
| 2 | Nephrogenic syndrome of inappropriate antidiuresis | 99.28% | L5 | Hold |
| 3 | Tourette syndrome | 99.22% | L5 | Hold |
| 4 | Manic bipolar affective disorder | 99.18% | L4 | Research Question |
| 5 | Myositis fibrosa | 99.02% | L5 | Hold |
| 6 | Idiopathic granulomatous myositis | 99.02% | L5 | Hold |
| 7 | Fibromyalgia | 99.02% | L5 | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for fosphenytoin is not available in the data compiled for this report. Based on known information, fosphenytoin is a prodrug of phenytoin, a voltage-gated sodium channel blocker used for seizure control. Its efficacy in epilepsy and status epilepticus is established.

For the top-ranked prediction, **conjunctivitis**, no clear mechanistic link was identified. Systemic sodium channel blockade has no established role in infectious or allergic conjunctivitis. The high score is a graph-based prediction only, and should be read with caution.

The most plausible candidate is **manic bipolar affective disorder**. Anticonvulsants with sodium channel activity (carbamazepine, valproate, lamotrigine) are established mood stabilizers, so reducing neuronal hyperexcitability is a reasonable hypothesis for an antimanic effect. However, phenytoin itself has not been established as an effective antimanic agent.

The remaining candidates have weak or no mechanistic support:
- **Nephrogenic syndrome of inappropriate antidiuresis**: caused by gain-of-function variants in the vasopressin V2 receptor. Phenytoin's inhibition of ADH release would not act on a constitutively active receptor.
- **Tourette syndrome**: sodium channel blockade could theoretically reduce hyperexcitability, but current standards of care act through different mechanisms, and an intravenous-only prodrug is impractical for a chronic condition.
- **Myositis fibrosa and idiopathic granulomatous myositis**: no known role for sodium channel blockade in fibrosis or immune-mediated inflammation. Phenytoin-related hypersensitivity reactions and connective tissue effects argue against benefit.
- **Fibromyalgia**: related anticonvulsants (pregabalin, gabapentin) act on calcium channel subunits, not sodium channels. Parenteral dosing and a large interaction burden make chronic use unfavorable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction (conjunctivitis) or any of the other predicted indications.

---

## Literature Evidence

No literature is available for conjunctivitis. The only publication identified across the predicted indications relates to manic bipolar affective disorder:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12716241](https://pubmed.ncbi.nlm.nih.gov/12716241/) | 2003 | Unclassified (likely small exploratory clinical study) | The Journal of Clinical Psychiatry | Tested whether intravenous high-dose fosphenytoin, a phenytoin prodrug with few cardiac or local vein side effects, has acute antimanic effects. Design and size are not confirmed. |

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 86034 | Fosolin 750mg Injection (Zydus Cadila) | Vial of 10 ml injection | Not specified |
| 87299 | Fosphen 75mg Injection (Intas Pharmaceuticals Ltd) | Vial of 10 ml injection | Not specified |
| 85048 | Fosphen 150mg Injection (Intas Pharmaceuticals Ltd) | Vial of 2 ml injection | Not specified |
| 88578 | Fosentin 75mg Injection (Sun Pharmaceutical Industries Ltd) | Vial of 2 ml injection | Not specified |
| 84397 | Fosolin 75mg Injection (Zydus Cadila) | Vial of 2 ml injection | Not specified |

Ten valid single-ingredient registrations are on record; the five above are shown. All products are injectables.

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: Conditions flagged for fosphenytoin include:
  - Cardiac: long QT syndrome (including familial), torsades de pointes, sudden cardiac arrest, heart conduction disease, atrioventricular block, Adams-Stokes syndrome, hypotensive disorder.
  - Haematological: thrombocytopenia, leukopenia, pancytopenia, agranulocytosis, neutropenia (including congenital forms).
  - Organ disease: kidney disease, liver disease, gallbladder disease.
  - Other: systemic lupus erythematosus, substance abuse/dependence, hyperphosphatemia.
- **Drug Interactions**: 306 interactions are recorded. Examples from the retrieved list:
  - **Major**: cimetidine, eliglustat.
  - **Moderate**: acarbose, famotidine, ranitidine, doxycycline, hydrocortisone, clarithromycin, aprepitant, calcitriol, and others.
  - **Minor**: acetylsalicylic acid.

Please also refer to the package insert for label warnings and contraindications, which were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (conjunctivitis) has no clinical trials, no literature, and no plausible mechanism, so it is supported by model output alone (L5). The only signal of interest is in manic bipolar affective disorder, where a single 2003 study of uncertain design exists. That is best treated as a research question rather than a repurposing candidate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the India regulatory source (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Full-text review of PMID 12716241 to confirm study design, size and outcomes
- Preclinical or clinical evidence for any candidate indication, with route-compatibility assessment (all marketed products are injectables)
- A cardiovascular and haematological safety plan, given the infusion-related cardiac risks and the number of flagged interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

