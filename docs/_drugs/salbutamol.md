---
layout: default
title: Salbutamol
parent: Model Prediction Only (L5)
nav_order: 761
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Salbutamol: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Asthma, bronchial disease"
monitor_inn: "Salbutamol"
predicted_indications: ["papillary conjunctivitis", "nasal cavity disease", "pharyngitis", "bronchitis", "acute laryngopharyngitis", "anaphylaxis", "common cold", "atopic conjunctivitis", "anorectal stricture"]
---

# Salbutamol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Salbutamol: From Asthma to Papillary Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Salbutamol is a short-acting beta-2 agonist bronchodilator, originally used to treat asthma and bronchial disease.
The TxGNN model's top-ranked prediction is **papillary conjunctivitis**, but **no clinical trials and no publications** currently support it (evidence level L5, prediction only).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, bronchial disease (the India license records contain no approved indication text) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| India Market Status | Marketed (valid licences on record: at least 20) |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, salbutamol is a beta-2 adrenergic agonist. Its efficacy in asthma and bronchial disease is established, and it relaxes airway smooth muscle.

For papillary conjunctivitis, the only support is indirect. Beta-2 agonists show some anti-inflammatory and mast-cell stabilizing effects in the conjunctiva in preclinical models. No direct evidence exists for this condition.

The other predictions vary in plausibility:
- **Obstructive lung disease** is a natural extension of the bronchodilator mechanism. It is largely on-label or label-adjacent rather than true repurposing.
- **Atopic conjunctivitis** has preclinical support: topical salbutamol suppressed immediate allergic conjunctivitis in guinea pigs (PMID 3666475), and beta-2 agonists showed topical anti-inflammatory activity in the conjunctiva (PMID 2906082).
- **Anaphylaxis** has a plausible rationale through bronchial relaxation and inhibition of mast-cell mediator release. Salbutamol is already used for anaphylactic bronchospasm, but it is not a substitute for epinephrine.
- **Bronchitis** evidence concerns mainly infant bronchiolitis, where meta-analyses show little or no clinically meaningful benefit from bronchodilators.
- **Pharyngitis, nasal cavity disease, acute laryngopharyngitis and anorectal stricture** have no plausible mechanism and no supporting studies.

---

## Clinical Trial Evidence

For the top-ranked prediction (papillary conjunctivitis), there are currently no related clinical trials registered.

The trials below come from the lower-ranked predictions with the most evidence.


| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02177253](https://clinicaltrials.gov/study/NCT02177253) | Phase 3 | Completed | 1118 | 12-week ipratropium/salbutamol (Respimat) vs Combivent vs ipratropium vs placebo in COPD; tests a combination, so salbutamol alone is not isolated |
| [NCT05987371](https://clinicaltrials.gov/study/NCT05987371) | Phase 2 | Completed | 75 | Placebo-controlled dose-exploration trial of an inhaled suspension (TQC3721) in moderate to severe COPD; relevance to salbutamol is unclear |
| [NCT02686086](https://clinicaltrials.gov/study/NCT02686086) | N/A | Completed | 60 | Lung volume and symptom scores after bronchodilator via vibrating mesh vs jet nebuliser in COPD |
| [NCT01721291](https://clinicaltrials.gov/study/NCT01721291) | Phase 4 | Completed | 64 | Inhaler treatment and small-airway assessment in COPD |
| [NCT01521572](https://clinicaltrials.gov/study/NCT01521572) | N/A | Unknown | 200 | Bronchodilator response to salbutamol on respiratory mechanics in healthy people, smokers and COPD |

**Anaphylaxis (rank 6)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05653024](https://clinicaltrials.gov/study/NCT05653024) | Phase 3 | Terminated | 24 | Double-blind inhaled salbutamol vs placebo for abdominal pain in food-induced IgE-mediated reactions; terminated early, so efficacy cannot be established |

**Bronchitis / bronchiolitis (rank 4)**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | N/A | Unknown | 600 | Epinephrine vs albuterol in bronchiolitis |
| [NCT00696540](https://clinicaltrials.gov/study/NCT00696540) | Phase 2 | Unknown | 74 | Hypertonic vs normal saline as diluent of salbutamol nebulisation in bronchiolitis |
| [NCT06665711](https://clinicaltrials.gov/study/NCT06665711) | N/A | Not yet recruiting | 100 | 3% hypertonic saline vs salbutamol in children with bronchiolitis |
| [NCT05932316](https://clinicaltrials.gov/study/NCT05932316) | N/A | Unknown | 96 | Bronchodilator response in bronchiectasis |

---

## Literature Evidence

For the top-ranked prediction (papillary conjunctivitis), there is currently no related literature available.

The most relevant publications for the other predicted indications are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24937099](https://pubmed.ncbi.nlm.nih.gov/24937099/) | 2014 | Meta-analysis | Cochrane Database Syst Rev | Bronchodilators for bronchiolitis in infants |
| [33893229](https://pubmed.ncbi.nlm.nih.gov/33893229/) | 2021 | Meta-analysis | Pediatrics | Network meta-analysis of bronchiolitis interventions in acute care |
| [36765418](https://pubmed.ncbi.nlm.nih.gov/36765418/) | 2023 | Guideline | Ital J Pediatr | Italian bronchiolitis guidelines; management is largely supportive |
| [35383741](https://pubmed.ncbi.nlm.nih.gov/35383741/) | 2022 | RCT | Mymensingh Med J | Nebulized 3% hypertonic saline vs normal saline and salbutamol in acute bronchiolitis |
| [26859020](https://pubmed.ncbi.nlm.nih.gov/26859020/) | 2014 | RCT | East Afr Med J | Honey vs salbutamol vs placebo for cough in children with common cold; abstract not available, so findings cannot be verified |
| [1729064](https://pubmed.ncbi.nlm.nih.gov/1729064/) | 1992 | RCT (crossover) | Chest | Theophylline and salbutamol improved pulmonary function in irreversible COPD (n=12) |
| [34366098](https://pubmed.ncbi.nlm.nih.gov/34366098/) | 2021 | Review | J Allergy Clin Immunol Pract | Salbutamol use for gastrointestinal anaphylaxis |
| [3666475](https://pubmed.ncbi.nlm.nih.gov/3666475/) | 1987 | Preclinical | Graefes Arch Clin Exp Ophthalmol | Topical salbutamol strongly suppressed immediate allergic conjunctivitis in guinea pigs |
| [2906082](https://pubmed.ncbi.nlm.nih.gov/2906082/) | 1985 | Preclinical | J Ocul Pharmacol | Topical anti-inflammatory activity of beta-2 agonists in the conjunctiva |
| [115530](https://pubmed.ncbi.nlm.nih.gov/115530/) | 1979 | Preclinical | Br J Pharmacol | Anti-anaphylactic activity of salbutamol vs disodium cromoglycate |

---

## India Market Information

Salbutamol has 20 valid single-ingredient registrations. The records contain no approved indication text. Five main authorizations are shown.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 26 | Asthalin 100mcg Inhaler (Cipla Ltd) | Packet of 200 MDI inhaler | Not recorded |
| 237 | Asthalin Respirator Solution (Cipla Ltd) | Bottle of 15 ml solution for inhalation | Not recorded |
| 7563 | Aerotide Forte 400mcg/200mcg Diskette (Sun Pharmaceutical Industries Ltd) | Packet of 8 inhaler | Not recorded |
| 237125 | Vent ET 2mg/100mg Tablet (Merck Ltd) | Strip of 10 tablets | Not recorded |
| 26954 | Bromosal Syrup (Smilax Pharmaceuticals) | Bottle of 100 ml syrup | Not recorded |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** hypertension, long QT syndrome, epilepsy, potassium deficiency, diabetes mellitus and diabetic ketoacidosis, metabolic acidosis, benign prostatic hyperplasia, bladder neck obstruction, ocular hypertension and angle-closure glaucoma, hyperthyroidism and thyrotoxicosis, sudden cardiac arrest, heart conduction disease, myocardial ischemia and coronary artery disease.
- **Drug Interactions:** 754 interactions were recorded. Examples include moderate interactions with epinephrine, clarithromycin, cisapride, and antidiabetic drugs (acarbose, alogliptin, canagliflozin, dapagliflozin, chlorpropamide, acetohexamide, albiglutide). Minor interactions include corticosteroids (hydrocortisone, dexamethasone, budesonide, beclomethasone, betamethasone).
- **Hypersensitivity:** a case report of anaphylaxis to salbutamol itself exists (PMID 18447148).

Please also refer to the package insert for full warnings and contraindications, as label-based safety data were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, papillary conjunctivitis, rests on model score alone, with no trials or publications. The better-supported indication (obstructive lung disease, L1) is essentially an existing use rather than new repurposing. Anaphylaxis (L2) rests on one terminated, underpowered Phase 3 trial. Bronchitis/bronchiolitis evidence is largely negative to equivocal.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the India-marketed products (a blocking gap for safety screening)
- Detailed mechanism of action data
- For papillary conjunctivitis: any preclinical or clinical data on topical or ocular beta-2 agonist use in the condition
- For anaphylaxis: an adequately powered randomized trial of salbutamol as an adjunct to epinephrine
- For obstructive lung disease: confirmation that the indication is covered by existing labeling, and a note that the Phase 3 trial tested a combination rather than salbutamol alone
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

