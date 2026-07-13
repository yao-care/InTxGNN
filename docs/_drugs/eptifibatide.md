---
layout: default
title: Eptifibatide
parent: 僅模型預測 (L5)
nav_order: 279
evidence_level: L5
indication_count: 10
---

# Eptifibatide
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

# Eptifibatide: From Acute Coronary Syndrome to Rheumatoid Arthritis

## One-Sentence Summary

Eptifibatide (Integrilin) is a reversible αIIbβ3 integrin (GP IIb/IIIa) inhibitor originally approved for acute coronary syndromes (ACS), where it prevents platelet aggregation during percutaneous coronary interventions and unstable angina management.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis** with a prediction score of **99.99%**; however, this is currently supported by **no clinical trials and no published literature**, making it a pure model-generated hypothesis at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute Coronary Syndrome (ACS) / Percutaneous Coronary Intervention |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, eptifibatide is a synthetic cyclic heptapeptide that reversibly blocks the αIIbβ3 integrin (glycoprotein IIb/IIIa receptor) — the final common pathway of platelet aggregation. Its clinical efficacy in ACS has been validated in landmark trials (PURSUIT, ESPRIT). The drug is administered intravenously and acts rapidly, making it well-suited for acute cardiovascular settings.

The theoretical bridge to rheumatoid arthritis relies on the observation that αIIbβ3 integrin is expressed in RA synovial tissue, and activated platelets release pro-inflammatory mediators — including IL-1β and PDGF — that can amplify synovial inflammation. In this model, blocking platelet aggregation via GP IIb/IIIa inhibition could theoretically reduce the inflammatory burden in the joint microenvironment.

However, this mechanistic link is highly indirect and speculative. RA pathogenesis is predominantly driven by the T-cell/B-cell/TNF-α/synovial fibroblast axis — mechanisms fundamentally distinct from platelet-mediated thromboinflammation. No preclinical RA model has tested eptifibatide, and the drug's exclusively intravenous route of administration presents a practical barrier to chronic disease management. The TxGNN prediction most likely reflects topological proximity in the knowledge graph rather than a validated disease–drug relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Eptifibatide is **not currently registered or marketed in India**. There are no product licenses on record with the regulatory authority.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No registrations found |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings and contraindications data were identified as a blocking data gap (DG001). Full safety evaluation requires downloading and parsing the official prescribing information. Based on eptifibatide's drug class (GP IIb/IIIa inhibitor), clinicians should be aware that **bleeding risk** is a primary class-level concern, and this would be especially relevant if considering use in non-ACS populations such as RA patients who may already receive concurrent NSAIDs or DMARDs.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score to rheumatoid arthritis, but this remains a purely computational signal (Evidence Level L5) with no preclinical, translational, or clinical data to support it. The indirect mechanistic hypothesis and the IV-only route of administration present significant barriers to development in a chronic inflammatory disease context.

**Notably, a higher-priority repurposing opportunity exists within this same evidence pack:** Eptifibatide for **hemoglobinopathy / sickle cell disease** (rank #7) carries Evidence Level L3, supported by 1 Phase I/II randomised controlled clinical trial ([NCT00834899](https://clinicaltrials.gov/study/NCT00834899)) and 4 peer-reviewed publications — including a Phase I clinical study (PMID [17916103](https://pubmed.ncbi.nlm.nih.gov/17916103/)) and a pilot efficacy study (PMID [23973010](https://pubmed.ncbi.nlm.nih.gov/23973010/)). That indication is recommended for **Research Question** evaluation and represents a more scientifically grounded repurposing path.

**To advance the rheumatoid arthritis hypothesis, the following is needed:**

- **Preclinical validation:** In vivo testing in collagen-induced arthritis (CIA) or adjuvant-induced arthritis (AIA) animal models to confirm anti-inflammatory activity
- **Biomarker studies:** In vitro confirmation of functional αIIbβ3 expression in RA synoviocytes and fibroblast-like synoviocytes (FLS)
- **MOA documentation:** Retrieval of complete mechanism of action data from DrugBank (remediation for DG002)
- **Safety profile review:** Full prescribing information and contraindication data from official package insert (remediation for DG001 — currently Blocking severity)
- **Route compatibility assessment:** Evaluation of whether IV administration can be adapted (e.g., oral antiplatelet alternatives with similar targets) for chronic RA management
- **Comparative opportunity analysis:** Weigh investment in RA (L5, no evidence) against the sickle cell disease cluster (L3–L4, existing clinical data) as a higher-yield priority
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

