---
layout: default
title: Sirolimus
parent: 僅模型預測 (L5)
nav_order: 768
evidence_level: L5
indication_count: 10
---

# Sirolimus
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

# Sirolimus: From Organ Transplant Rejection Prophylaxis to Liposarcoma

## One-Sentence Summary

> Sirolimus (DrugBank DB00877) is an mTOR inhibitor globally established for prophylaxis of organ rejection after renal transplantation, though it is currently **not marketed in India**.
> The TxGNN model's top-ranked candidate indication is **Liposarcoma**, supported by **5 clinical trials** and **12 publications**, but only one trial directly tests sirolimus itself in this disease — most other evidence comes from related mTOR inhibitors (temsirolimus, everolimus, ridaforolimus).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in India regulatory data (drug not marketed); the molecule is globally established for prophylaxis of renal transplant rejection |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

A formal DrugBank-sourced mechanism-of-action record was not available for this evaluation (data gap DG002). However, the mechanistic role of sirolimus is well documented throughout the collected literature and trial descriptions: it inhibits **mammalian target of rapamycin (mTOR)**, a serine/threonine kinase that integrates growth-factor and nutrient signaling to drive cell proliferation, growth and survival (e.g., PMID 37400145: "Rapamycin (RAPA) is an inhibitor of mTOR").

The connection between sirolimus's original use (immunosuppression in transplantation) and the proposed new indication (liposarcoma) runs through this same mTOR pathway. Dedifferentiated liposarcoma has been shown to exhibit constitutive activation of the Akt-mTOR and MAPK pathways (PMID 26518767), providing a biological rationale for mTOR blockade as an anti-proliferative strategy. This has motivated a class-wide interest in "rapalogs" (sirolimus, temsirolimus, everolimus, ridaforolimus) across sarcoma subtypes, illustrated by several trials in the evidence pack (NCT00093080, NCT03114527, NCT00949325, NCT01614795).

Only one trial directly evaluates sirolimus itself in this indication — **NCT02821507**, a Phase 2 study of sirolimus + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma (n=70, Grade A relevance). The remaining trials and much of the literature test related rapalogs, so the current evidence base for liposarcoma is best characterized as **class-effect support with limited drug-specific confirmation**.

**Portfolio note:** Among the 10 candidate indications surfaced for sirolimus in this evidence pack, two reach a substantially stronger evidence tier (**L1**, decision stage S3, "Proceed with Guardrails"): **lymphangiomyoma/LAM** (rank 5) and **lung PEComa** (rank 9). Both are underpinned by completed Phase 3 RCTs of sirolimus itself (MILES trial, NCT00414648) and an existing FDA approval (2015) for LAM. Given that sirolimus has zero current registrations in India, these two indications likely represent a more mature and lower-risk repurposing opportunity than liposarcoma and warrant separate evaluation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Sirolimus + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma — direct sirolimus evidence in this indication |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (AP23573), an mTOR inhibitor, in advanced sarcoma (QDx5 every 2 weeks regimen) |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab (IGF-1R antibody) + temsirolimus in pediatric recurrent/refractory sarcoma |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + everolimus in advanced dedifferentiated liposarcoma and leiomyosarcoma |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Temsirolimus (Torisel) + liposomal doxorubicin in advanced soft tissue/bone sarcoma |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | RCT (Phase 2) | Clin Cancer Res | SAR-096: Ribociclib + everolimus in advanced dedifferentiated liposarcoma and leiomyosarcoma |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Overview of novel therapeutics in soft tissue sarcoma, including mTOR-pathway agents |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | Rationale and results of molecular-targeted agent trials in advanced sarcomas |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Targeted treatment of rare connective tissue tumors and sarcomas, including mTOR-directed approaches |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | Cohort | J Am Soc Nephrol | Sirolimus after early cyclosporine withdrawal reduces cancer risk in renal transplant recipients |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Mechanistic/Preclinical | Tumour Biol | Akt-mTOR and MAPK pathway activation demonstrated in dedifferentiated liposarcoma specimens |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Preclinical | Cancer Genomics Proteomics | Chloroquine + rapamycin combination effective against well-differentiated liposarcoma models |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Preclinical | In Vivo | Chloroquine + rapamycin arrests tumor growth in a dedifferentiated liposarcoma PDOX mouse model |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Preclinical | Mol Cancer Ther | MLN0128, an ATP-competitive mTOR kinase inhibitor, shows antitumor activity in bone/soft-tissue sarcoma |
| [32711543](https://pubmed.ncbi.nlm.nih.gov/32711543/) | 2020 | Case report | Diagn Pathol | Fibro-adipose vascular anomaly (FAVA) cases with mTOR pathway activation; sirolimus response noted |

---

## India Market Information

Sirolimus currently has **no registered products in India** (market status: Not Marketed; total registrations: 0). No license or dosage-form data is available for this evaluation.

---

## Safety Considerations

**Drug Interactions**: Sirolimus has 645 documented interactions on record. Notable **Major**-severity interactions include:
- Amphotericin B / Amphotericin B (lipid complex)
- Clarithromycin
- Mesalazine
- Balsalazide

Numerous **Moderate**-severity interactions are also documented, including with corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (metformin, pioglitazone, acarbose, alogliptin, canagliflozin, dapagliflozin, chlorpropamide, albiglutide), aprepitant, and cimetidine.

Drug-specific key warnings and contraindications (TFDA/local package insert equivalent) were **not available** for this evaluation (data gap DG001, flagged as *Blocking* — this prevents completion of the S1 safety pre-screen).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for sirolimus in liposarcoma reaches only L2 (a single direct sirolimus trial, n=70; remaining support is class-effect from related rapalogs), and local safety documentation (warnings/contraindications) is currently a blocking data gap. This combination does not yet meet the bar for proceeding, even with guardrails.

**To proceed, the following is needed:**
- TFDA-equivalent package insert warnings and contraindications (DG001 — blocking, required for S1 safety screen)
- Formal DrugBank/verified mechanism-of-action documentation (DG002)
- Additional direct sirolimus (not rapalog-class) trial data in liposarcoma, ideally Phase 2/3
- Separately, given the absence of any India registration for sirolimus, consider prioritizing a parallel evaluation of **lymphangiomyoma/LAM** and **lung PEComa** (both L1 evidence, existing FDA-approved precedent) as potentially faster-track repurposing candidates for this molecule
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

