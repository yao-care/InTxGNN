---
layout: default
title: Lynestrenol
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
---

# Lynestrenol
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

# Lynestrenol: From Progestogen / Oral Contraceptive to Migraine with or without Aura

## One-Sentence Summary

Lynestrenol (historically marketed as Orgametril) is a synthetic progestogen primarily used as an oral contraceptive and for hormone-related conditions, with a historical record of use in migraine prophylaxis.
The TxGNN model predicts it may be relevant for **Migraine with or without Aura (Susceptibility)**, with **no registered clinical trials** but **20 publications** exploring the neurobiological overlap between epilepsy and migraine that forms the mechanistic backbone of this prediction.
Currently, Lynestrenol is not marketed in India and detailed MOA and safety data require supplementation before this candidate can be formally evaluated.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Progestogen / Oral contraceptive (no India registration found) |
| Predicted New Indication | Migraine with or without aura, susceptibility to |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L4 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacology, Lynestrenol is a synthetic progestogen that is rapidly converted to norethisterone (a potent progestin) in the body. Its primary clinical use has been in hormonal contraception and management of menstrual disorders; notably, it was marketed as Orgametril and investigated for migraine prophylaxis as early as the 1960s (see PMID 14091721).

The top-ranked TxGNN indication — "migraine with or without aura, susceptibility to" — is closely connected to epilepsy through shared pathophysiology. Both conditions involve abnormal neuronal excitability, ion channel dysfunction (notably SCN1A variants), and neuroinflammatory cascades. The literature evidence pack predominantly captures this epilepsy-migraine mechanistic overlap, including shared genetic susceptibility (SCN1A polymorphisms, MTHFR methylation pathway) and bidirectional neuroinflammation, which likely drove the model's high prediction score for migraine susceptibility.

The proposed pharmacological rationale is that progesterone and its metabolites may modulate neuronal excitability thresholds — possibly through neuroactive steroid metabolites (e.g., partial conversion toward allopregnanolone-like compounds that act as GABA-A positive allosteric modulators) or by stabilizing estrogen-cycle fluctuations that trigger menstrual migraine. However, this mechanistic link remains inferential, and there is a well-established safety concern: combined hormonal agents (especially those with progestogenic activity) in migraine **with aura** patients are associated with elevated stroke risk due to interactions with cortical spreading depression. This safety signal significantly limits the direct repurposing pathway.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

*(Extracted from predicted_indications\[0\] — "migraine with or without aura, susceptibility to"; literature primarily addresses the epilepsy-migraine mechanistic overlap underpinning the TxGNN prediction)*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33856647](https://pubmed.ncbi.nlm.nih.gov/33856647/) | 2021 | Review | Molecular Neurobiology | Epilepsy and migraine share ion channel mutations (SCN1A), serotonergic pathways, and neuroinflammation; discusses overlapping therapeutic strategies relevant to both conditions |
| [23294289](https://pubmed.ncbi.nlm.nih.gov/23294289/) | 2013 | Genetic Study | Epilepsia | Demonstrates shared genetic susceptibility to migraine and epilepsy in the EPGP cohort, supporting the comorbidity via common genetic architecture |
| [17460155](https://pubmed.ncbi.nlm.nih.gov/17460155/) | 2007 | Genetic Linkage Study | Neurology | Familial occipitotemporal lobe epilepsy co-segregating with migraine with visual aura mapped to chromosome 9q; direct genetic link between epilepsy and migraine with aura |
| [24076350](https://pubmed.ncbi.nlm.nih.gov/24076350/) | 2014 | Meta-analysis | Gene | SCN1A IVS5N+5G>A polymorphism associated with epilepsy with febrile seizures susceptibility; SCN1A is also implicated in familial hemiplegic migraine pathogenesis |
| [30267335](https://pubmed.ncbi.nlm.nih.gov/30267335/) | 2018 | Meta-analysis | Neurological Sciences | MTHFR C677T polymorphism as a risk factor for epilepsy; MTHFR is independently associated with migraine susceptibility, suggesting a shared metabolic/methylation pathway |
| [34575901](https://pubmed.ncbi.nlm.nih.gov/34575901/) | 2021 | Review | Int J Mol Sci | Molecular targets for antiepileptogenesis; several targets (neuroinflammation, mTOR, GABAergic modulation) are also relevant in migraine prevention strategies |
| [34209535](https://pubmed.ncbi.nlm.nih.gov/34209535/) | 2021 | Review | Int J Mol Sci | Bidirectional neuroinflammation in epilepsy — neuroinflammatory cascades are also central to migraine pathophysiology and represent a potential shared therapeutic target |
| [22266888](https://pubmed.ncbi.nlm.nih.gov/22266888/) | 2011 | Review | Seminars in Neurology | Genetics of epilepsy as a heterogeneous neurological disorder; highlights genetic modulators of neuronal excitability applicable to migraine susceptibility research |
| [16201993](https://pubmed.ncbi.nlm.nih.gov/16201993/) | 2005 | Review | Epilepsia | Developmental changes in GABAergic and glutamatergic receptor composition drive neuronal excitability; relevant to understanding how neuroactive steroids (including progestogen metabolites) may modulate seizure and migraine thresholds |
| [28086980](https://pubmed.ncbi.nlm.nih.gov/28086980/) | 2017 | Review | Journal of Neuroinflammation | Neuroinflammation in post-traumatic epileptogenesis; highlights overlapping inflammatory mediators (COX-2, IL-1β, TGF-β) also implicated in central sensitization during migraine attacks |

> **Note for reviewers:** The most directly relevant Lynestrenol-migraine publication — a 1963 historical clinical observation on prophylactic migraine treatment with Lynestrenol/Orgametril (PMID [14091721](https://pubmed.ncbi.nlm.nih.gov/14091721/)) — appears in the Rank 2 indication ("migraine disorder") evidence set. A 2026 comparative review of combined oral contraceptives in migraine (PMID [41723577](https://pubmed.ncbi.nlm.nih.gov/41723577/)) is also available there. Both are highly relevant to the overall evaluation of this candidate.

---

## India Market Information

Lynestrenol is currently **not marketed in India**. No registered products were identified in the regulatory database (total registrations: 0). Regulatory approval would need to be pursued from the ground up if this candidate advances.

---

## Safety Considerations

- **Critical Safety Signal:** As a progestogen with partial conversion to norethisterone, Lynestrenol shares the class safety concern that **combined hormonal contraceptive-class agents are contraindicated in migraine with aura** due to increased ischemic stroke risk. This is a major limiting factor for the primary predicted indication.

Please refer to the package insert for complete safety information. Package insert review (TFDA/CDSCO) is currently pending and flagged as a blocking data gap (DG001).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.51%), the evidence supporting Lynestrenol for migraine with or without aura susceptibility is limited to mechanistic and genetic overlap studies (L4), with no clinical trials and no direct clinical evidence. More critically, the predicted indication (migraine with aura) sits in direct conflict with a well-established class safety concern — progestogenic hormonal agents are generally contraindicated in this patient population due to elevated stroke risk.

**To proceed, the following is needed:**

- **MOA documentation:** Retrieve full DrugBank API entry for DB12474 to confirm mechanism, receptor targets, and neuroactive metabolite profile (addresses DG002)
- **Regulatory safety review:** Download and parse the CDSCO/TFDA package insert PDF to obtain key warnings, contraindications, and drug interaction data (addresses DG001, currently Blocking)
- **Safety differentiation analysis:** Assess whether Lynestrenol's specific pharmacological profile (progestogen-only, without estrogen) meaningfully separates it from the stroke-risk concern associated with combined hormonal contraceptives in migraine with aura patients
- **Historical evidence retrieval:** Obtain full text of PMID 14091721 (1963 Orgametril migraine prophylaxis study) to characterize the clinical population, dosing, and outcomes from the historical use case
- **Preclinical study design:** If the safety differentiation analysis is favorable, design a preclinical study targeting cortical spreading depression and trigeminovascular pathway modulation by Lynestrenol/norethisterone
- **India regulatory pathway assessment:** Evaluate what is required for first-in-India approval given zero existing registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

