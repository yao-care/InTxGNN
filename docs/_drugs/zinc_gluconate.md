---
layout: default
title: Zinc Gluconate
parent: Model Prediction Only (L5)
nav_order: 906
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "Zinc gluconate"
predicted_indications: ["anemia of prematurity", "injury", "cell proliferation disorder", "florid cemento-osseous dysplasia", "segmental odontomaxillary dysplasia", "perinatal disease", "radiation or chemically induced disorder", "disease by subcellular system affected", "iatrogenic disease", "regional odontodysplasia"]
description: "Zinc Gluconate: predicted new indication Anemia of prematurity (evidence level L5). Approved use: Not recorded in the local data"
---

# Zinc Gluconate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Zinc Gluconate: Anemia of prematurity
{: .text-alpha }

## One-Sentence Summary

Zinc gluconate is a zinc salt, and it is marketed in India as oral zinc products.
The TxGNN model predicts it may be useful for **anemia of prematurity** (score 0.9994), but **no clinical trials and no publications** were found for this indication, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Anemia of prematurity |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (9 of 9) – CDSCO approval status is not included in this data |
| Number of Listed Products | 9 (valid: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Zinc is an essential trace element involved in many enzymatic processes, including erythropoiesis and the balance of iron and copper in the body. This gives a plausible biological link to anemia in premature infants.

The original indications (ascorbic acid deficiency and scurvy) are nutritional deficiencies, and anemia of prematurity is also partly related to nutrient status. That is a loose conceptual connection, not direct evidence. The prediction has not been tested in any trial or publication compiled for this report. Note also that chronic excess zinc is known to cause copper-deficiency anemia (see the case report PMID 12728841 in the data), so the direction of effect on blood parameters needs careful study.

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 249882 | Zincorun Oral Solution | Bottle of 100 ml oral solution | Not stated in the records |
| 109187 | IZinc Oral Suspension | Bottle of 100 ml oral suspension | Not stated in the records |
| 113921 | Jink Syrup | Bottle of 100 ml oral solution | Not stated in the records |
| 248473 | Zincotus Syrup | Bottle of 100 ml syrup | Not stated in the records |
| 246658 | Zioral Drops | Bottle of 15 ml oral drops | Not stated in the records |

All 9 registrations are valid single-ingredient products; the five above are shown.

## Safety Considerations

- **Drug Interactions**: 103 interactions were recorded. Most listed ones are Minor (for example abatacept, adalimumab, hydrocortisone, dexamethasone). The Moderate ones include alendronic acid, risedronic acid, ibandronate, tetracycline and baloxavir marboxil. These are consistent with zinc reducing the absorption of some drugs, so dosing should be separated in time.
- **Knowledge-graph contraindication signals** (not label text): hypertension, rheumatoid arthritis, systemic lupus erythematosus, multiple sclerosis, allergic rhinitis, blood coagulation disease, sickle cell anemia, iron metabolism diseases (hereditary hemochromatosis, hemosiderosis), Wilson disease, primary hyperoxaluria, asthma, diarrheal disease, HIV/AIDS and leukemia. These need verification against the package insert.
- **Other safety signals in the literature**: intranasal zinc gluconate has been linked to loss of smell (anosmia), and chronic excessive zinc intake can cause copper-deficiency anemia. Both are relevant to any new use, particularly in infants.

Package insert warnings and contraindications for the Indian products were not available and should be obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for anemia of prematurity is supported only by the TxGNN score, with no trials or literature. The broader zinc-related literature for the other predicted indications is mostly animal or mechanistic work, and the safety record includes anemia from zinc excess in humans.

**To proceed, the following is needed:**
- A literature and trial search specific to zinc supplementation in preterm infants and anemia of prematurity
- Mechanism of action data (for example from DrugBank)
- Package insert warnings and contraindications from the Indian regulator's records
- A dose and copper-status safety assessment for neonates and preterm infants
- Confirmation of the original approved indications, since the licence records contain no indication text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

