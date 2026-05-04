---
layout: default
title: Aztreonam
parent: 僅模型預測 (L5)
nav_order: 86
evidence_level: L5
indication_count: 10
---

# Aztreonam
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

# Aztreonam: From Gram-Negative Bacterial Infections to Gonococcal Urethritis

## One-Sentence Summary

Aztreonam is a monobactam β-lactam antibiotic with a narrow spectrum exclusively targeting gram-negative bacteria, originally used for serious infections including urinary tract infections, lower respiratory tract infections, septicemia, and intra-abdominal infections.
Among 10 TxGNN-predicted new indications evaluated in this multi-indication report, **gonococcal urethritis** emerges as the sole clinically actionable prediction, supported by **1 completed Phase 2/3 clinical trial** (NCT03867734) and **8 publications** — the remaining 9 predictions are currently rated Hold due to absent evidence or fundamental mechanistic contradictions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Serious gram-negative bacterial infections (UTI, lower respiratory tract, septicemia, intra-abdominal, skin/soft tissue) |
| Top TxGNN-Scored Prediction | Hyperamylasemia (Score 99.73%, Rank #5294) |
| Primary Actionable Prediction | Gonococcal urethritis (Score 99.59%, Rank #7243) |
| Evidence Level | L2 — gonococcal urethritis (1 Phase 2/3 trial + 8 publications) |
| India Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** (gonococcal urethritis only); **Hold** for all other 9 predictions |

---

## Prediction Landscape Summary (All 10 Indications)

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation | Key Issue |
|------|-----------|-------------|---------------|---------------|-----------|
| 1 | Hyperamylasemia | 99.73% | L5 | Hold | No trials or literature; indirect relevance only |
| 2 | Polyclonal hyperviscosity syndrome | 99.73% | L5 | Hold | Causal chain too indirect; no clinical basis |
| 3 | Congenital analbuminemia | 99.69% | L5 | Hold | Genetic disorder; no biological plausibility |
| 4 | Ureaplasma urethritis | 99.59% | L5 | Hold | ⚠️ **Fundamental mechanistic contradiction**: *Ureaplasma* lacks a cell wall; Aztreonam has no target |
| **5** | **Gonococcal urethritis** | **99.59%** | **L2** | **Proceed with Guardrails** | **1 Phase 2/3 trial + 8 publications; strongest evidence** |
| 6 | Blood group incompatibility | 99.59% | L5 | Hold | Immune mechanism; sole literature is a false association |
| 7 | Premalignant hematological disease | 99.54% | L5 | Hold | Clonal disorder; antibiotic has no disease-modifying role |
| 8 | Epiglottitis | 99.53% | L4 | Research Question | One 1986 paediatric case series; limited and non-specific |
| 9 | Monoclonal gammopathy | 99.50% | L4 | Hold | Sole literature addresses haematology patients with infections, not the disease itself |
| 10 | Xanthogranulomatous pyelonephritis (XGP) | 99.49% | L5 | Research Question | Biologically plausible but surgery-dominant; no comparative trial |

---

## Why is This Prediction Reasonable?

### Mechanism of Action

Detailed mechanism of action data for Aztreonam is not available from the Evidence Pack (Data Gap: DG002). Based on established pharmacological knowledge, Aztreonam is a monobactam antibiotic that selectively inhibits **Penicillin-Binding Protein 3 (PBP3)** of gram-negative bacteria, disrupting cell wall synthesis and leading to bacterial lysis. Its unique structural feature — a monocyclic β-lactam ring — confers minimal cross-reactivity with penicillins and cephalosporins, making it an important option for patients with severe β-lactam allergy.

### Link Between Original and Predicted Indication

*Neisseria gonorrhoeae* is a gram-negative diplococcus — precisely within Aztreonam's antibacterial spectrum. The biological rationale is direct: Aztreonam binds PBP3 of *N. gonorrhoeae*, inhibiting cell wall synthesis and exerting bactericidal activity. This is not an indirect extrapolation but a class-level mechanistic match.

### Clinical Urgency Strengthens the Case

The prediction gains further weight from a public health imperative. The CDC has designated antimicrobial-resistant *N. gonorrhoeae* as one of the nation's **top three urgent antimicrobial resistance threats**. Since the 1930s, gonococci have developed resistance to every first-line antibiotic in succession — sulfonamides, penicillin, tetracyclines, fluoroquinolones, and now with emerging resistance to third-generation cephalosporins (ceftriaxone). Aztreonam's status as a non-routinely-used agent means selective pressure for resistance has been minimal, making repurposing not only biologically rational but strategically valuable as a resistance-sparing alternative.

---

## Clinical Trial Evidence (Gonococcal Urethritis)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT03867734](https://clinicaltrials.gov/study/NCT03867734) | Phase 2/3 | Completed | 32 | Open-label demonstration study of Aztreonam for **pharyngeal gonorrhoea** — the most treatment-refractory site. Single-dose intramuscular Aztreonam 2 g evaluated in men. Pharyngeal gonorrhoea was the primary focus given historically poor eradication rates at this anatomic site. Completed September 2019. |

> **Note**: Pharyngeal gonorrhoea represents the highest unmet need among gonococcal infection sites; the choice of this endpoint reflects the greatest clinical challenge.

---

## Literature Evidence (Gonococcal Urethritis)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Open-label Clinical Trial | *Antimicrobial Agents and Chemotherapy* | Single-arm trial of single-dose IM Aztreonam 2 g (Apr–Sep 2019); evaluated eradication of *N. gonorrhoeae* including pharyngeal infections; confirmed efficacy against modern strains. Core contemporary evidence. |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Microbiological Surveillance | *J Infect Chemother* | Emergence of high-level cephem- and Aztreonam-resistant *N. gonorrhoeae* without β-lactamase production in Japan; important resistance signal requiring monitoring. |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Clinical Study | *Antimicrobial Agents and Chemotherapy* | Aztreonam 1 g IM vs. spectinomycin 2 g IM for uncomplicated gonorrhoea; no treatment failures in either arm (urethral n=26, rectal n=3, endocervical n=3); established single-dose efficacy. |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Clinical Study | *Genitourinary Medicine* | Aztreonam 1 g IM single dose cleared infection at all sites in 61 men and 26 women, except one pharyngeal case; effective against both penicillin-sensitive and resistant strains; well tolerated. |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | Clinical Study | *J Infectious Diseases* | Early demonstration of Aztreonam efficacy against penicillinase-producing *N. gonorrhoeae* (PPNG) at a time when treatment options were scarce; established foundational evidence. |
| [6438364](https://pubmed.ncbi.nlm.nih.gov/6438364/) | 1984 | Bacteriological & Clinical Evaluation | *Jpn J Antibiotics* | 30 male patients with gonococcal urethritis; 61 strains tested (15% PPNG); bacteriological and clinical outcomes reported; documented activity against both PPNG and non-PPNG strains. |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Epidemiological/Therapeutic Study | *Acta Urologica Japonica* | One-shot Aztreonam therapy in gonococcal infections; 244 clinical strains assessed, 17.2% PPNG; epidemiological analysis of patient demographics and outcomes. |
| [6226596](https://pubmed.ncbi.nlm.nih.gov/6226596/) | 1983 | Clinical Study | *Giornale Italiano di Dermatologia* | Early Italian clinical study of Aztreonam in acute gonococcal urethritis; confirms early European clinical experience. |

---

## India Market Information

Aztreonam is currently **not marketed in India**. No drug registrations are on file.

> This represents both a regulatory challenge and an opportunity: if evidence for gonococcal urethritis repurposing proceeds, a new drug application pathway will be required. The absence of existing market presence eliminates concerns about label confusion but requires a full regulatory submission.

---

## Safety Considerations

Detailed product warnings and contraindications are not available from the Evidence Pack (Data Gap: DG001). Please refer to the originator package insert for complete safety information.

**Drug Interactions (27 interactions identified via DDInter):**

Clinically notable interactions include:

| Interacting Drug | Interaction Level | Clinical Relevance |
|----------------|------------------|--------------------|
| Warfarin | **Moderate** | Monitor INR; Aztreonam may potentiate anticoagulant effect |
| Dicoumarol | **Moderate** | Same mechanism as Warfarin interaction; monitor closely |
| Picosulfuric acid | **Moderate** | Monitor for additive effects; clinical significance uncertain |

The remaining 24 interactions are classified as **Unknown** severity. Drugs involved include Vancomycin, Fluconazole, Tacrolimus, Metronidazole, Amikacin, Amphotericin B, Dexamethasone, Hydrocortisone, Ondansetron, Morphine, and others commonly co-administered in hospital settings. The Unknown classification reflects insufficient interaction data rather than confirmed safety, and clinicians should exercise standard monitoring in complex regimens.

---

## Conclusion and Next Steps

### Decision: **Proceed with Guardrails** (Gonococcal Urethritis)

**Rationale:**
Gonococcal urethritis is the only indication among 10 TxGNN predictions with actionable clinical evidence: a completed Phase 2/3 trial (NCT03867734) and 8 publications spanning 1983–2020 collectively demonstrate efficacy of single-dose IM Aztreonam against *N. gonorrhoeae*, including modern strains and the clinically challenging pharyngeal site. The biological rationale is unambiguous (gram-negative cell wall target), and the public health urgency of multidrug-resistant gonorrhoea provides strong motivation for development.

### Decision: **Hold** (All Other 9 Indications)

**Rationale:**
The top TxGNN-ranked indication (hyperamylasemia, score 99.73%) and 8 of the remaining predictions lack any supporting clinical evidence. Critically, Ureaplasma urethritis (rank #4, score 99.59%) contains a **fundamental mechanistic contradiction** — *Ureaplasma* organisms have no cell wall and are intrinsically resistant to all β-lactam antibiotics including Aztreonam — demonstrating a known limitation of graph-neural-network predictions that do not encode mechanism-level constraints.

---

**To proceed with gonococcal urethritis repurposing, the following is needed:**

- **Safety data**: Retrieve and review the full package insert (warnings, contraindications) from the originator label to complete the S1 safety screening (Data Gap DG001 — Blocking)
- **MOA confirmation**: Formally document Aztreonam PBP3-binding mechanism via DrugBank API query (Data Gap DG002)
- **NCT03867734 full results**: Obtain published or grey-literature results from the 2019 pharyngeal gonorrhoea trial; the PMID 33077658 publication likely constitutes these results but cross-verification is needed
- **Resistance monitoring**: Evaluate current local *N. gonorrhoeae* susceptibility data for Aztreonam (reference: PMID 11406757 documents high-level resistance emergence in Japan)
- **Regulatory pathway**: Consult CDSCO on the pathway for a new indication registration given zero existing India market presence
- **Formulation assessment**: Confirm intramuscular formulation availability and supply chain, as all efficacy data use IM administration (1–2 g single dose)

---

> ⚠️ **YMYL Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. All predictions are generated by computational models (TxGNN) and must be interpreted in the context of established clinical pharmacology and regulatory requirements.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

