---
layout: default
title: Sofosbuvir
parent: Moderate Evidence (L3-L4)
nav_order: 775
evidence_level: L3
indication_count: 8
---

# Sofosbuvir
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **8** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Sofosbuvir: From Hepatitis C Virus Infection to Hepatitis B Virus Infection

## One-Sentence Summary

> Sofosbuvir is a nucleotide analogue NS5B (RdRp) inhibitor originally developed for chronic Hepatitis C virus (HCV) infection.
> The TxGNN model predicts it may also be effective for **Hepatitis B Virus (HBV) Infection**,
> with **17+ clinical trials** and **18 publications** currently associated with this direction — though most of this evidence actually concerns HCV treatment in HCV/HBV coinfected patients rather than direct anti-HBV activity, and includes safety signals of HBV reactivation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Hepatitis C Virus (HCV) infection (inferred from mechanism-of-action statements in the evidence pack; India-approved label text unavailable since the product is not marketed) |
| Predicted New Indication | Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available from a formal DrugBank query (flagged as a High-severity data gap, DG002). Based on information embedded in the evidence pack's repurposing rationale, however, sofosbuvir is a nucleotide analogue that is metabolized intracellularly to its active triphosphate form and inhibits the HCV NS5B RNA-dependent RNA polymerase (RdRp) — the mechanism underlying its established use in chronic hepatitis C.

HBV, by contrast, is a partially double-stranded DNA virus that replicates via reverse transcriptase, not an NS5B-type RdRp. Mechanistically, sofosbuvir was not designed against this target, and the TxGNN prediction rationale itself explicitly notes this discordance. The large majority of clinical trials and literature returned for this candidate are actually **HCV treatment studies conducted in patients coinfected with HBV** (i.e., sofosbuvir clearing HCV while HBV status is monitored as a safety covariate), rather than trials demonstrating anti-HBV efficacy. A small number of exploratory studies (e.g., a Phase II open-label pilot of ledipasvir/sofosbuvir in HBV-monoinfected subjects) directly test the hypothesis, but these are early-stage, small-sample, and not confirmatory. Notably, several publications describe **HBV reactivation** as an adverse consequence of sofosbuvir-based DAA therapy in HCV/HBV coinfected patients — a safety signal that runs counter to, rather than supports, the repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03312023](https://clinicaltrials.gov/study/NCT03312023) | Phase 2 | Completed | 21 | Open-label study of ledipasvir/sofosbuvir for 12 weeks specifically in subjects with HBV infection (not HCV), evaluating decline in HBsAg and HBV DNA — the most direct test of this hypothesis. |
| [NCT03261349](https://clinicaltrials.gov/study/NCT03261349) | Phase 2 | Unknown | 21 | Pilot study of ledipasvir/sofosbuvir in HCV-associated indolent B-cell lymphoma; graded "A" relevance as it directly tests LDV/SOF in HBV-affected patients, but is a small, single-arm, status-unknown trial. |
| [NCT02613871](https://clinicaltrials.gov/study/NCT02613871) | Phase 3 | Completed | 111 | LDV/SOF fixed-dose combination in HCV genotype 1/2 patients coinfected with HBV in Taiwan; primary endpoint is HCV clearance, with HBV monitored as safety covariate. |
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Prospective study of DAA therapy in chronic HCV/HBV coinfection, focused on incidence and predictors of **HBV reactivation** during anti-HCV treatment. |
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | Unknown | 120 | SOF/VEL regimen combined with prophylactic TAF specifically to prevent HBV reactivation in HCV/HBV coinfected patients — supports a safety-management use case, not a therapeutic HBV indication. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36045503](https://pubmed.ncbi.nlm.nih.gov/36045503/) | 2023 | Phase 2 open-label pilot | Journal of Medical Virology | LDV/SOF administered to HBV-monoinfected subjects; hypothesis based on modest HBsAg reduction previously observed in HBV/HCV coinfected patients. Primary/secondary endpoints: decline in HBsAg and HBV DNA at Week 12. |
| [34864948](https://pubmed.ncbi.nlm.nih.gov/34864948/) | 2022 | Cohort (Taiwan) | Clinical Infectious Diseases | 108-week follow-up of HBV reactivation risk during LDV/SOF treatment of HCV/HBV coinfected patients in Taiwan. |
| [29334502](https://pubmed.ncbi.nlm.nih.gov/29334502/) | 2018 | Cohort | J Clin Gastroenterology | Examines risk of HBV reactivation in actively infected or previously exposed patients during/after LDV/SOF treatment for HCV. |
| [31722032](https://pubmed.ncbi.nlm.nih.gov/31722032/) | 2020 | Cohort | Trans R Soc Trop Med Hyg | Sofosbuvir/daclatasvir-based therapy outcomes in chronic HCV and HCV/HBV coinfected patients in Egypt. |
| [33031326](https://pubmed.ncbi.nlm.nih.gov/33031326/) | 2020 | Case report | Medicine | HBV reactivation after successful HCV treatment with sofosbuvir and ribavirin — safety signal. |
| [31632097](https://pubmed.ncbi.nlm.nih.gov/31632097/) | 2019 | Case series | Infection and Drug Resistance | Management of HBV reactivation post-DAA treatment in HCV/HBV coinfected patients with pretreatment HBeAg seroconversion. |
| [33523503](https://pubmed.ncbi.nlm.nih.gov/33523503/) | 2021 | Prospective observational | J Viral Hepatitis | HBV reactivation in cancer patients receiving DAAs for HCV, in HBV/HCV coinfection. |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Overview of antiviral medications for HBV and HCV and their renal effects; background context, not sofosbuvir-specific HBV data. |
| [25253190](https://pubmed.ncbi.nlm.nih.gov/25253190/) | 2014 | Review | Minerva Pediatrica | Overview of treatment options for hepatitis B and C in children; background context only. |

---

## India Market Information

Sofosbuvir currently has **no registered marketing authorizations in India** in this dataset (`market_status`: Not Marketed; `total_licenses`: 0). No product name, dosage form, or approved indication text is available.

---

## Safety Considerations

**Key Warnings** and **Contraindications** are not available in this evidence pack (data gap, DG001 — TFDA/label warnings, classified as Blocking severity for safety review).

**Drug Interactions** (8 documented interactions):

| Interacting Drug | Severity Level | Source |
|---|---|---|
| Apalutamide | Major | DDInter |
| Enzalutamide | Major | DDInter |
| Lorlatinib | Major | DDInter |
| Fostamatinib | Moderate | DDInter |
| Warfarin | Moderate | DDInter |
| Dicoumarol | Moderate | DDInter |
| Encorafenib | Moderate | DDInter |
| Cyclosporine | Minor | DDInter |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- A Blocking-severity data gap exists (no TFDA/label warnings or contraindications available), which prevents completion of even a preliminary (S1) safety assessment.
- The bulk of clinical trial and literature evidence is confounded — it demonstrates sofosbuvir's efficacy in clearing **HCV** in HBV-coinfected patients, not efficacy against HBV itself; direct evidence (e.g., NCT03312023, PMID 36045503) is limited to small, early-phase, non-confirmatory studies.
- Multiple independent publications report **HBV reactivation** as an adverse consequence of sofosbuvir-based DAA therapy, which is a safety concern directly relevant to (and in tension with) this repurposing hypothesis.
- The product is not currently marketed in India (0 registrations), so there is no existing regulatory or commercial foundation to build on.

**To proceed, the following is needed:**
- Formal DrugBank MOA data and TFDA/local label warnings and contraindications to close the Blocking data gap
- A dedicated, adequately powered trial testing sofosbuvir (or ledipasvir/sofosbuvir) as monotherapy against HBV-specific endpoints (HBsAg loss/seroconversion, HBV DNA suppression), independent of HCV coinfection status
- A structured risk assessment of HBV reactivation associated with sofosbuvir-based regimens before considering any HBV-directed use
- Regulatory pathway assessment for India, given the drug currently has no market presence there
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

