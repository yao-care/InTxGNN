---
layout: default
title: Cytarabine
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 9
---

# Cytarabine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Cytarabine: From Acute Myeloid Leukemia to Small Cell Lung Carcinoma

## One-Sentence Summary

Cytarabine (Ara-C) is a pyrimidine antimetabolite classically used to treat acute leukemias (AML/ALL); a formal Taiwan/India regulatory indication text is not available in this evidence pack (drug is currently **not marketed**, 0 registrations).
The TxGNN model predicts it may be effective for **Small Cell Lung Carcinoma**, with **3 clinical trials** and **20 publications** currently associated with this direction — though the registered trials test it only indirectly, while historical (1979–1990) small non-randomized studies provide the more direct signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute Myeloid Leukemia / Acute Lymphocytic Leukemia (based on general pharmacological knowledge; no Taiwan/India license record exists in this evidence pack) |
| Predicted New Indication | Small Cell Lung Carcinoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L3 (uncontrolled/non-randomized human Phase II studies; no RCT of cytarabine specifically in SCLC identified) |
| India Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, cytarabine is a cytidine (pyrimidine nucleoside) analog that is phosphorylated intracellularly to ara-CTP, which competitively inhibits DNA polymerase and is misincorporated into replicating DNA, halting synthesis in S-phase cells. This gives it broad cytotoxic activity against rapidly dividing malignant cells, which is why it has historically been explored beyond leukemia in other rapidly proliferating tumors.

Small cell lung carcinoma is one of the most rapidly proliferating solid tumors, with a high growth fraction similar in principle to acute leukemia — the pharmacological rationale that supports cytarabine's efficacy in leukemia (S-phase-specific cytotoxicity against fast-dividing cells) plausibly extends to SCLC. This is reflected in the literature: several combination regimens (cytarabine + cyclophosphamide/adriamycin, cytarabine + etoposide, cytarabine + cisplatin) were tested in SCLC and NSCLC as early as the late 1970s–1990s, and cytarabine remains a recognized agent for intrathecal chemotherapy of leptomeningeal metastases arising from lung cancer.

However, it is important to note that the three registered clinical trials in this evidence pack do not directly test cytarabine as the investigational agent for SCLC — they primarily study pemetrexed- or platinum-based regimens, with cytarabine mentioned only as background/alternative intrathecal therapy. The more direct supporting evidence comes from older, small, non-randomized Phase II literature rather than from confirmatory randomized trials.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863512](https://clinicaltrials.gov/study/NCT00863512) | Phase 3 | Terminated | 34 | Adjuvant chemotherapy vs. observation after surgery in early-stage NSCLC (regimen used vinorelbine/cisplatin/docetaxel/gemcitabine/pemetrexed, not cytarabine) |
| [NCT03507244](https://clinicaltrials.gov/study/NCT03507244) | Phase 1/2 | Completed | 34 | Intrathecal pemetrexed + concurrent radiotherapy for leptomeningeal metastasis from solid tumors (cytarabine cited as a comparator intrathecal agent, not the study drug) |
| [NCT03101579](https://clinicaltrials.gov/study/NCT03101579) | Phase 1 | Completed | 13 | Intrathecal pemetrexed for recurrent leptomeningeal metastasis from NSCLC; notes cytarabine as a commonly used intrathecal chemotherapy drug for this setting |

*Note: none of the above trials use cytarabine as the primary investigational agent for small cell lung carcinoma — relevance to this specific indication is indirect.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9363869](https://pubmed.ncbi.nlm.nih.gov/9363869/) | 1997 | RCT | J Clin Oncol | CALGB randomized trial of chemotherapy + radiotherapy ± warfarin in limited-stage SCLC; chemo backbone included cytarabine-containing regimens |
| [6095640](https://pubmed.ncbi.nlm.nih.gov/6095640/) | 1984 | Phase II (uncontrolled) | Am J Clin Oncol | Continuous-infusion Ara-C alone (no responses, severe toxicity) and Ara-C added to CAV in extensive-stage SCLC |
| [2841844](https://pubmed.ncbi.nlm.nih.gov/2841844/) | 1988 | Phase II (uncontrolled) | Am J Clin Oncol | Etoposide + infusional Ara-C in relapsed SCLC refractory to combination chemotherapy |
| [232239](https://pubmed.ncbi.nlm.nih.gov/232239/) | 1979 | Case series | Med Pediatr Oncol | Cyclophosphamide + Adriamycin + cytosine arabinoside plus thoracic/whole-brain irradiation in untreated SCLC |
| [6264785](https://pubmed.ncbi.nlm.nih.gov/6264785/) | 1981 | Cohort study | Am J Med | Intensive chemotherapy (incl. Ara-C-based regimens) for meningeal carcinomatosis in SCLC; 78% response rate |
| [2157307](https://pubmed.ncbi.nlm.nih.gov/2157307/) | 1990 | Phase II | Tumori | Cisplatin + vindesine + cytarabine in advanced NSCLC (18% response rate) |
| [2156598](https://pubmed.ncbi.nlm.nih.gov/2156598/) | 1990 | Phase II | Cancer | High-dose cytarabine + cisplatin in chemo-naive advanced NSCLC (14% response; Grade III/IV myelosuppression in 46%) |
| [2820740](https://pubmed.ncbi.nlm.nih.gov/2820740/) | 1987 | Pilot study | Eur J Cancer Clin Oncol | Cisplatin + cytarabine combination in advanced NSCLC |
| [28223673](https://pubmed.ncbi.nlm.nih.gov/28223673/) | 2017 | Case report | Gan To Kagaku Ryoho | Multidisciplinary treatment (incl. intrathecal chemotherapy) of meningeal carcinomatosis from SCLC |
| [348088](https://pubmed.ncbi.nlm.nih.gov/348088/) | 1978 | Review (mechanism) | Antibiot Chemother | Review of Ara-C analogs and cytidine deaminase-mediated deactivation, relevant to mechanistic rationale |

## India Market Information

Cytarabine is currently **not marketed** under this evidence pack's regulatory registry (`market_status: 未上市`, `total_licenses: 0`). No license or product registration records are available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (pyrimidine/nucleoside antimetabolite class) |
| Myelosuppression Risk | High (dose-limiting toxicity; neutropenia, thrombocytopenia, and anemia are well-documented, especially with high-dose regimens — general pharmacological knowledge, not sourced from this evidence pack) |
| Emetogenicity Classification | Moderate to High, dose-dependent (high-dose regimens are more emetogenic — general pharmacological knowledge) |
| Monitoring Items | CBC with differential and platelets, liver and renal function; for high-dose regimens also neurological (cerebellar) exam and ocular exam (conjunctivitis/keratitis) |
| Handling Protection | Yes — must be handled under standard cytotoxic/hazardous drug handling protocols (PPE, closed-system transfer devices) during preparation and administration |

*The above cytotoxicity profile reflects general pharmacological knowledge, since no DrugBank toxicity data was returned in this evidence pack.*

## Safety Considerations

- **Drug Interactions**: The DDI query returned 365 total interactions. Among the sampled results, the only interaction flagged at a defined severity level was with **Naltrexone (Moderate)**; **Levofloxacin** was flagged as Minor. The remaining sampled interactions (e.g., Pantoprazole, Metformin, Omeprazole, Morphine, Vancomycin) were listed with an "Unknown" severity level and require further characterization.

*Key warnings and contraindications from the TFDA-equivalent label are not available (Blocking data gap DG001) — refer to the official package insert once obtained.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The drug is not currently marketed under this jurisdiction (0 registrations) and TFDA-equivalent label safety data is a **Blocking** data gap (DG001), preventing initial safety evaluation (S1). While TxGNN's prediction score is high and there is plausible mechanistic and historical literature support for cytarabine in SCLC, the registered clinical trials in this pack do not directly test cytarabine for this indication, and the strongest direct evidence consists of small, non-randomized Phase II studies from 1979–1990.

**To proceed, the following is needed:**
- TFDA/local label data: key warnings, contraindications (DG001, Blocking)
- Confirmed mechanism-of-action documentation (DG002, High)
- Modern trial or real-world evidence directly evaluating cytarabine (not just cytarabine-adjacent regimens) in SCLC
- Route compatibility assessment for the proposed use (IV vs. intrathecal) against required administration routes for SCLC
- A defined safety monitoring plan given the high myelosuppression risk of this cytotoxic agent
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

