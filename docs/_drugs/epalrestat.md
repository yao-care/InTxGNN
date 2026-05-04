---
layout: default
title: Epalrestat
parent: 僅模型預測 (L5)
nav_order: 233
evidence_level: L5
indication_count: 10
---

# Epalrestat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Epalrestat: From Diabetic Peripheral Neuropathy to Type 2 Diabetes Nephropathy

## One-Sentence Summary

Epalrestat is an aldose reductase inhibitor (ARI) approved in several Asian countries for diabetic peripheral neuropathy.
The TxGNN model predicts it may be effective for **Type 2 Diabetes Nephropathy**,
with **0 registered clinical trials** and **5 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diabetic peripheral neuropathy |
| Predicted New Indication | Type 2 Diabetes Nephropathy |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism of action data was not retrieved in this evidence pack. Based on available literature, Epalrestat is an aldose reductase inhibitor (ARI) that blocks the polyol pathway — the enzymatic conversion of glucose to sorbitol (and subsequently to fructose) — by competitively inhibiting the aldose reductase enzyme. This reduces intracellular sorbitol accumulation, NADPH depletion, and downstream oxidative stress. Because this mechanism directly targets the molecular driver of diabetic peripheral neuropathy, Epalrestat is already approved for that indication in India, China, and Japan.

The mechanistic connection to diabetic nephropathy is strong and biologically coherent: the same polyol pathway is active in renal tubular and glomerular cells under chronic hyperglycemia. Sorbitol accumulation in these cells promotes osmotic stress and drives the overproduction of advanced glycation end products (AGEs). AGEs then bind to RAGE receptors on mesangial cells, triggering pro-fibrotic signaling cascades — glomerular basement membrane thickening, mesangial expansion, and tubular fibrosis — which are the defining pathological events in diabetic nephropathy.

Clinical evidence reinforces this link: a 5-year prospective study (PMID 11522497) showed epalrestat preserved renal function in type 2 diabetic patients with microalbuminuria, and separate work (PMID 12792982) confirmed epalrestat reduces circulating AGE levels. The mechanistic overlap between the established neuropathy indication and the predicted nephropathy indication is therefore not coincidental — both arise from the same upstream polyol pathway dysregulation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov or ICTRP for the Epalrestat × Type 2 Diabetes Nephropathy combination.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11522497](https://pubmed.ncbi.nlm.nih.gov/11522497/) | 2001 | Prospective Controlled Trial | J Diabetes Complications | 5-year study in type 2 diabetic patients with microalbuminuria: epalrestat 150 mg/day significantly slowed progression of incipient diabetic nephropathy compared with matched controls |
| [39423107](https://pubmed.ncbi.nlm.nih.gov/39423107/) | 2024 | Clinical Study | Iranian J Kidney Diseases | Built a diagnostic risk prediction model for DN in type 2 diabetes and evaluated therapeutic outcomes of combined epalrestat + dapagliflozin; combination showed additive renoprotective effect |
| [12792982](https://pubmed.ncbi.nlm.nih.gov/12792982/) | 2003 | Clinical/Mechanistic Study | In Vivo | Epalrestat administration significantly reduced plasma AGE levels in type 2 diabetic patients, providing direct mechanistic evidence for its anti-AGE, anti-fibrotic renal action |
| [9571366](https://pubmed.ncbi.nlm.nih.gov/9571366/) | 1998 | Pharmacodynamic Study | Diabetes Care | Demonstrated that epalrestat measurably reduces erythrocyte sorbitol concentrations in diabetic patients with complications, confirming target engagement of polyol pathway inhibition |
| [41830794](https://pubmed.ncbi.nlm.nih.gov/41830794/) | 2026 | Review/Hypothesis | Medical Gas Research | Proposes the "glycohypoxia" framework — chronic hyperglycemia induces functional cellular hypoxia that drives diabetic complications including nephropathy; contextualizes ARI therapy within a hypoxia-centric pathophysiology |

---

## India Market Information

Epalrestat currently has **no registered products** in the Indian CDSCO database according to this Evidence Pack (0 authorizations on record). The India market status is listed as not marketed.

> **Data Note**: Independent sources indicate that Epalrestat-containing products are commercially available in India (e.g., for diabetic neuropathy). The zero-registration result likely reflects a data collection gap rather than true absence from the market. Direct verification via the CDSCO online drug database is strongly recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic case for Epalrestat in diabetic nephropathy is strong — it targets the same polyol pathway that drives both peripheral neuropathy (its approved indication) and renal mesangial/tubular injury. A prospective controlled trial and multiple clinical/mechanistic studies provide L2-level human evidence, making this among the most credible repurposing candidates in this analysis.

**To proceed, the following is needed:**

- **Formal MOA data**: Retrieve complete DrugBank pharmacology record (DB15293) to document the MOA and known targets for regulatory submissions
- **CDSCO safety data**: Download and parse the Indian package insert PDF to extract boxed warnings, contraindications, and special population guidance (currently a blocking data gap)
- **Drug interaction profile**: Resolve the DDinter file path error and complete the DDI lookup, particularly for common co-medications in type 2 diabetic patients (metformin, ACE inhibitors, SGLT2 inhibitors)
- **Prospective RCT confirmation**: The 2001 prospective study (PMID 11522497) predates modern nephropathy outcome standards; a contemporary Phase 2/3 RCT with UACR and eGFR endpoints is needed to support a formal label extension
- **India registration status verification**: Confirm actual CDSCO registration status and retrieve approved indication text to assess whether off-label use would be needed or whether an indication expansion filing is the appropriate pathway
- **Combination therapy data**: The 2024 study (PMID 39423107) on epalrestat + dapagliflozin combination warrants closer review, given the widespread use of SGLT2 inhibitors in diabetic nephropathy

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

