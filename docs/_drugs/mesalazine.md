---
layout: default
title: Mesalazine
parent: 僅模型預測 (L5)
nav_order: 326
evidence_level: L5
indication_count: 7
---

# Mesalazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Mesalazine: From Ulcerative Colitis to Rheumatoid Arthritis

## One-Sentence Summary

Mesalazine (5-aminosalicylic acid, 5-ASA) is the pharmacologically active metabolite of sulfasalazine, primarily established as a first-line therapy for ulcerative colitis and inflammatory bowel disease.
The TxGNN model predicts it may have therapeutic utility in **Rheumatoid Arthritis (RA)** — a disease for which its parent compound sulfasalazine was originally designed in the 1940s — with **6 clinical trials** and **20 publications** currently supporting this research direction.
Notably, however, the dominant body of historical evidence suggests sulfapyridine (not mesalazine) is the primary DMARD-active moiety in sulfasalazine, making this repurposing hypothesis mechanistically plausible but requiring direct clinical validation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ulcerative colitis / Inflammatory bowel disease |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Mesalazine is not formally available in this evidence pack. Based on known pharmacology, Mesalazine (5-ASA) is a salicylate-based anti-inflammatory agent that suppresses mucosal and systemic inflammation through multiple mechanisms: inhibition of the NF-κB signaling pathway (reducing TNF-α and IL-1β transcription), suppression of both COX and LOX branches of the arachidonic acid cascade (lowering PGE2 and LTB4 levels), and agonism of PPARγ (promoting resolution of inflammation and protection of extracellular matrix-producing cells). These are among the most conserved pathways in chronic inflammatory diseases.

The connection to rheumatoid arthritis is historically grounded. Sulfasalazine — the prodrug from which mesalazine is released by colonic bacterial azoreductases — was explicitly designed in the 1940s to treat rheumatoid polyarthritis, and only later found to be highly effective in IBD. Sulfasalazine remains a recognized DMARD for RA in international treatment guidelines today. Since mesalazine is a direct metabolite of sulfasalazine, and shares the NF-κB / COX-LOX anti-inflammatory axis relevant to synovial inflammation, the TxGNN model's prediction of RA efficacy is pharmacologically coherent.

A critical nuance must be acknowledged: multiple clinical comparative studies (PMID 2860942, 1985; PMID 2877851, 1986; PMID 8535642, 1995) systematically investigated whether 5-ASA or sulfapyridine carries the antirheumatic activity in sulfasalazine, and the prevailing consensus favors **sulfapyridine** as the dominant DMARD-active component. In these trials, 5-ASA monotherapy demonstrated only a weak first-line anti-inflammatory effect in RA, significantly less than intact sulfasalazine. That said, in vitro evidence published in 2000 (PMID 10743803) shows that 5-ASA does modulate mRNA expression of IL-1β, TNF-α, and matrix metalloproteinases (MMP-1, MMP-3) in rheumatoid synovial fibroblasts — suggesting a direct mechanistic role at the tissue level that may not have been fully captured by systemic efficacy trials using standard oral dosing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02930343](https://clinicaltrials.gov/study/NCT02930343) | Phase 3 | Terminated | 136 | Sulfasalazine vs. leflunomide-based combination DMARD therapy in RA patients failing MTX monotherapy; provides the most directly relevant class-level evidence, though study was terminated before completing primary endpoint |
| [NCT00637780](https://clinicaltrials.gov/study/NCT00637780) | Phase 4 | Terminated | 2 | Steady-state pharmacokinetics of sulfasalazine delayed-release tablets in pediatric Juvenile Idiopathic Arthritis; very limited scientific value due to near-zero enrollment |
| [NCT05580861](https://clinicaltrials.gov/study/NCT05580861) | Phase 1/2 | Recruiting | 64 | Sulfasalazine combined with standard AML induction therapy in patients ≥60; the mechanism here is xCT inhibition by intact sulfasalazine — not applicable to mesalazine (5-ASA does not inhibit xCT) |
| [NCT06201793](https://clinicaltrials.gov/study/NCT06201793) | Phase 2 | Completed | 46 | Minocycline as adjunct to mesalamine in ulcerative colitis; study subject is minocycline, mesalamine is background therapy only — not applicable to RA repurposing |
| [NCT03591770](https://clinicaltrials.gov/study/NCT03591770) | Phase 4 | Terminated | 15 | Shingrix vaccine immunogenicity and safety in UC patients on tofacitinib; not relevant to RA repurposing, terminated early |
| [NCT00514982](https://clinicaltrials.gov/study/NCT00514982) | Phase 2 | Withdrawn | 0 | IBD therapy in Hermansky-Pudlak syndrome-associated colitis; withdrawn before any enrollment, no usable data |

> **Note:** No clinical trials directly studying Mesalazine (5-ASA) monotherapy in rheumatoid arthritis were identified. All arthritis-relevant trials test the parent compound sulfasalazine.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7588084](https://pubmed.ncbi.nlm.nih.gov/7588084/) | 1995 | Systematic Review | Drugs | Comprehensive pharmacology and efficacy review of sulfasalazine as an established DMARD in RA; notes ongoing uncertainty regarding whether SP or 5-ASA carries the antirheumatic activity |
| [2899645](https://pubmed.ncbi.nlm.nih.gov/2899645/) | 1988 | Prospective Clinical Study | J Rheumatol | 12-week sulfasalazine treatment normalizes elevated activated lymphocytes and aberrant mitogen response in RA patients; in vitro lymphocyte inhibition study clarifies immunomodulatory mechanism |
| [2860942](https://pubmed.ncbi.nlm.nih.gov/2860942/) | 1985 | Clinical Comparative Study | BMJ (Clin Res Ed) | Landmark study: sulphapyridine showed pronounced second-line DMARD effect in RA over 24 weeks; 5-aminosalicylic acid showed only a weak first-line effect — primary evidence questioning mesalazine as the active RA moiety |
| [2877851](https://pubmed.ncbi.nlm.nih.gov/2877851/) | 1986 | Clinical Comparative Study | Drugs | 30 active RA patients randomized to 5-ASA or sulphapyridine monotherapy for 6 months; sulphapyridine group showed significant improvement across clinical and biochemical parameters; 5-ASA group did not improve despite adequate plasma concentrations |
| [8535642](https://pubmed.ncbi.nlm.nih.gov/8535642/) | 1995 | Review | Br J Rheumatol | Synthesizes evidence that sulphapyridine (not 5-ASA) is the primary antirheumatic moiety; notes ~30% of intact sulfasalazine absorbed unaltered may independently contribute |
| [10743803](https://pubmed.ncbi.nlm.nih.gov/10743803/) | 2000 | In Vitro Mechanistic Study | J Rheumatol | 5-ASA modulates steady-state mRNA of IL-1β, TNF-α, MMP-1, MMP-3, MMP-2 and TIMP in rheumatoid synovial fibroblasts — provides direct molecular evidence that mesalazine acts on RA-relevant tissue targets |
| [17708602](https://pubmed.ncbi.nlm.nih.gov/17708602/) | 2007 | Review | World J Gastroenterol | Historical account documenting that sulfasalazine was originally designed to treat rheumatoid arthritis in the 1940s; pivotal context for understanding the RA–mesalazine connection |
| [12235076](https://pubmed.ncbi.nlm.nih.gov/12235076/) | 2002 | Pharmacovigilance Study | Gut | Analysis of serious adverse reaction reports for sulfasalazine and mesalazine submitted to the UK Committee on Safety of Medicines; characterizes the comparative safety profiles of both compounds |
| [41443863](https://pubmed.ncbi.nlm.nih.gov/41443863/) | 2025 | Case Report | Intern Med (Tokyo) | Important safety signal: mesalazine-induced colitis in a 76-year-old RA patient without prior IBD history who received sulfasalazine then mesalazine for RA; drug-induced lymphocyte stimulation test confirmed mesalazine hypersensitivity — paradoxical colitis risk in RA setting |
| [16885699](https://pubmed.ncbi.nlm.nih.gov/16885699/) | 2006 | Review | J Clin Gastroenterol | Reviews mesalazine metabolism and pharmacokinetics; confirms sulfasalazine was initially developed for RA and that several 5-ASA formulations were created to avoid the sulfapyridine-related side effects of sulfasalazine |

---

## Safety Considerations

**Drug Interactions** (291 total interactions identified via DDInter):

*Major interactions requiring close monitoring:*
- **Cidofovir** (Major): Risk of additive nephrotoxicity; avoid concurrent use
- **Human Botulinum Neurotoxin A/B Immune Globulin** (Major): Requires careful monitoring if co-administered

*Clinically significant moderate interactions:*
- **NSAIDs** (Ketorolac, Ibuprofen, Celecoxib, Bromfenac): Combination may increase gastrointestinal and renal adverse effects — particularly relevant in RA, where NSAIDs are frequently co-prescribed
- **Azathioprine**: Commonly co-used in IBD and RA; mesalazine may inhibit thiopurine methyltransferase (TPMT), increasing azathioprine toxicity risk
- **Nephrotoxic antibiotics** (Amikacin, Amikacin liposome, Capreomycin, Bacitracin, Amphotericin B and its formulations): Additive renal toxicity risk
- **Antidiabetics** (Acetohexamide, Chlorpropamide): Moderate interaction, monitor glycemic control
- **Anticoagulants** (Anisindione): Potential for altered anticoagulation effect
- **Cisplatin** (Moderate): Additive nephrotoxicity concern
- **Acyclovir** (Moderate): Renal clearance interaction

Please refer to the complete package insert for full warnings and contraindications, as detailed labeling data was not available for this review.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Sulfasalazine — the prodrug from which mesalazine is derived — is an established RA DMARD with decades of clinical use, providing strong historical and mechanistic grounding for this repurposing hypothesis. In vitro evidence confirms that mesalazine (5-ASA) directly modulates RA-relevant synovial tissue targets (cytokines, MMPs) via NF-κB and COX/LOX pathways. However, the critical limitation is that clinical comparative trials have consistently shown sulfapyridine — not 5-ASA — to be the dominant antirheumatic moiety in sulfasalazine, meaning mesalazine monotherapy in RA remains an untested hypothesis requiring purpose-designed clinical evidence.

**To proceed, the following is needed:**
- Obtain full mechanism of action (MOA) documentation from DrugBank API (data gap DG002)
- Obtain India/regional regulatory labeling (package insert) for complete warnings and contraindications (data gap DG001)
- Design a dedicated Phase 2 pilot trial of oral mesalazine monotherapy in early or mild-to-moderate RA, with PK/PD endpoints establishing achievable systemic 5-ASA concentrations
- Conduct pharmacokinetic modeling to determine whether oral mesalazine can achieve synovial tissue concentrations sufficient for the anti-inflammatory effects demonstrated in vitro
- Assess TPMT genotype and azathioprine co-medication status in any RA patient population enrolled, given the DDI signal
- Monitor for the paradoxical risk of mesalazine-induced colitis, as documented in the 2025 case report (PMID 41443863) in RA patients
- Explore whether a systemic (non-enteric-coated) formulation would improve bioavailability and mechanistic reach beyond the colonic mucosa
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

