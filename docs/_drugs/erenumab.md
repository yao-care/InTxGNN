---
layout: default
title: Erenumab
parent: 僅模型預測 (L5)
nav_order: 293
evidence_level: L5
indication_count: 1
---

# Erenumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Erenumab: From Migraine Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Erenumab (Aimovig®) is a fully human monoclonal antibody targeting the CGRP receptor, originally approved by the US FDA (May 2018) and EMA (August 2018) for the preventive treatment of migraine.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**, a specific migraine subtype involving cortical spreading depression extending to the posterior fossa.
This prediction is supported by **0 dedicated clinical trials** and **20 publications**, with a strong mechanistic rationale based on direct CGRP receptor blockade.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Preventive treatment of migraine (episodic and chronic; FDA/EMA approved) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Erenumab is a fully human IgG2 monoclonal antibody that blocks the **CGRP receptor** (AMY1R/CLR complex). Calcitonin gene-related peptide (CGRP) is a potent vasoactive neuropeptide released during migraine attacks, acting as a key mediator of trigeminal neurogenic inflammation and pain transmission. In preclinical assays, erenumab abolishes CGRP-stimulated cAMP production with an IC₅₀ of 2.3 nM and demonstrates greater than 5000-fold selectivity for the CGRP receptor over other calcitonin family receptors.

Migraine with brainstem aura (formerly "basilar-type migraine") is pathophysiologically distinguished by cortical spreading depression (CSD) that propagates into the posterior fossa, triggering massive CGRP release from trigeminal and cervical afferents supplying the brainstem. This makes the CGRP receptor the central mechanistic target for this subtype. Erenumab's blockade of the same receptor implicated in standard migraine—combined with evidence that it reduces headache frequency across migraine phenotypes including aura subtypes (PMID 34928306)—provides strong biological plausibility for efficacy in migraine with brainstem aura.

An important safety consideration is that CGRP plays a physiological protective role in maintaining posterior circulation perfusion. However, existing data (PMID 32867533) indicate that erenumab does not significantly alter cerebral vasomotor reactivity or endothelial function in migraine patients during short-term use, and pooled long-term trial data show no meaningful increase in cardiovascular risk (PMID 36942409). The mechanistic confidence is rated **High** by TxGNN's repurposing rationale module, with a **Moderate** safety concern level requiring ongoing posterior circulation monitoring.

---

## Clinical Trial Evidence

Currently no related clinical trials registered specifically for erenumab in migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30360965](https://pubmed.ncbi.nlm.nih.gov/30360965/) | 2018 | Phase 3b RCT (LIBERTY) | *The Lancet* | Erenumab effective and tolerable in episodic migraine patients who failed 2–4 prior preventives; established core efficacy |
| [34928306](https://pubmed.ncbi.nlm.nih.gov/34928306/) | 2022 | RCT Secondary Analysis | *JAMA Neurology* | Erenumab demonstrated comparable safety and efficacy in migraine with aura vs. without aura; directly relevant to aura subtypes |
| [37012858](https://pubmed.ncbi.nlm.nih.gov/37012858/) | 2023 | Systematic Review | *Int Immunopharmacol* | Confirms erenumab efficacy across episodic and chronic migraine phenotypes; supports broad-spectrum CGRP blockade |
| [36942409](https://pubmed.ncbi.nlm.nih.gov/36942409/) | 2023 | Cohort (Post-hoc pooled) | *Headache* | Long-term erenumab use shows no significant cardiovascular risk elevation, including in high-CV-risk patients with aura |
| [35230406](https://pubmed.ncbi.nlm.nih.gov/35230406/) | 2022 | Clinical Report | *JAMA* | Editorial endorsing erenumab safety and effectiveness in migraine with aura based on 2022 JAMA Neurology analysis |
| [40275185](https://pubmed.ncbi.nlm.nih.gov/40275185/) | 2025 | Biomarker Cohort | *J Headache Pain* | Plasma suPAR (elevated in migraine with aura) associated with response to erenumab; links aura inflammation to CGRP pathway |
| [32867533](https://pubmed.ncbi.nlm.nih.gov/32867533/) | 2021 | Mechanistic/PD Study | *Cephalalgia* | Erenumab does not alter cerebral vasomotor reactivity or flow-mediated dilation; posterior circulation safety supported |
| [35151970](https://pubmed.ncbi.nlm.nih.gov/35151970/) | 2022 | Real-World Observational | *Clin Neurol Neurosurg* | 6-month real-world data in treatment-resistant chronic migraine; confirms tolerability profile |
| [30725283](https://pubmed.ncbi.nlm.nih.gov/30725283/) | 2019 | Review | *Handb Exp Pharmacol* | Comprehensive review of CGRP's role in migraine pathophysiology, including aura and trigeminal-cervical complex activation |
| [38637736](https://pubmed.ncbi.nlm.nih.gov/38637736/) | 2024 | Cohort (Biomarker) | *J Headache Pain* | Dynamic CGRP fluctuations across migraine frequency spectrum; supports CGRP as validated target across phenotypes including aura |

---

## India Market Information

Erenumab is currently **not registered** in India. No marketing authorizations are on record with CDSCO.

For reference, erenumab holds regulatory approval in:
- **USA** (FDA, May 2018): Preventive treatment of migraine in adults, marketed as Aimovig® (70 mg/140 mg monthly subcutaneous injection)
- **EU** (EMA, August 2018): Patients with ≥4 migraine days/month

---

## Safety Considerations

**Drug-Target Pharmacology:**
Erenumab is a selective antagonist antibody at the CGRP receptor (AMY1R/CLR complex). It is 5000-fold selective for the CGRP receptor over other human calcitonin family receptors. The drug has no meaningful small-molecule drug–drug interactions typical of hepatically metabolized compounds, as it is a monoclonal antibody cleared via proteolytic catabolism.

**Vascular Safety in Aura Patients:**
Migraine with aura is independently associated with elevated vascular risk. Pooled long-term clinical trial analysis (PMID 36942409) found no significant increase in cardiovascular or cerebrovascular events attributable to erenumab in high-CV-risk patients. Cerebral hemodynamic studies (PMID 32867533) confirm no alteration of vasomotor reactivity.

**Constipation:**
Class-level adverse effect of CGRP receptor blockade; noted across anti-CGRP antibody class.

> For complete warnings, contraindications, and prescribing information, please refer to the Aimovig® package insert (Amgen/Novartis). TFDA package insert data was not available for this analysis.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Erenumab directly targets the CGRP receptor, which is the primary mediator of the neurogenic inflammation cascade in migraine with brainstem aura. The drug already holds regulatory approval for broad migraine prevention, and secondary analyses of Phase 3 RCTs demonstrate efficacy across aura subtypes (PMID 34928306). No dedicated trials exist for the specific brainstem aura subtype, but the mechanistic overlap is direct, and posterior circulation safety has been assessed. The main barrier is the absence of dedicated evidence and India registration.

**To proceed, the following is needed:**

- **Regulatory pathway**: Apply for CDSCO marketing authorization; consider bridging strategy from existing FDA/EMA approval package
- **Dedicated clinical evidence**: Initiate or identify an observational study or subgroup analysis specifically in migraine with brainstem aura patients (IHS classification 1.2.2) to generate indication-specific data
- **Complete safety dossier**: Obtain and review the full Aimovig® package insert (TFDA/CDSCO format) to fill current data gaps on contraindications and black box warnings (DG001)
- **MOA documentation**: Formally document mechanism of action for the regulatory submission dossier (DG002)
- **Posterior circulation monitoring plan**: Develop a pharmacovigilance protocol for ischemic risk monitoring given the theoretical concern in posterior circulation CGRP blockade in brainstem aura patients
- **Local pharmacoeconomic analysis**: Assess cost-effectiveness and reimbursement feasibility for the India market given the drug's biologic pricing

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application. All predictions from TxGNN require prospective clinical verification.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

