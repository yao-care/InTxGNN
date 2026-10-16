---
layout: default
title: Methylene Blue
parent: Model Prediction Only (L5)
nav_order: 538
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Methylene Blue: predicted new indication Bronchitis (evidence level L5). Approved use: Methemoglobinemia, sulfhemoglobinemia"
monitor_inn: "Methylene blue"
predicted_indications: ["bronchitis", "methemoglobinemia, alpha type", "methemoglobinemia due to deficiency of methemoglobin reductase"]
---

# Methylene Blue
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Methylene Blue: From Methemoglobinemia to Bronchitis

## One-Sentence Summary

Methylene blue is an injectable redox agent, originally used to treat methemoglobinemia and sulfhemoglobinemia.
The TxGNN model predicts it may be effective for **bronchitis**, but **no clinical trials** and **8 publications** were found, and none of those publications tests methylene blue as a treatment for bronchitis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Methemoglobinemia, sulfhemoglobinemia (from the knowledge-graph indication data; the India license records contain no indication text) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Methylene blue is generally known as a redox agent that also inhibits nitric oxide synthase and guanylate cyclase. In theory, this could affect airway inflammation or smooth muscle tone.

Its original indication, methemoglobinemia, is a blood disorder. Bronchitis is an inflammatory airway disease, so the two conditions are not obviously related. None of the retrieved literature tests the airway-related mechanism.

In the bronchitis-related records, methylene blue appears only as a diagnostic stain (for example, in bronchoscopy) or as a keyword match. The very high model score is therefore not backed by a plausible, data-supported mechanistic link. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below is a clinical study of methylene blue treating bronchitis. They are listed in order of relevance, and no RCTs or systematic reviews were found.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9387672](https://pubmed.ncbi.nlm.nih.gov/9387672/) | 1996 | Diagnostic study | Zhonghua Wai Ke Za Zhi | Methylene blue staining during fiberoptic bronchoscopy: 97.14% of central malignant bronchial tumours stained versus 8.33% of bronchitis cases. This is a diagnostic use, not a treatment. |
| [7313968](https://pubmed.ncbi.nlm.nih.gov/7313968/) | 1981 | Diagnostic staining study | Terapevticheskii Arkhiv | Chromoendoscopy with methylene blue to distinguish benign from malignant gastrointestinal and bronchial neoplasms. |
| [8420409](https://pubmed.ncbi.nlm.nih.gov/8420409/) | 1993 | Methodological | Am Rev Respir Dis | Methylene blue used as one of five markers to quantify intraalveolar fluid in bronchoalveolar lavage. |
| [6121761](https://pubmed.ncbi.nlm.nih.gov/6121761/) | 1982 | Pharmacology study | Int J Clin Pharmacol Ther Toxicol | A beta-blocker study that used methylene blue only as an indicator for circulation time. |
| [31419501](https://pubmed.ncbi.nlm.nih.gov/31419501/) | 2020 | Preclinical (ex vivo) | J Ethnopharmacol | Lippia alnifolia essential oil relaxes guinea-pig trachea. Bronchitis is mentioned only as a folk-medicine use, and this is not about methylene blue as a therapy. |
| [21767626](https://pubmed.ncbi.nlm.nih.gov/21767626/) | 2011 | Preclinical (animal) | J Ethnopharmacol | Antidepressant-like effects of Aloysia gratissima through the nitric oxide–cGMP pathway. Bronchitis is mentioned only as a traditional use. |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytical/biosensor | Anal Chim Acta | An electrochemical aptasensor for detecting theophylline, a bronchodilator. Not relevant to methylene blue therapy. |
| [20084922](https://pubmed.ncbi.nlm.nih.gov/20084922/) | 2009 | Case report | Mikrobiyol Bul | Moraxella catarrhalis endocarditis. Bronchitis is mentioned only as background. |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| Registration No. 200838 | Sam MB 10mg Injection | Vial of 1 injection | Samarth Life Sciences Pvt Ltd |
| Registration No. 27392 | Blue Beam Injection | Ampoule of 10 ml injection | Flagship Biotech International |

Both registrations are valid single-ingredient injectable products.

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (not taken from label text). The following conditions are linked to methylene blue as contraindications, so they should be checked against the official package insert:
  - G6PD deficiency (risk of hemolysis)
  - Cardiovascular conditions: hypertension, congestive heart failure, coronary artery disease, sudden cardiac arrest, heart conduction disease
  - Liver and kidney conditions: liver failure, liver disease, cirrhosis, kidney disease, gallbladder disease
  - Blood disorders: anemia, macrocytic anemia, blood coagulation disease, hemophilia
  - Metabolic conditions: diabetes mellitus, diabetic ketoacidosis, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, glycogen storage disease, galactosemia, cystinuria
  - Neuromuscular conditions: myasthenia gravis, neuromuscular junction disease
  - Other: gastritis, benign prostatic hyperplasia, pyoureter
- **Drug interactions**: 186 interactions are recorded. Many of the major ones involve serotonergic or sympathomimetic drugs, which raises a concern about serotonin syndrome. Examples of major interactions:
  - Bupropion
  - Morphine and opium
  - Ondansetron, granisetron, dolasetron and palonosetron
  - Ephedrine
  - Phentermine, diethylpropion, mazindol, fenfluramine, dexfenfluramine and lorcaserin
  - Isometheptene
- **Moderate interactions** include epinephrine (including nasal, ophthalmic and topical forms) and ephedrine.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The bronchitis prediction has a very high model score but no clinical trials, no supportive literature and no data-backed mechanism, so the evidence level is only L5. The other two predictions for this drug are better supported, but both overlap with its approved use:
- Methemoglobinemia due to methemoglobin reductase deficiency (L3) is supported by veterinary and human case reports. It could proceed with guardrails: G6PD screening, serotonergic interaction checks and dose limits.
- Alpha-type methemoglobinemia (L4) is uncertain, because the alpha-globin variants are resistant to reduction.

**To proceed, the following is needed:**
- Detailed mechanism of action data, plus preclinical evidence that methylene blue acts on airway inflammation or smooth muscle
- Any clinical or in vivo studies of methylene blue as a treatment (not a stain) in bronchitis
- Package insert warnings and contraindications from the India regulatory source
- A safety plan covering G6PD screening and serotonergic drug interactions, and a route and formulation assessment, since only injectable forms are marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

