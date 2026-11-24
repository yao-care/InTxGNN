---
layout: default
title: Ephedrine
parent: Moderate Evidence (L3-L4)
nav_order: 312
evidence_level: L4
indication_count: 2
last_modified_at: 2026-11-24
monitor_inn: "Ephedrine"
predicted_indications: ["nasal cavity disease", "trigeminal autonomic cephalalgia"]
description: "Ephedrine: predicted new indication Nasal cavity disease (evidence level L4). In India: 3 listed products (3 not discontinued)"
---

# Ephedrine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

## Ephedrine: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Ephedrine is a sympathomimetic drug originally used for upper-airway and allergic conditions such as allergic rhinitis, vasomotor rhinitis, and the common cold.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but this largely overlaps with its existing indications rather than being a distinct new use.
Evidence is thin: **no registered clinical trials** and **2 low-quality publications** (a 1964 clinical testing report and a 2000 preliminary observation).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L4 |
| India Market Status | Listed in a compiled Indian medicine price dataset (3 of 3) – CDSCO approval status is not included in this data |
| Number of Listed Products | 3 (valid: 3) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ephedrine is a mixed-acting sympathomimetic. It directly stimulates alpha and beta adrenergic receptors and also triggers the release of norepinephrine. This description is based on known pharmacology. According to the Mechanism of Action section of the US FDA-approved prescribing information for ephedrine: "Ephedrine sulfate is a sympathomimetic amine that directly acts as an agonist at α- and β-adrenergic receptors and indirectly causes the release of norepinephrine from sympathetic neurons. Pressor effects by direct alpha- and beta-adrenergic receptor activation are mediated by increases in arterial pressures, cardiac output, and peripheral resistance." ([DailyMed: Emerphed Pfs (ephedrine sulfate) prescribing information, Nexus Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=14601778-93ac-43ec-b66b-5a942317133f), label version 2024-09-16; accessed 2026-11-19.)

Alpha-1 mediated constriction of nasal mucosal blood vessels reduces swelling and congestion, which makes ephedrine biologically plausible for nasal cavity disorders. Because ephedrine is already linked to allergic rhinitis, vasomotor rhinitis, and rhinitis, the prediction is mostly a near-neighbour of existing uses. It is not a genuinely new therapeutic area.

The benefit would be symptomatic relief (decongestion), not disease modification.

### Other Predicted Indications (lower priority)

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Trigeminal autonomic cephalalgia | 0.9934 | L5 | Computational prediction only. Mechanistic rationale is weak, because vasoconstriction does not address the hypothalamic and trigeminovascular pathways. Cardiovascular stimulation may worsen headache. Hold. |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14211229](https://pubmed.ncbi.nlm.nih.gov/14211229/) | 1964 | Clinical testing report | Svenska lakartidningen | Experimental clinical testing of an antihistamine (N-hydroxyethylpromethazine chloride) combined with ephedrine hydrochloride in the nasal cavity. Low quality by modern standards, no abstract available. |
| [11789239](https://pubmed.ncbi.nlm.nih.gov/11789239/) | 2000 | Preliminary clinical observation | Zhongguo Zhong Xi Yi Jie He Za Zhi | Preliminary observation of a rhinitis spray for chronic rhinitis. The formulation is not confirmed to contain ephedrine, so attribution is uncertain. |

---

## India Market Information

<!-- licenses:begin -->

| Dataset ID | Product Name | Pack Size | Status |
|------|------|------|------|
| 4873 | Adrena 2mg Injection | Vial of 2 ml Injection | Valid |
| 72763 | Efipres Injection | Vial of 1 ml Injection | Valid |
| 216752 | Tedral 24mg/130mg Tablet | Strip of 10 tablets | Valid |

Source: Indian Medicine Dataset (junioralive/Indian-Medicine-Dataset on GitHub), a third-party compilation of Indian medicine prices; dataset ID, product name and pack size as recorded in the dataset. CDSCO approval status is not included in this data.

<!-- licenses:end -->

All registrations are valid licenses. Available forms are oral (tablet) and injectable.

<!-- review:begin in-lic-20261106-ephedrine-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All three registrations are valid single-ingredient licenses." Removed: it described the products as single-ingredient or combination products in a way that did not match the Indian medicine data (the Indian Medicine Dataset as of 2026-11-06). Revised 2026-11-24: the hard-coded number of records and the wording about the old table were dropped; the Quick Overview and the product table under India Market Information show the current figures. Source: [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset).

<!-- review:end in-lic-20261106-ephedrine-1 -->

---

## Safety Considerations

**Contraindications suggested by the knowledge graph (not label text):**
The knowledge graph links ephedrine to caution or contraindication in the following groups:
- **Cardiovascular:** hypertension, congestive heart failure
- **Respiratory:** chronic obstructive pulmonary disease
- **Neurological and psychiatric:** epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder, psychotic disorders (including schizophreniform and schizoaffective disorder)
- **Endocrine:** hypothyroidism, myxedema, congenital hypothyroidism
- **Hepatic, renal, and gastrointestinal:** liver failure, liver disease, kidney disease, gallbladder disease, pancreatitis, gastric ulcer, peptic ulcer disease, inflammatory bowel disease
- **Metabolic and haematological:** porphyria (inherited and other porphyrin metabolism disease), thrombocytopenia
- **Other:** open-angle glaucoma, pyoureter

**Drug Interactions:** 197 interactions were identified. Examples of **major** interactions include:
- Tramadol
- Amitriptyline
- Bupropion
- Methylene blue

Examples of moderate interactions include other adrenergic and stimulant drugs (formoterol, salbutamol, arformoterol, methylphenidate, amphetamine, atomoxetine), beta-blockers (atenolol, acebutolol), and antidiabetic drugs (metformin, acarbose, alogliptin, albiglutide).

For warnings and contraindications from the label, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the predicted indication largely overlaps with ephedrine's existing rhinitis uses. The only support is two low-quality or uncertainly attributed publications and no registered trials. The safety profile is broad, with many cardiovascular and psychiatric cautions and many drug interactions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from India's regulatory sources, which currently block safety screening
- Mechanism-of-action data (for example from DrugBank)
- Approved indication text for the three India registrations
- Clarification of whether "nasal cavity disease" adds anything beyond existing rhinitis indications
- Modern controlled studies of ephedrine for nasal congestion, with cardiovascular safety assessment

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against the Indian medicine data used by this site (the Indian Medicine Dataset, a third-party compilation of Indian medicine prices). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient" | Corrected (revised 2026-11-24; earlier version kept in the record) | [Indian Medicine Dataset](https://github.com/junioralive/Indian-Medicine-Dataset) |
| 2026-11-20 | "Detailed mechanism-of-action data was not available in the data compiled for this report, so this description is based on known pharmacology" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt (revised 2026-11-20; earlier version kept in the record) | [DailyMed: Emerphed Pfs (ephedrine sulfate) prescribing information, Nexus Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=14601778-93ac-43ec-b66b-5a942317133f) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

