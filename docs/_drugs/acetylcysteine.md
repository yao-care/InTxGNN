---
layout: default
title: Acetylcysteine
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 10
---

# Acetylcysteine
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

# Acetylcysteine: From Mucolytic Agent to Thrombotic Disease

## One-Sentence Summary

Acetylcysteine (NAC) is a well-established thiol compound, clinically recognized as a mucolytic agent for respiratory conditions and an antidote for acetaminophen overdose.
The TxGNN model predicts it may be effective for **Thrombotic Disease** — particularly thrombotic microangiopathy (TMA) subtypes such as TTP and TA-TMA —
with **9 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mucolytic agent (respiratory conditions); antidote for acetaminophen overdose |
| Predicted New Indication | Thrombotic Disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory dossier. Based on known pharmacology, Acetylcysteine (NAC) is a thiol-containing small molecule that functions as a direct precursor to glutathione — the body's primary endogenous antioxidant — and as a mucolytic agent via cleavage of disulfide bonds within mucus glycoprotein chains.

For thrombotic disease, a mechanistically specific and compelling rationale exists: NAC directly cleaves disulfide bonds within ultra-large von Willebrand factor (ULVWF) multimers. ULVWF accumulation is the central pathological driver in thrombotic microangiopathies (TMA), including thrombotic thrombocytopenic purpura (TTP) and transplantation-associated TMA (TA-TMA). By reducing VWF multimer size and activity, NAC prevents platelet-VWF string formation and subsequent microvascular thrombosis — a mechanism validated in both mouse and baboon preclinical models (Chen et al., 2011, *J Clin Invest*), and further supported by in vitro studies in human plasma.

Beyond VWF modulation, NAC's antioxidant properties provide endothelial cytoprotection by scavenging reactive oxygen species (ROS), reducing the oxidative pro-thrombotic microenvironment that characterizes TMA conditions. This dual mechanism — direct VWF disulfide bond cleavage combined with endothelial protection — is mechanistically distinct from most conventional antithrombotic therapies, making NAC a scientifically rational repurposing candidate that complements, rather than duplicates, existing treatment approaches.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Phase 3 | Completed | 170 | Prospective Phase 3 trial evaluating NAC safety and efficacy in HSCT-associated thrombotic microangiopathy (TA-TMA); the highest-quality direct clinical evidence available for this indication |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Phase 2 | Completed | 40 | RENACTIF: randomized, double-blind, placebo-controlled crossover trial assessing NAC's reduction of thrombotic phenotype in patients with chronic kidney disease and uremic toxin (indoxyl sulfate) accumulation; directly supports broader thrombotic disease indication |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Phase 2/3 | Active, Not Recruiting | 44 | Multicenter prospective single-arm trial evaluating NAC efficacy and safety for TA-TMA; ongoing validation reinforcing the TA-TMA evidence base |
| [NCT05907486](https://clinicaltrials.gov/study/NCT05907486) | Phase 3 | Unknown | 260 | Large Phase 3 trial assessing NAC for prevention of thrombotic events after allogeneic HSCT; scope and scale directly relevant — status requires follow-up confirmation |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Phase 1/2 | Unknown | 200 | Multicentre study combining atorvastatin, acetylcysteine, and danazol in steroid-resistant/relapsed immune thrombocytopenia; NAC's independent contribution cannot be isolated from this combination design |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Phase 2 | Unknown | 44 | NAC plus high-dose dexamethasone in newly diagnosed primary immune thrombocytopenia; provides indirect evidence of NAC's role in platelet-related thrombotic disorders |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Early Phase 1 | Completed | 15 | Exploratory assessment of atorvastatin and NAC to elevate platelet count in steroid-resistant ITP; early-phase signal only due to very small sample size |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Early Phase 1 | Completed | 3 | Pilot study of IV NAC in suspected TTP patients receiving therapeutic plasma exchange; extremely limited statistical power but represents the earliest clinical probe in TTP |
| [NCT06518044](https://clinicaltrials.gov/study/NCT06518044) | Phase 2 | Not Yet Recruiting | 30 | NAC to promote hematopoietic recovery in severe aplastic anemia post-haploidentical transplantation; limited direct relevance to thrombotic disease mechanism |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Retrospective Cohort | Annals of Hematology | Real-world cohort study evaluating association between NAC treatment and in-hospital mortality in acquired TTP; provides clinical evidence for NAC's role in aTTP management |
| [35940529](https://pubmed.ncbi.nlm.nih.gov/35940529/) | 2022 | RCT | Transplantation and Cellular Therapy | Randomized placebo-controlled trial of NAC as prophylactic therapy for TA-TMA in HSCT patients; supports preventive use in transplant-related thrombotic disease |
| [21266777](https://pubmed.ncbi.nlm.nih.gov/21266777/) | 2011 | Preclinical | The Journal of Clinical Investigation | Landmark mechanistic study demonstrating NAC reduces size and activity of VWF multimers in human plasma and mouse models; foundational evidence for the thrombotic disease rationale |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Review | Expert Review of Hematology | Comprehensive review of repurposed drugs and novel agents in TTP, specifically covering NAC among emerging therapeutic options alongside rituximab and caplacizumab |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Preclinical | Blood | NAC in preclinical mouse and baboon TTP models; validates in vivo efficacy and reinforces the VWF-disulfide cleavage mechanism |
| [39737637](https://pubmed.ncbi.nlm.nih.gov/39737637/) | 2025 | Case Report | J Pediatric Hematology/Oncology | Congenital TTP with acute renal failure treated with plasma exchange and NAC combination; demonstrates clinical application in rare genetic TTP variant |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Review | Journal of Clinical Medicine | Comprehensive TTP review covering pathophysiology, diagnosis, and management; contextualizes NAC within current treatment strategies |
| [28382967](https://pubmed.ncbi.nlm.nih.gov/28382967/) | 2017 | Review | Nature Reviews Disease Primers | Authoritative overview of TTP (Moschcowitz disease) in Nature Reviews, establishing disease context and unmet therapeutic needs where NAC may contribute |
| [28645643](https://pubmed.ncbi.nlm.nih.gov/28645643/) | 2017 | Review | Transfusion Clinique et Biologique | Management overview of acquired TTP including current standard of care (TPE, rituximab) and emerging agents; positions NAC within the evolving treatment algorithm |
| [36410267](https://pubmed.ncbi.nlm.nih.gov/36410267/) | 2022 | Review | Journal of Infection and Public Health | Reviews NAC in COVID-19 management, including its relevance to SARS-CoV-2-associated prothrombotic states; extends the thrombotic disease rationale to infection-triggered TMA |

---

## India Market Information

Acetylcysteine is currently **not registered** in India under the regulatory data available for this evaluation. No product authorizations were identified at the time of this report.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No registered products found |

> Independent verification of current CDSCO registration status is recommended, as data availability may be incomplete.

---

## Safety Considerations

**Drug Interactions (247 total interactions identified; source: DDInter):**

| Interacting Drug | Severity Level |
|-----------------|---------------|
| Insulin human (inhalation, rapid acting) | **Moderate** |
| Activated charcoal | Minor |
| Mannitol | Unknown |
| Bupropion | Unknown |
| Omeprazole | Unknown |
| Pantoprazole | Unknown |
| Lansoprazole | Unknown |
| Vancomycin | Unknown |
| Morphine | Unknown |
| Metformin | Unknown |

The most clinically relevant confirmed interaction is with **inhaled insulin** (Moderate severity) and **activated charcoal** (Minor — oral activated charcoal may reduce NAC bioavailability when co-administered orally). The majority of the 247 catalogued interactions are currently classified as "Unknown" severity and require clinical judgment on a case-by-case basis.

> Complete warnings and contraindications are not available in this data package. Please refer to the approved package insert for full safety information before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
At least one completed Phase 3 trial (NCT03252925, n=170) and one completed Phase 2 RCT (NCT03636932, n=40) directly support NAC in thrombotic disease subtypes, with a mechanistic basis — VWF disulfide bond cleavage — that is both specific and experimentally validated at multiple levels from in vitro to clinical. The 99.96% TxGNN prediction score, combined with L1 evidence grade, provides sufficient confidence to advance under structured monitoring conditions.

**To proceed, the following is needed:**
- Obtain the complete NAC package insert from CDSCO or reference regulatory agencies to fill the data gap on formal warnings and contraindications
- Narrow the therapeutic scope to evidence-supported subtypes: current data is strongest for **TMA-spectrum disorders (TTP, TA-TMA, CKD-related thrombotic phenotype)** rather than all thrombotic diseases broadly
- Follow up on the status of NCT05907486 (Phase 3, n=260; status listed as Unknown) to determine whether that large-scale dataset is accessible
- Evaluate import/registration pathway for NAC in India given its complete absence from the current market, and assess whether IV-grade NAC formulations can be reliably sourced
- Define a monitoring protocol covering coagulation parameters, renal function, and VWF levels for any prospective clinical application in Indian patient populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

