---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 165
evidence_level: L5
indication_count: 2
---

# Denosumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Denosumab: From Osteoporosis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Denosumab is a fully human monoclonal antibody targeting RANKL (Receptor Activator of Nuclear Factor Kappa-B Ligand), primarily approved for osteoporosis and prevention of skeletal-related events associated with bone metastases.
The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**, with a near-perfect prediction score of 99.63%.
However, **no clinical trials** and **no publications** currently directly support this specific indication — this prediction is entirely model-driven at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoporosis; prevention of skeletal-related events in bone metastases (known approved indications globally) |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from our regulatory data sources. Based on known pharmacology, Denosumab is a fully human IgG2 monoclonal antibody that binds and inhibits RANKL, thereby suppressing osteoclast formation, function, and survival — the core mechanism underlying its approvals for osteoporosis and bone metastases management in markets such as the US, EU, and Japan.

The mechanistic bridge to severe nonproliferative diabetic retinopathy (SNPDR) is biologically plausible but unvalidated. The RANKL/OPG signaling axis may play a role in retinal pericyte survival, and RANKL inhibition could theoretically suppress downstream NF-κB-driven inflammatory pathways relevant to diabetic microvascular damage. Separately, a real-world cohort study (PMID 38899553, evaluating the broader diabetic retinopathy category) suggests Denosumab may reduce microvascular complications in type 2 diabetes — possibly through secondary improvements in insulin sensitivity — providing a weak indirect signal.

That said, none of these mechanistic links have been validated specifically in retinal tissue, and the high TxGNN score (0.9963) most likely reflects indirect pathway associations in the knowledge graph (connecting bone metabolism nodes to diabetic microvascular disease nodes) rather than direct biological evidence. The mechanistic leap from systemic RANKL inhibition in bone to retinal microvasculature pathology requires substantial preclinical investigation before a clinical hypothesis can be responsibly articulated.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for severe nonproliferative diabetic retinopathy.

---

## Literature Evidence

Currently no related literature available for severe nonproliferative diabetic retinopathy.

---

## India Market Information

Denosumab is currently not registered or marketed in India. No approved indication data is available from the regulatory database (0 active licenses on record).

---

## Safety Considerations

**Drug Interactions**: Denosumab has **193 recorded interactions** in the DDInter database. All interactions identified in this evidence pack are classified as **Moderate** severity. Key interaction categories include:

| Interacting Drug(s) | Level | Clinical Note |
|---------------------|-------|---------------|
| Corticosteroids (Hydrocortisone, Dexamethasone, Prednisolone, Prednisone, Betamethasone, Budesonide, Methylprednisolone, Triamcinolone) | Moderate | Concurrent use may potentiate immunosuppression and increase infection risk; corticosteroids also independently impair bone metabolism |
| Tacrolimus | Moderate | Additive immunosuppression requires monitoring for opportunistic infections |
| Dupilumab | Moderate | Combined immunomodulation warrants clinical vigilance |
| Mercaptopurine | Moderate | Potential additive immunosuppression |
| Radiopharmaceuticals (Ibritumomab tiuxetan, Tositumomab I-131, Iobenguane I-131) | Moderate | Combination with myelosuppressive agents may increase hematologic toxicity risk |
| Levamisole, Trimetrexate | Moderate | Immunomodulatory interactions; clinical significance requires case-by-case assessment |

> Formal warnings, contraindications, and full prescribing information were not available in this evidence pack (Data Gap DG001). Please refer to the FDA/EMA package insert for complete safety guidance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.63%), there is currently zero direct clinical or preclinical evidence linking Denosumab to severe nonproliferative diabetic retinopathy. The mechanistic rationale rests entirely on indirect inference from knowledge graph topology, and the drug has no regulatory presence in India.

**To proceed, the following is needed:**

- **Preclinical validation**: In vitro and in vivo studies to assess whether RANKL inhibition has measurable effects on retinal pericyte survival and retinal microvasculature in diabetic animal models
- **Mechanistic clarification**: Establish whether the RANKL/OPG pathway is functionally active in retinal tissue and whether Denosumab's known downstream effects (NF-κB suppression, OPG upregulation) are relevant in a diabetic retinal context
- **Broader DR signal review**: The related evidence for the rank-2 indication (Diabetic Retinopathy — PMID 38899553 cohort study and NCT00925600 Phase 3 trial) should be fully reviewed to determine whether any signal is transferable to the more severe SNPDR subtype
- **MOA data retrieval**: Retrieve complete DrugBank MOA record (Data Gap DG002) to enable a rigorous mechanistic link analysis
- **Safety profile completion**: Obtain TFDA/FDA package insert to resolve key warnings and contraindications (Data Gap DG001) before any S1 safety screening can proceed
- **Regulatory pathway scoping**: If preclinical signals emerge, a regulatory strategy for India market entry would need to be defined prior to any clinical development planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

