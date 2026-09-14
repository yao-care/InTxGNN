---
layout: default
title: Vinblastine
parent: 僅模型預測 (L5)
nav_order: 881
evidence_level: L5
indication_count: 10
---

# Vinblastine
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

# Vinblastine: From Hodgkin Lymphoma to Rhabdomyosarcoma

## One-Sentence Summary

> Vinblastine is a vinca alkaloid historically used to treat Hodgkin lymphoma, testicular cancer, and other malignancies, though it currently holds no marketing authorization in India.
> The TxGNN model predicts it may be effective for **Rhabdomyosarcoma**,
> with **0 clinical trials directly testing vinblastine** and **16 publications** (mostly case reports and preclinical studies) currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not locally registered (globally used for Hodgkin lymphoma, testicular cancer, and other malignancies as part of combination chemotherapy) |
| Predicted New Indication | Rhabdomyosarcoma (disease) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L3 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the evidence pack (data gap DG002). Based on established pharmacology, vinblastine is a vinca alkaloid that binds tubulin and inhibits microtubule polymerization, arresting cells in mitosis (M-phase) — a class effect shared with vincristine and vinorelbine.

Rhabdomyosarcoma (RMS) is a pediatric soft-tissue sarcoma for which the standard-of-care VAC regimen (vincristine, actinomycin-D, cyclophosphamide) already relies on a vinca alkaloid. This creates strong mechanistic plausibility for vinblastine: the closely related agent vinorelbine has demonstrated activity in Phase II pediatric sarcoma trials, and individual case reports document vinblastine-containing combination regimens producing partial responses in perianal and prostatic RMS.

However, evidence for vinblastine *specifically* (as opposed to its vinca-alkaloid relatives vincristine/vinorelbine) remains limited to small case reports, xenograft models, and decades-old case series. No completed clinical trial has tested vinblastine directly in RMS, which is why the evidence level is capped at L3 despite the very high TxGNN prediction score.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38050209](https://pubmed.ncbi.nlm.nih.gov/38050209/) | 2023 | Case report | Medicine | Adult perianal RMS with nodal metastases achieved partial response after nivolumab, dacarbazine, cisplatin, and vinblastine following progression on prior therapy |
| [2451411](https://pubmed.ncbi.nlm.nih.gov/2451411/) | 1987 | Case report/review | Hinyokika Kiyo | Refractory prostatic RMS in a child; cisplatin + vinblastine + peplomycin (PVP) rapidly reduced pelvic tumor mass after relapse |
| [3329524](https://pubmed.ncbi.nlm.nih.gov/3329524/) | 1987 | Preclinical mechanistic | Anti-Cancer Drug Design | Examined therapeutic selectivity of vinca alkaloids (vincristine/vinblastine) using human RMS xenograft models in mice |
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Phase II trial (vinorelbine, related agent) | Eur J Cancer | Vinorelbine + low-dose cyclophosphamide showed efficacy and good tolerance in relapsed/refractory pediatric RMS |
| [15378498](https://pubmed.ncbi.nlm.nih.gov/15378498/) | 2004 | Pilot study (vinorelbine, related agent) | Cancer | Pilot study defining optimal vinorelbine + low-dose cyclophosphamide dosing ahead of European RMS protocol |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | Clinical study (vinorelbine, related agent) | Cancer | Vinorelbine showed activity in previously treated advanced pediatric sarcomas including RMS |
| [22156656](https://pubmed.ncbi.nlm.nih.gov/22156656/) | 2011 | Pilot study | Oncotarget | Metronomic 4-drug pediatric regimen explored as alternative strategy against resistant sarcomas |
| [26024389](https://pubmed.ncbi.nlm.nih.gov/26024389/) | 2015 | In vitro mechanistic | Cell Death Differ | PLK1 inhibitors synergize with microtubule-destabilizing drugs (vinca-alkaloid class) in preclinical RMS models |
| [16302215](https://pubmed.ncbi.nlm.nih.gov/16302215/) | 2007 | Case series (related sarcoma) | Pediatr Blood Cancer | Vinorelbine/low-dose cyclophosphamide regimen (developed for RMS) showed response in desmoplastic small round cell tumor |
| [41216926](https://pubmed.ncbi.nlm.nih.gov/41216926/) | 2026 | Prospective trial (non-RMS soft tissue sarcoma) | Pediatr Blood Cancer | CWS-96/CWS-2002P trials establish risk stratification and chemotherapy regimens for non-RMS soft tissue sarcomas, providing regimen context |

---

## India Market Information

Vinblastine currently holds **no marketing authorization** in India — market status is "Not Marketed" with 0 registered licenses on file. No product registration data is available to summarize.

---

## Cytotoxicity

Based on established pharmacological classification (DrugBank-level data not available in this evidence pack; DG002):

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Vinca alkaloid / microtubule inhibitor class) |
| Myelosuppression Risk | High — neutropenia is the primary dose-limiting toxicity of vinblastine |
| Emetogenicity Classification | Low to Moderate |
| Monitoring Items | CBC with differential (before each dose), liver function tests, assessment for peripheral neuropathy, extravasation site monitoring (vesicant) |
| Handling Protection | Required — vinblastine is a hazardous/cytotoxic agent and a vesicant; standard cytotoxic drug handling precautions apply. As a well-established class safety fact, vinca alkaloids including vinblastine are **fatal if administered intrathecally** — this is not sourced from local label data (which is a blocking data gap, DG001) and must be confirmed against the official package insert once available. |

---

## Safety Considerations

- **Drug Interactions**: 371 total interactions on file. Notable examples include a **Major** interaction with Clarithromycin, and **Moderate** interactions with Aprepitant, Dexamethasone, Metronidazole, Eliglustat, Miconazole, Rolapitant, Rosuvastatin, Simvastatin, Tinidazole, Glycerol phenylbutyrate, and Troglitazone. A Minor interaction is noted with Levofloxacin.

Key warnings and contraindications are not available in the current evidence pack (data gap DG001, Blocking severity) — please refer to the official package insert once obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence supporting vinblastine specifically (not just the vinca-alkaloid class) in rhabdomyosarcoma is limited to case reports, xenograft studies, and decades-old case series — no completed trial has tested vinblastine directly in this indication. Combined with the drug's complete absence from the India market (0 registrations) and a blocking data gap on local safety labeling, the evidence does not yet support proceeding.

**To proceed, the following is needed:**
- TFDA-equivalent package insert / local label data (warnings, contraindications) — DG001, Blocking
- Confirmed mechanism of action documentation via DrugBank — DG002
- A direct clinical study (even Phase I/II) evaluating vinblastine — not just related vinca alkaloids — in RMS
- A pathway for market authorization in India if this indication is pursued further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

