---
layout: default
title: Carbenicillin
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 7
---

# Carbenicillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Carbenicillin: From Gram-Negative Bacterial Infections to Ureaplasma Urethritis

## One-Sentence Summary

Carbenicillin is a broad-spectrum, extended-spectrum penicillin (β-lactam class) antibiotic historically used against gram-negative bacterial infections, including *Pseudomonas aeruginosa* and urinary tract pathogens.
The TxGNN model predicts it may be effective for **Ureaplasma Urethritis**;
however, **0 clinical trials** and **0 publications** support this direction, and the prediction is mechanistically implausible — *Ureaplasma* completely lacks a cell wall, making it intrinsically resistant to all β-lactam antibiotics.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gram-negative bacterial infections (historical; no India regulatory records found) |
| Predicted New Indication | Ureaplasma Urethritis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Carbenicillin is a broad-spectrum extended-spectrum penicillin that inhibits bacterial cell wall synthesis by binding to Penicillin-Binding Proteins (PBPs) — particularly PBP2 — disrupting peptidoglycan cross-linking and leading to osmotic lysis. Historically, it demonstrated activity against *Pseudomonas aeruginosa*, *Escherichia coli*, *Proteus* species, and other aerobic gram-negative organisms.

**This prediction is, however, mechanistically untenable.** *Ureaplasma urealyticum* belongs to the class Mollicutes and completely lacks a cell wall — there is no peptidoglycan layer and no PBPs present. This constitutes absolute, intrinsic resistance to every β-lactam antibiotic, including Carbenicillin. No dose optimization or formulation change can overcome this biological structural reality; the drug's target simply does not exist in this pathogen.

The high TxGNN score (99.98%) most likely reflects disease-node similarity within the knowledge graph: both Ureaplasma urethritis and Carbenicillin's established indications cluster within the "urogenital infection" disease space. This is a graph topology artifact — a proximity signal — rather than a genuine antibacterial activity prediction. This result should be treated as a **false positive** and does not warrant clinical development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

**Drug Interactions** — 18 interactions identified (DDInter database):

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Methotrexate | **Major** | Penicillins compete with methotrexate for renal tubular secretion, potentially causing methotrexate toxicity (myelosuppression, mucositis) |
| Warfarin | Moderate | Broad-spectrum antibiotics alter gut flora, reducing Vitamin K synthesis and potentially enhancing anticoagulant effect |
| Dicoumarol | Moderate | Same mechanism as Warfarin interaction |
| Pemetrexed | Moderate | Reduced renal clearance may increase Pemetrexed plasma exposure |
| Mycophenolic acid | Moderate | Antibiotics may disrupt enterohepatic recirculation, reducing immunosuppressant efficacy |
| Ethinylestradiol | Moderate | Broad-spectrum antibiotics may reduce oral contraceptive efficacy via gut flora disruption |
| Doxycycline | Moderate | Bacteriostatic tetracyclines may antagonize the bactericidal activity of penicillins |
| Tetracycline | Moderate | Bacteriostatic antagonism |
| Minocycline | Moderate | Bacteriostatic antagonism |
| Demeclocycline | Moderate | Bacteriostatic antagonism |
| Oxytetracycline | Moderate | Bacteriostatic antagonism |
| Chloramphenicol | Moderate | Bacteriostatic antagonism of penicillin activity |
| Balsalazide | Moderate | Antibiotic-mediated gut flora changes may alter balsalazide conversion |
| Picosulfuric acid | Moderate | Antibiotics may interfere with bowel preparation activation |
| Iodide I-131 | Moderate | Antibiotic-class interaction |
| Iodide I-123 | Moderate | Antibiotic-class interaction |
| Clarithromycin | Minor | Possible pharmacodynamic interaction |
| Erythromycin | Minor | Possible pharmacodynamic interaction |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
*Ureaplasma urealyticum* is a naturally cell-wall-deficient organism for which all β-lactam antibiotics are fundamentally inactive by mechanism. The TxGNN score of 99.98% reflects urogenital disease-node clustering in the knowledge graph rather than any real biological activity, and there is zero supporting clinical or preclinical evidence. Pursuing this indication would be scientifically unsound.

**Note on Other Predicted Indications:**
Across the full set of 7 TxGNN predictions for Carbenicillin, the only indication with meaningful clinical evidence is **Gonococcal Urethritis (Rank 2, L3)** — 4 historical publications (1972–2001) directly document Carbenicillin's use against *Neisseria gonorrhoeae* via PBP2 inhibition. However, this also faces major barriers: modern *N. gonorrhoeae* is predominantly penicillin-resistant (PPNG strains), WHO no longer recommends penicillin-class antibiotics for gonorrhea, and Carbenicillin has been withdrawn from most markets. The remaining 5 predicted indications (uterine inflammatory disease, xanthogranulomatous pyelonephritis, urogenital tuberculosis, epiglottitis, laryngitis) are all rated L4–L5 with Hold recommendations, ranging from incomplete coverage to mechanistic impossibility (TB).

**To proceed, the following is needed:**
- Mechanistic justification review: confirm whether any predicted indication has a valid β-lactam–sensitive pathogen as primary etiology
- For gonococcal urethritis specifically: obtain current PPNG prevalence data in the target population to assess residual susceptibility
- Obtain the TFDA/CDSCO package insert (or equivalent historical labeling) to fill the Blocking data gap on warnings and contraindications before any safety evaluation
- Regulatory pathway assessment for a drug that has been withdrawn from most major markets
- Evaluate whether updated formulations (e.g., oral Carbenicillin indanyl sodium) could be sourced or reformulated if any indication proceeds
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

