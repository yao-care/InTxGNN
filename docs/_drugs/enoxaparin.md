---
layout: default
title: Enoxaparin
parent: 僅模型預測 (L5)
nav_order: 282
evidence_level: L5
indication_count: 1
---

# Enoxaparin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Enoxaparin: From Venous Thromboembolism to Thrombophilia due to Protein C Deficiency (Autosomal Recessive)

## One-Sentence Summary

Enoxaparin is a low molecular weight heparin (LMWH) widely used for the prevention and treatment of venous thromboembolism (VTE) and acute coronary syndromes.
The TxGNN model predicts it may be effective for **Thrombophilia due to Protein C Deficiency, Autosomal Recessive**,
with **no registered clinical trials** and **no published literature** currently available for this specific indication. The mechanistic rationale, however, is strong and well-recognised by hematology guidelines.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Venous thromboembolism (DVT/PE) prevention and treatment; acute coronary syndromes |
| Predicted New Indication | Thrombophilia due to Protein C Deficiency, Autosomal Recessive |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Enoxaparin is a low molecular weight heparin that exerts its anticoagulant effect by binding to and activating **Antithrombin III (AT-III)**, which in turn strongly inhibits **Factor Xa** (anti-Xa activity) and, to a lesser extent, **Thrombin (Factor IIa)**. Although detailed MOA data was not retrieved from DrugBank in this evidence pack, Enoxaparin's pharmacology is extensively characterised in the literature: its anti-Xa to anti-IIa ratio of approximately 3.8:1 distinguishes it from unfractionated heparin and confers more predictable anticoagulant kinetics.

**Autosomal recessive Protein C deficiency** creates a profoundly hypercoagulable state. Protein C, once activated by thrombin bound to thrombomodulin, normally cleaves and inactivates **Factor Va and Factor VIIIa**, the two critical co-factors that amplify thrombin generation. Without Protein C, this brake is absent, resulting in unchecked thrombin formation and a high risk of life-threatening thrombosis in infancy. The complementary pathway is direct:

> Protein C deficiency → ↑ Factor Va / VIIIa → ↑ Thrombin generation → Thrombosis
> ← **[Enoxaparin intervenes via anti-Xa / anti-IIa inhibition]**

By blocking Factor Xa upstream and suppressing Thrombin directly, Enoxaparin compensates for the lost Protein C anticoagulant activity at the downstream effector level. This mechanistic rationale is recognised in ISTH and ASH guidelines for the management of hereditary thrombophilia, where LMWH is used as a bridge or long-term maintenance therapy. It is important to note that Enoxaparin **does not restore Protein C function itself**; in severe homozygous neonates, Protein C Concentrate (PCC) or fresh frozen plasma (FFP) remains the primary intervention, with LMWH serving an adjunctive and prophylactic role.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Enoxaparin in thrombophilia due to Protein C deficiency, autosomal recessive.

---

## Literature Evidence

Currently no related literature available for this specific indication.

---

## India Market Information

Enoxaparin is currently **not marketed in India**. No registered product licences were found in the regulatory database at the time of this report (data cut-off: 2026-04-04).

---

## Safety Considerations

**Drug Interactions:** Enoxaparin has **174 known drug interactions** in the DDInter database. The following major and selected moderate interactions are clinically most relevant:

| Interacting Drug | Severity | Clinical Note |
|-----------------|----------|---------------|
| Acetylsalicylic acid (Aspirin) | Major | Combined antiplatelet + anticoagulant; significantly elevated bleeding risk |
| Abciximab | Major | GP IIb/IIIa inhibitor; additive haemorrhagic risk |
| Alteplase | Major | Thrombolytic agent; concurrent use markedly increases bleeding |
| Ibuprofen | Major | NSAID-mediated platelet inhibition + GI bleeding risk |
| Ketorolac | Major | High-risk NSAID; combination generally contraindicated |
| Acalabrutinib | Major | BTK inhibitor; additive bleeding risk, especially intracranial |
| Deferasirox | Major | Iron chelator; increased bleeding and GI adverse events |
| Ibritumomab tiuxetan | Major | Radioimmunotherapy; myelosuppression compounds bleeding risk |
| Tositumomab (I-131) | Major | Radioimmunotherapy; additive haemorrhagic risk |
| Trastuzumab emtansine | Major | ADC with thrombocytopenia risk; additive with anticoagulants |
| Dexfenfluramine | Moderate | Serotonergic agents may mildly alter platelet function |
| Sugammadex | Moderate | Theoretical displacement of heparin from plasma proteins |
| Iodide I-131 / I-123 | Moderate | Monitor for altered biodistribution |
| Aliskiren | Moderate | Additive hypotensive / renal effects in high-risk patients |
| Diclofenac (topical) | Moderate | Low systemic absorption, but monitor in high-dose application |

> **Note:** Formal warnings and contraindications (e.g., active major bleeding, heparin-induced thrombocytopenia history) could not be retrieved from the package insert in this evidence pack. Please refer to the official prescribing information for the complete safety profile.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between Enoxaparin and autosomal recessive Protein C deficiency thrombophilia is pharmacologically sound and complementary—Enoxaparin's downstream inhibition of Factor Xa and Thrombin directly compensates for the absent Protein C anticoagulant brake. However, no clinical trials or indexed publications were identified for this precise indication, placing current evidence at **L4 (mechanistic/preclinical reasoning only)**. Off-label use of LMWH in hereditary thrombophilia is guideline-acknowledged but not systematically studied under this rare disease classification.

**To proceed, the following is needed:**

- **Broader literature search:** Re-query PubMed/EMBASE using broader terms (e.g., "LMWH + Protein C deficiency", "hereditary thrombophilia + enoxaparin") to capture evidence not indexed under the OMIM/ORDO disease name
- **Guideline review:** Retrieve ISTH, ASH, and EHA guidelines on anticoagulation in Protein C deficiency to document current standard-of-care role of LMWH
- **Package insert retrieval:** Download and parse Enoxaparin's official prescribing information (FDA/EMA label) to fill the critical DG001 safety gap (warnings, contraindications)
- **MOA documentation:** Query DrugBank API (DB01225) to formally document mechanism of action and fill DG002
- **Comparator assessment:** Evaluate availability of Protein C Concentrate in the target market, as this determines whether Enoxaparin would serve as a primary or bridging therapy
- **Rare disease registry check:** Search EURODIS, Orphanet, and national rare disease registries for case series or real-world data on anticoagulation strategies in this population
- **India registration pathway:** As Enoxaparin is not currently marketed in India, assess regulatory pathway (new drug application or orphan designation) before any clinical development can be initiated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

