---
layout: default
title: Olaparib
parent: High Evidence (L1-L2)
nav_order: 611
evidence_level: L1
indication_count: 1
---

# Olaparib
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **1** 
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

# Olaparib: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Olaparib is a PARP1/2 inhibitor originally used as maintenance therapy for platinum-sensitive, BRCA1/2-mutated relapsed ovarian cancer. The TxGNN model predicts it may also be effective for **Female Breast Carcinoma**, and this direction is already backed by **50 clinical trials** and **20 publications**, including two pivotal completed Phase 3 RCTs (OlympiAD, OlympiA) in gBRCA1/2-mutated, HER2-negative breast cancer.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (platinum-sensitive relapsed, BRCA1/2-mutated maintenance) — per clinical trial records; no India label on file |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Olaparib is a poly(ADP-ribose) polymerase (PARP1/2) inhibitor. It works by trapping PARP–DNA complexes at sites of single-strand DNA damage, blocking base-excision repair. In tumor cells with homologous recombination deficiency (HRD) — most commonly caused by germline or somatic BRCA1/2 mutations — this creates synthetic lethality, selectively killing cancer cells that cannot repair the resulting double-strand breaks. (Detailed formal MOA documentation from DrugBank is still pending — see DG002 below; the mechanism above is drawn from the trial-level evidence in this pack.)

Ovarian and breast cancer share a substantial biological link: both are classic BRCA1/2-associated malignancies, and patients with germline BRCA1/2 mutations carry elevated lifetime risk for both cancers. Since olaparib's efficacy in ovarian cancer is driven specifically by HRD/BRCA-mutation status rather than tissue-of-origin, the same synthetic-lethality mechanism plausibly extends to BRCA-mutated breast tumors.

This is not merely theoretical — the evidence pack shows olaparib has already completed pivotal Phase 3 trials in breast cancer (OlympiAD for metastatic disease, OlympiA for adjuvant high-risk early breast cancer), both restricted to germline BRCA1/2-mutated, HER2-negative populations. This strongly corroborates the TxGNN prediction and indicates the "new indication" is mechanistically well-established rather than speculative, even though it is not yet reflected in an India market authorization.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | Olaparib monotherapy vs. physician's-choice chemotherapy in gBRCA1/2-mutated, platinum-sensitive relapsed patients after ≥2 prior platinum regimens. Source flags this as high-relevance to the breast cancer evidence base (OlympiAD analog), but the trial title describes an ovarian cancer population — recommend manual verification of indication tagging. |
| [NCT06580314](https://clinicaltrials.gov/study/NCT06580314) | Phase 3 | Recruiting | 880 | One vs. two years of maintenance olaparib ± bevacizumab in BRCA1/2-mutated or HRD+ ovarian cancer after first-line platinum chemotherapy. |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | Completed | 202 | Real-world Phase 4 study in **Indian patients** with platinum-sensitive relapsed ovarian cancer and gBRCA1/2-mutated metastatic breast cancer — directly relevant to the India market context. |
| [NCT05498155](https://clinicaltrials.gov/study/NCT05498155) | Phase 2 | Active, not recruiting | 50 | Neoadjuvant olaparib monotherapy vs. olaparib + durvalumab in BRCA-mutated, early-stage HER2-negative breast cancer. |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | Completed | 25 | Carboplatin + olaparib followed by olaparib maintenance vs. capecitabine as first-line therapy in BRCA1/2-mutated, HER2-negative advanced breast cancer. |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Phase 1 | Completed | 103 | Dose-finding of olaparib + carboplatin in BRCA1/2 carriers with breast and ovarian cancer, including sporadic triple-negative breast cancer. |
| [NCT01237067](https://clinicaltrials.gov/study/NCT01237067) | Phase 1 | Completed | 77 | PK/PD study of olaparib + carboplatin in refractory/recurrent breast, ovarian, uterine, and cervical cancers. |
| [NCT04553926](https://clinicaltrials.gov/study/NCT04553926) | N/A | Completed | 661 | Real-world post-marketing surveillance of Lynparza (olaparib) tablets across approved indications in South Korea. |
| [NCT02264678](https://clinicaltrials.gov/study/NCT02264678) | Phase 1/2 | Active, not recruiting | 357 | Modular study of ceralasertib (ATR inhibitor) combined with chemotherapy and/or olaparib in advanced solid malignancies; supportive safety/PK data. |
| [NCT05932862](https://clinicaltrials.gov/study/NCT05932862) | Phase 1 | Recruiting | 429 | First-in-human study of XL309 (ISM3091) alone or combined with olaparib in advanced solid tumors. |

40 additional trials were identified but are lower priority (early-phase combination studies, terminated/withdrawn, or non-breast-specific populations).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | N Engl J Med | OlympiA: adjuvant olaparib significantly improved invasive disease-free survival in gBRCA1/2-mutated, HER2-negative high-risk early breast cancer. |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | N Engl J Med | OlympiAD: olaparib improved progression-free survival vs. chemotherapy in gBRCA-mutated, HER2-negative metastatic breast cancer. |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Ann Oncol | OlympiA overall survival update: adjuvant olaparib confirmed an OS benefit in high-risk early breast cancer. |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT | Eur J Cancer | OlympiAD extended follow-up: median OS 19.3 vs. 17.1 months for olaparib vs. chemotherapy (not statistically significant); safety profile consistent. |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Ann Oncol | OlympiAD final OS/tolerability results — favorable tolerability profile vs. chemotherapy. |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | RCT | J Clin Oncol | TBCRC 048: olaparib shows activity in metastatic breast cancer with somatic BRCA1/2 or other HR-pathway gene mutations, beyond germline BRCA. |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | RCT | Cancer Cell | I-SPY2: durvalumab + olaparib + paclitaxel increased pathologic complete response rates vs. paclitaxel alone in high-risk HER2-negative breast cancer. |
| [38588696](https://pubmed.ncbi.nlm.nih.gov/38588696/) | 2024 | RCT | Nature | PARTNER trial: neoadjuvant olaparib added to carboplatin-paclitaxel evaluated in BRCA-wildtype triple-negative breast cancer (n=559). |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Review | Target Oncol | Overview of PARP inhibitors (olaparib, talazoparib) approved for gBRCA-mutated, HER2-negative breast cancer. |
| [31650727](https://pubmed.ncbi.nlm.nih.gov/31650727/) | 2020 | Review | Ann Lab Med | Review of treatment and prevention strategies for BRCA1/2 pathogenic-variant breast cancer, including the role of PARP inhibitors. |

10 additional publications (mechanistic/functional variant-classification studies) support the BRCA/HRD rationale but are secondary to the clinical evidence above.

---

## India Market Information

Olaparib currently has **no market authorization on file in India** (market status: Not Marketed; 0 registrations). No product/license records are available to summarize.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor; synthetic lethality in HRD/BRCA-mutated tumors) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

**Drug Interactions**: 444 documented interactions on file. Notable **Major**-severity interactions include Aprepitant, Dexamethasone, and Clarithromycin. Multiple **Moderate**-severity interactions are also documented, including Metformin, Bupropion, Cimetidine, Miconazole, Ondansetron, Rosuvastatin, and Simvastatin.

Key warnings and contraindications are not yet available in this evidence pack — please refer to the package insert once available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence strength is high (L1) — two completed pivotal Phase 3 RCTs (OlympiAD, OlympiA) already establish olaparib's efficacy in gBRCA1/2-mutated, HER2-negative breast cancer, reinforced by an India-specific real-world Phase 4 study (NCT04330040). However, olaparib has no current India market authorization and two blocking/high-severity data gaps remain open, so guardrails are needed before advancing.

**To proceed, the following is needed:**
- India-specific label warnings/contraindications (DG001, Blocking — source: TFDA-equivalent regulator, PDF label parsing)
- Formal mechanism-of-action documentation via DrugBank API (DG002, High)
- Confirmation of India registration/licensing pathway status
- Verification that the indication population is restricted to germline BRCA1/2-mutated, HER2-negative breast cancer (consistent with the approved global label), including confirmation of the NCT02282020 population mismatch noted above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

