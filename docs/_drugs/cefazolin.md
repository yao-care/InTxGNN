---
layout: default
title: Cefazolin
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 8
---

# Cefazolin
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

# Cefazolin: From Bacterial Infections to Infectious Otitis Media

## One-Sentence Summary

Cefazolin is a first-generation cephalosporin antibiotic established internationally for surgical prophylaxis and gram-positive bacterial infections, though it holds no registered indication in India.
The TxGNN model predicts it may have activity against **Infectious Otitis Media**, supported by **1 clinical trial** (subsequently terminated) and **3 publications**.
The mechanistic rationale is plausible but partial — coverage gaps for key otitis media pathogens limit its candidacy as a frontline therapy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No registered indication in India (international use: surgical prophylaxis, gram-positive bacterial infections) |
| Predicted New Indication | Infectious Otitis Media |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Cefazolin is a first-generation beta-lactam cephalosporin that inhibits bacterial cell wall synthesis by binding to penicillin-binding proteins (PBPs), disrupting peptidoglycan cross-linking and causing bacterial cell lysis. It has excellent coverage against methicillin-susceptible *Staphylococcus aureus* (MSSA) and beta-hemolytic *Streptococcus* species, making it a reliable antibiotic for surgical prophylaxis and skin/soft tissue infections.

Infectious otitis media (acute otitis media, AOM) is predominantly caused by *Streptococcus pneumoniae*, *Haemophilus influenzae*, and *Moraxella catarrhalis*. Cefazolin covers *S. pneumoniae* and MSSA reasonably well, but its activity against *H. influenzae* (particularly beta-lactamase-producing strains) and *M. catarrhalis* is suboptimal — two of the three leading AOM pathogens. Standard-of-care therapy currently favours amoxicillin-clavulanate or higher-generation cephalosporins (e.g., cefdinir, cefuroxime) with broader gram-negative coverage.

The TxGNN prediction likely reflects Cefazolin's antibiotic class membership and antibacterial activity against gram-positive cocci that contribute to otitis media, as well as proximity in the drug-disease knowledge graph to otitis-related nodes. The mechanistic link is therefore partial: valid for a subset of causative organisms but not the full etiological spectrum of infectious otitis media. This is not a repurposing signal of novel mechanism — it is a spectrum-of-coverage question.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01511107](https://clinicaltrials.gov/study/NCT01511107) | Phase 2b | Terminated | 520 | Multicenter, double-blind, placebo-controlled RCT comparing 5-day (short course) vs. 10-day (standard) antibiotic treatment in children aged 6–23 months with AOM, targeting antimicrobial resistance impact. Trial was terminated before completion — the specific reason must be investigated: administrative/funding termination preserves the research question; efficacy failure would substantially downgrade the evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [39567876](https://pubmed.ncbi.nlm.nih.gov/39567876/) | 2025 | Case Report | Ann Otol Rhinol Laryngol | Ceftazidime-Cefazolin empiric combination used for Gradenigo Syndrome (petrous apicitis as a rare complication of AOM); demonstrates Cefazolin's inclusion in multi-drug empiric regimens for severe otitis media complications, though it targets gram-positive coverage in the combination |
| [877649](https://pubmed.ncbi.nlm.nih.gov/877649/) | 1977 | Review | Southern Medical Journal | Broad review of cephalosporin antibiotics in pediatric infections including ear infections; highlights gram-positive efficacy and relative safety profile, while acknowledging spectrum limitations relevant to otitis media |
| [3742953](https://pubmed.ncbi.nlm.nih.gov/3742953/) | 1986 | Review | Clinical Pharmacy | Stevens-Johnson syndrome case review in a paediatric patient with a treatment history including antibiotics for otitis media; Cefazolin mentioned in therapeutic context rather than as primary studied agent |

---

## India Market Information

Cefazolin is currently **not registered in India**. No marketing authorizations have been identified in the CDSCO database, and the regulatory market status is confirmed as not marketed. There are no approved indications, no local prescribing information, and no post-marketing safety data from the Indian population available for review.

---

## Safety Considerations

**Drug Interactions:** 112 drug interactions have been identified in the DDInter database. The following carry a confirmed Moderate severity classification:

| Interacting Drug | Severity | Clinical Note |
|------|------|------|
| Kanamycin | Moderate | Combined nephrotoxicity risk when co-administered with aminoglycosides |
| Neomycin | Moderate | Additive nephrotoxicity risk |
| Streptomycin | Moderate | Additive nephrotoxicity risk with aminoglycosides |
| Picosulfuric acid | Moderate | Potential interaction in bowel preparation or perioperative settings |

An additional 108 interactions are classified as "Unknown" severity — the full interaction profile should be reviewed before any clinical application.

Please refer to the product package insert for complete warnings and contraindications (prescribing information was not available in the current evidence pack).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Cefazolin's antibacterial mechanism is mechanistically plausible for gram-positive otitis media pathogens (MSSA, *Streptococcus*), but its coverage of *H. influenzae* and *M. catarrhalis* — the two most prevalent AOM co-pathogens — is insufficient for a competitive repurposing claim. The sole identified clinical trial was terminated before completion, and the available literature comprises retrospective reviews and a single case report, falling short of the evidence threshold needed to advance this candidate. Note that a related indication, **Middle Ear Disease** (rank 3), carries stronger evidence (L2, two clinical trials including an ongoing Phase 4) and a "Proceed with Guardrails" recommendation — that pathway may be more productive to pursue.

**To proceed, the following is needed:**
- Clarification of the NCT01511107 termination reason (administrative/funding versus efficacy or safety failure)
- CDSCO registration and package insert retrieval to establish warnings and contraindications for India-specific use
- Complete mechanism of action data from the DrugBank API (DrugBank ID: DB01327)
- Microbiological susceptibility data for dominant AOM pathogens in the target Indian patient population
- Assessment of whether the surgical prophylaxis use case (Middle Ear Disease, rank 3) offers a more viable near-term pathway than de novo AOM treatment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

