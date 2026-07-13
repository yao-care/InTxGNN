---
layout: default
title: Isoflurane
parent: 僅模型預測 (L5)
nav_order: 321
evidence_level: L5
indication_count: 7
---

# Isoflurane
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Isoflurane: From General Anaesthesia to Prinzmetal Angina

## One-Sentence Summary

Isoflurane is a volatile halogenated inhalation agent used as the primary drug for induction and maintenance of general anaesthesia in surgical settings.
The TxGNN model predicts it may be effective for **Prinzmetal Angina** (variant angina caused by coronary artery vasospasm),
with a prediction score of **99.67%** but **no supporting clinical trials or published literature** identified for this specific indication.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | General Anaesthesia (inhalation induction and maintenance) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacology, Isoflurane is a halogenated volatile anaesthetic whose CNS effects are mediated primarily through potentiation of GABA-A receptors and inhibition of NMDA glutamate receptors. At the cardiovascular level, Isoflurane produces dose-dependent vasodilation and reduces systemic vascular resistance.

The TxGNN model may have linked Isoflurane to Prinzmetal Angina through this vasodilatory profile: since Prinzmetal Angina is driven by episodic coronary artery vasospasm, a vasodilator in principle could reduce spasm severity. This mechanistic path is biologically plausible in the abstract.

However, this prediction carries a **well-recognised, serious counterargument**: Isoflurane is known to cause **coronary steal syndrome** — preferential dilation of non-stenotic vessels that diverts blood flow away from ischaemic myocardium. This adverse effect makes Isoflurane potentially harmful rather than therapeutic in patients with coronary artery disease, including variant angina. The mechanism is therefore bidirectional, with the harmful direction better-established than any potential benefit. No clinical or preclinical study supports this repurposing direction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the Prinzmetal Angina indication.

---

## Safety Considerations

**Drug Interactions** (38 total interactions identified):

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|---------------|
| Epinephrine | **Major** | Isoflurane sensitises the myocardium to catecholamines; concurrent epinephrine significantly increases the risk of ventricular arrhythmias |
| Morphine | Moderate | Additive CNS and respiratory depression; careful dose titration required |
| Opium | Moderate | Additive CNS and respiratory depression |
| Ondansetron, Metoclopramide, Ranitidine, Famotidine, Pantoprazole, Omeprazole | Unknown | Interaction magnitude unclear; monitor in perioperative setting |
| Dexamethasone, Hydrocortisone | Unknown | Potential haemodynamic interactions; clinical significance unclear |
| Vancomycin, Metronidazole | Unknown | No well-characterised PK/PD interaction; monitor |
| Mannitol | Unknown | Both agents affect intracranial pressure; monitor in neurosurgical contexts |

Please refer to the package insert for complete warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure model-prediction finding (L5) with no supporting clinical trials, no supportive literature for the Prinzmetal Angina indication, and a mechanistic concern — coronary steal syndrome — that actively argues against safety in this patient population. The benefit-risk ratio is unfavourable without any further evidence.

**To proceed, the following would be needed:**

- Preclinical studies in vasospasm animal models demonstrating net coronary vasodilatory benefit without steal — this is the minimum bar before any human research can be justified
- Detailed MOA characterisation (DrugBank / peer-reviewed pharmacology sources) to verify whether any Isoflurane target directly modulates coronary vasospasm pathways independent of the steal mechanism
- A clinical-use-case framing: if explored at all, it would need to be in a tightly controlled inpatient/ICU setting with continuous haemodynamic monitoring, not as a conventional therapeutic
- Formal safety review addressing the coronary steal syndrome risk before this candidate can be elevated from Hold to any active development stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

