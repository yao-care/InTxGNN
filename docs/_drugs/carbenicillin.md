---
layout: default
title: Carbenicillin
parent: Model Prediction Only (L5)
nav_order: 143
evidence_level: L5
indication_count: 7
monitor_inn: "Carbenicillin"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "urogenital tuberculosis", "epiglottitis", "laryngitis"]
last_modified_at: 2026-10-30
description: "Carbenicillin: predicted new indication Ureaplasma urethritis (evidence level L5). Approved use: Not recorded in the local data"
---

# Carbenicillin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Carbenicillin: Extended-spectrum penicillin (beta-lactam) → Ureaplasma urethritis
{: .text-alpha }

## One-Sentence Summary

Carbenicillin is an extended-spectrum penicillin that blocks bacterial cell wall synthesis.
The TxGNN model predicts it may be effective for **Ureaplasma urethritis**, with a score of 0.9998, but **no clinical trials and no publications** support this prediction.
The mechanism is also doubtful, because Ureaplasma bacteria have no cell wall for a beta-lactam to attack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (2 of 2) – CDSCO approval status is not included in this data |
| Number of Listed Products | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Based on its drug class, carbenicillin is a beta-lactam that inhibits bacterial cell wall synthesis, and it has activity against many urinary-tract bacteria.

For Ureaplasma urethritis, however, this mechanism does not fit. Ureaplasma species lack a cell wall, so beta-lactams are expected to be intrinsically ineffective. The high TxGNN score most likely reflects the drug's general association with urogenital infections rather than a real pharmacological link. The prediction should therefore be treated as a weak, unsupported signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 50906 | CARBELIN 5GM INJECTION | Vial of 1 injection | Not recorded |
| 42088 | CARBELIN 1GM INJECTION | Vial of 1 injection | Not recorded |

Both licences are valid single-ingredient products from Lyka Labs.

---

## Safety Considerations

- **Drug Interactions**: 18 interactions were found. The most important is **methotrexate (Major)**. Moderate interactions include warfarin, dicoumarol, tetracyclines (doxycycline, minocycline, tetracycline, demeclocycline, oxytetracycline), chloramphenicol, ethinylestradiol, mycophenolic acid, pemetrexed, balsalazide, picosulfuric acid and radioactive iodide (I-123, I-131). Clarithromycin and erythromycin are Minor.

For other safety information, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- There is no clinical or published evidence for Ureaplasma urethritis, and the lack of a bacterial cell wall in Ureaplasma argues against any benefit from a beta-lactam. The prediction is supported by the model score alone.

**To proceed, the following is needed:**
- Laboratory data showing carbenicillin activity against Ureaplasma, which is unlikely given the mechanism
- Detailed mechanism-of-action data
- Package insert warnings and contraindications
- A comparison against current standard treatments for Ureaplasma infection, which use agents that do not depend on a cell wall
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

