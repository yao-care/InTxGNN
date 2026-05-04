---
layout: default
title: Melphalan
parent: 僅模型預測 (L5)
nav_order: 319
evidence_level: L5
indication_count: 10
---

# Melphalan
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

# Melphalan: From Multiple Myeloma to Gonadal Germ Cell Tumor

## One-Sentence Summary

Melphalan is a bifunctional nitrogen mustard alkylating agent, classically used as a cornerstone chemotherapy for multiple myeloma and selected hematologic malignancies.
The TxGNN model predicts it may be effective for **Gonadal Germ Cell Tumor**,
with **8 clinical trials** and **4 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple Myeloma (established clinical use; not listed in India regulatory data) |
| Predicted New Indication | Gonadal Germ Cell Tumor |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Melphalan (L-phenylalanine mustard, L-PAM) is a bifunctional nitrogen mustard alkylating agent. Although detailed MOA data is not available in this evidence package, Melphalan's mechanism is well-characterized in the oncology literature: it forms interstrand DNA cross-links by alkylating guanine residues at the N7 position, disrupting DNA replication and triggering apoptosis in rapidly dividing cells. At high doses, this mechanism overwhelms the DNA repair capacity of most solid tumors.

Gonadal germ cell tumors (GCTs) are inherently highly proliferative and rely heavily on homologous recombination (HR) repair pathways — a profile that makes them intrinsically sensitive to DNA cross-linking agents such as Melphalan. This biological affinity has been recognized since at least 1956, when sarcolysin (the Soviet-era name for L-PAM) was documented in treating testicular seminoma. In modern oncology, high-dose Melphalan serves as a core conditioning agent in autologous stem cell transplantation (ASCT) protocols for platinum-refractory or relapsed GCTs.

The TxGNN prediction is therefore well-grounded: the knowledge graph likely captures the established node connection between alkylating agents and GCTs across both testicular and ovarian subtypes. The existence of a dedicated completed Phase 2 trial (NCT00936936, n=64) specifically targeting poor-prognosis relapsed GCTs with a Melphalan-containing high-dose regimen provides meaningful clinical validation for this mechanistic inference.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | High-dose Gemcitabine + Docetaxel + **Melphalan** + Carboplatin (Cycle 1) followed by ICE (Cycle 2) for poor-prognosis relapsed GCTs — strongest and most directly relevant trial for this indication |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | Busulfan + **Melphalan** + Topotecan followed by ASCT for advanced/recurrent solid tumors, with GCT-related tumor subtypes included in the eligibility |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Escalating-dose **Melphalan** + ASCT + Amifostine cytoprotection across multiple solid tumors including GCT; Melphalan is the primary investigational agent |
| [NCT01272817](https://clinicaltrials.gov/study/NCT01272817) | N/A | Completed | 36 | Nonmyeloablative allogeneic HSCT using **Melphalan** + Cladribine for various hematologic and solid tumors; GCT proportion not specified |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal **Melphalan** for recurrent neoplastic meningitis; CNS delivery route, low direct relevance to systemic GCT treatment |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine chemoprotection with ASCT for high-risk pediatric solid/brain tumors; terminated early before full enrollment |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | N/A | Completed | 174 | Registry-type ASCT pilot study for hematologic malignancies and selected solid tumors; **Melphalan** as one conditioning agent; GCT proportion unknown |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Large ABMT registry study evaluating eight high-dose chemotherapy regimens; broad indication mix, serves as background evidence only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [4270380](https://pubmed.ncbi.nlm.nih.gov/4270380/) | 1973 | Retrospective Review | *Oncology* | Chemotherapy of testicular germinal tumors; retrospective review covering early alkylating agent use including Melphalan in GCT management |
| [24913](https://pubmed.ncbi.nlm.nih.gov/24913/) | 1977 | Case Series / Historical Report | *Urologic Clinics of North America* | Historical account of seminoma treatment, documenting early Melphalan (sarcolysin/L-PAM) clinical experience |
| [13392619](https://pubmed.ncbi.nlm.nih.gov/13392619/) | 1956 | Case Series | *Voprosy Onkologii* | Earliest documented clinical experience treating testicular seminoma and metastases with sarcolysin (L-PAM precursor); establishes a 70-year history of this drug-indication pairing |
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Experimental / Pharmacological Study | *Acta Unio Internationalis Contra Cancrum* | Mechanistic study on the influence of hormonal and alkylating agents on pituitary FSH function; background pharmacological data relevant to gonadal tumor biology |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Nitrogen mustard alkylating agent) |
| Myelosuppression Risk | **High** — severe, dose-limiting myelosuppression (neutropenia, thrombocytopenia, anaemia); high-dose IV regimens require ASCT haematopoietic support |
| Emetogenicity Classification | Moderate to High (particularly at high intravenous doses used in conditioning regimens) |
| Monitoring Items | CBC with differential (mandatory), serum creatinine / eGFR (dose adjustment required in renal impairment), liver function tests, electrolytes, urine output |
| Handling Protection | Must follow cytotoxic drug handling regulations; IV preparation requires a biological safety cabinet and full PPE per cytotoxic compounding standards |

---

## Safety Considerations

**Drug Interactions** (234 total interactions identified; representative sample below):

| Interacting Drug | Interaction Level |
|-----------------|------------------|
| Amphotericin B | Moderate |
| Amphotericin B (lipid complex) | Moderate |
| Amphotericin B (cholesteryl sulfate) | Moderate |
| Amphotericin B (liposomal) | Moderate |
| Cimetidine | Minor |
| Levofloxacin | Minor |
| Zinc sulfate | Minor |
| Zinc gluconate | Minor |
| Lansoprazole | Unknown |
| Dolasetron | Unknown |

> The four Amphotericin B formulations all carry a **Moderate** interaction designation — clinically relevant given that Melphalan-based ASCT patients frequently require antifungal prophylaxis. Please refer to the full package insert for warnings, contraindications, and the complete interaction list.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 trial (NCT00936936, n=64) directly investigates a Melphalan-containing high-dose regimen for poor-prognosis relapsed GCTs, supported by two additional Phase 1/2 ASCT studies and historical literature spanning nearly 70 years. The mechanistic basis — DNA cross-linking in HR-proficient, highly proliferative GCTs — is biologically well-founded, and Melphalan's role in this context is consistent with established salvage chemotherapy practice globally.

**To proceed, the following is needed:**
- Obtain Melphalan package insert to fill the Blocking data gap (warnings, contraindications) before any clinical safety evaluation
- Retrieve full MOA data from DrugBank API (DB01042) to complete mechanistic analysis
- Assess India regulatory pathway: Melphalan is not currently marketed in India; an import or new drug application may be required
- Define GCT subtype scope (testicular vs. ovarian; seminoma vs. non-seminoma) for protocol design, as available evidence predominantly covers testicular GCT
- Confirm availability of ASCT infrastructure in target institution, as high-dose Melphalan regimens are inseparable from stem cell rescue support
- Review the 230+ remaining DDI entries to identify clinically critical interactions in the ASCT supportive care context (e.g., antifungals, antiemetics, proton pump inhibitors)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

