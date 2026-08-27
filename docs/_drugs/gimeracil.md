---
layout: default
title: Gimeracil
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
---

# Gimeracil
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

Using the drug-repurposing evidence pack, here is the evaluation report for **Gimeracil**, focused on its top-ranked predicted indication (Colonic Neoplasm), which is the only candidate with meaningful clinical/literature support (L1). The other 9 predicted indications (rank 2–10) are Hold/Research-Question stage with L4–L5 evidence and are summarized briefly at the end for completeness, per the evidence pack's decision staging.

---

# Gimeracil: From Gastric Cancer to Colonic Neoplasm

## One-Sentence Summary

Gimeracil is the DPD-inhibitor component of the S-1 combination (tegafur + gimeracil + oteracil), a fluoropyrimidine-based regimen whose proven efficacy is in gastric cancer. The TxGNN model predicts it may also be effective for **Colonic Neoplasm** (colorectal cancer), with **8 clinical trials** and **15 publications** currently supporting this direction — though the clinical evidence is attributable to the S-1 combination as a whole, not to Gimeracil as a standalone agent, and Gimeracil is not currently marketed in Taiwan.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric cancer (as a component of the S-1 combination; not individually registered in Taiwan) |
| Predicted New Indication | Colonic Neoplasm (Colorectal Cancer) |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L1 |
| Taiwan Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Gimeracil alone is not available (Data Gap). Based on known information, Gimeracil is part of the S-1 combination (tegafur/gimeracil/oteracil), where it functions as a dihydropyrimidine dehydrogenase (DPD) inhibitor. By blocking DPD-mediated breakdown of 5-fluorouracil (the active metabolite of tegafur), Gimeracil raises and sustains intratumoral 5-FU concentrations, and its efficacy as part of S-1 in gastric cancer has been proven in multiple regulatory jurisdictions.

Gastric cancer and colonic neoplasm are both gastrointestinal adenocarcinomas that respond to fluoropyrimidine-based chemotherapy through the same core mechanism — thymidylate synthase inhibition potentiated by DPD blockade. This mechanistic overlap is precisely why S-1 has already been separately approved and extensively trialed for colorectal cancer in multiple countries (including large Phase 3 adjuvant and metastatic trials), independent of the TxGNN prediction.

The caveat is that the supporting clinical evidence below is generated with the *S-1 combination product*, not Gimeracil in isolation. Since Gimeracil is not marketed as a standalone drug in Taiwan and has no local approval record, any repurposing pathway would need to proceed via the combination product or with explicit bridging justification for the single component.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | SALTO trial — randomized S-1 vs. capecitabine (± bevacizumab) as first-line therapy for metastatic colorectal cancer; direct head-to-head efficacy/safety evidence for S-1 (Grade A relevance). |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | Large adjuvant RCT comparing UFT+leucovorin vs. TS-1 (S-1) in Stage III colon cancer, with gene-expression predictive-factor analysis (Grade A relevance). |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1191 | SOX (S-1+oxaliplatin) vs. XELOX as adjuvant chemotherapy for Stage III colorectal cancer; large sample size but results not yet publicly reported. |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Phase 2 | Unknown | 82 | Raltitrexed + S-1 for metastatic colorectal cancer after failure of standard chemotherapy; primary endpoint was progression-free survival. |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Phase 2 | Unknown | 40 | S-1 + bevacizumab in unresectable/recurrent colorectal cancer after prior irinotecan/oxaliplatin failure. |
| [NCT00524706](https://clinicaltrials.gov/study/NCT00524706) | Phase 1/2 | Unknown | 42 | S-1 + oral leucovorin + oxaliplatin (SOL regimen) in untreated metastatic colorectal cancer; early-phase activity/toxicity data. |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Phase 2 | Terminated | 20 | Evaluated cardiac microvascular safety of S-1/capecitabine + oxaliplatin in metastatic GI adenocarcinoma; not an efficacy trial, low relevance. |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Phase 2 | Not yet recruiting | 52 | Planned trial of fruquintinib + S-1 as third-line therapy for advanced metastatic CRC; no data available yet. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41724114](https://pubmed.ncbi.nlm.nih.gov/41724114/) | 2026 | Real-world cohort | European Journal of Cancer | Population-based study of S-1 safety/feasibility as adjuvant therapy after capecitabine-induced hand-foot syndrome or cardiotoxicity in colon cancer. |
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Cohort | Gan To Kagaku Ryoho | Risk-factor analysis for Grade 3–4 hematologic toxicity in 87 patients receiving S-1 + irinotecan for advanced/recurrent colonic cancer (16.1% severe toxicity rate). |
| [21875473](https://pubmed.ncbi.nlm.nih.gov/21875473/) | 2011 | Cohort | Zhonghua Zhong Liu Za Zhi | Efficacy and adverse-effect profile of oxaliplatin + S-1 in postoperative colorectal cancer patients. |
| [20841935](https://pubmed.ncbi.nlm.nih.gov/20841935/) | 2010 | Cohort/PK study | Gan To Kagaku Ryoho | Pharmacokinetics of S-1 in a mouse model of peritoneal metastasis from colon cancer. |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Preclinical/Xenograft | Oncology Reports | Irinotecan overcomes 5-FU resistance in colon cancer xenografts via S-1-mediated thymidylate synthase down-regulation. |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Case Report | Anticancer Research | Complete response maintained with S-1 + CPT-11 in hepatic metastases of colon cancer. |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Case Report | Gan To Kagaku Ryoho | Two-stage hepatectomy following SOX (S-1+oxaliplatin) + panitumumab downstaging for irresectable colorectal liver metastases. |
| [29483452](https://pubmed.ncbi.nlm.nih.gov/29483452/) | 2018 | Case Report | Gan To Kagaku Ryoho | Transverse colon cancer with liver metastasis and portal vein tumor thrombosis effectively treated with combination chemotherapy including S-1-based regimens. |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | Case Report | J Oncol Pharm Practice | Hypertriglyceridemia induced by S-1 in a colorectal cancer patient — a distinct safety signal. |
| [28414195](https://pubmed.ncbi.nlm.nih.gov/28414195/) | 2017 | Case Report | Eur J Dermatol | TS-1 (tegafur/gimeracil/oteracil)-induced erythroderma with extensive mucosal involvement and hand-foot syndrome. |

---

## Taiwan Market Information

Gimeracil currently has **no marketing authorization in Taiwan** (`market_status: 未上市`, 0 registrations, no license records available). No approved product, dosage form, or labeled indication exists locally for this drug as a standalone entity or within an S-1 combination product.

---

## Cytotoxicity

Gimeracil, as the DPD-inhibitor component of the cytotoxic fluoropyrimidine combination S-1, is classified as an antineoplastic agent.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine-potentiating agent; DPD inhibitor component of the S-1 regimen) |
| Myelosuppression Risk | Moderate — literature reports a 16.1% rate of Grade 3–4 hematologic toxicity with S-1 + irinotecan in colonic cancer patients (PMID 21084813) |
| Emetogenicity Classification | Low to moderate (consistent with fluoropyrimidine-class regimens) |
| Monitoring Items | CBC with differential, liver and renal function, serum triglycerides (per reported hypertriglyceridemia signal), skin/mucosal assessment (per reported erythroderma and hand-foot syndrome) |
| Handling Protection | Standard cytotoxic drug handling precautions apply, as Gimeracil is administered only as part of a cytotoxic combination regimen |

---

## Safety Considerations

No formal drug label warnings, contraindications, or drug-drug interaction data are currently available for Gimeracil (label review and DDI database queries returned no results). Please refer to the package insert for official safety information.

**Adverse events reported in the literature** (not formal label warnings, but noted for awareness):
- Hypertriglyceridemia associated with S-1 administration (PMID 32936722)
- Erythroderma with extensive mucosal involvement and hand-foot syndrome (PMID 28414195)
- Grade 3–4 hematologic toxicity in 16.1% of patients receiving S-1 + irinotecan (PMID 21084813)

---

## Other Predicted Indications (Lower Priority)

The remaining 9 TxGNN-predicted indications for Gimeracil all fall at L4–L5 evidence levels with **Hold** or **Research Question** status, and are not recommended for near-term action:

- **Cardia cancer** (L4, Research Question) — mechanistically plausible (gastric adenocarcinoma subtype) but supported only by a single case report.
- **Rectosigmoid junction neoplasm** (L5, Research Question) — anatomically/histologically adjacent to colonic neoplasm; no direct trial or literature evidence yet.
- **Cecum villous adenoma, malignant gastric granular cell tumor, lipoma of colon, cecum neuroendocrine tumor G1, colonic lymphangioma, colon leiomyoma, gastric lymphoma** (all L5, Hold) — benign, non-chemotherapy-responsive, or mechanistically unrelated conditions with no supporting clinical trial or literature evidence; likely low-specificity artifacts of the knowledge graph.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 3 RCTs (including two large, completed trials: SALTO, n=161, and the UFT+LV vs. TS-1 adjuvant trial, n=1535) directly support the efficacy of the S-1 combination — which contains Gimeracil — in colorectal cancer. However, this evidence is attributable to the combination product, not Gimeracil as a standalone agent, and Gimeracil has no market authorization or safety labeling in Taiwan.

**To proceed, the following is needed:**
- TFDA-approved package insert data (warnings, contraindications) — currently a Blocking data gap
- Formal mechanism-of-action documentation for Gimeracil specifically (via DrugBank or manufacturer data) — currently a High-severity data gap
- Clarification on whether the repurposing pathway targets Gimeracil alone or the full S-1 combination product, since all supporting clinical evidence is combination-based
- A regulatory strategy given the drug's current unmarketed status in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

