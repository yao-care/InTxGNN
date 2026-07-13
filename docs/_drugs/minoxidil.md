---
layout: default
title: Minoxidil
parent: 僅模型預測 (L5)
nav_order: 424
evidence_level: L5
indication_count: 10
---

# Minoxidil
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

# Minoxidil: From Hypertension to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Minoxidil is a potassium channel opener originally approved for the treatment of severe systemic hypertension, which subsequently gained widespread recognition as a topical and oral treatment for androgenetic alopecia due to its hair follicle-stimulating properties.
The TxGNN model predicts it may be effective for **Hypotrichosis Simplex of the Scalp** (a rare hereditary progressive hair loss disorder), with **0 registered clinical trials** and **3 publications** currently supporting this direction.
The evidence is limited to small case series and case reports, and this prediction is assessed as a preliminary research question rather than a ready clinical candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe hypertension; androgenetic alopecia (topical/oral) |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.9999% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on well-established pharmacological literature, Minoxidil acts as an ATP-sensitive potassium channel (K_ATP) opener that induces direct peripheral vasodilation. When applied to the scalp or taken orally at low doses, it promotes hair follicle survival through multiple complementary pathways: K_ATP channel activation increases follicular microvascular blood flow, upregulates vascular endothelial growth factor (VEGF), prolongs the anagen (active growth) phase of the hair cycle, and may activate Wnt/β-catenin signalling to support follicular proliferation.

Hypotrichosis simplex of the scalp (HSS) is a rare autosomal dominant monogenic disorder caused primarily by loss-of-function mutations in genes encoding structural follicular proteins — most notably *CDSN* (corneodesmosin), *LPAR6*, and *LIPH*. The result is progressive miniaturisation and loss of scalp hair follicles from early childhood, without other ectodermal involvement. Minoxidil does not target the underlying genetic defect. However, the phenotypic overlap is meaningful: both HSS and androgenetic alopecia (the established Minoxidil indication) involve follicular miniaturisation and premature transition into telogen rest. In follicles that retain residual structural integrity, Minoxidil's pro-anagen and pro-vascular mechanism could provide symptomatic benefit — slowing or partially reversing the functional decline even if the genetic lesion persists.

The three published reports in this evidence pack are consistent with this rationale, demonstrating partial but clinically observable responses (improved hair density and length) when oral or topical Minoxidil was used in confirmed HSS patients, including in paediatric cases. The prediction is therefore biologically plausible but mechanistically indirect, and must be interpreted as symptomatic adjunct therapy rather than disease-modifying treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | Case Series | Dermatologic Therapy | Hereditary HSS patients treated with oral minoxidil combined with topical growth factors showed observable improvement in hair density and length |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | Case Report | Journal of Dermatological Treatment | A 14-year-old HSS patient treated with combined platelet-rich plasma (PRP) intralesional injections and topical minoxidil 2% achieved improvement in hair density, assessed clinically and dermoscopically |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | Case Report | Frontiers in Genetics | An 8-year-old male with genetically confirmed HSS (*CDSN* mutation) was treated with botanical extracts combined with minoxidil; partial clinical response reported, illustrating feasibility of minoxidil use in paediatric HSS |

---

## India Market Information

Minoxidil (DB00350) currently has no registered products in the India regulatory database. No authorisation records are available.

---

## Safety Considerations

**Drug Interactions:** Minoxidil has 275 documented drug interactions on record. The following are representative moderate-level interactions relevant to clinical use:

| Interacting Drug | Interaction Level | Clinical Relevance |
|-----------------|------------------|--------------------|
| Hydrocortisone | Moderate | Corticosteroids may antagonise hypotensive effects; monitor blood pressure |
| Dexamethasone | Moderate | As above; monitor cardiovascular response |
| Prednisolone / Prednisone | Moderate | As above |
| Betamethasone / Budesonide / Triamcinolone | Moderate | As above |
| Canagliflozin / Dapagliflozin / Empagliflozin / Ertugliflozin | Moderate | SGLT-2 inhibitors may potentiate hypotensive effect; additive blood pressure lowering risk |
| Bupropion | Moderate | Monitor for cardiovascular effects including elevated heart rate |
| Morphine / Opium | Moderate | Additive hypotensive risk; monitor haemodynamics |
| Sapropterin | Moderate | Monitor haemodynamic parameters |
| Nabilone / Dronabinol | Moderate | Additive hypotensive risk with cannabinoids |

> Warnings and contraindications data are not available in the current evidence pack. Please refer to the package insert for complete safety information before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The current evidence base consists entirely of 3 case reports and case series (Evidence Level L4), with no registered clinical trials for this specific indication. Although the biological rationale is plausible — Minoxidil's pro-anagen mechanism may partially compensate for the follicular functional decline in HSS — the drug does not address the underlying genetic structural defect, limiting its therapeutic role to symptomatic support. The paediatric onset of HSS also raises additional safety considerations that have not been systematically evaluated.

**To proceed, the following is needed:**

- **Prospective pilot study:** A structured observational study or small interventional study with standardised trichoscopic endpoints (hair count per cm², hair shaft diameter) specifically in genetically confirmed HSS patients
- **Mechanism of action documentation:** Retrieve full MOA data from DrugBank API to support the mechanistic link argument
- **Paediatric safety profile:** Assess systemic absorption and cardiovascular safety data for oral and topical Minoxidil in paediatric populations (HSS often presents in childhood)
- **India regulatory pathway assessment:** If a clinical study is planned in India, evaluate whether Minoxidil's existing regulatory status (e.g., off-label use) facilitates a Phase 2 investigator-initiated trial
- **Package insert review:** Download and parse the package insert to identify contraindications and black-box warnings not captured in the current evidence pack (Data Gap DG001)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

