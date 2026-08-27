---
layout: default
title: Iron
parent: 僅模型預測 (L5)
nav_order: 346
evidence_level: L5
indication_count: 6
---

# Iron
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Iron: From Iron Deficiency Anemia to Plummer-Vinson Syndrome

## One-Sentence Summary

Iron is an essential mineral with a well-established role in treating iron deficiency anemia.
The TxGNN model's most clinically actionable prediction is that iron supplementation may be effective for **Plummer-Vinson Syndrome** — a rare triad of dysphagia, iron deficiency anemia, and esophageal webs,
with **0 registered clinical trials** but **19 supporting publications** in the literature.

> **Note on Top-Ranked Prediction:** The rank #1 TxGNN output (vitamin B12- and folate-independent constitutional megaloblastic anemia, score 99.89%) has been flagged as a likely **false positive**. Megaloblastic anemia is caused by impaired DNA synthesis from B12/folate metabolic defects — mechanistically unrelated to iron deficiency. The high score likely reflects graph-level proximity between "anemia" nodes in the knowledge graph. This report therefore focuses on **rank #2 — Plummer-Vinson Syndrome** — the highest-evidenced, mechanistically coherent, and actionable prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Iron deficiency anemia |
| Predicted New Indication | Plummer-Vinson Syndrome (TxGNN Rank #2) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacology, iron supplementation restores systemic iron stores — raising serum ferritin, hemoglobin, and transferrin saturation — and corrects the downstream consequences of iron deficiency across multiple organ systems.

Plummer-Vinson Syndrome (also called Paterson-Kelly-Brown syndrome) is defined by a classical triad: progressive dysphagia, iron deficiency anemia, and esophageal webs in the post-cricoid region. Iron deficiency is not merely associated with PVS — it is widely accepted as a **direct etiological driver**: depleted iron leads to mucosal atrophy and oxidative damage in the upper esophageal epithelium, triggering fibrous ring formation and web development. Correcting iron deficiency therefore addresses the root cause. In multiple reported cases, iron supplementation resolved anemia, improved dysphagia symptoms, and even led to spontaneous disappearance of esophageal webs.

This makes PVS fundamentally different from a conventional drug repurposing scenario: iron supplementation is a **causal treatment** for an iron-deficiency-driven disease, rather than an off-label use based on mechanistic extrapolation. The main reason it is classified as a "repurposing" candidate is that DrugBank does not formally list PVS as a registered indication for iron — a regulatory gap rather than a scientific one. The declining incidence of PVS in high-income countries (attributed to improved nutritional status) further confirms that correcting iron deficiency is both preventive and curative in this condition.

---

## Clinical Trial Evidence

Currently no clinical trials directly investigating iron supplementation specifically for Plummer-Vinson Syndrome are registered on ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38871147](https://pubmed.ncbi.nlm.nih.gov/38871147/) | 2024 | Review / Case Series | Clin Gastroenterol Hepatol | Comprehensive review of PVS as a classic triad; iron supplementation is central to management alongside endoscopic dilation |
| [29089792](https://pubmed.ncbi.nlm.nih.gov/29089792/) | 2017 | Narrative Review | J Blood Medicine | Iron supplementation resolves anemia and often leads to web regression; declining syndrome prevalence linked to improved iron nutrition globally |
| [31417270](https://pubmed.ncbi.nlm.nih.gov/31417270/) | 2019 | Review | J Multidisciplinary Healthcare | Multidisciplinary approach recommended; iron supplementation first-line; long-term surveillance warranted due to carcinoma risk |
| [34651287](https://pubmed.ncbi.nlm.nih.gov/34651287/) | 2022 | Case-based Review | Immunologic Research | PVS in a Sjögren syndrome patient; systematic review of PVS-autoimmune associations with shared iron deficiency mechanism |
| [38034443](https://pubmed.ncbi.nlm.nih.gov/38034443/) | 2023 | Case Report | JPGN Reports | Pediatric PVS in a 4-year-old; iron deficiency confirmed as a crucial causal factor; balloon dilatation plus iron supplementation effective |
| [26502163](https://pubmed.ncbi.nlm.nih.gov/26502163/) | 2015 | Case Series | J Pediatr Gastroenterol Nutr | PVS in children; iron deficiency consistently present; supplementation recommended as first step before invasive procedures |
| [12823219](https://pubmed.ncbi.nlm.nih.gov/12823219/) | 2003 | Case Report | Dis Esophagus | Two middle-aged women with PVS; iron supplementation eliminated dysphagia and associated symptoms in both cases |
| [7575056](https://pubmed.ncbi.nlm.nih.gov/7575056/) | 1995 | Case Report | Arch Intern Med | Iron repletion frequently improves dysphagia; highlights elevated postcricoid carcinoma risk requiring surveillance endoscopy |
| [7865729](https://pubmed.ncbi.nlm.nih.gov/7865729/) | 1994 | Historical Review | J Gastroenterol Hepatol | Historical analysis identifies iron deficiency as the primary predisposing condition; decreased incidence correlates with nutritional improvement |
| [39760192](https://pubmed.ncbi.nlm.nih.gov/39760192/) | 2025 | Systematic Review | Oral Diseases | Systematic review of head and neck cancer in PVS patients; underscores importance of treating underlying iron deficiency and conducting oncological surveillance |

---

## India Market Information

Iron (DrugBank ID: DB01592) currently has **no registered pharmaceutical products** in India according to this evidence pack. No authorization records are available.

> **Clinical Note:** Elemental iron is widely available in India as over-the-counter nutritional supplements and is included in national anemia control programs (e.g., the National Iron Plus Initiative). Formal pharmaceutical licensing under CDSCO may not capture all routes of access. A regulatory pathway assessment is recommended before drawing conclusions about availability.

---

## Safety Considerations

**Drug Interactions — 79 total interactions identified (key examples shown):**

*Major interactions:*
- **Dolutegravir** — Iron substantially reduces dolutegravir absorption through chelation; iron should be taken at least 2 hours before or 6 hours after dolutegravir
- **Bictegravir** — Same chelation mechanism; critical for HIV patients on integrase inhibitor regimens

*Moderate interactions (selected):*
- **Omeprazole / Rabeprazole** — Proton pump inhibitors raise gastric pH and impair non-heme iron absorption; commonly co-prescribed in anemia patients
- **Doxycycline / Tetracycline / Ciprofloxacin / Delafloxacin** — Mutual chelation reduces bioavailability of both iron and the antibiotic; separate doses by at least 2–3 hours
- **Alendronic acid / Risedronic acid / Ibandronate** — Iron chelates bisphosphonates, reducing their efficacy; timing separation required
- **Levodopa** — Iron forms chelates with levodopa, reducing its absorption and antiparkinsonian effect — clinically significant in elderly patients with comorbid Parkinson's disease
- **Deferiprone** — Combining iron supplementation with an iron chelator directly antagonizes therapeutic intent; avoid concurrent use

Please refer to the package insert for complete warnings and contraindications, as CDSCO-specific labeling data was not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Plummer-Vinson Syndrome is pathophysiologically rooted in iron deficiency, making iron supplementation a direct causal intervention with consistent support across 19 publications including case reports, narrative reviews, and historical analyses. Although no prospective clinical trials have been specifically registered for PVS, the mechanistic and clinical case for iron is well-established in the medical literature.

**To proceed, the following is needed:**
- Retrieve CDSCO package insert to document formal warnings, contraindications, and approved dosage forms
- Confirm MOA data from DrugBank API (currently missing from this evidence pack)
- Assess India-specific availability: confirm whether oral ferrous sulfate, ferrous fumarate, or intravenous iron formulations are accessible under existing nutritional supplement or prescription frameworks
- Define appropriate iron formulation and dosing for PVS: oral iron is first-line; intravenous formulations may be needed in severe malabsorption cases
- Establish oncological surveillance protocol: PVS carries an elevated risk of postcricoid esophageal carcinoma, requiring endoscopic follow-up even after successful iron repletion
- Monitor resolution of esophageal webs: imaging or endoscopic confirmation of web regression may be needed; cases with persistent dysphagia despite iron correction require esophageal dilation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

