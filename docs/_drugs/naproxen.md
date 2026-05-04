---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 376
evidence_level: L5
indication_count: 4
---

# Naproxen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Naproxen: From Pain & Inflammation to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Naproxen is a well-established non-steroidal anti-inflammatory drug (NSAID) widely used for pain relief, fever, and inflammatory conditions such as arthritis.
The TxGNN model predicts it may be effective for **Brachydactyly-Syndactyly Syndrome**, a rare congenital skeletal malformation disorder.
Currently, **no clinical trials** and **no supporting publications** exist for this combination, leaving the prediction at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain, inflammation, and fever (NSAID; analgesic/antipyretic use) |
| Predicted New Indication | Brachydactyly-Syndactyly Syndrome |
| TxGNN Prediction Score | 99.35% |
| Evidence Level | L5 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Naproxen in this context. Based on known pharmacological information, Naproxen is a propionic acid-class NSAID that inhibits cyclooxygenase (COX-1 and COX-2) enzymes, thereby suppressing the synthesis of prostaglandins — most notably prostaglandin E2 (PGE2). This action underlies its well-established analgesic, antipyretic, and anti-inflammatory effects.

The connection to brachydactyly-syndactyly syndrome is mechanistically indirect. PGE2 is known to play a modulatory role in skeletal development, including regulation of bone morphogenetic protein (BMP) signalling and osteoblast/chondrocyte activity during embryogenesis. Brachydactyly-syndactyly syndrome, however, is a congenital structural defect caused by mutations in RAS-MAPK and related developmental signalling pathways, resulting in permanent anatomical abnormalities of the digits and limbs that are established during embryonic development.

Suppression of PGE2 via COX inhibition cannot reverse pre-existing congenital skeletal malformations. The high TxGNN score (0.9935) most likely reflects high topological connectivity of skeletal-related nodes in the knowledge graph rather than a direct pharmacological rationale. There is no mechanistic pathway by which post-natal NSAID therapy could modify the structural phenotype of this syndrome.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

Naproxen currently has **no registered products** in the Indian market (CDSCO licensing data). No authorization records are available for this drug under the dataset reviewed.

---

## Safety Considerations

**Drug Interactions (309 interactions on record):** The following are representative moderate-severity interactions identified in the DDInter database:

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Acetylsalicylic acid | Moderate | Concurrent NSAID use increases GI bleeding risk and may reduce aspirin's antiplatelet efficacy |
| Dexamethasone / Hydrocortisone / Betamethasone / Budesonide / Triamcinolone | Moderate | Combined NSAID + corticosteroid use significantly elevates risk of GI ulceration and haemorrhage |
| Metformin | Moderate | NSAIDs may reduce renal clearance of metformin, increasing metformin plasma levels |
| Famotidine / Ranitidine / Cimetidine / Rabeprazole / Dexlansoprazole | Moderate | GI protectants co-prescribed to mitigate NSAID-associated gastropathy; pharmacokinetic interactions possible |
| Mesalazine / Balsalazide | Moderate | Concurrent use with NSAIDs may exacerbate inflammatory bowel disease |
| Chlorpropamide | Moderate | NSAIDs may potentiate hypoglycaemic effects of sulfonylureas |
| Aprepitant | Moderate | Potential CYP-mediated interaction affecting naproxen metabolism |
| Picosulfuric acid / Polyethylene glycol (3350 with electrolytes) / Potassium citrate / Potassium bicarbonate | Moderate | Electrolyte balance and renal handling may be affected |

> Warnings and contraindications data from the regulatory package insert were not available in this dataset. Please refer to the approved product labelling for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Brachydactyly-syndactyly syndrome is an irreversible congenital skeletal malformation caused by germline mutations in developmental signalling pathways. There is no pharmacological mechanism by which Naproxen's COX inhibition could modify the structural phenotype, and the complete absence of clinical trial or literature evidence confirms this prediction is not actionable at this time. The TxGNN high score reflects knowledge-graph topology rather than biological plausibility.

**To proceed, the following would be needed:**
- **Mechanistic validation:** Preclinical evidence (cell or animal model) demonstrating that COX/PGE2 inhibition meaningfully modulates the specific genetic defect(s) underlying brachydactyly-syndactyly syndrome
- **MOA clarification:** Full DrugBank MOA data for Naproxen should be retrieved to rule out any secondary targets relevant to congenital skeletal disorders
- **Regulatory safety data:** CDSCO / TFDA package insert warnings and contraindications (DG001) must be retrieved before any safety-based evaluation can proceed
- **India market registration:** If clinical repurposing research is considered, a regulatory pathway for India market entry would need to be defined from scratch given zero current registrations
- **Rare disease context:** Given the ultra-rare nature of brachydactyly-syndactyly syndrome, any future study design would require patient registry identification and orphan drug designation assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

