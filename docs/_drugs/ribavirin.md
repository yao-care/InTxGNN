---
layout: default
title: Ribavirin
parent: 僅模型預測 (L5)
nav_order: 729
evidence_level: L5
indication_count: 10
---

# Ribavirin
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

# Ribavirin: From Chronic Hepatitis C to Chronic Hepatitis B Virus Infection

## One-Sentence Summary

Ribavirin is a nucleoside antiviral agent whose established clinical role is in combination with (peg)interferon for treating chronic hepatitis C (HCV). The TxGNN model predicts it may also be effective for **Chronic Hepatitis B Virus Infection**, with **50 clinical trials** and **20 publications** retrieved — however, essentially all of this evidence actually concerns HCV treatment or HBV/HCV co-infection management rather than direct antiviral activity against HBV itself.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Hepatitis C, in combination with peginterferon (India-specific approved label text not available) |
| Predicted New Indication | Chronic Hepatitis B Virus Infection |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Ribavirin is not available (DrugBank MOA lookup pending). Based on known clinical use, Ribavirin is a nucleoside analogue antiviral that has been used for decades in combination with peginterferon as standard-of-care therapy for chronic hepatitis C, an RNA virus infection. Its established antiviral activity works through mechanisms understood to target RNA virus replication (e.g., IMPDH inhibition, lethal mutagenesis of viral RNA).

Chronic hepatitis B (HBV) and chronic hepatitis C (HCV) share clinical overlap — they are both hepatotropic viruses that frequently co-occur in endemic regions and are managed together in co-infected patients — but they are virologically distinct: HBV is a DNA virus, while HCV is an RNA virus. Ribavirin's antiviral mechanism has no established, direct activity against HBV replication.

Reviewing the retrieved evidence confirms this gap: all 50 clinical trials are titled and designed around HCV treatment regimens (peginterferon/ribavirin, boceprevir, danoprevir, and other direct-acting antivirals), not HBV. The literature is dominated by reviews of HBV/HCV **co-infection management** rather than studies demonstrating ribavirin's efficacy against HBV in isolation. The high TxGNN score therefore likely reflects strong knowledge-graph proximity between HBV and HCV (shared literature co-occurrence, shared treatment contexts) rather than a genuine, independently validated antiviral mechanism against HBV. This is consistent with the evidence pack's own assessment (Evidence Level L4, decision stage S1, "Research Question").

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | Completed | 23 | Most directly relevant trial — studied HBV reactivation risk during direct-acting antiviral treatment of HCV/HBV co-infected patients; not a test of ribavirin's efficacy against HBV itself |
| [NCT00215865](https://clinicaltrials.gov/study/NCT00215865) | Phase 3 | Completed | 600 | PEGIntron + ribavirin dosing comparison in HCV patients with prior treatment failure (relevance grade C — HCV only) |
| [NCT01220947](https://clinicaltrials.gov/study/NCT01220947) | Phase 2 | Completed | 421 | Danoprevir/ritonavir + Pegasys/Copegus (ribavirin) vs. Pegasys/Copegus alone in treatment-naive HCV (relevance grade C — HCV only) |
| [NCT01598090](https://clinicaltrials.gov/study/NCT01598090) | Phase 3 | Completed | 881 | Peginterferon lambda-1a + ribavirin + telaprevir vs. peginterferon alfa-2a regimen in genotype-1 HCV (relevance grade C — HCV only) |
| [NCT00265395](https://clinicaltrials.gov/study/NCT00265395) | Phase 3 | Completed | 1428 | PEG-Intron + Rebetol (ribavirin) duration comparison (48 vs 72 weeks) in genotype-1 HCV slow responders |
| [NCT00940420](https://clinicaltrials.gov/study/NCT00940420) | Phase 4 | Completed | 2695 | Large safety/tolerability study of Pegasys + Copegus (ribavirin) combination in chronic HCV |
| [NCT02996682](https://clinicaltrials.gov/study/NCT02996682) | Phase 3 | Completed | 102 | Sofosbuvir/velpatasvir ± ribavirin in HCV patients with decompensated cirrhosis |
| [NCT01854697](https://clinicaltrials.gov/study/NCT01854697) | Phase 3 | Completed | 311 | ABT-450/r/ABT-267 + ABT-333 ± ribavirin vs. telaprevir regimen in treatment-naive genotype-1 HCV |
| [NCT00086541](https://clinicaltrials.gov/study/NCT00086541) | Phase 3 | Completed | 515 | Interferon alfacon-1 + ribavirin vs. no treatment in HCV nonresponders to prior pegIFN/ribavirin |
| [NCT01937728](https://clinicaltrials.gov/study/NCT01937728) | Phase 4 | Completed | 542 | Tailored peginterferon alfa-2a + ribavirin duration per viral kinetics in genotype-1 HCV |

*Note: None of the above trials directly test ribavirin's efficacy against HBV; all are HCV treatment protocols or HCV/HBV co-infection management studies.*

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | Reviews HBV/HCV co-infection management; notes pegIFN + ribavirin as historical therapy for co-infected, HCV-RNA-positive patients |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | Updates on treatment/outcomes of dual chronic HCV/HBV infection |
| [18804888](https://pubmed.ncbi.nlm.nih.gov/18804888/) | 2008 | Review | J Hepatol | Discusses ongoing challenges in treating HBV/HCV co-infection |
| [19669238](https://pubmed.ncbi.nlm.nih.gov/19669238/) | 2009 | Review | Hepatology Int | Reviews viral interaction dynamics and treatment approaches in dual HBV/HCV infection |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Review | World J Gastroenterol | IL28B polymorphism's association with HCV treatment response; relevance to HBV outcomes remains unclear |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | Reviews treatment options for chronic HBV and HCV infection in children |
| [27433078](https://pubmed.ncbi.nlm.nih.gov/27433078/) | 2016 | Review | World J Gastroenterol | Discusses IFN-α ± ribavirin as prototype therapy for both HBV and HCV; notes HBV persists despite DAA/ribavirin-based regimens |
| [21538279](https://pubmed.ncbi.nlm.nih.gov/21538279/) | 2011 | Review | Semin Liver Dis | Host genetic determinants of chronic HBV and HCV infection outcomes |
| [15864105](https://pubmed.ncbi.nlm.nih.gov/15864105/) | 2005 | Review | Curr Opin Infect Dis | Reviews natural history and treatment efficacy for pediatric HBV and HCV infection |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Review | Curr Opin Virol | Effect of IL28B genotype on treatment-induced and spontaneous clearance in HCV, with discussion of HBV genotype associations |

*Note: No literature directly demonstrates ribavirin monotherapy or combination efficacy specifically against HBV; several sources instead note that HBV persists despite DAA/ribavirin-based regimens.*

---

## India Market Information

Ribavirin currently has **no marketing authorization registered in India** (0 registrations; market status: Not Marketed). No license/product data is available for review.

---

## Safety Considerations

- **Drug Interactions**: A DDInter query identified **105 total known interactions** for Ribavirin. Severity levels are not classified in the source data (all listed as "Unknown"). Interacting drugs include Calcitriol, Pantoprazole, Glimepiride, Mesalazine, Doxycycline, Clotrimazole, Morphine, Metformin, Omeprazole, Lansoprazole, Cimetidine, Nizatidine, Prednisone, Amphotericin B, Hydrocortisone, Potassium chloride, Dicyclomine, Acarbose, Sucralfate, and Rosiglitazone, among others. Clinical significance of these interactions requires further review, as severity classification is currently unavailable.

*Key warnings and contraindications from India regulatory labeling are not yet available; formal safety evaluation (S1) is blocked pending this data (see Data Gap DG001).*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a very high prediction score (99.86%) and a large volume of trials/literature was retrieved, virtually none of this evidence directly supports ribavirin's antiviral activity against HBV — the trials are HCV treatment protocols, and the literature centers on HBV/HCV co-infection management where HBV persistence despite ribavirin-containing regimens is repeatedly noted. The mechanistic basis for extending an RNA-virus-targeted mutagen to a DNA virus (HBV) is not established. Combined with missing MOA and India regulatory/safety label data, this candidate is not ready to advance past the research-question stage.

**To proceed, the following is needed:**
- Confirmed Ribavirin mechanism of action data (DrugBank API query, per DG002)
- India-specific approved indication text and label warnings/contraindications (per DG001, currently Blocking)
- Direct preclinical or clinical evidence of antiviral activity against HBV specifically (not merely HCV/HBV co-infection management context)
- DDI severity/clinical significance classification (currently 105 interactions with "Unknown" level)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

