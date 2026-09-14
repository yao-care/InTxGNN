---
layout: default
title: Vandetanib
parent: 僅模型預測 (L5)
nav_order: 873
evidence_level: L5
indication_count: 10
---

# Vandetanib
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

# Vandetanib: From Medullary Thyroid Cancer to Renal Cell Carcinoma

## One-Sentence Summary

> Vandetanib is a multi-targeted tyrosine kinase inhibitor (VEGFR2/3, EGFR, RET) originally used to treat advanced medullary thyroid cancer.
> The TxGNN model predicts it may be effective for **Renal Cell Carcinoma**,
> with **4 clinical trials** and **6 publications** currently supporting this direction — though most trials are small, terminated, or Phase 2 only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Medullary Thyroid Cancer (per literature evidence; not formally captured in structured `original_indications`) |
| Predicted New Indication | Renal Cell Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Vandetanib is a multi-target tyrosine kinase inhibitor with activity against VEGFR2/3, EGFR, and RET. Its approved use in medullary thyroid cancer is driven primarily by RET pathway inhibition (constitutively activated RET kinase in MTC). Structured mechanism-of-action data was not available in DrugBank for this Evidence Pack, so the MOA description above is reconstructed from the literature and predicted-indication rationale fields supplied in the pack rather than a formal `original_moa` record.

Renal cell carcinoma — particularly Von Hippel-Lindau (VHL)-associated and clear cell subtypes — is a prototypically angiogenesis-dependent tumor, driven by the VHL-HIF-VEGF axis. Because vandetanib's VEGFR2 inhibitory activity is a core part of its pharmacology (independent of its RET activity in MTC), there is a direct mechanistic rationale for activity in VEGF-driven RCC subtypes, even though the two cancers are unrelated by tissue origin.

This mechanistic plausibility is reflected in the trial record: the strongest single study (NCT00566995) specifically enrolled patients with VHL disease and renal tumors, directly testing the VEGFR-inhibition hypothesis. However, several other RCC-labeled trials in this Evidence Pack (e.g., NCT01191892, using a carboplatin+gemcitabine backbone) appear to actually target urothelial/transitional cell carcinoma rather than renal cell carcinoma, suggesting a possible disease-label mismatch that should be verified before relying on aggregate trial counts.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | Completed | 37 | Tested vandetanib in VHL disease and renal tumors; directly probes VEGFR-driven RCC biology (Grade A relevance). |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | Completed | 82 | Randomized carboplatin+gemcitabine ± vandetanib in cisplatin-ineligible advanced urothelial cancer; chemo backbone suggests this is urothelial, not RCC, cancer — disease label likely mismatched (Grade C). |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | Terminated | 7 | Vandetanib + metformin in HLRCC/SDH-associated kidney cancer or sporadic papillary RCC; terminated early, very small n. |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | Terminated | 3 | Vandetanib monotherapy in advanced clear cell RCC; terminated with only 3 patients enrolled — hypothesis-generating only. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clinical & Experimental Metastasis | Discusses targeted therapy combinations under evaluation for fumarate hydratase-deficient RCC, a molecularly defined RCC subtype with no established standard regimen. |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review | OncoTargets and Therapy | Reviews antiangiogenic TKIs (including vandetanib) approved across solid tumor types, framing the VEGFR-inhibition rationale for angiogenesis-dependent cancers. |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Review | Bulletin du Cancer | Reviews cabozantinib (VEGFR2/MET/RET inhibitor) MOA and efficacy, providing class-level context for RET/VEGFR-targeted agents like vandetanib. |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | ASCO Educational Book | Confirms vandetanib's FDA approval for RET-driven medullary thyroid cancer — the drug's established original indication. |
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | Trial (different drug) | Clinical Cancer Research | Phase 2 trial of guadecitabine (not vandetanib) in SDH-deficient tumors including HLRCC-associated RCC; relevant disease context but not direct vandetanib evidence. |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclinical/Animal Model | Molecular Cancer Research | Mouse model of TFE3 translocation RCC identifying novel therapeutic targets and a diagnostic biomarker (GPNMB); does not test vandetanib directly. |

---

## India Market Information

Vandetanib is **not currently marketed in India** (0 registrations, market status: not marketed). No authorization records are available for review.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor: VEGFR2/3, EGFR, RET) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Not directly reported in this Evidence Pack for vandetanib specifically; please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Not directly reported in this Evidence Pack; please refer to the package insert warnings and precautions |
| Monitoring Items | Hepatic function (class-level meta-analysis of anti-angiogenic TKI hepatotoxicity, PMID 23981115) and renal function/urinalysis for proteinuria (class-level VEGFR-TKI meta-analysis, PMID 32105149) |
| Handling Protection | No vandetanib-specific handling data in this pack; as an oral antineoplastic agent, follow institutional hazardous-drug handling protocols pending confirmation |

---

## Safety Considerations

**Drug Interactions** (296 total interactions on file; sample below):

| Interacting Drug | Severity |
|---|---|
| Clarithromycin | Major |
| Picosulfuric acid | Major |
| Polyethylene glycol (3350 with electrolytes) | Major |
| Dolasetron | Major |
| Palonosetron | Major |
| Sodium sulfate | Major |
| Levofloxacin | Major |
| Famotidine | Moderate |
| Metformin | Moderate |
| Loperamide | Moderate |
| Dexamethasone | Moderate |
| Bisacodyl | Moderate |
| Lactitol | Moderate |

Minor-level interactions (Ranitidine, Rabeprazole, Dexlansoprazole, Naloxegol, Lansoprazole, Metronidazole, Omeprazole) are also on file but generally require no action.

No structured key warnings or contraindications are currently available — please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
A blocking data gap exists on India-specific labeling (warnings/contraindications), which prevents completion of the S1 safety assessment. While the mechanistic rationale for VEGFR-driven RCC subtypes (especially VHL-associated/clear cell RCC) is sound and supported by an L2-level completed Phase 2 trial, the overall evidence base is thin — most trials are small, terminated, or possibly mislabeled — and the drug has no market presence in India.

**To proceed, the following is needed:**
- Resolve DG001 (India labeling/warnings/contraindications) — currently Blocking
- Resolve DG002 (formal MOA confirmation via DrugBank API)
- Verify whether NCT01191892 is correctly labeled as RCC or is actually urothelial cancer, before counting it as supporting evidence
- Prioritize confirmatory studies in VHL-associated/clear cell RCC specifically, where mechanistic and trial evidence is strongest
- Establish an India regulatory pathway assessment given current non-marketed status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

