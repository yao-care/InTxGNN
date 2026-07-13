---
layout: default
title: Cefoperazone
parent: 僅模型預測 (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
---

# Cefoperazone
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

# Cefoperazone: From Bacterial Infections to Sclerosing Cholangitis

## One-Sentence Summary

Cefoperazone is a third-generation cephalosporin antibiotic with broad-spectrum antibacterial activity, established for treating serious bacterial infections including pneumonia, intra-abdominal infections, and septicemia — notably distinguished by its predominant biliary excretion (~70% excreted unchanged in bile).
The TxGNN model predicts it may be effective for **Sclerosing Cholangitis**, with **no clinical trials** and **no publications** currently supporting this specific direction.
Evidence is at the model-prediction level only (L5), and this candidate is currently recommended to **Hold** pending mechanistic validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no registrations in India) |
| Predicted New Indication | Sclerosing Cholangitis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Cefoperazone is a third-generation cephalosporin — a β-lactam antibiotic that inhibits bacterial cell wall (peptidoglycan) synthesis by covalently binding to penicillin-binding proteins (PBPs), ultimately triggering bacterial autolysis. It is clinically used both as monotherapy and in combination with the β-lactamase inhibitor sulbactam (Cefoperazone/Sulbactam) to extend coverage against β-lactamase-producing organisms, including multidrug-resistant Acinetobacter baumannii.

A distinctive pharmacokinetic feature of Cefoperazone is its predominant biliary excretion: approximately 70% of the drug is eliminated unchanged via bile, resulting in substantially higher concentrations in the biliary tract compared to plasma. This property provides a theoretical mechanistic rationale for potential activity in biliary conditions — the drug reaches the target tissue at levels far exceeding typical systemic antibiotics.

Sclerosing cholangitis — particularly primary sclerosing cholangitis (PSC) — involves immune dysregulation and gut microbiome perturbation. The gut-bile axis hypothesis proposes that intestinal bacteria may drive biliary inflammation and fibrosis, and antibiotic interventions have been explored in PSC (e.g., oral vancomycin in pediatric patients). Cefoperazone's high biliary concentration theoretically positions it as a candidate for modulating the biliary microbial environment. However, this mechanistic link remains entirely speculative: the TxGNN prediction most likely originates from knowledge graph (KG) associations between the biliary excretion pathway node and biliary tract disease nodes, rather than from validated pharmacological evidence. No clinical or preclinical data currently support this repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Cefoperazone is currently **not registered in India**. No product authorizations, brand names, or approved indications are available from the local regulatory database.

---

## Safety Considerations

**Drug Interactions** (14 moderate-level interactions identified via DDInter):

| Interacting Drug | Level | Clinical Relevance |
|-----------------|-------|-------------------|
| Warfarin | Moderate | Cephalosporins with the N-methylthiotetrazole (NMTT) side chain (present in Cefoperazone) may inhibit vitamin K–dependent clotting factor synthesis, potentiating anticoagulation |
| Heparin | Moderate | Additive bleeding risk; monitor coagulation parameters closely |
| Ethanol | Moderate | NMTT side chain causes disulfiram-like reaction (flushing, tachycardia, nausea) — avoid alcohol during and 5 days after treatment |
| Kanamycin / Amikacin / Amikacin (liposome) / Gentamicin / Neomycin / Streptomycin | Moderate | Concurrent aminoglycosides increase nephrotoxicity and ototoxicity risk; renal function monitoring required |
| Chloramphenicol | Moderate | Potential pharmacodynamic antagonism with β-lactam antibiotics |
| Ethinylestradiol | Moderate | Gut flora disruption may reduce enterohepatic recycling of estrogen; consider backup contraception |
| Mycophenolic acid | Moderate | Antibiotic-induced gut flora changes may reduce mycophenolate bioavailability; monitor immunosuppressant levels |
| Pemetrexed | Moderate | Cefoperazone may reduce renal clearance of pemetrexed, increasing toxicity risk |
| Picosulfuric acid | Moderate | Concurrent use may reduce bowel preparation efficacy |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a very high prediction score (99.98%) to sclerosing cholangitis, likely driven by Cefoperazone's unique biliary excretion pharmacokinetics creating a KG pathway association with biliary tract diseases — not by validated pharmacological or clinical evidence. No clinical trials or publications support this repurposing direction, and the evidence level is L5 (model prediction only). Furthermore, Cefoperazone is not registered in India, presenting an additional regulatory barrier.

**To proceed, the following is needed:**

- **MOA confirmation**: Query DrugBank API to obtain formal mechanism of action, pharmacodynamics, and pharmacokinetic data for Cefoperazone (DB01329)
- **Regulatory safety data**: Obtain package insert (SmPC or local equivalent) to establish key warnings and contraindications before any safety evaluation
- **Preclinical hypothesis testing**: Investigate whether Cefoperazone's biliary drug concentrations are sufficient to modulate biliary microbiota in PSC animal models (e.g., *Mdr2*-knockout mice)
- **Literature gap assessment**: Search specifically for Cefoperazone + gut microbiome, bile acid, or cholestasis interactions — the current query returned zero results but a broader mechanistic search may yield indirect evidence
- **Prioritize higher-evidence candidates**: The same Evidence Pack identifies **Pneumonia** (rank 3, L2 evidence, 2 clinical trials + 20 publications, "Proceed with Guardrails") and **Bronchitis** (rank 7, L3 evidence, 20 publications, "Proceed with Guardrails") as more immediately viable repurposing targets for Cefoperazone; these should be advanced in parallel
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

