---
layout: default
title: Atorvastatin
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 6
---

# Atorvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Atorvastatin: From Hyperlipidemia to Familial Hypercholesterolemia

## One-Sentence Summary

Atorvastatin is a potent HMG-CoA reductase inhibitor (statin) globally established for the treatment of primary hypercholesterolemia and cardiovascular risk reduction, though it currently holds no approved registration in the India market according to available regulatory data.
The TxGNN model predicts it may be highly effective for **Familial Hypercholesterolemia (FH)**, with **35 clinical trials** and **19 publications** currently supporting this direction — yielding the highest achievable evidence level (L1) among all predicted indications.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperlipidemia / primary hypercholesterolemia and cardiovascular risk reduction (global approvals; no India registration on record) |
| Predicted New Indication | Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L1 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the India regulatory dossier. Based on published literature, atorvastatin belongs to the statin class and works by competitively inhibiting HMG-CoA reductase — the rate-limiting enzyme in hepatic cholesterol biosynthesis. This inhibition reduces intracellular cholesterol, which triggers upregulation of LDL receptors on hepatocytes, increasing the clearance of circulating LDL-cholesterol from plasma. Atorvastatin's prolonged half-life of 20–30 hours, combined with active metabolites, sustains enzyme inhibition throughout the day and additionally suppresses hepatic apolipoprotein B production.

Familial hypercholesterolemia (FH) arises primarily from loss-of-function mutations in the LDL receptor gene, causing severely elevated LDL-cholesterol from birth. Because atorvastatin directly compensates for deficient LDL-receptor activity by reducing the upstream synthesis of LDL, it is mechanistically well-matched to FH pathophysiology. For heterozygous FH (HeFH), patients retain some residual LDL-receptor function, and statin therapy typically achieves meaningful LDL-C reductions. For homozygous FH (HoFH), near-complete loss of LDL-receptor activity means statin monotherapy is often insufficient, requiring combination with PCSK9 inhibitors or LDL apheresis.

The TxGNN confidence score of 99.42% is strongly borne out by the clinical evidence: multiple completed Phase 3 RCTs confirm atorvastatin's efficacy across both HeFH and HoFH populations, and international guidelines (AACE/ACE, ESC/EAS) recognize statins as the first-line pharmacotherapy for all FH subtypes. The primary guardrail is ensuring appropriate combination strategies for HoFH and maintaining vigilance for statin-associated muscle symptoms — particularly given significant drug-drug interaction risks with CYP3A4 inhibitors such as clarithromycin.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | Completed | 486 | Randomized, double-blind, placebo-controlled: alirocumab (PCSK9 inhibitor) added to background statin therapy (including atorvastatin) in HeFH patients inadequately controlled on lipid-modifying therapy; demonstrated significant LDL-C reduction at 24 weeks vs. placebo |
| [NCT00136981](https://clinicaltrials.gov/study/NCT00136981) | Phase 3 | Completed | 800 | Carotid B-mode ultrasound evaluation of torcetrapib/atorvastatin vs. maximally tolerated atorvastatin alone in HeFH over 24 months; used carotid intima-media thickness (IMT) as surrogate endpoint for atherosclerosis progression |
| [NCT01954394](https://clinicaltrials.gov/study/NCT01954394) | Phase 3 | Completed | 986 | Long-term open-label extension study assessing safety and efficacy of alirocumab added to lipid-lowering therapy (including atorvastatin) in HeFH patients who had completed earlier Phase 3 trials; evaluated multi-year durability and immunogenicity |
| [NCT03867318](https://clinicaltrials.gov/study/NCT03867318) | Phase 3 | Completed | 621 | Ezetimibe 10 mg co-administered with atorvastatin 10 mg in HeFH and coronary heart disease patients not controlled by atorvastatin monotherapy; demonstrated additive LDL-C reduction beyond statin alone |
| [NCT03882996](https://clinicaltrials.gov/study/NCT03882996) | Phase 3 | Completed | 432 | Long-term (12-month) safety and tolerability of ezetimibe co-administered with atorvastatin 10–80 mg daily in HeFH and CHD patients; confirmed a durable safety profile across the full dose titration range |
| [NCT01730040](https://clinicaltrials.gov/study/NCT01730040) | Phase 3 | Completed | 355 | Four-arm head-to-head comparison in high-risk patients: alirocumab + atorvastatin vs. ezetimibe + atorvastatin vs. atorvastatin dose escalation vs. switch to rosuvastatin in patients uncontrolled on atorvastatin, including HeFH subgroup |
| [NCT00827606](https://clinicaltrials.gov/study/NCT00827606) | Phase 3 | Completed | 272 | Three-year open-label study of atorvastatin in children and adolescents with HeFH; characterized growth and development parameters (height, weight, BMI, Tanner Stage) alongside long-term cholesterol-lowering efficacy |
| [NCT02584504](https://clinicaltrials.gov/study/NCT02584504) | Phase 3 | Completed | 163 | Alirocumab as add-on to non-statin or lowest-strength statin therapy in hypercholesterolemia; demonstrated LDL-C reduction at 12 weeks including in populations unable to tolerate full-dose statins |
| [NCT00134511](https://clinicaltrials.gov/study/NCT00134511) | Phase 3 | Completed | 30 | Forced-titration evaluation of torcetrapib/atorvastatin in homozygous FH patients; directly evaluated LDL-C efficacy and safety in HoFH (Torcetrapib project subsequently terminated due to safety findings unrelated to atorvastatin) |
| [NCT00739999](https://clinicaltrials.gov/study/NCT00739999) | Phase 1 | Completed | 39 | Pharmacokinetics, pharmacodynamics, safety and tolerability of atorvastatin in children and adolescents with HeFH; established the PK basis for pediatric dosing recommendations in FH |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Current Atherosclerosis Reports | Comprehensive review of novel pharmacological therapies for LDL-C lowering in homozygous FH; situates statins as the foundational therapy upon which newer agents are added |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Clinical Guideline | Endocrine Practice | AACE/ACE guidelines for dyslipidemia management and cardiovascular prevention; establishes evidence-based statin dosing targets and treatment algorithms including FH-specific recommendations |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | Cohort Study | JACC | Quantified statin-induced reduction in coronary artery disease events and all-cause mortality in HeFH patients; provides robust real-world evidence for long-term cardiovascular benefit of statin therapy in FH |
| [9793596](https://pubmed.ncbi.nlm.nih.gov/9793596/) | 1998 | Clinical Review | Annals of Pharmacotherapy | Early systematic review of atorvastatin efficacy and safety in primary hypercholesterolemia and mixed dyslipidemias; foundational evidence establishing atorvastatin's clinical role |
| [27678432](https://pubmed.ncbi.nlm.nih.gov/27678432/) | 2016 | Clinical Trial | Journal of Clinical Lipidology | Three-year atorvastatin study in children/adolescents aged 6–17 years with HeFH; demonstrated sustained LDL-C reduction and a favorable safety profile including normal growth and development across extended follow-up |
| [22957727](https://pubmed.ncbi.nlm.nih.gov/22957727/) | 2013 | Clinical Trial | Echocardiography | Atorvastatin improved myocardial and peripheral blood flow reserve in FH patients without overt coronary atherosclerosis; demonstrated pleiotropic microcirculatory benefits beyond LDL-C reduction |
| [35361995](https://pubmed.ncbi.nlm.nih.gov/35361995/) | 2022 | Genetic Study | The Pharmacogenomics Journal | NGS strategy combining FH gene panel with statin pharmacogenomic markers; supports individualized atorvastatin prescribing based on genotype-guided risk stratification in FH |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Clinical Trial | Nutrition Metabolism & Cardiovascular Diseases | Direct comparison of atorvastatin vs. simvastatin in HeFH; assessed NCEP LDL-C goal attainment rates and effects on fibrinogen and coagulative variables |
| [10582478](https://pubmed.ncbi.nlm.nih.gov/10582478/) | 1999 | Drug Review | Revue Médicale de Bruxelles | Describes atorvastatin's mechanism (HMG-CoA reductase inhibition → upregulation of LDL receptors), prolonged half-life of active metabolites, and dose-dependent biological efficacy across the statin class |
| [26988948](https://pubmed.ncbi.nlm.nih.gov/26988948/) | 2016 | Clinical Quality Improvement | JACC | Highlights systematic deficiencies in FH monitoring and care delivery; underscores importance of optimizing statin therapy, including appropriate use of atorvastatin, to reduce cardiovascular risk in FH populations |

---

## India Market Information

Atorvastatin currently has **no registered products** in the India market and is classified as **Not Marketed** (total licenses: 0). No individual license records are available for tabulation.

> Atorvastatin (brand name Lipitor®, Pfizer) is approved in major international markets — including the US (FDA), European Union (EMA), and Japan (PMDA) — for hyperlipidemia, mixed dyslipidemia, and cardiovascular risk reduction, with pediatric FH indications also established. A dedicated India regulatory submission to CDSCO would be required to obtain local approval.

---

## Safety Considerations

**Drug Interactions** (301 total interactions identified; key interactions listed below):

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|--------------|
| Clarithromycin | **Major** | Strong CYP3A4 inhibitor; markedly increases atorvastatin plasma exposure — substantially raises risk of myopathy and rhabdomyolysis; avoid concurrent use or use the lowest effective atorvastatin dose with close monitoring |
| Aprepitant | Moderate | Moderate CYP3A4 inhibition; may increase atorvastatin levels; monitor for myopathy symptoms |
| Clotrimazole / Miconazole | Moderate | Azole antifungals inhibit CYP3A4; monitor closely for adverse effects |
| Omeprazole / Esomeprazole / Lansoprazole / Pantoprazole | Moderate | PPI class interaction; monitor lipid response and for adverse effects |
| Cimetidine | Moderate | May interfere with atorvastatin metabolism; monitor LDL-C response |
| Dexamethasone | Moderate | CYP3A4 induction may reduce atorvastatin plasma levels and efficacy |
| Rosuvastatin / Simvastatin | Moderate | Combining two statins increases myopathy risk; concurrent use generally not recommended |
| Metronidazole / Naltrexone / Eluxadoline / Eliglustat / Pectin | Moderate | Various pharmacokinetic or pharmacodynamic interactions; monitor for efficacy and tolerability |
| Aluminum hydroxide / Magnesium hydroxide / Liraglutide | Minor | Antacids may reduce atorvastatin absorption (administer separately); liraglutide interaction is minor |

For complete safety information, including contraindications and full prescribing warnings, please refer to the originator package insert.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs with up to 986 participants establish a Level 1 evidence base for atorvastatin in familial hypercholesterolemia, and international guidelines uniformly endorse statins as first-line therapy. The absence of India market registration represents a regulatory gap — not a safety or efficacy gap — and the biological mechanism is directly aligned with FH pathophysiology.

**To proceed, the following is needed:**
- Prepare and submit a regulatory dossier to CDSCO for India market approval, referencing existing Phase 3 clinical data and international approvals (US FDA, EMA)
- Obtain the complete atorvastatin package insert (CDSCO or reference product) to document India-specific warnings, contraindications, and dosing recommendations
- Develop a risk management plan addressing CYP3A4 drug interaction monitoring (major concern: clarithromycin) and systematic myopathy surveillance (baseline and periodic CK and hepatic function monitoring)
- Differentiate clinical strategy by FH subtype: HeFH (atorvastatin monotherapy or combination with ezetimibe/PCSK9 inhibitor based on LDL-C response); HoFH (mandatory combination therapy — PCSK9 inhibitors or LDL apheresis required alongside statin)
- Evaluate pediatric FH indication separately, given Phase 1 PK data and three-year Phase 3 safety data supporting use from age 6 years
- Conduct a pharmacoeconomic analysis to assess cost-effectiveness relative to other statins already marketed in India
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

