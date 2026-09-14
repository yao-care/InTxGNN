---
layout: default
title: Temsirolimus
parent: 僅模型預測 (L5)
nav_order: 807
evidence_level: L5
indication_count: 3
---

# Temsirolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Temsirolimus: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

> Temsirolimus is an mTOR inhibitor known internationally as an antineoplastic agent; India-specific approved-indication data is not present in this evidence pack.
> The TxGNN model predicts it may be effective for **Liposarcoma**,
> with **5 clinical trials** and **1 publication** currently supporting this direction, though only one trial uses Temsirolimus itself directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in evidence pack (`original_indications` empty; Temsirolimus is globally recognized as an antineoplastic mTOR inhibitor) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.54% (rank 7926) |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in the evidence pack (flagged as a High-severity data gap, DG002). Based on the drug's known pharmacological class, Temsirolimus is a rapalog (mTOR inhibitor) that blocks signaling through the PI3K/AKT/mTOR pathway, a pathway central to cell growth and proliferation control in oncology.

The evidence pack does not record an India-approved original indication for Temsirolimus (market status: not marketed, 0 registrations), so a direct "original vs. new indication" comparison cannot be made from local regulatory data. However, per the evidence pack's own repurposing rationale, the PI3K/AKT/mTOR pathway is frequently dysregulated in well-differentiated and dedifferentiated liposarcoma — often downstream of MDM2/CDK4 amplification — which provides a plausible mechanistic basis for mTOR-inhibitor activity in this tumor type.

That said, direct clinical evidence using Temsirolimus itself (rather than same-class agents such as sirolimus, ridaforolimus, or everolimus) in liposarcoma is limited to a single small Phase 1/2 combination trial (NCT00949325, n=24). The majority of supporting evidence reflects a **class effect** across rapalogs rather than drug-specific confirmation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Torisel (Temsirolimus brand name) combined with liposomal doxorubicin in advanced soft tissue/bone sarcoma, including liposarcoma; the only trial directly evidencing Temsirolimus in this disease group. |
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | Sirolimus (same-class rapalog) + cyclophosphamide in metastatic/unresectable myxoid liposarcoma and chondrosarcoma; disease-specific but different drug. |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | AP23573 (ridaforolimus, same-class mTOR inhibitor) in advanced sarcoma; largest trial supporting rapalog activity in sarcoma. |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib + Everolimus (same-class) in advanced dedifferentiated liposarcoma and leiomyosarcoma. |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Cixutumumab + Temsirolimus in pediatric recurrent/refractory sarcoma; direct drug use but pediatric, non-liposarcoma-specific population. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bulletin du cancer | Reviews targeted treatment approaches for rare connective tissue tumors and sarcomas, classified by molecular subgroup, including pathways relevant to mTOR-targeted therapy. |

---

## India Market Information

Temsirolimus is not currently marketed in India. No registration records are available in this evidence pack (`total_licenses: 0`).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor / rapalog class) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Suggested based on DDI profile: renal and hepatic function, blood glucose and lipid panel, complete blood count |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The evidence pack records 540 total interactions (ddinter source). Notable **Major**-level interactions include:
  - Amphotericin B / Amphotericin B (lipid complex)
  - Dexamethasone
  - Clarithromycin

  Notable **Moderate**-level interactions include Acarbose, Hydrocortisone, Metformin, Pioglitazone, Aprepitant, Cimetidine, Canagliflozin, Dapagliflozin, and several corticosteroids (Betamethasone, Budesonide, Triamcinolone), among others.

> Key warnings and contraindications are not available in this evidence pack (flagged as Blocking data gap DG001). Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking-severity data gap (missing India label warnings/contraindications, DG001) prevents completion of the S1 safety initial review, and evidence level is L2 with only one small Phase 1/2 trial (n=24) directly using Temsirolimus in the liposarcoma population — most supporting data reflects a rapalog class effect rather than drug-specific evidence. The drug is also not currently marketed in India.

**To proceed, the following is needed:**
- India-specific label warnings and contraindications (resolve DG001, Blocking)
- Confirmed mechanism of action data from DrugBank (resolve DG002)
- Larger, disease-specific clinical evidence using Temsirolimus itself in liposarcoma (beyond the single n=24 trial)
- Regulatory pathway assessment given current "not marketed" status in India
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

