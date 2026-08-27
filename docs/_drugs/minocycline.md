---
layout: default
title: Minocycline
parent: 僅模型預測 (L5)
nav_order: 448
evidence_level: L5
indication_count: 2
---

# Minocycline
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

# Minocycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Minocycline is a broad-spectrum second-generation tetracycline antibiotic, classically used to treat bacterial infections including acne vulgaris, respiratory tract infections, and sexually transmitted diseases.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis (PEK)**, yet **no direct clinical trials or published literature** currently support this specific indication — the prediction rests on mechanistic plausibility and knowledge graph topology, placing it at **Evidence Level L4**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (acne vulgaris, respiratory tract infections, STIs) |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 — Mechanistic / preclinical reasoning only |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Minocycline is a second-generation tetracycline with well-established antibacterial activity, but it also carries significant anti-inflammatory properties that extend well beyond its antibiotic function. It inhibits NF-κB signaling, downregulates pro-inflammatory cytokines (IL-1β, TNF-α), and suppresses matrix metalloproteinases MMP-2 and MMP-9. These mechanisms are directly relevant to ocular surface pathology: MMP-2/MMP-9 are key drivers of corneal basement membrane degradation, and chronic low-grade inflammation is the central feature of Punctate Epithelial Keratoconjunctivitis (PEK).

The pharmacological analogy to doxycycline — a structurally related tetracycline — lends indirect support. Doxycycline already has clinical precedent in treating Meibomian Gland Dysfunction (MGD), which is one of the principal upstream causes of PEK, through the same MMP-inhibition and anti-inflammatory pathway. If doxycycline can modify the inflammatory milieu responsible for PEK, minocycline — with comparable or superior tissue penetration and anti-inflammatory potency — may offer similar benefit.

The TxGNN model's high prediction score (0.9963) reflects meaningful connectivity between minocycline-related nodes and corneal epithelial disease nodes in the knowledge graph. However, this remains an inference: no dedicated clinical trials or publications directly testing minocycline in PEK were identified. The mechanistic case is plausible but unconfirmed, and formal preclinical validation is the necessary next step before any clinical translation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions** — 272 total interactions identified. Key interactions requiring clinical attention are summarised below.

**Major interactions (avoid concurrent use):**

| Interacting Drug | Severity | Clinical Significance |
|------------------|----------|-----------------------|
| Isotretinoin | **Major** | Concurrent use significantly increases risk of pseudotumour cerebri (benign intracranial hypertension); combination should be avoided |
| Acitretin | **Major** | Same mechanism — retinoids combined with tetracyclines carry established risk of raised intracranial pressure |

**Notable moderate interactions:**

| Interacting Drug | Severity | Notes |
|------------------|----------|-------|
| Ethinylestradiol | Moderate | Potential reduction of oral contraceptive efficacy; additional contraception advised |
| Amoxicillin / Ampicillin | Moderate | Pharmacodynamic antagonism between bacteriostatic (minocycline) and bactericidal (penicillins) agents |
| Calcium Phosphate / Calcium acetate | Moderate | Chelation in the gut reduces minocycline oral bioavailability; separate dosing by ≥2 hours |
| Aminolevulinic acid (topical) | Moderate | Additive photosensitivity risk |
| Cannabidiol | Moderate | Monitor for overlapping adverse effects |
| Brentuximab vedotin | Moderate | Monitor closely; mechanism not fully characterised |

> A total of **272 drug interactions** have been catalogued. A thorough medication reconciliation is essential before initiating minocycline in any patient, particularly those on retinoids, oral contraceptives, or calcium-containing preparations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.63%) to minocycline for punctate epithelial keratoconjunctivitis, and the mechanistic rationale — MMP-2/MMP-9 inhibition combined with NF-κB-mediated anti-inflammatory activity, supported by cross-class analogy with doxycycline in MGD — is scientifically coherent. However, the complete absence of direct clinical trials or published literature (Evidence Level L4) means this remains a hypothesis. The drug is also not currently registered in India, adding a regulatory pathway requirement.

**To proceed, the following is needed:**
- Preclinical studies (in vitro corneal epithelial cell models and/or animal PEK models) to confirm minocycline's direct activity on the target pathology
- Targeted literature review for indirect evidence — doxycycline clinical data in MGD/PEK, or any minocycline ocular surface case reports — that may upgrade the evidence level
- Determination of the appropriate delivery route (topical ophthalmic formulation vs. low-dose systemic oral), given that ocular bioavailability and corneal penetration are route-dependent
- Retrieval of full MOA data from DrugBank (Data Gap DG002) to substantiate the mechanistic linkage for regulatory dossiers
- Full safety package including prescribing information warnings and contraindications (Data Gap DG001), which are currently unavailable
- CDSCO regulatory pathway assessment: a new drug or new indication application will be required given zero existing registrations in India
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

