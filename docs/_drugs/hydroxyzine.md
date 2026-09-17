---
layout: default
title: Hydroxyzine
parent: Moderate Evidence (L3-L4)
nav_order: 412
evidence_level: L3
indication_count: 5
---

# Hydroxyzine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **5** 
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

# Hydroxyzine: From First-Generation Antihistamine to Allergic Urticaria

## One-Sentence Summary

Hydroxyzine is a first-generation H1-antihistamine; detailed original-indication licensing data is not available in this evidence pack, as the drug is currently **not marketed** in Taiwan (India regulatory field mirrors this). The TxGNN model predicts it may be effective for **Allergic Urticaria**, with **1 clinical trial** and **20 publications** currently supporting this direction, corresponding to an Evidence Level of **L3**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no license/label data in this evidence pack (drug not marketed) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L3 |
| India Market Status | Not Marketed (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold (pipeline-scored as "Research Question", decision stage S1) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for hydroxyzine is not available from DrugBank in this evidence pack. Based on the information that is available, hydroxyzine belongs to the **first-generation H1-antihistamine** class, and its evidence-pack rationale explicitly frames this prediction as an "indication extension within the same drug class."

Allergic urticaria is pathophysiologically driven by mast-cell histamine release acting on peripheral H1 receptors, producing the wheal-and-flare reaction. H1-receptor blockade — the defining pharmacology of first-generation antihistamines such as hydroxyzine — directly targets this mechanism, which is why the TxGNN prediction is mechanistically plausible even without a confirmatory hydroxyzine-specific trial.

Supporting this further, a closely related TxGNN-predicted indication for the same drug, **cold urticaria** (rank 3), carries stronger evidence (L2, "Proceed with Guardrails") and includes literature directly comparing hydroxyzine against other antihistamines in physical urticaria. This lends indirect but meaningful corroboration to the pharmacological plausibility of the allergic urticaria prediction, even though the allergic urticaria evidence itself is largely class-level (cetirizine/levocetirizine, both hydroxyzine metabolites/relatives) rather than hydroxyzine-specific.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Multicenter pilot RCT comparing IV cetirizine vs. IV diphenhydramine for acute urticaria in ED/urgent care settings. Relevance graded **B**: a feasibility pilot study of a related antihistamine, not a direct hydroxyzine confirmatory trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Guideline/Position statement | Allergy Asthma Clin Immunol | CSACI statement explicitly naming hydroxyzine among first-generation antihistamines used for urticaria, noting sedation/safety concerns vs. newer agents |
| [28913986](https://pubmed.ncbi.nlm.nih.gov/28913986/) | 2017 | Review | Allergy Asthma Immunol Res | Chronic spontaneous urticaria treatment algorithm; explicitly lists hydroxyzine (Atarax) as historical high-dose first-line therapy before omalizumab |
| [21793329](https://pubmed.ncbi.nlm.nih.gov/21793329/) | 2010 | Cohort/Clinical study | Chin J Physiol | Taiwanese multicentre observational study of levocetirizine (cetirizine-class) in allergic rhinitis/urticaria (N=333) |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Review | Drugs | Review of cetirizine — the carboxylated hydroxyzine metabolite — in allergic rhinitis and chronic urticaria |
| [11034010](https://pubmed.ncbi.nlm.nih.gov/11034010/) | 2000 | Case report | J Clin Gastroenterol | Case of cetirizine-induced cholestasis; cetirizine noted as a hydroxyzine human metabolite |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | Review | Clin Pharmacokinet | Comparative PK/PD review of desloratadine, fexofenadine, levocetirizine for allergic disease |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Review of oral antihistamines for allergic rhinitis and chronic idiopathic urticaria |
| [18201439](https://pubmed.ncbi.nlm.nih.gov/18201439/) | 2007 | Review | Allergy Asthma Proc | Review of levocetirizine for allergic rhinitis and chronic idiopathic urticaria |
| [19808127](https://pubmed.ncbi.nlm.nih.gov/19808127/) | 2009 | Review | Clin Ther | Review of levocetirizine efficacy/safety for allergic rhinitis and chronic idiopathic urticaria |
| [22686617](https://pubmed.ncbi.nlm.nih.gov/22686617/) | 2012 | Review | Drugs | Review of bilastine (second-generation antihistamine) in allergic rhinitis and urticaria |

---

## India Market Information

No registration records are present in this evidence pack — hydroxyzine's market status is **"Not marketed" (Not Marketed)** with 0 total licenses recorded.

---

## Safety Considerations

- **Drug Interactions**: Hydroxyzine has 297 recorded interactions in the DDI database. Notable **Major**-level interactions include Morphine, Potassium citrate, and Dolasetron. **Moderate**-level interactions include Famotidine, Hyoscyamine, Loperamide, Atropine, Bisacodyl, Clarithromycin, Picosulfuric acid, Polyethylene glycol (3350 with electrolytes), Dicyclomine, Dronabinol, Eluxadoline, Palonosetron, Trospium, Sodium sulfate, Nabilone, and Levofloxacin. A **Minor**-level interaction is noted with Cimetidine.

Key warnings and contraindications are not available in this evidence pack (blocked by data gap DG001 — TFDA label warnings/contraindications not yet retrieved).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence-pack's own scoring for this indication (decision stage S1, recommendation "Research Question") reflects that supporting evidence is largely class-level (cetirizine/levocetirizine literature) rather than hydroxyzine-specific, and the single relevant clinical trial is graded only Grade B relevance (indirect comparator study, not a hydroxyzine RCT). Critically, data gap DG001 (TFDA warnings/contraindications) is flagged as **Blocking**, meaning this candidate cannot yet complete the S1 safety pre-assessment.

**To proceed, the following is needed:**
- TFDA label PDF (warnings, contraindications) to resolve blocking data gap DG001
- DrugBank mechanism-of-action data to resolve data gap DG002 and strengthen the mechanistic rationale
- A hydroxyzine-specific (not class-level) clinical trial or observational study in allergic urticaria
- Consider prioritizing the sibling candidate **cold urticaria** (L2, "Proceed with Guardrails"), which currently has stronger direct evidence for the same drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

