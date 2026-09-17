---
layout: default
title: Prasugrel
parent: Model Prediction Only (L5)
nav_order: 687
evidence_level: L5
indication_count: 10
---

# Prasugrel
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Prasugrel: From Antiplatelet Therapy in ACS/PCI to Pulmonary Hypertension

## One-Sentence Summary

Prasugrel is a thienopyridine-class P2Y12 inhibitor used as antiplatelet therapy in patients with acute coronary syndrome (ACS) undergoing percutaneous coronary intervention (PCI). The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, but the **2 clinical trials** and **2 publications** currently retrieved are not actually about Prasugrel or pulmonary hypertension, so this remains a model-only signal with no supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Antiplatelet therapy in acute coronary syndrome / post-PCI (per literature evidence; no official India label text available — see note below) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

*Note: `taiwan_regulatory.licenses` is empty (drug not marketed in India), so no regulatory-label indication text is available. The original indication above is derived from literature evidence in this pack (PMID 21241206), not from an official product label.*

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Prasugrel is a thienopyridine-class P2Y12 inhibitor (the same class as clopidogrel) used in combination with aspirin for at least 12 months following stent placement in ACS patients undergoing PCI, to prevent stent thrombosis and recurrent ischemic events.

The TxGNN model's high score for pulmonary hypertension most likely reflects a knowledge-graph association between antiplatelet drugs and thrombosis-related pulmonary hypertension (e.g., chronic thromboembolic pulmonary hypertension, CTEPH), where microthrombotic mechanisms are pathophysiologically relevant and platelet inhibition could plausibly be applicable.

However, none of the retrieved clinical trials or literature actually study Prasugrel in a pulmonary hypertension population — the two trials concern NOAC management in atrial fibrillation and cancer-associated thrombosis, and the two publications concern clopidogrel/prasugrel adherence after PCI and COVID-19 comorbidity outcomes. The mechanistic link is therefore a plausible hypothesis inferred from drug class, not a substantiated finding.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | N/A | Completed | 500 | Observational cross-sectional study of NOAC management in elderly non-valvular atrial fibrillation patients in Spain; not related to Prasugrel or pulmonary hypertension (relevance grade C) |
| [NCT04846556](https://clinicaltrials.gov/study/NCT04846556) | N/A | Completed | 300 | Retrospective study on eligibility of cancer-associated thrombosis patients for trials like CARAVAGGIO; does not involve Prasugrel or pulmonary hypertension (relevance grade C) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Cohort | Current Medical Research and Opinion | Confirms guideline use of aspirin plus clopidogrel or prasugrel for ≥12 months post-stent in ACS/PCI patients; does not address pulmonary hypertension |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Cohort | Kardiologiia | Examines effect of background cardiovascular therapy on COVID-19 outcomes in a large registry; not specific to Prasugrel or pulmonary hypertension |

## India Market Information

Prasugrel is currently not marketed in India — no registration or product license data is available in this pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the only available clinical trial and literature evidence is unrelated to Prasugrel's use in pulmonary hypertension, and the drug is not currently marketed in India. This is a model-prediction-only signal (L5) with no direct or indirect clinical support.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data (currently a Data Gap, High severity)
- Official safety labeling — key warnings, contraindications, and DDI data (currently a Data Gap, Blocking severity for S1 safety review)
- Targeted literature/trial search specifically on Prasugrel (or thienopyridine-class antiplatelets) in CTEPH or pulmonary hypertension populations
- India regulatory pathway assessment, since the drug currently has zero registrations in-market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

