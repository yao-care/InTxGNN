---
layout: default
title: Lindane
parent: 僅模型預測 (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
---

# Lindane
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

# Lindane: From Scabies/Pediculosis to Cervical Neuroblastoma

## One-Sentence Summary

Lindane is an organochlorine compound historically used as a topical treatment for scabies and lice infestations (pediculosis). The TxGNN model predicts it may be effective for **Cervical Neuroblastoma**, with **0 clinical trials** and **0 publications** currently supporting this direction. This prediction rests entirely on computational modeling with no empirical evidence whatsoever.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Scabies, pediculosis (lice infestation) — topical ectoparasiticide |
| Predicted New Indication | Cervical Neuroblastoma |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Lindane (gamma-hexachlorocyclohexane, γ-HCH) is an organochlorine insecticide that acts as a GABA-A receptor antagonist—it blocks chloride ion channels in neuronal membranes, causing uncontrolled neuronal excitation and paralysis in ectoparasites. It has been used topically for scabies and lice, though many regulatory agencies have restricted or banned it due to environmental persistence and human toxicity concerns.

The TxGNN model's prediction for cervical neuroblastoma appears to rely on the fact that neuroblastoma cells (neural crest origin) express GABA-A receptors to some extent. The hypothesis might follow that GABA-A modulation could influence tumor cell signaling. However, Lindane is a neuroexcitatory toxin, not a cytostat or apoptosis inducer, and there is no established pathway by which GABA-A chloride channel blockade translates into anti-tumor activity against neuroblastoma.

Most critically, Lindane is classified as an **IARC Group 1 Known Human Carcinogen**, with demonstrated epidemiological association with non-Hodgkin lymphoma (NHL). Applying a known carcinogen to treat a pediatric solid tumor presents a fundamental safety and ethical paradox. Combined with its CNS neurotoxicity, potential ototoxicity, and complete absence of any preclinical or clinical oncology data, this prediction is mechanistically implausible and clinically untenable in its current form.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Lindane currently has no product registrations in India. No authorizations are on record.

---

## Safety Considerations

**Drug Interactions (179 total interactions on record):**

The following are the most clinically significant interactions identified:

| Severity | Interacting Drug | Clinical Concern |
|----------|-----------------|-----------------|
| **Major** | Bupropion | Both agents lower the seizure threshold; co-administration substantially increases seizure risk |
| **Major** | Iopamidol | Intrathecal contrast agents combined with CNS-penetrating GABA antagonists markedly raise neurotoxicity/seizure risk |
| **Major** | Iohexol | Same mechanism as above; avoid concurrent use |
| Moderate | Morphine | Additive CNS/respiratory depression |
| Moderate | Morphine (liposomal) | Same as above |
| Moderate | Opium | Same as above |
| Moderate | Promethazine | Enhanced CNS sedation and neurological effects |
| Moderate | Metoclopramide | Risk of additive extrapyramidal/neurological effects |
| Moderate | Levofloxacin | Fluoroquinolone-GABA antagonism may compound seizure risk |
| Moderate | Ephedrine | Cardiovascular and neurological overstimulation |
| Moderate | Sibutramine | CNS stimulant interaction |
| Moderate | Dronabinol | Unpredictable CNS interaction |
| Moderate | Fenfluramine / Dexfenfluramine / Phentermine / Diethylpropion / Mazindol | Multiple CNS stimulant interactions with seizure risk implications |
| Moderate | Picosulfuric acid / Sodium sulfate / Polyethylene glycol (3350 with electrolytes) | Bowel preparation agents may alter Lindane absorption if co-administered orally |

> ⚠️ **Additional Safety Flags:** Lindane is an IARC Group 1 carcinogen (NHL risk). It demonstrates known CNS neurotoxicity with systemic absorption, suspected ototoxicity, and environmental persistence. It is banned or severely restricted in many jurisdictions. Full package insert warnings and contraindications were not available in this evidence pack—please consult the current prescribing information before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predicted indications for Lindane sit at Evidence Level L5 (model prediction only, zero empirical support), and the top indication—cervical neuroblastoma—carries a mechanistically implausible rationale compounded by Lindane's established carcinogenicity and neurotoxicity. There is no reasonable basis to advance this candidate under current evidence.

**To proceed, the following is needed:**

- Obtain full package insert safety data: warnings, contraindications, and special population restrictions (currently unavailable — blocking gap)
- Confirm complete MOA data via DrugBank API query
- Verify Lindane's current regulatory status in India (whether it is banned, restricted, or subject to special controls)
- Commission focused preclinical studies (in vitro neuroblastoma models) to determine whether any GABA-A–mediated anti-proliferative effect exists at non-toxic concentrations
- Conduct a formal carcinogenicity risk–benefit analysis before any oncology indication development given IARC Group 1 classification
- If preclinical signal is found, a structured safety package addressing genotoxicity, systemic exposure, and pediatric tolerability would be mandatory prior to any first-in-human oncology study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

