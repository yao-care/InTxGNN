---
layout: default
title: Doxapram
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
---

# Doxapram
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

# Doxapram: From Respiratory Stimulation to Vascular Disease

## One-Sentence Summary

Doxapram is a respiratory stimulant (analeptic) used clinically for drug-induced respiratory depression, post-anesthetic respiratory depression, and apnea of prematurity — acting primarily by stimulating carotid body chemoreceptors to increase respiratory drive.
The TxGNN model predicts it may have activity against **Vascular Disease**, with **0 clinical trials** and **17 publications** currently available; however, none of the literature directly supports a therapeutic application, and several studies indicate potential harm signals.
The overall evidence base is weak, and this candidate is currently rated as **Hold** pending mechanistic clarification.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Respiratory depression (drug-induced, post-anesthetic); apnea of prematurity |
| Predicted New Indication | Vascular Disease |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank record. Based on known pharmacology, Doxapram stimulates peripheral chemoreceptors — primarily the carotid body — and to a lesser extent brainstem respiratory centres. This stimulation increases respiratory rate and tidal volume and is accompanied by a sympathomimetic surge: elevation of blood pressure, heart rate, and cardiac output. It is this hemodynamic footprint that the TxGNN knowledge graph links to the "vascular disease" node cluster.

However, the biological plausibility of a **therapeutic** application in vascular disease is not supported by the available evidence. PMID 10704775 (neonatal rat model) explicitly shows that doxapram **worsened** white matter injury following bilateral carotid artery occlusion. PMID 4398848 records hemodynamic responses in dogs but describes no treatment benefit for vascular pathology. The mechanistic link in this case represents a **potential harm signal** rather than a repurposing opportunity.

In short, the high TxGNN score most likely reflects topological clustering of vascular-related nodes in the knowledge graph — an artefact of doxapram's sympathomimetic side-effect profile — rather than evidence of a genuinely tractable mechanism. The prediction should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 17 retrieved publications are predominantly animal studies, case reports, and retrospective studies. None directly evaluate doxapram as a **treatment** for vascular disease. The table below lists the most informative entries in descending tier order.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [8737758](https://pubmed.ncbi.nlm.nih.gov/8737758/) | 1996 | Clinical Observational (RCT aborted) | Eur J Clin Pharmacol | Randomised trial of doxapram vs. placebo for post-operative hypoxaemia was terminated early due to adverse events; no vascular benefit demonstrated |
| [11743509](https://pubmed.ncbi.nlm.nih.gov/11743509/) | 2001 | Retrospective Cohort | J Pediatrics | Prolonged doxapram therapy in VLBW infants associated with isolated mental developmental delay; raises CNS safety concerns |
| [8870121](https://pubmed.ncbi.nlm.nih.gov/8870121/) | 1996 | Physiological Study (Clinical) | Semin Perinatol | Doxapram studied as a modulator of hypoxic pulmonary vasoconstriction in neonatal piglets; findings inform pulmonary vascular physiology but not systemic vascular therapy |
| [10704775](https://pubmed.ncbi.nlm.nih.gov/10704775/) | 2000 | Animal Study (Neonatal Rat) | Neurosci Lett | Doxapram **accentuated** white matter injury after bilateral carotid artery occlusion; represents a harm signal for cerebrovascular use |
| [4398848](https://pubmed.ncbi.nlm.nih.gov/4398848/) | 1971 | Animal Study (Dog) | Anesth Analg | Documented hemodynamic responses (BP, CO increases) to doxapram in normovolemic and hypovolemic dogs; no therapeutic vascular benefit |
| [4706757](https://pubmed.ncbi.nlm.nih.gov/4706757/) | 1973 | Case Report | Anesthesiology | Single case of recovery from central respiratory failure in a patient with a brainstem lesion; tangentially related to cerebrovascular context only |
| [4764360](https://pubmed.ncbi.nlm.nih.gov/4764360/) | 1973 | Clinical Study | Crit Care Med | Doxapram in critically ill patients — questions whether increased oxygen consumption reflects benefit or debt; hemodynamic concerns highlighted |
| [18371030](https://pubmed.ncbi.nlm.nih.gov/18371030/) | 2008 | Retrospective Veterinary Study | J Vet Intern Med | Comparison of caffeine vs. doxapram for hypercapnia in foals with hypoxic-ischaemic encephalopathy; limited translational value |
| [35318792](https://pubmed.ncbi.nlm.nih.gov/35318792/) | 2022 | Retrospective Veterinary Study | J Vet Emerg Crit Care | Cardiopulmonary arrest in hospitalised birds — doxapram mentioned as a resuscitation agent; no vascular disease relevance |
| [4402447](https://pubmed.ncbi.nlm.nih.gov/4402447/) | 1971 | Clinical Study | Eur J Toxicol | Effects of doxapram on chronic respiratory insufficiency; cardiovascular side effects noted but no vascular treatment data |

> **Note:** PMID 40023176 (PRESTIGE-AF trial on DOACs in intracerebral haemorrhage) appears to be a retrieval artefact unrelated to doxapram; it has been excluded from the table.

---

## India Market Information

Doxapram is **not currently marketed in India**. No drug authorisation licences are on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|------------|-------------------|
| — | — | — | No registered products found |

---

## Safety Considerations

**Drug Interactions (55 interactions identified; selected major interactions below):**

| Interacting Drug | Severity | Clinical Concern |
|-----------------|---------|----------------|
| Bupropion | **Major** | Additive CNS stimulation; increased seizure risk |
| Methylene blue | **Major** | Risk of serotonergic excess and hypertensive crisis |
| Iobenguane (I-131) | **Major** | Sympathomimetic interference with radiopharmaceutical uptake |
| Iohexol | **Major** | Enhanced risk of seizure or cardiovascular toxicity with iodinated contrast |
| Iopamidol | **Major** | Same mechanism as Iohexol |
| Tramadol | **Major** | Additive CNS stimulation; lowered seizure threshold |
| Epinephrine | Moderate | Additive cardiovascular stimulation; hypertension, arrhythmia risk |
| Ephedrine | Moderate | Additive pressor effect |
| Pseudoephedrine | Moderate | Additive sympathomimetic effects |
| Salbutamol / Formoterol / Arformoterol | Moderate | Additive cardiovascular stimulation with beta-agonists |

> For complete warnings and contraindications, please refer to the doxapram package insert. TFDA label data was not available at time of this report (Data Gap DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for doxapram in vascular disease is limited to indirect mechanistic associations and a handful of animal/observational studies — none of which support a therapeutic benefit. Critically, at least one animal study (PMID 10704775) demonstrates that doxapram may **worsen** vascular injury outcomes. The TxGNN prediction appears driven by knowledge graph topology rather than biological plausibility, and the sympathomimetic profile of doxapram raises active safety concerns for patients with vascular conditions.

**To proceed, the following is needed:**

- **MOA verification:** Retrieve full DrugBank mechanism of action data (Data Gap DG002) to confirm or refute any plausible link to vascular biology
- **Safety review:** Obtain and parse the TFDA/CDSCO package insert to fill key warnings and contraindications gap (Data Gap DG001)
- **Mechanistic pre-screening:** Conduct a formal in silico or in vitro assessment to determine whether doxapram has any direct vascular effect (e.g., endothelial, smooth muscle) independent of its sympathomimetic action
- **Harm signal assessment:** The carotid artery occlusion white matter injury data (PMID 10704775) should be evaluated for its relevance to human vascular disease before any further development is considered
- **Re-evaluate lower-ranked predictions:** Indications outside the vascular disease cluster (e.g., apnea of prematurity, respiratory conditions) may yield better evidence-to-mechanism alignment for repurposing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

