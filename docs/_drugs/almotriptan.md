---
layout: default
title: Almotriptan
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 3
---

# Almotriptan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Almotriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Almotriptan is a selective serotonin 5-HT1B/1D receptor agonist (triptan class), approved in multiple countries for the acute treatment of migraine with or without aura in adults.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**,
with **0 registered clinical trials** and **19 publications** currently supporting this direction (primarily covering the broader migraine indication).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute migraine with or without aura (adults) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on published literature, Almotriptan is a selective agonist of serotonin 5-HT1B and 5-HT1D receptors. It acts by causing cranial vasoconstriction and inhibiting the release of pro-inflammatory neuropeptides from trigeminal nerve terminals, thereby interrupting the cascade of events that produces migraine pain. This mechanism is shared by all drugs in the triptan class.

Migraine with brainstem aura (MBA; formerly called "basilar-type migraine") is a subtype of migraine with aura in which aura symptoms originate from the brainstem — including diplopia, dysarthria, tinnitus, vertigo, and ataxia — followed by headache. Because the underlying trigeminovascular and serotonergic pathophysiology is identical to other forms of migraine with aura, the mechanistic rationale for triptan use extends logically to this subtype. Almotriptan is already FDA-approved for migraine with or without aura, and the 2013 International Headache Society reclassification explicitly removed the prior contraindication language around triptan use in what was then called basilar migraine.

The high TxGNN score (99.98%) likely reflects the knowledge graph's recognition that Almotriptan's existing indication and MBA share the same disease ontology branch (migraine → migraine with aura → migraine with brainstem aura). This is less a "true" repurposing prediction and more an indication-extension signal within the same therapeutic axis — a mechanistically coherent finding that merits specialist guidance before formalising a clinical protocol.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Almotriptan in migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [18302700](https://pubmed.ncbi.nlm.nih.gov/18302700/) | 2008 | RCT | Headache | AEGIS Trial: Early intervention with almotriptan vs placebo significantly reduced functional disability and improved health-related quality of life in acute migraine |
| [11768838](https://pubmed.ncbi.nlm.nih.gov/11768838/) | 2001 | RCT | Clinical Therapeutics | Dose-finding RCT: subcutaneous almotriptan was well tolerated and efficacious for acute migraine treatment |
| [18234046](https://pubmed.ncbi.nlm.nih.gov/18234046/) | 2008 | Clinical Study | Headache | Almotriptan effective in both menstrually related and non-menstrually related migraine subtypes; supports broad applicability across migraine variants |
| [30845850](https://pubmed.ncbi.nlm.nih.gov/30845850/) | 2019 | Review | Expert Review of Neurotherapeutics | 20-year narrative review of almotriptan (>15,000 patients in studies; >150 million treated attacks); comprehensive safety and efficacy profile confirmed |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Evidence Assessment | Headache | American Headache Society updated evidence assessment: almotriptan among established first-line agents for acute migraine pharmacotherapy |
| [25916333](https://pubmed.ncbi.nlm.nih.gov/25916333/) | 2015 | Meta-analysis | The Journal of Headache and Pain | Comparative meta-analysis of triptans in migraine with aura; confirms triptan class (including almotriptan) efficacy during headache phase of aura attacks |
| [12455302](https://pubmed.ncbi.nlm.nih.gov/12455302/) | 2002 | Review | AJHP | Comprehensive review of almotriptan pharmacology and pharmacokinetics; FDA-approved for migraine with or without aura; selective 5-HT1B/1D agonist profile confirmed |
| [20945537](https://pubmed.ncbi.nlm.nih.gov/20945537/) | 2010 | Review | Expert Review of Neurotherapeutics | 10-year review including large RCTs and post-marketing data; early treatment (mild pain) yields better sustained pain-free outcomes |
| [14629242](https://pubmed.ncbi.nlm.nih.gov/14629242/) | 2003 | Clinical Study | Headache | Early intervention with almotriptan (at mild pain) improves 1- and 2-hour pain-free rates versus treatment at moderate/severe intensity |
| [15595988](https://pubmed.ncbi.nlm.nih.gov/15595988/) | 2004 | Review | Cephalalgia | Migraine pathophysiology review: cortical spreading depression activates trigeminal afferents; serotonergic modulation central to both aura and headache phases — supports triptan use in aura subtypes |

---

## India Market Information

Almotriptan is currently **not registered** in India. No licence data is available.

---

## Safety Considerations

**Drug Interactions (56 total interactions identified; key interactions listed below):**

| Interacting Drug | Severity | Clinical Concern |
|-----------------|----------|-----------------|
| Dexfenfluramine | **Major** | Serotonin syndrome risk (combined serotonergic activity) |
| Fenfluramine | **Major** | Serotonin syndrome risk |
| Lorcaserin | **Major** | Serotonin syndrome risk |
| Sibutramine | **Major** | Serotonin syndrome risk |
| Dolasetron | **Major** | Combined serotonergic/5-HT3 effects; QT prolongation concern |
| Granisetron | **Major** | Combined serotonergic activity |
| Ondansetron | **Major** | Combined serotonergic activity; QT prolongation concern |
| Palonosetron | **Major** | Combined serotonergic activity |
| Clarithromycin | Moderate | CYP3A4 inhibition may increase almotriptan exposure |
| Aprepitant | Moderate | CYP3A4 inhibition may increase almotriptan exposure |
| Morphine | Moderate | Additive CNS effects possible |

> **Note:** Formal CDSCO package insert warnings and contraindications were not available in this Evidence Pack. Please refer to the full prescribing information before clinical use. Serotonin syndrome is the most clinically significant risk, particularly when co-administered with other serotonergic agents.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Almotriptan is already an approved migraine therapy with a well-characterised 20-year safety record; migraine with brainstem aura is a recognised migraine subtype sharing the same trigemino-vascular pathophysiology, and recent IHS guidelines no longer contraindicate triptan use in this subtype. However, the specific subtype evidence gap (no dedicated RCTs, no India registration) warrants specialist-supervised use rather than broad adoption.

**To proceed, the following is needed:**

- **Formal MOA data:** Retrieve full DrugBank entry (DB00918) to complete mechanism of action documentation
- **India regulatory pathway:** Initiate CDSCO registration or evaluate import licence options, as Almotriptan is currently not marketed in India
- **Subtype-specific evidence:** Commission or identify any prospective observational data for almotriptan specifically in migraine with brainstem aura (ICHD-3 criteria)
- **Package insert review:** Obtain and parse the full prescribing information (EU SmPC or US PI) to document contraindications and black-box warnings formally
- **Neurologist consultation:** Confirm that the prescribing context excludes patients with hemiplegic migraine (where triptans remain relatively contraindicated) and establishes monitoring for atypical aura features
- **Serotonin syndrome protocol:** Given multiple major DDIs with serotonergic agents, a co-medication screening checklist should be developed prior to any clinical protocol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

