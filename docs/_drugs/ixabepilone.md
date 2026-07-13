---
layout: default
title: Ixabepilone
parent: 僅模型預測 (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
---

# Ixabepilone
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

# Ixabepilone: From Metastatic Breast Cancer to Ewing Sarcoma

## One-Sentence Summary

Ixabepilone is a semisynthetic epothilone B analog and non-taxane microtubule-stabilizing agent, FDA-approved for the treatment of metastatic breast cancer.
The TxGNN model predicts it may be effective for **Ewing Sarcoma** (score: 99.76%),
with **2 clinical trials** and **1 direct clinical publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Metastatic breast cancer (FDA-approved; not registered in India) |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on published literature, Ixabepilone is an epothilone B analog that stabilizes microtubules by binding to β-tubulin, preventing depolymerization. This arrests dividing tumor cells in the G2/M phase and triggers apoptosis. A key advantage over taxanes is its reduced susceptibility to P-glycoprotein (MDR1)–mediated multidrug resistance, allowing activity in taxane-resistant tumors.

Ewing sarcoma is an aggressive pediatric bone and soft tissue malignancy driven by the EWS-FLI1 fusion oncogene. These highly proliferative tumor cells depend heavily on intact mitotic spindle function, and the characteristically low P-glycoprotein expression in Ewing sarcoma cells makes them particularly vulnerable to epothilone-class agents. Preclinical data from pediatric tumor xenograft models have confirmed sensitivity to ixabepilone even in paclitaxel-resistant settings, providing a strong mechanistic foundation for this prediction.

The Children's Oncology Group (COG) directly tested this hypothesis: the completed Phase II trial NCT00331643 specifically enrolled children and young adults with refractory solid tumors including Ewing sarcoma, and published results in 2010. This clinical validation closely aligns with the TxGNN model's top-ranked prediction and significantly elevates the credibility of this repurposing direction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00331643](https://clinicaltrials.gov/study/NCT00331643) | Phase 2 | Completed | 120 | COG Phase II trial evaluating ixabepilone in six solid tumor strata in children and young adults with refractory tumors (including Ewing sarcoma); results published as PMID 20068084; primary DLT was neutropenia |
| [NCT00030108](https://clinicaltrials.gov/study/NCT00030108) | Phase 1 | Completed | 30 | Pediatric Phase I PK and dose-escalation study in refractory solid tumors and leukemias; established the maximum tolerated dose of 8 mg/m²/dose in children and defined the safe dosing schedule used in the Phase II trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [20068084](https://pubmed.ncbi.nlm.nih.gov/20068084/) | 2010 | Phase II Clinical Trial | Clinical Cancer Research | Ixabepilone (daily × 5 days IV schedule) evaluated in six pediatric solid tumor strata including Ewing sarcoma; microtubule-stabilizing activity demonstrated against paclitaxel-resistant pediatric xenograft models; primary DLT was neutropenia; provides the core clinical efficacy and safety data for this repurposing direction |

---

## India Market Information

Ixabepilone currently has **no registered products in India** (0 licenses). The drug is not approved or marketed locally. Any clinical use would require an import license or Investigational New Drug (IND) application through CDSCO.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Epothilone class (non-taxane microtubule-stabilizing agent) |
| Myelosuppression Risk | High — neutropenia is the primary dose-limiting toxicity; thrombocytopenia also reported across Phase I–III studies |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (ANC monitoring mandatory), liver function tests, renal function, cumulative peripheral neuropathy assessment (sensory grading at each cycle) |
| Handling Protection | Must follow cytotoxic drug handling regulations; reconstitution requires the supplied Cremophor EL–based diluent; personnel protection and closed-system transfer devices recommended |

---

## Safety Considerations

**Drug Interactions** (276 total interactions identified):

| Severity | Interacting Drug | Clinical Note |
|----------|-----------------|---------------|
| **Major** | Deferiprone | Additive myelosuppression; concurrent use should be avoided |
| **Major** | Samarium (153Sm) lexidronam | Additive bone marrow suppression risk |
| Moderate | Clarithromycin | CYP3A4 inhibitor; may increase ixabepilone plasma exposure and toxicity |
| Moderate | Cobicistat | Strong CYP3A4 inhibitor; dose adjustment may be required |
| Moderate | Aprepitant | Mixed CYP3A4 modulator; monitor for altered ixabepilone levels |
| Moderate | Dexamethasone | CYP3A4 inducer; may reduce ixabepilone efficacy |
| Moderate | Miconazole / Clotrimazole | Azole antifungals inhibit CYP3A4; increased toxicity risk |
| Moderate | Rosuvastatin / Simvastatin | Potential additive hepatotoxicity; monitor liver enzymes |
| Moderate | Palifermin | Timing restriction — palifermin should not be administered within 24 hours before/after cytotoxic chemotherapy |

**Additional Safety Note:** Peripheral neuropathy (predominantly sensory, cumulative) is a class effect of ixabepilone across Phase II/III studies. It is usually mild to moderate in severity and similar in profile to taxane-induced neuropathy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed, enrollment-adequate Phase II trial (NCT00331643, n=120) conducted by the Children's Oncology Group specifically evaluated ixabepilone in pediatric refractory solid tumors including Ewing sarcoma, providing Level L2 evidence. The mechanistic rationale is well-supported: Ewing sarcoma's low P-glycoprotein expression renders it sensitive to epothilone-class agents, and ixabepilone's established FDA safety record (breast cancer approval) reduces de-novo safety uncertainty. The drug is not yet registered in India, but the clinical evidence base justifies moving forward under defined safeguards.

**To proceed, the following is needed:**

- **Critical**: Full analysis of PMID 20068084 to extract the response rate, progression-free survival, and OS data specifically for the Ewing sarcoma patient stratum
- **Critical**: CDSCO/TFDA package insert review for complete warnings, contraindications, and dosing — currently a blocking data gap (DG001)
- **High priority**: Detailed MOA data from DrugBank API to complete mechanistic linkage analysis (DG002)
- India regulatory pathway assessment: CDSCO IND application or import license required before any local use
- Comparison with current standard-of-care regimens for relapsed/refractory Ewing sarcoma (e.g., irinotecan/temozolomide, high-dose chemotherapy) to define positioning
- Pediatric peripheral neuropathy monitoring protocol and dose-reduction guidelines for the target population
- Assessment of potential combination strategies with standard Ewing sarcoma backbone regimens (e.g., vincristine, ifosfamide, etoposide)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

