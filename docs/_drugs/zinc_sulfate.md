---
layout: default
title: Zinc Sulfate
parent: 僅模型預測 (L5)
nav_order: 899
evidence_level: L5
indication_count: 4
---

# Zinc Sulfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Zinc Sulfate: From Zinc Deficiency to Pharyngitis

## One-Sentence Summary

> Zinc sulfate is classically used as a mineral supplement to correct zinc deficiency and support mucosal/immune health.
> The TxGNN model predicts it may be effective for **Pharyngitis**,
> with **4 clinical trials** and **3 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no India/Taiwan license record); classically used for zinc deficiency/dietary supplementation |
| Predicted New Indication | Pharyngitis |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L3 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for zinc sulfate. Based on known information, zinc is an essential trace mineral involved in mucosal epithelial integrity, wound healing, and local antiviral/antimicrobial defense — properties that are directly relevant to inflamed pharyngeal mucosa.

The relationship between zinc's classic use (correcting zinc deficiency) and the predicted new indication (pharyngitis) is plausible on mechanistic grounds: several of the supporting studies specifically use zinc lozenges, gargles, or irrigation to reduce pharyngeal/throat inflammation, either as prophylaxis (postoperative sore throat, COVID-19 outpatient prevention) or as adjunct therapy (radiation-induced pharyngitis/mucositis in head and neck cancer). This convergent, if indication-adjacent, evidence base supports the biological plausibility of the TxGNN prediction, though none of the identified trials or publications enrolled a primary "acute pharyngitis" population directly.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04370782](https://clinicaltrials.gov/study/NCT04370782) | Phase 4 | Completed | 18 | Open-label RCT of hydroxychloroquine + zinc combined with azithromycin or doxycycline for outpatient COVID-19, a condition presenting with sore throat/pharyngitis among core symptoms |
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | N/A | Completed | 87 | Double-blind, placebo-controlled RCT of preoperative oral zinc lozenges for prevention of postoperative sore throat after endotracheal intubation |
| [NCT04621461](https://clinicaltrials.gov/study/NCT04621461) | Phase 4 | Completed | 3 | Placebo-controlled RCT of zinc monotherapy for outpatient COVID-19 treatment (very small enrollment) |
| [NCT04446104](https://clinicaltrials.gov/study/NCT04446104) | Phase 3 | Completed | 4257 | Large open-label prophylaxis trial in high-risk migrant workers for COVID-19, a disease commonly presenting with fever, cough, and sore throat |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | J Med Assoc Thai | Randomized, double-blind, placebo-controlled trial showing zinc sulfate supplementation reduced radiation-induced oral mucositis and pharyngitis in head and neck cancer patients |
| [38693477](https://pubmed.ncbi.nlm.nih.gov/38693477/) | 2024 | RCT | BMC Anesthesiology | Randomized controlled trial comparing preoperative zinc, magnesium, and budesonide gargles for reducing incidence/severity of postoperative sore throat |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | Case-related report | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | Discussion of long-lasting post-tonsillectomy taste dysgeusia, noting dietary zinc deficiency as a possible contributing factor |

---

## India Market Information

No India market authorization data is available — zinc sulfate is currently listed as **not marketed** in this evidence pack, with 0 registered licenses.

---

## Safety Considerations

**Drug Interactions**: The DDI database records 103 total documented interactions. Notable **Moderate**-level interactions include:
- **Alendronic acid, Risedronic acid, Ibandronate** (bisphosphonates) — co-administration with zinc may reduce bisphosphonate absorption
- **Tetracycline** — zinc chelation may reduce tetracycline absorption
- **Baloxavir marboxil** — reduced antiviral absorption via chelation with polyvalent cations

Most remaining catalogued interactions (e.g., with immunosuppressants and biologics such as Abatacept, Adalimumab, Azathioprine, Anakinra, and corticosteroids) are classified as **Minor**.

Key warnings and contraindications from the official label are not currently available — please refer to the package insert once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A Blocking data gap exists — official label warnings/contraindications (TFDA source) are unavailable, which prevents the S1 safety screening step. In addition, zinc sulfate is not currently marketed locally, and the supporting evidence for pharyngitis is drawn from adjacent conditions (postoperative sore throat, radiation-induced mucositis, COVID-19 prevention) rather than direct RCTs in primary acute pharyngitis populations.

**To proceed, the following is needed:**
- Official package insert / label data on warnings and contraindications (resolves Blocking gap DG001)
- Confirmed mechanism of action via DrugBank query (resolves High-severity gap DG002)
- Direct RCT evidence in a primary/uncomplicated pharyngitis population
- Confirmation of local market authorization or registration pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

