---
layout: default
title: Dapsone
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 1
---

# Dapsone
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

# Dapsone: From Leprosy to Pneumocystosis

## One-Sentence Summary

Dapsone is a sulfonamide antibiotic with established use in leprosy treatment and dermatological conditions such as dermatitis herpetiformis. The TxGNN model predicts it may be effective for **Pneumocystosis** (Pneumocystis jirovecii pneumonia, PCP), with **14 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Leprosy; dermatitis herpetiformis |
| Predicted New Indication | Pneumocystosis (Pneumocystis jirovecii Pneumonia) |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L1 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dapsone is a diaminodiphenyl sulfone antibiotic with both anti-microbial and anti-inflammatory properties. Although detailed mechanism-of-action data are not available in the current Evidence Pack, the published literature clearly demonstrates that dapsone blocks folic acid synthesis in *Pneumocystis jirovecii* by inhibiting dihydropteroate synthetase (DHPS) activity — the same enzyme-blocking pathway underlying its anti-leprosy efficacy. This mechanistic overlap makes the TxGNN prediction highly plausible.

Leprosy and pneumocystosis are both infectious diseases in which the causative organisms depend on folate metabolism for survival. Because dapsone is a DHPS inhibitor, its activity extends naturally to *P. jirovecii*, which shares this biosynthetic vulnerability. Synergistic combinations with trimethoprim (which blocks the next step of the same pathway) are well-established in clinical practice, further validating the rationale.

Importantly, dapsone is already a recognised second-line agent for PCP prophylaxis and treatment in clinical guidelines internationally — for example, the ECIL-5 guidelines recommend it as an alternative to TMP-SMX in haematological patients. The TxGNN model is therefore re-discovering a mechanistically and clinically coherent association, and the body of evidence is strong enough to consider dapsone for formal regulatory evaluation in India.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Completed | 290 | Dapsone + trimethoprim vs TMP/SMX for mild-to-moderate PCP in AIDS patients; also evaluated clindamycin/primaquine arm |
| [NCT00000802](https://clinicaltrials.gov/study/NCT00000802) | Phase 3 | Completed | 700 | Dapsone vs atovaquone for PCP prophylaxis in HIV-infected patients intolerant to TMP/SMX (CD4 ≤200) |
| [NCT00001028](https://clinicaltrials.gov/study/NCT00001028) | Phase 3 | Completed | 400 | Aerosolized pentamidine vs thrice-weekly dapsone for PCP prophylaxis in high-risk HIV patients intolerant to sulfonamides |
| [NCT00000991](https://clinicaltrials.gov/study/NCT00000991) | Phase 3 | Completed | 600 | Three-arm comparison of anti-pneumocystis regimens plus zidovudine for primary prevention in advanced HIV (CD4 <200) |
| [NCT00002283](https://clinicaltrials.gov/study/NCT00002283) | N/A | Completed | N/A | Dapsone + trimethoprim vs TMP/SMX for first-episode PCP in AIDS patients; evaluated adverse effect severity and suitability for outpatient use |
| [NCT00002043](https://clinicaltrials.gov/study/NCT00002043) | N/A | Completed | N/A | Dapsone 100 mg vs 50 mg daily as primary PCP prophylaxis in patients with ARC (oral thrush / hairy leukoplakia, CD4 <400) |
| [NCT00002120](https://clinicaltrials.gov/study/NCT00002120) | Phase 1 | Completed | 20 | Trimetrexate + leucovorin + dapsone vs TMP/SMX for moderately severe PCP; pharmacokinetic profiling of dapsone in this combination |
| [NCT00000739](https://clinicaltrials.gov/study/NCT00000739) | Phase 1 | Completed | 96 | Daily vs weekly dapsone PCP prophylaxis toxicity and pharmacokinetics in HIV-infected infants and children |
| [NCT04328688](https://clinicaltrials.gov/study/NCT04328688) | N/A | Completed | 30 | Clindamycin–TMP/SMX for PCP after solid organ transplantation; dapsone listed as an established second-line alternative context |
| [NCT02550080](https://clinicaltrials.gov/study/NCT02550080) | Phase 4 | Unknown | 3,130 | Prospective HLA-B\*1301 genetic screening to reduce dapsone hypersensitivity syndrome across dapsone-naive patients including PCP indication |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38583518](https://pubmed.ncbi.nlm.nih.gov/38583518/) | 2024 | Systematic review / NMA | *Clin Microbiol Infect* | Network meta-analysis of RCTs comparing PCP prophylaxis regimens in PLHIV; dapsone-based regimens evaluated for efficacy and safety vs TMP-SMX, aerosolised pentamidine, atovaquone |
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Systematic review / NMA | *Clin Microbiol Infect* | Network meta-analysis of PCP treatment regimens in PLHIV; TMP-SMX is primary treatment, dapsone-based combinations evaluated as alternatives |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Review | *Expert Opin Pharmacother* | Comprehensive review of *P. jirovecii* biology, risk factors, diagnosis, prevention, and treatment including dapsone regimens |
| [27550992](https://pubmed.ncbi.nlm.nih.gov/27550992/) | 2016 | Clinical guideline | *J Antimicrob Chemother* | ECIL-5 evidence-based recommendations for PCP prophylaxis in haematological malignancy and HSCT recipients; TMP-SMX first-line, dapsone as alternative |
| [9675476](https://pubmed.ncbi.nlm.nih.gov/9675476/) | 1998 | Review | *Clin Infect Dis* | Comprehensive review of dapsone's anti-*Pneumocystis* activity (in vitro, animal, clinical); confirms DHPS inhibition mechanism, pharmacokinetics, and clinical trial results |
| [8605054](https://pubmed.ncbi.nlm.nih.gov/8605054/) | 1995 | RCT | *AIDS* | Three-arm RCT: aerosolised pentamidine vs cotrimoxazole vs dapsone–pyrimethamine for primary PCP and toxoplasmic encephalitis prophylaxis in HIV patients |
| [8018144](https://pubmed.ncbi.nlm.nih.gov/8018144/) | 1993 | RCT | *Am J Med* | Prospective RCT comparing dapsone vs aerosolised pentamidine for PCP and toxoplasmic encephalitis prophylaxis in HIV-infected patients with CD4 <250 |
| [11155588](https://pubmed.ncbi.nlm.nih.gov/11155588/) | 2001 | Review | *Dermatol Clin* | Overview of dapsone and sulfapyridine pharmacology; notes anti-microbial and anti-inflammatory dual action, utility in PCP prophylaxis for HIV patients |
| [9606476](https://pubmed.ncbi.nlm.nih.gov/9606476/) | 1998 | Case report | *Ann Pharmacother* | Case of methemoglobinemia during dapsone PCP prophylaxis — important safety signal for monitoring |
| [32714715](https://pubmed.ncbi.nlm.nih.gov/32714715/) | 2020 | Case report | *Cureus* | Case of dapsone-induced hypoxia from methemoglobinemia; underscores the need for clinical vigilance in patients on dapsone therapy |

---

## India Market Information

Dapsone currently has **no registered products** in India. No authorisation records are available.

---

## Safety Considerations

**Drug Interactions:** A total of 350 drug–drug interactions have been identified for dapsone. The following are the principal **Moderate-level** interactions of clinical relevance:

| Interacting Drug | Interaction Level | Clinical Note |
|-----------------|------------------|---------------|
| Aprepitant | Moderate | CYP3A4-mediated interaction may alter dapsone levels |
| Metronidazole | Moderate | Additive haematological toxicity risk |
| Tinidazole | Moderate | Similar to metronidazole; monitor for haematotoxicity |
| Rosuvastatin | Moderate | Monitor for potential pharmacokinetic interaction |
| Simvastatin | Moderate | CYP-mediated interaction; monitor lipid-lowering therapy |
| Nateglinide | Moderate | Potential interaction affecting glucose regulation |
| Activated charcoal | Moderate | May reduce dapsone absorption if co-administered |
| Picosulfuric acid | Moderate | Clinical significance uncertain; monitor |
| Nitisinone | Moderate | Monitor for overlapping metabolic pathway effects |
| Troglitazone | Moderate | Historical concern; troglitazone withdrawn in most markets |

**Additional safety note from literature:** Methemoglobinemia is a known but manageable complication of dapsone therapy. Clinicians should monitor for cyanosis, unexplained hypoxia, and elevated methemoglobin levels, particularly at doses ≥100 mg/day or in patients with G6PD deficiency.

Detailed package-insert warnings and contraindications for the Indian market are not yet available and should be obtained from the CDSCO (Central Drugs Standard Control Organisation) or the product's originator dossier before prescribing.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for dapsone in pneumocystosis is exceptionally strong — at least four completed Phase 3 RCTs directly evaluate dapsone for PCP treatment or prophylaxis, and two recent systematic reviews with network meta-analysis (2024, 2025) confirm its role in clinical guidelines. The TxGNN prediction score of 99.73% is consistent with this robust clinical record. However, dapsone is not currently registered in India, and the formal package-insert safety data (warnings and contraindications specific to CDSCO approval) remain unavailable.

**To proceed, the following is needed:**
- **Regulatory pathway**: File a New Drug Application (NDA) or import licence request with CDSCO, or identify a local manufacturing partner for technology transfer
- **Safety documentation**: Obtain and review the full SmPC / package insert (including CDSCO-specific warnings and contraindications) before initiating any clinical use
- **MOA data**: Formally retrieve dapsone's DrugBank mechanism-of-action record (DB00250) to complete the mechanistic justification file
- **G6PD screening plan**: Establish a pre-treatment G6PD deficiency screening protocol to mitigate methemoglobinemia risk in the Indian population, where G6PD deficiency prevalence is significant
- **Pharmacovigilance plan**: Define methemoglobin monitoring schedule (baseline, weeks 1–2, and periodically thereafter) as a mandatory risk-minimisation measure
- **HLA-B\*1301 screening consideration**: In light of NCT02550080, evaluate whether prospective genetic screening for dapsone hypersensitivity syndrome is warranted in Indian patients prior to initiation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

