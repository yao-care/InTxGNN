---
layout: default
title: Raltegravir
parent: 僅模型預測 (L5)
nav_order: 714
evidence_level: L5
indication_count: 3
---

# Raltegravir
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

# Raltegravir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Raltegravir is an HIV-1 integrase strand transfer inhibitor (INSTI) with an established antiretroviral profile, but it is not currently marketed in Taiwan and detailed original-indication/MOA data are missing from this evidence pack.
> The TxGNN model's top prediction — **Simian Immunodeficiency Virus (SIV) Infection** — is not a human clinical indication; it is an animal-model disease used in HIV translational research, and the single linked clinical trial is a mismatched pairing artifact.
> Evidence level is **L4** (mechanistic/preclinical only), supported by **1 loosely related clinical trial** and **~20 preclinical/animal publications**, none of which establish a human therapeutic use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap); Raltegravir is clinically known as an HIV-1 integrase inhibitor |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L4 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (DG002, High severity). Based on known pharmacology, Raltegravir is an HIV-1 integrase strand transfer inhibitor (INSTI), and its efficacy in HIV-1 infection is well established in clinical practice, even though the formal Taiwan-approved indication text is not present in this dataset (drug is currently not marketed in Taiwan, 0 registrations).

The mechanistic rationale for the predicted indication rests on viral homology rather than a distinct human disease target: SIV and HIV are both lentiviruses with highly conserved integrase structures, so INSTIs like raltegravir are pharmacologically active against SIV in vitro and in nonhuman primate models. However, **SIV infection is a disease of nonhuman primates (e.g., rhesus macaques), not a human condition** — it is used almost exclusively as a translational research model to study HIV pathophysiology, viral reservoirs, and antiretroviral pharmacodynamics, not as a target for new human drug indications.

The single clinical trial linked to this prediction (NCT00863668) was itself a human HIV decay-kinetics study, was withdrawn (enrollment = 0), and was flagged by the source evidence pack as a mismatched pairing ("Grade C" relevance — disease label does not match trial content). All supporting literature consists of tier-3 animal/in-vitro studies. Taken together, this prediction should be interpreted as a knowledge-graph artifact driven by semantic/ontological proximity between "HIV" and "SIV," rather than a genuine actionable repurposing signal. (The pack's own two lower-ranked predictions — feline AIDS and a rare pediatric neurodevelopmental disorder — show the same pattern: no credible mechanistic or clinical link, evidence level L5, recommendation Hold.)

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | Withdrawn | 0 | Study of HIV (not SIV) viral decay kinetics under raltegravir-based ART; withdrawn with zero enrollment. Flagged as a disease-label mismatch (Grade C) — not genuine SIV evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20233398](https://pubmed.ncbi.nlm.nih.gov/20233398/) | 2010 | Animal model (SIVmac251 macaque) | Retrovirology | Raltegravir-based ART regimen tested in SIVmac251-infected macaques as a model for lentiviral persistence during therapy |
| [29643246](https://pubmed.ncbi.nlm.nih.gov/29643246/) | 2018 | Animal study (viral dynamics) | Journal of Virology | 2-LTR circle dynamics in raltegravir-treated SIV-infected macaques with/without CD8+ cells |
| [31597776](https://pubmed.ncbi.nlm.nih.gov/31597776/) | 2019 | Animal study (viral genomics) | Journal of Virology | Intactness of persistent SIV genomes in macaques after early ART initiation |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | Animal/cell study (metabolic toxicity) | Clin Infect Dis | Raltegravir and dolutegravir show proadipogenic/profibrotic effects and insulin resistance in adipose tissue |
| [29466356](https://pubmed.ncbi.nlm.nih.gov/29466356/) | 2018 | Animal study (resistance) | PLoS One | Resistance mutations emerge in SIV-infected macaques on non-suppressive raltegravir-containing ART |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | Animal/resistance profiling | Journal of Virology | Drug resistance profiles of integrase inhibitors characterized in SIVmac239 |
| [24622515](https://pubmed.ncbi.nlm.nih.gov/24622515/) | 2014 | Animal study (prevention) | Science Translational Medicine | Topical integrase inhibitors for post-exposure protection against vaginal SHIV infection in macaques |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal/neuroimmune study | mBio | Lentiviral persistence in brain despite effective ART in animal/human tissue models |
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | In vitro/animal antiviral activity | Antimicrob Agents Chemother | Bictegravir/cabotegravir activity against integrase-inhibitor-resistant SIVmac239 and HIV-1 (raltegravir comparator) |
| [23365453](https://pubmed.ncbi.nlm.nih.gov/23365453/) | 2013 | In vitro susceptibility | Journal of Virology | Susceptibility of simian retrovirus type 4 to antiretrovirals including raltegravir |

---

## Taiwan Market Information

Raltegravir is currently **not marketed in Taiwan** (0 registered licenses). No product registration, dosage form, or approved-indication text is available in this evidence pack.

---

## Safety Considerations

**Drug Interactions** (from DDI database, 36 total interactions identified; key clinically relevant ones below):

| Interacting Drug | Severity |
|---|---|
| Aluminum hydroxide | Major |
| Calcium carbonate | Major |
| Zinc sulfate | Major |
| Zinc acetate | Major |
| Magnesium oxide | Moderate |
| Magnesium sulfate | Moderate |
| Magnesium chloride | Moderate |
| Orlistat | Moderate |
| Omeprazole, Esomeprazole, Pantoprazole, Lansoprazole, Dexlansoprazole, Rabeprazole (PPIs) | Minor |
| Famotidine, Ranitidine, Cimetidine, Nizatidine (H2 blockers) | Minor |
| Pioglitazone, Dexamethasone | Minor |

The Major-severity pattern (polyvalent cation antacids/minerals — Al, Ca, Zn, Mg) is consistent with raltegravir's known chelation-mediated absorption reduction and should be treated as clinically significant even though formal Taiwan label warnings and contraindications are not available in this dataset (data gap DG001, Blocking severity).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (SIV infection) targets a nonhuman-primate disease with no human clinical relevance; its only linked clinical trial is a confirmed disease-label mismatch, and all literature is preclinical/animal-model research (Evidence Level L4). The two next-ranked predictions (feline AIDS, a rare pediatric neurodevelopmental disorder) are even weaker (L5, no trials, no literature) and represent likely knowledge-graph artifacts rather than actionable signals.

**To proceed, the following is needed:**
- TFDA label warnings/contraindications (DG001, Blocking) before any safety evaluation (S1) can begin
- Confirmed mechanism of action from DrugBank (DG002)
- Re-run TxGNN disease-candidate review with non-human/veterinary and ultra-rare monogenic disease categories filtered out, to surface genuinely actionable human indications further down the ranked list
- If a human-relevant indication is identified in later ranks, re-evaluate market entry strategy given raltegravir's current non-marketed status in Taiwan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

