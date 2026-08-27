---
layout: default
title: Imipenem
parent: 僅模型預測 (L5)
nav_order: 326
evidence_level: L5
indication_count: 10
---

# Imipenem
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

# Imipenem: From Serious Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Imipenem is a broad-spectrum carbapenem antibiotic used as a last-resort treatment for serious hospital-acquired bacterial infections, including those caused by multidrug-resistant organisms.
The TxGNN model's top-ranked prediction is **Diffuse Scleroderma** (systemic sclerosis),
however, **no clinical trials** and **no publications** currently support this direction — the evidence base is entirely model-derived, making this an L5 prediction.

> **Note:** Among all 10 ranked predictions, the most clinically actionable indication is **Staphylococcus aureus infection** (Rank 9, L2, Proceed with Guardrails), backed by a Phase 4 RCT and substantial literature. The sections below follow the format specification and report on the top-ranked prediction first.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious bacterial infections (carbapenem antibiotic, hospital-acquired) |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Imipenem is a carbapenem beta-lactam antibiotic whose efficacy against serious bacterial infections is well established. Carbapenems work by binding to penicillin-binding proteins (PBPs) in bacterial cell walls, inhibiting cell wall synthesis and causing bacterial death. This mechanism has no recognized direct relevance to autoimmune or fibrotic disease pathways.

Diffuse scleroderma is an autoimmune fibrotic disease driven by immune dysregulation, vascular injury, and progressive fibrosis of the skin and internal organs. It is not caused by bacteria and does not respond to cell wall synthesis inhibitors by any established mechanism.

According to this Evidence Pack's repurposing rationale, the elevated TxGNN score for this pairing most likely originates from indirect edges in the knowledge graph — specifically, shared comorbidity nodes representing infectious complications that arise in immunocompromised scleroderma patients. In other words, the model learned that Imipenem and scleroderma co-occur in clinical contexts (infection management in immunosuppressed patients), not that Imipenem treats scleroderma directly. This is likely a false positive.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Imipenem in diffuse scleroderma.

---

## Literature Evidence

Currently no related literature available for Imipenem in diffuse scleroderma.

---

## India Market Information

Imipenem is not currently registered in India. No licensed products are on record in the Indian regulatory database (total registrations: 0).

---

## Safety Considerations

**Drug Interactions** (15 interactions identified; source: DDInter):

**Major interactions — require clinical attention before co-prescribing:**

| Interacting Drug | Severity | Clinical Concern |
|-----------------|----------|-----------------|
| Bupropion | Major | Imipenem lowers seizure threshold; combination significantly increases seizure risk |
| Iohexol | Major | Iodinated contrast agent; risk of seizure or neurotoxicity in combination |
| Iopamidol | Major | Iodinated contrast agent; same concern as Iohexol |

**Moderate interactions — monitor if co-prescribed:**

| Interacting Drug | Clinical Concern |
|-----------------|-----------------|
| Theophylline / Aminophylline / Dyphylline / Oxtriphylline | Xanthine derivatives; imipenem may reduce theophylline clearance, increasing seizure and toxicity risk |
| Warfarin / Dicoumarol | Anticoagulant effect may be potentiated; INR monitoring required |
| Cyclosporine | CNS toxicity (tremor, seizure) may be enhanced |
| Mycophenolic acid | Imipenem/cilastatin may reduce mycophenolate plasma levels by ~30–50%, risking transplant rejection |
| Pemetrexed | Imipenem may delay pemetrexed renal clearance, increasing pemetrexed toxicity |
| Ethinylestradiol | Antibiotic-related reduction of hormonal contraceptive efficacy |
| Polyethylene glycol (3350 with electrolytes) | Moderate interaction |
| Lindane | Moderate interaction; both lower seizure threshold |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or preclinical evidence supporting the use of Imipenem in diffuse scleroderma. The high TxGNN score almost certainly reflects indirect knowledge graph co-occurrence (infection management in immunocompromised patients) rather than a genuine anti-fibrotic or immunomodulatory mechanism. A carbapenem antibiotic targeting bacterial PBPs has no established basis for treating an autoimmune fibrotic disease, and antimicrobial stewardship principles strongly discourage use outside of infectious indications.

**To proceed from L5 toward any investigable hypothesis, the following would be needed:**
- A plausible mechanistic hypothesis linking carbapenem activity to scleroderma pathogenesis (e.g., microbiome modulation, anti-fibrotic signaling — currently speculative)
- Preclinical data (in vitro fibroblast/immune cell models or animal model) showing relevant biological activity
- If a microbiome-mediated hypothesis is proposed, 16S rRNA or metagenomic evidence linking specific microbial dysbiosis to scleroderma progression

---

> **Actionable alternative:** If this report is being used to prioritize Imipenem repurposing opportunities, **Staphylococcus aureus infection** (Rank 9) represents the most evidence-supported direction — with 1 completed Phase 4 RCT ([NCT00871104](https://clinicaltrials.gov/study/NCT00871104): fosfomycin + imipenem for MRSA endocarditis), 13 clinical trials, and 20 publications, yielding an L2 rating and a "Proceed with Guardrails" recommendation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

