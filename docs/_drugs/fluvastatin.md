---
layout: default
title: Fluvastatin
parent: High Evidence (L1-L2)
nav_order: 371
evidence_level: L1
indication_count: 10
---

# Fluvastatin
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Fluvastatin: From Hypercholesterolemia (Unlicensed in India) to Hyperlipoproteinemia

## One-Sentence Summary

Fluvastatin is an HMG-CoA reductase inhibitor (statin) already used internationally to treat hypercholesterolemia and familial hypercholesterolemia, but it currently holds **no market authorization in India**. The TxGNN model's top-ranked prediction — **Hyperlipoproteinemia** — closely mirrors this well-established statin use, supported by **5 clinical trials** and **20 publications**, several of which test fluvastatin directly.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file in this evidence pack — no India license or original-indication text is recorded. Trial/literature evidence (e.g., NCT00171236, NCT00726362) confirms fluvastatin's established global use for hypercholesterolemia/familial hypercholesterolemia. |
| Predicted New Indication | Hyperlipoproteinemia |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| India Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for fluvastatin is not available in this evidence pack (flagged as a High-severity data gap requiring DrugBank API lookup). Based on the pharmacological context captured in the repurposing rationale, fluvastatin acts through the standard statin mechanism — reducing LDL cholesterol and apolipoprotein B — and has been the subject of numerous direct trials in hyperlipidemia and mixed hyperlipoproteinemia.

The predicted indication, hyperlipoproteinemia, is mechanistically and clinically almost synonymous with fluvastatin's known therapeutic role: multiple RCTs in the evidence set (e.g., the FACT study, PMID 10856536) test fluvastatin directly — alone or combined with bezafibrate/fenofibrate — in patients with mixed hyperlipidaemia. This means the TxGNN signal here largely **confirms an already-established drug class use** rather than identifying a genuinely novel off-label application, which strengthens confidence in the model's output but tempers its novelty value for this specific candidate.

Because fluvastatin is not currently licensed in India, the practical value of this prediction lies less in discovering a new indication and more in supporting a potential India market-entry/registration case for a globally validated lipid-lowering therapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00532311](https://clinicaltrials.gov/study/NCT00532311) | Phase 3 | Terminated | 411 | Lapaquistat acetate (not fluvastatin) added to statin therapy for hypercholesterolemia; terminated. |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Alirocumab (PCSK9 inhibitor, not fluvastatin) in pediatric homozygous familial hypercholesterolemia. |
| [NCT04608474](https://clinicaltrials.gov/study/NCT04608474) | Phase 4 | Unknown | 120 | Evolocumab pilot study for hyperlipidemia in renal transplant recipients; different drug class. |
| [NCT00726362](https://clinicaltrials.gov/study/NCT00726362) | N/A | Completed | 3270 | Large real-world survey comparing commercially available statins, including fluvastatin, in hyperlipidemia patients. |
| [NCT01634906](https://clinicaltrials.gov/study/NCT01634906) | N/A | Completed | 55 | Non-randomized study on erythrocyte-bound apolipoprotein B changes after statin withdrawal. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10856536](https://pubmed.ncbi.nlm.nih.gov/10856536/) | 2000 | RCT | Atherosclerosis | FACT study: fluvastatin + bezafibrate combination effective and safe in mixed hyperlipidaemia (n=333). |
| [11219479](https://pubmed.ncbi.nlm.nih.gov/11219479/) | 2001 | RCT | Clinical Therapeutics | Fluvastatin extended-release vs. immediate-release formulation compared for primary hypercholesterolemia. |
| [15598476](https://pubmed.ncbi.nlm.nih.gov/15598476/) | 2004 | RCT | Clinical Therapeutics | 12-month RCT: fluvastatin+fenofibrate vs. fluvastatin monotherapy in combined hyperlipidemia with T2DM and CHD. |
| [8192170](https://pubmed.ncbi.nlm.nih.gov/8192170/) | 1994 | RCT | Am J Medicine | Fluvastatin-bezafibrate vs. fluvastatin-cholestyramine combinations compared in familial hypercholesterolemia. |
| [9271817](https://pubmed.ncbi.nlm.nih.gov/9271817/) | 1997 | Cohort | Thrombosis Research | Fluvastatin's effect on tissue factor pathway inhibitor in type IIa/IIb hyperlipidemia and post-MI patients. |
| [7604804](https://pubmed.ncbi.nlm.nih.gov/7604804/) | 1995 | Open-label | Am J Cardiology | High-dose fluvastatin ± bezafibrate in severe heterozygous familial hypercholesterolemia. |
| [7604807](https://pubmed.ncbi.nlm.nih.gov/7604807/) | 1995 | Open-label | Am J Cardiology | Triple therapy (fluvastatin-bezafibrate-cholestyramine) for severe familial hypercholesterolemia. |
| [8157036](https://pubmed.ncbi.nlm.nih.gov/8157036/) | 1993 | Double-blind | Eur J Clin Pharmacol | High-dose fluvastatin efficacy/safety in 52 patients with familial hypercholesterolaemia. |
| [17062478](https://pubmed.ncbi.nlm.nih.gov/17062478/) | 2006 | Clinical study | Acta Paediatrica | Fluvastatin efficacy and safety in children/adolescents with heterozygous familial hypercholesterolaemia. |
| [7517835](https://pubmed.ncbi.nlm.nih.gov/7517835/) | 1994 | Open study | Drugs | Fluvastatin efficacy, safety, and tolerability in elderly hypercholesterolaemic women. |

---

## India Market Information

Fluvastatin is **not currently licensed or marketed in India** — the evidence pack records zero registrations and no license entries.

---

## Safety Considerations

- **Drug Interactions**: The DDI database records **159 total interactions** for fluvastatin. Among the sample returned, the following are flagged as **Moderate**-level interactions requiring clinical attention: Aprepitant, Metronidazole, Oxandrolone, Naltrexone, Nateglinide, Nitisinone, Rosuvastatin, Simvastatin, Tinidazole, Glyburide, and Pectin. Additional interactions with Calcitriol, Doxycycline, Cimetidine, Epinephrine, Mannitol, Dicyclomine, Famotidine, Acetylsalicylic acid, and Pantoprazole are on record with unclassified severity. Separately, literature evidence (PMID 23703578, PMID 19838098) highlights a clinically relevant CYP-mediated interaction between statins and HIV protease inhibitors, relevant to any HIV-related lipid-management use of fluvastatin.

Package insert warnings and contraindications are not currently available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The predicted indication (hyperlipoproteinemia) is supported by L1-level evidence, including multiple direct fluvastatin RCTs, and effectively reconfirms an established statin indication rather than a novel use. However, fluvastatin holds no current India market authorization, and core safety data (warnings, contraindications) are missing, which blocks a full safety assessment.

**To proceed, the following is needed:**
- TFDA/India package insert data — key warnings and contraindications (currently a Blocking data gap, DG001)
- Confirmed mechanism of action via DrugBank API (High-severity data gap, DG002)
- An India regulatory pathway/licensing assessment, since the drug is not currently marketed there
- Review of the several clinical trials and literature items still marked "pending" relevance classification to finalize the evidence grade
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

