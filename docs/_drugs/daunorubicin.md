---
layout: default
title: Daunorubicin
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 10
---

# Daunorubicin
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

# Daunorubicin: From Acute Leukemia to Hodgkin's Lymphoma

## One-Sentence Summary

Daunorubicin is a classic anthracycline antibiotic originally approved for the treatment of acute leukemia (AML and ALL), where it acts as a cytotoxic backbone agent in induction chemotherapy.
The TxGNN model predicts it may be effective for **Hodgkin's Lymphoma**, with **50 clinical trials** and **20 publications** currently supporting this direction.
While direct Daunorubicin data in Hodgkin's Lymphoma remains limited, robust Phase 3 evidence from the broader anthracycline drug class provides a strong mechanistic and clinical foundation for this prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute leukemia (AML / ALL) |
| Predicted New Indication | Hodgkin's Lymphoma |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L2 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacology, Daunorubicin is an anthracycline antibiotic that exerts cytotoxic effects primarily through intercalation into the DNA double helix and inhibition of topoisomerase II — an enzyme essential for DNA replication and repair. This disrupts DNA synthesis, triggers DNA strand breaks, and ultimately induces apoptosis in rapidly dividing cells. It was originally approved for the treatment of **acute leukemia**, where its activity in highly proliferative hematologic malignancies is well documented.

Hodgkin's Lymphoma (HL) is likewise a hematologic malignancy arising from clonal B-lymphocytes (Reed–Sternberg cells), characterized by rapid cellular proliferation — precisely the biological substrate that anthracyclines target. The mechanistic parallel between leukemia and HL is direct: both are highly chemosensitive lymphoid malignancies driven by DNA replication. Indeed, Doxorubicin (the structural analogue of Daunorubicin within the same anthracycline class) forms the backbone of the ABVD and AVD regimens, which are the current standard of care for HL. Daunorubicin shares the same core pharmacophore and mode of action as Doxorubicin, differing only in a minor side-chain modification.

Direct supporting evidence for Daunorubicin in lymphoma appears in early clinical literature: PMID 9387047 (1997) evaluated liposomal Daunorubicin (DaunoXome) in 19 patients with relapsed or refractory lymphoma, demonstrating objective responses at higher dose schedules with a manageable cardiac safety profile. PMID 378369 (1979) provides an early analytical comparison of Daunorubicin and Doxorubicin across cancer types, confirming overlapping therapeutic activity. The TxGNN knowledge graph prediction (score 99.81%) therefore reflects a biologically coherent inference grounded in both drug-class clinical success and pharmacological similarity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT05922904](https://clinicaltrials.gov/study/NCT05922904) | Phase 2 | Active, Not Recruiting | 25 | BV + Pembrolizumab + Doxorubicin + Dacarbazine in Stage II bulky or Stage III/IV classic HL; evaluates PET-adapted de-escalation |
| [NCT04685616](https://clinicaltrials.gov/study/NCT04685616) | Phase 3 | Recruiting | 1,042 | RADAR trial: ABVD vs A2VD ± ISRT in untreated Stage IA/IIA HL; landmark Phase 3 with PET response-adapted design |
| [NCT06745076](https://clinicaltrials.gov/study/NCT06745076) | Phase 2 | Recruiting | 125 | PRECISE-HL: ctDNA-guided personalised reduction of Nivolumab + Doxorubicin + Vinblastine + Dacarbazine intensity in advanced HL |
| [NCT00822120](https://clinicaltrials.gov/study/NCT00822120) | Phase 2 | Completed | 371 | Response-adapted therapy for Stage III–IV HL using interim FDG-PET; tested escalation to BEACOPP for PET-positive patients |
| [NCT02797717](https://clinicaltrials.gov/study/NCT02797717) | — | Recruiting | 2,200 | EuroNet-C1: International multicentre trial reducing radiotherapy in classical HL in children and adolescents |
| [NCT00005578](https://clinicaltrials.gov/study/NCT00005578) | Phase 3 | Completed | 219 | Paediatric advanced-stage HL: combination chemotherapy ± dexrazoxane (cardioprotection); confirmed anthracycline necessity |
| [NCT00302003](https://clinicaltrials.gov/study/NCT00302003) | Phase 3 | Completed | 287 | Low-risk paediatric Hodgkin's disease: chemotherapy before radiation and/or additional chemo; established anthracycline backbone |
| [NCT06831370](https://clinicaltrials.gov/study/NCT06831370) | Phase 4 | Recruiting | 124 | **India-specific** — BV + AVD (Doxorubicin + Vinblastine + Dacarbazine) in Indian patients with untreated Stage 3/4 classical HL; includes cardiac monitoring (ECHO, PFT) |
| [NCT02191930](https://clinicaltrials.gov/study/NCT02191930) | Phase 2 | Completed | 70 | BV or B-CAP in older patients with newly diagnosed classical HL; ORR and 3-year PFS as co-primary endpoints |
| [NCT01868451](https://clinicaltrials.gov/study/NCT01868451) | — | Active, Not Recruiting | 118 | BV + AVD in early-stage unfavourable-risk HL; evaluates feasibility of omitting bleomycin and radiation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39413375](https://pubmed.ncbi.nlm.nih.gov/39413375/) | 2024 | RCT | N Engl J Med | Nivolumab + AVD (Doxorubicin + Vinblastine + Dacarbazine) vs ABVD in advanced classic HL; nivolumab combination improved PFS while maintaining safety |
| [35830649](https://pubmed.ncbi.nlm.nih.gov/35830649/) | 2022 | RCT follow-up | N Engl J Med | 5-year follow-up of A+AVD vs ABVD in Stage III/IV HL; confirmed long-term overall survival benefit with BV-augmented Doxorubicin regimen |
| [27332902](https://pubmed.ncbi.nlm.nih.gov/27332902/) | 2016 | RCT | N Engl J Med | PET-CT interim response-adapted strategy in advanced HL; escalation to BEACOPP for interim PET-positive patients improved outcomes |
| [20818855](https://pubmed.ncbi.nlm.nih.gov/20818855/) | 2010 | RCT | N Engl J Med | 4-arm randomised trial comparing chemotherapy intensity and radiation dose in early-stage favourable HL; established anthracycline minimisation principles |
| [9387047](https://pubmed.ncbi.nlm.nih.gov/9387047/) | 1997 | Phase I/II | Invest New Drugs | **Direct Daunorubicin evidence**: Liposomal Daunorubicin (DaunoXome) in 19 relapsed/refractory lymphoma patients; 1 CR + 2 PR at 120 mg/m² with manageable cardiac toxicity |
| [36271128](https://pubmed.ncbi.nlm.nih.gov/36271128/) | 2022 | Retrospective cohort | Sci Rep | Interim FDG-PET/CT predictive value in 245 HL patients treated with ABVD; interim PET-2 negativity strongly correlated with long-term disease-free survival |
| [378369](https://pubmed.ncbi.nlm.nih.gov/378369/) | 1979 | Review | Cancer Treat Rep | **Direct Daunorubicin evidence**: Comparative analysis of Daunorubicin and Adriamycin (Doxorubicin) across cancer types; documented overlapping therapeutic roles in haematologic malignancies |
| [28365830](https://pubmed.ncbi.nlm.nih.gov/28365830/) | 2017 | Review | Curr Oncol Rep | Current role of radiotherapy in early-stage HL within risk-adapted and response-adapted treatment frameworks; context for non-anthracycline adjuncts |
| [14584273](https://pubmed.ncbi.nlm.nih.gov/14584273/) | 2003 | Review | Gan To Kagaku Ryoho | Overview of haematologic tumour chemotherapy development; explicitly discusses Daunorubicin's role in AML and the evolution of ABVD as the HL standard |
| [21774715](https://pubmed.ncbi.nlm.nih.gov/21774715/) | 2011 | Editorial | N Engl J Med | "Hodgkin's lymphoma — the great teacher": landmark perspective on how HL shaped modern oncology, including the central role of anthracycline-containing combination regimens |

---

## Cytotoxicity

Daunorubicin is a conventional cytotoxic anthracycline chemotherapy agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Anthracycline class (intercalating agent / topoisomerase II inhibitor) |
| Myelosuppression Risk | High — severe neutropenia, thrombocytopenia, and anaemia are expected dose-limiting toxicities; nadir typically occurs at 10–14 days post-infusion |
| Emetogenicity Classification | Moderate to high emetogenicity (5-HT₃ antagonist + dexamethasone prophylaxis recommended) |
| Monitoring Items | CBC with differential (pre-cycle and at nadir), liver function tests, renal function, serum uric acid (tumour lysis risk), and serial cardiac monitoring (LVEF by ECHO or MUGA at baseline and after cumulative dose thresholds) |
| Handling Protection | Must follow cytotoxic drug safe handling regulations — closed system drug transfer devices, protective PPE, designated preparation area required |

> **Cardiac Toxicity Note**: Daunorubicin carries a cumulative dose-dependent cardiotoxicity risk (dilated cardiomyopathy, congestive heart failure). Cumulative lifetime dose should be carefully tracked. Dexrazoxane should be considered as a cardioprotectant in settings with high cumulative anthracycline exposure. PMID 9387047 noted no clinical cardiac deterioration with liposomal Daunorubicin at 120 mg/m², suggesting formulation may influence cardiac risk profile.

---

## Safety Considerations

**Drug Interactions** (387 interactions identified; representative selection below):

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|---------|-------------------|
| Cisapride | **Major** | Risk of QT prolongation and potentially fatal arrhythmia; avoid combination |
| Dolasetron | **Major** | Additive QT prolongation risk; use alternative antiemetics (ondansetron with monitoring) |
| Papaverine | **Major** | Additive QT prolongation; avoid co-administration |
| Deferiprone | **Major** | Additive myelosuppression risk; avoid concurrent use during chemotherapy cycles |
| Macimorelin | **Major** | Potential QT prolongation interaction; avoid if cardiac monitoring unavailable |
| Clarithromycin | Moderate | CYP3A4 inhibition may increase daunorubicin exposure; monitor for enhanced toxicity |
| Ondansetron | Moderate | Additive QT prolongation; ECG monitoring recommended when co-administered |
| Levofloxacin | Moderate | Additive QT prolongation risk; prefer alternative antibiotics |
| Granisetron / Palonosetron / Rolapitant | Moderate | QT prolongation; balance antiemetic benefit vs. cardiac risk with ECG monitoring |
| Eliglustat | Moderate | P-gp/CYP2D6 interaction may alter drug levels |

> Total DDI database entries: 387. The predominant interaction theme is **QT prolongation** (relevant for pre-existing cardiac conditions or concurrent QT-prolonging antiemetics) and **additive myelosuppression**. A full medication reconciliation is mandatory before each treatment cycle.

---

## India Market Information

Daunorubicin is currently **not registered or marketed in India** (0 active authorisations in the CDSCO database). Clinical use would require individual patient import approval or compassionate use authorisation. This absence of a local regulatory filing is a key consideration for any market development strategy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction score of 99.81% for Hodgkin's Lymphoma is mechanistically well-supported: Daunorubicin and Doxorubicin share the same anthracycline pharmacophore, and Doxorubicin-based regimens (ABVD, AVD, A+AVD) represent the global standard of care for HL across multiple completed Phase 3 trials. Direct evidence for Daunorubicin in lymphoma exists (PMID 9387047, PMID 378369), and the class-level evidence is strong. However, drug-specific Phase 3 data for Daunorubicin in HL is absent, and the drug is not currently registered in India.

**To proceed, the following is needed:**

- **MOA documentation**: Retrieve complete mechanism of action and pharmacokinetic data from DrugBank API or package insert (remediation for DG002) to support regulatory submissions
- **India package insert safety data**: Download and parse the reference country (e.g., US, EU) prescribing information to complete the safety profile — including full black-box warnings, contraindications, and dose-limiting toxicity thresholds (remediation for DG001)
- **Head-to-head comparison with Doxorubicin**: Conduct a structured literature review to determine whether Daunorubicin offers any clinical advantage (e.g., liposomal formulation reducing cardiac toxicity per PMID 9387047) over Doxorubicin in HL, particularly for patient populations with pre-existing cardiac risk
- **Regulatory pathway assessment**: Evaluate CDSCO requirements for new drug application or import licence for Daunorubicin in India, referencing existing approvals in US/EU (Cerubidine, DaunoXome)
- **Cardiac safety monitoring plan**: Design a prospective cardiac monitoring protocol (baseline ECHO, serial LVEF assessments, cumulative dose ceiling) prior to any clinical study initiation
- **QT risk management protocol**: Given 5 Major DDIs involving QT prolongation, develop a medication restriction list and ECG monitoring schedule for co-administered drugs in any investigator-initiated study

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

