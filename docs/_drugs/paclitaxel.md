---
layout: default
title: Paclitaxel
parent: High Evidence (L1-L2)
nav_order: 630
evidence_level: L1
indication_count: 10
---

# Paclitaxel
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Paclitaxel: From Established Oncology Indications to Female Breast Carcinoma

## One-Sentence Summary

Paclitaxel is a taxane-class antineoplastic agent with long-established use across multiple solid tumors (ovarian, breast, and non-small-cell lung cancer). The TxGNN model additionally scores it very highly for **Female Breast Carcinoma**, a prediction supported by **50 registered clinical trials** identified in this evidence pack, though a dedicated PubMed search under this exact disease label returned no indexed publications.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian, breast, and non-small-cell lung cancer (established global indications; not itemized in this evidence pack's regulatory data) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Taiwan Market Status | Not marketed (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for this evidence pack is not available (flagged as a High-severity data gap, DG002). Based on well-established pharmacological knowledge, however, paclitaxel is a taxane-class microtubule-stabilizing agent: it binds β-tubulin, promotes microtubule polymerization, and prevents normal microtubule disassembly. This arrests rapidly dividing cells at the G2/M phase of mitosis and ultimately triggers apoptosis.

Paclitaxel's original approved indications already include breast cancer alongside ovarian and non-small-cell lung cancer, so the TxGNN prediction for "Female Breast Carcinoma" largely reconfirms an existing, guideline-endorsed therapeutic relationship rather than identifying a truly novel indication. This is reflected in the evidence pack's own rationale: paclitaxel is described as "one of the standard chemotherapy backbones for breast cancer regardless of subtype."

Mechanistically, this is unsurprising — breast carcinoma cells, like other rapidly proliferating solid tumor cells, are highly dependent on functional mitotic spindle assembly, making them broadly sensitive to microtubule-stabilizing cytotoxics. The very large volume of Phase 2/3 clinical trial activity (50 trials identified) reflects paclitaxel's role as a chemotherapy backbone used alone or combined with targeted agents (trastuzumab, pertuzumab, lapatinib), immunotherapy (atezolizumab, pembrolizumab), and other cytotoxics across essentially all breast cancer subtypes (HER2+, HR+, and triple-negative).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00281658](https://clinicaltrials.gov/study/NCT00281658) | Phase 3 | Completed | 444 | Randomized, placebo-controlled: lapatinib + paclitaxel vs. placebo + paclitaxel in ErbB2-amplified metastatic breast cancer |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | Completed | 455 | NeoALTTO: neoadjuvant lapatinib and/or trastuzumab plus paclitaxel in HER2/ErbB2-positive primary breast cancer |
| [NCT00004067](https://clinicaltrials.gov/study/NCT00004067) | Phase 3 | Completed | 2130 | AC followed by paclitaxel vs. AC-paclitaxel + trastuzumab in HER2-overexpressing node-positive breast cancer |
| [NCT02954055](https://clinicaltrials.gov/study/NCT02954055) | Phase 2 | Completed | 140 | Randomized: metronomic vinorelbine/cyclophosphamide/capecitabine vs. weekly paclitaxel in ER+/HER2- advanced breast cancer |
| [NCT03799679](https://clinicaltrials.gov/study/NCT03799679) | Phase 4 | Unknown | 60 | Nab-paclitaxel followed by dose-intensive epirubicin + cyclophosphamide as neoadjuvant therapy in triple-negative breast cancer |
| [NCT02301988](https://clinicaltrials.gov/study/NCT02301988) | Phase 2 | Completed | 151 | Randomized, double-blind: ipatasertib (AKT inhibitor) + paclitaxel vs. placebo + paclitaxel, neoadjuvant, early-stage triple-negative breast cancer |
| [NCT01091428](https://clinicaltrials.gov/study/NCT01091428) | Phase 2 | Completed | 191 | MLN8237 (Aurora A kinase inhibitor) + weekly paclitaxel vs. weekly paclitaxel alone, including a breast cancer Phase 1 cohort |
| [NCT00096291](https://clinicaltrials.gov/study/NCT00096291) | Phase 2 | Completed | 62 | Comparison of two doxorubicin/paclitaxel neoadjuvant regimens with physiologic, radiologic and molecular response markers |
| [NCT02909751](https://clinicaltrials.gov/study/NCT02909751) | Phase 2 | Completed | 80 | Tocotrienol added to neoadjuvant chemotherapy to improve efficacy/reduce toxicity in breast cancer |
| [NCT00005581](https://clinicaltrials.gov/study/NCT00005581) | Phase 3 | Unknown | 1000 | Randomized: epirubicin + paclitaxel vs. CEF (cyclophosphamide/epirubicin/5-FU) as adjuvant therapy for node-positive breast cancer |

---

## Literature Evidence

Currently no related literature available (a dedicated PubMed search under the "female breast carcinoma" TxGNN disease label returned 0 results in this evidence pack; broader breast-cancer-subtype searches for other ranked indications did return relevant literature — see note in Conclusion).

---

## Taiwan Market Information

Paclitaxel is currently recorded as **not marketed** in Taiwan under this evidence pack (0 registered licenses). No product registration records were available to summarize.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Taxane class — microtubule-stabilizing agent) |
| Myelosuppression Risk | High — neutropenia is the dose-limiting, class-defining toxicity of taxanes; drug-specific toxicity data was not provided in this evidence pack |
| Emetogenicity Classification | Low to moderate (per standard taxane emetogenicity classification; higher when combined with other agents such as anthracyclines or platinums) |
| Monitoring Items | Complete blood count with differential, liver function, infusion-related hypersensitivity reactions, peripheral neuropathy assessment |
| Handling Protection | Yes — requires handling as a hazardous/cytotoxic drug per standard chemotherapy handling protocols |

---

## Safety Considerations

**Drug Interactions**: DrugBank-derived interaction data lists **553 total interactions**. Notable moderate-level interactions include: Aprepitant, Cimetidine, Clarithromycin, Clotrimazole, Dexamethasone, Eliglustat, Metronidazole, Miconazole, Rolapitant, Rosuvastatin, Simvastatin, Tinidazole, and Troglitazone. Minor-level interactions include Ascorbic acid and Levofloxacin. Several unclassified ("Unknown" level) interactions were also flagged, including Glimepiride, Doxycycline, Morphine, Metformin, and Omeprazole, and should be reviewed individually before combination use.

(Formal package-insert warnings and contraindications were not available in this evidence pack — see Conclusion for remediation.)

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2/3 randomized trials — including large studies such as NCT00004067 (2,130 patients) and NCT00553358 (455 patients) — support paclitaxel's established efficacy as a breast cancer chemotherapy backbone, giving this prediction Level 1 evidence. However, this pack lacks Taiwan-specific regulatory documentation (blocking gap) and a formal MOA record, so guardrails are needed before this can move to unrestricted clinical guidance.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (currently a Blocking data gap — DG001; remediation: download and parse the official TFDA label PDF)
- Formal DrugBank-sourced mechanism of action record (High-severity gap — DG002; remediation: query the DrugBank API)
- Verification of actual Taiwan market/registration status for paclitaxel-containing products, since the "0 licenses / Not marketed" result is unusual for a globally standard chemotherapy agent and may reflect a data-collection gap rather than true absence from the market
- Route-of-administration compatibility confirmation (marked "pending" in this evidence pack)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

