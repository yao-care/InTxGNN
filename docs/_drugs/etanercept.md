---
layout: default
title: Etanercept
parent: 僅模型預測 (L5)
nav_order: 301
evidence_level: L5
indication_count: 6
---

# Etanercept
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

# Etanercept: From Rheumatoid Arthritis to Rheumatoid Vasculitis

## One-Sentence Summary

Etanercept is a soluble TNF-α receptor fusion protein (p75-Fc dimeric protein) approved globally for rheumatoid arthritis, psoriatic arthritis, ankylosing spondylitis, and related autoimmune inflammatory conditions — though it is not currently registered in India.
The TxGNN model predicts it may be effective for **Rheumatoid Vasculitis**, with **6 clinical trials** and **20 publications** currently supporting this direction — however, the evidence carries a critical paradoxical signal: Etanercept has itself been documented to *induce* drug-related vasculitis in some patients, making this a complex repurposing scenario requiring careful interpretation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis and related inflammatory autoimmune diseases (globally approved; not registered in India) |
| Predicted New Indication | Rheumatoid Vasculitis |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L3 |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, Etanercept is a dimeric fusion protein composed of two p75 (type II) TNF receptor domains linked to the Fc portion of human IgG1. It binds both soluble and membrane-bound TNF-α (and TNF-β/lymphotoxin), preventing interaction with cell-surface receptors and thereby suppressing downstream inflammatory signalling cascades — including NF-κB activation, cytokine production, and endothelial cell activation.

Rheumatoid vasculitis (RV) is one of the most severe extra-articular manifestations of long-standing rheumatoid arthritis, characterised by necrotising inflammation of small and medium blood vessels. TNF-α is a key mediator in the vascular wall inflammatory process, making TNF blockade a mechanistically plausible intervention. The 2021 systematic review (PMID 33058033) confirms that biological agents — including TNF inhibitors — have been incorporated into the therapeutic armamentarium for RV alongside corticosteroids and conventional immunosuppressants.

However, a critical paradox complicates this prediction: multiple published case series and cohort studies (PMID 15853915, PMID 12209493, PMID 11792895, PMID 28123776) document that Etanercept can itself *paradoxically induce* cutaneous and systemic vasculitis via immune complex deposition, complement activation, and B-cell hyperactivation. Furthermore, the most directly relevant interventional trial (NCT00001901) tested Etanercept in Wegener's granulomatosis (ANCA-associated vasculitis), and the subsequent larger WGET trial found no benefit. This dual signal — potential therapeutic use versus drug-induced adverse vasculitis — necessitates careful mechanistic distinction between RA-associated RV and drug-induced vasculitis before any repurposing strategy proceeds.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Phase 2 | Completed | 60 | Most directly relevant interventional trial — tested Etanercept (TNFR:Fc) in Wegener's granulomatosis (ANCA-associated vasculitis). Standard treatment involved prednisone plus cytotoxic agents. Subsequent larger WGET trial did not support routine use in ANCA vasculitis; indirect evidence only for RA-associated RV |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | Completed | 808 | Observational cross-sectional study of biological DMARD treatment patterns in RA patients in China; vasculitis was not a primary endpoint — low direct relevance |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | Completed | 184 | Non-interventional observational study of tocilizumab in RA patients inadequately responding to DMARDs or one biologic; evaluates 6-month treatment outcomes in general RA population, not vasculitis-specific |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large pharmacoepidemiology safety study on risk of incident immune-mediated inflammatory diseases in patients treated with biologics/immunosuppressants; provides risk signal data for drug-induced IMID but not therapeutic efficacy |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | N/A | Completed | 1,754 | Real-world study comparing moderate RA patients newly started on Etanercept vs. non-biologic therapy using BSRB Register data; vasculitis not a primary endpoint |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Assesses immunosuppressant management timing around elective shoulder arthroplasty in rheumatology patients; perioperative drug management focus, not vasculitis treatment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | PRISMA systematic review on biological drugs in rheumatoid vasculitis treatment; documents therapeutic evidence for TNF inhibitors in RV including corticosteroid/immunosuppressant refractory cases |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Review | Nephrology Dialysis Transplantation | Reviews mechanistic evidence for TNF-α role in ANCA-associated vasculitis pathophysiology; analyses results from clinical trials of TNFα blockade in AAV — findings largely do not support routine use |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort | RMD Open | BSRBR-RA data comparing drug-specific risk of vasculitis-like events in TNFi-treated vs. nbDMARD-treated RA patients; quantifies risk differential across TNF inhibitor agents |
| [31668853](https://pubmed.ncbi.nlm.nih.gov/31668853/) | 2019 | Comparative Study | Biologicals | Real-world national cohort comparing efficacy and safety of biosimilar etanercept (SB4) vs. originator etanercept in active RA; confirms comparable therapeutic profiles |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Case Series | Scandinavian Journal of Immunology | Immunological analysis of cutaneous vasculitis associated with both etanercept and infliximab; proposes mechanism of drug-induced vasculitis via immune complex deposition and complement activation |
| [25544845](https://pubmed.ncbi.nlm.nih.gov/25544845/) | 2014 | Case Report | Case Reports in Medicine | Large vessel vasculitis arising in an RA patient under anti-TNF therapy; demonstrates biologics-induced vasculitis risk in the same patient population |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Case Report | Arthritis and Rheumatism | Early documentation of accelerated nodulosis and vasculitis following etanercept therapy in RA; establishes paradoxical adverse vasculitis signal |
| [11792895](https://pubmed.ncbi.nlm.nih.gov/11792895/) | 2002 | Case Series | Rheumatology (Oxford) | Multiple cases of cutaneous vasculitis associated with both etanercept and infliximab use; corroborates class-level paradoxical vasculitis risk |
| [15801034](https://pubmed.ncbi.nlm.nih.gov/15801034/) | 2005 | Case Report | Journal of Rheumatology | Proliferative lupus nephritis and leukocytoclastic vasculitis during etanercept treatment; serious overlapping adverse drug reaction illustrating autoimmune induction risk |
| [15468348](https://pubmed.ncbi.nlm.nih.gov/15468348/) | 2004 | Review | Journal of Rheumatology | Mechanistic discussion of TNF-α blockade and risk of vasculitis induction; analyses why TNF inhibitors may paradoxically trigger rather than suppress vasculitis in select patients |

---

## India Market Information

Etanercept currently has **no regulatory registrations** in India. There are no authorisation numbers, approved product names, dosage forms, or approved indications on record in the India regulatory database.

---

## Safety Considerations

**Drug Interactions (352 total interactions on record):**

*Major interactions — requires clinical co-administration review:*
- **Corticosteroids** (Hydrocortisone, Dexamethasone, Betamethasone, Budesonide, Triamcinolone, Triamcinolone ophthalmic, Prednisolone, Prednisone): Combined immunosuppression substantially elevates the risk of serious infections, including opportunistic infections and tuberculosis reactivation
- **Deferiprone**: Risk of agranulocytosis potentiation; concurrent use generally contraindicated
- **Radioimmunotherapy agents** (Iobenguane I-131, Ibritumomab tiuxetan, Tositumomab I-131, Tositumomab): Immunosuppression may interfere with radioimmunotherapy efficacy and increase haematological toxicity

*Moderate interactions — monitor closely:*
- **Statins** (Rosuvastatin, Simvastatin): Moderate pharmacodynamic or pharmacokinetic interaction
- **Nitroimidazoles** (Metronidazole, Tinidazole): Moderate interaction

*Minor interactions:*
- **Zinc salts** (Zinc sulfate, Zinc acetate, Zinc gluconate): Minor interaction, unlikely to require dose adjustment

> For complete warnings and contraindications (TFDA/FDA package insert data not yet retrieved), please refer to the official prescribing information. This represents a Blocking data gap (DG001) that must be resolved before safety evaluation can be finalised.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While TNF-α blockade is mechanistically plausible for rheumatoid vasculitis given TNF-α's established role in vascular wall inflammation, the available evidence presents a paradoxical and contradictory signal — Etanercept has been documented to *induce* vasculitis as an adverse effect through immune complex deposition and B-cell hyperactivation, and the only directly relevant interventional trial (Phase 2 in Wegener's granulomatosis) was followed by a larger trial yielding negative results. The evidence level of L3 (observational and systematic review data) without a completed RCT in rheumatoid vasculitis specifically does not support advancement to the next development stage without first resolving the mechanistic ambiguity.

**To proceed, the following is needed:**
- Retrieve package insert warnings and contraindications from the regulatory authority (Blocking gap DG001) to complete the safety evaluation
- Obtain DrugBank MOA data (High severity gap DG002) to confirm molecular targets relevant to RV pathophysiology versus ANCA-associated vasculitis
- Commission a focused literature analysis distinguishing *therapeutic use in RV* from *drug-induced vasculitis as adverse event* — these currently conflate in the evidence base
- Define patient selection biomarkers (e.g., ANA, anti-dsDNA, immunoglobulin levels, ANCA status) to stratify RA-RV patients at benefit vs. paradoxical harm risk
- Evaluate feasibility of a prospective observational registry study for RA patients with concurrent vasculitis manifestations, prior to any interventional trial design
- Conduct India-specific regulatory assessment: if future evidence supports advancement, initiation of a pre-submission meeting with CDSCO would be required given zero existing registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

