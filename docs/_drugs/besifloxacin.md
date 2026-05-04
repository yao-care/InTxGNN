---
layout: default
title: Besifloxacin
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 8
---

# Besifloxacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Besifloxacin: From Bacterial Conjunctivitis to Bronchitis

## One-Sentence Summary

Besifloxacin (Besivance®) is a fourth-generation fluoroquinolone antibiotic formulated exclusively as an ophthalmic suspension for the treatment of bacterial conjunctivitis.
The TxGNN model assigns its highest prediction score to **Bronchitis** (99.84%), but this likely reflects a **class-effect over-extrapolation** from the broader fluoroquinolone drug class — besifloxacin's systemic bioavailability after topical ocular administration is near-zero (<1 ng/mL plasma concentration), rendering the respiratory indication pharmacologically implausible in its current formulation.
There are **no clinical trials** and **no publications** directly supporting this predicted new indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial Conjunctivitis (ophthalmic topical use) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Besifloxacin belongs to the **fluoroquinolone antibiotic class**, acting by inhibiting bacterial DNA gyrase (topoisomerase II) and topoisomerase IV — enzymes essential for bacterial DNA replication, transcription, and repair. Its antibacterial spectrum covers key ocular pathogens (*Staphylococcus aureus*, *Staphylococcus epidermidis*, *Streptococcus pneumoniae*, *Haemophilus influenzae*), which overlap substantially with common bronchitis-causing bacteria.

The TxGNN score of 99.84% for bronchitis is almost certainly driven by **class-level knowledge graph linkages** rather than drug-specific signals. Systemic fluoroquinolones such as levofloxacin and moxifloxacin carry approved respiratory indications — including community-acquired pneumonia and acute bacterial exacerbation of chronic bronchitis — and these drug-disease edges in the knowledge graph are likely being inherited by besifloxacin. This is a recognised limitation of graph-based prediction models when a drug belongs to a well-characterised pharmacological class.

There is, however, a critical and deliberate pharmacological barrier: besifloxacin was **engineered specifically to minimise systemic absorption**. Phase 1 pharmacokinetic data (NCT00407589) confirm that plasma concentrations after topical ocular dosing remain well below 1 ng/mL — many orders of magnitude below the minimum inhibitory concentrations required to treat lower respiratory tract pathogens. No systemic oral or parenteral formulation of besifloxacin exists. The prediction does not represent a feasible repurposing opportunity under the drug's current formulation strategy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Besifloxacin in Bronchitis.

> **Context note:** Six clinical trials were retrieved when querying Besifloxacin against the adjacent predicted indication "post-bacterial disorder" (rank 3), but **all six trials involve the drug's existing ophthalmic indications** (bacterial conjunctivitis treatment and cataract surgery prophylaxis). They provide no evidence of new indication development and are listed here for transparency only.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01175590](https://clinicaltrials.gov/study/NCT01175590) | Phase 3 | Completed | 518 | Safety of Besivance 0.6% vs. vehicle TID × 7 days in bacterial conjunctivitis — established local ocular safety profile |
| [NCT01740388](https://clinicaltrials.gov/study/NCT01740388) | Phase 3 | Terminated | 136 | Efficacy of Besifloxacin BID × 3 days vs. vehicle in bacterial conjunctivitis — terminated early, reducing evidence quality |
| [NCT01478256](https://clinicaltrials.gov/study/NCT01478256) | Phase 4 | Completed | 30 | Besifloxacin vs. erythromycin ointment for acute blepharitis — small post-marketing comparator study |
| [NCT01296542](https://clinicaltrials.gov/study/NCT01296542) | Phase 4 | Completed | 60 | Besivance vs. VIGAMOX for pre-operative conjunctival decontamination before cataract surgery |
| [NCT00407589](https://clinicaltrials.gov/study/NCT00407589) | Phase 1 | Completed | 24 | Systemic pharmacokinetics after single/multiple topical instillations — **confirmed near-zero systemic exposure (<1 ng/mL)**, key finding limiting all systemic repurposing hypotheses |
| [NCT04542759](https://clinicaltrials.gov/study/NCT04542759) | Phase 1 | Completed | 60 | Reduction of ocular surface microbiota prior to cataract surgery — microbiological endpoints only, no new indication signal |

---

## Literature Evidence

Currently no related literature available for Besifloxacin in Bronchitis.

---

## India Market Information

Besifloxacin is currently **not marketed in India**. No product authorisations or registration numbers are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Package insert data (TFDA/CDSCO warnings, contraindications) were not available at the time of this analysis. Retrieval from the regulatory agency's official website is recommended before any prescribing or protocol development.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite an exceptionally high TxGNN prediction score (99.84%), the bronchitis indication is **pharmacologically implausible** for besifloxacin in its current ophthalmic formulation. The signal is a class-effect artefact derived from the broader fluoroquinolone drug class — not a drug-specific repurposing opportunity. No clinical trials, literature, or preclinical data support this new use, and the drug's deliberate design for minimal systemic absorption constitutes a fundamental formulation barrier.

**To proceed, the following is needed:**

- **Formulation feasibility assessment**: Determine whether a systemic oral or IV formulation of besifloxacin has ever been developed or is pharmacologically viable; without this, no systemic indication can be pursued
- **PK/PD modelling**: Establish theoretical plasma concentrations achievable under a hypothetical systemic formulation and compare against MIC breakpoints for *S. pneumoniae*, *H. influenzae*, and *M. pneumoniae*
- **Mechanism of action documentation**: Retrieve full MOA data from DrugBank (DB06771) to enable mechanistic link analysis
- **Safety data retrieval**: Download and parse the TFDA/CDSCO package insert PDF to extract warnings, contraindications, and special population data
- **Exploratory hypothesis — Otitis Externa**: Among all 8 TxGNN predictions reviewed, **otitis externa (rank 8, score 99.03%)** is the only indication with a mechanistic rationale consistent with besifloxacin's topical route. Other fluoroquinolone ear drop formulations (ciprofloxacin/dexamethasone, ofloxacin) target the same pathogens (*P. aeruginosa*, *S. aureus*) via the same local delivery mechanism. This hypothesis warrants a dedicated preclinical feasibility study before any clinical development decision

> ⚠️ *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

