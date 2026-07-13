---
layout: default
title: Desmopressin
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Desmopressin
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

# Desmopressin: From von Willebrand Disease / Mild Hemophilia A to Congenital Prothrombin Deficiency

---

## One-Sentence Summary

Desmopressin (DDAVP) is a synthetic vasopressin analog established in the management of von Willebrand disease (type 1), mild hemophilia A, and nocturnal enuresis, acting primarily by releasing von Willebrand factor (vWF) and Factor VIII from vascular endothelium.
The TxGNN model predicts it may have utility in **Congenital Prothrombin Deficiency** (Factor II deficiency), with a prediction score of **99.70%**; however, current evidence consists of only **4 publications** (all case reports or narrative reviews) and **no directly relevant clinical trials**, and the mechanistic rationale is questionable given that desmopressin does not directly supplement prothrombin.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | von Willebrand Disease / Mild Hemophilia A (known established use; not formally approved or marketed in India) |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L4 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Desmopressin is a synthetic analog of arginine vasopressin (ADH) that binds to V2 receptors on vascular endothelial cells, triggering rapid release of pre-formed von Willebrand factor (vWF) multimers and coagulation Factor VIII (FVIII) from Weibel-Palade bodies. This 3–5 fold transient elevation of circulating vWF and FVIII underpins its established use in von Willebrand disease (type 1) and mild hemophilia A.

Congenital prothrombin deficiency (Factor II deficiency) is a rare autosomal recessive bleeding disorder caused by mutations in the prothrombin gene (*F2*), leading to impaired thrombin generation within the common coagulation pathway. There is a fundamental mechanistic gap: desmopressin releases vWF and FVIII but has no direct pathway to supplement prothrombin. The two conditions share the broad phenotypic category of "inherited bleeding disorder," which likely explains why the TxGNN knowledge graph assigns high connectivity between the two nodes.

One case report (PMID 2607619) describes DDAVP administration in combined Factor V + Factor VIII deficiency—not prothrombin deficiency—raising concern about disease classification misalignment within the knowledge graph. The TxGNN high prediction score most plausibly reflects generalized graph proximity among congenital hemostatic disorders rather than a pharmacologically specific relationship between desmopressin and Factor II deficiency.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04567511](https://clinicaltrials.gov/study/NCT04567511) | Phase 4 | Recruiting | 20 | Single-arm study evaluating emicizumab (a bispecific antibody bridging FIXa/FX) in mild hemophilia A males; assesses coagulation laboratory parameters, joint health, and quality of life. The study drug is emicizumab — **not desmopressin** — and the indication is mild hemophilia A, not congenital prothrombin deficiency. Relevance to this repurposing hypothesis is absent. |

> No clinical trials directly investigating desmopressin for congenital prothrombin deficiency were identified.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Narrative Review | *Drugs* | Rational treatment options for common inherited bleeding disorders; identifies desmopressin as preferred first-line therapy for mild hemophilia A and most von Willebrand disease subtypes based on safety, efficacy, and cost. No mention of prothrombin deficiency. |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case Report | *Rinsho Ketsueki* (Jpn. J. Clin. Hematol.) | DDAVP administration in a case of **combined Factor V + Factor VIII deficiency** (not prothrombin/Factor II deficiency); describes partial hemostatic improvement. This represents a disease classification mismatch with the predicted indication. |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case Report | *Rinsho Ketsueki* (Jpn. J. Clin. Hematol.) | Management of cesarean section under Factor VIII concentrate replacement therapy in a patient with combined FV + FVIII deficiency; does not involve prothrombin deficiency or desmopressin as primary intervention. |
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | *Autoimmunity Reviews* | Acquired hemophilia A: pathophysiology, aetiology, and management including FVIII inhibitors; discusses desmopressin's role in raising FVIII transiently. Only tangentially relevant; addresses acquired rather than congenital prothrombin deficiency. |

---

## Safety Considerations

**Drug Interactions (172 total interactions on record; representative key interactions below):**

| Severity | Interacting Drugs |
|----------|-------------------|
| **Major** | Hydrocortisone, Dexamethasone, Prednisolone, Prednisone, Beclomethasone dipropionate, Betamethasone, Budesonide, Triamcinolone |
| **Moderate** | Epinephrine, Loperamide, Morphine, Morphine (liposomal), Opium, Chlorpropamide |
| **Minor** | Acetylsalicylic acid |

Major interactions are predominantly with corticosteroids. Concurrent use of desmopressin with systemic corticosteroids may increase the risk of water retention and severe hyponatremia. Close monitoring of serum sodium is mandatory when these combinations cannot be avoided.

Please refer to the package insert for complete warnings and contraindications (full data not available in this evidence pack).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Desmopressin's established mechanism—releasing vWF and FVIII from endothelial stores—does not address the underlying coagulation defect in congenital prothrombin (Factor II) deficiency, which lies downstream in the common coagulation pathway. The high TxGNN prediction score (99.70%) most likely reflects broad knowledge graph connectivity among inherited bleeding disorders, and the available literature provides only indirect or misclassified evidence. There is no clinical or mechanistic basis sufficient to proceed with further evaluation at this time.

**To proceed, the following is needed:**
- Verification that the TxGNN knowledge graph correctly classifies "congenital prothrombin deficiency" as a node distinct from Factor V/VIII-related disorders; suspected misclassification should be corrected before re-scoring
- Retrieval of full MOA data from DrugBank (DG002) to formally exclude any secondary mechanism that could benefit Factor II deficiency
- A dedicated, targeted literature search using MeSH terms for "desmopressin" AND "prothrombin deficiency" / "Factor II deficiency" to confirm the absence of any relevant evidence
- Acquisition of full package insert safety data (DG001) — currently blocking entry into safety screening — particularly regarding hyponatremia risk and contraindications in coagulopathic patients
- Expert hematology consultation to assess whether any indirect hemostatic benefit (e.g., vWF-mediated platelet plug enhancement) could be clinically meaningful in severe prothrombin deficiency before any prospective investigation is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

