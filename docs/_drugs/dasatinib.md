---
layout: default
title: Dasatinib
parent: 僅模型預測 (L5)
nav_order: 158
evidence_level: L5
indication_count: 10
---

# Dasatinib
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

# Dasatinib: From Myeloid Leukemia to Ewing Sarcoma

## One-Sentence Summary

Dasatinib (Sprycel®) is a second-generation BCR-ABL/Src dual tyrosine kinase inhibitor, globally established for the treatment of Chronic Myeloid Leukemia (CML) and Philadelphia chromosome-positive Acute Lymphoblastic Leukemia (Ph+ ALL), but currently not registered in India.
The TxGNN model predicts it may be effective for **Ewing Sarcoma**, with **3 clinical trials** and **9 publications** currently supporting this direction.
The mechanistic rationale is grounded in Dasatinib's potent inhibition of Src family kinases (SFKs), which are recognized drivers of invasion and metastasis in Ewing sarcoma cells — though single-agent clinical translation has yet to be fully established.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Myeloid Leukemia (CML) / Ph+ Acute Lymphoblastic Leukemia (globally approved; not registered in India) |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known information, Dasatinib is a small-molecule, orally bioavailable inhibitor of multiple tyrosine kinases — prominently BCR-ABL, Src family kinases (SFKs), c-KIT, and PDGFR-β. Its established efficacy in Ph+ leukemia is primarily driven by BCR-ABL inhibition, but its broad SFK activity represents a distinct and pharmacologically relevant asset that extends its potential into solid tumor settings.

Ewing sarcoma is a highly aggressive bone and soft-tissue malignancy predominantly affecting children and young adults, with dismal outcomes in the metastatic and relapsed setting. Mechanistic studies have demonstrated that Ewing sarcoma cells highly express SFKs, and the Src/FAK signaling axis is a critical driver of tumor invasion, invadopodia formation, and metastatic progression (PMID 27566104, 31521948). Under microenvironmental stress conditions, Src activation amplifies invasive behavior — a process that Dasatinib directly targets through dual Src/ABL inhibition (PMID 17363602, 18202781). In vitro work confirmed antiproliferative and antimigratory activity of Dasatinib in Ewing sarcoma cell lines.

The completed large Phase 2 basket trial (NCT00464620, n=366) enrolled patients with advanced sarcomas including an Ewing sarcoma subgroup, providing the primary clinical-level anchor for this prediction. However, a key limitation has emerged: Src inhibition by Dasatinib as a single agent has not produced durable clinical responses in Ewing sarcoma, suggesting that combination approaches — pairing Dasatinib with cytotoxic chemotherapy or FAK inhibitors — may be necessary for meaningful efficacy. The mechanistic rationale remains coherent, but clinical translation requires further refinement.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464620](https://clinicaltrials.gov/study/NCT00464620) | Phase 2 | Completed | 366 | Large basket trial examining response rate and 6-month PFS in advanced sarcomas treated with dasatinib; includes Ewing sarcoma subgroup — primary L2 clinical evidence; subgroup-specific efficacy data requires review of original publication |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Pediatric trial of dasatinib combined with ifosfamide, carboplatin, and etoposide in Ewing sarcoma and other pediatric tumors; terminated early (n=7), provides preliminary safety signals only; termination reason warrants clarification |
| [NCT06500819](https://clinicaltrials.gov/study/NCT06500819) | Phase 1 | Recruiting | 41 | B7-H3 CAR-T cell therapy in relapsed/refractory solid tumors expressing B7-H3 (not a dasatinib trial); indirect relevance — dasatinib is known to enhance CAR-T function but is not the primary investigational agent in this study |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [17363602](https://pubmed.ncbi.nlm.nih.gov/17363602/) | 2007 | In vitro | Cancer Research | Dasatinib inhibits migration and invasion in diverse human sarcoma cell lines; bone sarcoma cells dependent on Src kinase for survival undergo apoptosis — foundational preclinical rationale |
| [18202781](https://pubmed.ncbi.nlm.nih.gov/18202781/) | 2008 | In vitro | Oncology Reports | Dasatinib demonstrates antiproliferative and antimigratory activity in Ewing sarcoma cell lines via c-KIT and PDGFR inhibition — direct in vitro evidence in ES cells |
| [27566104](https://pubmed.ncbi.nlm.nih.gov/27566104/) | 2016 | Preclinical | Neoplasia | Microenvironmental stress induces Src-dependent invadopodia activation and cell migration in Ewing sarcoma; establishes mechanistic rationale for Src targeting in invasive disease |
| [31521948](https://pubmed.ncbi.nlm.nih.gov/31521948/) | 2019 | Preclinical | Neoplasia | Tenascin C and Src cooperate to drive invadopodia formation in Ewing sarcoma; further validates Src/FAK axis as a actionable therapeutic node |
| [35655525](https://pubmed.ncbi.nlm.nih.gov/35655525/) | 2022 | Translational | Sarcoma | FAK-Src complex targeted across DSRCT, Ewing sarcoma, and rhabdomyosarcoma; dasatinib failed as single agent in Phase 2, supporting the need for combination strategies |
| [26170970](https://pubmed.ncbi.nlm.nih.gov/26170970/) | 2015 | Review | Oncology Letters | Comprehensive review of Src signaling in sarcoma; discusses Src as a potential drug target, including in Ewing sarcoma, and summarizes therapeutic feasibility |
| [29776413](https://pubmed.ncbi.nlm.nih.gov/29776413/) | 2018 | In vitro/Animal | Cell Commun Signal | CXCR4 antagonist study in Ewing sarcoma activating receptor tyrosine kinase signaling — contextual evidence for combinatorial targeting strategies in ES microenvironment |

---

## India Market Information

Dasatinib is **not currently registered or marketed in India**. No CDSCO license records are available. There are 0 approved registrations.

For reference, Dasatinib is globally approved under the brand name **Sprycel®** (Bristol-Myers Squibb) in the US (FDA), Europe (EMA), and multiple other markets for:
- Newly diagnosed Ph+ CML in chronic phase (first-line)
- CML in chronic, accelerated, or blast phase resistant/intolerant to prior therapy including imatinib (second-line)
- Ph+ Acute Lymphoblastic Leukemia (ALL) resistant or intolerant to prior therapy

Market entry into India would require a new drug application to CDSCO and may be supported by referencing existing FDA/EMA approvals under the accelerated pathway for drugs approved in ICH reference countries.

---

## Cytotoxicity

Dasatinib is an antineoplastic targeted therapy agent used in hematologic malignancies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Tyrosine Kinase Inhibitor (BCR-ABL/Src class; second-generation TKI) |
| Myelosuppression Risk | Moderate to High — neutropenia, thrombocytopenia, and anemia are common, dose-dependent adverse effects; CBC monitoring is essential |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | Complete blood count (CBC with differential), liver function tests (ALT/AST), renal function, pulmonary function (pleural effusion is a class-specific risk), ECG (QTc interval), and body weight/fluid status |
| Handling Protection | Standard oral cytotoxic precautions apply; intact tablets should not be crushed — if manipulation is required (e.g., pediatric dosing), cytotoxic PPE is recommended per institutional guidelines |

---

## Safety Considerations

**Drug Interactions**: Dasatinib has 691 documented drug-drug interactions in the DDInter database. Clinically significant interactions of immediate concern:

- **Major interactions**: Famotidine, Ranitidine, Cimetidine, Omeprazole, Rabeprazole — antacids, H₂-blockers, and proton pump inhibitors reduce gastric pH and substantially decrease dasatinib absorption; H₂-blockers should be separated by ≥2 hours, PPIs are generally contraindicated with dasatinib. Dexamethasone — CYP3A4 inducer that reduces dasatinib plasma levels; Acetylsalicylic acid — additive bleeding risk given dasatinib's platelet effects; Clarithromycin — strong CYP3A4 inhibitor that markedly increases dasatinib exposure and toxicity risk.
- **Moderate interactions**: Hydrocortisone, Budesonide, Aprepitant, Saxagliptin, Magnesium oxide, Aluminum hydroxide, Calcium carbonate, Loperamide, Bisacodyl, Polyethylene glycol with electrolytes, Castor oil.

> ⚠️ Formal package insert safety data (key warnings and contraindications from the CDSCO/TFDA label) is not available in this Evidence Pack and represents a **blocking data gap** for complete safety pre-screening. Please consult the current Sprycel® prescribing information for a full list of warnings, contraindications, and special population guidance prior to any clinical planning.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Dasatinib has a biologically coherent and well-supported mechanistic rationale for Ewing sarcoma through Src/FAK axis inhibition, anchored by multiple in vitro studies and one completed Phase 2 basket trial (n=366). However, single-agent Src inhibition has shown limited clinical activity in this subtype, indicating that combination approaches and patient selection biomarkers are prerequisites before this direction can advance to confirmatory development.

**To proceed, the following is needed:**
- Obtain and review full package insert (warnings, contraindications) — currently a **blocking data gap** before safety pre-screening can be completed
- Confirm Ewing sarcoma-specific subgroup efficacy and response rates from NCT00464620 primary publication
- Identify predictive biomarkers for Src-pathway dependency in individual Ewing sarcoma tumors (e.g., SFK expression levels, FAK phosphorylation status)
- Design combination trial strategy — evaluate synergy with standard-of-care chemotherapy (ifosfamide/etoposide backbone) or FAK inhibitors in preclinical models
- Establish pediatric-specific PK/PD and dosing data, given that Ewing sarcoma primarily affects adolescents and young adults
- Assess India regulatory pathway: file a new drug application with CDSCO referencing existing FDA/EMA approvals, given zero current registration status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

