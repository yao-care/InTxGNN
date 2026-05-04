---
layout: default
title: Azithromycin
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
---

# Azithromycin
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

# Azithromycin: From Bacterial Infections to Polyclonal Hyperviscosity Syndrome (Multi-Indication Evaluation)

## One-Sentence Summary

Azithromycin is a macrolide antibiotic widely used to treat bacterial infections including community-acquired pneumonia, sexually transmitted infections, and skin and soft tissue infections.
The TxGNN model evaluates **10 new potential indications** for this drug, with the highest-ranked prediction being **Polyclonal Hyperviscosity Syndrome** (score 99.81%); however, the most clinically actionable signals emerge from **Congenital Hematological Disorder** (rank 10, particularly sickle cell disease) and **Monoclonal Gammopathy** (rank 7), with **4 registered clinical trials** and **8 publications** across these two indications supporting further investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (community-acquired pneumonia, STIs, skin infections) |
| Top Predicted Indication | Polyclonal Hyperviscosity Syndrome |
| TxGNN Prediction Score (Rank 1) | 99.81% |
| Evidence Level (Rank 1) | L5 |
| India Market Status | ✗ Not Marketed (0 registrations found) |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Ranks 1–3, 5–6, 8) / Research Question (Ranks 4, 7, 9, 10) |

---

## All Predicted Indications at a Glance

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation |
|------|-----------|-------------|----------------|----------------|
| 1 | Polyclonal Hyperviscosity Syndrome | 99.81% | L5 | Hold |
| 2 | Hyperamylasemia | 99.81% | L5 | Hold |
| 3 | Congenital Analbuminemia | 99.79% | L5 | Hold |
| 4 | Punctate Epithelial Keratoconjunctivitis | 99.78% | L4 | Research Question |
| 5 | Blood Group Incompatibility | 99.70% | L5 | Hold |
| 6 | Premalignant Hematological System Disease | 99.64% | L5 | Hold |
| 7 | Monoclonal Gammopathy | 99.61% | L4 | Research Question |
| 8 | Hematological Disease + Acquired Peripheral Neuropathy | 99.56% | L5 | Hold |
| 9 | Septicemic Plague | 99.52% | L4 | Research Question |
| 10 | Congenital Hematological Disorder | 99.40% | L4 | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Azithromycin is a macrolide antibiotic that inhibits bacterial protein synthesis by binding to the 50S ribosomal subunit and blocking peptide chain elongation. Beyond its antibacterial action, azithromycin exhibits well-documented immunomodulatory properties—including suppression of NF-κB signaling, inhibition of neutrophil chemotaxis, and reduction of pro-inflammatory cytokines (IL-8, TNF-α)—that have been therapeutically leveraged in chronic inflammatory pulmonary conditions such as diffuse panbronchiolitis and cystic fibrosis. Additionally, macrolide antibiotics including azithromycin have been shown to block autophagy flux and induce endoplasmic reticulum (ER) stress in malignant cells, a property relevant to oncological applications.

The TxGNN model's predictions cluster heavily around hematological and rare blood disorders. Most high-ranked predictions (ranks 1–3, 5–6, 8) appear to reflect indirect knowledge graph co-morbidity associations—such as the infection-dysproteinemia axis—rather than genuine mechanistic treatment links. For example, polyclonal hyperviscosity syndrome (rank 1) is driven by plasma exchange, not antibiotics; blood group incompatibility (rank 5) involves alloantibody-mediated hemolysis with no relevant azithromycin mechanism; and congenital analbuminemia (rank 3) is a structural gene defect unreachable by any antibiotic mechanism. These should be regarded as model artifacts.

The most mechanistically grounded predictions are **Congenital Hematological Disorder / Sickle Cell Disease** (rank 10) and **Monoclonal Gammopathy** (rank 7). For sickle cell disease, two independent research teams designed and registered clinical trials (NCT02630394, NCT02960503) hypothesizing that azithromycin's anti-inflammatory effects could reduce acute chest syndrome (ACS) incidence—a finding that represents genuine research community validation of the hypothesis, even though both trials were ultimately withdrawn before enrollment. For monoclonal gammopathy, an in vitro study (PMID 23546223) directly demonstrates that azithromycin enhances bortezomib cytotoxicity in multiple myeloma cell lines through ER stress accumulation, providing a preclinical mechanistic basis for further investigation.

---

## Clinical Trial Evidence

Evidence from Rank 10 (Congenital Hematological Disorder / Sickle Cell Disease):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02630394](https://clinicaltrials.gov/study/NCT02630394) | Phase 1 | Withdrawn | 0 | Pilot study of Azithromycin prophylaxis for acute chest syndrome in sickle cell disease; ACS is a leading cause of death in SCD and involves airway inflammation and atypical pulmonary organisms—targets amenable to azithromycin's dual antibacterial/anti-inflammatory action. Withdrawn before enrollment; reason undocumented. |
| [NCT02960503](https://clinicaltrials.gov/study/NCT02960503) | Phase 1/2 | Withdrawn | 0 | Macrolide therapy to improve FEV1 in adults with sickle cell disease; lung-specific inflammation is a hallmark of SCA and underlies pulmonary pathology. Withdrawn before enrollment; reason undocumented. |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5,000 | PK/PD and safety umbrella study for understudied drugs in children; not disease-specific to congenital hematological disorders—marginal relevance as a general pharmacokinetics reference. |
| [NCT04294641](https://clinicaltrials.gov/study/NCT04294641) | Phase 2 | Completed | 10 | Ibrutinib as first-line treatment for newly diagnosed chronic GvHD; not azithromycin-related, and GvHD is an acquired rather than congenital hematological condition—low relevance. |

> **Important**: The two directly relevant trials (NCT02630394, NCT02960503) were both withdrawn before enrolling any participants. The undocumented withdrawal reasons are a key information gap—determining whether withdrawal stemmed from funding loss, recruitment failure, or safety concerns is essential before proposing any new trial design.

---

## Literature Evidence

Evidence aggregated across all ranked predictions with available literature (priority: preclinical mechanistic > systematic review > case report):

| PMID | Year | Type | Journal | Relevant Indication (Rank) | Key Findings |
|------|------|------|---------|---------------------------|---------|
| [23546223](https://pubmed.ncbi.nlm.nih.gov/23546223/) | 2013 | In Vitro / Preclinical | Int J Oncol | Monoclonal Gammopathy (7) | Azithromycin blocks autophagy flux (LC3B-II and p62 accumulation) and, combined with bortezomib, enhances cytotoxicity in multiple myeloma cell lines (U266, IM-9, RPMI8226) via ER stress-mediated CHOP induction—the most mechanistically direct study in this pack |
| [26408070](https://pubmed.ncbi.nlm.nih.gov/26408070/) | 2015 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Congenital Hematological Disorder (10) | Antibiotics for preventing lower respiratory tract infections in high-risk children aged ≤12 years; may include sickle cell disease subgroups—specific sub-analysis not confirmable from abstract alone |
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In Vitro Antimicrobial Susceptibility | Antimicrob Agents Chemother | Septicemic Plague (9) | MIC data for 78 Yersinia pestis strains; ceftriaxone and ciprofloxacin were most active—azithromycin showed **poor in vitro activity**, directly contra-indicating its use for septicemic plague outside special populations |
| [12698575](https://pubmed.ncbi.nlm.nih.gov/12698575/) | 2002 | Animal Study | Antibiot Khimioter | Septicemic Plague (9) | Azithromycin showed high efficacy in experimental brucellosis (not plague); Brucella is susceptible in vitro to azithromycin with rapid normalization of bactericidal activity in peripheral blood cells |
| [19392866](https://pubmed.ncbi.nlm.nih.gov/19392866/) | 2009 | Systematic Review | Aliment Pharmacol Ther | Septicemic Plague (9) | Epidemiology and clinical features of travellers' diarrhoea; tangential relevance—azithromycin is used for travellers' diarrhoea treatment but this is not relevant to septicemic plague |
| [32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/) | 2021 | Case Report | Cornea | Punctate Epithelial Keratoconjunctivitis (4) | Molecular diagnosis of Encephalitozoon hellem microsporidia keratoconjunctivitis in an immunocompetent adult via metagenomic deep sequencing; azithromycin relevant only for this narrow infectious subtype, not for viral or allergic causes of punctate keratoconjunctivitis |
| [18355359](https://pubmed.ncbi.nlm.nih.gov/18355359/) | 2008 | Review | Clin Exp Dermatol | Monoclonal Gammopathy (7) | 50-year review of subcorneal pustular dermatosis (Sneddon-Wilkinson disease) with IgA monoclonal gammopathy association; azithromycin not discussed as treatment—tangential relevance to disease entity only |
| [22825522](https://pubmed.ncbi.nlm.nih.gov/22825522/) | 2012 | Case Report | Tumori | Monoclonal Gammopathy (7) | Ozone gas insufflation for bisphosphonate-related osteonecrosis of the jaw in a multiple myeloma patient; azithromycin 500 mg/day administered as supportive antibiotic, not for myeloma—not a repurposing signal |
| [34471086](https://pubmed.ncbi.nlm.nih.gov/34471086/) | 2021 | Case Report | Am J Case Rep | Congenital Hematological Disorder (10) | Megadose methylprednisolone for COVID-19-associated immune thrombocytopenia in an infant; azithromycin used concomitantly for infection management, not as ITP therapy |
| [33389938](https://pubmed.ncbi.nlm.nih.gov/33389938/) | 2020 | Case Report | Turk J Ophthalmol | Monoclonal Gammopathy (7) | Bartonella henselae neuroretinitis in a POEMS syndrome patient; azithromycin implied as potential treatment for Bartonella but not for POEMS or monoclonal gammopathy per se |

---

## India Market Information

No registrations were identified for Azithromycin in the current dataset (0 licenses, market status: Not Marketed).

> **Data Quality Note**: This finding is inconsistent with the global distribution of azithromycin, which is one of the world's most widely prescribed antibiotics and is registered in virtually every regulated market including India. This absence almost certainly reflects a data gap rather than actual regulatory status. Verification against CDSCO (Central Drugs Standard Control Organisation) official records is strongly recommended before drawing any regulatory conclusions.

---

## Safety Considerations

**Drug Interactions**: Azithromycin has 235 documented drug-drug interactions. Key interactions by severity level:

| Severity | Interacting Drug(s) | Clinical Concern |
|----------|---------------------|-----------------|
| **Major** | Cisapride | QT interval prolongation; risk of potentially fatal cardiac arrhythmia (torsades de pointes)—combination is generally contraindicated |
| **Major** | Dolasetron | Additive QT prolongation risk; cardiac monitoring required if co-administration is unavoidable |
| **Moderate** | Clarithromycin, Levofloxacin, Granisetron | Additional QT-prolonging agents; cumulative cardiac risk requires clinical assessment |
| **Moderate** | Famotidine, Aluminum hydroxide, Magaldrate, Magnesium hydroxide, Magnesium carbonate, Magnesium citrate | Antacids may reduce azithromycin absorption; administer at least 2 hours apart |
| **Moderate** | Loperamide, Bisacodyl, Lactulose, Lactitol, Castor oil, Glycerin, Balsalazide | GI motility interactions; clinical monitoring recommended |
| **Minor** | Amoxicillin, Metronidazole | Minimal clinical significance in most contexts |

> Please refer to the package insert for complete warnings and contraindications. Full package insert data (warnings, contraindications) was not available in this Evidence Pack and should be retrieved directly from official regulatory sources.

---

## Conclusion and Next Steps

**Decision: Hold** (Ranks 1–3, 5–6, 8) | **Research Question** (Ranks 4, 7, 9, 10)

**Rationale:**
Six of the ten TxGNN predictions (polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant hematological disease, and hematological disease with peripheral neuropathy) lack mechanistic plausibility and supporting evidence—these are most likely knowledge graph artifacts driven by comorbidity co-occurrence rather than genuine treatment signals, and should not advance further. The remaining four predictions (ranks 4, 7, 9, 10) each carry at least one piece of supporting evidence or a mechanistically defensible hypothesis, warranting designation as active research questions.

**Priority research directions and required actions:**

*Rank 10 – Sickle Cell Disease (Congenital Hematological Disorder)*
- Determine withdrawal reasons for NCT02630394 and NCT02630394 by contacting PIs or reviewing ClinicalTrials.gov change history
- Conduct systematic literature search for macrolide prophylaxis in sickle cell disease (2016–2026)
- Assess long-term safety profile of azithromycin in this population (macrolide resistance emergence, QTc effects, hepatotoxicity)
- If withdrawal was due to funding/logistics rather than safety: consider designing a new feasibility trial

*Rank 7 – Monoclonal Gammopathy / Multiple Myeloma*
- Replicate PMID 23546223 findings (azithromycin + bortezomib synergy) in additional myeloma cell lines and patient-derived samples
- Search for subsequent clinical translation of this preclinical finding (2013–2026)
- Assess interaction profile of azithromycin with standard myeloma regimens (bortezomib-based, IMiD-based)

*Foundational data gaps (all indications)*
- Retrieve full MOA documentation via DrugBank API (Data Gap DG002—currently rated High severity)
- Obtain official package insert warnings and contraindications from CDSCO (Data Gap DG001—currently rated Blocking)
- Verify India market status directly via CDSCO query (current dataset data appears incomplete)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

