---
layout: default
title: Clofazimine
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 3
---

# Clofazimine
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

Using the report structure from your v5 prompt, I'll flag upfront: `original_indications` and `taiwan_regulatory.licenses` are both empty in this Evidence Pack, so "Leprosy" below is stated as general pharmacological background knowledge (also corroborated by the literature entries in this same pack — e.g. PMID 12616942 references leprosy MDT with clofazimine), not extracted from a Taiwan license record. I did not guess at anything not otherwise supportable.

# Clofazimine: From Leprosy to Pneumocystosis

## One-Sentence Summary

Clofazimine is a riminophenazine antimycobacterial historically used to treat leprosy (Hansen's disease) as part of WHO multidrug therapy. The TxGNN model predicts potential efficacy against **Pneumocystosis**, but this is currently supported by only **1 clinical trial** (which actually targets a different pathogen — MAC, not *Pneumocystis*) and **4 publications**, none of which provide direct evidence of clofazimine treating or preventing *Pneumocystis* infection. Evidence quality is low, and the prediction rationale itself suggests the score may reflect a knowledge-graph confounding artifact rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Leprosy (Hansen's disease) — general pharmacological knowledge; no Taiwan-specific license text available |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Taiwan Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (Data Gap DG002). Based on known information, Clofazimine is a riminophenazine-class antimycobacterial agent used primarily in the WHO multidrug therapy (MDT) regimen for leprosy (*Mycobacterium leprae* infection), and its efficacy in that indication has been well established for decades. Mechanistically, it binds mycobacterial DNA, generates reactive oxygen species, and stabilizes cell membranes — actions oriented specifically toward mycobacterial pathogens.

*Pneumocystis jirovecii*, the causative organism of pneumocystosis, is a fungus-like organism that is biologically and pharmacologically distinct from *Mycobacterium leprae*. There is no established pharmacological pathway connecting clofazimine's antimycobacterial mechanism to antifungal or anti-*Pneumocystis* activity.

Per the repurposing rationale accompanying this prediction, the model's high confidence score likely arises from co-occurrence bias in the underlying knowledge graph: in HIV/AIDS literature, prophylaxis against *Mycobacterium avium* complex (MAC) and prophylaxis/treatment of *Pneumocystis carinii* pneumonia (PCP) are frequently discussed together, since both are common opportunistic infections in the same immunocompromised patient population. Clofazimine's well-documented role as a MAC prophylactic agent may have caused the model to associate it with PCP by proximity in the literature, rather than through any direct biological mechanism. This substantially weakens the biological plausibility of the prediction and is the main driver of the Hold recommendation below.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002058](https://clinicaltrials.gov/study/NCT00002058) | N/A | Completed | N/A | Randomized prophylaxis trial of clofazimine to prevent *Mycobacterium avium* complex (MAC) infection in HIV-positive patients. Targets MAC, **not** *Pneumocystis*; relevance graded **C (low)** — included in this evidence set only because both are AIDS-related opportunistic infection topics. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Review | PI Perspective | General review of opportunistic infection updates in AIDS; no clofazimine–*Pneumocystis* specific data available. |
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | Cohort/clinical study (MAC, not PCP) | The Journal of Infectious Diseases | Community-based trial of clofazimine prophylaxis for disseminated MAC infection in HIV patients with a prior PCP episode or CD4 ≤100/mm³; evaluates MAC prevention, not *Pneumocystis* treatment. |
| [6299154](https://pubmed.ncbi.nlm.nih.gov/6299154/) | 1983 | Case report | Annals of Internal Medicine | Hemophilia patient with PCP and disseminated MAC bacteremia; clofazimine's role, if any, is not tied to PCP management. |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Case report | Infection | AIDS patient with *M. kansasii* lung disease complicated by PCP, treated with a multidrug regimen (including clofazimine) plus TMP-SMX for PCP; clofazimine's independent contribution to PCP resolution is not established. |

---

## Safety Considerations

**Drug Interactions**: 111 total interactions identified for Clofazimine. Notable examples:
- **Major**: Cisapride, Dolasetron (additive QT-prolongation/arrhythmia risk — clofazimine itself is associated with QT prolongation)
- **Moderate**: Famotidine, Loperamide, Bisacodyl, Clarithromycin, Levofloxacin, Picosulfuric acid, and several osmotic/laxative agents (polyethylene glycol with electrolytes, castor oil, glycerin, lactitol, lactulose, magnesium citrate, magnesium hydroxide, mineral oil), plus 5-HT3 antiemetics (Granisetron, Ondansetron, Palonosetron)
- **Minor**: Metronidazole

Detailed prescribing warnings and contraindications (DG001, Blocking severity) are not currently available in this evidence pack — please refer to the official package insert for complete safety information before any clinical use.

---

## Other Predicted Indications Screened (Lower Priority)

For completeness, two additional TxGNN candidates were screened in this evidence pack but are not the focus of this report, given weaker evidence:

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|-------------|-----------------|-----------------|------|
| 2 | Malaria | 99.60% | L4 | Research Question | Only *in vitro* activity reported for clofazimine **analogues** (not clofazimine itself); no clinical trials; most retrieved literature is about drug-resistant tuberculosis and is not actually malaria-relevant. |
| 3 | Gastrin secretion abnormality | 99.57% | L5 | Hold | No clinical trials or literature support whatsoever — score is a pure model output with no biological rationale. |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence quality for the pneumocystosis prediction is low (L4): the sole clinical trial targets MAC prophylaxis rather than *Pneumocystis*, and none of the four literature citations demonstrate clofazimine efficacy against *Pneumocystis jirovecii*. The prediction rationale itself indicates the high TxGNN score likely reflects knowledge-graph co-occurrence bias (MAC and PCP prophylaxis frequently discussed together in AIDS literature) rather than a genuine mechanistic link.

**To proceed, the following is needed:**
- TFDA package insert warnings/contraindications (DG001, Blocking) — required before any S1 safety evaluation can begin
- Confirmed mechanism-of-action data for Clofazimine (DG002, High)
- Direct preclinical or *in vitro* evidence of clofazimine activity against *Pneumocystis jirovecii* specifically (not MAC)
- If pursuing further research, a dedicated study design that isolates *Pneumocystis* outcomes from MAC co-infection confounding
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

