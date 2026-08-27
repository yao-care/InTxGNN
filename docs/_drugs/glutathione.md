---
layout: default
title: Glutathione
parent: 僅模型預測 (L5)
nav_order: 315
evidence_level: L5
indication_count: 10
---

# Glutathione
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

# Glutathione: From Antioxidant/Detoxification Use to Sclerosing Cholangitis

## One-Sentence Summary

> Glutathione is an endogenous tripeptide antioxidant commonly used as a detoxification/antioxidant supplement, though it is **not currently marketed in India** and has no approved indication on file.
> The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**, with a prediction score of **98.14%**,
> but the supporting evidence consists entirely of **preclinical/observational pathophysiology studies (0 clinical trials, 17 publications)** — and part of that literature raises a potential safety caution rather than a positive treatment signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — no approved indication on file (drug is unmarketed in India) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 98.14% |
| Evidence Level | L4 |
| India Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for glutathione is not available in this evidence pack. Based on known pharmacology, glutathione is the principal intracellular antioxidant and a substrate of glutathione S-transferase (GST) enzymes, which participate in detoxification of reactive oxygen species and xenobiotic metabolites. Because glutathione has no confirmed approved indication on file (India market status: not marketed, 0 registrations), there is no established original-indication baseline to compare against — the reasonableness of this prediction must rest on mechanistic and disease-biology grounds alone.

Sclerosing cholangitis (primary sclerosing cholangitis, PSC) is a chronic cholestatic liver disease marked by oxidative stress and biliary inflammation, which is superficially consistent with a role for an antioxidant such as glutathione. However, the literature retrieved for this candidate is almost entirely **disease pathophysiology research, not therapeutic intervention research**: studies document GST autoantibodies, trace-element (copper/selenium) metabolism abnormalities, and glutathione-pathway changes in xenobiotic-induced cholestasis animal models — none test glutathione administration as a treatment for PSC.

Notably, one line of evidence (PMID 18242955, PMID 15041041) shows that GST isoforms are themselves targets of autoantibodies in PSC and autoimmune hepatitis, suggesting that increasing GST-related antigen exposure (e.g., via exogenous glutathione) could theoretically aggravate rather than ameliorate autoimmune biliary injury. This means the mechanistic story is double-edged, and the prediction should be read as a hypothesis-generating signal rather than a validated therapeutic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36447600](https://pubmed.ncbi.nlm.nih.gov/36447600/) | 2021 | Cohort/Transcriptomic Study | Wellcome Open Research | Tissue-specific transcriptional/microbial differences in PSC-associated IBD linked to elevated colorectal cancer risk; no glutathione intervention tested |
| [9053974](https://pubmed.ncbi.nlm.nih.gov/9053974/) | 1995 | Cohort | Scandinavian Journal of Gastroenterology | Abnormal hepatic retention of copper and selenium found in PSC patients, indicating disrupted trace-element/antioxidant metabolism |
| [18242955](https://pubmed.ncbi.nlm.nih.gov/18242955/) | 2008 | Cohort (autoantibody study) | Journal of Autoimmunity | Identified autoantibodies against glutathione S-transferase theta 1 (GSTT1) in PSC/IBD patients — GST may be an autoimmune target, not just a protective enzyme |
| [29148959](https://pubmed.ncbi.nlm.nih.gov/29148959/) | 2017 | Cohort (parenteral nutrition/GGT monitoring) | JPEN | Case observations of antioxidant depletion in cholestatic patients with overlapping PSC/ulcerative colitis, monitored via γ-GT |
| [15041041](https://pubmed.ncbi.nlm.nih.gov/15041041/) | 2004 | Cohort (autoantibody study) | Journal of Autoimmunity | Anti-GST A1-1 autoantibodies detected in autoimmune hepatitis, reinforcing GST as an immune target in autoimmune/cholestatic liver disease |
| [17600122](https://pubmed.ncbi.nlm.nih.gov/17600122/) | 2007 | Animal Model | The American Journal of Pathology | Established a xenobiotic-induced (DDC-fed) mouse model of sclerosing cholangitis/biliary fibrosis to study cholangiopathy mechanisms |
| [39130146](https://pubmed.ncbi.nlm.nih.gov/39130146/) | 2023 | Mechanistic/Molecular Study | Gastro Hep Advances | Described early deregulation of cholangiocyte NR0B2 in PSC pathogenesis via omics profiling |
| [22370917](https://pubmed.ncbi.nlm.nih.gov/22370917/) | 2012 | Histopathology Study | Digestive Diseases and Sciences | Evaluated thioredoxin family proteins/proliferation markers as premalignancy biomarkers in PSC-associated gallbladder dysplasia |
| [30009888](https://pubmed.ncbi.nlm.nih.gov/30009888/) | 2018 | Animal Model/Metabolomics | Food and Chemical Toxicology | Metabolomic profiling of cholestatic liver damage in mice to elucidate injury mechanisms |
| [35863741](https://pubmed.ncbi.nlm.nih.gov/35863741/) | 2022 | Animal Model | Cellular and Molecular Gastroenterology and Hepatology | Prolonged melatonin (not glutathione) administration improved liver phenotypes in a cholestatic mouse model via MT1/MT2 receptor signaling |

---

## Safety Considerations

Please refer to the package insert for safety information. (No TFDA/local warnings, contraindications, or DDI data are currently available; a DDI database lookup also failed due to a missing local reference file.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence for sclerosing cholangitis is limited to preclinical and observational pathophysiology studies (Evidence Level L4) with zero clinical trials, and part of the literature (GST autoantibody findings) suggests a plausible safety concern rather than a supportive treatment signal — the mechanistic rationale is not strong enough to proceed. In addition, TFDA-equivalent label warnings/contraindications are marked as a **Blocking** data gap (DG001), which by itself prevents this candidate from entering an initial safety screen (S1).

**To proceed, the following is needed:**
- TFDA (or equivalent regulatory) label warnings and contraindications for glutathione (blocking gap — required before any S1 safety screening)
- Confirmed mechanism of action (MOA) and any officially approved indication (currently a data gap)
- A targeted assessment of whether the GST-autoantibody signal represents a real autoimmune-flare risk before any further investigation of glutathione in PSC
- Consideration of redirecting research priority to **myelodysplastic syndrome** (rank 2 candidate: Evidence Level L2, decision stage S2, 6 clinical trials on ezatiostat — a glutathione-analogue prodrug), which currently has substantially stronger clinical-trial-backed evidence than the top-ranked sclerosing cholangitis prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

