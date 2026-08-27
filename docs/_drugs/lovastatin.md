---
layout: default
title: Lovastatin
parent: 僅模型預測 (L5)
nav_order: 398
evidence_level: L5
indication_count: 6
---

# Lovastatin
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

# Lovastatin: From Hypercholesterolemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Lovastatin is an HMG-CoA reductase inhibitor, widely used as first-line therapy for primary hypercholesterolemia and cardiovascular risk reduction.
The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia (HoFH)**,
with **3 clinical trials** and **19 publications** currently supporting this direction — however, mechanistic analysis reveals critical limitations specific to this genetically severe patient subgroup.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Primary hypercholesterolemia (HMG-CoA reductase inhibitor class; India regulatory data unavailable) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L3 |
| India Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the regulatory database. Based on established pharmacology, Lovastatin inhibits HMG-CoA reductase — the rate-limiting enzyme in hepatic cholesterol biosynthesis. This causes a compensatory upregulation of LDL receptor (LDLR) expression on liver cells, accelerating clearance of plasma LDL-cholesterol. In heterozygous FH (HeFH), one functional LDLR allele remains, and Lovastatin can upregulate it effectively to reduce LDL-C by 25–40%. This is the drug's core pharmacological mechanism.

In **homozygous FH (HoFH)**, however, both LDLR alleles carry loss-of-function mutations. Functional receptor activity is severely diminished or entirely absent. As a result, the principal therapeutic mechanism of Lovastatin — receptor upregulation — is rendered largely ineffective. Direct clinical evidence confirms this: a prospective study (PMID 3397806) in three receptor-negative HoFH children demonstrated **no reduction in LDL-C concentration or turnover** during Lovastatin therapy at 2 mg/kg/day.

The TxGNN model's high prediction score most likely reflects the topological proximity of Lovastatin to the HoFH node within the lipid metabolism knowledge graph, rather than genuine clinical efficacy. A meaningful exception exists: patients with residual receptor activity (receptor-defective or compound heterozygous genotypes) may derive limited, genotype-dependent benefit from Lovastatin — particularly when combined with LDL apheresis or additional agents. Phenotypic receptor activity, therefore, is the critical determinant.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab (PCSK9 inhibitor) in HoFH children aged 8–17 years on background therapy including statins; evaluates LDL-C reduction at weeks 12, 24, and 48 — provides disease-context evidence but no Lovastatin-specific efficacy data |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | Long-term open-label safety of ezetimibe co-administered with atorvastatin or simvastatin in HoFH over 24 months; demonstrates statin class-level tolerability in this population |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Double-blind RCT of ezetimibe 10 mg added to atorvastatin or simvastatin in HoFH patients; modest LDL-C lowering observed — supports statin combination approach in patients with residual LDLR activity |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [12034651](https://pubmed.ncbi.nlm.nih.gov/12034651/) | 2002 | RCT | *Circulation* | Multicenter double-blind RCT (n=50): ezetimibe + atorvastatin or simvastatin in HoFH; confirms modest statin-based LDL-C lowering; highlights pharmacological limitations in receptor-deficient patients |
| [3397806](https://pubmed.ncbi.nlm.nih.gov/3397806/) | 1988 | Prospective Clinical Study | *Journal of Pediatrics* | **Critical negative finding**: Lovastatin (2 mg/kg/day) in 3 receptor-negative HoFH children — no decrease in LDL-C levels or LDL turnover rates; directly demonstrates drug inefficacy in LDLR-null phenotype |
| [7229037](https://pubmed.ncbi.nlm.nih.gov/7229037/) | 1981 | In Vitro / Mechanistic | *Journal of Clinical Investigation* | Compactin (structurally related statin) in HoFH fibroblasts: receptor-negative cells showed zero LDLR response; receptor-defective cells showed partial upregulation — mechanistically explains the genotype-dependent response |
| [3534334](https://pubmed.ncbi.nlm.nih.gov/3534334/) | 1986 | Case Report | *JAMA* | After liver transplantation restored ~60% LDLR activity in an HoFH child, Lovastatin normalised cholesterol levels — directly confirms that LDLR functional capacity governs statin responsiveness |
| [29284604](https://pubmed.ncbi.nlm.nih.gov/29284604/) | 2018 | Cohort Study | *Arteriosclerosis, Thrombosis, and Vascular Biology* | HoFH patients with identical LDLR mutations show variable residual LDLR expression; variable response to PCSK9 inhibition and by extension to statins; underscores need for phenotypic receptor assessment |
| [1785747](https://pubmed.ncbi.nlm.nih.gov/1785747/) | 1991 | Retrospective Study | *Anales Españoles de Pediatría* | Lovastatin combined with probucol and cholestyramine in 2 HoFH patients (receptor-defective); partial cholesterol reduction observed — suggests limited but measurable benefit in non-null genotypes |
| [2209665](https://pubmed.ncbi.nlm.nih.gov/2209665/) | 1990 | Clinical Study | *European Journal of Pediatrics* | LDL plasmapheresis (HELP) combined with Lovastatin in a 7-year-old HoFH girl; Lovastatin addition provided marginal incremental LDL reduction above apheresis alone, with regression of xanthomata |
| [2252289](https://pubmed.ncbi.nlm.nih.gov/2252289/) | 1990 | Clinical Study | *Anales Españoles de Pediatría* | Cholestyramine + Lovastatin combination in a receptor-defective HoFH patient; promising LDL-C reduction — consistent with residual LDLR activity hypothesis |
| [29233637](https://pubmed.ncbi.nlm.nih.gov/29233637/) | 2018 | Case Report | *Journal of Clinical Lipidology* | Compound heterozygous FH in a Chinese child with de novo and inherited LDLR mutations; highlights genotypic heterogeneity within the HoFH spectrum and its implications for treatment selection |
| [10146648](https://pubmed.ncbi.nlm.nih.gov/10146648/) | 1993 | Clinical Study | *Transfusion Science* | Long-term plasma exchange and LDL-apheresis ± simvastatin in 2 HoFH girls over 7 years; statin addition to apheresis provided incremental LDL-C benefit in selected patients |

---

## India Market Information

Lovastatin currently has **no registered products** in the India regulatory database.

> No authorisation records were found. The drug is not marketed in this jurisdiction based on available regulatory data.

---

## Safety Considerations

**Drug Interactions (247 total interactions identified):**

The following represent the highest-priority interactions clinicians should be aware of:

| Interacting Drug | Severity | Clinical Relevance |
|-----------------|----------|--------------------|
| Clarithromycin | **Major** | Strong CYP3A4 inhibitor; markedly increases lovastatin plasma exposure — significantly elevated risk of myopathy and rhabdomyolysis; avoid concomitant use |
| Miconazole | Moderate | Azole antifungal inhibits CYP3A4 metabolism of lovastatin; monitor for muscle toxicity |
| Clotrimazole | Moderate | Similar CYP3A4 inhibition mechanism; use with caution |
| Simvastatin | Moderate | Additive statin-related myopathy risk; concurrent use generally avoided |
| Rosuvastatin | Moderate | Additive myopathy risk with dual-statin regimens |
| Troglitazone | Moderate | May reduce lovastatin efficacy; clinical monitoring advised |
| Aprepitant | Moderate | Moderate CYP3A4 inhibitor; may increase lovastatin levels |
| Omeprazole / Esomeprazole / Lansoprazole / Pantoprazole | Moderate | PPI-class interactions; monitor lipid control |
| Metronidazole / Tinidazole | Moderate | Monitor for adverse events during co-administration |
| Exenatide | Minor | Minimal clinical impact; routine monitoring sufficient |

> Key warnings and contraindications were not available in the current dataset. Please refer to the package insert for complete safety information before clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although Lovastatin has strong, well-validated efficacy in heterozygous FH (L1 evidence, confirmed by multiple RCTs and a direct Phase 2/3 trial), its application in **homozygous FH** is mechanistically constrained: the drug's therapeutic action is dependent on functional LDL receptors, which are severely deficient or absent in most HoFH patients. Direct Lovastatin data (PMID 3397806) confirms lack of efficacy in receptor-negative patients, and the TxGNN high score reflects lipid metabolic pathway topology rather than actionable clinical evidence. A "Hold" is warranted until receptor phenotyping data can stratify patients who might benefit.

**To proceed, the following is needed:**
- **Genotypic and phenotypic characterisation** of the target HoFH patient population — residual LDLR activity (receptor-defective vs. receptor-negative genotype) is the single most important determinant of potential Lovastatin benefit
- **Mechanism of action data** from DrugBank to formally document pharmacological rationale in the evidence record
- **India regulatory (CDSCO) package insert** for key warnings and contraindications to support safety evaluation (currently a blocking data gap)
- **Consider pivoting focus** to the Rank 2 indication (**Hyperlipoproteinemia**, Evidence Level L1, decision "Proceed with Guardrails") or Rank 4 (**Familial Hypercholesterolemia**, Evidence Level L1, decision "Proceed with Guardrails"), where both mechanistic plausibility and direct Lovastatin RCT evidence are substantially stronger
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

