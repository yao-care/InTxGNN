---
layout: default
title: Artemether
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Artemether
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

# Artemether: From Malaria to Acquired Angioedema

## One-Sentence Summary

Artemether is an artemisinin-derived antimalarial drug, established globally as a first-line treatment for *Plasmodium falciparum* malaria, but not currently registered in India.
The TxGNN model predicts it may be effective for **Acquired Angioedema**, with the proposed mechanism involving DHA-mediated inhibition of NF-κB signalling and complement pathway activation.
Currently, **0 clinical trials** and **0 publications** directly support this repurposing direction — evidence is at the model-prediction stage only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malaria (globally established antimalarial; no India registration on record) |
| Predicted New Indication | Acquired Angioedema |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data was not retrieved for this evidence pack. Based on established pharmacology, Artemether is a semi-synthetic methyl ether derivative of dihydroartemisinin (DHA). After oral absorption, it is rapidly metabolised to DHA, which generates carbon-centred free radicals through heme-catalysed cleavage of its endoperoxide bridge. These radicals covalently alkylate PfATP6 — a *Plasmodium falciparum* SERCA-type calcium ATPase — disrupting intracellular calcium homeostasis and damaging mitochondrial membranes to kill erythrocytic-stage parasites. This mechanism is why Artemether (typically co-formulated with lumefantrine as Coartem®) is WHO-recommended as a front-line artemisinin-based combination therapy (ACT).

The predicted connection to **Acquired Angioedema** rests on secondary pharmacological properties of DHA. Preclinical studies have demonstrated that DHA can suppress NF-κB transcription factor activity and attenuate complement pathway activation. Acquired angioedema is pathophysiologically driven by C1-inhibitor deficiency or functional impairment, resulting in uncontrolled kallikrein–kinin system activation and excessive bradykinin generation — ultimately causing increased vascular permeability and episodic tissue swelling. Suppression of complement overactivation could theoretically interrupt part of this cascade, providing a plausible but indirect mechanistic bridge.

However, this mechanistic link remains speculative and has not been experimentally validated. There is no in vitro, in vivo, or clinical data that directly tests Artemether activity against C1-inhibitor deficiency or bradykinin excess. The TxGNN model identifies this association through knowledge-graph topology; the prediction should therefore be treated strictly as a hypothesis requiring dedicated laboratory investigation before any development decision is made.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Artemether in Acquired Angioedema.

---

## Literature Evidence

Currently no related literature available for Artemether in Acquired Angioedema.

---

## India Market Information

Artemether is not currently registered or marketed in India. No product authorisations are on record in the regulatory database.

---

## Safety Considerations

**Drug Interactions** (95 total interactions identified; representative selection shown below):

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Clarithromycin | **Major** | Strong CYP3A4 inhibitor; may significantly increase artemether plasma exposure and toxicity risk |
| Cobicistat | **Major** | Potent CYP3A4 pharmacokinetic booster (used in HIV regimens); high risk of artemether accumulation |
| Amprenavir | **Major** | HIV protease inhibitor; CYP3A4-mediated bidirectional interaction |
| Apalutamide | **Major** | Strong CYP3A4 inducer; may substantially reduce artemether efficacy |
| Atazanavir | **Major** | HIV protease inhibitor; potential for mutual PK interference |
| Boceprevir | **Major** | HCV NS3/4A protease inhibitor; CYP3A4 interaction risk |
| Dexamethasone | Moderate | CYP3A4 inducer; may reduce artemether blood levels |
| Miconazole | Moderate | CYP3A4 inhibitor; increased artemether exposure possible |
| Deferasirox | Moderate | Iron chelator; potential pharmacokinetic interaction |
| Fostamatinib | Moderate | CYP3A4 substrate overlap; monitor for adverse effects |

> A total of **95 drug–drug interactions** have been catalogued (source: DDInter). The full interaction profile should be reviewed before any co-administration.

Please refer to the package insert for complete warnings and contraindications, as these data were not available in the current evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.90%), there is currently zero experimental or clinical evidence supporting Artemether as a treatment for acquired angioedema. The proposed mechanistic bridge through DHA's NF-κB/complement-inhibitory activity is biologically plausible in concept, but has not been tested in any angioedema-relevant disease model, making advancement premature.

**To proceed, the following is needed:**
- In vitro studies evaluating DHA/Artemether activity in C1-inhibitor deficiency models or bradykinin generation assays
- In vivo validation in established animal models of acquired or hereditary angioedema (e.g., C1-INH knockout mouse models)
- Systematic literature review of Artemether's anti-inflammatory and immunomodulatory properties, with particular focus on complement and kallikrein–kinin pathway interactions
- Retrieval of full prescribing information (package insert) to complete the safety profile, including warnings, contraindications, and teratogenicity data (currently not available)
- India regulatory pathway assessment (CDSCO import/new drug application requirements) if preclinical results are encouraging

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

