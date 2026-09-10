---
layout: default
title: Pembrolizumab
parent: 僅模型預測 (L5)
nav_order: 648
evidence_level: L5
indication_count: 10
---

# Pembrolizumab
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

# Pembrolizumab: From Advanced Melanoma to Gingival Fibromatosis

## One-Sentence Summary

Pembrolizumab (Keytruda®) is a PD-1 immune checkpoint inhibitor first approved for advanced/unresectable melanoma and since expanded to more than a dozen solid and hematologic cancers. The TxGNN model's top-ranked repurposing candidate in this batch is **Gingival Fibromatosis** (prediction score **99.40%**), but this specific prediction currently has **0 clinical trials** and **0 publications** supporting it — it is a model-only signal (Evidence Level L5) that the model's own rationale flags as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Advanced/unresectable Melanoma (first global approval, 2014); since expanded to NSCLC, HNSCC, classical Hodgkin lymphoma, urothelial carcinoma, MSI-H/dMMR solid tumors, and others |
| Predicted New Indication | Gingival Fibromatosis (fibromatosis, gingival) |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Pembrolizumab's confirmed mechanism (drawn from the pharmacology data in this evidence pack, since a formal DrugBank MOA field is still pending) is a humanized IgG4 monoclonal antibody that blocks PD-1 (CD279) on T-cells, preventing PD-1/PD-L1 mediated immune evasion by tumor cells. This mechanism underlies its efficacy across a wide range of malignancies with high tumor mutational burden or PD-L1 expression — melanoma, NSCLC, head and neck squamous cell carcinoma, MSI-H/dMMR tumors, and more.

Gingival fibromatosis, however, is a benign, non-neoplastic overgrowth of gingival connective tissue, typically driven by fibroblast proliferation (hereditary or drug-induced, e.g., by phenytoin, cyclosporine, or calcium channel blockers) rather than by immune evasion or checkpoint dysregulation. There is no established tumor-immunology pathway connecting PD-1 blockade to fibroblast-driven connective tissue overgrowth.

Consequently, the model's own generated rationale for this candidate explicitly states that gingival fibromatosis is a benign connective-tissue disorder — not an immune-evasive or neoplastic lesion — and that there is no plausible mechanistic link to PD-1 inhibition. With zero clinical trials and zero literature records retrieved, this prediction should be treated as a low-confidence embedding artifact rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Pembrolizumab has no registered licenses in India in this dataset (0 total licenses; market status: Not Marketed). No product/dosage-form/indication records are available to tabulate.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (anti-PD-1 immune checkpoint inhibitor monoclonal antibody) — not a conventional cytotoxic agent |
| Myelosuppression Risk | Low — checkpoint inhibitors act via immune activation rather than direct cytotoxicity; the dominant toxicity class is immune-related adverse events (irAEs) rather than bone marrow suppression |
| Emetogenicity Classification | Low |
| Monitoring Items | Thyroid function, liver function, renal function, pulmonary status (pneumonitis), skin, and signs of immune-related adverse events (colitis, hepatitis, endocrinopathy, myocarditis/myositis/myasthenia gravis, neurologic irAEs) — per general checkpoint-inhibitor toxicity literature retrieved in this pack |
| Handling Protection | As a biologic monoclonal antibody administered by IV/SC infusion, pembrolizumab does not require conventional hazardous cytotoxic drug handling precautions (e.g., NIOSH cytotoxic PPE); standard biologic infusion handling protocols apply |

---

## Safety Considerations

**Drug Interactions** (13 total on file):
- **Major**: Lenalidomide, Pomalidomide, Thalidomide
- **Moderate**: Hydrocortisone, Triamcinolone, Dexamethasone, Betamethasone, Budesonide, Prednisolone, Prednisone, Methylprednisolone, Deflazacort

(Systemic corticosteroids may blunt immunotherapy efficacy via immunosuppression; concomitant IMiDs carry major-level interaction flags.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Gingival Fibromatosis) has no clinical trial or literature support and is explicitly flagged by the model's own rationale as mechanistically implausible — it is best interpreted as an embedding-based ontology artifact rather than a genuine signal. Regulatory safety documentation (warnings/contraindications) is also incomplete, blocking a full safety assessment.

**To proceed, the following is needed:**
- TFDA/India label warnings and contraindications (currently a blocking data gap)
- Confirmed mechanism-of-action record via DrugBank API
- Re-review of disease-ontology mapping across this candidate batch — several other ranked candidates (e.g., "lung benign neoplasm," "lung germ cell tumor") show clinical trial/literature evidence that actually pertains to NSCLC rather than the labeled disease, suggesting systematic ontology-neighbor mismatches worth investigating before any candidate in this batch advances past Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

