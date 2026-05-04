---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: From Taxane Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Docetaxel (DrugBank DB01248) is a globally established taxane-class cytotoxic chemotherapy agent used across multiple solid tumors, including breast, lung, and prostate cancer.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma** with a score of **99.90%**, supported by **multiple completed Phase 3 RCTs** and **20 publications** in the literature.
Docetaxel is currently not registered in India, making this evaluation a critical step toward addressing a significant unmet clinical need.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in India (globally used for multiple solid tumors including breast, lung, and prostate cancer) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Docetaxel is a semisynthetic taxane derived from the European yew tree (*Taxus baccata*). Detailed mechanism of action data is not available in the current database (marked as Data Gap); however, from the published scientific literature, docetaxel is well-established to bind to the N-terminal taxane-binding domain of β-tubulin, promoting microtubule polymerization and inhibiting depolymerization. This leads to mitotic arrest at the G2/M phase and subsequent induction of apoptosis. Its mechanism is fundamentally distinct from other cytotoxics such as vinca alkaloids, which destabilize microtubules.

Breast cancer cells—particularly HER2-positive and triple-negative subtypes (TNBC)—exhibit high proliferative rates and are particularly susceptible to agents that disrupt mitotic spindle assembly. In HER2-positive disease, trastuzumab and docetaxel demonstrate synergistic activity, partly because HER2 downstream signaling suppresses taxane-resistance pathways (e.g., Bcl-2 upregulation). This dual-target rationale has been validated across multiple regimens including TCH (Docetaxel + Carboplatin + Herceptin) and AC→T schedules.

The TxGNN knowledge-graph prediction of 99.90% for this indication is strongly corroborated by one of the most extensive clinical evidence bases in oncology. Multiple large completed Phase 3 RCTs—including trials of over 2,700 patients—have established docetaxel-containing regimens (TAC, TC, EC→T, FEC→T) as standard-of-care in both early-stage (adjuvant and neoadjuvant) and metastatic breast cancer. This is less a classical "repurposing" scenario and more a formal evidence validation for India regulatory consideration.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003519](https://clinicaltrials.gov/study/NCT00003519) | Phase 3 | Completed | 2,778 | Adriamycin/Taxotere vs Adriamycin/Cytoxan for adjuvant treatment of node-positive or high-risk node-negative breast cancer; one of the largest Docetaxel adjuvant trials |
| [NCT00129935](https://clinicaltrials.gov/study/NCT00129935) | Phase 3 | Completed | 1,384 | Prospective RCT comparing EC→Docetaxel vs ET→Capecitabine as adjuvant chemotherapy for HER2-negative, node-positive breast cancer; head-to-head efficacy and safety evaluation |
| [NCT00288002](https://clinicaltrials.gov/study/NCT00288002) | Phase 3 | Completed | 1,500 | Capecitabine concurrent or sequential with EC-Docetaxel ± trastuzumab as neoadjuvant treatment; assessed pathologic complete response rates |
| [NCT01354522](https://clinicaltrials.gov/study/NCT01354522) | Phase 3 | Completed | 204 | TAC (Docetaxel+Doxorubicin+Cyclophosphamide) vs TCX (Docetaxel+Cyclophosphamide+Capecitabine) as adjuvant for high-risk HER2-negative breast cancer |
| [NCT00963729](https://clinicaltrials.gov/study/NCT00963729) | Phase 3 | Completed | 756 | Neoadjuvant combination chemotherapy (Docetaxel-based) vs letrozole endocrine therapy in postmenopausal primary breast cancer |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | Completed | 263 | Docetaxel+Trastuzumab vs Docetaxel+Carboplatin+Trastuzumab (TCH) as first-line for HER2-positive advanced breast cancer; established TCH as standard regimen |
| [NCT02402712](https://clinicaltrials.gov/study/NCT02402712) | Phase 3 | Completed | 418 | Herceptin SC + Perjeta + Docetaxel in HER2-positive metastatic/locally recurrent breast cancer; safety and tolerability of subcutaneous trastuzumab combination |
| [NCT00005963](https://clinicaltrials.gov/study/NCT00005963) | Phase 2 | Completed | 53 | Docetaxel + Carboplatin as first-line therapy for metastatic breast cancer; evaluated objective response rate and toxicity profile |
| [NCT00003953](https://clinicaltrials.gov/study/NCT00003953) | Phase 2 | Completed | 39 | Preoperative dose-dense sequential Doxorubicin → Docetaxel for Stage II–IIIB breast cancer; assessed pathologic response and feasibility |
| [NCT02400567](https://clinicaltrials.gov/study/NCT02400567) | Phase 2 | Completed | 125 | Randomized trial of FEC→Docetaxel vs Letrozole+Palbociclib as neoadjuvant treatment for PAM50-defined luminal breast cancer in postmenopausal women |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | ABC Trials (USOR 06-090, NSABP B-46-I, B-49): TC6 vs TaxAC adjuvant regimens in early breast cancer; TaxAC demonstrated superior outcomes in certain subgroups |
| [11481357](https://pubmed.ncbi.nlm.nih.gov/11481357/) | 2001 | RCT | J Clin Oncol | Dose-dense Doxorubicin+Docetaxel ± Tamoxifen preoperative therapy in operable breast cancer; pathologic response rate and G-CSF support assessed |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Prospective Cohort | Breast Cancer (Tokyo) | Docetaxel+Cyclophosphamide+Trastuzumab (HER-TC) as neoadjuvant chemotherapy for HER2-positive breast cancer; pCR rates stratified by hormone receptor status |
| [19755993](https://pubmed.ncbi.nlm.nih.gov/19755993/) | 2009 | Cohort/Biomarker | Br J Cancer | Gene expression profiling to identify predictive markers of pCR to trastuzumab-docetaxel-based neoadjuvant treatment in HER2-positive breast cancer |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Prospective Phase II | Cancer | TEX regimen (Capecitabine + Docetaxel + Epirubicin) as first-line for locally advanced/metastatic breast cancer; objective response rate 68%, manageable toxicity |
| [15074734](https://pubmed.ncbi.nlm.nih.gov/15074734/) | 2004 | Phase II | Clin Oncol | Trastuzumab + Docetaxel for HER2-overexpressing metastatic breast cancer at an Indian cancer centre; toxicity profile and clinical effectiveness in Indian patients |
| [15858439](https://pubmed.ncbi.nlm.nih.gov/15858439/) | 2005 | Phase II | Breast Cancer (Tokyo) | Interim analysis of CEF followed by Docetaxel as neoadjuvant chemotherapy (JBCRG trial); clinical response and safety in 79 patients |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Review | J Clin Oncol | Landmark comprehensive review of Docetaxel's preclinical pharmacology, mechanism of action, and early clinical profile across solid tumors |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | Comparative assessment of paclitaxel and docetaxel in breast and ovarian cancer; efficacy evidence and licensing status at that time |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Cohort | Anti-Cancer Drugs | Retrospective analysis of adjuvant docetaxel-based chemotherapy and breast cancer-related lymphedema; fluid retention as a potential contributing mechanism |

---

## India Market Information

Docetaxel currently has **no registered products** in India's drug regulatory system. There are no marketing authorization records to display.

---

## Cytotoxicity

Docetaxel is an antineoplastic taxane. This section applies as docetaxel is a conventional cytotoxic chemotherapy agent.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (microtubule-stabilizing agent) |
| Myelosuppression Risk | **High** — Neutropenia is the principal dose-limiting toxicity; febrile neutropenia incidence is significant, particularly with TAC regimen (up to 25% without G-CSF prophylaxis); thrombocytopenia and anemia also observed |
| Emetogenicity Classification | Low to moderate (lower than cisplatin-based regimens; antiemetic prophylaxis still recommended) |
| Monitoring Items | CBC with differential (before each cycle and as clinically indicated), hepatic function (AST, ALT, alkaline phosphatase, bilirubin — dose reduction required if elevated), renal function, fluid retention assessment (body weight, peripheral edema) |
| Handling Protection | Must be handled strictly per cytotoxic drug handling regulations; appropriate PPE (gloves, gown, eye protection) required during preparation and administration; spill management protocol mandatory |

---

## Safety Considerations

**Drug Interactions** (569 total known interactions; key interactions listed below):

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Clarithromycin | **Major** | Strong CYP3A4 inhibitor; significantly increases docetaxel plasma exposure and toxicity risk — avoid concurrent use or dose-adjust carefully |
| Aprepitant | Moderate | Moderate CYP3A4 inhibitor; may increase docetaxel AUC — monitor for enhanced toxicity when used as antiemetic |
| Metronidazole | Moderate | CYP3A4 inhibition potential; monitor docetaxel toxicity if co-administered |
| Cimetidine | Moderate | CYP3A4 inhibition; may elevate docetaxel levels — prefer alternative H2 blockers |
| Miconazole | Moderate | Systemic azole antifungal with CYP3A4 inhibitory activity; monitor toxicity closely |
| Rosuvastatin | Moderate | Possible pharmacokinetic interaction; monitor for statin-related adverse effects |
| Simvastatin | Moderate | CYP3A4 substrate; combination may increase myopathy/rhabdomyolysis risk — consider switching to a non-CYP3A4-metabolized statin |
| Rolapitant | Moderate | NK1 receptor antagonist used for CINV prophylaxis; interaction monitoring recommended |
| Eliglustat | Moderate | CYP2D6/CYP3A4 substrate/inhibitor interaction; monitor for pharmacokinetic changes |
| Tinidazole | Moderate | Potential CYP3A4-mediated interaction; monitor clinical status |
| Dexamethasone | Minor | Standard premedication for docetaxel (reduces hypersensitivity reactions and fluid retention); this interaction is generally clinically beneficial |
| Prednisolone / Prednisone | Minor | Concurrent corticosteroid use is common as part of supportive care; monitor for immunosuppression |
| Levofloxacin | Minor | Monitor for additive QTc effects in high-risk patients |

Please refer to the full prescribing information for comprehensive contraindications and warnings. CDSCO-approved package insert data is not yet available for this drug in the Indian regulatory database.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Docetaxel has the strongest possible evidence level (L1) for female breast carcinoma, supported by numerous completed Phase 3 RCTs across adjuvant, neoadjuvant, and metastatic settings, as well as FDA, EMA, and multiple other regulatory approvals worldwide. Its absence from the Indian market represents a critical unmet clinical need, particularly given that breast cancer is the leading cancer in Indian women. The TxGNN score of 99.90% further validates what global clinical practice has confirmed for three decades.

**To proceed, the following is needed:**
- File a New Drug Application (NDA) or Abbreviated New Drug Application (ANDA) with CDSCO for Indian market authorization
- Supplement the DrugBank mechanism of action data gap (DG002) to support dossier completeness
- Obtain and localize the full prescribing information (PI/package insert) to meet CDSCO format requirements, addressing the TFDA PI data gap (DG001)
- Establish a pharmacovigilance and risk management plan in accordance with Indian Schedule Y requirements
- Develop a mandatory monitoring protocol: CBC with differential before each cycle, hepatic function panel, fluid retention assessment, and febrile neutropenia management guidelines
- Evaluate G-CSF primary prophylaxis policy for high-risk regimens (e.g., TAC) per ASCO/NCCN/Indian oncology guidelines
- Assess local manufacturing or import pathway for reliable supply chain; consider cold-chain logistics for lyophilized formulations
- Special population considerations: validate dose adjustment protocols for hepatic impairment (common in Indian patients with tuberculosis or hepatitis B co-morbidities) in the dossier
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

