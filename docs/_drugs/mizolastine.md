---
layout: default
title: Mizolastine
parent: 僅模型預測 (L5)
nav_order: 429
evidence_level: L5
indication_count: 10
---

# Mizolastine
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

# Mizolastine: From Allergic Conditions to Acute Intermittent Porphyria

## One-Sentence Summary

Mizolastine is a second-generation selective H₁ receptor antagonist, commercially available as an antiallergy medication in multiple countries outside the US (marketed as Mizollen®).
The TxGNN model predicts it may be effective for **Acute Intermittent Porphyria** with a prediction score of **99.76%**,
however **no clinical trials and no supporting publications** have been identified for this indication, placing this prediction at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic conditions (antiallergy / antihistamine) |
| Predicted New Indication | Acute Intermittent Porphyria |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Mizolastine (MKC-431 / SL-850324) is a selective H₁ receptor antagonist targeting the histamine H₁ receptor encoded by the *HRH1* gene (Entrez: 3269, ENSEMBL: ENSG00000196639). Unlike first-generation antihistamines, Mizolastine is a second-generation agent with low central nervous system penetration, meaning its primary pharmacological activity is peripheral H₁ blockade. It is available internationally (e.g., Mizollen®) but has not received US FDA approval.

Acute Intermittent Porphyria (AIP) is a metabolic disorder caused by a deficiency in hydroxymethylbilane synthase (porphobilinogen deaminase), leading to accumulation of δ-aminolevulinic acid (ALA) and porphobilinogen. The theoretical mechanistic link to Mizolastine is extremely tenuous: histamine has been proposed to indirectly modulate neurological regulation of ALA synthase activity, and H₁ receptor blockade might theoretically influence this pathway. However, this connection has no published experimental or clinical basis.

Critically, there is an important **safety concern** that actually works *against* this repurposing hypothesis: several antihistamine-class drugs have been reported to trigger or exacerbate acute porphyria attacks. This means the risk-benefit ratio for this specific indication may be unfavorable without considerably more mechanistic evidence. The TxGNN prediction likely arises from network topology proximity in the knowledge graph rather than a pharmacologically sound mechanistic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Mizolastine is currently **not marketed in India**. No drug licenses or regulatory approvals are on record.

---

## Safety Considerations

- **Pharmacological Target**: Mizolastine acts as a selective antagonist at the human H₁ receptor (HRH1 gene). Its clinical use is as an antiallergy agent; it is not approved in the US.
- **Key Safety Concern for This Indication**: Multiple antihistamine agents are classified as **potentially porphyrinogenic** — i.e., capable of precipitating acute attacks in patients with AIP. This is a critical contraindication consideration that must be investigated before any repurposing evaluation proceeds.

For full prescribing warnings, contraindications, and drug interaction data, please refer to the approved package insert (e.g., Mizollen® SmPC).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is currently supported only by TxGNN model output (L5 evidence) with zero clinical trials, zero literature, and a mechanistic link that is speculative at best and potentially hazardous — antihistamines as a class carry a known risk of inducing acute porphyria attacks, making Mizolastine a particularly questionable candidate for AIP repurposing without substantially more investigation.

**To proceed, the following is needed:**

- **Safety clearance**: Conduct a formal porphyrinogenicity assessment for Mizolastine specifically (in vitro ALA induction assay; review of case reports for antihistamine-triggered AIP attacks)
- **Mechanistic validation**: Obtain and review the complete MOA profile from DrugBank (DG002 data gap), including any known off-target activities beyond H₁ antagonism
- **Regulatory package insert review**: Retrieve TFDA or EMA/MHRA package inserts for full contraindications and warnings (DG001 data gap)
- **India regulatory pathway**: As Mizolastine is not marketed in India, a full regulatory strategy (new drug application) would be required before any clinical development
- **Expert consultation**: Engage a metabolism/rare disease specialist to evaluate whether any H₁-independent mechanisms (e.g., mast cell stabilisation, anti-inflammatory effects) could plausibly address AIP pathophysiology
- If safety data clears, consider a **preclinical AIP animal model study** before any human investigation

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

