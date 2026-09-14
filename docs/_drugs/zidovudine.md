---
layout: default
title: Zidovudine
parent: 僅模型預測 (L5)
nav_order: 894
evidence_level: L5
indication_count: 6
---

# Zidovudine
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

# Zidovudine: From HIV/AIDS to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

> Zidovudine (AZT) is a nucleoside reverse transcriptase inhibitor (NRTI) originally developed and approved for HIV/AIDS treatment.
> The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) infection** — a lentiviral disease that only occurs in non-human primates —
> with **0 clinical trials** and **20 publications** (all preclinical animal-model studies) supporting this specific direction.
> Because SIV is not a human disease, this is not a translatable repurposing candidate; it reflects a mechanistic analogy (same NRTI target, same viral genus) rather than a new clinical indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV/AIDS (Human Immunodeficiency Virus infection) — established international indication; no India regulatory license text is present in this evidence pack |
| Predicted New Indication | Simian Immunodeficiency Virus Infection (non-human primate lentiviral disease) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L4 (preclinical/mechanistic studies only) |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in this evidence pack (DG002). Based on the available literature, zidovudine is an NRTI: it is phosphorylated intracellularly and, as the triphosphate, competitively inhibits reverse transcriptase and causes viral DNA chain termination — the mechanism that made it the first approved antiretroviral for HIV/AIDS.

SIV and HIV are both members of the *Lentivirus* genus and share highly homologous reverse transcriptase enzymes, which is why AZT shows measurable antiviral activity against SIV in vitro and in rhesus/cynomolgus macaque models. This explains why TxGNN's knowledge graph places these two diseases close together and assigns a very high similarity score.

However, this mechanistic overlap does not make SIV infection a viable human repurposing target: SIV does not infect humans, and all 20 supporting publications are animal-model or in vitro studies (prophylaxis, viral-load kinetics, resistance mutations) rather than human clinical evidence. This is best understood as TxGNN correctly identifying a biologically real drug-target relationship that happens to fall on a non-human disease node — useful for validating the model, but not actionable as a new human indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1489181](https://pubmed.ncbi.nlm.nih.gov/1489181/) | 1992 | Animal model | Antimicrob Agents Chemother | Oral AZT prevented SIV infection in infant rhesus macaques given pre/post-exposure prophylaxis |
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | Animal model | AIDS | AZT+3TC+indinavir postexposure prophylaxis prevented vaginal SIV transmission in macaques |
| [7848683](https://pubmed.ncbi.nlm.nih.gov/7848683/) | 1994 | Animal model | AIDS Res Hum Retroviruses | AZT reduced viral load kinetics during acute SIV infection in cynomolgus macaques |
| [7695293](https://pubmed.ncbi.nlm.nih.gov/7695293/) | 1995 | Animal model | Antimicrob Agents Chemother | Immediate AZT treatment protected SIV-infected newborn macaques from rapid-onset AIDS |
| [7797947](https://pubmed.ncbi.nlm.nih.gov/7797947/) | 1995 | Animal model | J Infect Dis | AZT prolonged survival and lowered CNS/CSF virus load in perinatally SIV-infected macaques |
| [9021180](https://pubmed.ncbi.nlm.nih.gov/9021180/) | 1997 | Animal model (resistance) | Antimicrob Agents Chemother | Identified AZT-resistant SIV mutant (Q151M in reverse transcriptase) causing AIDS in newborn macaques |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal model | J Virol | Quadruple antiretroviral therapy (incl. AZT) produced rapid viral decay in SIV-infected macaques |
| [2016686](https://pubmed.ncbi.nlm.nih.gov/2016686/) | 1991 | Animal model | J Acquir Immune Defic Syndr | Compared antiviral effects of AZT vs. 3'-fluorothymidine in SIV-infected cynomolgus monkeys |
| [22713337](https://pubmed.ncbi.nlm.nih.gov/22713337/) | 2012 | In vitro/animal model | Antimicrob Agents Chemother | SIV response to a novel NRTI benchmarked in vitro and in vivo against existing NRTIs including AZT |
| [8452370](https://pubmed.ncbi.nlm.nih.gov/8452370/) | 1993 | In vitro | Antimicrob Agents Chemother | AZT vs. neutralizing antibodies on SIV-infected macaque macrophages |

---

## India Market Information

Zidovudine currently has **no registered license** in this evidence pack (`total_licenses: 0`, market status: Not Marketed). No authorization records are available to summarize.

---

## Safety Considerations

**Drug Interactions (DDI):** The database records 235 total documented interactions. Notable examples from the returned set:

- **Moderate-level:** Amphotericin B (all formulations), Betamethasone, Budesonide, Dexamethasone, Hydrocortisone, Prednisolone, Prednisone, Triamcinolone, Naltrexone, Orlistat, Rosuvastatin, Simvastatin
- **Minor-level:** Cimetidine, Clarithromycin
- **Level not classified:** Pantoprazole, Morphine, Metformin, Omeprazole

Key warnings and contraindications are not available in this evidence pack (flagged as Blocking data gap DG001 — TFDA/India label warnings and contraindications). Please refer to the official package insert once available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (SIV infection) and the second-ranked prediction (feline AIDS) are non-human animal diseases and therefore not viable human repurposing targets, despite very high TxGNN similarity scores (~99.96%). Two other high-scoring predictions in this pack (an ultra-rare neurodevelopmental disorder and an "obsolete" metabolic disease concept) have zero supporting trials or literature and are best treated as knowledge-graph noise (L5). Two lower-ranked entries in this set — "AIDS related complex" and "congenital HIV" — are not new indications at all; they are zidovudine's own original, already-approved uses (including the landmark ACTG 076 perinatal-transmission trials), and their L1/"Proceed with Guardrails" status reflects mature standard-of-care evidence rather than a repurposing opportunity.

**To proceed, the following is needed:**
- TFDA/India label warnings, contraindications, and boxed-warning text (DG001, Blocking)
- Formal mechanism-of-action documentation from DrugBank (DG002)
- A re-run of the TxGNN candidate list filtered to exclude non-human disease nodes and the drug's own original indications, to surface genuinely novel human repurposing candidates
- If India market entry is being considered even for the existing HIV/AIDS indication, a full regulatory dossier and local licensing pathway assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

