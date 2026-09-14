---
layout: default
title: Telbivudine
parent: 僅模型預測 (L5)
nav_order: 804
evidence_level: L5
indication_count: 10
---

# Telbivudine
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

# Telbivudine: From Chronic Hepatitis B to Chronic Hepatitis C Virus Infection

## One-Sentence Summary

> Telbivudine is a nucleoside analog antiviral internationally approved for chronic hepatitis B (CHB) treatment.
> The TxGNN model's top-ranked prediction suggests possible activity against **chronic hepatitis C virus infection**,
> but a review of the **10 clinical trials** and **10 publications** cited shows none actually test telbivudine in HCV-infected patients — all directly relevant records concern HBV. This prediction should be treated as a likely false positive.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis B (based on established pharmacology; not present in the supplied regulatory dataset) |
| Predicted New Indication | Chronic Hepatitis C Virus Infection |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed official mechanism-of-action data is not available for telbivudine. Based on known pharmacology, telbivudine is an L-nucleoside (thymidine) analog that, after intracellular phosphorylation, specifically inhibits the HBV DNA polymerase (a reverse-transcriptase-dependent enzyme), causing viral DNA chain termination. This is telbivudine's established, approved mechanism in chronic hepatitis B.

HCV, in contrast, is an RNA virus whose replication depends on an RNA-dependent RNA polymerase (NS5B) — a structurally and catalytically distinct target from HBV's DNA polymerase. There is no established biochemical pathway by which telbivudine would inhibit HCV replication.

Reviewing the clinical trials and literature linked to this prediction confirms this concern: every directly relevant trial enrolls chronic **hepatitis B** patients, and the cited publications are largely general reviews that discuss "hepatitis B and C" jointly without providing telbivudine-specific HCV efficacy data. This pattern is consistent with a knowledge-graph co-occurrence artifact (telbivudine frequently appears in literature alongside broad "HBV and HCV" review titles) rather than a genuine pharmacological signal. Given the mechanistic mismatch and complete absence of direct supporting evidence, this predicted indication does not currently warrant further development.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00805675](https://clinicaltrials.gov/study/NCT00805675) | Phase 3 | Completed | 83 | Compared telbivudine + tenofovir vs. monotherapy on HBV DNA kinetics — HBV patients, not HCV |
| [NCT01925820](https://clinicaltrials.gov/study/NCT01925820) | Phase 4 | Unknown | 540 | Pegasys + entecavir vs. entecavir vs. Pegasys in HBeAg-negative CHB; telbivudine mentioned only as a comparator class |
| [NCT00142298](https://clinicaltrials.gov/study/NCT00142298) | Phase 3 | Completed | 1869 | Open-label extension of telbivudine in CHB patients — **Grade C**: study population is Chronic Hepatitis B, not HCV |
| [NCT03181607](https://clinicaltrials.gov/study/NCT03181607) | N/A | Unknown | 300 | Telbivudine/tenofovir to reduce HBV mother-to-child transmission — HBV, not HCV |
| [NCT00412529](https://clinicaltrials.gov/study/NCT00412529) | Phase 3 | Completed | 44 | Viral kinetics of telbivudine vs. entecavir in HBeAg-positive CHB |
| [NCT00810524](https://clinicaltrials.gov/study/NCT00810524) | Phase 4 | Unknown | 600 | Long-term prognosis of antiviral treatment in chronic HBV infection |
| [NCT02956850](https://clinicaltrials.gov/study/NCT02956850) | Phase 1 | Completed | 160 | Safety/PK study of RO7020531 in chronic hepatitis B patients; telbivudine not the study drug |
| [NCT02058108](https://clinicaltrials.gov/study/NCT02058108) | Phase 3 | Terminated | 53 | Pediatric telbivudine study in HBeAg-positive/negative CHB — **Grade C**: HBV, not HCV |
| [NCT01083251](https://clinicaltrials.gov/study/NCT01083251) | N/A | Unknown | 120 | Vitamin D as adjunct to Peg-IFN or telbivudine in chronic HBV — **Grade C**: HBV population |
| [NCT05466071](https://clinicaltrials.gov/study/NCT05466071) | N/A | Unknown | 200 | Tenofovir alafenamide (not telbivudine) to prevent HBV mother-to-child transmission |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19344237](https://pubmed.ncbi.nlm.nih.gov/19344237/) | 2009 | Review | Expert Rev Anti Infect Ther | General perspective on managing chronic hepatitis B and C jointly; no HCV-specific telbivudine data |
| [16937041](https://pubmed.ncbi.nlm.nih.gov/16937041/) | 2006 | Review | Wien Med Wochenschr | Overview of current/future HBV and HCV therapies; telbivudine discussed only in the HBV context |
| [25233195](https://pubmed.ncbi.nlm.nih.gov/25233195/) | 2014 | Review | J Perinatol | HBV/HCV in pregnancy review; telbivudine mentioned as an HBV mother-to-child transmission agent |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | Reviews antiviral medications for HBV and HCV separately and their renal effects; telbivudine listed under HBV agents |
| [28845882](https://pubmed.ncbi.nlm.nih.gov/28845882/) | 2018 | Cohort | J Viral Hepat | US veteran cohort on HBV reactivation during DAA therapy for HCV; does not evaluate telbivudine efficacy in HCV |
| [18330099](https://pubmed.ncbi.nlm.nih.gov/18330099/) | 2007 | Guideline | Acta Gastroenterol Belg | Belgian guidelines for chronic HBV management |
| [18340426](https://pubmed.ncbi.nlm.nih.gov/18340426/) | 2008 | Review | Der Internist | German guidelines on antiviral therapy for HBV and HCV; telbivudine listed as an HBV monotherapy option |
| [23697556](https://pubmed.ncbi.nlm.nih.gov/23697556/) | 2013 | Clinical study | J Interferon Cytokine Res | IL-37 levels and HBeAg seroconversion during telbivudine treatment — HBV patients only |
| [21964179](https://pubmed.ncbi.nlm.nih.gov/21964179/) | 2011 | Review | Mayo Clin Proc | General review of antiviral drugs for herpes, hepatitis, and influenza viruses; no HCV-telbivudine data |
| [21999649](https://pubmed.ncbi.nlm.nih.gov/21999649/) | 2011 | Review | Paediatr Drugs | Pediatric chronic liver disease management overview; telbivudine noted only for HBV |

## India Market Information

Telbivudine is currently **not marketed in India** — 0 registrations are recorded in the available regulatory dataset, so no product/license details can be listed.

## Safety Considerations

**Drug Interactions**: A total of **96 interactions** are recorded (source: DDInter). A sample of 19 moderate-severity interactions includes:
- Corticosteroids: Hydrocortisone, Triamcinolone, Dexamethasone, Betamethasone, Budesonide, Prednisone
- Antifungals: Amphotericin B (and lipid complex / cholesteryl sulfate formulations)
- Aminoglycosides/antibiotics: Kanamycin, Neomycin, Vancomycin, Metronidazole
- 5-ASA agents: Mesalazine, Balsalazide, Olsalazine, Sulfasalazine
- Statins: Rosuvastatin, Simvastatin
- Orlistat

All listed interactions are classified as **Moderate** severity. No mechanism detail is provided in the source data beyond severity level.

Key warnings and contraindication data are not currently available for this drug; please refer to the official package insert once accessible.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted association with chronic hepatitis C virus infection lacks mechanistic plausibility (telbivudine targets HBV DNA polymerase, not HCV's RNA-dependent RNA polymerase) and is not supported by any of the 10 clinical trials or 10 publications cited — all directly relevant evidence concerns HBV, not HCV. The evidence level is L4 (mechanism/preclinical-tier at best, with no genuine target-specific data), and the score appears driven by knowledge-graph co-occurrence rather than pharmacological signal.

**To proceed, the following is needed:**
- Confirmed mechanism of action data from DrugBank (currently a data gap, DG002)
- TFDA/CDSCO label warnings and contraindications (currently a blocking data gap, DG001)
- Direct in vitro or clinical evidence of telbivudine activity against HCV NS5B or HCV replicons, if this indication is to be pursued further

**Additional note:** Within this same evidence pack, the model's second-ranked prediction — **hepatitis B virus infection** — has substantially stronger support (Evidence Level L1, decision stage S3, "Proceed with Guardrails"), reflecting telbivudine's already-established antiviral mechanism and extensive direct clinical trial evidence. This is not a novel repurposing candidate, but it is the mechanistically and clinically credible entry in this prediction set and may be of separate interest for market-status review in India.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

