---
layout: default
title: Clioquinol
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 7
---

# Clioquinol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Clioquinol: From Topical Antifungal/Antibacterial Use to Cutaneous Candidiasis

## One-Sentence Summary

Clioquinol (iodochlorhydroxyquin) is a halogenated hydroxyquinoline long formulated into topical corticosteroid-antimicrobial combination creams (e.g., Vioform-hydrocortisone, Locacorten-Vioform), though it currently holds no market registration in this system and no detailed mechanism-of-action record is on file. The TxGNN model predicts it may be effective for **cutaneous candidiasis**, and — unusually for a pure model prediction — this direction is already backed by **6 historical clinical publications** describing clioquinol-containing creams used against candidal skin infections, even though **no modern clinical trials** have been registered. This gives the prediction an evidence level of **L3**, reflecting observational/comparative clinical use rather than either a purely computational guess or a modern RCT-confirmed indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file — drug is unregistered locally, no approved indication text available (see Market Information below) |
| Predicted New Indication | Cutaneous Candidiasis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for clioquinol is not available in this evidence pack (data gap DG002, High severity). Based on general pharmacological knowledge, clioquinol is a halogenated 8-hydroxyquinoline derivative that has long been formulated into topical corticosteroid–antimicrobial combination products (e.g., Vioform-hydrocortisone, Locacorten-Vioform, halcinonide-Vioform). Its antifungal activity is generally attributed to metal chelation that disrupts the cell membrane and enzymatic systems of *Candida albicans* and related fungi.

Clioquinol's own historical clinical use is concentrated in dermatological infections — including cutaneous candidiasis, the very indication TxGNN is now predicting. Several older comparative studies captured in this evidence pack (PMID 155507, 6459255, 128475) directly evaluated clioquinol-containing creams against cutaneous candidiasis and secondarily infected dermatoses, with one reporting a 95% overall therapeutic response rate. This makes the TxGNN output less a novel discovery than a model-driven re-confirmation of a use pattern with decades of documented clinical precedent — though contemporary randomized controlled trial data is absent.

Mechanistically, cutaneous candidiasis is a superficial yeast infection of the skin, squarely within the antimicrobial spectrum long attributed to iodochlorhydroxyquin-based products. This gives the TxGNN-predicted association strong biological plausibility, even in the absence of a documented formal MOA record.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [155507](https://pubmed.ncbi.nlm.nih.gov/155507/) | 1979 | Cohort/Clinical Evaluation | Current Medical Research and Opinion | Halcinonide-neomycin-amphotericin cream vs. iodochlorhydroxyquin-hydrocortisone in cutaneous candidiasis: 95% (38/40) vs. 43% (17/40) overall therapeutic response |
| [6459255](https://pubmed.ncbi.nlm.nih.gov/6459255/) | 1981 | Cohort/Clinical Evaluation | The Journal of International Medical Research | Randomized comparison (n=154) of two topical corticosteroid-antimicrobial creams, one containing iodochlorhydroxyquin, showed equivalent therapeutic responses in cutaneous candidiasis and infected eczematous dermatoses |
| [128475](https://pubmed.ncbi.nlm.nih.gov/128475/) | 1975 | Cohort/Clinical Evaluation | Dermatologica | Double-blind study (n=430): Locacorten-Vioform (clioquinol) cream markedly more effective than either agent alone or placebo against secondarily infected dermatoses |
| [136333](https://pubmed.ncbi.nlm.nih.gov/136333/) | 1976 | Cohort/Clinical Evaluation | Current Therapeutic Research, Clinical and Experimental | Clinical evaluation of a new halcinonide-antifungal (clioquinol) combination cream (abstract not available) |
| [4220930](https://pubmed.ncbi.nlm.nih.gov/4220930/) | 1965 | Case Report/Etiology Study | Zeitschrift für Haut- und Geschlechtskrankheiten | Discussion of yeast (Candida) involvement in the etiology of Danbolt-Closs acrodermatitis enteropathica |
| [2978600](https://pubmed.ncbi.nlm.nih.gov/2978600/) | 1988 | Review/Prevention Study | Przegląd Dermatologiczny | In vitro evaluation of antimicrobial soap additives with fungicidal activity against *Candida albicans*, aimed at preventing occupational infection |

---

## India Market Information

Clioquinol currently has no market authorization or registration on file (market status: **Not Marketed**; total licenses: **0**).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple historical cohort/comparative studies (evidence level L3) directly support clioquinol's antifungal efficacy in cutaneous candidiasis-type infections, and the mechanistic plausibility is strong given its well-established antimicrobial spectrum. However, the absence of modern RCT data, no current local market authorization, and a **Blocking** data gap on regulatory safety warnings (DG001) mean this cannot yet advance past a guarded, staged evaluation.

**To proceed, the following is needed:**
- Local label warnings and contraindications data (DG001, Blocking) — required before Stage 1 safety screening can be completed
- Documented mechanism-of-action data from DrugBank (DG002, High) to formally support the mechanistic rationale
- A completed drug interaction (DDI) database query (current status: not found)
- Separate evaluation of the other TxGNN-predicted indications for this drug (Majocchi granuloma, ectothrix/endothrix infectious disease, superficial mycosis, scalp/beard dermatophytosis, tinea profunda) — all score above 99% but remain at evidence level L5 (model prediction only, Research Question stage) and should not be prioritized ahead of cutaneous candidiasis
- Updated local market/registration status assessment if local registration is being considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

