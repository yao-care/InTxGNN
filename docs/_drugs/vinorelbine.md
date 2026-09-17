---
layout: default
title: Vinorelbine
parent: High Evidence (L1-L2)
nav_order: 883
evidence_level: L2
indication_count: 10
---

# Vinorelbine
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Vinorelbine: From Non-Small Cell Lung Cancer to Ewing Sarcoma

## One-Sentence Summary

Vinorelbine is a semi-synthetic vinca alkaloid chemotherapy agent, established globally as first-line/adjuvant therapy for non-small cell lung cancer (NSCLC) and metastatic breast cancer.
The TxGNN model predicts it may be effective for **Ewing Sarcoma**,
with **4 clinical trials** and **5 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Evidence Pack (India regulatory data shows 0 licenses on file); based on general pharmacological knowledge, vinorelbine's established indications are NSCLC and metastatic breast cancer |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack (Data Gap DG002). Based on general pharmacological knowledge, Vinorelbine belongs to the vinca alkaloid class of antineoplastic agents. Its efficacy in NSCLC and metastatic breast cancer has been well established through multiple Phase 3 trials (e.g., ANITA trial, PMID 16945766), and mechanistically it may be applicable to Ewing sarcoma.

Vinorelbine binds tubulin and inhibits microtubule polymerization, arresting tumor cells in mitosis (M phase) and inducing apoptosis. This antimitotic mechanism is not tumor-type specific — it is broadly cytotoxic to any highly proliferative malignancy. Ewing sarcoma is a small round blue cell tumor with a very high mitotic index, which is mechanistically consistent with vinca alkaloid sensitivity.

Supporting this link, vinorelbine (and related vinca alkaloids such as vincristine/vinblastine) already has a track record in pediatric refractory/relapsed sarcomas. A completed Phase II study (NCT00003234) tested vinorelbine specifically in children with recurrent or refractory malignancies including Ewing tumors, and a Phase II RCT (PMID 22633624, SFCE group) demonstrated good tolerability and efficacy of vinorelbine + low-dose cyclophosphamide in relapsed/refractory pediatric solid tumors, including the Ewing family of tumors — providing early, repeated clinical validation in this population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003234](https://clinicaltrials.gov/study/NCT00003234) | Phase 2 | Completed | 50 | Vinorelbine tested in children with recurrent/refractory malignancies (including Ewing sarcoma) |
| [NCT00180947](https://clinicaltrials.gov/study/NCT00180947) | Phase 2 | Unknown | 210 | Vinorelbine + cyclophosphamide in refractory/relapsed rhabdomyosarcoma, Ewing tumors, osteosarcoma, neuroblastoma, medulloblastoma |
| [NCT05999994](https://clinicaltrials.gov/study/NCT05999994) | Phase 2 | Recruiting | 105 | CAMPFIRE master protocol — common infrastructure for multiple pediatric oncology drug/disease-specific sub-studies |
| [NCT06451302](https://clinicaltrials.gov/study/NCT06451302) | N/A (Observational) | Active, not recruiting | 100 | Multicenter cohort study on risk-stratified treatment outcomes/safety in pediatric Ewing sarcoma (China) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Phase II / RCT | European Journal of Cancer | Vinorelbine + continuous low-dose oral cyclophosphamide in relapsed/refractory pediatric solid tumors — good tolerance and efficacy signal in the Ewing family of tumors and rhabdomyosarcoma |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Phase II | Cancer | Vinorelbine in previously treated advanced childhood sarcomas; activity demonstrated, including Ewing sarcoma cohort |
| [37637411](https://pubmed.ncbi.nlm.nih.gov/37637411/) | 2023 | Review | Frontiers in Pharmacology | Review of chemotherapeutic drug options for soft tissue sarcomas |
| [26260582](https://pubmed.ncbi.nlm.nih.gov/26260582/) | 2016 | Preclinical | International Journal of Cancer | Synergistic apoptosis induction by PLK1 inhibitor BI 6727 combined with microtubule-interfering agents (including vinorelbine) in Ewing sarcoma cell lines |
| [36451163](https://pubmed.ncbi.nlm.nih.gov/36451163/) | 2022 | Case Report | BMC Urology | Case report and literature review of extraosseous Ewing's sarcoma/pPNET of the kidney (background/diagnostic context, not a treatment trial) |

---

## India Market Information

Vinorelbine currently has no registered license or marketed product on file in India (0 licenses recorded; market status: Not Marketed).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Vinca alkaloid class — microtubule/tubulin polymerization inhibitor) |
| Myelosuppression Risk | High — neutropenia is the characteristic dose-limiting toxicity of vinorelbine (consistent with literature, e.g., PMID 9535205) |
| Emetogenicity Classification | Low to moderate (typical for vinca alkaloids) |
| Monitoring Items | CBC with differential (especially ANC), liver function, peripheral neuropathy assessment; vesicant — monitor injection site for extravasation |
| Handling Protection | Yes — vinorelbine is a vesicant cytotoxic agent and must be prepared/administered under standard hazardous/cytotoxic drug handling protocols |

---

## Safety Considerations

- **Drug Interactions**: 465 total interactions on file. Notable examples include:
  - **Major**: Clarithromycin
  - **Moderate**: Aprepitant, Dexamethasone, Metronidazole, Eliglustat, Miconazole, Rolapitant, Rosuvastatin, Simvastatin, Tinidazole, Glycerol phenylbutyrate
  - **Minor**: Levofloxacin

No package insert warnings or contraindications are currently on file (Data Gap DG001, Blocking) — please refer to the official package insert once available.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase II trial (NCT00003234) and a Phase II RCT (PMID 22633624) both directly evaluated vinorelbine in pediatric refractory/relapsed sarcoma populations including Ewing sarcoma, supporting L2-level evidence. However, no Ewing-sarcoma-specific confirmatory Phase 2/3 trial has been completed (NCT00180947 status is Unknown; CAMPFIRE is still recruiting), so guardrails are warranted before advancing further.

**To proceed, the following is needed:**
- TFDA/CDSCO package insert warnings and contraindications (Blocking data gap DG001) — required before S1 safety review
- Detailed mechanism of action documentation (DG002)
- Confirmation of India regulatory/import pathway, given 0 current licenses and "Not Marketed" status
- An Ewing-sarcoma-specific (rather than broad pediatric-refractory-tumor) confirmatory trial
- A pediatric-population-specific safety monitoring plan, given the target age range in the supporting trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

