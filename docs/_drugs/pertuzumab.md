---
layout: default
title: Pertuzumab
parent: 僅模型預測 (L5)
nav_order: 652
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Pertuzumab (Perjeta®, DB06366) is a HER2-targeted humanized monoclonal antibody originally developed for HER2-overexpressing breast cancer, used in combination with trastuzumab and docetaxel.
The TxGNN model predicts it may also be effective in **progesterone-receptor (PR) positive breast cancer**,
with **10 clinical trials** and **20 publications** currently supporting this direction — though this "new" indication is largely a hormone-receptor subgroup of the drug's existing HER2+ population rather than a novel mechanistic hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-overexpressing (HER2-positive) breast cancer, in combination with trastuzumab ± docetaxel |
| Predicted New Indication | Progesterone-receptor positive breast cancer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Pertuzumab is a humanized IgG1 monoclonal antibody (research code 2C4; trade name Perjeta) that binds subdomain II of the HER2/ERBB2 extracellular domain, blocking HER2–HER3 heterodimerization and downstream PI3K/AKT and MAPK signaling. Its approved clinical use is "treatment of HER2-overexpressing breast cancer, in combination with trastuzumab and docetaxel."

Progesterone-receptor status is a hormone-receptor classifier layered on top of HER2 status — it does not define an independent disease mechanism. Because pertuzumab's antitumor activity is driven by HER2 pathway blockade rather than hormone-receptor signaling, PR-positive and PR-negative HER2+ breast cancer patients are both mechanistically plausible responders; PR status functions as a stratification variable within trials rather than a distinct target population.

Consistent with this, the clinical trial evidence for this candidate largely overlaps with pertuzumab's core HER2+ breast cancer development program (neoadjuvant/adjuvant and metastatic settings, ER/PR ± subgroups), rather than representing a genuinely new indication. This means the "repurposing" signal here is best read as confirmatory of an already-recognized subgroup rather than a novel mechanistic hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Randomized double-blind trial of QL1209 (biosimilar) vs. pertuzumab + docetaxel + trastuzumab in early/locally advanced HER2+, ER/PR-negative breast cancer |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050: atezolizumab or placebo + neoadjuvant AC-paclitaxel-trastuzumab-pertuzumab in early HER2+ breast cancer |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | Active, not recruiting | 398 | Head-to-head neoadjuvant comparison of BCD-178 (biosimilar) vs. Perjeta in HER2+, ER/PR-negative breast cancer |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Completed | 417 | 4-arm neoadjuvant study of Herceptin/docetaxel/pertuzumab combinations; classic pertuzumab pCR design (NeoSphere-type) |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | Unknown | 7 | Neoadjuvant aromatase inhibitor + pertuzumab/trastuzumab, chemo-free, in HR+/HER2+ early breast cancer |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Active, not recruiting | 164 | Preoperative T-DM1 + pertuzumab in early-stage HER2+ breast cancer, examining HER2 heterogeneity |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | Active, not recruiting | 128 | Neoadjuvant lapatinib + trastuzumab ± endocrine therapy in HER2-overexpressing breast cancer |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Terminated | 139 | DECRESCENDO: de-escalated neoadjuvant chemo + SC pertuzumab/trastuzumab in HER2+/ER-negative/node-negative breast cancer |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completed | 1151 | Retrospective non-interventional study on HER2-low prevalence and treatment patterns in metastatic breast cancer |
| [NCT03058939](https://clinicaltrials.gov/study/NCT03058939) | Phase 2 | Withdrawn | 0 | Weekly neoadjuvant paclitaxel response rate study in Nigerian women with breast cancer (withdrawn, no enrollment) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT (WSG-ADAPT) | Ann Oncol | 12-week neoadjuvant dual HER2 blockade (trastuzumab+pertuzumab) ± paclitaxel in HR-/HER2+ early breast cancer; response and predictive markers |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT (biosimilar) | Br J Cancer | Phase 3 equivalence trial of QL1209 vs. reference pertuzumab + trastuzumab + docetaxel in HER2+, ER/PR-negative breast cancer |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT (WSG-TP-II) | JAMA Oncol | Endocrine therapy + trastuzumab/pertuzumab vs. de-escalated chemotherapy in HR+/HER2+ early breast cancer |
| [37609714](https://pubmed.ncbi.nlm.nih.gov/37609714/) | 2023 | RCT (DECRESCENDO) | Future Oncol | De-escalated chemotherapy with SC pertuzumab/trastuzumab in HR-negative, HER2+, node-negative early breast cancer |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT long-term follow-up (NeoSphere) | Lancet Oncol | 5-year PFS/DFS and safety of neoadjuvant pertuzumab + trastuzumab in HER2+ breast cancer |
| [30106636](https://pubmed.ncbi.nlm.nih.gov/30106636/) | 2018 | RCT (PERTAIN) | J Clin Oncol | Phase 2 open-label trial: trastuzumab + aromatase inhibitor ± pertuzumab in HER2+/HR+ metastatic/locally advanced breast cancer |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Review (ASCO guideline) | J Clin Oncol | ASCO guideline update on systemic therapy for advanced HER2+ breast cancer, including pertuzumab-based regimens |
| [40076535](https://pubmed.ncbi.nlm.nih.gov/40076535/) | 2025 | Systematic Review | Int J Mol Sci | Pertuzumab + trastuzumab + docetaxel as adjuvant doublet therapy for HER2+ breast cancer |
| [32905036](https://pubmed.ncbi.nlm.nih.gov/32905036/) | 2020 | Review | Cureus | Literature review of therapeutic strategies for HER2+ metastatic breast cancer, including anti-HER2 receptor status subtypes |
| [33662161](https://pubmed.ncbi.nlm.nih.gov/33662161/) | 2021 | Review | Eur J Clin Invest | CDK4/6 and PI3K inhibitors as emerging combination partners with anti-HER2 therapy (incl. pertuzumab) |

---

## India Market Information

Pertuzumab currently has **no registered product license in India** (0 registrations; market status: Not Marketed). No local product/dosage-form data is available in this evidence pack.

---

## Cytotoxicity

*(Antineoplastic — Pertuzumab is a HER2/ERBB2-targeted monoclonal antibody approved for HER2-overexpressing breast cancer.)*

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2/ERBB2-targeted monoclonal antibody; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low as monotherapy; risk increases substantially when co-administered with taxane chemotherapy (docetaxel/paclitaxel), as used in most trial regimens above |
| Emetogenicity Classification | Low (consistent with monoclonal antibody class) |
| Monitoring Items | Please refer to the package insert warnings and precautions (no India-specific label data available); general anti-HER2 practice includes cardiac/LVEF monitoring, and CBC/liver-renal function when combined with chemotherapy |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: Moderate-level interaction reported with **Idelalisib** (source: DDInter).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Evidence level is L1, supported by ≥2 completed Phase 3 RCTs (NCT04629846, NCT03726879) plus multiple Phase 2 trials, and the mechanistic link is strong since pertuzumab's activity depends on HER2 status rather than PR status. However, this predicted indication substantially overlaps with pertuzumab's already-established HER2+ breast cancer population, and the drug is not yet registered in India.

**To proceed, the following is needed:**
- India-specific product label / warnings and contraindications (currently a Blocking data gap — required before any S1 safety assessment)
- Formal DrugBank-sourced mechanism-of-action confirmation (currently a High-severity data gap)
- Regulatory pathway assessment for India market entry (currently 0 registrations)
- Clarification of whether "PR-positive breast cancer" should be evaluated as a genuinely distinct indication or folded into the existing HER2+ breast cancer label as a subgroup
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

