---
layout: default
title: Doxycycline
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
---

# Doxycycline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Doxycycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Doxycycline is a broad-spectrum tetracycline antibiotic, established as a first-line treatment for a wide range of bacterial infections including *Chlamydia trachomatis*, Lyme disease (*Borrelia burgdorferi*), Q fever (*Coxiella burnetii*), Rocky Mountain spotted fever, and sexually transmitted infections (STIs).
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
with **0 clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (Chlamydia, Lyme disease, Q fever, STIs, Rickettsia) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data source. Based on known information, Doxycycline is a tetracycline-class broad-spectrum antibiotic with established efficacy against intracellular pathogens — particularly *Chlamydia trachomatis* — and has been used for decades as the preferred oral treatment for chlamydial infections, trachoma, and related ocular diseases. It also possesses well-documented anti-inflammatory properties, including inhibition of matrix metalloproteinases (MMP-8, MMP-9) and modulation of the NF-κB pathway, which may have additional relevance beyond direct antimicrobial activity.

The mechanistic link to punctate epithelial keratoconjunctivitis is indirect. *Chlamydia trachomatis* is the leading cause of trachoma and infectious follicular conjunctivitis, both of which can result in punctate epithelial keratitis as a post-infection sequela. The sole supporting publication (PMID 1424659, 1992) describes two patients who developed persistent superficial punctate keratitis following chlamydial follicular conjunctivitis, initially treated with oral tetracycline or doxycycline. This case series suggests that the epithelial lesions may persist even after the primary infection resolves, indicating that the keratoconjunctivitis seen here is a post-infectious complication rather than an active infection directly amenable to antibiotic therapy.

The high TxGNN prediction score (99.94%) likely reflects the model's recognition of doxycycline's well-established role in treating the causative organism (*Chlamydia*) rather than direct evidence of efficacy against the keratitis lesion itself. In the absence of clinical trials or direct treatment data for punctate epithelial keratoconjunctivitis as a standalone indication, this prediction is best interpreted as a hypothesis generated from known biological relationships rather than a validated repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case Observation | *Cornea* | Two patients developed persistent bilateral punctate epithelial keratitis following chlamydial follicular conjunctivitis treated with oral tetracycline or doxycycline; lesions persisted after resolution of follicular infection, suggesting a post-infectious epithelial process distinct from the primary infection |

---

## India Market Information

Currently no product licenses registered for Doxycycline in India within this dataset.

---

## Safety Considerations

**Drug Interactions:** A total of **471 drug-drug interactions** have been identified. Key interactions to monitor include:

| Interacting Drug | Severity | Clinical Significance |
|-----------------|----------|-----------------------|
| Isotretinoin | **Major** | Risk of pseudotumor cerebri (benign intracranial hypertension); concurrent use is contraindicated |
| Acitretin | **Major** | Risk of pseudotumor cerebri; concurrent use is contraindicated |
| Aminolevulinic acid (systemic) | **Major** | Additive photosensitization reactions |
| Aluminum hydroxide | Moderate | Divalent/trivalent cations chelate doxycycline, significantly reducing oral absorption |
| Amoxicillin / Ampicillin | Moderate | Potential antagonism between bacteriostatic (doxycycline) and bactericidal (penicillins) antibiotics |
| Aminophylline | Moderate | Doxycycline may alter theophylline metabolism |
| Amobarbital | Moderate | Barbiturates induce hepatic enzymes, reducing doxycycline plasma levels |
| Bedaquiline | Moderate | Additive QT prolongation risk |

> Note: The full interaction list (471 entries) should be consulted via the package insert or clinical decision support tool before co-administration with any drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's high prediction score reflects a biologically plausible but mechanistically indirect link — doxycycline treats the causative pathogen (*Chlamydia trachomatis*) but has no demonstrated direct efficacy against post-infectious punctate epithelial keratoconjunctivitis as an isolated condition. The entire evidence base consists of a single 1992 case observation involving only two patients, with no clinical trials registered globally.

**To proceed, the following is needed:**

- **Mechanistic clarification**: Determine whether the target lesion represents active chlamydial infection (potentially treatable) or a sterile post-infectious epitheliopathy (for which antibiotics are unlikely to be effective)
- **Clinical trial evidence**: At least one prospective pilot study or observational cohort specifically targeting this diagnosis as an endpoint
- **MOA data**: Retrieve full DrugBank record for Doxycycline (DB00254) to characterize anti-inflammatory properties (MMP inhibition, NF-κB modulation) and assess whether these non-antibiotic effects may be relevant to the keratitis lesion
- **India regulatory baseline**: Download and parse package insert (PI) from the regulatory authority to identify approved indications, key warnings, and contraindications before any safety assessment can proceed
- **Comparator assessment**: Review whether topical ophthalmic formulations (not oral doxycycline) could be more appropriate for an ocular surface indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

