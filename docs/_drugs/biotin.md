---
layout: default
title: Biotin
parent: 僅模型預測 (L5)
nav_order: 111
evidence_level: L5
indication_count: 2
---

# Biotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Biotin: From Nutritional Supplement to Dyspepsia

## One-Sentence Summary

Biotin (Vitamin B7) is an essential micronutrient acting as a coenzyme for multiple carboxylases, traditionally used as a nutritional supplement without a registered drug indication in India's market.
The TxGNN model predicts it may be effective for **Dyspepsia**,
however, current evidence support is limited — with **0 directly relevant clinical trials** and only **1 marginally related publication** — placing this candidate at evidence level **L4**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Nutritional supplement (Vitamin B7); no registered drug indication on record |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L4 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why Is This Prediction Reasonable?

Biotin (Vitamin B7) serves as an essential cofactor for multiple carboxylase enzymes — including acetyl-CoA carboxylase, pyruvate carboxylase, and propionyl-CoA carboxylase — playing a central role in fatty acid synthesis, gluconeogenesis, and amino acid metabolism. Biotin deficiency is known to manifest with gastrointestinal symptoms such as nausea and vomiting, suggesting an indirect relationship between Biotin status and digestive tract function.

A second line of reasoning links Biotin to gut health through the gut microbiome: intestinal bacteria can both produce and consume Biotin, and Biotin may modulate intestinal epithelial barrier integrity. Functional dyspepsia is increasingly understood as a disorder with multifactorial pathogenesis, including microbiome dysbiosis and impaired mucosal barrier function. The theoretical chain connecting Biotin repletion to symptomatic relief in dyspepsia is therefore mechanistically plausible — but remains at the level of hypothesis.

Importantly, no direct mechanistic evidence or controlled clinical data currently establish Biotin as an active therapeutic agent for dyspepsia. The TxGNN model's graph-based prediction may reflect shared network proximity between Biotin's metabolic nodes and gastrointestinal disease pathways, rather than a direct causal pharmacological link. This prediction should be interpreted as a hypothesis-generating signal, not a validated therapeutic claim.

---

## Clinical Trial Evidence

Both trials retrieved from ClinicalTrials.gov were assessed as **Grade C** (false-positive retrieval, no direct relevance):

| Trial Number | Phase | Status | Enrollment | Assessment |
|---------|------|------|------|---------|
| [NCT05389813](https://clinicaltrials.gov/study/NCT05389813) | Phase 2/3 | Unknown | 150 | **Irrelevant** — Compares Oxycodone vs Pregabalin for postoperative pain control; no connection to Biotin or dyspepsia |
| [NCT03360435](https://clinicaltrials.gov/study/NCT03360435) | N/A | Completed | 99 | **Indirectly related at best** — Examines transdermal vitamin absorption (including Biotin) in post-bariatric surgery patients; dyspepsia is not an endpoint; population-specific findings are not generalizable |

> **Note:** No clinical trials directly investigating Biotin for dyspepsia treatment were identified.

---

## Literature Evidence

Of 7 publications retrieved, only 1 has meaningful (though indirect) relevance to Biotin in dyspepsia. The remainder concern IBS pathophysiology, H. pylori gastritis, or unrelated conditions where Biotin appears incidentally.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [25384804](https://pubmed.ncbi.nlm.nih.gov/25384804/) | 2014 | Clinical Interventional Study | Minerva Gastroenterol Dietol | Open multicentric study evaluating a multi-ingredient supplement (sodium alginate, calcium carbonate, pineapple, papaya, ginger, α-galactosidase, fennel — product name "Bioten") in functional dyspepsia post-H. pylori treatment; Biotin itself is not an independent variable |
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case Report | J Dermatology | Infant with Biotin deficiency initially diagnosed as having dyspepsia and fed amino acid formula; Biotin deficiency caused dermatological manifestations — dyspepsia was the presenting context, not the outcome |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Clinical Study | Exp Clin Gastroenterology | Evaluates a prebiotic supplement (Stimbifid) containing inulin, oligofructose, and multiple vitamins including Biotin in patients with bronchopulmonary disease on antibiotics; GI microbiota correction was assessed, dyspepsia not a primary endpoint |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Observational | Int J Mol Med | Describes antral endocrine cell changes in IBS patients vs healthy controls; no Biotin involvement |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Observational | World J Gastrointest Endoscopy | Examines oxyntic mucosa endocrine cells in IBS; no Biotin involvement |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Histological/Immunological Study | J Clin Pathol | IL-10 localisation in H. pylori-associated gastritis; no Biotin involvement |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Basic/Histological Study | Kidney International | Small bowel mucosal findings in IgA nephropathy; unrelated to Biotin or dyspepsia |

> **Summary:** No published RCT or controlled study directly tests Biotin as a treatment for dyspepsia. The most relevant paper (PMID 25384804) evaluates a compound supplement where Biotin is not an isolable variable.

---

## India Market Information

Biotin is **not registered as a pharmaceutical product** in India's drug regulatory database. No marketing authorisations were identified.

> Biotin may be commercially available in India as a food supplement, nutraceutical, or over-the-counter vitamin product, but this falls outside the scope of the drug repurposing regulatory framework evaluated here.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No drug-drug interaction data were identified in the DDI database query. No formal key warnings or contraindications data were retrieved from the regulatory source. Given Biotin's status as an essential micronutrient with a well-established safety profile at physiological doses, the absence of formal safety filings reflects its classification as a nutritional supplement rather than a high-risk pharmaceutical.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.43%) for Biotin in dyspepsia, but this score does not correspond to clinical evidence — both retrieved clinical trials are false-positive matches, and no controlled study has specifically tested Biotin as a therapeutic agent for dyspepsia. The mechanistic rationale is theoretically coherent (cofactor role in gut metabolism, microbiome interactions, epithelial barrier modulation) but remains unvalidated. With evidence level L4 and no India market presence, this candidate is not ready for clinical translation.

**To proceed, the following would be needed:**

- **Mechanistic validation**: Preclinical studies (in vitro / animal models) directly testing Biotin supplementation in dyspepsia models, including functional dyspepsia and gastroparesis
- **Human pilot data**: A prospective observational or open-label pilot study assessing Biotin status and GI symptom correlation in dyspepsia patients
- **Dose-response clarification**: Distinction between physiological supplementation doses (µg/day) and pharmacological doses (e.g., high-dose MD1003 used in neurological research), since the therapeutic hypothesis may require supratherapeutic dosing
- **Regulatory pathway assessment**: Determine whether the relevant submission would proceed under a drug or functional food/nutraceutical regulatory framework in India
- **Safety package**: Formal retrieval of package insert warnings and contraindications data from a regulatory source, particularly if high-dose Biotin is being evaluated (high-dose Biotin is known to interfere with immunoassay-based laboratory tests, a clinically significant concern)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

