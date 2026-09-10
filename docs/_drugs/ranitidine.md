---
layout: default
title: Ranitidine
parent: 僅模型預測 (L5)
nav_order: 719
evidence_level: L5
indication_count: 10
---

# Ranitidine
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

# Ranitidine: From Peptic Ulcer Disease to Active Peptic Ulcer Disease

## One-Sentence Summary

Ranitidine is a histamine H2-receptor antagonist historically used to reduce gastric acid secretion in peptic ulcer disease. The TxGNN model's top-ranked prediction is **Active Peptic Ulcer Disease** — which is essentially the drug's own long-standing core indication rather than a genuinely new use — supported by **1 clinical trial** (of limited direct relevance) and **20 publications**, several of which are randomized controlled trials from ranitidine's original development era.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the India regulatory dataset (no active license on file); historically approved worldwide as an H2-antagonist for peptic ulcer disease / GERD |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal DrugBank mechanism-of-action text is not yet available in this dataset. However, the evidence pack's own mechanistic annotations are unambiguous: ranitidine is a competitive **H2-receptor antagonist** that blocks histamine-stimulated gastric acid secretion at the parietal cell, the same mechanism that underlies decades of use in treating duodenal and gastric ulcers.

This is an important caveat for interpreting the prediction: "active peptic ulcer disease" is not a *new* therapeutic area for ranitidine — it is the disease family the drug was originally developed and marketed for (see also rank #7 in the full candidate list, "peptic ulcer disease," which the model itself flags as "not repurposing, but the original core indication"). The high TxGNN score therefore reflects re-identification of a well-established drug–disease relationship embedded in the knowledge graph, rather than a novel repositioning hypothesis.

The mechanistic plausibility is nonetheless real and well documented: multiple historical RCTs (1980s–1990s) directly demonstrate ranitidine's efficacy in healing active duodenal and gastric ulcers, often head-to-head against cimetidine, famotidine, and omeprazole. The key complicating factor is regulatory, not pharmacological — ranitidine is currently **unmarketed** following the 2020 global withdrawal after detection of NDMA (N-nitrosodimethylamine), a probable human carcinogen, in multiple manufacturers' products.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Evaluated PPI/statin interference with clopidogrel antiplatelet effect in PCI patients; ranitidine was not the primary study drug — **low direct relevance** (relevance grade C) to active peptic ulcer disease treatment. |

No trial in this evidence pack directly tests ranitidine as an intervention for active peptic ulcer disease; supporting evidence for efficacy comes from the literature below.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3909374](https://pubmed.ncbi.nlm.nih.gov/3909374/) | 1985 | RCT | Scand J Gastroenterol | Ranitidine 300mg/day: 91% healing at 4 wks for duodenal ulcer; maintenance therapy reduced relapse vs placebo over 1 year (n=108) |
| [2491360](https://pubmed.ncbi.nlm.nih.gov/2491360/) | 1989 | RCT | J Gastroenterol Hepatol | Double-blind trial (n=270): omeprazole vs ranitidine 150mg BID for duodenal ulcer healing and relapse prevention, weekly endoscopic assessment |
| [2877570](https://pubmed.ncbi.nlm.nih.gov/2877570/) | 1986 | RCT | Am J Med | Multicenter international study (n=1,031, 19 countries): famotidine vs ranitidine for active duodenal ulcer healing |
| [1863945](https://pubmed.ncbi.nlm.nih.gov/1863945/) | 1991 | RCT | Clin Ther | Famotidine vs ranitidine in 160 patients with endoscopically confirmed active duodenal ulcer, including NSAID/aspirin-related ulcers, plus 6-month maintenance |
| [2092029](https://pubmed.ncbi.nlm.nih.gov/2092029/) | 1990 | RCT | J Assoc Physicians India | Double-blind trial (n=40): famotidine 40mg vs ranitidine 300mg nocturnal dosing for active gastric/duodenal ulcer |
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Review | Drug Intell Clin Pharm | Foundational review confirming FDA approval of ranitidine for short-term treatment of active duodenal ulcer and hypersecretory conditions |
| [1976583](https://pubmed.ncbi.nlm.nih.gov/1976583/) | 1990 | Review | Hepato-gastroenterology | Reviews acid suppression as the mechanistic driver of peptic ulcer healing across H2-antagonists |
| [1717223](https://pubmed.ncbi.nlm.nih.gov/1717223/) | 1991 | Review | Drugs | Comparator H2RA (roxatidine) review contextualizing ranitidine's antisecretory potency and therapeutic positioning |
| [2905640](https://pubmed.ncbi.nlm.nih.gov/2905640/) | 1988 | Review | Drugs | Comparator H2RA (nizatidine) review referencing ranitidine as the established therapeutic benchmark |
| [12749277](https://pubmed.ncbi.nlm.nih.gov/12749277/) | 2003 | Controlled study | Hepato-gastroenterology | Ranitidine vs ranitidine+ecabet: inhibition of ulcer relapse independent of H. pylori eradication status |

---

## India Market Information

Ranitidine currently holds **no active regulatory registrations in India** (0 licenses on file; market status: Not Marketed). This is consistent with the global 2020 withdrawal after NDMA (a probable human carcinogen) was detected as a manufacturing/degradation impurity across multiple ranitidine product lines worldwide.

---

## Safety Considerations

- **Key Warnings**: Ranitidine was withdrawn from markets globally in 2020 due to detection of NDMA (N-nitrosodimethylamine), a probable human carcinogen, in finished products — this is a regulatory/manufacturing safety issue distinct from the drug's therapeutic efficacy, but it directly blocks current clinical availability.
- **Drug Interactions**: DDI database lists **585 total documented interactions**. Notable entries from the returned subset:

| Interacting Drug | Severity |
|---|---|
| Atazanavir | Major |
| Acalabrutinib | Moderate |
| Acetohexamide | Moderate |
| Aminophylline | Moderate |
| Bacampicillin | Moderate |
| Bosutinib | Moderate |
| Brigatinib | Moderate |
| Cefditoren / Cefpodoxime / Cefuroxime | Moderate |
| Ceritinib | Moderate |
| Chlorpropamide | Moderate |
| Acetaminophen, Alendronic acid, Aluminum hydroxide, Calcium carbonate, Cisapride, Atracurium, Cisatracurium, Axitinib | Minor |

Formal India (CDSCO) labeling warnings and contraindications have not yet been retrieved for this drug — this is flagged as a blocking data gap for full safety assessment (see Conclusion).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- The underlying pharmacology and historical RCT record (evidence level L2) strongly support ranitidine's efficacy in active peptic ulcer disease — but this is a rediscovery of the drug's own original indication, not a novel repurposing signal, so its value for a repurposing pipeline is limited. Other candidate indications in this evidence pack (gastrojejunal ulcer, gastroduodenitis — L3; peptic ulcer perforation, duodenogastric reflux, duodenal obstruction — L4; mastocytosis/glucagon-related predictions — L5) are progressively weaker and mostly mechanistic extrapolations without direct trial support.
- The dominant practical barrier is not efficacy but regulatory: ranitidine is unmarketed in India following the 2020 NDMA-contamination withdrawal.

**To proceed, the following is needed:**
- Retrieve formal CDSCO/India labeling (warnings, contraindications) — currently a blocking data gap (DG001)
- Retrieve formal DrugBank MOA documentation (DG002)
- Manufacturing quality/impurity certification (NDMA-free) before any relisting or clinical use is considered
- Clarify decision value: given rank #1 mirrors ranitidine's original indication, consider whether resources are better directed at the lower-confidence but genuinely novel candidates (e.g., gastrojejunal ulcer, gastroduodenitis)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

