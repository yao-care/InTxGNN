---
layout: default
title: Roxatidine Acetate
parent: Model Prediction Only (L5)
nav_order: 756
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Roxatidine Acetate: predicted new indication Active peptic ulcer disease (evidence level L5). Approved use: Gastric ulcer, gastroesophageal reflux disease, esophagitis…"
monitor_inn: "Roxatidine acetate"
predicted_indications: ["peptic ulcer perforation", "gastroduodenitis", "duodenal obstruction"]
---

# Roxatidine Acetate
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

# Roxatidine Acetate: From Gastric Ulcer to Active Peptic Ulcer Disease

## One-Sentence Summary

Roxatidine acetate is a histamine H2-receptor antagonist originally used to treat gastric ulcer, reflux disease and related acid-related disorders.
The TxGNN model predicts it may be effective for **active peptic ulcer disease**, which is closely aligned with its existing uses.
No clinical trials are registered for this indication, but **14 publications** (including randomized trials and reviews) support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric ulcer, gastroesophageal reflux disease, esophagitis, Zollinger-Ellison syndrome (the licence entries in India carry no indication text) |
| Predicted New Indication | Active peptic ulcer disease |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L1 (based on randomized controlled trials in the literature; see note below) |
| India Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Proceed with Guardrails |

*Note: Peptic ulcer disease is essentially an on-label use, so this is not a true repurposing. The L1 grade rests on published double-blind RCTs rather than registered trials, and the grade is moderately uncertain.*

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on the published literature, roxatidine acetate is a histamine H2-receptor antagonist. It is almost completely absorbed after oral dosing (more than 95%) and is rapidly converted to its active metabolite, roxatidine. Roxatidine inhibits basal and stimulated gastric acid secretion by blocking H2 receptors on gastric parietal cells.

Peptic ulcers develop when acid and other aggressive factors overwhelm the protective defences of the stomach and duodenal lining. Reducing acid lets the ulcer heal. The drug's original indications (gastric ulcer, reflux disease, esophagitis) rely on the same acid-suppression effect, so the predicted indication follows directly from its known mechanism.

Preclinical work in rats also suggests a cytoprotective effect on the gastric mucosa, which may add to the benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1674231](https://pubmed.ncbi.nlm.nih.gov/1674231/) | 1991 | RCT | Clin Ther | Two double-blind placebo-controlled studies (725 patients) of 75 mg at night as 12-month maintenance therapy after ulcer healing, in duodenal and gastric ulcer |
| [1717223](https://pubmed.ncbi.nlm.nih.gov/1717223/) | 1991 | Review | Drugs | Pharmacology and therapeutic potential in peptic ulcer disease; near-complete oral absorption, potent acid inhibition, no anti-androgenic effects |
| [2906456](https://pubmed.ncbi.nlm.nih.gov/2906456/) | 1988 | Review | Scand J Gastroenterol Suppl | 150 mg at bedtime was optimal for suppressing nocturnal acid secretion |
| [2184124](https://pubmed.ncbi.nlm.nih.gov/2184124/) | 1990 | Review | Gastroenterol Clin North Am | Roxatidine and nizatidine described as safe and effective H2 blockers without new clinically important properties |
| [2905237](https://pubmed.ncbi.nlm.nih.gov/2905237/) | 1988 | Review | Drugs | Role of prostaglandins and H2-receptor antagonists in peptic ulcer disease |
| [8097411](https://pubmed.ncbi.nlm.nih.gov/8097411/) | 1993 | Review | Baillieres Clin Gastroenterol | Pharmacology of gastric acid regulation and inhibition |
| [2906472](https://pubmed.ncbi.nlm.nih.gov/2906472/) | 1988 | Review | Scand J Gastroenterol Suppl | Drug-interaction mechanisms; roxatidine acts differently on hepatic enzymes than cimetidine and ranitidine |
| [2906796](https://pubmed.ncbi.nlm.nih.gov/2906796/) | 1988 | Preclinical | Arch Int Pharmacodyn Ther | Cytoprotective action against experimental gastric mucosal lesions |
| [26883979](https://pubmed.ncbi.nlm.nih.gov/26883979/) | 2016 | Animal study | Life Sci | Gastroprotective effects of several H2 blockers on ibuprofen-induced gastric ulcer in rats |

## India Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| 250522 | Zorpex 75mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 14 tablets | Not specified |
| 251681 | Zorpex 150mg Tablet (Sun Pharmaceutical Industries Ltd) | Strip of 14 tablets | Not specified |
| 189348 | Rotane Forte Tablet (Sanofi India Ltd) | Strip of 10 tablets | Not specified |
| 188497 | Rotane 75mg Tablet (Sanofi India Ltd) | Strip of 14 tablets | Not specified |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Peptic ulcer disease is an established use of this H2-receptor antagonist, and the published randomized trials and reviews support it. Because no trials are registered and the safety label data could not be obtained, the evidence grade is moderately uncertain and the decision should carry guardrails.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Indian marketed products (currently missing, and this blocks safety screening)
- Confirmed mechanism of action data from DrugBank
- Approved indication text for the four Indian registrations
- Comparison with proton pump inhibitors as the current standard of care

---

### Other Predicted Indications (Brief Note)

| Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|
| Gastrojejunal ulcer | 99.55% | L1 (indirect; trials are in gastric/duodenal ulcer and reflux esophagitis, so this is an extrapolation) | Proceed with Guardrails |
| Gastroduodenitis | 99.28% | L4 (indirect evidence from NSAID-induced lesion prevention) | Research Question |
| Peptic ulcer perforation | 99.55% | L5 | Hold |
| Duodenogastric reflux | 99.21% | L5 | Hold |
| Duodenal obstruction | 99.09% | L5 | Hold |

For gastrojejunal ulcer, guardrails include confirming the diagnosis, checking for H. pylori and NSAID causes, and considering a PPI as the standard comparator. Several head-to-head randomized trials against ranitidine exist for duodenal ulcer (PMIDs 2905255, 1679668), gastric ulcer (2905240) and reflux esophagitis (8100189), but none are specific to post-surgical marginal ulcer.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

