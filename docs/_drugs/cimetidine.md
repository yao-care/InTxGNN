---
layout: default
title: Cimetidine
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 9
---

# Cimetidine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Cimetidine: From Peptic Ulcer Disease to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Cimetidine is the first-generation histamine H2 receptor antagonist, originally developed and widely used for peptic ulcer disease and gastric acid hypersecretion conditions.
The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis (SSM)**, based on its capacity to block H2 receptors and relieve histamine-mediated gastrointestinal symptoms that are characteristic of mast cell disorders.
Currently, there are **no dedicated clinical trials** and **no directly relevant publications** for this specific indication, placing the evidence at Level **L4** (mechanistic rationale without direct clinical data).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Peptic ulcer disease and gastric acid hypersecretion (well-established pharmacological use; no India regulatory record available) |
| Predicted New Indication | Smouldering Systemic Mastocytosis |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| India Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data is not currently available from the DrugBank record for this analysis. Based on established pharmacology, Cimetidine is a competitive antagonist at histamine H2 receptors located primarily on gastric parietal cells. By blocking these receptors, it suppresses cyclic AMP-mediated acid secretion, promoting mucosal healing in peptic ulcer disease. At higher doses (1.2–1.6 g/day), Cimetidine also demonstrates weak anti-androgenic activity through competitive androgen receptor blockade — a property relevant to some of its off-label applications such as acne.

Smouldering Systemic Mastocytosis is defined by high clonal mast cell burden in the bone marrow without overt organ damage. A defining pathophysiological feature across all systemic mastocytosis variants is uncontrolled histamine release from neoplastic mast cells. In the gastrointestinal tract, this excess histamine drives acid hypersecretion, peptic ulceration, abdominal cramping, and diarrhoea — effects mediated specifically through H2 receptors on parietal cells. This mechanistic link forms the biological basis for the TxGNN prediction.

Current clinical practice guidelines for systemic mastocytosis recommend combining H1 and H2 receptor antagonists as the first-line approach to symptomatic management. Cimetidine directly addresses the H2-mediated component of histamine excess. However, it is critical to understand that H2 blockade provides symptomatic relief only and exerts no effect on the underlying clonal mast cell proliferation. For SSM — a high-burden subtype that may require disease-modifying therapy — Cimetidine's role is strictly adjunctive, not curative.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Smouldering Systemic Mastocytosis.

---

## Literature Evidence

Currently no related literature directly investigating Cimetidine in Smouldering Systemic Mastocytosis is available.

---

## India Market Information

Cimetidine currently holds no product registrations in India and is not marketed. No authorisation records were identified in the India regulatory database.

---

## Safety Considerations

**Drug Interactions**: Cimetidine carries an exceptionally high drug interaction burden, with **551 documented interactions**. This is primarily driven by its broad inhibition of hepatic CYP450 enzymes (CYP1A2, CYP2C9, CYP2C19, CYP2D6, CYP3A4), which can elevate plasma concentrations of co-administered drugs. Representative interactions include:

| Severity | Interacting Drug | Clinical Note |
|----------|-----------------|---------------|
| Moderate | Paclitaxel | CYP3A4 inhibition may increase taxane exposure |
| Moderate | Acalabrutinib | Requires gastric acid for absorption; H2 blockade reduces bioavailability |
| Moderate | Fentanyl | Increased opioid plasma levels via CYP3A4 inhibition |
| Moderate | Alfentanil | Increased opioid exposure |
| Moderate | Nifedipine | Elevated nifedipine levels; monitor blood pressure |
| Moderate | Lidocaine | Reduced lidocaine clearance |
| Moderate | Tramadol | Enhanced opioid effect |
| Moderate | Codeine | Enhanced opioid effect via CYP2D6 inhibition |
| Moderate | Dihydrocodeine | Enhanced opioid effect |
| Moderate | Acebutolol | Altered beta-blocker pharmacokinetics |
| Minor | Dolutegravir | Minor pharmacokinetic interaction |
| Minor | Zidovudine | Minor interaction |
| Minor | Acetaminophen | Minor interaction |

> The 551-interaction burden is of particular concern in SSM patients, who frequently require multiple concurrent medications including cytoreductive agents (e.g., Midostaurin, Avapritinib) and combination antihistamine therapy. Cimetidine's CYP450 inhibition profile may meaningfully alter the pharmacokinetics of these agents. A comprehensive drug interaction review is mandatory before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials or publications directly support the use of Cimetidine in Smouldering Systemic Mastocytosis. While the mechanistic reasoning — H2 blockade to manage histamine-driven gastrointestinal symptoms in mast cell disease — is biologically sound and consistent with guideline recommendations, the absence of direct clinical evidence and the drug's substantial interaction profile preclude advancement beyond the research hypothesis stage.

**To proceed, the following is needed:**
- Prospective clinical studies or systematic evidence specifically evaluating H2 receptor antagonist therapy in SSM patients
- Formal MOA documentation retrieved from the DrugBank API (currently a data gap)
- Dedicated drug interaction assessment for SSM-specific concurrent medications, particularly Midostaurin and Avapritinib, which are CYP3A4 substrates susceptible to Cimetidine inhibition
- A pharmacovigilance plan addressing polypharmacy risk given the 551-interaction burden in the typical SSM patient population
- India regulatory pathway assessment, as Cimetidine has no current market authorisation in India and a new drug application or import licence would be required prior to any clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

