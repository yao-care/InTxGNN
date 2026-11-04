---
layout: default
title: Vandetanib
parent: Moderate Evidence (L3-L4)
nav_order: 882
evidence_level: L3
indication_count: 10
last_modified_at: 2026-11-04
monitor_inn: "Vandetanib"
predicted_indications: ["renal cell carcinoma (disease)", "renal cell carcinoma associated with neuroblastoma", "unclassified renal cell carcinoma", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "renal pelvis carcinoma", "clear cell renal carcinoma", "childhood kidney cell carcinoma", "renal carcinoma", "angiolipoma", "familial spontaneous pneumothorax"]
description: "Vandetanib: predicted new indication Renal cell carcinoma (disease) (evidence level L3). Approved use: Not recorded in the local data"
---

# Vandetanib
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

## Vandetanib: Renal cell carcinoma (disease)
{: .text-alpha }

## One-Sentence Summary

Vandetanib is an oral multi-target kinase inhibitor that blocks VEGFR2, EGFR and RET.
The TxGNN model predicts it may be effective for **renal cell carcinoma (disease)**.
This direction is supported by **4 clinical trials** (all Phase 1/2 or Phase 2, two terminated early with very few patients) and **5 publications**, none of which show vandetanib efficacy in renal cell carcinoma. Evidence level: **L3**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Renal cell carcinoma (disease) |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L3 |
| India Market Status | Listed in a compiled Indian medicine price dataset (1 of 1) – CDSCO approval status is not included in this data |
| Number of Listed Products | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Vandetanib inhibits the VEGFR2, EGFR and RET tyrosine kinases. Detailed mechanism-of-action data were not available in the data compiled for this report, so the description above comes from the trial and literature records.

Clear cell renal cell carcinoma is often driven by loss of the VHL gene. This stabilises HIF and drives VEGF-dependent blood vessel growth. Blocking VEGFR2 targets this pathway directly. Approved VEGFR inhibitors such as sunitinib and pazopanib already validate the pathway in renal cell carcinoma. Rarer subtypes (FH-deficient and SDH-deficient tumours) may also respond to combined anti-angiogenic and EGFR-targeted therapy.

The caveat is that the trials are small, two were terminated early, and no efficacy results are provided in the data compiled for this report. The mechanistic rationale is plausible but unproven for vandetanib itself.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | Completed | 37 | Vandetanib in von Hippel-Lindau disease with renal tumours; mechanistically well aligned, no outcome data provided |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | Terminated | 7 | Vandetanib plus metformin in HLRCC- or SDH-associated kidney cancer or papillary renal cell carcinoma; hypothesis-generating only |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | Terminated | 3 | Vandetanib in advanced clear cell renal carcinoma; too few patients to interpret |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | Completed | 82 | Carboplatin and gemcitabine with or without vandetanib in advanced urothelial cancer; only indirectly relevant to renal cell carcinoma |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clin Exp Metastasis | Targeted and epigenetic approaches in metastatic FH-deficient renal cell carcinoma; several Phase 2 combination trials under way |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | Am Soc Clin Oncol Educ Book | Systemic therapy for advanced thyroid cancers, including vandetanib as a RET inhibitor |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review | OncoTargets Ther | Anti-angiogenic agents in solid tumours, including vandetanib |
| [42107510](https://pubmed.ncbi.nlm.nih.gov/42107510/) | 2026 | Review | Pharmacol Res | RET kinase inhibitors in RET-driven thyroid and lung cancer |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Preclinical (mouse model) | Mol Cancer Res | TFE3 translocation renal cell carcinoma mouse model; tangentially relevant |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 38486 | Caprelsa Tablet (AstraZeneca) | Bottle of 30 tablets (oral) | Indication text not provided |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Electrocardiogram (QT interval), electrolytes (potassium, calcium, magnesium), thyroid function, blood pressure, liver and renal function |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Conditions listed as contraindications or cautions in the drug-disease records:** hypertension, long QT syndrome (including familial forms), torsades de pointes, hypothyroidism, potassium deficiency, hypercalcaemia, impaired renal function, interstitial lung disease, heart failure, brain ischaemia or transient ischaemic attack, and posterior leukoencephalopathy syndrome. These are not taken from label text.
- **Drug interactions:** 296 interactions were found. Major-level ones include clarithromycin, levofloxacin, dolasetron, palonosetron, picosulfuric acid, sodium sulfate and polyethylene glycol with electrolytes. Moderate-level ones include famotidine, metformin, loperamide, dexamethasone, bisacodyl and lactitol. The major interactions are mostly QT-prolonging drugs or agents that shift electrolytes, which matters because vandetanib itself prolongs the QT interval.
- **Class-level safety literature:** meta-analyses of VEGFR inhibitors report liver toxicity, proteinuria and treatment-related mortality (PMIDs 23981115, 32105149, 22651902).

Package insert warnings and contraindications were not available; please refer to the package insert.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The strongest support is one completed Phase 2 trial in von Hippel-Lindau disease with renal tumours (NCT00566995). The other renal cell carcinoma trials were terminated early with very few patients, and no efficacy results are available. The mechanism is plausible, but the evidence supports further research only, not clinical use.

**To proceed, the following is needed:**
- Results from NCT00566995 and the other renal trials
- Package insert warnings and contraindications, with a cardiac (QT) and electrolyte monitoring plan
- Detailed mechanism-of-action data
- A properly powered Phase 2 study in clear cell renal cell carcinoma or VHL-associated tumours

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

