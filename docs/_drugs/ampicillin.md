---
layout: default
title: Ampicillin
parent: 僅模型預測 (L5)
nav_order: 58
evidence_level: L5
indication_count: 10
---

# Ampicillin
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

# Ampicillin: From Bacterial Infections to Laryngitis

## One-Sentence Summary

Ampicillin is a broad-spectrum aminopenicillin antibiotic classically used for the treatment of various bacterial infections including respiratory tract infections, urinary tract infections, meningitis, and septicaemia.
The TxGNN model predicts it may be effective for **Laryngitis**,
with **1 clinical trial** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in India; known use: broad-spectrum bacterial infections (respiratory, urinary tract, meningitis) |
| Predicted New Indication | Laryngitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the provided dataset. Based on established pharmacology, Ampicillin is a beta-lactam antibiotic that inhibits bacterial cell wall synthesis by covalently binding to penicillin-binding proteins (PBPs), disrupting peptidoglycan cross-linking and ultimately causing bacterial cell lysis. Its spectrum covers gram-positive cocci (Streptococcus pyogenes, Streptococcus pneumoniae) and select gram-negative bacilli (non-beta-lactamase-producing Haemophilus influenzae), which are recognized causative agents of bacterial laryngitis.

The mechanistic link to laryngitis is biologically plausible in a narrow context: confirmed bacterial laryngitis caused by susceptible organisms — particularly laryngeal abscess, Lyme-associated laryngeal involvement, or laryngeal actinomycosis — falls squarely within Ampicillin's activity profile. Case-level evidence (PMIDs 24930374, 30579693, 35923122) confirms beta-lactam antibiotics, including penicillin-class agents, are used effectively in these specific bacterial laryngeal complications.

However, this prediction comes with a critical caveat: 85–95% of laryngitis cases are viral in aetiology, where antibiotics confer no benefit. In the minority of bacterial cases, contemporary resistance patterns — particularly beta-lactamase-producing H. influenzae strains (prevalence 30–40%) — substantially limit Ampicillin monotherapy. The TxGNN prediction likely captures a shared disease-ontology signal between known Ampicillin-responsive bacterial infections and laryngitis co-morbidity clustering, rather than a validated direct therapeutic application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01406275](https://clinicaltrials.gov/study/NCT01406275) | N/A | Completed | 363 | Post-marketing surveillance of CLAVAMOX® (Amoxicillin/Clavulanate) in Japanese paediatric patients across multiple indications including laryngitis. Indirect evidence only — the study drug is amoxicillin/clavulanate combination, not Ampicillin monotherapy; results are not specific to laryngitis as an isolated endpoint. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39879424](https://pubmed.ncbi.nlm.nih.gov/39879424/) | 2025 | Guideline Review | CoDAS | Assessed methodological quality of clinical guidelines for laryngitis and pharyngitis management using AGREE II; identifies evidence gaps in current treatment guidelines |
| [25944348](https://pubmed.ncbi.nlm.nih.gov/25944348/) | 2015 | Retrospective Cohort | Otolaryngology–Head and Neck Surgery | Hospital- and physician-level variation in perioperative antibiotic use for laryngectomy; antibiotic choice (including beta-lactams) correlated with surgical site infection and wound dehiscence rates |
| [38145982](https://pubmed.ncbi.nlm.nih.gov/38145982/) | 2024 | Retrospective Study | Eur Arch Otorhinolaryngol | Microbiological profiling and drug-sensitivity analysis of neck abscesses in diabetic vs. non-diabetic patients; highlights appropriate antibiotic selection strategies for deep laryngeal/cervical infections |
| [35923122](https://pubmed.ncbi.nlm.nih.gov/35923122/) | 2023 | Case Report/Review | Ann Otol Rhinol Laryngol | Historical and modern case review of spontaneous laryngeal abscess; penicillin-class antibiotics noted as cornerstone treatment when bacterial aetiology is confirmed |
| [34986973](https://pubmed.ncbi.nlm.nih.gov/34986973/) | 2023 | Case Report | Auris Nasus, Larynx | COVID-19 presenting as acute epiglottitis with necrotic laryngeal lesions; emergency antibiotic treatment required for secondary bacterial laryngeal involvement |
| [30579693](https://pubmed.ncbi.nlm.nih.gov/30579693/) | 2019 | Case Report | Auris Nasus, Larynx | Laryngeal actinomycosis in a 14-year-old post-bone marrow transplant; condition resolved with penicillin-class antibiotic therapy |
| [24930374](https://pubmed.ncbi.nlm.nih.gov/24930374/) | 2014 | Case Report | Journal of Voice | Laryngeal actinomycosis in an immunocompromised 74-year-old; successfully resolved with a prolonged course of penicillin — provides direct support for beta-lactam use in laryngeal actinomycotic infections |
| [41536375](https://pubmed.ncbi.nlm.nih.gov/41536375/) | 2025 | Case Report | Cureus | Atypical croup presentation in a 3-year-old; illustrates scenarios where bacterial superinfection of laryngeal structures requires antibiotic escalation |
| [3977063](https://pubmed.ncbi.nlm.nih.gov/3977063/) | 1985 | Case Series | Anaesthesia and Intensive Care | 161 children with acute epiglottitis over 9 years; antibiotic therapy (ampicillin-class drugs were standard of care in this era) combined with airway management; five deaths noted, highlighting severity |
| [12402494](https://pubmed.ncbi.nlm.nih.gov/12402494/) | 2002 | Case Series | Acta Otorrinolaringológica Española | Two cases of paraglottic laryngeal abscess — a rare but life-threatening entity requiring prompt antibiotic therapy and surgical drainage |

---

## India Market Information

Ampicillin currently has **no registered products** in India. There are 0 approved licences on record, and the drug is classified as **not marketed**.

---

## Safety Considerations

**Drug Interactions (61 total interactions identified; key interactions listed below):**

| Interacting Drug | Level | Clinical Relevance |
|---|---|---|
| Tetracycline | Moderate | Tetracyclines are bacteriostatic and may antagonise the bactericidal activity of Ampicillin — avoid co-administration when possible |
| Doxycycline | Moderate | Same mechanism of antagonism as tetracycline; co-use for laryngitis should be carefully evaluated |
| Minocycline | Moderate | Same mechanism of antagonism; co-administration not recommended |
| Lansoprazole | Moderate | Proton pump inhibitors may alter gastric pH and affect oral ampicillin absorption |
| Dexlansoprazole | Moderate | Same mechanism as lansoprazole |
| Kanamycin | Moderate | Potential pharmacodynamic interaction with this aminoglycoside; monitor renal function if combined |
| Balsalazide | Moderate | Antibiotic co-administration may disrupt the gut flora required for balsalazide activation |
| Picosulfuric acid | Moderate | Osmotic laxatives may accelerate GI transit and reduce oral Ampicillin absorption |
| Clarithromycin | Minor | Macrolides are bacteriostatic; minor potential for pharmacodynamic antagonism |

Please refer to the full package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for Ampicillin in laryngitis is theoretically plausible but clinically narrow — applicable only to confirmed bacterial laryngitis caused by susceptible organisms (e.g., laryngeal actinomycosis, abscess, or streptococcal laryngitis). Current evidence is at L4 (preclinical/mechanistic level), supported only by case reports and one indirect post-marketing surveillance study that used a different drug (amoxicillin/clavulanate). The predominance of viral laryngitis aetiology and rising beta-lactamase resistance further limit the repurposing case. Ampicillin is also not registered in India, adding a substantial regulatory barrier.

**To proceed, the following is needed:**
- A prospective clinical trial directly evaluating Ampicillin (or ampicillin/sulbactam) vs. standard of care in microbiologically confirmed bacterial laryngitis
- Epidemiological data on bacterial laryngitis pathogen distribution and ampicillin susceptibility rates in the Indian patient population
- India regulatory registration pathway for Ampicillin (currently 0 licences)
- Formal MOA documentation from DrugBank or equivalent source (currently a data gap)
- Assessment of beta-lactamase resistance prevalence among laryngitis-causing pathogens locally to determine whether ampicillin monotherapy or ampicillin/sulbactam combination would be required
- Download and analysis of prescribing information (package insert) to identify formal warnings and contraindications (currently blocking S1 safety evaluation)

---

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

