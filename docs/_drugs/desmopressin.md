---
layout: default
title: Desmopressin
parent: Model Prediction Only (L5)
nav_order: 244
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-30
description: "Desmopressin: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Hereditary von Willebrand disease (also von Willebrand disease…"
monitor_inn: "Desmopressin"
predicted_indications: ["congenital prothrombin deficiency", "inherited thrombophilia", "Glanzmann thrombasthenia", "primary release disorder of platelets", "Scott syndrome", "flood factor deficiency"]
---

# Desmopressin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Desmopressin: From von Willebrand Disease to Congenital Prothrombin Deficiency
{: .text-alpha }

## One-Sentence Summary

Desmopressin is a synthetic vasopressin analogue originally used for hereditary von Willebrand disease, hemophilia A (including symptomatic female carriers) and nocturnal enuresis.
The TxGNN model's top-ranked prediction is **congenital prothrombin deficiency** (score 0.9970), but it has **no clinical trials** and only **1 general review** behind it, and the mechanism does not hold up.
The best-supported option among the ten predictions is a different one: **primary release disorder of platelets**, with one pediatric cohort study and a 2023 review.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hereditary von Willebrand disease (also von Willebrand disease, hemophilia, nocturnal enuresis) |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 0.9970 |
| Evidence Level | L5 |
| India Market Status | Listed in a compiled Indian medicine price dataset (10 of 10) – CDSCO approval status is not included in this data |
| Number of Registrations | 10 (valid: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, desmopressin is a vasopressin analogue that raises plasma von Willebrand factor (VWF) and factor VIII. Its efficacy in von Willebrand disease and mild hemophilia A is established.

For the top-ranked prediction, **congenital prothrombin deficiency**, this mechanism does not apply. Prothrombin (factor II) levels are not affected by desmopressin, so there is no plausible way for it to correct this deficiency. The only linked paper is a 1993 general review of inherited bleeding disorders. The high score (0.9970) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Across the ten predictions, the picture is mixed:

- **Most plausible:** *Primary release disorder of platelets* (L3). VWF release and improved platelet adhesion may partly compensate for granule-release defects (storage pool and aspirin-like disorders). Evidence is small and non-randomized, and responses are variable.
- **Research questions only:** *Glanzmann thrombasthenia* (L4) and *bleeding diathesis due to a collagen receptor defect* (L4). Desmopressin does not correct the underlying defects. In Glanzmann thrombasthenia it is at most an adjunct for mild bleeding.
- **Safety signals rather than benefits:** *Inherited thrombophilia*, *thrombocytopenic purpura* (including TTP) and *pseudo-von Willebrand disease* (platelet-type). Desmopressin-induced VWF release may worsen these conditions. Case reports describe desmopressin-induced or worsened TTP.
- **Likely artifacts:** *Flood factor deficiency* (not an established disease name), *Scott syndrome* and *hereditary thrombocytosis with transverse limb defect*. These have no supporting evidence of desmopressin use.

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the ten predicted indications.

## Literature Evidence

**Top-ranked prediction (congenital prothrombin deficiency)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7684674](https://pubmed.ncbi.nlm.nih.gov/7684674/) | 1993 | Review | Drugs | General review of treatment options for inherited bleeding disorders; no specific evidence for desmopressin in prothrombin deficiency |

**Best-supported prediction (primary release disorder of platelets)**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36656570](https://pubmed.ncbi.nlm.nih.gov/36656570/) | 2023 | Review | Eur J Haematol | Desmopressin releases VWF and FVIII, enhances platelet adhesion and shortens bleeding time. Effective in mild hemophilia A, certain VWD subtypes, uremia and liver disease. Use can be complicated by hyponatremia and, rarely, arterial thrombotic events |
| [21509710](https://pubmed.ncbi.nlm.nih.gov/21509710/) | 2011 | Cohort | Klin Padiatr | Effect of desmopressin on primary hemostasis in children with aspirin-like defect (hereditary thrombocytopathy) |
| [23051555](https://pubmed.ncbi.nlm.nih.gov/23051555/) | 2013 | Cohort | Haemophilia | Increased amounts of VWF bound to microparticles after desmopressin infusion; may help explain effects in platelet disorders |
| [22057877](https://pubmed.ncbi.nlm.nih.gov/22057877/) | 2011 | Case report | Hamostaseologie | Therapy-refractory menorrhagia as first manifestation of Hermansky-Pudlak syndrome (platelet storage pool defect) |
| [22726100](https://pubmed.ncbi.nlm.nih.gov/22726100/) | 2012 | Review | Haemophilia | Overview of inherited platelet disorders |

**Other predictions: key items**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10509036](https://pubmed.ncbi.nlm.nih.gov/10509036/) | 1999 | Not classified | Haematologica | In vitro and ex vivo effects of desmopressin on platelet function (Glanzmann thrombasthenia prediction) |
| [16444446](https://pubmed.ncbi.nlm.nih.gov/16444446/) | 2006 | Case report | Clin Appl Thromb Hemost | Dental extraction in a patient with Glanzmann thrombasthenia: desmopressin was ineffective, and bleeding was controlled with recombinant factor VIIa |
| [1785670](https://pubmed.ncbi.nlm.nih.gov/1785670/) | 1991 | Cohort | Am J Pediatr Hematol Oncol | Desmopressin plus ethamsylate synergistically shortened bleeding time in 12 patients with constitutional bleeding disorders who did not respond to desmopressin alone |
| [22726101](https://pubmed.ncbi.nlm.nih.gov/22726101/) | 2012 | Review | Haemophilia | Treatment of inherited platelet disorders; platelet transfusion is frequently needed in severe cases |
| [15499705](https://pubmed.ncbi.nlm.nih.gov/15499705/) | 2004 | Case report | Thromb Haemost | **Safety signal:** worsening of TTP symptoms after desmopressin |
| [21921792](https://pubmed.ncbi.nlm.nih.gov/21921792/) | 2011 | Case report | Blood Coagul Fibrinolysis | **Safety signal:** Moschcowitz-like syndrome (TTP-like) after desmopressin for postpartum hemorrhage |
| [16460464](https://pubmed.ncbi.nlm.nih.gov/16460464/) | 2006 | Case report | J Thromb Haemost | Link between desmopressin use for nocturnal enuresis and inherited TTP (Upshaw-Schulman syndrome) |
| [12109311](https://pubmed.ncbi.nlm.nih.gov/12109311/) | 2002 | Case report | Ned Tijdschr Geneeskd | **Safety signal:** a trial dose of desmopressin caused severe thrombocytopenia in a patient with VWD type 2B |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 59569 | Dpressin 0.1mg Tablet (United Biotech) | Strip of 10 tablets | Not stated |
| 133549 | Minirin 0.1mg Tablet (Ferring) | Bottle of 15 tablets | Not stated |
| 134712 | Minirin Melt 120mcg Tablet (Ferring) | Strip of 10 tablets | Not stated |
| 133878 | Minirin Nasal Spray (Ferring) | 2.5 ml nasal spray | Not stated |
| 59224 | Dpressin Nasal Spray (United Biotech) | 5 ml nasal spray | Not stated |

Ten valid single-ingredient registrations are on record in total, covering oral tablets (including melt/orally disintegrating forms) and nasal sprays. Approved indication text was not available for any of them.

## Safety Considerations

- **Contraindications and disease associations (knowledge graph, not label text):** hypertension and hypertensive disorder, coronary artery disease, impaired renal function, cystic fibrosis, water intoxication, polydipsia, dipsogenic diabetes insipidus, allergic and vasomotor rhinitis, common cold, pharyngitis, respiratory tract infection, and von Willebrand disease (the last likely refers to specific subtypes such as type 2B).
- **Drug interactions:** 172 interactions were identified. Major interactions are with corticosteroids: hydrocortisone, triamcinolone, dexamethasone, beclomethasone, betamethasone, budesonide, prednisolone and prednisone. Moderate interactions include epinephrine, loperamide, morphine, opium and chlorpropamide. Aspirin is a minor interaction.
- **Literature-based safety signals:**
  - Hyponatremia and rarely arterial thrombotic events (2023 review).
  - Worsening or induction of TTP-like syndromes.
  - Severe thrombocytopenia in VWD type 2B.
  
  These signals bear directly on three of the ten predictions (inherited thrombophilia, thrombocytopenic purpura, pseudo-von Willebrand disease).

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, congenital prothrombin deficiency, has no clinical trials, one general review, and no plausible mechanism, since desmopressin does not raise prothrombin. Across all ten predictions there are no registered clinical trials. Three predictions carry safety signals of possible harm, and several others probably reflect similarities the TxGNN model (deep learning) learned between related diseases, not biological evidence. The only prediction with meaningful support is primary release disorder of platelets (L3), and that evidence is small, non-randomized and variable.

**To proceed, the following is needed:**
- Shift the focus from the top-ranked prediction to **primary release disorder of platelets**. Plan a prospective, controlled study of desmopressin response in storage pool and aspirin-like disorders, with a desmopressin challenge test before use.
- Treat Glanzmann thrombasthenia and collagen receptor defects as research questions only, with desmopressin positioned at most as an adjunct.
- Flag thrombotic thrombocytopenic purpura, inherited thrombophilia and platelet-type (pseudo-) von Willebrand disease as **cautions, not opportunities**, in any repurposing plan.
- Verify the disease definition of "flood factor deficiency" before any assessment.
- Obtain package insert warnings and contraindications from the India regulatory sources, as well as approved indication text for the ten registrations.
- Obtain detailed mechanism of action data from DrugBank.
- Define a monitoring plan for hyponatremia (sodium and fluid restriction) and for thrombotic risk in any new population.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

