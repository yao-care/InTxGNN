---
layout: default
title: Blonanserin
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 9
---

# Blonanserin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Blonanserin: From Schizophrenia to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Blonanserin is an atypical antipsychotic approved in Japan (marketed as Lonasen®), primarily acting as a D2/D3 and 5-HT2A receptor antagonist for the treatment of schizophrenia.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, with a prediction score of **99.98%** — however, there are currently **0 clinical trials** and **0 publications** supporting this direction.
This prediction is classified as a model-only signal and warrants careful scrutiny before any further development.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia (approved in Japan) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the India regulatory dataset. Based on pharmacological target data, Blonanserin (CAS 132810-10-7) is a synthetic organic compound that antagonises the **D2/D3 dopamine receptors** (DRD2, gene ID 1813) and **5-HT2A serotonin receptors** (HTR2A, gene ID 3356). This dual receptor blockade profile is the basis for its antipsychotic activity in schizophrenia treatment.

Retinal dystrophy with or without extraocular anomalies is a group of hereditary, progressive photoreceptor and retinal pigment epithelium (RPE) degenerative diseases driven by genetic mutations such as RPGR and RPGRIP1L. While the retina does contain dopaminergic amacrine neurons — which modulate contrast sensitivity and circadian adaptation — their functional role is distinct from the genetic and structural mechanisms underlying inherited retinal dystrophy. Blonanserin's D2/5-HT2A antagonism has no known pharmacological intersection with photoreceptor structural maintenance or genetic defect repair pathways.

The TxGNN model produces a high numerical score for this pairing, but this is most likely a **model false positive**. The biological plausibility is very low: the primary pathology in retinal dystrophy is irreversible photoreceptor degeneration driven by structural gene mutations, a disease mechanism that dopamine receptor modulation cannot address. This prediction does not rise above a speculative computational association at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Blonanserin is currently **not registered or marketed in India**. No product licenses are on file.

---

## Safety Considerations

**Drug-Receptor Interactions (Pharmacological Targets):**
Based on available pharmacology data, Blonanserin acts on the following human receptors:

- **5-HT2A receptor** (HTR2A, ENSG00000102468) — antagonism contributes to atypical antipsychotic profile
- **D2 receptor** (DRD2, ENSG00000149295) — blockade underlies antipsychotic efficacy and extrapyramidal side-effect risk

> For full prescribing warnings, contraindications, and drug interaction data, please refer to the Japanese package insert (Lonasen®), as India-specific labelling data is not available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero clinical or preclinical evidence supporting Blonanserin's use in retinal dystrophy. The mechanistic link between D2/5-HT2A receptor antagonism and hereditary photoreceptor degeneration is not established, and the TxGNN high-score prediction is assessed as a likely model false positive for this indication.

**To proceed, the following would be needed:**

- **Mechanistic validation**: Identify any credible biological pathway linking D2 or 5-HT2A receptor modulation to photoreceptor/RPE cell survival in retinal dystrophy models
- **Preclinical proof-of-concept**: In vitro or in vivo studies in retinal dystrophy animal models (e.g., rd1, rd10 mice) before any human study could be considered
- **India package insert / safety dossier**: Obtain TFDA/CDSCO-equivalent labelling data to complete the safety assessment (Data Gaps DG001 and DG002 must be resolved)
- **DrugBank MOA data**: Retrieve full mechanism of action profile to enable proper mechanistic relevance scoring
- **Regulatory pathway assessment**: Confirm whether Blonanserin would require a new drug application in India before any clinical investigation could begin
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

