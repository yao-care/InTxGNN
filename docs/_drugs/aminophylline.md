---
layout: default
title: Aminophylline
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
---

# Aminophylline
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

# Aminophylline: From Bronchospasm to Migraine Disorder

## One-Sentence Summary

Aminophylline is a methylxanthine compound used as a bronchodilator for the management of bronchospasm and asthma, belonging to the same pharmacological class as caffeine and theophylline.
The TxGNN model predicts it may be effective for **Migraine Disorder** (TxGNN score 99.88%), with **0 registered clinical trials** and **6 publications** currently supporting this direction.
The available evidence is primarily mechanistic and observational, centred on the adenosine signalling pathway.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bronchospasm / Asthma (pharmacological class; no India regulatory record available) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L3 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Aminophylline is a water-soluble salt of theophylline and ethylenediamine. Its two primary mechanisms are non-selective adenosine receptor antagonism (A1/A2A subtypes) and phosphodiesterase (PDE) inhibition, which elevates intracellular cyclic AMP. Detailed pharmacodynamic data from the regulatory database are currently unavailable; the following rationale draws on the published literature and the mechanistic notes embedded in the Evidence Pack.

The adenosine pathway provides a biologically coherent bridge to migraine. During a migraine attack, activation of A2A receptors on meningeal nociceptors is associated with trigeminovascular sensitisation and meningeal vasodilation. Two lines of evidence support this: (1) regadenoson, a selective A2A agonist used in cardiac stress testing, has been documented to trigger hemiplegic migraine episodes that are reversible with methylxanthines including aminophylline (PMID 34308528); (2) in vitro data show adenosine selectively dilates intracranial pial arteries but not extracranial vessels (PMID 219563), pointing to a site-specific mechanism relevant to migraine headache.

Caffeine — a first-degree pharmacological relative of aminophylline sharing both adenosine antagonism and PDE inhibition — is already an established adjuvant in combination migraine therapies. A 2023 review and observational case series (PMID 38059379) directly proposes that pathologically elevated adenosine drives migraine via impaired brain energy metabolism, and presents direct clinical observations showing strong therapeutic benefit from aminophylline in pain and headache. This class-level validation, combined with the reverse-pharmacology evidence from regadenoson cases, makes the TxGNN prediction mechanistically plausible.

---

## Clinical Trial Evidence

Currently no clinical trials directly evaluating Aminophylline for Migraine Disorder are registered on ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Review / Case Series | *Pain Management* | Proposes migraine is driven by impaired brain energy metabolism and pathologically high adenosine. Aminophylline, as an adenosine receptor antagonist, is reported to provide strong therapeutic relief in pain and post-dural headache; a published observational case series demonstrates direct clinical benefit in migraine. |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Case Report | *Journal of Nuclear Cardiology* | Regadenoson (selective A2A adenosine agonist) triggered a hemiplegic migraine episode during cardiac stress imaging. Symptoms were reversed by methylxanthines including aminophylline — reverse pharmacological proof of concept for the adenosine–migraine axis. |
| [219563](https://pubmed.ncbi.nlm.nih.gov/219563/) | 1979 | In Vitro | *Stroke* | Adenosine and adenine compounds selectively dilated feline and human intracranial pial arteries (but not extracranial arteries) in vitro, with effects amplified by elevated vascular tone. Provides a mechanistic basis for intracranial-specific adenosine involvement in migraine. |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Case Report | *Canadian Journal of Cardiology* | A patient with "myocardial migraine" (Syndrome X with excessive adenosine effect) experienced disabling pain without ischaemia; dipyridamole (an adenosine potentiator) reproduced the pain, illustrating adenosine-mediated vascular pain pathways. |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Review | *Aggiornamenti clinicoterapeutici* | Historical Italian clinical observations on pharmacological treatment of headache; provides early contextual evidence of xanthine-class drugs in headache management. |

---

## India Market Information

Aminophylline (DB01223) currently holds **no regulatory authorisations** in India. The drug is not marketed and no licence records are on file.

---

## Safety Considerations

**Drug Interactions:** Aminophylline has a total of **279 documented interactions**. The most clinically significant are listed below:

| Severity | Interacting Drug | Clinical Relevance |
|---------|-----------------|-------------------|
| **Major** | Bupropion | Risk of serious adverse effects (seizure threshold lowering); co-administration warrants close monitoring or avoidance |
| Moderate | Clarithromycin | CYP3A4/CYP1A2 inhibition raises theophylline plasma levels; dose adjustment may be required |
| Moderate | Cimetidine | CYP1A2 inhibition increases aminophylline exposure; consider alternative H2-blocker |
| Moderate | Famotidine, Ranitidine, Nizatidine | Moderate H2-blocker interactions; monitor aminophylline levels |
| Moderate | Dexamethasone, Hydrocortisone, Budesonide, Betamethasone, Triamcinolone | Corticosteroids may alter aminophylline metabolism; clinically relevant in respiratory co-treatment |
| Moderate | Doxycycline, Tetracycline, Minocycline | Tetracycline-class antibiotics may affect aminophylline pharmacokinetics |
| Minor | Lansoprazole | Minimal interaction; routine monitoring sufficient |

Please refer to the package insert for complete warnings and contraindications — this information represents a currently blocking data gap that must be resolved before clinical use assessment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The adenosine-antagonism hypothesis linking aminophylline to migraine relief is biologically coherent, supported by a dedicated 2023 review/case series (PMID 38059379), reverse pharmacological evidence from regadenoson case reports, and the established clinical precedent of caffeine as a migraine adjuvant. However, no prospective clinical trials have yet been conducted specifically for this indication, and the drug is not currently marketed in India.

**To proceed, the following is needed:**

- **Resolve blocking safety gap (DG001):** Obtain and review the package insert (warnings, contraindications, and special population precautions) before any clinical planning
- **Confirm mechanism of action data (DG002):** Query DrugBank API to formally document Aminophylline's pharmacodynamic profile
- **Design a prospective proof-of-concept study:** A small randomised controlled trial evaluating aminophylline for acute migraine rescue or as a prophylactic adjuvant would elevate evidence from L3 to L2
- **Clarify optimal route and dosing:** Determine whether intravenous, oral, or rectal administration is appropriate for a migraine indication; review pharmacokinetic data for non-IV routes
- **Drug interaction review in migraine context:** Assess compatibility with commonly co-prescribed migraine medications (triptans, ergotamines, NSAIDs, antiemetics) given the 279 documented interactions
- **India regulatory pathway assessment:** Determine the requirements for a new indication filing or an investigational new drug application, given the drug's current non-marketed status in India

> ⚠️ *This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

