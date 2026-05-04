---
layout: default
title: Busulfan
parent: 僅模型預測 (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
---

# Busulfan
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

# Busulfan: From Chronic Myelogenous Leukemia to Myelodysplastic Syndrome

## One-Sentence Summary

Busulfan is a bifunctional alkylating agent historically established as cytoreductive (conditioning) chemotherapy prior to allogeneic hematopoietic stem cell transplantation (allo-HSCT), with its roots in the treatment of chronic myelogenous leukemia (CML) before the targeted therapy era.
The TxGNN model predicts it may be effective for **Myelodysplastic Syndrome (MDS)**, with **50 clinical trials** and **20 publications** currently supporting this direction.
The overall evidence is exceptionally strong, anchored by Phase 3 randomised controlled data and multiple completed Phase 2 studies evaluating busulfan-based conditioning regimens specifically in MDS patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic myelogenous leukemia; haematopoietic stem cell transplantation conditioning |
| Predicted New Indication | Myelodysplastic Syndrome (MDS) |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Busulfan is a bifunctional alkylating agent that cross-links DNA strands within rapidly dividing cells, causing irreversible damage to haematopoietic progenitors. This myeloablative property is precisely the mechanism exploited in conditioning regimens before allo-HSCT: by eradicating the patient's existing bone marrow — including malignant or dysplastic clones — busulfan creates the physical and immunological space required for donor stem cells to engraft and re-establish normal haematopoiesis.

Currently, detailed mechanism of action data from DrugBank is not available in this Evidence Pack. Based on known pharmacological information, busulfan belongs to the alkylsulfonate class of alkylating agents. Its DNA cross-linking action is not cell-type-specific; it targets any rapidly proliferating haematopoietic clone regardless of underlying pathology, which is why it has been broadly applied across haematological malignancies. In the MDS setting, the goal is not direct anti-tumour cytotoxicity in the traditional sense, but rather the destruction of abnormal dysplastic clones to allow donor haematopoiesis to take over.

MDS and CML share the same fundamental target tissue — the bone marrow — and both involve abnormal haematopoietic stem cell clones. Busulfan-based conditioning (typically combined with fludarabine or cyclophosphamide) serves as the backbone preparative regimen for MDS allo-HSCT. A landmark Phase 3 randomised trial published in *The Lancet Haematology* (2020) directly compared busulfan/fludarabine against treosulfan/fludarabine in older MDS and AML patients undergoing allo-HSCT, formally establishing busulfan as the reference standard conditioning regimen. A 2023 Phase 3 trial in the same journal further demonstrated that adding G-CSF and decitabine to busulfan-cyclophosphamide significantly reduced relapse in high-risk MDS. The TxGNN prediction is therefore not a speculative extrapolation but a formal recognition of an existing, evidence-supported clinical application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02744742](https://clinicaltrials.gov/study/NCT02744742) | Phase 2/3 | Completed | 202 | Prospective RCT directly comparing G-CSF+Decitabine+Bu+Cy vs Bu+Cy conditioning in RAEB-1, RAEB-2 and AML secondary to MDS undergoing allo-HSCT; highest-grade direct evidence for MDS-specific busulfan use |
| [NCT01471444](https://clinicaltrials.gov/study/NCT01471444) | Phase 3 | Completed | 256 | Randomised trial of once-daily Fludarabine+Clofarabine vs Fludarabine alone combined with IV Busulfan for AML and MDS; confirmed Bu+Flu as the standard myeloablative backbone |
| [NCT00629798](https://clinicaltrials.gov/study/NCT00629798) | Phase 2 | Completed | 64 | Bu+Melphalan+Flu with peri-transplant Palifermin for T-cell–depleted allo-HSCT specifically in advanced MDS and AML; directly assessed MDS transplant outcomes and mucositis prophylaxis |
| [NCT00475020](https://clinicaltrials.gov/study/NCT00475020) | Phase 2 | Completed | 63 | Reduced-intensity Fludarabine+Busulfan+ATG conditioning specifically designed for myelofibrosis and MDS; evaluated disease control, engraftment, and safety over a 10-year follow-up |
| [NCT01168219](https://clinicaltrials.gov/study/NCT01168219) | Phase 2 | Completed | 68 | Azacitidine added to Bu+Flu+ATG RIC allo-HSCT for high-risk MDS and older AML; explored maintenance strategies within busulfan-based conditioning frameworks |
| [NCT05453552](https://clinicaltrials.gov/study/NCT05453552) | Phase 2/3 | Unknown | 242 | Prospective comparison of G-CSF+DAC+BUCY vs G-CSF+DAC+BF conditioning for high-risk MDS undergoing allo-HSCT; large ongoing Chinese multicentre study |
| [NCT01683123](https://clinicaltrials.gov/study/NCT01683123) | Phase 2 | Completed | 143 | Retrospective analysis of once-daily IV busulfan+fludarabine conditioning for HLA-identical sibling allo-HSCT in myeloid malignancies including MDS; generated key pharmacokinetic and outcome data |
| [NCT00863148](https://clinicaltrials.gov/study/NCT00863148) | Phase 2 | Completed | 30 | Clofarabine+IV Busulfan+Thymoglobulin as reduced-intensity conditioning prior to allo-HSCT in high-risk AML, MDS, or ALL; explored stronger anti-tumour RIC alternatives |
| [NCT03412409](https://clinicaltrials.gov/study/NCT03412409) | Phase 2 | Recruiting | 50 | Busulfan-based RIC for elderly or high-comorbidity patients receiving haploidentical HSCT; addresses an unmet need in older MDS populations unsuitable for myeloablative conditioning |
| [NCT00691015](https://clinicaltrials.gov/study/NCT00691015) | Phase 2 | Completed | 48 | Evaluated Sirolimus+Tacrolimus+Thymoglobulin GVHD prophylaxis strategy in unrelated donor HSCT, with busulfan-based myeloablative conditioning as the preparative backbone |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [36702138](https://pubmed.ncbi.nlm.nih.gov/36702138/) | 2023 | Phase 3 RCT | *Lancet Haematology* | G-CSF+decitabine+Bu-Cy significantly reduced relapse vs Bu-Cy alone in MDS-RAEB and secondary AML undergoing allo-HSCT, without increasing non-relapse mortality |
| [31606445](https://pubmed.ncbi.nlm.nih.gov/31606445/) | 2020 | Phase 3 RCT | *Lancet Haematology* | MC-FludT.14/L trial (n=476): treosulfan+Flu non-inferior to busulfan+Flu in older/comorbid AML and MDS patients; formally established busulfan/fludarabine as the reference standard |
| [35617104](https://pubmed.ncbi.nlm.nih.gov/35617104/) | 2022 | RCT Final Analysis | *Am J Hematology* | Final analysis of the above 476-patient Phase 3 trial confirming durable non-inferiority of treosulfan vs reduced-intensity busulfan in AML/MDS allo-HCT |
| [38648898](https://pubmed.ncbi.nlm.nih.gov/38648898/) | 2024 | Prospective Comparative | *Transplant Cell Ther* | Single-centre propensity score-matched cohort of 138 MDS patients directly comparing treosulfan vs busulfan-based conditioning outcomes at a Canadian transplant centre |
| [40079242](https://pubmed.ncbi.nlm.nih.gov/40079242/) | 2025 | Systematic Review | *Am J Hematology* | Contemporary review of allo-HCT for MDS and myelofibrosis; covers genomic risk stratification, optimal conditioning intensity selection, and personalised patient management |
| [28380315](https://pubmed.ncbi.nlm.nih.gov/28380315/) | 2017 | Phase 3 RCT | *J Clin Oncology* | BMT CTN Phase 3 trial comparing myeloablative (including busulfan-based) vs reduced-intensity conditioning in AML/MDS; pivotal comparative effectiveness and survival data |
| [37579918](https://pubmed.ncbi.nlm.nih.gov/37579918/) | 2023 | Prospective Phase 2 | *Transplant Cell Ther* | Myeloablative Bu+Flu with in vivo T-cell depletion demonstrated safe and effective conditioning for AML/MDS patients without requiring an arbitrary upper age limit |
| [33471943](https://pubmed.ncbi.nlm.nih.gov/33471943/) | 2021 | Retrospective Cohort | *Cancer* | Fractionated myeloablative IV busulfan safely administered to older patients showed superior event-free survival vs lower-dose (RIC) regimens in AML/MDS |
| [33425740](https://pubmed.ncbi.nlm.nih.gov/33425740/) | 2020 | Meta-Analysis | *Frontiers in Oncology* | Systematic review and meta-analysis of treosulfan vs busulfan-based conditioning for MDS/AML allo-HCT across multiple studies; quantified relapse and toxicity tradeoffs |
| [34489555](https://pubmed.ncbi.nlm.nih.gov/34489555/) | 2021 | Retrospective Cohort | *Bone Marrow Transplantation* | Japanese nationwide registry analysis (2006–2018) comparing Flu/Bu4 vs Bu4/Cy as myeloablative conditioning specifically in MDS patients undergoing allo-HSCT |

---

## India Market Information

Busulfan is currently **not marketed in India** and holds no product registrations with the CDSCO. No licensing data is available for the Indian market. Institutions requiring busulfan for clinical use would need to pursue individual import authorisation or a compassionate-use pathway through CDSCO before this drug can be deployed in an Indian centre.

---

## Cytotoxicity

Busulfan is a cytotoxic alkylating agent (bifunctional alkylsulfonate). Its original and predicted indications are both haematological in nature, its mechanism of action is myeloablative, and it belongs to the alkylating agent class of conventional cytotoxics. This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Bifunctional alkylating agent (alkylsulfonate class) |
| Myelosuppression Risk | **Very High** — Profound pancytopenia is the intended therapeutic outcome (myeloablation); daily CBC monitoring is mandatory throughout the conditioning period |
| Emetogenicity Classification | Low to Moderate (oral); IV formulation warrants scheduled antiemetic prophylaxis per institutional protocol |
| Monitoring Items | CBC with differential (daily during conditioning), liver function tests (risk of hepatic veno-occlusive disease / sinusoidal obstruction syndrome), renal function, busulfan plasma concentration (therapeutic drug monitoring with AUC targeting is standard of care), neurological status (seizure prophylaxis with benzodiazepines is routine) |
| Handling Protection | Must follow cytotoxic drug handling regulations; IV formulation requires closed-system drug transfer devices (CSTDs) and appropriate personal protective equipment throughout preparation and administration |

---

## Safety Considerations

**Drug Interactions** (228 total interactions identified; clinically significant selections listed below):

| Interacting Drug | Severity | Clinical Note |
|----------------|----------|---------------|
| Metronidazole | **Major** | May inhibit busulfan metabolism, substantially increasing plasma exposure and toxicity risk; concurrent use should be avoided if possible |
| Aprepitant | Moderate | NK1 antagonist antiemetic may alter busulfan pharmacokinetics via CYP3A4 modulation; consider substituting with a non-CYP3A4-interacting antiemetic during busulfan dosing |
| Miconazole | Moderate | Azole antifungal may elevate busulfan plasma levels through enzyme inhibition; alternative antifungal agents should be considered |
| Levofloxacin | Minor | Minor pharmacokinetic interaction; routine monitoring sufficient if concurrent use is clinically necessary |

Interactions of currently uncertain severity have also been identified with agents commonly co-administered in the peri-transplant setting, including proton pump inhibitors (Pantoprazole, Omeprazole, Lansoprazole), antiemetics (Ondansetron, Granisetron, Metoclopramide), corticosteroids (Prednisone, Hydrocortisone, Prednisolone, Dexamethasone), opioids (Morphine), antifungals (Amphotericin B), and osmotic agents (Mannitol). Given the high density of polypharmacy in the HSCT setting, a formal pharmacist-led medication review and busulfan therapeutic drug monitoring are strongly recommended to manage cumulative interaction risk.

For complete prescribing information including package insert warnings and contraindications, please refer to the current US FDA or EMA approved labelling, as India-specific regulatory labelling is not yet available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Busulfan holds Level 1 evidence (L1) for use in MDS allo-HSCT conditioning, supported by at least two completed Phase 3 randomised controlled trials published in *The Lancet Haematology* (2020, 2023) with direct MDS patient populations, alongside numerous Phase 2 studies and a robust body of retrospective and registry data. The TxGNN prediction formally validates an application already recognised in international transplant guidelines, making this a regulatory and logistical challenge rather than a scientific one.

**To proceed, the following is needed:**
- Obtain CDSCO import authorisation or establish a compassionate-use registration pathway before clinical deployment in India
- Retrieve and review the full prescribing information (US FDA Busulfex® or equivalent) for complete warnings, contraindications, and dose-adjustment guidance in hepatic/renal impairment
- Establish busulfan therapeutic drug monitoring (TDM) capability at the treating centre — plasma AUC-guided dosing (targeting 900–1350 µmol·min/L per dose) is the current standard of care and reduces both under-dosing (graft failure risk) and over-dosing (toxicity risk)
- Develop an institutional drug interaction management protocol, with particular attention to the **Major** Metronidazole interaction and Moderate interactions with azole antifungals commonly used for prophylaxis
- Define the target MDS patient subpopulation for the institutional transplant protocol: disease risk score (IPSS-R), donor source (matched related, matched unrelated, or haploidentical), and conditioning intensity (myeloablative vs reduced-intensity) based on patient age and comorbidity burden
- Consider enrolling patients in ongoing international trials (e.g., NCT05453552, NCT03412409) to generate India-specific outcome data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

