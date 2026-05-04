---
layout: default
title: Alpelisib
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 10
---

# Alpelisib
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

# Alpelisib: From HR+/HER2- Advanced Breast Cancer to Pulmonary Hypertension

## One-Sentence Summary

Alpelisib (Piqray®) is a selective PI3Kα inhibitor used in combination with fulvestrant for the treatment of HR+/HER2- advanced breast cancer harboring PIK3CA mutations.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension** with a score of 99.03%, however the **1 retrieved clinical trial** and **2 publications** both represent adverse event signals rather than therapeutic evidence — making this prediction a likely false positive.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HR+/HER2- advanced breast cancer with PIK3CA mutation (post-aromatase inhibitor therapy) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Alpelisib is a selective inhibitor of PI3Kα (the alpha isoform of phosphoinositide 3-kinase, encoded by PIK3CA). By blocking the PI3K/AKT/mTOR signaling cascade, it suppresses tumor cell growth and proliferation in PIK3CA-mutated cancers. This mechanism provides its approved efficacy in HR+/HER2- advanced breast cancer, where aberrant PI3Kα activity is a primary oncogenic driver.

The theoretical rationale for pulmonary hypertension is rooted in vascular biology: the PI3K/AKT/mTOR pathway is known to promote pulmonary arterial smooth muscle cell (PASMC) proliferation and vascular remodeling — the central pathological features of pulmonary arterial hypertension (PAH). Selective PI3Kα inhibition could, in principle, attenuate PASMC hyperplasia and reverse adverse vascular remodeling. This provides a plausible mechanistic bridge between the drug's molecular target and the predicted indication.

However, the available evidence contradicts any therapeutic benefit in this setting. One case report documents alpelisib-induced interstitial lung disease in a breast cancer patient, and a preclinical study shows PI3Kα pathway inhibition combined with doxorubicin causes biventricular cardiac atrophy and right ventricular dysfunction. These findings suggest that alpelisib carries pulmonary and cardiopulmonary **toxicity risk** in the context of lung disease, rather than benefit. The sole retrieved clinical trial is a breast cancer real-world study with no connection to pulmonary hypertension. This prediction is most likely a graph-distance inference artifact in the knowledge graph.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06705504](https://clinicaltrials.gov/study/NCT06705504) | N/A | Completed | 435 | Multinational retrospective cohort study (REASSURE) assessing real-world effectiveness and safety of ribociclib or alpelisib in HR+/HER2- advanced or metastatic breast cancer (Europe, 2018–2021). **No relation to pulmonary hypertension** — retrieved due to a data-mapping artifact. |

> ⚠️ The only retrieved trial has no relevance to pulmonary hypertension (relevance grade C). No dedicated clinical trial investigating alpelisib for pulmonary hypertension has been identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | Case Report | J Oncol Pharm Pract | Alpelisib-induced interstitial lung disease (ILD) in a patient with advanced breast cancer. This is an **adverse event report** — not evidence of therapeutic benefit in pulmonary hypertension. |
| [31039672](https://pubmed.ncbi.nlm.nih.gov/31039672/) | 2019 | Preclinical Study | J Am Heart Assoc | PI3Kα pathway inhibition combined with doxorubicin produces distinct biventricular cardiac atrophy and right ventricular dysfunction in a preclinical model. **Signals potential cardiopulmonary toxicity** from PI3Kα inhibition rather than benefit. |

> ⚠️ Both publications represent **negative signals** for pulmonary use of alpelisib. Neither supports therapeutic investigation in pulmonary hypertension.

---

## India Market Information

Alpelisib is currently **not marketed in India**. No approved licenses or drug registrations have been identified.

---

## Cytotoxicity

Alpelisib is an antineoplastic targeted therapy used in oncology; this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — selective PI3Kα inhibitor (not a conventional cytotoxic agent) |
| Myelosuppression Risk | Low (PI3Kα inhibition does not primarily target hematopoietic cells; mild anemia reported at low frequency) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Fasting blood glucose and HbA1c (hyperglycemia is the most common Grade 3/4 adverse event), CBC with differential, liver function, renal function, skin (rash), pulmonary status (ILD surveillance) |
| Handling Protection | Standard oncology drug handling precautions; not classified as a conventional cytotoxic requiring special containment |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Known class-level alert:** Hyperglycemia is the most clinically significant adverse event associated with alpelisib (Grade 3/4 incidence ~37% in the SOLAR-1 pivotal trial). Baseline fasting glucose and HbA1c screening is essential before initiation, with antidiabetic therapy co-management if needed. Alpelisib-induced interstitial lung disease has also been documented (PMID 35730191), which is particularly relevant given the predicted indication is a pulmonary disease.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score of 99.03% for pulmonary hypertension is not supported by any meaningful therapeutic evidence — the sole retrieved clinical trial is a breast cancer study, and both literature items describe adverse pulmonary and cardiac effects of alpelisib rather than benefit. The mechanistic hypothesis, while theoretically plausible, is directly contradicted by the existing safety signals in lung and cardiac tissue.

**To proceed, the following would be needed:**

- Dedicated preclinical studies assessing alpelisib (or a selective PI3Kα inhibitor) in validated PAH animal models (e.g., monocrotaline or chronic hypoxia models), with explicit measurement of PASMC proliferation endpoints
- Contextualisation of the ILD adverse event signal: determining whether alpelisib's pulmonary toxicity is exclusive to patients with pre-existing malignancy-related lung compromise or a broader class effect
- Isoform selectivity clarification: establishing whether PI3Kα (vs. PI3Kβ or PI3Kδ) specifically drives PASMC proliferation — the published PAH mechanistic literature more broadly implicates pan-PI3K activity
- If preclinical signals are positive: identification of a PIK3CA-dysregulated PAH patient subgroup as a potential biomarker-selected population
- Detailed MOA and safety data retrieval from DrugBank and the approved package insert to complete the pharmacological safety profile before any further development decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

