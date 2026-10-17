---
layout: default
title: Pheniramine
parent: Moderate Evidence (L3-L4)
nav_order: 662
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Pheniramine: predicted new indication Allergic urticaria (evidence level L4). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Pheniramine"
predicted_indications: ["nasal cavity disease"]
---

# Pheniramine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
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

# Pheniramine: From Allergic Rhinitis and Related Allergic Conditions to Allergic Urticaria

## One-Sentence Summary

Pheniramine is a first-generation H1 antihistamine, originally used for allergic and upper-airway conditions such as allergic rhinitis, vasomotor rhinitis, conjunctivitis, the common cold, urticaria and angioedema.
The TxGNN model predicts it may be effective for **allergic urticaria**, but this is largely an overlap with its existing indications rather than a true new use.
Currently there are **0 clinical trials** and **4 publications** (3 case reports and 1 review of a different drug), so the evidence is mainly a model prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, conjunctivitis (atopic, papillary, vernal), urticaria, angioedema and others (the India licence indication text is empty, so this list comes from the knowledge-graph indication edges) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L4 |
| India Market Status | ✓ Marketed |
| Number of Registrations | 16 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Based on known drug-class information, pheniramine is a first-generation H1-receptor antagonist. By blocking histamine at H1 receptors, it can reduce the wheal-and-flare response, itching and swelling that characterise urticaria.

Urticaria and angioedema are already among pheniramine's listed indications, so allergic urticaria falls largely within the existing scope. This is closer to an on-label use than true repurposing. The very high TxGNN score probably reflects this overlap with known antihistamine indications.

Two other predictions were also made: **nasal cavity disease** (score 99.28%) and **acute laryngopharyngitis** (score 99.25%). Both rest on overlap with existing rhinitis, pharyngitis and common cold indications. They have no supporting trials or literature in the data compiled. Antihistamines have limited proven benefit in infectious pharyngitis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40324831](https://pubmed.ncbi.nlm.nih.gov/40324831/) | 2025 | Case report | Indian J Pharmacol | Loss of consciousness after concurrent intravenous pheniramine and hydrocortisone given for a drug-induced allergic reaction (a safety report) |
| [40125237](https://pubmed.ncbi.nlm.nih.gov/40125237/) | 2025 | Case report | Cureus | Immediate hypersensitivity reaction to pheniramine in a patient with multiple drug hypersensitivity syndrome (a safety report) |
| [16854350](https://pubmed.ncbi.nlm.nih.gov/16854350/) | 2006 | Case report | Allergol Immunopathol | Life-threatening facial oedema after ingesting a pine processionary caterpillar, mimicking an allergic event (not about pheniramine efficacy) |
| [2859711](https://pubmed.ncbi.nlm.nih.gov/2859711/) | 1985 | Review (of a different drug) | Z Hautkr | Review of astemizole trials, with pheniramine mentioned only as a comparator (not direct evidence for pheniramine) |

None of these publications provides direct efficacy evidence for pheniramine in allergic urticaria.

---

## India Market Information

Pheniramine is marketed in India with 16 valid single-ingredient registrations and no cancelled ones. Dosage forms include injections, tablets and syrup. The indication text is empty in the registration records. Five main registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| Registration No. 114 | Avil Injection (Sanofi India Ltd) | Vial of 2 ml injection | Not stated in the records |
| Registration No. 56 | Avil Injection (Sanofi India Ltd) | Vial of 10 ml injection | Not stated in the records |
| Registration No. 5 | Avil 25 Tablet (Sanofi India Ltd) | Strip of 15 tablets | Not stated in the records |
| Registration No. 226 | Avil 50mg Tablet (Sanofi India Ltd) | Strip of 15 tablets | Not stated in the records |
| Registration No. 178677 | Pheril 100mg Syrup (Ciron Drugs & Pharmaceuticals) | Bottle of 100 ml syrup | Not stated in the records |

---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these come from drug-disease relationship data, not from label text, and need confirmation against the package insert):
- Cardiovascular and respiratory: hypertension, chronic obstructive pulmonary disease, bronchitis
- Neurological and psychiatric: epilepsy, insomnia, psychotic and schizophrenia-spectrum disorders, mental disorder
- Gastrointestinal and hepatobiliary: gastric ulcer, peptic ulcer disease, gastritis, inflammatory bowel disease, pancreatitis, liver disease and liver failure, gallbladder disease
- Renal and urological: kidney disease, pyoureter, benign prostatic hyperplasia
- Endocrine and metabolic: diabetes mellitus, diabetic ketoacidosis, hyperglycaemia, hypothyroidism (including myxoedema and congenital hypothyroidism)
- Other: thrombocytopenia, dermatitis herpetiformis

**Safety signals from the literature:**
- Two recent case reports describe serious adverse events with pheniramine: loss of consciousness after intravenous administration together with hydrocortisone, and an immediate hypersensitivity reaction. Both are single-case observations.

Package insert warnings and drug interaction data were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication of allergic urticaria largely overlaps with pheniramine's existing urticaria and angioedema indications, so it is not a distinct repurposing opportunity. The data compiled contain no clinical trials and no literature showing pheniramine efficacy, so the evidence is limited to a model prediction and drug-class reasoning (L4). The other two predictions (nasal cavity disease, acute laryngopharyngitis) have no direct supporting evidence at all (L5).

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indication text for the India registrations, which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Controlled clinical evidence for pheniramine in urticaria (or confirmation that the existing indication already covers it)
- Review of the knowledge-graph contraindications against the label, and of the reported hypersensitivity and intravenous administration safety signals
- Confirmation of whether any new route or formulation would be needed (route compatibility has not yet been assessed)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

