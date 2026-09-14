---
layout: default
title: Topotecan
parent: 僅模型預測 (L5)
nav_order: 843
evidence_level: L5
indication_count: 10
---

# Topotecan
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

Using no additional skill — this is a direct content-generation task fully specified by the provided report template and Evidence Pack JSON, not a coding/architecture task requiring the skills system.

---

# Topotecan: From Cytotoxic Chemotherapy for Solid Tumors to Female Breast Carcinoma

## One-Sentence Summary

> Topotecan is a topoisomerase I inhibitor (camptothecin derivative) already established as a cytotoxic chemotherapy agent for various solid tumors; the evidence pack does not record its original TFDA/registered indication text.
> The TxGNN model predicts it may be effective for **Female Breast Carcinoma**,
> with **5 clinical trials** and **20 publications** currently available as supporting context, though most are small Phase I/II or preclinical studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in the current data pack (no TFDA license text or `original_indications` entries available — see data gap DG001/DG002) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal drug-label mechanism of action (MOA) data is not available for Topotecan. Based on the mechanistic evidence supplied with the prediction, Topotecan is a Topoisomerase I inhibitor that induces single-strand DNA breaks and replication fork collapse, producing a cytotoxic effect in highly proliferative tumor cells with high replication stress.

Breast carcinoma — particularly triple-negative (TNBC) or MYC-driven subtypes — has documented mechanistic evidence of vulnerability to Topo I inhibition through R-loop accumulation and synthetic lethality (PMID 37987734), which supports extending Topotecan's cytotoxic activity to this tumor type. As Topotecan is already an approved cytotoxic chemotherapy agent in other solid tumor settings, its systemic safety profile is well characterized, even though breast-cancer-specific efficacy data remain limited to older, small Phase II/pilot trials rather than confirmatory Phase III studies.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02282020](https://clinicaltrials.gov/study/NCT02282020) | Phase 3 | Completed | 266 | Olaparib vs. physician's choice chemotherapy in gBRCA-mutated ovarian cancer; Topotecan's role as trial-arm vs. background comparator agent unconfirmed (Grade B relevance). |
| [NCT04739800](https://clinicaltrials.gov/study/NCT04739800) | Phase 2 | Active, not recruiting | 120 | Durvalumab + olaparib + cediranib combinations in platinum-resistant ovarian/peritoneal/fallopian cancer; Topotecan appears as a possible backbone agent, not independently tested (Grade B). |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | N/A | Intensive-dose Topotecan + Ifosfamide/Mesna + Etoposide (TIME) followed by autologous stem cell rescue in metastatic breast cancer — direct treatment regimen evidence, but trial was terminated (Grade A relevance, weak completion). |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminated | 221 | Selinexor combined with multiple standard chemo/immunotherapy regimens (possibly including Topotecan) in advanced malignancies; low specificity, terminated (Grade C). |
| [NCT04279509](https://clinicaltrials.gov/study/NCT04279509) | N/A | Unknown status | 35 | Patient-derived organoid high-throughput drug screening (SCORE) for refractory solid tumors; translational/preclinical, not a direct efficacy trial (Grade C). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10362325](https://pubmed.ncbi.nlm.nih.gov/10362325/) | 1999 | Phase II trial | American Journal of Clinical Oncology | CALGB Phase II trial of Topotecan in previously treated advanced breast cancer; 47 evaluable patients — most direct clinical efficacy evidence available. |
| [9626200](https://pubmed.ncbi.nlm.nih.gov/9626200/) | 1998 | Phase II trial | J Clin Oncol | Multicenter Phase II trial of paclitaxel + Topotecan with G-CSF support in stage IV breast cancer; PK/toxicity correlation reported. |
| [9413954](https://pubmed.ncbi.nlm.nih.gov/9413954/) | 1997 | Phase II trial | British Journal of Cancer | Continuous infusional Topotecan in advanced breast cancer and NSCLC; no evidence of increased efficacy over standard dosing. |
| [11455218](https://pubmed.ncbi.nlm.nih.gov/11455218/) | 2001 | Pilot cohort study | Onkologie | Topotecan chemotherapy pilot study in breast cancer patients with brain metastases. |
| [40300683](https://pubmed.ncbi.nlm.nih.gov/40300683/) | 2025 | Preclinical | Int J Biol Macromolecules | TFDP1 identified as a therapeutic target for Topotecan in triple-negative breast cancer (TNBC), supporting senescence-suppression mechanism. |
| [37987734](https://pubmed.ncbi.nlm.nih.gov/37987734/) | 2023 | Preclinical/mechanistic | Cancer Research | Topo I inhibition in MYC-driven breast cancer cell lines promotes R-loop accumulation and synthetic lethality via CRISPR screen. |
| [9445630](https://pubmed.ncbi.nlm.nih.gov/9445630/) | 1997 | Review | Gynäkologisch-Geburtshilfliche Rundschau | Review of new cytotoxic agents (including Topotecan) in breast carcinoma therapy. |
| [26623560](https://pubmed.ncbi.nlm.nih.gov/26623560/) | 2015 | Preclinical | Oncotarget | Metronomic Topotecan + pazopanib combination shows potent efficacy in preclinical models of primary/metastatic TNBC. |
| [31408695](https://pubmed.ncbi.nlm.nih.gov/31408695/) | 2019 | Preclinical | Pharmacological Research | Daidzein enhances Topotecan's anticancer effect and reverses BCRP-mediated drug resistance in breast cancer cells. |
| [10472342](https://pubmed.ncbi.nlm.nih.gov/10472342/) | 1999 | Preclinical (xenograft) | Anticancer Research | Comparative efficacy of doxorubicin, cisplatin, irinotecan and Topotecan in colon, lung and breast carcinoma xenografts. |

---

## India Market Information

Topotecan is currently **not marketed** in India according to this evidence pack — 0 registrations/licenses are on record, and no authorization details, product names, or approved indication text are available.

---

## Cytotoxicity

Topotecan is a known cytotoxic antineoplastic agent (topoisomerase I inhibitor / camptothecin derivative class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic chemotherapy (Topoisomerase I inhibitor, camptothecin derivative) |
| Myelosuppression Risk | High — dose-limiting toxicity is typically neutropenia/thrombocytopenia. Supporting evidence from a related Topotecan trial (PMID 8617580, germ cell tumor cohort) reported median nadir leukocyte count 1.75 ×10³/mm³, neutrophil count 1.55 ×10³/mm³, and platelet count 20,500/mm³, indicating substantial marrow suppression. |
| Emetogenicity Classification | Moderate (consistent with general classification of topoisomerase I inhibitors) |
| Monitoring Items | Complete blood count with differential (neutrophils, platelets), renal function (Topotecan is renally cleared and requires dose adjustment in renal impairment), liver function |
| Handling Protection | Yes — must be handled under standard cytotoxic/hazardous drug handling protocols (PPE, closed-system transfer devices) |

---

## Safety Considerations

- **Drug Interactions**: The safety database records **296 total documented interactions**. Notable higher-severity interactions include:
  - **Major**: Deferiprone, Samarium (153Sm) lexidronam
  - **Moderate**: Eliglustat, Rolapitant, Iobenguane (I-131), Palifermin, Strontium chloride Sr-89, Ibritumomab tiuxetan
  - Several additional interactions (e.g., with proton pump inhibitors, H2 antagonists, antiemetics, corticosteroids) are recorded at "Unknown" severity and should be reviewed individually before combination use.

Formal key warnings and contraindications are not available in the current data pack; please refer to the official package insert once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap (missing TFDA label warnings/contraindications, DG001) prevents completion of the initial safety assessment (S1), and the lead predicted indication (female breast carcinoma) is only evidence level L2 — supported mainly by small, decades-old Phase II/pilot studies rather than confirmatory Phase III data. Topotecan also currently has zero registrations in the India market, adding a regulatory barrier beyond the science.

**To proceed, the following is needed:**
- Official TFDA/Indian package insert (warnings, contraindications) to close DG001
- Formal MOA documentation to close DG002 and support the mechanistic rationale beyond model-derived text
- Confirmation of route of administration compatibility for the breast carcinoma indication
- Updated/contemporary clinical trial evidence specifically in breast carcinoma populations (most current literature is >20 years old); a targeted search for recent Phase II/III breast cancer trials is recommended
- Regulatory pathway assessment given the drug's current "Not Marketed" status in India
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

