---
layout: default
title: Mebendazole
parent: 僅模型預測 (L5)
nav_order: 408
evidence_level: L5
indication_count: 10
---

# Mebendazole
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

# Mebendazole: From Intestinal Helminth Infections to Echinococcosis

## One-Sentence Summary

Mebendazole is a benzimidazole anthelmintic established for treating intestinal parasitic worm infections, including roundworm, whipworm, hookworm, and pinworm.
The TxGNN model identifies **Alveolar Echinococcosis** as the most evidentially supported predicted indication, with **1 clinical trial** and **20 publications** currently providing supporting data — consistent with Mebendazole's WHO-recognized role as an established alternative benzimidazole therapy for echinococcosis.
However, Mebendazole is not currently registered in India, and pharmacokinetic challenges related to oral bioavailability remain a practical barrier for echinococcosis treatment.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Intestinal parasitic infections (ascariasis, trichuriasis, hookworm, enterobiasis / pinworm) |
| Predicted New Indication | Alveolar Echinococcosis (*Echinococcus multilocularis* infection) |
| TxGNN Prediction Score | 94.2% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## All TxGNN Predicted Indications

This Evidence Pack covers **10 predicted indications** for Mebendazole. The table below summarizes all predictions ranked by TxGNN score.

| Rank | Indication | TxGNN Score | Evidence Level | Mechanistic Link | Recommendation |
|------|-----------|-------------|----------------|-----------------|----------------|
| 1 | Acne (disease) | 99.2% | L5 | None — graph proximity artifact, no biological basis | Hold |
| 2 | Leishmaniasis, diffuse cutaneous | 98.4% | L5 | Weak indirect (Leishmania carries β-tubulin but structural differences limit applicability) | Hold |
| 3 | Echinococcus granulosus infectious disease | 95.6% | L3 | **Direct** — established benzimidazole anti-tubulin mechanism | Proceed with Guardrails |
| 4 | Hordeolum | 94.9% | L5 | None — staphylococcal eyelid infection, bacterial etiology unrelated | Hold |
| 5 | **Alveolar echinococcosis** | **94.2%** | **L3** | **Direct** — established benzimidazole anti-tubulin mechanism | **Proceed with Guardrails** |
| 6 | Inhalational botulism | 93.8% | L5 | None — neurotoxin-mediated mechanism has no connection to anthelmintics | Hold |
| 7 | Toxin-mediated infectious botulism | 93.5% | L5 | None — same neurotoxin rationale as above | Hold |
| 8 | Impetigo | 93.2% | L5 | None — gram-positive bacterial skin infection unrelated | Hold |
| 9 | Sorsby's fundus dystrophy | 93.1% | L5 | None — TIMP3 genetic retinal disease has no pharmacological connection | Hold |
| 10 | Demodicidosis of sebaceous gland | 93.0% | L5 | Weak indirect (*Demodex* is an arthropod with tubulin, but standard treatments are ivermectin/permethrin) | Hold |

> **Key finding**: Among all 10 TxGNN predictions, only **Echinococcus granulosus** (rank 3) and **Alveolar echinococcosis** (rank 5) carry direct mechanistic support and clinical literature evidence. The top-scoring prediction (acne, 99.2%) reflects knowledge graph structural proximity rather than true drug-disease biology, and is not supported by any mechanistic or clinical data.

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in this Evidence Pack. Based on established pharmacology, Mebendazole is a benzimidazole-class anthelmintic that selectively binds β-tubulin in helminths and inhibits tubulin polymerization, preventing microtubule assembly. This disrupts the parasite's cytoskeletal integrity, blocks glucose uptake, and ultimately causes parasite immobilization and death. The key feature of this mechanism is its selectivity for helminth tubulin over mammalian tubulin at therapeutic doses.

Both *Echinococcus granulosus* (causing cystic echinococcosis, CE) and *Echinococcus multilocularis* (causing alveolar echinococcosis, AE) are cestode tapeworms whose larval metacestode stages carry β-tubulin susceptible to benzimidazole inhibition. For CE, mebendazole impairs protoscolex viability and germinal layer integrity of hydatid cysts. For AE — the more dangerous form, with infiltrative growth resembling cancer — mebendazole inhibits vesicular metacestode budding and proliferation by the same mechanism. WHO guidelines have formally recognized both albendazole and mebendazole as the standard benzimidazole chemotherapy options for echinococcosis since the 1990s. Albendazole is preferred due to superior oral bioavailability and tissue penetration, but mebendazole is an established, guideline-endorsed alternative.

The mechanistic bridge from intestinal nematode treatment to echinococcal cestode disease is pharmacologically coherent — the anti-tubulin target is conserved across helminth classes. The defining challenge for echinococcosis specifically is the need for high, sustained plasma mebendazole concentrations (target >0.25 µmol/L) to reach tissue-embedded metacestodes, a pharmacokinetic requirement that demands therapeutic drug monitoring (TDM). This is especially important when CYP-inducing antiepileptic drugs such as carbamazepine, phenytoin, or phenobarbital are co-prescribed, as these can significantly reduce plasma mebendazole levels and undermine efficacy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02876146](https://clinicaltrials.gov/study/NCT02876146) | Observational | Completed | 50 | EchinoVISTA: Prospective study of hepatic AE patients treated with benzimidazoles (primarily albendazole); evaluated parasite viability biomarkers and imaging follow-up markers to optimize treatment withdrawal timing; provides a clinical monitoring framework directly applicable to mebendazole-treated AE patients |

---

## Literature Evidence

### Alveolar Echinococcosis — 20 Publications Available (Top 10 Shown)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [10980173](https://pubmed.ncbi.nlm.nih.gov/10980173/) | 2000 | Comparative Clinical Study | J Antimicrob Chemother | Open-label study of 35 AE patients followed for avg 39 months; mebendazole vs albendazole compared; treatment success (disease non-progression) demonstrated for both; foundational comparative efficacy data |
| [7197224](https://pubmed.ncbi.nlm.nih.gov/7197224/) | 1981 | PK / Clinical Study | Eur J Clin Pharmacol | Plasma mebendazole concentration targets established: >0.25 µmol/L required for anti-echinococcal activity; underpins the TDM requirement for echinococcosis treatment |
| [9875648](https://pubmed.ncbi.nlm.nih.gov/9875648/) | 1998 | Long-term Clinical Case | J Hepatology | 13-year continuous mebendazole therapy (~45–48 mg/kg/day) in non-resectable AE patient; long-term therapy may achieve parasitocidal effect; demonstrates extended tolerability |
| [16044412](https://pubmed.ncbi.nlm.nih.gov/16044412/) | 2005 | Clinical Cohort | Brit J Surgery | 25-year prospective data comparing three AE treatment strategies: benzimidazole alone, curative resection + 2-year adjuvant, and partial debulking + continuous benzimidazole |
| [8789923](https://pubmed.ncbi.nlm.nih.gov/8789923/) | 1996 | WHO Guidelines | Bull World Health Org | WHO Working Group guidelines: mebendazole and albendazole are recommended chemotherapy for CE and AE; perioperative and standalone use protocols defined |
| [27686694](https://pubmed.ncbi.nlm.nih.gov/27686694/) | 2016 | Expert Review | Expert Rev Anti-Infect Ther | Current interventional strategy for hepatic AE; integrates surgical, percutaneous, and perendoscopic approaches with benzimidazole chemotherapy; hepatic resection preferred when feasible |
| [39311470](https://pubmed.ncbi.nlm.nih.gov/39311470/) | 2024 | Review | Parasite (Paris) | Benzimidazoles (albendazole or mebendazole) remain the only recommended chemotherapy for AE; parasitostatic effect means treatment is typically lifelong; hepatotoxicity and drug interactions are key ongoing management concerns |
| [39606163](https://pubmed.ncbi.nlm.nih.gov/39606163/) | 2024 | Review | World J Hepatol | AE drug therapy update; long incubation period leads to late diagnosis with complications; mebendazole and albendazole as primary pharmacotherapy; surgery + chemotherapy combination critical |
| [19254162](https://pubmed.ncbi.nlm.nih.gov/19254162/) | 2009 | Consensus Review | Expert Rev Anti-Infect Ther | Expert consensus confirming mebendazole and albendazole as standard-of-care benzimidazoles for both CE and AE |
| [40093668](https://pubmed.ncbi.nlm.nih.gov/40093668/) | 2025 | Review | World J Gastroenterol | Most recent comprehensive management review of liver echinococcosis; surgical removal is cornerstone; AE resembles carcinoma and is fatal without treatment; benzimidazoles essential as adjuvant |

### Echinococcus granulosus Infectious Disease — Key Supporting Publications

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [2585032](https://pubmed.ncbi.nlm.nih.gov/2585032/) | 1989 | Clinical Observational Series | J Chemotherapy | 70 patients, 150 hydatid cysts treated with mebendazole per WHO protocol; 6 months–5 years follow-up; morphological or volumetric response observed in 64.3% of cysts; direct clinical efficacy evidence |
| [24686032](https://pubmed.ncbi.nlm.nih.gov/24686032/) | 2014 | In Vitro Study | Int J Surgery | Selenium nanoparticles as scolicidal agents evaluated against CE; mebendazole and albendazole cited as established perioperative chemotherapy standard |
| [39178325](https://pubmed.ncbi.nlm.nih.gov/39178325/) | 2024 | Experimental | PLoS Pathogens | Monoclonal antibody immunotherapy evaluated for echinococcosis; benzimidazoles acknowledged as current chemotherapy backbone with limited efficacy; novel combination approaches under development |

---

## India Market Information

Mebendazole is **not registered or marketed in India**. There are **0 approved product licenses** in the Indian regulatory database. No authorized product information is available through Indian regulatory channels.

For patient access in India, physicians would need to evaluate importation authorization under applicable Indian regulations or seek institutional compassionate use pathways, referencing international approvals such as the WHO Essential Medicines List, US FDA, or EMA authorizations as supporting documentation.

---

## Safety Considerations

**Drug Interactions** (10 interactions identified, source: DDInter):

| Interacting Drug | Level | Clinical Note |
|-----------------|-------|---------------|
| Phenobarbital | Moderate | CYP inducer — substantially reduces mebendazole plasma levels; critical risk for echinococcosis treatment where TDM is required |
| Carbamazepine | Moderate | CYP inducer — same mechanism as phenobarbital; co-prescription warrants dose review |
| Phenytoin | Moderate | CYP inducer — reduces mebendazole levels; especially relevant in epilepsy patients with concurrent parasitic disease |
| Fosphenytoin | Moderate | Phenytoin prodrug — same CYP induction concern |
| Primidone | Moderate | Metabolized to phenobarbital — same CYP induction risk |
| Metronidazole | Moderate | Pharmacokinetic interaction; monitor when co-administering |
| Ritonavir | Moderate | CYP inhibitor — may increase mebendazole plasma levels; monitor for concentration-related toxicity |
| Iodide I-131 | Moderate | Monitor when co-administering with radioiodine therapy |
| Iodide I-123 | Moderate | Monitor when co-administering with radioiodine imaging procedures |
| Cimetidine | Minor | Minor pharmacokinetic interaction; generally manageable without dose adjustment |

> **Clinical Priority for Echinococcosis Treatment**: The interaction between mebendazole and antiepileptic CYP inducers (phenobarbital, carbamazepine, phenytoin, primidone) is the most clinically significant safety concern. These drugs can substantially reduce mebendazole plasma concentrations below the therapeutic threshold required for anti-echinococcal activity. Therapeutic drug monitoring (target plasma level ≥0.25 µmol/L) is strongly recommended when any of these agents are co-prescribed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Mebendazole's use for echinococcosis (CE and AE) is supported by WHO guidelines, multiple clinical observational studies, and extensive review literature (L3 evidence), representing a pharmacologically well-grounded extension of its established anti-tubulin mechanism into cestode larval disease — not a speculative repurposing hypothesis. The main barriers to use in India are the complete absence of local marketing authorization and the pharmacokinetic challenge of achieving and maintaining adequate plasma concentrations, particularly in patients on interacting medications.

**To proceed, the following is needed:**
- **Regulatory pathway assessment**: Evaluate options for Indian registration, licensed importation authorization, or institutional compassionate use protocol for echinococcosis patients who have no other treatment options
- **Pharmacokinetic monitoring protocol**: Establish mebendazole plasma concentration targets (≥0.25 µmol/L) and a TDM procedure feasible within Indian clinical settings; consider whether albendazole (higher bioavailability) is more practical as first-line
- **Drug interaction management plan**: Screen all patients for concurrent CYP-inducing antiepileptics; establish dose adjustment criteria or alternative benzimidazole selection if significant interaction is identified
- **Hepatotoxicity monitoring schedule**: Define liver function monitoring intervals (ALT, AST, bilirubin) for patients requiring long-term benzimidazole therapy
- **Safety gap remediation (DG001)**: Obtain and review full package insert including contraindications and warnings from a reference regulatory authority (e.g., US FDA, EMA)
- **MOA documentation (DG002)**: Retrieve complete mechanism of action data via DrugBank API to formalize the mechanistic analysis in this report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

