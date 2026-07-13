---
layout: default
title: Miconazole
parent: 僅模型預測 (L5)
nav_order: 415
evidence_level: L5
indication_count: 1
---

# Miconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Miconazole: From Antifungal Treatment to Acne

## One-Sentence Summary

Miconazole is an imidazole-class antifungal agent widely used to treat fungal and yeast infections of the skin and mucous membranes.
The TxGNN model predicts it may be effective for **Acne (disease)**,
with **1 clinical trial** and **4 publications** currently providing supporting evidence for this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antifungal (fungal skin infections, mucosal candidiasis) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Miconazole is an imidazole-class antifungal agent that works primarily by inhibiting ergosterol biosynthesis, disrupting fungal cell membrane integrity. Its original clinical use is well established in treating dermatophyte infections, cutaneous candidiasis, and mucosal yeast infections. Notably, detailed mechanism of action data is not currently available in this Evidence Pack; the following analysis is based on published literature and the TxGNN repurposing rationale.

Three mechanistic pathways link Miconazole to acne: First, *in vitro* studies have demonstrated that azole-class antifungals, including Miconazole, exhibit direct antibacterial activity against *Cutibacterium acnes* (formerly *Propionibacterium acnes*), the key pathogen driving inflammatory acne lesions (PMID 20045949). Second, Miconazole's well-documented antifungal activity against *Malassezia* spp. may address *Malassezia* (Pityrosporum) folliculitis, a condition frequently misdiagnosed as acne vulgaris, expanding its practical utility in acne-like presentations. Third, independent literature reviews document anti-inflammatory adjunct effects of Miconazole nitrate beyond its antifungal mechanism (PMID 18627330), which could theoretically attenuate the inflammatory component of acne.

However, it is important to note that the high TxGNN score (0.9954) is primarily driven by structural associations within the knowledge graph (antifungal → skin condition pathway) rather than direct causal mechanistic evidence. No randomised controlled trial has tested Miconazole as a standalone acne treatment, and the mechanistic link remains at the preclinical/in vitro level.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Evaluated a triple-combination cream (Beclomethasone 0.025% + Gentamicin 0.1% + Clotrimazole 1%) in patients with contaminated dermatosis showing acne features; not Miconazole-specific and provides no isolatable efficacy data for Miconazole |

> **Note:** The only registered trial tests a combination product containing Clotrimazole (not Miconazole), was suspended, and cannot support attribution of any effect to Miconazole alone.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Narrative Review | *Expert Opinion on Pharmacotherapy* | Summarises multifaceted skin effects of Miconazole nitrate beyond antifungal action, including anti-inflammatory properties relevant to acne pathophysiology |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Split-face Clinical Study | *Skin Research and Technology* | Assessed management of mild catamenial (hormonal) acne; Miconazole-containing formulation evaluated in a split-face design; provides limited direct clinical evidence |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Case Series | *Clinical and Experimental Dermatology* | Pityrosporum folliculitis in 62 patients frequently misdiagnosed as acne vulgaris; Miconazole among antifungals trialled; highlights the diagnostic overlap and potential utility |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro Laboratory Study | *Biological & Pharmaceutical Bulletin* | Azole antifungals including Miconazole demonstrated inhibitory activity against *P. acnes* isolates *in vitro*; minimum inhibitory concentrations reported; no clinical translation data provided |

---

## India Market Information

Miconazole currently has **no registered products** in India. No authorisation numbers, brand names, or approved indications are on file.

> Miconazole is a well-established antifungal widely available in many markets (e.g., EU, US, Japan) in topical and oral gel formulations. A regulatory filing would be required for any indication in India, including the predicted acne use.

---

## Safety Considerations

**Drug Interactions:** A total of **376 drug-drug interactions** have been identified. The most clinically significant ones include:

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|-------------------|
| Paclitaxel | Moderate | CYP3A4 inhibition may increase taxane exposure |
| Fentanyl | Moderate | CYP3A4 inhibition may enhance opioid effects |
| Acalabrutinib | Moderate | Possible increase in BTK inhibitor plasma levels |
| Nifedipine | Moderate | Calcium channel blocker levels may be elevated |
| Ethinylestradiol | Moderate | Potential alteration of oral contraceptive exposure |
| Alfentanil | Moderate | Opioid metabolism may be impaired |
| Alfuzosin | Moderate | Risk of hypotension may increase |
| Amiodarone | Moderate | QTc prolongation risk via CYP inhibition |
| Amitriptyline | Moderate | Tricyclic antidepressant levels may rise |
| Amlodipine | Moderate | CYP3A4-mediated interaction possible |
| Alprazolam | Moderate | Benzodiazepine sedation may be prolonged |
| Dolutegravir | Minor | Limited clinical significance |

> Key warnings and contraindications are not available in this Evidence Pack. Please refer to the official package insert for complete safety information before any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Current evidence is at the preclinical/in vitro level (L4), with no completed clinical trial specifically evaluating Miconazole monotherapy for acne. The single registered trial used a different azole (Clotrimazole) in a combination product and was suspended. While the mechanistic hypothesis is biologically plausible, it does not yet meet the threshold for clinical repurposing investment.

**To proceed, the following is needed:**

- **Confirm mechanism of action (MOA):** Retrieve full DrugBank entry for DB01110 to document the ergosterol-inhibition mechanism and any documented anti-inflammatory or antibacterial activities
- **Safety baseline:** Download and parse the official prescribing information (package insert) to establish key warnings and contraindications before any S1 safety screen
- **Topical formulation feasibility assessment:** Confirm whether existing Miconazole topical formulations (e.g., 2% nitrate cream) achieve sufficient follicular drug concentrations for anti-acne effect
- **Prospective in vitro / ex vivo study:** A controlled *in vitro* study comparing Miconazole's anti-*C. acnes* MIC against standard of care antibiotics (clindamycin, benzoyl peroxide) would be a low-cost next step before any clinical investment
- **Pilot clinical trial design:** If in vitro data supports efficacy, consider a small split-face randomised pilot (n ≈ 30–40) comparing Miconazole 2% cream to vehicle in mild-to-moderate acne vulgaris
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

