---
layout: default
title: Micafungin
parent: 僅模型預測 (L5)
nav_order: 414
evidence_level: L5
indication_count: 1
---

# Micafungin
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

# Micafungin: From Invasive Candidiasis to Urinary Tract Infection

## One-Sentence Summary

Micafungin is an echinocandin class antifungal agent approved in multiple countries for the treatment and prophylaxis of invasive candidiasis and esophageal candidiasis.
The TxGNN model predicts it may be effective for **Urinary Tract Infection (Candida UTI)**,
with **0 clinical trials** and **13 publications** currently supporting this direction — though the mechanistic basis for this indication remains pharmacokinetically controversial.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Invasive candidiasis; esophageal candidiasis; prophylaxis in hematopoietic stem cell transplant recipients |
| Predicted New Indication | Urinary Tract Infection (Candida UTI) |
| TxGNN Prediction Score | 99.03% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Micafungin belongs to the echinocandin class of antifungal agents. Its mechanism of action is the inhibition of β-1,3-D-glucan synthase — an enzyme essential for fungal cell wall biosynthesis that has no mammalian equivalent. This mechanism is broadly fungicidal against *Candida* species, including many azole-resistant strains such as *Candida krusei* and *Candida glabrata*. Because urinary tract infections caused by *Candida* (candiduria) share the same pathogens treated by micafungin in systemic settings, the TxGNN model likely identified this mechanistic overlap and awarded a high prediction score.

However, there is a well-recognised pharmacokinetic barrier for this indication: echinocandins including micafungin are excreted in urine at extremely low concentrations — less than 1% of the administered dose reaches the urine as active drug. IDSA guidelines therefore do not recommend echinocandins as first-line agents for Candida UTI, precisely because urine drug concentrations are unlikely to achieve the minimum inhibitory concentration (MIC) at standard doses. The high TxGNN score (0.990) most plausibly reflects the drug's general anti-*Candida* activity rather than site-specific pharmacodynamic evidence for the urinary compartment.

Despite this limitation, the published literature documents a niche where micafungin has been used off-label with reported success: patients with fluconazole-resistant or azole-intolerant *Candida* UTI (e.g., transplant recipients, premature neonates, patients with hepatic dysfunction), particularly when alternative options are exhausted. One pharmacokinetic study (PMID 27424599) argued that therapeutic drug monitoring of urinary micafungin levels could optimise dosing for selected cases. This positions micafungin as a potential salvage-therapy option rather than a broad repurposing candidate, and the current evidence base does not yet support a formal development programme for this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [27587066](https://pubmed.ncbi.nlm.nih.gov/27587066/) | 2016 | Retrospective Cohort | Int J Urol Nephrol | Examined candiduria elimination rates in micafungin-treated hospitalised patients; echinocandins active against azole-resistant *Candida* but limited by low urinary concentrations |
| [29109159](https://pubmed.ncbi.nlm.nih.gov/29109159/) | 2018 | Multi-site Retrospective | Antimicrob Agents Chemother | Characterised candiduria management in 305 hospitalised patients across multiple institutions; found significant antifungal overuse in asymptomatic candiduria contrary to guidelines |
| [35146837](https://pubmed.ncbi.nlm.nih.gov/35146837/) | 2022 | Retrospective Case Series | Pediatrics International | Reported treatment outcomes of critically ill PICU patients receiving micafungin for hospital-acquired *Candida* UTIs; analysed success rates across *Candida* species |
| [27424599](https://pubmed.ncbi.nlm.nih.gov/27424599/) | 2016 | Pharmacokinetic Study | Int J Antimicrob Agents | Six cases of *Candida* UTI (including 4 fluconazole-resistant) successfully treated with micafungin; proposed that therapeutic drug monitoring of urinary levels may enable optimal pharmacodynamic targeting |
| [26937340](https://pubmed.ncbi.nlm.nih.gov/26937340/) | 2016 | Case Series | Med Mycol Case Rep | Five cases of candiduria treated with parenteral micafungin for ≥6 days; all achieved resolution of fungal growth within 30 days of treatment completion |
| [31111613](https://pubmed.ncbi.nlm.nih.gov/31111613/) | 2019 | Case Report | Transplant Infect Dis | Successful eradication of chronic symptomatic *Candida krusei* UTI with increased-dose micafungin in a liver–kidney transplant recipient with intrinsic fluconazole resistance |
| [40765059](https://pubmed.ncbi.nlm.nih.gov/40765059/) | 2025 | Case Report | J Pharm Health Care Sci | Pyelonephritis and bacteraemia from fluconazole-resistant *Candida glabrata* in a patient on SGLT2 inhibitor; successfully treated with micafungin |
| [38827222](https://pubmed.ncbi.nlm.nih.gov/38827222/) | 2024 | Case Report | Front Pediatrics | *Candida glabrata* UTI in a premature neonate (NICU) treated successfully with micafungin; highlighted rising incidence of non-albicans *Candida* in vulnerable neonatal populations |
| [38681664](https://pubmed.ncbi.nlm.nih.gov/38681664/) | 2024 | Case Report | Med Mycol Case Rep | Unilateral renal fungus ball (micafungin-sensitive *Candida glabrata*) managed with combined antifungal therapy and endoscopic extraction |
| [33520520](https://pubmed.ncbi.nlm.nih.gov/33520520/) | 2020 | Case Report | Cureus | *Candida auris* UTI in a nursing home patient with multiple comorbidities; discussed micafungin as one of the few active options against this multidrug-resistant emerging pathogen |

---

## India Market Information

Micafungin is currently **not marketed in India**. No product registrations are on record (0 authorisations).

---

## Safety Considerations

**Drug Interactions (all Moderate level, source: DDInter):**

| Interacting Drug | Level | Clinical Note |
|-----------------|-------|--------------|
| Amphotericin B | Moderate | Potential additive nephrotoxicity; monitor renal function closely |
| Nitisinone | Moderate | Possible pharmacokinetic interaction; monitor for adverse effects |
| Everolimus | Moderate | Micafungin may increase everolimus plasma exposure; dose adjustment and level monitoring may be required |
| Ribociclib | Moderate | Monitor for increased drug exposure and QTc effects |
| Sirolimus | Moderate | Micafungin has been reported to increase sirolimus AUC; monitor trough levels and toxicity |

Please refer to the package insert for complete warnings and contraindications, as this data was not available for review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a high prediction score (99.03%) reflecting micafungin's potent anti-*Candida* activity, the fundamental pharmacokinetic barrier — less than 1% urinary excretion of active drug — directly undermines the mechanistic premise for treating urinary tract infections. The entire current evidence base (L4) consists of case reports, small case series, and retrospective studies with no registered prospective clinical trials, placing this firmly in the research-question stage. IDSA guidelines explicitly advise against echinocandins for Candida UTI except in highly selected refractory scenarios.

**To proceed, the following is needed:**

- **PK/PD validation**: Prospective pharmacokinetic data confirming that urinary micafungin concentrations at clinically safe doses can reliably exceed the MIC for target *Candida* species
- **Defined patient population**: Identify a specific subgroup (e.g., fluconazole-resistant *Candida* UTI in transplant recipients) where the benefit–risk calculation favours off-label use
- **Prospective study**: At least one Phase 2 or prospective observational study before clinical development can be justified
- **Regulatory package insert review**: Obtain CDSCO/TFDA package insert to document approved warnings and contraindications (currently a blocking data gap)
- **MOA data**: Retrieve full DrugBank MOA entry to complete mechanistic analysis
- **India regulatory pathway**: Assess whether compassionate use or off-label prescribing frameworks in India would apply for refractory candiduria cases while formal evidence is gathered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

