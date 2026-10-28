---
layout: default
title: Dipyridamole
parent: Moderate Evidence (L3-L4)
nav_order: 276
evidence_level: L4
indication_count: 8
monitor_inn: "Dipyridamole"
predicted_indications: ["thrombotic disease", "sick sinus syndrome 2, autosomal dominant", "transient ischemic attack (disease)", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "lateral sinus thrombosis", "cavernous sinus thrombosis"]
last_modified_at: 2026-10-28
description: "Dipyridamole: predicted new indication Thrombotic disease (evidence level L4). Approved use: Atrial fibrillation"
---

# Dipyridamole
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **8** 
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

## Dipyridamole: From Atrial Fibrillation to Thrombotic Disease
{: .text-alpha }

## One-Sentence Summary

Dipyridamole is an antiplatelet and vasodilator drug. The knowledge graph records atrial fibrillation as its original indication, but this is a recorded relation, not an approved indication.
The TxGNN model predicts it may be effective for **thrombotic disease**, a broad category.
No clinical trials are registered for this term, and the supporting evidence is **about 10 relevant publications**, mostly older narrative reviews and one case report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation (a relation recorded in the knowledge graph; the local licence records contain no approved indication text) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L4 |
| India Market Status | Marketed (valid licences: 6 of 6) |
| Number of Registrations | 6 (valid: 6) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Dipyridamole inhibits adenosine reuptake (via ENT1) and phosphodiesterases (PDE3/PDE5). This raises extracellular adenosine and platelet cAMP/cGMP levels, which suppresses platelet aggregation. The literature also describes possible vascular protective effects, including potentiation of nitric oxide signalling and antioxidant activity.

Atrial fibrillation is a thromboembolic-risk condition, and thrombotic disease is driven largely by platelet activation and clot formation. The antiplatelet mechanism therefore fits the predicted use, which is why the model links the two.

Three limits apply:
- The predicted term is very broad and does not name a specific thrombotic condition.
- The retrieved literature gives no disease-specific randomised evidence for it.
- Platelet-directed therapy is a weaker fit for coagulation-driven venous thrombosis.

Because of this, the support is mechanistic and indirect, not confirmatory.

## Clinical Trial Evidence

Currently no related clinical trials registered for "thrombotic disease".

The data compiled for this report do contain a more specific, better-supported prediction: transient ischemic attack. It includes the large randomised trial ESPRIT ([NCT00161070](https://clinicaltrials.gov/study/NCT00161070), Phase 4, completed, 4,500 patients), which compared aspirin plus dipyridamole with aspirin alone after TIA or minor stroke of arterial origin. That evidence belongs to the TIA indication, not to the broad thrombotic disease term assessed here.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18174451](https://pubmed.ncbi.nlm.nih.gov/18174451/) | 2008 | Review | Arterioscler Thromb Vasc Biol | Dipyridamole is a PDE inhibitor that raises cAMP/cGMP, reversibly inhibits platelet aggregation, and may enhance nitric oxide vascular effects |
| [2182246](https://pubmed.ncbi.nlm.nih.gov/2182246/) | 1990 | Review | Clin Cardiol | Aspirin with dipyridamole in coronary thrombosis: partial effectiveness in experimental models, with limitations in coronary artery disease |
| [12765506](https://pubmed.ncbi.nlm.nih.gov/12765506/) | 2003 | Review | Med J Aust | Antiplatelet drugs protect against myocardial infarction, stroke and other vascular events in high-risk patients |
| [382146](https://pubmed.ncbi.nlm.nih.gov/382146/) | 1979 | Review | Postgrad Med | Aspirin, dipyridamole and sulfinpyrazone show antithrombotic effects in humans |
| [20955428](https://pubmed.ncbi.nlm.nih.gov/20955428/) | 2010 | Review | Ann N Y Acad Sci | Dipyridamole in acute stroke: antithrombotic plus possible anti-inflammatory and neuroprotective effects |
| [25697566](https://pubmed.ncbi.nlm.nih.gov/25697566/) | 2015 | Review | Curr Top Med Chem | Described as a long-used antithrombotic and vasodilator, with previously unrecognised antioxidant activity |
| [559478](https://pubmed.ncbi.nlm.nih.gov/559478/) | 1977 | Case report | Arch Intern Med | In thrombotic thrombocytopenic purpura, one patient relapsed when dipyridamole was tapered and remitted again at a higher dose |
| [2440111](https://pubmed.ncbi.nlm.nih.gov/2440111/) | 1987 | Review | Semin Hematol | Antiplatelet agents have been linked to resolution of thrombocytopenia in many TTP cases; failures were attributed to dose and disease severity |
| [15494585](https://pubmed.ncbi.nlm.nih.gov/15494585/) | 2004 | Review | JAMA | Antiplatelet agents, alone or combined, prevent recurrent vascular events in established vascular disease |
| [11945125](https://pubmed.ncbi.nlm.nih.gov/11945125/) | 2002 | Review | Curr Med Chem | Platelet aggregation drives thromboembolic disease, and the antiplatelet armamentarium has expanded |

Several other retrieved papers (for example a bevacizumab mesothelioma trial and a heparin-induced thrombocytopenia report) are off-target and are not listed.

## India Market Information

Dipyridamole is marketed in India with 6 valid single-ingredient registrations. The licence records provide no approved indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| 111097 | Infartin 60 Tablet | Strip of 30 tablets | Jenburkt Pharmaceuticals Ltd |
| 220671 | Thrombonil 75mg Tablet | Strip of 10 tablets | Sun Pharmaceutical Industries Ltd |
| 176522 | Persantin 100mg Tablet | Strip of 10 tablets | German Remedies |
| 41947 | Cardiwell 75mg Tablet | Strip of 10 tablets | Torrent Pharmaceuticals Ltd |
| 44912 | Cardiwell 100mg Tablet | Strip of 10 tablets | Torrent Pharmaceuticals Ltd |

## Safety Considerations

- **Contraindication-type relations in the knowledge graph (not label text):** The graph links dipyridamole to conditions including kidney disease, liver disease, gallbladder disease, thrombocytopenia, peptic ulcer disease, hypotensive disorder, gout, hemophilia, acute coronary syndrome, myocardial infarction, anemia, gastritis, Reye syndrome and Alzheimer disease. These need verification against the approved label.
- **Drug interactions:** 321 interactions were identified in total. Moderate-level interactions include dexfenfluramine, sibutramine and fenfluramine. Other listed interacting drugs, with unclassified severity, include acetylsalicylic acid, cimetidine, omeprazole, pantoprazole, metformin, simvastatin and morphine.
- **Mechanism-related caution:** Because dipyridamole raises adenosine, it may slow sinus and AV node conduction. Bleeding risk is also a concern when it is combined with aspirin or anticoagulants.

Package insert warnings and contraindications for the Indian products were not available. Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible, but "thrombotic disease" is a broad term with no registered trials and no disease-specific randomised evidence in the compiled literature. The supporting papers are mostly older reviews, and the prediction comes only from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence.

**To proceed, the following is needed:**
- Define a specific thrombotic condition. The TIA/secondary stroke prevention indication, backed by ESPRIT, is the strongest candidate and should be assessed separately.
- Obtain the Indian package insert text to confirm approved indications, warnings and contraindications.
- Confirm formal mechanism-of-action data from a curated source.
- Review the large interaction burden, especially combinations with aspirin and anticoagulants.
- Verify the knowledge-graph contraindication relations against the label.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

